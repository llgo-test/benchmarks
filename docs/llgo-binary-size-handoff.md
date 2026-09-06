# LLGo Binary-Size CI & Pages

## Goals and Repositories

- Official repository: `llgo-test/benchmarks`
- Official working branch: `main`
- Personal testing repository: `zhouguangyuan0718/benchmarks` (only the historical run records below are kept here)
- History/site source branch: `pages`
- Dashboard URL: https://llgo-test.github.io/benchmarks/ (available after the first deployment)
- Goal: for every update to the exact commit on `xgo-dev/llgo:main`, build binary sizes, persist the JSON results, and browse/compare them on Pages.

## Current Status Snapshot

The table below lists the verified run records from the personal testing phase. The official repository accumulates its own history independently, starting from its first successful publish.

| Run | Commit | Status | Notes |
| --- | --- | --- | --- |
| [#15](https://github.com/zhouguangyuan0718/benchmarks/actions/runs/29910425368) | [40bedb5](https://github.com/zhouguangyuan0718/benchmarks/commit/40bedb5b4bbd48e9ed0d3b46ed9219a8ba24639a) | success | Confirmed the LLVM/Clang version fix works. |
| [#16](https://github.com/zhouguangyuan0718/benchmarks/actions/runs/29917227390) | [9f49cb9](https://github.com/zhouguangyuan0718/benchmarks/commit/9f49cb91f9c319a4aeaf6ed36dd918e4ce4575d6) | success | Jekyll Pages migration verified. |
| [#17](https://github.com/zhouguangyuan0718/benchmarks/actions/runs/29917749490) | [7fbe18a](https://github.com/zhouguangyuan0718/benchmarks/commit/7fbe18ad2ab96146c036a1a463dd3779961c601a) | cancelled | Proactively stopped before a new commit was pushed. |
| [#18](https://github.com/zhouguangyuan0718/benchmarks/actions/runs/29923518473) | [6563c96](https://github.com/zhouguangyuan0718/benchmarks/commit/6563c9658a0d1486d4b266126e31bbdfde71ed5b) | success | All five configuration builds and the Pages deployment succeeded; results confirmed Sarama was missing. |

The workflow sets `concurrency.group: llgo-binary-size-pages` with `cancel-in-progress: false`, so runs on the same branch publish their Pages history serially.

## CI Structure

Entry workflow: [.github/workflows/llgo-binary-size.yml](../.github/workflows/llgo-binary-size.yml)

1. Reads the default LLGo, Go, and LLVM versions from [ci/llgo-size/llgo-version.env](../ci/llgo-size/llgo-version.env); a cross-repo event from LLGo `main` first updates this pin, then explicitly triggers one build and Pages publish.
2. Installs LLVM 19 and builds the LLGo command and the LTO plugin.
3. Uses Bent to run Go plus 5 LLGo configurations for each suite, producing `benchsize`'s JSON/TSV/raw files. Bent schedules these builds serially; each LLGo invocation uses the compiler's own package-level parallelism.
4. [report.sh](../ci/llgo-size/report.sh) collates the results along with build/download timing.
5. [publish.sh](../ci/llgo-size/publish.sh) archives the results to `pages/data/runs/<run>-<attempt>/` and updates `data/index.json`.
6. The `deploy-pages` job checks out the `pages` branch, builds it with Jekyll, and deploys via the GitHub Pages artifact.

When only the dashboard source or the page-publishing script is changed, the binary-size build is not triggered; a separate `llgo-binary-size-pages.yml` workflow refreshes the `pages` branch directly and deploys the site. Both this workflow and the publish job of the main workflow are restricted to `main`. Ordinary PRs only run the Go-configuration case validation; if a PR modifies `llgo-version.env`, the full LLGo binary-size matrix runs and the artifact is uploaded for developer reference, but neither type of PR publishes to Pages.
The two workflows use independent concurrency queues, so a page refresh does not preempt a pending binary-size build.
The history directory and index now use the full LLGo commit as the key, rather than the Actions run number, as the history identifier.

Core files:

- [Bent suites](../cmd/bent/configs/benchmarks-llgo-size.toml)
- [Six compilation configurations](../cmd/bent/configs/configurations-llgo-size.toml)
- [Result publishing script](../ci/llgo-size/publish.sh)
- [Workflow timing helper](../ci/llgo-size/timing.sh)
- [Dashboard page](../ci/llgo-size/site/index.html)
- [Dashboard script](../ci/llgo-size/site/app.js)
- [Jekyll config](../ci/llgo-size/site/_config.yml)

## Current Benchmark Set

- `toml`
- `aws_restjson`
- `dustin_humanize` (`BenchmarkParseBigBytes`)
- `k8s_workqueue`
- `uber_zap`
- `gorm_schema`

`hugo_hugolib` was removed in [7fbe18a](https://github.com/zhouguangyuan0718/benchmarks/commit/7fbe18ad2ab96146c036a1a463dd3779961c601a): it made the LTO build stage significantly slower. Sarama was silently disabled by Bent in #18, and has now been replaced with `dustin_humanize`, which has been verified to build and produce `benchsize` output.

## Key Issues Resolved

### Bent's `go env` output swallowed by the timing wrapper

Commit: [061cfcc](https://github.com/zhouguangyuan0718/benchmarks/commit/061cfcc70861eebae800a962053e600f7402ae9f)

Bent runs `go env GOROOT GOVERSION` and reads its stdout. The earlier download-timing wrapper redirected the output of every `go` subcommand, causing `go env returned 1 values for 2 variables`. The wrapper now only logs `go get`; all other commands `exec` the real Go binary directly.

### LLVM 19 bitcode read by an LLVM 18 linker

Commit: [40bedb5](https://github.com/zhouguangyuan0718/benchmarks/commit/40bedb5b4bbd48e9ed0d3b46ed9219a8ba24639a)

Failure signature:

```
Invalid attribute group entry (Producer: 'LLVM19.1.1' Reader: 'LLVM 18.1.3')
```

The workflow now installs `clang-19` and prepends `/usr/lib/llvm-19/bin` to PATH. The log prints the selected `llvm-config` and `clang++` versions. Verified successful in #15.

## Jekyll Pages Migration

Commit: [9f49cb9](https://github.com/zhouguangyuan0718/benchmarks/commit/9f49cb91f9c319a4aeaf6ed36dd918e4ce4575d6)

- The `pages` branch continues to hold the site source and accumulated data; it is not a one-off build artifact.
- The publish script copies `_config.yml` and removes the old `.nojekyll`.
- The new job uses `actions/configure-pages@v5`, `actions/jekyll-build-pages@v1`, `actions/upload-pages-artifact@v4`, and `actions/deploy-pages@v4`.

This deployment pipeline has been verified in the personal testing repository. Before the official repository's first run, **Settings → Pages → Build and deployment → Source** must be set to **GitHub Actions**; the publish script will automatically create the first `pages` branch.

## Follow-up Recommendations

1. After configuring `BENCHMARKS_DISPATCH_TOKEN` in `xgo-dev/llgo`, monitor the run automatically triggered by each `main` update: it will pin to the corresponding commit and require complete results for all six cases.
2. If a run fails, first check the failed step in its `binary-size` job and the `[toolchain]`, `[timing]`, and `[bent-download]` lines in the logs.
3. After success, check whether a new run appears on the Pages dashboard and compare it against the previous historical result.
5. If further time reduction is still needed, use `build-times.tsv` and `timing-summary.md` first to identify the slowest suite, then replace that single suite; do not remove any of the six compilation configurations, as doing so would reduce the comparative value of Go deadcode drop, LTO, and GlobalDCE.

## Common Troubleshooting Entry Points

- Actions list: https://github.com/llgo-test/benchmarks/actions
- Pages dashboard: https://llgo-test.github.io/benchmarks/
- Pages history index: https://llgo-test.github.io/benchmarks/data/index.json
- GitHub Pages custom workflow documentation: https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages
