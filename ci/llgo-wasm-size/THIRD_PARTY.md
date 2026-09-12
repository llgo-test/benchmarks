# External WASM applications

No external application source or module metadata is archived in this repository.
The executable manifest is [`apps.tsv`](apps.tsv): it records repository URLs,
full commit SHAs, and upstream entries. Tests download those revisions into a
separate temporary source directory; source checkouts are not published as results.

| Applications | Repository | Fixed commit | Upstream entry |
| --- | --- | --- | --- |
| Fibonacci | [mattn/wasi-benchmark](https://github.com/mattn/wasi-benchmark) | `c7d73b7b1e03b352791f91ed207c6b9c79559453` | `main.go` |
| Convolution | [universonic/go-rust-wasm-bench](https://github.com/universonic/go-rust-wasm-bench) | `6d1b98c971d6206c313a6d1233d9f2687c50febe` | `go/cmd/conv-wasi` |
| JSON | same repository | same commit | `go/cmd/json-wasi` |
| SHA-256 | same repository | same commit | `go/cmd/sha-wasi` |
| llimport | [goplus/llcppg](https://github.com/goplus/llcppg) | `d62a300b00d567ce2737ab085cef18c06d43f7d7` | `cmd/llimport` |

Builds use the original entry and module graph. The Git checkout is verified
against the fixed commit, including when reused, and must stay clean after each
compiler invocation. No entry wrappers, generated modules, dependency pruning,
or Go-directive downgrades are applied. Upstream license files remain in their
original repositories and downloaded checkouts.

Fibonacci has no upstream `go.mod`; its `main.go` is passed directly to each
compiler. The convolution, JSON, and SHA-256 commands share one downloaded
checkout and use its root module.

llimport retains its original Go 1.27.0 module and dependencies. Its TinyGo
build is optional because TinyGo 0.41.1 rejects Go 1.27. A failed attempt is
reported as missing with its log, while Go and the four LLGo builds are required.
Ordinary package importing invokes the external `go` command, unavailable in
WASI; size results and limited usage/`unsafe` smoke checks do not imply complete
WASI functionality.
