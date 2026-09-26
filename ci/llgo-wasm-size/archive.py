#!/usr/bin/env python3
"""Archive one WASM size result in an existing Pages checkout."""

from __future__ import annotations

import glob
import json
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path


SAFE_KEY = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*")


def run_key(document: dict) -> str:
    run = document.get("run", {})
    key = str(run.get("llgoCommit") or run.get("sourceCommit") or run.get("id") or "manual")
    if not SAFE_KEY.fullmatch(key):
        raise ValueError(f"invalid WASM run key: {key!r}")
    return key


def archive(run_dir: Path, pages_dir: Path) -> str:
    required = [run_dir / "results.json", run_dir / "summary.md", run_dir / "sizes.tsv"]
    for path in required:
        if not path.is_file() or path.stat().st_size == 0:
            raise ValueError(f"missing WASM result: {path}")
    with required[0].open(encoding="utf-8") as source:
        document = json.load(source)
    if document.get("format") != "wasm-file-size":
        raise ValueError(f"unexpected WASM result format: {document.get('format')!r}")
    if document.get("schemaVersion", 1) not in (1, 2):
        raise ValueError(f"unsupported WASM schema: {document.get('schemaVersion')!r}")

    key = run_key(document)
    data_dir = pages_dir / "data" / "wasm"
    published_dir = data_dir / "runs" / key
    published_dir.mkdir(parents=True, exist_ok=True)
    suite = document.get("suite", "all")
    previous = published_dir / "results.json"
    if suite in {"standard", "tsgo"} and previous.exists():
        stored = json.loads(previous.read_text())
        # Each independent runner replaces only its own rows, in either order.
        retained = [row for row in stored["benchmarks"]
                    if (row["id"] == "tsgo") != (suite == "tsgo")]
        document["benchmarks"] = sorted(retained + document["benchmarks"], key=lambda row: row["id"])
        from report import comparisons, write_summary
        rows = document["benchmarks"]
        document["protocol"]["sameGoToolchain"] = len({row["goVersion"] for row in rows}) == 1
        document["comparisons"] = comparisons(rows)
        document["comparisonsByTarget"] = {
            target: comparisons([row for row in rows if row.get("target", {}).get("goos", "wasip1") == target])
            for target in {row.get("target", {}).get("goos", "wasip1") for row in rows}
        }
        document["target"] = {"goos": "per-application", "goarch": "wasm"}
        previous.write_text(json.dumps(document, indent=2) + "\n")
        write_summary(document, published_dir / "summary.md")
        lines = ["app\tconfig\tbytes\tstatus\n"]
        for row in rows:
            for config in document["configs"]:
                value = row["values"][config]
                lines.append(f"{row['id']}\t{config}\t{value if value is not None else 'null'}\t{row['builds'][config]['status']}\n")
        (published_dir / "sizes.tsv").write_text("".join(lines))
    else:
        for source in required:
            shutil.copy2(source, published_dir / source.name)
    # Keep build-status log references usable from the archived JSON as well
    # as from the full CI artifact. Older schema-v1 runs may have no logs.
    logs = published_dir / "logs"
    if logs.exists() and suite not in {"standard", "tsgo"}:
        shutil.rmtree(logs)
    if (run_dir / "logs").is_dir():
        shutil.copytree(run_dir / "logs", logs, dirs_exist_ok=True)

    runs = []
    for result_path_string in glob.glob(str(data_dir / "runs" / "*" / "results.json")):
        result_path = Path(result_path_string)
        with result_path.open(encoding="utf-8") as source:
            stored = json.load(source)
        run = stored.get("run", {})
        stored_key = result_path.parent.name
        runs.append({
            "schemaVersion": stored.get("schemaVersion", 1),
            "configs": stored.get("configs", ["Go", "TinyGo", "LLGo"]),
            "key": stored_key,
            "id": run.get("id", ""),
            "attempt": run.get("attempt"),
            "number": run.get("number"),
            "createdAt": run.get("createdAt", ""),
            "sourceCommit": run.get("sourceCommit", ""),
            "ref": run.get("ref", ""),
            "llgoRepository": run.get("llgoRepository", ""),
            "llgoCommit": run.get("llgoCommit", ""),
            "llgoMainIndex": run.get("llgoMainIndex"),
            "llgoCommittedAt": run.get("llgoCommittedAt", ""),
            "llgoBuildGoVersion": run.get("llgoBuildGoVersion", ""),
            "goVersion": run.get("goVersion", ""),
            "llvmVersion": run.get("llvmVersion", ""),
            "tinygoVersion": run.get("tinygoVersion", ""),
            "binaryenVersion": run.get("binaryenVersion", ""),
            "workflowUrl": run.get("workflowUrl", ""),
            "path": f"wasm/runs/{stored_key}/results.json",
        })
    runs.sort(
        key=lambda item: (item["llgoMainIndex"] if isinstance(item["llgoMainIndex"], int) else -1, item["createdAt"]),
        reverse=True,
    )
    index = {
        "schemaVersion": 1,
        "generatedAt": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "runs": runs,
    }
    data_dir.mkdir(parents=True, exist_ok=True)
    with (data_dir / "index.json").open("w", encoding="utf-8") as destination:
        json.dump(index, destination, indent=2)
        destination.write("\n")
    return key


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print("usage: archive.py RUN_DIR PAGES_DIR", file=sys.stderr)
        return 2
    try:
        key = archive(Path(argv[1]), Path(argv[2]))
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(error, file=sys.stderr)
        return 1
    print(key)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
