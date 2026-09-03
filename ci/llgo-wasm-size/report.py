#!/usr/bin/env python3
"""Turn one Go/TinyGo/LLGo WASM build round into publishable results."""

from __future__ import annotations

import csv
import json
import math
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


APP_ID = re.compile(r"[a-z0-9][a-z0-9-]*")


def read_manifest(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as source:
        rows = list(csv.DictReader(source, delimiter="\t"))
    expected = {"id", "command", "source", "provenance", "kind", "description"}
    if not rows or set(rows[0]) != expected:
        raise ValueError(f"{path}: expected columns {sorted(expected)}")
    seen: set[str] = set()
    for row in rows:
        app_id = row["id"]
        if not APP_ID.fullmatch(app_id) or app_id in seen:
            raise ValueError(f"{path}: invalid or duplicate app id {app_id!r}")
        if not all(row[field] for field in expected):
            raise ValueError(f"{path}: empty field in app {app_id!r}")
        seen.add(app_id)
    return rows


def read_sizes(path: Path) -> dict[str, tuple[int, int, int]]:
    with path.open(newline="", encoding="utf-8") as source:
        rows = list(csv.DictReader(source, delimiter="\t"))
    expected = {"app", "go_bytes", "tinygo_bytes", "llgo_bytes"}
    if not rows or set(rows[0]) != expected:
        raise ValueError(f"{path}: expected columns {sorted(expected)}")
    sizes: dict[str, tuple[int, int, int]] = {}
    for row in rows:
        app_id = row["app"]
        if app_id in sizes:
            raise ValueError(f"{path}: duplicate app {app_id!r}")
        values = (int(row["go_bytes"]), int(row["tinygo_bytes"]), int(row["llgo_bytes"]))
        if min(values) <= 0:
            raise ValueError(f"{path}: non-positive size for {app_id!r}")
        sizes[app_id] = values
    return sizes


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


def build_document(manifest: list[dict[str, str]], sizes: dict[str, tuple[int, int, int]]) -> dict:
    manifest_ids = {row["id"] for row in manifest}
    if set(sizes) != manifest_ids:
        missing = sorted(manifest_ids - set(sizes))
        extra = sorted(set(sizes) - manifest_ids)
        raise ValueError(f"size rows do not match app manifest; missing={missing}, extra={extra}")

    benchmarks = []
    for app in manifest:
        go_bytes, tinygo_bytes, llgo_bytes = sizes[app["id"]]
        benchmarks.append({
            "id": app["id"],
            "command": app["command"],
            "source": app["source"],
            "provenance": app["provenance"],
            "kind": app["kind"],
            "description": app["description"],
            "values": {"Go": go_bytes, "TinyGo": tinygo_bytes, "LLGo": llgo_bytes},
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
        "schemaVersion": 1,
        "format": "wasm-file-size",
        "run": run,
        "target": {"goos": "wasip1", "goarch": "wasm"},
        "configs": ["Go", "TinyGo", "LLGo"],
        "metric": "total-bytes",
        "protocol": {
            "Go": ["build", "-trimpath", "-ldflags=-s -w"],
            "TinyGo": ["build", "-opt=z", "-no-debug"],
            "LLGo": ["build", "-Oz"],
            "LLGoPostLink": ["Emscripten wasm-opt", "Asyncify and standardized exception translation"],
            "sameGoToolchain": True,
        },
        "toolVersions": {
            "Go": os.environ.get("GO_ACTUAL_VERSION", ""),
            "TinyGo": os.environ.get("TINYGO_ACTUAL_VERSION", ""),
            "LLGo": os.environ.get("LLGO_ACTUAL_VERSION", ""),
            "Clang": os.environ.get("CLANG_ACTUAL_VERSION", ""),
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
    rows = document["benchmarks"]
    tinygo_ratios = [row["values"]["TinyGo"] / row["values"]["Go"] for row in rows]
    llgo_ratios = [row["values"]["LLGo"] / row["values"]["Go"] for row in rows]
    tinygo_geomean = math.exp(sum(math.log(value) for value in tinygo_ratios) / len(tinygo_ratios))
    llgo_geomean = math.exp(sum(math.log(value) for value in llgo_ratios) / len(llgo_ratios))
    lines = [
        "# Go, TinyGo, and LLGo WASM application size",
        "",
        "`wasip1/wasm`; smaller is better. All three compilers use the same pinned Go toolchain.",
        "Go uses `-trimpath -ldflags='-s -w'`; TinyGo uses `-opt=z -no-debug`; LLGo uses `-Oz`.",
        "LLGo uses the `wasm-opt` bundled with pinned Emscripten for Asyncify and exception",
        "translation; TinyGo continues to use its separately pinned Binaryen release.",
        "",
        f"Geometric-mean TinyGo/Go size ratio: **{tinygo_geomean:.3f}x**.",
        f"Geometric-mean LLGo/Go size ratio: **{llgo_geomean:.3f}x**.",
        "",
        "| Application | Kind | Go bytes | TinyGo bytes | LLGo bytes | TinyGo vs Go | LLGo vs Go |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in rows:
        go_bytes = row["values"]["Go"]
        tinygo_bytes = row["values"]["TinyGo"]
        llgo_bytes = row["values"]["LLGo"]
        tinygo_delta = (tinygo_bytes / go_bytes - 1) * 100
        llgo_delta = (llgo_bytes / go_bytes - 1) * 100
        lines.append(
            f"| `{row['command']}` | {row['kind']} | {go_bytes} | {tinygo_bytes} | {llgo_bytes} | "
            f"{tinygo_delta:+.1f}% | {llgo_delta:+.1f}% |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(argv: list[str]) -> int:
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
    with (output_dir / "results.json").open("w", encoding="utf-8") as destination:
        json.dump(document, destination, indent=2)
        destination.write("\n")
    write_summary(document, output_dir / "summary.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
