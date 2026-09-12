#!/usr/bin/env python3
"""Resolve pinned external commands without copying or rewriting their sources."""
from __future__ import annotations

import hashlib
import os
from pathlib import Path
import subprocess
import sys

from report import read_manifest


def git(root: Path, *args: str) -> str:
    return subprocess.check_output(["git", "-C", str(root), *args], text=True).strip()


def checkout(repository: str, revision: str, cache: Path) -> Path:
    key = hashlib.sha256(repository.encode()).hexdigest()[:16] + "-" + revision
    root = cache / key
    if not root.exists():
        root.mkdir(parents=True)
        try:
            git(root, "init", "-q")
            git(root, "remote", "add", "origin", repository)
            git(root, "fetch", "--depth=1", "origin", revision)
            git(root, "checkout", "--detach", "-q", "FETCH_HEAD")
        except BaseException:
            # Remove incomplete checkouts so a retry fetches verified sources.
            import shutil
            shutil.rmtree(root)
            raise
    if git(root, "remote", "get-url", "origin") != repository:
        raise ValueError(f"unexpected source remote: {root}")
    if git(root, "rev-parse", "HEAD") != revision:
        raise ValueError(f"unexpected source revision: {root}")
    if git(root, "status", "--porcelain", "--untracked-files=all"):
        raise ValueError(f"source checkout is modified: {root}")
    return root.resolve()


def prepare(manifest: Path, local: Path, cache: Path) -> list[list[str]]:
    plan = []
    for app in read_manifest(manifest):
        external = app["repository"] != "-"
        root = checkout(app["repository"], app["revision"], cache) if external else local.resolve()
        entry = (root / app["source"]).resolve()
        if not entry.is_relative_to(root) or not entry.exists():
            raise ValueError(f"invalid application entry: {app['id']}: {entry}")
        if external:
            # Build from the upstream root, preserving its module and entry path.
            target = "./" + app["source"]
            cwd = root
            revision = app["revision"]
        else:
            if not entry.is_dir():
                raise ValueError(f"local application must be a directory: {entry}")
            cwd, target, revision = entry, ".", "-"
        version = os.environ["GO_VERSION"] if app["go_version"] == "default" else app["go_version"]
        plan.append([app["id"], app["command"], str(cwd), target, app["tinygo"], "go" + version.removeprefix("go"), revision])
    return plan


def main() -> None:
    if len(sys.argv) != 5:
        raise SystemExit("usage: prepare_sources.py MANIFEST LOCAL_APPS CACHE PLAN_TSV")
    rows = prepare(Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]))
    Path(sys.argv[4]).write_text("".join("\t".join(row) + "\n" for row in rows))


if __name__ == "__main__":
    main()
