# Third-party WASM applications

## fibonacci

- Project: [mattn/wasi-benchmark](https://github.com/mattn/wasi-benchmark)
- Revision: [`c7d73b7b1e03b352791f91ed207c6b9c79559453`](https://github.com/mattn/wasi-benchmark/commit/c7d73b7b1e03b352791f91ed207c6b9c79559453)
- Source: [`main.go`](https://github.com/mattn/wasi-benchmark/blob/c7d73b7b1e03b352791f91ed207c6b9c79559453/main.go)
- License: MIT, as declared by the upstream README; a standard MIT license notice is included beside the source snapshot.

`apps/fibonacci/main.go` is a verbatim snapshot of the source above. Keeping
the revision and license in the repository makes the benchmark reproducible
without downloading mutable source during CI.

## convolution, json-roundtrip, and sha256

- Project: [universonic/go-rust-wasm-bench](https://github.com/universonic/go-rust-wasm-bench)
- Revision: [`6d1b98c971d6206c313a6d1233d9f2687c50febe`](https://github.com/universonic/go-rust-wasm-bench/commit/6d1b98c971d6206c313a6d1233d9f2687c50febe)
- Sources: [`go/conv`](https://github.com/universonic/go-rust-wasm-bench/tree/6d1b98c971d6206c313a6d1233d9f2687c50febe/go/conv), [`go/jsonrt`](https://github.com/universonic/go-rust-wasm-bench/tree/6d1b98c971d6206c313a6d1233d9f2687c50febe/go/jsonrt), [`go/sha`](https://github.com/universonic/go-rust-wasm-bench/tree/6d1b98c971d6206c313a6d1233d9f2687c50febe/go/sha), and their `go/cmd/*-wasi` entry points
- License: MIT; the upstream license is retained in the snapshot root.

`apps/external/go-rust-wasm-bench` is a verbatim, minimal snapshot containing
the upstream Go module metadata, three shared implementations, and three WASI
command entry points. Browser, Rust, harness, and generated-result directories
are outside this Go/TinyGo/LLGo size comparison and are not copied.

## llimport

- Project: [goplus/llcppg](https://github.com/goplus/llcppg)
- Revision: [`d62a300b00d567ce2737ab085cef18c06d43f7d7`](https://github.com/goplus/llcppg/commit/d62a300b00d567ce2737ab085cef18c06d43f7d7) (dev)
- Source: [`cmd/llimport/import.go`](https://github.com/goplus/llcppg/blob/d62a300b00d567ce2737ab085cef18c06d43f7d7/cmd/llimport/import.go)
- License: Apache-2.0; the upstream license is retained beside the snapshot.

`apps/external/llcppg/cmd/llimport/import.go` is copied verbatim. The isolated
benchmark module retains its upstream module path and pins the only imported
external dependency, `github.com/goplus/gogen v1.23.5`. Its Go directive uses
the shared benchmark baseline, Go 1.26.2, instead of upstream's Go 1.27.0;
other llcppg commands and their dependencies are outside this snapshot.

This measures the original command and its Go package importer/type-system
dependencies. Importing ordinary packages invokes an external `go` command,
which WASI cannot spawn. A successful WASM build or usage-message smoke test
is not a claim that ordinary package importing works in WASI. Go, TinyGo,
and all four LLGo modes are required; any failed build fails the run.
