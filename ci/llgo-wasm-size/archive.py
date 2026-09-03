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

    key = run_key(document)
    data_dir = pages_dir / "data" / "wasm"
    published_dir = data_dir / "runs" / key
    published_dir.mkdir(parents=True, exist_ok=True)
    for source in required:
        shutil.copy2(source, published_dir / source.name)

    runs = []
    for result_path_string in glob.glob(str(data_dir / "runs" / "*" / "results.json")):
        result_path = Path(result_path_string)
        with result_path.open(encoding="utf-8") as source:
            stored = json.load(source)
        run = stored.get("run", {})
        stored_key = result_path.parent.name
        runs.append({
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
