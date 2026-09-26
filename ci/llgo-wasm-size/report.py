#!/usr/bin/env python3
"""Turn one Go/TinyGo/LLGo WASM build round into publishable results."""

from __future__ import annotations

import csv
import json
import math
import os
import re
import shlex
import sys
from datetime import datetime, timezone
from pathlib import Path


# Shared with run.sh via --configs; flags are passed as separate TSV fields.
PROTOCOL = {
    "Go": ["build", "-trimpath", "-ldflags=-s -w"],
    "TinyGo": ["build", "-opt=z", "-no-debug"],
    "LLGoNoLTO": ["build", "-a", "-Oz"],
    "LLGoDeadcodeDrop": ["build", "-a", "-Oz", "-deadcodedrop"],
    "LLGoFullLTONoGlobalDCE": ["build", "-a", "-Oz", "-lto=full", "-globaldce=false"],
    "LLGoFullLTOGlobalDCE": ["build", "-a", "-Oz", "-lto=full", "-globaldce=true"],
}
# LLGo main's WASI external-clang path needs explicit LTO flags. Keep them
# visible in the published protocol. -a prevents reuse of archives created
# with different ambient CCFLAGS (not yet part of LLGo's cache fingerprint).
ENVIRONMENT = {
    "LLGoFullLTONoGlobalDCE": {"CCFLAGS": "-flto=full", "LDFLAGS": "-Wl,--lto-O2"},
    "LLGoFullLTOGlobalDCE": {
        "CCFLAGS": "-flto=full -fvirtual-function-elimination -fwhole-program-vtables",
        "LDFLAGS": "-Wl,--lto-O2",
    },
}
CONFIGS = list(PROTOCOL)
LLGO_CONFIGS = CONFIGS[2:]
LABELS = dict(zip(CONFIGS, ["Go", "TinyGo", "LLGo · no LTO", "LLGo · deadcode drop",
                          "LLGo · full LTO (GlobalDCE off)", "LLGo · full LTO + GlobalDCE"]))

APP_ID = re.compile(r"[a-z0-9][a-z0-9-]*")


