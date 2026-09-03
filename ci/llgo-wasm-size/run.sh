#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
output_dir="${1:-}"
if [[ -z "$output_dir" ]]; then
  echo "usage: run.sh OUTPUT_DIR" >&2
  exit 2
fi
mkdir -p "$output_dir"
output_dir="$(cd -- "$output_dir" && pwd)"
: "${LLGO_BIN:?LLGO_BIN must name the LLGo executable}"
: "${GO_VERSION:?GO_VERSION must select the shared Go toolchain}"
: "${TINYGO_VERSION:?TINYGO_VERSION must identify the TinyGo release}"
: "${BINARYEN_VERSION:?BINARYEN_VERSION must identify the TinyGo wasm-opt release}"
# The benchmark applications are self-contained modules. Do not let a caller's
# ambient workspace change their dependency graph or LLGo runtime resolution.
export GOWORK=off

tinygo_bin="$(command -v tinygo)"
go_bin="$(command -v go)"
clang_bin="$(command -v clang++)"
wasm_opt_bin="$(command -v wasm-opt)"
llgo_wasm_opt_bin="${LLGO_WASMOPT:-$wasm_opt_bin}"
if [[ ! -x "$llgo_wasm_opt_bin" ]]; then
  echo "LLGO_WASMOPT is not executable: $llgo_wasm_opt_bin" >&2
  exit 1
fi
go_toolchain="go${GO_VERSION#go}"
apps_dir="$script_dir/apps"
manifest="$script_dir/apps.tsv"
raw_dir="$output_dir/raw"
mkdir -p "$raw_dir/Go" "$raw_dir/TinyGo" "$raw_dir/LLGo" "$output_dir/logs"
sizes="$output_dir/sizes.tsv"
printf 'app\tgo_bytes\ttinygo_bytes\tllgo_bytes\n' > "$sizes"

GO_ACTUAL_VERSION="$(GOTOOLCHAIN="$go_toolchain" "$go_bin" version)"
TINYGO_ACTUAL_VERSION="$(GOTOOLCHAIN="$go_toolchain" "$tinygo_bin" version)"
LLGO_ACTUAL_VERSION="$($LLGO_BIN version)"
CLANG_ACTUAL_VERSION="$($clang_bin --version | head -n 1)"
TINYGO_WASM_OPT_ACTUAL_VERSION="$($wasm_opt_bin --version | head -n 1)"
LLGO_WASM_OPT_ACTUAL_VERSION="$($llgo_wasm_opt_bin --version | head -n 1)"
export GO_ACTUAL_VERSION TINYGO_ACTUAL_VERSION LLGO_ACTUAL_VERSION CLANG_ACTUAL_VERSION
export TINYGO_WASM_OPT_ACTUAL_VERSION LLGO_WASM_OPT_ACTUAL_VERSION

verify_wasm() {
  python3 - "$1" <<'PY'
from pathlib import Path
import sys

path = Path(sys.argv[1])
if path.read_bytes()[:4] != b"\0asm":
    raise SystemExit(f"{path}: output does not have the WebAssembly magic header")
PY
}

while IFS=$'\t' read -r app_id command source _provenance _kind _description; do
  [[ "$app_id" != "id" ]] || continue
  if [[ ! -d "$apps_dir/$source" ]]; then
    echo "application source does not exist: $source" >&2
    exit 1
  fi
  source_dir="$(cd -- "$apps_dir/$source" && pwd)"
  case "$source_dir/" in
    "$apps_dir"/*/) ;;
    *) echo "refusing application source outside $apps_dir: $source" >&2; exit 1 ;;
  esac
  go_out="$raw_dir/Go/$app_id.wasm"
  tinygo_out="$raw_dir/TinyGo/$app_id.wasm"
  llgo_out="$raw_dir/LLGo/$app_id.wasm"

  echo "[wasm-size] building $app_id ($command) with Go"
  if ! (
    cd "$source_dir"
    GOTOOLCHAIN="$go_toolchain" GOOS=wasip1 GOARCH=wasm \
      "$go_bin" build -trimpath -ldflags="-s -w" -o "$go_out" .
  ) >"$output_dir/logs/$app_id.Go.log" 2>&1; then
    tail -n 80 "$output_dir/logs/$app_id.Go.log" >&2
    exit 1
  fi

  echo "[wasm-size] building $app_id ($command) with TinyGo"
  if ! (
    cd "$source_dir"
    GOTOOLCHAIN="$go_toolchain" GOOS=wasip1 GOARCH=wasm \
      "$tinygo_bin" build -opt=z -no-debug -o "$tinygo_out" .
  ) >"$output_dir/logs/$app_id.TinyGo.log" 2>&1; then
    tail -n 80 "$output_dir/logs/$app_id.TinyGo.log" >&2
    exit 1
  fi

  echo "[wasm-size] building $app_id ($command) with LLGo"
  if ! (
    cd "$source_dir"
    WASMOPT="$llgo_wasm_opt_bin" \
      GOTOOLCHAIN="$go_toolchain" GOOS=wasip1 GOARCH=wasm \
      "$LLGO_BIN" build -Oz -o "$llgo_out" .
  ) >"$output_dir/logs/$app_id.LLGo.log" 2>&1; then
    tail -n 80 "$output_dir/logs/$app_id.LLGo.log" >&2
    exit 1
  fi

  verify_wasm "$go_out"
  verify_wasm "$tinygo_out"
  verify_wasm "$llgo_out"
  go_bytes="$(wc -c < "$go_out" | tr -d ' ')"
  tinygo_bytes="$(wc -c < "$tinygo_out" | tr -d ' ')"
  llgo_bytes="$(wc -c < "$llgo_out" | tr -d ' ')"
  printf '%s\t%s\t%s\t%s\n' "$app_id" "$go_bytes" "$tinygo_bytes" "$llgo_bytes" >> "$sizes"
done < "$manifest"

python3 "$script_dir/report.py" "$manifest" "$sizes" "$output_dir"
cat "$output_dir/summary.md"
