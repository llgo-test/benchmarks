# LLGo binary-size CI

The workflow builds a small Bent subset in six configurations:

1. native Go;
2. LLGo without LTO;
3. LLGo without LTO and with Go deadcode drop enabled;
4. LLGo full LTO with GlobalDCE disabled;
5. LLGo full LTO with GlobalDCE enabled;
6. LLGo full LTO, GlobalDCE, and the MethodByName LTO plugin.

The Bent suites include `toml`, `aws_restjson`, `dustin_humanize` (its
`BenchmarkParseBigBytes` case), `k8s_workqueue`, `uber_zap`, `gorm_schema`,
`etcdctl`, `XGo`, and `iXGo`. These cover widely used AWS SDK,
human-readable byte parsing, Kubernetes, Uber, GORM, the etcd command-line client,
and the Go+ toolchain. The GORM schema package is a real MethodByName consumer: its
package-global readonly `callbackTypes` slice supplies the callback names used
by `reflect.Value.MethodByName`. It therefore exercises the plugin through the
same `go test -c` path as the other test-mode results.
The etcdctl case sets `BuildMode = "build"` and exercises the new `go build` /
`llgo build` path against `go.etcd.io/etcd/etcdctl/v3`. All configurations use
Bent's configured build concurrency.

Every benchmark/configuration pair is built exactly once. Each configuration
first prewarms the standard-library packages required by the selected suites.
Every measured build then receives a private copy of that seed, so it can reuse
the standard library but cannot reuse module dependencies or target packages
compiled by an earlier pair. Native Go and LLGo follow the same cache policy;
the workflow also disables setup-go's cross-run build-cache restore. LLGo's
package-cache fingerprint still separates the LTO and plugin configurations.
The required suite set explicitly includes `dustin_humanize`'s `BenchmarkParseBigBytes`; the
report fails instead of silently publishing a partial result if any required
suite is absent.

`llgo-version.env` supplies the default pinned LLGo, Go, LLVM, and TinyGo
versions for branch and manual runs. The workflow also runs when Bent itself changes, so its
compiler integration remains covered. The workflow stores a Markdown summary
and TSV result as an artifact. The summary also contains Bent's native per-case
build timings; `build-times.tsv`, `timing-summary.md`, `download-timings.log`,
and raw `.build` files are retained for diagnosing slow downloads or builds.
The pinned LLVM toolchain is installed from the versioned apt.llvm.org
repository after its signing-key fingerprint is checked.
The dashboard treats Bent's `user + sys` time as the comparable build-time
metric. Wall time remains visible as a reference because concurrent builds and
runner scheduling can make it unsuitable for commit-to-commit comparisons.
The published dashboard presents wall time as its primary human-facing duration
and retains `user + sys` as secondary diagnostic context. Binary size and wall
time use separate commit matrices on the same page; each cell is ranked against
the other build modes for the same benchmark and commit, with smaller values
receiving the stronger favorable background. Matrix rows are visually grouped
by benchmark: the benchmark name appears once at the start of its build modes,
and a full-width separator marks the next benchmark. The row set is the union
of every published run, so a historical benchmark remains visible with `—` in
commit columns where it was not produced.

The `llgo-main-updated` repository-dispatch event from `xgo-dev/llgo` starts a
binary-size build directly with the complete dispatched SHA. A separate,
coalescible job updates `LLGO_COMMIT` on the benchmarks `main` branch to the
current LLGo main tip; coalescing that bookkeeping cannot discard a benchmark
revision. Distinct LLGo commits use distinct build concurrency keys, so a burst
of merges may run in parallel but every LLGo `main` update retains a comparable
data point. GitHub requires the receiver workflow to be on the benchmarks
repository's default branch before it can receive this event.
The workflow sources `timing.sh` for its shared CI step timing output.
Bent schedules benchmark/configuration builds serially; each LLGo invocation
uses the compiler's own package-level parallelism.


## Publishing and history

The workflow keeps Bent's native benchsize files, the existing Markdown summary, and TSV report in the uploaded artifact. It also emits results.json as a small publication index derived from those native records; the raw files remain the source for detailed inspection.

For pushes to `main`, LLGo merge dispatches, and manual runs from `main`, the
workflow copies the structured result into the pages branch. The Pages root is
the Go/TinyGo/LLGo WASM application-size comparison. The previous Linux ELF size and
build-time history lives at `linux.html`, where readers can compare any two runs
by benchmark and configuration. Pull requests use the lightweight Go-only
validation job described below; they do not produce a binary-size artifact or
modify the history.
Existing published runs load their retained `build-times.tsv` directly, while
new `results.json` documents also embed the same timing fields for each cell.
New documents additionally record runner metadata for the prominent
environment strip. Commit-to-commit deltas remain hidden until the reader
enables comparison and selects two commit columns.

Changes that only touch the dashboard source or its publication scripts use the
separate `llgo-binary-size-pages.yml` workflow. That path publishes the updated
site directly without rebuilding benchmarks, and its publication jobs are
restricted to `main`; pull-request builds cannot publish Pages.

The benchmark and page-only workflows use separate concurrency keys. Pages
publication retries from the latest `pages` tip if parallel benchmark runs
finish together. The index records each result's position on LLGo's first-parent
`main` history and displays commits in that order rather than build completion
order; the dashboard keeps the newest commits on the first page and orders its
columns newest to oldest. Trend charts reverse that selection for chronological
left-to-right display.

Pull requests that change the committed LLGo version, Bent, the LLGo-size
benchmark/configuration files, or the suite definitions used by those cases
run the full six-way matrix and upload the `llgo-binary-size` artifact for
review. They do not publish history. A PR outside that scope uses the separate
Go-only validation job, so dependency acquisition, compilation, and execution
remain checked without rebuilding LLGo or the five LLGo binary-size variants.

Published history is keyed by the full LLGo commit, so rerunning one commit
updates its existing entry instead of adding another build-round entry.

The same full benchmark job also runs the applications under `ci/llgo-wasm-size` and
publishes their compact results in the same Pages commit. See that directory's
README for the shared-toolchain protocol and the explicit LLVM 22 compatibility
flag. Full WASM binaries and compiler logs remain in the workflow artifact;
Pages stores only JSON, TSV, and Markdown results.

### First-time repository setup

The first publisher run creates the `pages` branch automatically. Before that
run, configure the repository's Pages source as **GitHub Actions** and allow
workflows to write repository contents. In `xgo-dev/llgo`, configure
`BENCHMARKS_DISPATCH_TOKEN` with permission to dispatch to
`xgo-dev/benchmarks`; this token is required only by the small sender workflow
that runs after `main` advances.
