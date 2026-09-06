# LLGo runtime performance

This job compares the pinned Go and LLGo toolchains with Bent. It runs the
checked-in cases five times each with a 500 ms benchmark target, grouped by
benchmark to reduce time-local runner noise, and publishes the raw Bent output,
native benchstat text/CSV, and a structured result used by the
runtime-performance Pages table. Benchstat uses a 90% confidence interval
because its default 95% interval requires at least six samples.

It runs only after the `xgo-dev/llgo` release workflow publishes a new tag and
dispatches the exact tag and commit. Ordinary pushes and pull requests do not
start a performance run.

The selected set contains 68 cases screened on Ubuntu/amd64 from
`benchmarks-100.toml`. Every case compiled and ran with Go, LLGo, and LLGo full
LTO; both LLGo execution-time ratios were within 20x of the Go baseline. The
workflow checks sample completeness but does not fail on a performance
percentage because hosted-runner measurements are not a reliable hard
regression gate.

Each successful release run is stored under `data/performance/runs/<tag>/` on
the `pages` branch. The lightweight `performance.html` view follows benchstat's
layout: Go is the baseline, with LLGo and LLGo full-LTO values, confidence
ranges, deltas, and p-values shown side by side. The Pages root now shows the
WASM size comparison, while `linux.html` retains the Linux binary-size and
build-time history.

The suite versions come from `cmd/bent/configs/suites.toml`. Keep those versions
pinned for comparable history; update them deliberately in a reviewed change.
