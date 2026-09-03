#!/usr/bin/env bash
set -euo pipefail

run_dir=$1
pages_dir=$2
site_dir=$3
if [[ -z "$run_dir" || -z "$pages_dir" || -z "$site_dir" ]]; then
  echo "usage: publish.sh RUN_DIR PAGES_DIR SITE_DIR" >&2
  exit 2
fi

result_json="$run_dir/results.json"
if [[ ! -s "$result_json" ]]; then
  echo "missing compatibility result: $result_json" >&2
  exit 1
fi

run_key=$(python3 - "$result_json" <<'PY'
import json
import re
import sys

with open(sys.argv[1], encoding="utf-8") as source:
    run = json.load(source)["run"]
key = str(run.get("llgoTag") or run.get("llgoCommit") or run.get("id") or "manual")
if not re.fullmatch(r"[A-Za-z0-9._-]+", key):
    raise SystemExit("invalid compatibility run key: " + repr(key))
print(key)
PY
)

compatibility_dir="$pages_dir/data/compatibility"
published_run_dir="$compatibility_dir/runs/$run_key"
mkdir -p "$published_run_dir/raw"
cp "$result_json" "$published_run_dir/results.json"
for config in Go LLGo; do
  if [[ -s "$run_dir/$config.log" ]]; then
    cp "$run_dir/$config.log" "$published_run_dir/raw/$config.log"
  fi
  matches=("$run_dir"/bench/*."$config".stdout)
  if ((${#matches[@]} == 1)) && [[ -s "${matches[0]}" ]]; then
    cp "${matches[0]}" "$published_run_dir/raw/$config.stdout"
  fi
done

python3 - "$compatibility_dir" <<'PY'
import glob
import json
import os
import sys
from datetime import datetime, timezone

data_dir = sys.argv[1]
runs = []
for path in glob.glob(os.path.join(data_dir, "runs", "*", "results.json")):
    with open(path, encoding="utf-8") as source:
        document = json.load(source)
    run = document.get("run", {})
    key = os.path.basename(os.path.dirname(path))
    runs.append({
        "key": key,
        "id": run.get("id", ""),
        "attempt": run.get("attempt"),
        "createdAt": run.get("createdAt", ""),
        "sourceCommit": run.get("sourceCommit", ""),
        "llgoRepository": run.get("llgoRepository", ""),
        "llgoCommit": run.get("llgoCommit", ""),
        "llgoTag": run.get("llgoTag", ""),
        "goVersion": run.get("goVersion", ""),
        "llvmVersion": run.get("llvmVersion", ""),
        "workflowUrl": run.get("workflowUrl", ""),
        "path": "compatibility/runs/" + key + "/results.json",
    })
runs.sort(key=lambda item: item["createdAt"], reverse=True)
index = {
    "schemaVersion": 1,
    "generatedAt": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
    "runs": runs,
}
os.makedirs(data_dir, exist_ok=True)
with open(os.path.join(data_dir, "index.json"), "w", encoding="utf-8") as destination:
    json.dump(index, destination, indent=2)
    destination.write("\n")
PY

# Result jobs can finish long after a newer site revision has been published.
# Seed a brand-new Pages branch, but leave existing static assets to the
# dedicated Pages workflow so an old result job cannot roll the UI back.
for file in index.html linux.html app.js wasm.js performance.html performance.js compatibility.html compatibility.js style.css _config.yml; do
  if [[ ! -e "$pages_dir/$file" ]]; then
    cp "$site_dir/$file" "$pages_dir/$file"
  fi
done
rm -f "$pages_dir/.nojekyll"

git -C "$pages_dir" config user.name "github-actions[bot]"
git -C "$pages_dir" config user.email "41898282+github-actions[bot]@users.noreply.github.com"
git -C "$pages_dir" add -A
if git -C "$pages_dir" diff --cached --quiet; then
  echo "Compatibility history is already up to date"
else
  git -C "$pages_dir" commit -m "ci: publish LLGo compatibility run $run_key"
  git -C "$pages_dir" push origin HEAD:pages
fi
