# Go, TinyGo, and LLGo WASM application-size CI

This benchmark builds ten runnable `wasip1/wasm` command-line applications with
the native Go compiler, TinyGo, and LLGo, then compares the final `.wasm` file
sizes. These are application workloads rather than single-package probes. The
suite covers image convolution, JSON processing, SHA-256, a streaming Base64
codec, multi-hash checksums, recursive computation, regular-expression and
wildcard filters, an HTML path report, and Unicode-aware text statistics.

Four commands are verbatim snapshots of upstream WASI applications: Fibonacci
from [`mattn/wasi-benchmark`](https://github.com/mattn/wasi-benchmark), plus
convolution, JSON, and SHA-256 from
[`universonic/go-rust-wasm-bench`](https://github.com/universonic/go-rust-wasm-bench).
Their fixed revisions and licenses are recorded in
[`THIRD_PARTY.md`](THIRD_PARTY.md). The other six commands are purpose-built
fixtures maintained in this repository. Those commands have standard-stream
I/O, argument/error handling, separate implementation packages, and functional
tests.

All three application builds resolve the same `GO_VERSION` from
`ci/llgo-size/llgo-version.env`; the newer toolchain needed to build the LLGo
command is pinned separately as `LLGO_BUILD_GO_VERSION`. Go uses
`-trimpath -ldflags='-s -w'` to remove path and debug metadata from the release
artifact. TinyGo uses `-opt=z -no-debug`, and LLGo uses `-Oz` with the pinned
LLVM 22 toolchain used by the selected `xgo-dev/llgo` main revision. TinyGo's
Binaryen 132 is pinned independently. LLGo uses the `wasm-opt` bundled with
Emscripten 4.0.21 for Asyncify and standardized exception translation,
matching LLGo main's own CI setup.
The runner disables any ambient Go workspace so all three compilers resolve the
application modules and LLGo runtime independently of the checkout location.

`run.sh` writes `results.json`, `summary.md`, `sizes.tsv`, compiler logs, and the
six sets of WASM binaries. CI uploads the complete directory as an artifact;
`archive.py` publishes JSON, Markdown, TSV, and compiler logs to the
`pages` branch. Published history is keyed by the full LLGo commit, matching the
Linux binary-size history.

The site has two views, **WASM binary size (vs. Go)** (`index.html`) and
**WASM binary size (vs. TinyGo)** (`wasm-tinygo.html`). Both use the same run.
Each view shows its baseline plus four LLGo configurations at `-Oz`:

| Configuration | LLGo flags | Additional clang environment |
| --- | --- | --- |
| no LTO | `-Oz` | none |
| deadcode drop | `-Oz -deadcodedrop` | none |
| full LTO, GlobalDCE off | `-Oz -lto=full -globaldce=false` | `CCFLAGS=-flto=full`, `LDFLAGS=-Wl,--lto-O2` |
| full LTO + GlobalDCE | `-Oz -lto=full -globaldce=true` | `CCFLAGS='-flto=full -fvirtual-function-elimination -fwhole-program-vtables'`, `LDFLAGS=-Wl,--lto-O2` |

The explicit clang flags are necessary for the pinned LLGo WASI external-clang
path: `-lto=full` alone does not cause that path to emit bitcode. All LLGo builds
also use `-a`, because ambient clang flags are not part of LLGo's package cache
fingerprint. This deliberately rebuilds packages instead of measuring potentially
stale archives. Compilation and linking must both use LLVM 22 (including
`wasm-ld`). `--lto-O2` matches LLGo's size-optimization linker setting on Linux;
LLVM and Binaryen still optimize each application at `-Oz`.
Put the pinned Binaryen's `bin` directory before TinyGo's `bin` on `PATH`:
the Linux TinyGo release bundles an older `wasm-opt`. The runner verifies the
resolved Binaryen version so this cannot silently change the baseline.
`report.py` is the source of truth for flags and records the complete protocol.
No LTO pass plugin is used for WASM.

`apps.tsv` explicitly declares TinyGo as `required` or `optional`. Existing
TinyGo-compatible applications remain required. Optional builds are still
attempted: compiler failure or invalid WASM output leaves a `null` value,
`failed` build status, and a compiler log. Go and all LLGo configurations are
required; any required failure fails the job. Invalid or stale output files
are never measured. `sizes.tsv` has one row per application/configuration with
`app`, `config`, `bytes`, and `status` columns.

Schema v2 records all six configurations, nullable values, build statuses and
log paths. The archive preserves these logs, while existing v1 history stays
unchanged. The frontend maps a legacy `LLGo` value to `LLGoNoLTO` only. Missing
baselines leave ratios, ranks and history points empty while retaining LLGo
absolute sizes. Each baseline's geometric mean uses only applications with
positive values for both sides and reports its own sample count; an empty
sample set has a null ratio.

Run the orchestration/report/archive tests with
`python3 -m unittest discover -s ci/llgo-wasm-size -p 'test_*.py' -v`,
frontend behavior tests with `node --test ci/llgo-wasm-size/test_wasm_site.cjs`,
and `shellcheck ci/llgo-wasm-size/run.sh`. The fake compiler tests exercise
required/optional failures and WASM headers; they do not substitute for the
real six-configuration matrix.
