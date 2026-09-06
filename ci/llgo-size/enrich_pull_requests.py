#!/usr/bin/env python3
"""Add dashboard metadata and merged pull-request links to the Pages index."""

import argparse
import csv
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


REPOSITORY_RE = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
COMMIT_RE = re.compile(r"^[0-9a-fA-F]{40}$")


def select_merged_pull_request(pulls, commit):
    merged = [
        pull
        for pull in pulls
        if pull.get("merged_at") and pull.get("html_url") and pull.get("number")
    ]
    if not merged:
        return None

    exact = [
        pull
        for pull in merged
        if str(pull.get("merge_commit_sha", "")).lower() == commit.lower()
    ]
    candidates = exact or merged
    # The exact squash/merge commit is authoritative. If GitHub only reports
    # PRs containing the commit, use the first PR that landed it.
    return min(candidates, key=lambda pull: pull["merged_at"])


def github_pull_request_lookup(repository, commit, api_url, token):
    path = "/repos/{}/commits/{}/pulls".format(
        urllib.parse.quote(repository, safe="/"),
        urllib.parse.quote(commit, safe=""),
    )
    credentials = [token, ""] if token else [""]
    pulls = None
    for credential in credentials:
        request = urllib.request.Request(
            api_url.rstrip("/") + path,
            headers={
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
                "User-Agent": "llgo-test-benchmarks-pages",
            },
        )
        if credential:
            request.add_header("Authorization", "Bearer " + credential)
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                pulls = json.load(response)
            break
        except urllib.error.HTTPError as error:
            detail = error.read(500).decode("utf-8", "replace")
            # GITHUB_TOKEN is scoped to the benchmark repository. Public LLGo
            # metadata remains available without authentication if that token
            # cannot read the separate LLGo repository.
            if credential and error.code in (403, 404):
                continue
            raise RuntimeError(
                "GitHub API returned {} for {}@{}: {}".format(
                    error.code, repository, commit, detail
                )
            ) from error
        except urllib.error.URLError as error:
            raise RuntimeError(
                "cannot query GitHub for {}@{}: {}".format(
                    repository, commit, error.reason
                )
            ) from error
    if not isinstance(pulls, list):
        raise RuntimeError("unexpected GitHub response for {}@{}".format(repository, commit))
    return select_merged_pull_request(pulls, commit)


def result_path(run, data_dir):
    path_value = run.get("path")
    if not path_value:
        return None
    data_root = data_dir.resolve()
    path = (data_dir / str(path_value)).resolve()
    try:
        path.relative_to(data_root)
    except ValueError:
        return None
    return path


def result_document(run, data_dir):
    path = result_path(run, data_dir)
    if path is None:
        return {}
    try:
        with path.open(encoding="utf-8") as result_file:
            return json.load(result_file)
    except (OSError, ValueError):
        return {}


def repository_from_result(run, data_dir):
    return str(result_document(run, data_dir).get("run", {}).get("llgoRepository", ""))


def load_main_history(path):
    if path is None:
        return []
    with path.open(encoding="utf-8") as history_file:
        commits = [line.strip().lower() for line in history_file if line.strip()]
    invalid = [commit for commit in commits if not COMMIT_RE.fullmatch(commit)]
    if invalid:
        raise ValueError("invalid LLGo main commit in history: " + repr(invalid[0]))
    return commits


def order_runs(index, main_history):
    positions = {commit: position for position, commit in enumerate(main_history, start=1)}
    for run in index.get("runs", []):
        commit = str(run.get("llgoCommit", "")).lower()
        if commit in positions:
            run["llgoMainIndex"] = positions[commit]

    runs = index.setdefault("runs", [])
    def is_main_run(run):
        position = run.get("llgoMainIndex")
        return isinstance(position, int) and not isinstance(position, bool)

    main_runs = [run for run in runs if is_main_run(run)]
    other_runs = [run for run in runs if not is_main_run(run)]
    main_runs.sort(key=lambda run: run["llgoMainIndex"], reverse=True)
    other_runs.sort(
        key=lambda run: (
            str(run.get("llgoCommittedAt") or run.get("createdAt") or ""),
            str(run.get("key", "")),
        ),
        reverse=True,
    )
    runs[:] = main_runs + other_runs


def legacy_wall_times(run, document, data_dir):
    native_path = document.get("native", {}).get("buildTimes")
    path = result_path(run, data_dir)
    if not native_path or path is None:
        return {}
    timing_path = (path.parent / str(native_path)).resolve()
    try:
        timing_path.relative_to(data_dir.resolve())
        with timing_path.open(newline="", encoding="utf-8") as timing_file:
            return {
                (row["benchmark"], row["configuration"]): int(row["real-ns"])
                for row in csv.DictReader(timing_file, delimiter="\t")
            }
    except (KeyError, OSError, TypeError, ValueError):
        return {}


