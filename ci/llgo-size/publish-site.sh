#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
pages_dir="$1"
site_dir="$2"
main_history="${3:-}"
if [[ -z "$pages_dir" || -z "$site_dir" ]]; then
  echo "usage: publish-site.sh PAGES_DIR SITE_DIR [LLGO_MAIN_HISTORY]" >&2
  exit 2
fi

for file in index.html linux.html app.js wasm.js performance.html performance.js compatibility.html compatibility.js style.css _config.yml; do
  cp "$site_dir/$file" "$pages_dir/$file"
done
rm -f "$pages_dir/.nojekyll"
if [[ -s "$pages_dir/data/index.json" ]]; then
  enrich_args=("$pages_dir/data/index.json")
  if [[ -n "$main_history" && -s "$main_history" ]]; then
    enrich_args+=(--main-history "$main_history")
  fi
  python3 "$script_dir/enrich_pull_requests.py" "${enrich_args[@]}"
fi

git -C "$pages_dir" config user.name "github-actions[bot]"
git -C "$pages_dir" config user.email "41898282+github-actions[bot]@users.noreply.github.com"
git -C "$pages_dir" add -A
if git -C "$pages_dir" diff --cached --quiet; then
  echo "Pages site is already up to date"
else
  git -C "$pages_dir" commit -m "ci: refresh LLGo binary-size site"
  git -C "$pages_dir" push origin HEAD:pages
fi