def read_manifest(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as source:
        rows = list(csv.DictReader(source, delimiter="\t"))
    expected = {"id", "command", "source", "provenance", "kind", "description", "tinygo", "repository", "revision", "go_version"}
    if not rows or set(rows[0]) not in (expected, expected | {"goos"}):
        raise ValueError(f"{path}: expected columns {sorted(expected)}")
    seen: set[str] = set()
    for row in rows:
        row.setdefault("goos", "wasip1")
        if row["goos"] not in {"wasip1", "js"}:
            raise ValueError(f"{path}: unsupported WASM host")
        app_id = row["id"]
        if not APP_ID.fullmatch(app_id) or app_id in seen:
            raise ValueError(f"{path}: invalid or duplicate app id {app_id!r}")
        if not all(row[field] for field in expected):
            raise ValueError(f"{path}: empty field in app {app_id!r}")
        if row["tinygo"] not in {"required", "optional"}:
            raise ValueError(f"{path}: invalid TinyGo policy for {app_id!r}")
        if row["repository"] == "-":
            if row["revision"] != "-":
                raise ValueError(f"{path}: local app cannot have an external revision")
        elif not re.fullmatch(r"https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+\.git", row["repository"]) or not re.fullmatch(r"[0-9a-f]{40}", row["revision"]):
            raise ValueError(f"{path}: external app requires a repository URL and full commit SHA")
        if row["go_version"] != "default" and not re.fullmatch(r"1\.\d+\.\d+", row["go_version"]):
            raise ValueError(f"{path}: invalid Go version")
        if Path(row["source"]).is_absolute() or ".." in Path(row["source"]).parts or "\\" in row["source"]:
            raise ValueError(f"{path}: entry must stay inside its source root")
        seen.add(app_id)
    return rows


def read_sizes(path: Path) -> dict[str, dict]:
    with path.open(newline="", encoding="utf-8") as source:
        rows = list(csv.DictReader(source, delimiter="\t"))
    expected = {"app", "config", "bytes", "status"}
    if not rows or set(rows[0]) != expected:
        raise ValueError(f"{path}: expected columns {sorted(expected)}")
    sizes: dict[str, dict] = {}
    for row in rows:
        app_id, config, status = row["app"], row["config"], row["status"]
        results = sizes.setdefault(app_id, {})
        if config not in CONFIGS or config in results:
            raise ValueError(f"{path}: unknown or duplicate config {config!r} for {app_id!r}")
        value = None if row["bytes"] == "null" else int(row["bytes"])
        if status not in {"success", "failed", "timeout"} or (status == "success") != (value is not None):
            raise ValueError(f"{path}: inconsistent status/size for {app_id!r}/{config}")
        if value is not None and value <= 0:
            raise ValueError(f"{path}: non-positive size for {app_id!r}/{config}")
        results[config] = {"bytes": value, "status": status}
    return sizes


def comparisons(benchmarks: list[dict]) -> dict:
    result = {}
    for baseline in ("Go", "TinyGo"):
        result[baseline] = {}
        for config in LLGO_CONFIGS:
            ratios = [row["values"][config] / row["values"][baseline] for row in benchmarks
                      if row["values"][config] and row["values"][baseline]]
            result[baseline][config] = {
                "ratio": math.exp(sum(map(math.log, ratios)) / len(ratios)) if ratios else None,
                "samples": len(ratios),
            }
    return result


def env_number(name: str) -> int | None:
    try:
        return int(os.environ.get(name, ""))
    except ValueError:
        return None


def workflow_url(repository: str, run_id: str) -> str:
    explicit = os.environ.get("LLGO_WASM_WORKFLOW_URL", "")
    if explicit:
        return explicit
    if repository and run_id:
        return f"https://github.com/{repository}/actions/runs/{run_id}"
    return ""


def build_document(manifest: list[dict[str, str]], sizes: dict[str, dict]) -> dict:
    manifest_ids = {row["id"] for row in manifest}
    if set(sizes) != manifest_ids:
        missing = sorted(manifest_ids - set(sizes))
        extra = sorted(set(sizes) - manifest_ids)
        raise ValueError(f"size rows do not match app manifest; missing={missing}, extra={extra}")

    benchmarks = []
    for app in manifest:
        results = sizes[app["id"]]
        if set(results) != set(CONFIGS):
            raise ValueError(f"incomplete configuration set for {app['id']!r}")
        for config, result in results.items():
            value, status = result["bytes"], result["status"]
            if status == "success" and type(value) is int and value > 0:
                continue
            if status in {"failed", "timeout"} and value is None:
                continue
            raise ValueError(f"invalid build result: {app['id']}/{config}")
        benchmarks.append({
            "id": app["id"],
            "command": app["command"],
            "source": app["source"],
            "provenance": app["provenance"],
            "kind": app["kind"],
            "description": app["description"],
            "tinygo": app["tinygo"],
            "target": {"goos": app.get("goos", "wasip1"), "goarch": "wasm"},
            "repository": app.get("repository", "-"),
            "revision": app.get("revision", "-"),
            "goVersion": os.environ.get("GO_VERSION", "") if app.get("go_version", "default") == "default" else app["go_version"],
            "values": {config: results[config]["bytes"] for config in CONFIGS},
            "builds": {config: {"status": results[config]["status"],
                                "log": f"logs/{app['id']}.{config}.log"} for config in CONFIGS},
        })

    repository = os.environ.get("GITHUB_REPOSITORY", "")
    run_id = os.environ.get("GITHUB_RUN_ID", "")
    run = {
        "id": run_id or "manual",
        "attempt": env_number("GITHUB_RUN_ATTEMPT"),
        "number": env_number("GITHUB_RUN_NUMBER"),
        "createdAt": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "repository": repository,
        "sourceCommit": os.environ.get("GITHUB_SHA", ""),
        "ref": os.environ.get("GITHUB_REF_NAME", ""),
        "llgoRepository": os.environ.get("LLGO_REPOSITORY", ""),
        "llgoCommit": os.environ.get("LLGO_COMMIT", ""),
        "llgoMainIndex": env_number("LLGO_MAIN_INDEX"),
        "llgoCommittedAt": os.environ.get("LLGO_COMMITTED_AT", ""),
        "llgoBuildGoVersion": os.environ.get("LLGO_BUILD_GO_VERSION", ""),
        "goVersion": os.environ.get("GO_VERSION", ""),
        "llvmVersion": os.environ.get("LLVM_VERSION", ""),
        "tinygoVersion": os.environ.get("TINYGO_VERSION", ""),
        "binaryenVersion": os.environ.get("BINARYEN_VERSION", ""),
        "event": os.environ.get("GITHUB_EVENT_NAME", ""),
        "workflowUrl": workflow_url(repository, run_id),
        "runnerOS": os.environ.get("RUNNER_OS", ""),
        "runnerArch": os.environ.get("RUNNER_ARCH", ""),
        "runnerImage": os.environ.get("ImageOS", ""),
    }
    return {
        "schemaVersion": 2,
        "format": "wasm-file-size",
        "run": run,
        "target": {"goos": "wasip1" if all(app.get("goos", "wasip1") == "wasip1" for app in manifest) else "per-application", "goarch": "wasm"},
        "configs": CONFIGS,
        "configLabels": LABELS,
        "comparisons": comparisons(benchmarks),
        "comparisonsByTarget": {target: comparisons([row for row in benchmarks if row["target"]["goos"] == target])
                                for target in sorted({row["target"]["goos"] for row in benchmarks})},
        "metric": "total-bytes",
        "protocol": {
            **PROTOCOL,
            "LLGoPostLink": ["Emscripten wasm-opt", "Upstream target-specific post-link processing"],
            "LLGoPostLinkByTarget": {
                "wasip1": "LLGo pre-Asyncify optimization, Asyncify and standardized exception translation",
                "js": "Upstream Emscripten driver; its Binaryen optimization level is not overridden by this benchmark",
            },
            "sameGoToolchain": len({app["goVersion"] for app in benchmarks}) == 1,
            "sameGoToolchainPerApplication": True,
            "modulePolicy": "GOFLAGS=-mod=readonly -p=1, GO111MODULE=on, GOWORK=off; no module rewrites",
            "sourcePolicy": "Download pinned upstream commits and build original entries with unchanged modules",
            "environment": {config: {"CCFLAGS": "", "LDFLAGS": "", "CFLAGS": "", **ENVIRONMENT.get(config, {})}
                            for config in CONFIGS},
            "resources": {"parallelBuilds": 1, "GOMAXPROCS": os.environ.get("GOMAXPROCS", "2"),
                          "BINARYEN_CORES": os.environ.get("BINARYEN_CORES", "2"),
                          "GOFLAGS": "-mod=readonly -p=1",
                          "buildTimeoutSeconds": float(os.environ.get("WASM_BUILD_TIMEOUT_SECONDS", "1200"))},
            "sizeScope": "Final .wasm only; JS host glue is retained in the CI artifact and excluded from size",
            "cachePolicy": "LLGo -a rebuilds all packages so ambient flag changes cannot reuse stale archives",
        },
        "toolVersions": {
            "Go": os.environ.get("GO_ACTUAL_VERSION", ""),
            "TinyGo": os.environ.get("TINYGO_ACTUAL_VERSION", ""),
            "LLGo": os.environ.get("LLGO_ACTUAL_VERSION", ""),
            "Clang": os.environ.get("CLANG_ACTUAL_VERSION", ""),
            "Wasm linker": os.environ.get("WASM_LD_ACTUAL_VERSION", ""),
            "TinyGo wasm-opt": os.environ.get("TINYGO_WASM_OPT_ACTUAL_VERSION", ""),
            "LLGo wasm-opt": os.environ.get("LLGO_WASM_OPT_ACTUAL_VERSION", ""),
        },
        "benchmarks": benchmarks,
        "native": {
            "summary": "summary.md",
            "tsv": "sizes.tsv",
            "binaryDir": "raw",
        },
    }


def write_summary(document: dict, path: Path) -> None:
    lines = ["# WASM binary size", "", "Per-application WASM host (wasip1 or js); smaller is better. JS glue is excluded.",
             "Each application uses the same pinned Go toolchain across compilers; per-application versions are recorded below.", ""]
    for config in CONFIGS:
        environment = " ".join(f"{key}={value!r}" for key, value in ENVIRONMENT.get(config, {}).items())
        lines.append(f"- {LABELS[config]}: `{environment + ' ' if environment else ''}{shlex.join(PROTOCOL[config])}`")
    lines += ["", "LLGo uses target-specific upstream Emscripten/Binaryen processing; see the recorded protocol.",
              "TinyGo uses its separately pinned Binaryen release.",
              "Failed builds are shown as — and excluded from comparisons; logs are included in the CI artifact.", ""]
    failures = [(app, config) for app in document["benchmarks"] for config in CONFIGS
                if app["builds"][config]["status"] != "success"]
    if failures:
        lines += ["## Failed builds", "", "| Application | Configuration | Policy | Status | Log |",
                  "| --- | --- | --- | --- | --- |"]
        for app, config in failures:
            policy = "optional" if config == "TinyGo" and app["tinygo"] == "optional" else "required"
            log = app["builds"][config]["log"]
            lines.append(f"| {app['id']} | {config} | {policy} | {app['builds'][config]['status']} | [{log}]({log}) |")
        lines.append("")
    lines += ["| Application | Target | Go toolchain | Source repository | Commit | Entry |",
              "| --- | --- | --- | --- | --- | --- |"]
    for app in document["benchmarks"]:
        lines.append(f"| {app['id']} | {app['target']['goos']}/wasm | {app['goVersion']} | {app['repository']} | {app['revision']} | {app['source']} |")
    lines.append("")
    for target, target_comparisons in document["comparisonsByTarget"].items():
        for baseline in ("Go", "TinyGo"):
            lines += [f"## {target}/wasm binary size (vs. {baseline})", "",
                      "| LLGo mode | Geometric mean / baseline | Valid samples |",
                      "| --- | ---: | ---: |"]
            for config, result in target_comparisons[baseline].items():
                ratio = f"{result['ratio']:.3f}x" if result["ratio"] is not None else "—"
                lines.append(f"| {LABELS[config]} | {ratio} | {result['samples']} |")
            lines += ["", f"| Application | {baseline} bytes | LLGo mode | LLGo bytes | vs. {baseline} |",
                      "| --- | ---: | --- | ---: | ---: |"]
            for row in document["benchmarks"]:
                if row["target"]["goos"] != target:
                    continue
                reference = row["values"][baseline]
                for config in LLGO_CONFIGS:
                    value = row["values"][config]
                    delta = f"{(value / reference - 1) * 100:+.1f}%" if value and reference else "—"
                    lines.append(f"| `{row['command']}` | {reference or '—'} | {LABELS[config]} | {value or '—'} | {delta} |")
            lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main(argv: list[str]) -> int:
    if len(argv) == 3 and argv[1] == "--configs":
        # Validate policy and identifiers before run.sh starts any compiler.
        read_manifest(Path(argv[2]))
        for config, flags in PROTOCOL.items():
            environment = ENVIRONMENT.get(config, {})
            print("\t".join([config, "CCFLAGS=" + environment.get("CCFLAGS", ""),
                             "LDFLAGS=" + environment.get("LDFLAGS", ""), *flags]))
        return 0
    if len(argv) != 4:
        print("usage: report.py MANIFEST_TSV SIZES_TSV OUTPUT_DIR", file=sys.stderr)
        return 2
    manifest_path, sizes_path, output_dir = map(Path, argv[1:])
    output_dir.mkdir(parents=True, exist_ok=True)
    try:
        document = build_document(read_manifest(manifest_path), read_sizes(sizes_path))
    except (OSError, ValueError) as error:
        print(error, file=sys.stderr)
        return 1
    for app in document["benchmarks"]:
        for config in CONFIGS:
            metadata = output_dir / "logs" / f"{app['id']}.{config}.log.json"
            if metadata.exists():
                command = json.loads(metadata.read_text())
                app["builds"][config].update(commandExitCode=command["exitCode"], seconds=command["seconds"])
    with (output_dir / "results.json").open("w", encoding="utf-8") as destination:
        json.dump(document, destination, indent=2)
        destination.write("\n")
    write_summary(document, output_dir / "summary.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