def build_trends(index, data_dir):
    names = set()
    runs = []
    for run in index.get("runs", []):
        document = result_document(run, data_dir)
        legacy_timings = legacy_wall_times(run, document, data_dir)
        benchmarks = []
        for benchmark in document.get("benchmarks", []):
            name = benchmark.get("name")
            if not name:
                continue
            name = str(name)
            names.add(name)
            values = {
                config: value
                for config, value in benchmark.get("values", {}).items()
                if isinstance(value, (int, float)) and not isinstance(value, bool)
            }
            build_times = {}
            for config, timing in benchmark.get("buildTimes", {}).items():
                wall_ns = timing.get("wallNs") if isinstance(timing, dict) else None
                if isinstance(wall_ns, (int, float)) and not isinstance(wall_ns, bool):
                    build_times[config] = {"wallNs": wall_ns}
            for (benchmark_name, config), wall_ns in legacy_timings.items():
                if benchmark_name == name and config not in build_times:
                    build_times[config] = {"wallNs": wall_ns}
            benchmarks.append({
                "name": name,
                "values": values,
                "buildTimes": build_times,
            })
        runs.append({"key": run.get("key", ""), "benchmarks": benchmarks})
    if names:
        index["benchmarkNames"] = sorted(names, key=str.casefold)
    return {
        "schemaVersion": 1,
        "generatedAt": index.get("generatedAt", ""),
        "runs": runs,
    }


def enrich_runs(index, data_dir, lookup, default_repository):
    queries = 0
    linked = 0
    cache = {}
    for run in index.get("runs", []):
        commit = str(run.get("llgoCommit", ""))
        repository = str(run.get("llgoRepository", ""))
        if not REPOSITORY_RE.fullmatch(repository):
            repository = repository_from_result(run, data_dir)
        if not REPOSITORY_RE.fullmatch(repository):
            repository = default_repository
        if not REPOSITORY_RE.fullmatch(repository) or not COMMIT_RE.fullmatch(commit):
            continue

        commit = commit.lower()
        commit_url = "https://github.com/{}/commit/{}".format(repository, commit)
        run["llgoRepository"] = repository
        run["commitUrl"] = commit_url
        if run.get("pullRequestResolved") is True:
            if run.get("pullRequestUrl"):
                linked += 1
            continue

        key = (repository, commit)
        if key not in cache:
            cache[key] = lookup(repository, commit)
            queries += 1
        pull = cache[key]
        run["pullRequestResolved"] = True
        if pull:
            run["pullRequestNumber"] = int(pull["number"])
            run["pullRequestUrl"] = str(pull["html_url"])
            run["pullRequestTitle"] = str(pull.get("title", ""))
            linked += 1
        else:
            run.pop("pullRequestNumber", None)
            run.pop("pullRequestUrl", None)
            run.pop("pullRequestTitle", None)
    return queries, linked


def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("index", type=Path, help="path to Pages data/index.json")
    parser.add_argument(
        "--default-repository",
        default="xgo-dev/llgo",
        help="LLGo repository for legacy results without repository metadata",
    )
    parser.add_argument(
        "--api-url",
        default=os.environ.get("GITHUB_API_URL", "https://api.github.com"),
    )
    parser.add_argument(
        "--main-history",
        type=Path,
        help="first-parent LLGo main commits, oldest first",
    )
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    if not REPOSITORY_RE.fullmatch(args.default_repository):
        raise SystemExit("invalid default repository: " + repr(args.default_repository))
    with args.index.open(encoding="utf-8") as index_file:
        index = json.load(index_file)
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN", "")

    order_runs(index, load_main_history(args.main_history))

    def lookup(repository, commit):
        return github_pull_request_lookup(repository, commit, args.api_url, token)

    trends = build_trends(index, args.index.parent)
    queries, linked = enrich_runs(index, args.index.parent, lookup, args.default_repository)
    trends_path = args.index.parent / "trends.json"
    trends_temporary = trends_path.with_suffix(trends_path.suffix + ".tmp")
    with trends_temporary.open("w", encoding="utf-8") as trends_file:
        json.dump(trends, trends_file, separators=(",", ":"))
        trends_file.write("\n")
    os.replace(trends_temporary, trends_path)
    temporary = args.index.with_suffix(args.index.suffix + ".tmp")
    with temporary.open("w", encoding="utf-8") as index_file:
        json.dump(index, index_file, indent=2)
        index_file.write("\n")
    os.replace(temporary, args.index)
    print(
        "Indexed {} benchmark name(s); resolved {} LLGo commit(s); {} run(s) link to merged PRs".format(
            len(index.get("benchmarkNames", [])), queries, linked
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
