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
wasm_ld_bin="$(command -v wasm-ld)"
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
mkdir -p "$raw_dir" "$output_dir/logs"
rm -f "$output_dir/results.json" "$output_dir/summary.md"
# Keep compiler flags identical to the protocol recorded by report.py.
python3 "$script_dir/report.py" --configs "$manifest" > "$output_dir/configs.tsv"
sizes="$output_dir/sizes.tsv"
printf 'app\tconfig\tbytes\tstatus\n' > "$sizes"

GO_ACTUAL_VERSION="$(GOTOOLCHAIN="$go_toolchain" "$go_bin" version)"
TINYGO_ACTUAL_VERSION="$(GOTOOLCHAIN="$go_toolchain" "$tinygo_bin" version)"
LLGO_ACTUAL_VERSION="$($LLGO_BIN version)"
CLANG_ACTUAL_VERSION="$($clang_bin --version | head -n 1)"
WASM_LD_ACTUAL_VERSION="$($wasm_ld_bin --version | head -n 1)"
TINYGO_WASM_OPT_ACTUAL_VERSION="$($wasm_opt_bin --version | head -n 1)"
LLGO_WASM_OPT_ACTUAL_VERSION="$($llgo_wasm_opt_bin --version | head -n 1)"
export GO_ACTUAL_VERSION TINYGO_ACTUAL_VERSION LLGO_ACTUAL_VERSION CLANG_ACTUAL_VERSION
export TINYGO_WASM_OPT_ACTUAL_VERSION LLGO_WASM_OPT_ACTUAL_VERSION
export WASM_LD_ACTUAL_VERSION
if [[ "$TINYGO_WASM_OPT_ACTUAL_VERSION" != "wasm-opt version $BINARYEN_VERSION" ]]; then
  echo "expected TinyGo Binaryen $BINARYEN_VERSION, got: $TINYGO_WASM_OPT_ACTUAL_VERSION ($wasm_opt_bin)" >&2
  exit 1
fi
# Bitcode requires a matching compiler/linker pair; a native-only build can
# accidentally hide an older wasm-ld elsewhere on PATH.
python3 - "$CLANG_ACTUAL_VERSION" "$WASM_LD_ACTUAL_VERSION" "${LLVM_VERSION:?LLVM_VERSION must identify the LLVM release}" <<'PY'
import re
import sys

for version in sys.argv[1:3]:
    match = re.search(r"\b(\d+)\.\d+", version)
    if not match or match[1] != sys.argv[3]:
        raise SystemExit(f"expected LLVM {sys.argv[3]} compiler and wasm-ld, got: {version}")
PY

verify_wasm() {
  python3 - "$1" <<'PY'
from pathlib import Path
import sys

path = Path(sys.argv[1])
if path.read_bytes()[:4] != b"\0asm":
    raise SystemExit(f"{path}: output does not have the WebAssembly magic header")
PY
}

while IFS=$'\t' read -r app_id command source _provenance _kind _description tinygo_policy; do
  [[ "$app_id" != "id" ]] || continue
  tinygo_policy="${tinygo_policy%$'\r'}"
  if [[ ! -d "$apps_dir/$source" ]]; then
    echo "application source does not exist: $source" >&2
    exit 1
  fi
  source_dir="$(cd -- "$apps_dir/$source" && pwd)"
  case "$source_dir/" in
    "$apps_dir"/*/) ;;
    *) echo "refusing application source outside $apps_dir: $source" >&2; exit 1 ;;
  esac
  while IFS=$'\t' read -r -a config_fields; do
    config="${config_fields[0]}"
    config_env=("${config_fields[@]:1:2}")
    flags=("${config_fields[@]:3}")
    compiler="$LLGO_BIN"
    postlink="$llgo_wasm_opt_bin"
    case "$config" in
      Go) compiler="$go_bin" ;;
      TinyGo) compiler="$tinygo_bin"; postlink="$wasm_opt_bin" ;;
    esac
    mkdir -p "$raw_dir/$config"
    binary="$raw_dir/$config/$app_id.wasm"
    log="$output_dir/logs/$app_id.$config.log"
    # A retry must never measure an artifact left by an earlier successful run.
    rm -f "$binary"
    echo "[wasm-size] building $app_id ($command) with $config"
    build_status=success
    if (
      cd "$source_dir" &&
      env "${config_env[@]}" CFLAGS= WASMOPT="$postlink" GOTOOLCHAIN="$go_toolchain" GOOS=wasip1 GOARCH=wasm \
        "$compiler" "${flags[@]}" -o "$binary" . && verify_wasm "$binary"
    ) >"$log" 2>&1; then
      bytes="$(wc -c < "$binary" | tr -d ' ')"
    else
      build_status=failed
      bytes=null
      rm -f "$binary"
      tail -n 80 "$log" >&2
    fi
    printf '%s\t%s\t%s\t%s\n' "$app_id" "$config" "$bytes" "$build_status" >> "$sizes"
    if [[ "$build_status" == failed ]]; then
      if [[ "$config" == TinyGo && "$tinygo_policy" == optional ]]; then
        echo "[wasm-size] optional TinyGo build failed: $app_id (see $log)" >&2
      else
        exit 1
      fi
    fi
  done < "$output_dir/configs.tsv"
done < "$manifest"

python3 "$script_dir/report.py" "$manifest" "$sizes" "$output_dir"
cat "$output_dir/summary.md"
