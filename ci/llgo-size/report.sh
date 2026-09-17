#!/usr/bin/env bash
set -euo pipefail

run_dir=$1
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
bench_dir="$run_dir/bench"
result_dir="$run_dir/results"
mkdir -p "$result_dir"

configs=(
  Go
  LLGoNoLTO
  LLGoDeadcodeDrop
  LLGoFullLTONoGlobalDCE
  LLGoFullLTOGlobalDCE
  LLGoFullLTOGlobalDCEPlugin
)

summary="$result_dir/summary.md"
tsv="$result_dir/total-bytes.tsv"
raw_dir="$result_dir/raw"
json="$result_dir/results.json"
build_tsv="$result_dir/build-times.tsv"
timing_summary="$result_dir/timing-summary.md"
mkdir -p "$raw_dir"

printf '%s\n' '# LLGo binary-size CI' > "$summary"
# shellcheck disable=SC2016 # Literal Markdown code span.
printf '%s\n\n' 'All values are ELF file sizes in bytes, collected by Bent `benchsize`.' >> "$summary"
printf 'benchmark' > "$tsv"
for config in "${configs[@]}"; do
  printf '\t%s' "$config" >> "$tsv"
done
printf '\n' >> "$tsv"

printf '| Benchmark |' >> "$summary"
for config in "${configs[@]}"; do
  printf ' %s |' "$config" >> "$summary"
done
printf '\n| --- |' >> "$summary"
for config in "${configs[@]}"; do
  printf ' ---: |' >> "$summary"
done
printf '\n' >> "$summary"

if [[ ! -d "$bench_dir" ]]; then
  echo "missing Bent output directory: $bench_dir" >&2
  exit 1
fi

# Include configured cases even if no compiler succeeded, and collect results
# from every configuration so a failed Go baseline cannot hide other results.
python3 - "$bench_dir" "$script_dir/../../cmd/bent/configs/benchmarks-llgo-size.toml" > "$result_dir/benchmarks.txt" <<'PY'
from pathlib import Path
import sys
import tomllib

with open(sys.argv[2], "rb") as source:
    cases = tomllib.load(source)["Benchmarks"]
names = {case["Name"][0].upper() + case["Name"][1:] for case in cases if not case.get("Disabled", False)}
for path in Path(sys.argv[1]).glob("*.benchsize"):
    for line in path.read_text().splitlines():
        fields = line.split()
        if len(fields) >= 4 and fields[0].startswith("Benchmark") and fields[3] == "total-bytes":
            names.add(fields[0][len("Benchmark"):])
print("\n".join(sorted(names)))
PY
missing=0
while IFS= read -r benchmark; do
  printf '%s' "$benchmark" >> "$tsv"
  printf '| %s |' "$benchmark" >> "$summary"
  for config in "${configs[@]}"; do
    value=$(find "$bench_dir" -maxdepth 1 -type f -name "*.$config.benchsize" -exec \
      awk -v key="Benchmark$benchmark" '$1 == key && $4 == "total-bytes" { print $3; exit }' {} +)
    value=${value%%$'\n'*}
    if [[ -z "$value" ]]; then
      echo "missing total-bytes result for $benchmark ($config)" >&2
      missing=$((missing + 1))
      value=null
    fi
    printf '\t%s' "$value" >> "$tsv"
    if [[ "$value" == null ]]; then
      printf ' — |' >> "$summary"
    else
      printf ' %s |' "$value" >> "$summary"
    fi
  done
  printf '\n' >> "$tsv"
  printf '\n' >> "$summary"
done < "$result_dir/benchmarks.txt"
if ((missing > 0)); then
  printf '\n%d results are missing; see the CI build log. Missing values are excluded from comparisons.\n' "$missing" >> "$summary"
fi


find "$bench_dir" -maxdepth 1 -type f -name '*.benchsize' -exec cp -f {} "$raw_dir/" \;

find "$bench_dir" -maxdepth 1 -type f -name '*.build' -exec cp -f {} "$raw_dir/" \;
: > "$result_dir/download-timings.log"
if [[ -s "$run_dir/download-timings.log" ]]; then
  cp "$run_dir/download-timings.log" "$result_dir/download-timings.log"
fi
if [[ -f "$run_dir/build.log" ]]; then
  cp "$run_dir/build.log" "$result_dir/build.log"
fi

