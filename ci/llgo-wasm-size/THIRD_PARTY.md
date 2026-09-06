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
