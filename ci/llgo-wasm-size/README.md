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
three sets of WASM binaries. CI uploads the complete directory as an artifact;
`archive.py` publishes only the compact JSON, Markdown, and TSV files to the
`pages` branch. Published history is keyed by the full LLGo commit, matching the
Linux binary-size history.