python3 "$script_dir/timing-report.py" "$bench_dir" "$build_tsv" "$timing_summary"

export LLGO_SIZE_TSV="$tsv"
export LLGO_BUILD_TIMES_TSV="$build_tsv"
export LLGO_SIZE_JSON="$json"
python3 - <<'PY'
import csv
import json
import os
from datetime import datetime, timezone

tsv = os.environ["LLGO_SIZE_TSV"]
build_times_tsv = os.environ["LLGO_BUILD_TIMES_TSV"]
output = os.environ["LLGO_SIZE_JSON"]
configs = [
    "Go",
    "LLGoNoLTO",
    "LLGoDeadcodeDrop",
    "LLGoFullLTONoGlobalDCE",
    "LLGoFullLTOGlobalDCE",
    "LLGoFullLTOGlobalDCEPlugin",
]

build_times = {}
with open(build_times_tsv, newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f, delimiter="\t"):
        user_ns = int(row["user-ns"])
        sys_ns = int(row["sys-ns"])
        build_times.setdefault(row["benchmark"], {})[row["configuration"]] = {
            "cpuNs": user_ns + sys_ns,
            "userNs": user_ns,
            "sysNs": sys_ns,
            "wallNs": int(row["real-ns"]),
        }

benchmarks = []
with open(tsv, newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f, delimiter="\t"):
        benchmarks.append({
            "name": row["benchmark"],
            "values": {name: None if row[name] == "null" else int(row[name]) for name in configs},
            "builds": {name: {"status": "missing" if row[name] == "null" else "success"} for name in configs},
            "buildTimes": build_times.get(row["benchmark"], {}),
        })

def env(name, fallback=""):
    return os.environ.get(name) or os.environ.get(fallback, "")

def number(name, fallback):
    value = env(name, fallback)
    try:
        return int(value)
    except ValueError:
        return None

repository = env("LLGO_SIZE_REPOSITORY", "GITHUB_REPOSITORY")
run_id = env("LLGO_SIZE_RUN_ID", "GITHUB_RUN_ID")
workflow_url = os.environ.get("LLGO_SIZE_WORKFLOW_URL", "")
if not workflow_url and repository and run_id:
    workflow_url = "https://github.com/" + repository + "/actions/runs/" + run_id

run = {
    "id": run_id,
    "attempt": number("LLGO_SIZE_RUN_ATTEMPT", "GITHUB_RUN_ATTEMPT"),
    "number": number("LLGO_SIZE_RUN_NUMBER", "GITHUB_RUN_NUMBER"),
    "createdAt": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
    "repository": repository,
    "sourceCommit": env("LLGO_SIZE_SOURCE_COMMIT", "GITHUB_SHA"),
    "ref": env("LLGO_SIZE_REF", "GITHUB_REF_NAME"),
    "llgoRepository": os.environ.get("LLGO_REPOSITORY", ""),
    "llgoCommit": os.environ.get("LLGO_COMMIT", ""),
    "llgoMainIndex": number("LLGO_MAIN_INDEX", ""),
    "llgoCommittedAt": os.environ.get("LLGO_COMMITTED_AT", ""),
    "goVersion": os.environ.get("GO_VERSION", ""),
    "llvmVersion": os.environ.get("LLVM_VERSION", ""),
    "event": env("LLGO_SIZE_EVENT", "GITHUB_EVENT_NAME"),
    "workflowUrl": workflow_url,
    "runnerOS": os.environ.get("RUNNER_OS", ""),
    "runnerArch": os.environ.get("RUNNER_ARCH", ""),
    "runnerImage": os.environ.get("ImageOS", ""),
}

document = {
    "schemaVersion": 1,
    "format": "bent-benchsize",
    "run": run,
    "configs": configs,
    "metric": "total-bytes",
    "buildTimeMetric": "user-plus-sys-ns",
    "benchmarks": benchmarks,
    "native": {
        "summary": "summary.md",
        "tsv": "total-bytes.tsv",
        "timingSummary": "timing-summary.md",
        "buildTimes": "build-times.tsv",
        "downloadTimings": "download-timings.log",
        "rawDir": "raw",
    },
}

with open(output, "w", encoding="utf-8") as f:
    json.dump(document, f, indent=2, sort_keys=False)
    f.write("\n")
PY

cat "$summary"
printf "\n"
cat "$timing_summary"
if ((missing > 0)); then
  exit 1
fi
