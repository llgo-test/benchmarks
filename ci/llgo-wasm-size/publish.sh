#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
results_dir="${1:-}"
pages_dir="${2:-}"
site_dir="${3:-}"
if [[ -z "$results_dir" || -z "$pages_dir" || -z "$site_dir" ]]; then
  echo "usage: publish.sh RESULTS_DIR PAGES_DIR SITE_DIR" >&2
  exit 2
fi

# Seed a new Pages branch without allowing an older result job to overwrite
# static assets already refreshed by the dedicated Pages workflow.
for file in index.html linux.html app.js wasm.js performance.html performance.js compatibility.html compatibility.js style.css _config.yml; do
  if [[ ! -e "$pages_dir/$file" ]]; then
    cp "$site_dir/$file" "$pages_dir/$file"
  fi
done
rm -f "$pages_dir/.nojekyll"

run_key="$(python3 "$script_dir/archive.py" "$results_dir" "$pages_dir")"

git -C "$pages_dir" config user.name "github-actions[bot]"
git -C "$pages_dir" config user.email "41898282+github-actions[bot]@users.noreply.github.com"
git -C "$pages_dir" add .
if git -C "$pages_dir" diff --cached --quiet; then
  echo "WASM Pages history is already up to date"
else
  git -C "$pages_dir" commit -m "ci: publish LLGo WASM size run $run_key"
  git -C "$pages_dir" push origin HEAD:pages
fi
