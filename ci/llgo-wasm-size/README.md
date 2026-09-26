# Go, TinyGo, and LLGo WASM application-size CI

This benchmark builds twelve command-line applications for `wasip1/wasm` or `js/wasm` with
the native Go compiler, TinyGo, and LLGo, then compares the final `.wasm` file
sizes. These are application workloads rather than single-package probes. The
suite covers image convolution, JSON processing, SHA-256, a streaming Base64
codec, multi-hash checksums, recursive computation, regular-expression and
wildcard filters, an HTML path report, Unicode-aware text statistics, and Go
package import/type metadata processing, and the TypeScript Go compiler.

External applications are **not stored in this repository**. `apps.tsv` records
an HTTPS repository URL, a full commit SHA, and the upstream command directory
or Go entry file. `prepare_sources.py` fetches that exact commit at test time,
checks the resolved HEAD and clean working tree, and builds directly from the
upstream checkout. The original source, `go.mod`, and `go.sum` are not rewritten.
The six local fixtures remain under `apps/`.

See [`THIRD_PARTY.md`](THIRD_PARTY.md) for the external repositories and entries.
Fibonacci's upstream has no Go module, so its original `main.go` is built as a
file argument without synthesizing a module. The other commands use their
original modules and command-package paths.

All compilers use the same Go toolchain **for a given application**. The default
is `GO_VERSION` from `ci/llgo-size/llgo-version.env`; an explicit `go_version` in
`apps.tsv` handles an upstream module that requires a newer release. The `goos` column selects the host per application (old manifests default to `wasip1`). Each
result records the application's Go version, repository, commit, and entry.
The Go toolchain is fixed through `GOTOOLCHAIN`, and `GOFLAGS=-mod=readonly`
prevents automatic module edits. The runner disables ambient Go workspaces and
checks that external checkouts remain unchanged after every build.

`llimport` keeps upstream's Go 1.27.0 requirement. Go and all four LLGo builds
are required. TinyGo 0.41.1 supports Go through 1.26, so it is attempted as an
optional build; the incompatibility produces a missing value and a compiler
log. Ordinary package imports spawn an external `go` command, which WASI cannot
run. Usage output and importing `unsafe` are limited runtime smoke checks,
not a claim of complete package-import functionality under WASI.

The newer toolchain needed to build LLGo itself is pinned separately as
`LLGO_BUILD_GO_VERSION`. Go uses `-trimpath -ldflags='-s -w'`, TinyGo uses
`-opt=z -no-debug`, and LLGo uses `-Oz` with the pinned LLVM 22 toolchain.
TinyGo's Binaryen 132 is pinned independently of LLGo's Emscripten 4.0.21
`wasm-opt`, which supplies Asyncify and exception translation.

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
WASI requests `-Oz` for LLVM and Binaryen. JS keeps the LLGo `-Oz` flag but
uses the upstream Emscripten driver for post-link processing. At LLGo
`4dbedca26aaa`, the observed JS Binaryen invocation uses `-O2` with Asyncify;
this benchmark does not override that driver-selected level.
Put the pinned Binaryen's `bin` directory before TinyGo's `bin` on `PATH`:
the Linux TinyGo release bundles an older `wasm-opt`. The runner verifies the
resolved Binaryen version so this cannot silently change the baseline.
`report.py` is the source of truth for flags and records the complete protocol.
No LTO pass plugin is used for WASM.

`apps.tsv` explicitly declares TinyGo as `required` or `optional`. Existing
TinyGo-compatible applications remain required. Optional builds are still
attempted: compiler failure or invalid WASM output leaves a `null` value,
`failed` build status, and a compiler log. Go and all LLGo configurations are
required. A failed build does not stop later configurations or applications.
After all builds, the runner writes the complete report and returns failure
if any required build failed. CI preserves artifacts, runs the native Bent
matrix, and publishes available results before reporting the overall failure.
Optional TinyGo failures do not fail the job. Invalid or stale output files
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

## WASI and JS/WASM views

The existing WASI views compare Go and TinyGo against four LLGo modes.
The two JS/WASM views (`js-wasm.html` and `js-wasm-tinygo.html`) use the
same applications, source revisions, entries, and compiler configurations,
plus `tsgo`. Each page filters tables, trends, and geometric means by target;
historical rows without target metadata remain WASI-only.

`tsgo` downloads microsoft/TypeScript at
`c975de5011fb7dfb32a491cf3fcf02d4f811f50e` and builds the original
`tsc/cmd/tsc` entry in its unchanged nested module with Go 1.27.0.
It follows the same build-size measurement and presentation as every other
application, with no application-specific runtime checks. TinyGo is optional,
as for llimport, because 0.41.1 does not support Go 1.27.

All four LLGo configurations retain `-Oz`. Local no-LTO qualification on
LLGo `4dbedca26aaa` produced a 96,005,826-byte JS/WASM artifact in 781 seconds.
This does not establish success of the other configurations or runtime
correctness. For JS targets, LLGo emits `.mjs` plus `.wasm`; measurements
count only the final `.wasm`, with both retained in the CI artifact.

Builds run serially in the existing job (there is no parallel configuration
matrix). `GOFLAGS=-mod=readonly -p=1`, `GOMAXPROCS=2`, and `BINARYEN_CORES=2`
limit concurrency. They do not guarantee that a single optimization task will
fit in runner RAM. Each compiler invocation has a 1200-second process-group
timeout via the existing `ci/llgo-size/bin/llgo-build-timeout` wrapper
(`LLGO_BUILD_TIMEOUT_SECONDS`), shared with the native size task. Successful, failed, and timed-out builds
remain distinct. Missing sizes are null, later configurations still run, logs
and exit codes are archived, and required failures/timeouts fail the task after
the partial report is written. The existing workflow publishes partial reports.

### Isolated tsgo runner

The `standard` suite builds the other 22 WASI/JS applications and all existing
Linux benchmarks. The `tsgo` suite builds only tsgo's six WASM configurations
on a separate runner. Both call the same reusable workflow, with independent
artifact upload, publication, and Pages deployment; neither waits for the
other. `WASM_SUITE` selects rows from the shared manifest. Publication replaces
only that suite's rows for the LLGo revision, preserving the other suite's
results regardless of completion order. A lost tsgo runner cannot prevent the
standard suite from publishing. No size or failure is fabricated when a runner
is lost before it produces a report.
