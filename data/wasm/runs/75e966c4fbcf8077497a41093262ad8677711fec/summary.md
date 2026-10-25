# WASM binary size

Per-application WASM host (wasip1 or js); smaller is better. JS glue is excluded.
Each application uses the same pinned Go toolchain across compilers; per-application versions are recorded below.

- Go: `build -trimpath '-ldflags=-s -w'`
- TinyGo: `build -opt=z -no-debug`
- LLGo · no LTO: `build -a -Oz`
- LLGo · deadcode drop: `build -a -Oz -deadcodedrop`
- LLGo · full LTO (GlobalDCE off): `CCFLAGS='-flto=full' LDFLAGS='-Wl,--lto-O2' build -a -Oz -lto=full -globaldce=false`
- LLGo · full LTO + GlobalDCE: `CCFLAGS='-flto=full -fvirtual-function-elimination -fwhole-program-vtables' LDFLAGS='-Wl,--lto-O2' build -a -Oz -lto=full -globaldce=true`

LLGo uses target-specific upstream Emscripten/Binaryen processing; see the recorded protocol.
TinyGo uses its separately pinned Binaryen release.
Failed builds are shown as — and excluded from comparisons; logs are included in the CI artifact.

## Failed builds

| Application | Configuration | Policy | Status | Log |
| --- | --- | --- | --- | --- |
| base64 | LLGoNoLTO | required | failed | [logs/base64.LLGoNoLTO.log](logs/base64.LLGoNoLTO.log) |
| base64 | LLGoDeadcodeDrop | required | failed | [logs/base64.LLGoDeadcodeDrop.log](logs/base64.LLGoDeadcodeDrop.log) |
| base64 | LLGoFullLTONoGlobalDCE | required | failed | [logs/base64.LLGoFullLTONoGlobalDCE.log](logs/base64.LLGoFullLTONoGlobalDCE.log) |
| base64 | LLGoFullLTOGlobalDCE | required | failed | [logs/base64.LLGoFullLTOGlobalDCE.log](logs/base64.LLGoFullLTOGlobalDCE.log) |
| checksum | LLGoNoLTO | required | failed | [logs/checksum.LLGoNoLTO.log](logs/checksum.LLGoNoLTO.log) |
| checksum | LLGoDeadcodeDrop | required | failed | [logs/checksum.LLGoDeadcodeDrop.log](logs/checksum.LLGoDeadcodeDrop.log) |
| checksum | LLGoFullLTONoGlobalDCE | required | failed | [logs/checksum.LLGoFullLTONoGlobalDCE.log](logs/checksum.LLGoFullLTONoGlobalDCE.log) |
| checksum | LLGoFullLTOGlobalDCE | required | failed | [logs/checksum.LLGoFullLTOGlobalDCE.log](logs/checksum.LLGoFullLTOGlobalDCE.log) |
| convolution | LLGoNoLTO | required | failed | [logs/convolution.LLGoNoLTO.log](logs/convolution.LLGoNoLTO.log) |
| convolution | LLGoDeadcodeDrop | required | failed | [logs/convolution.LLGoDeadcodeDrop.log](logs/convolution.LLGoDeadcodeDrop.log) |
| convolution | LLGoFullLTONoGlobalDCE | required | failed | [logs/convolution.LLGoFullLTONoGlobalDCE.log](logs/convolution.LLGoFullLTONoGlobalDCE.log) |
| convolution | LLGoFullLTOGlobalDCE | required | failed | [logs/convolution.LLGoFullLTOGlobalDCE.log](logs/convolution.LLGoFullLTOGlobalDCE.log) |
| fibonacci | LLGoNoLTO | required | failed | [logs/fibonacci.LLGoNoLTO.log](logs/fibonacci.LLGoNoLTO.log) |
| fibonacci | LLGoDeadcodeDrop | required | failed | [logs/fibonacci.LLGoDeadcodeDrop.log](logs/fibonacci.LLGoDeadcodeDrop.log) |
| fibonacci | LLGoFullLTONoGlobalDCE | required | failed | [logs/fibonacci.LLGoFullLTONoGlobalDCE.log](logs/fibonacci.LLGoFullLTONoGlobalDCE.log) |
| fibonacci | LLGoFullLTOGlobalDCE | required | failed | [logs/fibonacci.LLGoFullLTOGlobalDCE.log](logs/fibonacci.LLGoFullLTOGlobalDCE.log) |
| grep | LLGoNoLTO | required | failed | [logs/grep.LLGoNoLTO.log](logs/grep.LLGoNoLTO.log) |
| grep | LLGoDeadcodeDrop | required | failed | [logs/grep.LLGoDeadcodeDrop.log](logs/grep.LLGoDeadcodeDrop.log) |
| grep | LLGoFullLTONoGlobalDCE | required | failed | [logs/grep.LLGoFullLTONoGlobalDCE.log](logs/grep.LLGoFullLTONoGlobalDCE.log) |
| grep | LLGoFullLTOGlobalDCE | required | failed | [logs/grep.LLGoFullLTOGlobalDCE.log](logs/grep.LLGoFullLTOGlobalDCE.log) |
| glob | LLGoNoLTO | required | failed | [logs/glob.LLGoNoLTO.log](logs/glob.LLGoNoLTO.log) |
| glob | LLGoDeadcodeDrop | required | failed | [logs/glob.LLGoDeadcodeDrop.log](logs/glob.LLGoDeadcodeDrop.log) |
| glob | LLGoFullLTONoGlobalDCE | required | failed | [logs/glob.LLGoFullLTONoGlobalDCE.log](logs/glob.LLGoFullLTONoGlobalDCE.log) |
| glob | LLGoFullLTOGlobalDCE | required | failed | [logs/glob.LLGoFullLTOGlobalDCE.log](logs/glob.LLGoFullLTOGlobalDCE.log) |
| json-roundtrip | LLGoNoLTO | required | failed | [logs/json-roundtrip.LLGoNoLTO.log](logs/json-roundtrip.LLGoNoLTO.log) |
| json-roundtrip | LLGoDeadcodeDrop | required | failed | [logs/json-roundtrip.LLGoDeadcodeDrop.log](logs/json-roundtrip.LLGoDeadcodeDrop.log) |
| json-roundtrip | LLGoFullLTONoGlobalDCE | required | failed | [logs/json-roundtrip.LLGoFullLTONoGlobalDCE.log](logs/json-roundtrip.LLGoFullLTONoGlobalDCE.log) |
| json-roundtrip | LLGoFullLTOGlobalDCE | required | failed | [logs/json-roundtrip.LLGoFullLTOGlobalDCE.log](logs/json-roundtrip.LLGoFullLTOGlobalDCE.log) |
| llimport | TinyGo | optional | failed | [logs/llimport.TinyGo.log](logs/llimport.TinyGo.log) |
| llimport | LLGoNoLTO | required | failed | [logs/llimport.LLGoNoLTO.log](logs/llimport.LLGoNoLTO.log) |
| llimport | LLGoDeadcodeDrop | required | failed | [logs/llimport.LLGoDeadcodeDrop.log](logs/llimport.LLGoDeadcodeDrop.log) |
| llimport | LLGoFullLTONoGlobalDCE | required | failed | [logs/llimport.LLGoFullLTONoGlobalDCE.log](logs/llimport.LLGoFullLTONoGlobalDCE.log) |
| llimport | LLGoFullLTOGlobalDCE | required | failed | [logs/llimport.LLGoFullLTOGlobalDCE.log](logs/llimport.LLGoFullLTOGlobalDCE.log) |
| path-report | LLGoNoLTO | required | failed | [logs/path-report.LLGoNoLTO.log](logs/path-report.LLGoNoLTO.log) |
| path-report | LLGoDeadcodeDrop | required | failed | [logs/path-report.LLGoDeadcodeDrop.log](logs/path-report.LLGoDeadcodeDrop.log) |
| path-report | LLGoFullLTONoGlobalDCE | required | failed | [logs/path-report.LLGoFullLTONoGlobalDCE.log](logs/path-report.LLGoFullLTONoGlobalDCE.log) |
| path-report | LLGoFullLTOGlobalDCE | required | failed | [logs/path-report.LLGoFullLTOGlobalDCE.log](logs/path-report.LLGoFullLTOGlobalDCE.log) |
| sha256 | LLGoNoLTO | required | failed | [logs/sha256.LLGoNoLTO.log](logs/sha256.LLGoNoLTO.log) |
| sha256 | LLGoDeadcodeDrop | required | failed | [logs/sha256.LLGoDeadcodeDrop.log](logs/sha256.LLGoDeadcodeDrop.log) |
| sha256 | LLGoFullLTONoGlobalDCE | required | failed | [logs/sha256.LLGoFullLTONoGlobalDCE.log](logs/sha256.LLGoFullLTONoGlobalDCE.log) |
| sha256 | LLGoFullLTOGlobalDCE | required | failed | [logs/sha256.LLGoFullLTOGlobalDCE.log](logs/sha256.LLGoFullLTOGlobalDCE.log) |
| word-count | LLGoNoLTO | required | failed | [logs/word-count.LLGoNoLTO.log](logs/word-count.LLGoNoLTO.log) |
| word-count | LLGoDeadcodeDrop | required | failed | [logs/word-count.LLGoDeadcodeDrop.log](logs/word-count.LLGoDeadcodeDrop.log) |
| word-count | LLGoFullLTONoGlobalDCE | required | failed | [logs/word-count.LLGoFullLTONoGlobalDCE.log](logs/word-count.LLGoFullLTONoGlobalDCE.log) |
| word-count | LLGoFullLTOGlobalDCE | required | failed | [logs/word-count.LLGoFullLTOGlobalDCE.log](logs/word-count.LLGoFullLTOGlobalDCE.log) |
| base64-js | LLGoNoLTO | required | failed | [logs/base64-js.LLGoNoLTO.log](logs/base64-js.LLGoNoLTO.log) |
| base64-js | LLGoDeadcodeDrop | required | failed | [logs/base64-js.LLGoDeadcodeDrop.log](logs/base64-js.LLGoDeadcodeDrop.log) |
| base64-js | LLGoFullLTONoGlobalDCE | required | failed | [logs/base64-js.LLGoFullLTONoGlobalDCE.log](logs/base64-js.LLGoFullLTONoGlobalDCE.log) |
| base64-js | LLGoFullLTOGlobalDCE | required | failed | [logs/base64-js.LLGoFullLTOGlobalDCE.log](logs/base64-js.LLGoFullLTOGlobalDCE.log) |
| checksum-js | LLGoNoLTO | required | failed | [logs/checksum-js.LLGoNoLTO.log](logs/checksum-js.LLGoNoLTO.log) |
| checksum-js | LLGoDeadcodeDrop | required | failed | [logs/checksum-js.LLGoDeadcodeDrop.log](logs/checksum-js.LLGoDeadcodeDrop.log) |
| checksum-js | LLGoFullLTONoGlobalDCE | required | failed | [logs/checksum-js.LLGoFullLTONoGlobalDCE.log](logs/checksum-js.LLGoFullLTONoGlobalDCE.log) |
| checksum-js | LLGoFullLTOGlobalDCE | required | failed | [logs/checksum-js.LLGoFullLTOGlobalDCE.log](logs/checksum-js.LLGoFullLTOGlobalDCE.log) |
| convolution-js | LLGoNoLTO | required | failed | [logs/convolution-js.LLGoNoLTO.log](logs/convolution-js.LLGoNoLTO.log) |
| convolution-js | LLGoDeadcodeDrop | required | failed | [logs/convolution-js.LLGoDeadcodeDrop.log](logs/convolution-js.LLGoDeadcodeDrop.log) |
| convolution-js | LLGoFullLTONoGlobalDCE | required | failed | [logs/convolution-js.LLGoFullLTONoGlobalDCE.log](logs/convolution-js.LLGoFullLTONoGlobalDCE.log) |
| convolution-js | LLGoFullLTOGlobalDCE | required | failed | [logs/convolution-js.LLGoFullLTOGlobalDCE.log](logs/convolution-js.LLGoFullLTOGlobalDCE.log) |
| fibonacci-js | LLGoNoLTO | required | failed | [logs/fibonacci-js.LLGoNoLTO.log](logs/fibonacci-js.LLGoNoLTO.log) |
| fibonacci-js | LLGoDeadcodeDrop | required | failed | [logs/fibonacci-js.LLGoDeadcodeDrop.log](logs/fibonacci-js.LLGoDeadcodeDrop.log) |
| fibonacci-js | LLGoFullLTONoGlobalDCE | required | failed | [logs/fibonacci-js.LLGoFullLTONoGlobalDCE.log](logs/fibonacci-js.LLGoFullLTONoGlobalDCE.log) |
| fibonacci-js | LLGoFullLTOGlobalDCE | required | failed | [logs/fibonacci-js.LLGoFullLTOGlobalDCE.log](logs/fibonacci-js.LLGoFullLTOGlobalDCE.log) |
| grep-js | LLGoNoLTO | required | failed | [logs/grep-js.LLGoNoLTO.log](logs/grep-js.LLGoNoLTO.log) |
| grep-js | LLGoDeadcodeDrop | required | failed | [logs/grep-js.LLGoDeadcodeDrop.log](logs/grep-js.LLGoDeadcodeDrop.log) |
| grep-js | LLGoFullLTONoGlobalDCE | required | failed | [logs/grep-js.LLGoFullLTONoGlobalDCE.log](logs/grep-js.LLGoFullLTONoGlobalDCE.log) |
| grep-js | LLGoFullLTOGlobalDCE | required | failed | [logs/grep-js.LLGoFullLTOGlobalDCE.log](logs/grep-js.LLGoFullLTOGlobalDCE.log) |
| glob-js | LLGoNoLTO | required | failed | [logs/glob-js.LLGoNoLTO.log](logs/glob-js.LLGoNoLTO.log) |
| glob-js | LLGoDeadcodeDrop | required | failed | [logs/glob-js.LLGoDeadcodeDrop.log](logs/glob-js.LLGoDeadcodeDrop.log) |
| glob-js | LLGoFullLTONoGlobalDCE | required | failed | [logs/glob-js.LLGoFullLTONoGlobalDCE.log](logs/glob-js.LLGoFullLTONoGlobalDCE.log) |
| glob-js | LLGoFullLTOGlobalDCE | required | failed | [logs/glob-js.LLGoFullLTOGlobalDCE.log](logs/glob-js.LLGoFullLTOGlobalDCE.log) |
| json-roundtrip-js | LLGoNoLTO | required | failed | [logs/json-roundtrip-js.LLGoNoLTO.log](logs/json-roundtrip-js.LLGoNoLTO.log) |
| json-roundtrip-js | LLGoDeadcodeDrop | required | failed | [logs/json-roundtrip-js.LLGoDeadcodeDrop.log](logs/json-roundtrip-js.LLGoDeadcodeDrop.log) |
| json-roundtrip-js | LLGoFullLTONoGlobalDCE | required | failed | [logs/json-roundtrip-js.LLGoFullLTONoGlobalDCE.log](logs/json-roundtrip-js.LLGoFullLTONoGlobalDCE.log) |
| json-roundtrip-js | LLGoFullLTOGlobalDCE | required | failed | [logs/json-roundtrip-js.LLGoFullLTOGlobalDCE.log](logs/json-roundtrip-js.LLGoFullLTOGlobalDCE.log) |
| llimport-js | TinyGo | optional | failed | [logs/llimport-js.TinyGo.log](logs/llimport-js.TinyGo.log) |
| llimport-js | LLGoNoLTO | required | failed | [logs/llimport-js.LLGoNoLTO.log](logs/llimport-js.LLGoNoLTO.log) |
| llimport-js | LLGoDeadcodeDrop | required | failed | [logs/llimport-js.LLGoDeadcodeDrop.log](logs/llimport-js.LLGoDeadcodeDrop.log) |
| llimport-js | LLGoFullLTONoGlobalDCE | required | failed | [logs/llimport-js.LLGoFullLTONoGlobalDCE.log](logs/llimport-js.LLGoFullLTONoGlobalDCE.log) |
| llimport-js | LLGoFullLTOGlobalDCE | required | failed | [logs/llimport-js.LLGoFullLTOGlobalDCE.log](logs/llimport-js.LLGoFullLTOGlobalDCE.log) |
| path-report-js | LLGoNoLTO | required | failed | [logs/path-report-js.LLGoNoLTO.log](logs/path-report-js.LLGoNoLTO.log) |
| path-report-js | LLGoDeadcodeDrop | required | failed | [logs/path-report-js.LLGoDeadcodeDrop.log](logs/path-report-js.LLGoDeadcodeDrop.log) |
| path-report-js | LLGoFullLTONoGlobalDCE | required | failed | [logs/path-report-js.LLGoFullLTONoGlobalDCE.log](logs/path-report-js.LLGoFullLTONoGlobalDCE.log) |
| path-report-js | LLGoFullLTOGlobalDCE | required | failed | [logs/path-report-js.LLGoFullLTOGlobalDCE.log](logs/path-report-js.LLGoFullLTOGlobalDCE.log) |
| sha256-js | LLGoNoLTO | required | failed | [logs/sha256-js.LLGoNoLTO.log](logs/sha256-js.LLGoNoLTO.log) |
| sha256-js | LLGoDeadcodeDrop | required | failed | [logs/sha256-js.LLGoDeadcodeDrop.log](logs/sha256-js.LLGoDeadcodeDrop.log) |
| sha256-js | LLGoFullLTONoGlobalDCE | required | failed | [logs/sha256-js.LLGoFullLTONoGlobalDCE.log](logs/sha256-js.LLGoFullLTONoGlobalDCE.log) |
| sha256-js | LLGoFullLTOGlobalDCE | required | failed | [logs/sha256-js.LLGoFullLTOGlobalDCE.log](logs/sha256-js.LLGoFullLTOGlobalDCE.log) |
| word-count-js | LLGoNoLTO | required | failed | [logs/word-count-js.LLGoNoLTO.log](logs/word-count-js.LLGoNoLTO.log) |
| word-count-js | LLGoDeadcodeDrop | required | failed | [logs/word-count-js.LLGoDeadcodeDrop.log](logs/word-count-js.LLGoDeadcodeDrop.log) |
| word-count-js | LLGoFullLTONoGlobalDCE | required | failed | [logs/word-count-js.LLGoFullLTONoGlobalDCE.log](logs/word-count-js.LLGoFullLTONoGlobalDCE.log) |
| word-count-js | LLGoFullLTOGlobalDCE | required | failed | [logs/word-count-js.LLGoFullLTOGlobalDCE.log](logs/word-count-js.LLGoFullLTOGlobalDCE.log) |

| Application | Target | Go toolchain | Source repository | Commit | Entry |
| --- | --- | --- | --- | --- | --- |
| base64 | wasip1/wasm | 1.26.2 | - | - | base64 |
| checksum | wasip1/wasm | 1.26.2 | - | - | checksum |
| convolution | wasip1/wasm | 1.26.2 | https://github.com/universonic/go-rust-wasm-bench.git | 6d1b98c971d6206c313a6d1233d9f2687c50febe | go/cmd/conv-wasi |
| fibonacci | wasip1/wasm | 1.26.2 | https://github.com/mattn/wasi-benchmark.git | c7d73b7b1e03b352791f91ed207c6b9c79559453 | main.go |
| grep | wasip1/wasm | 1.26.2 | - | - | grep |
| glob | wasip1/wasm | 1.26.2 | - | - | glob |
| json-roundtrip | wasip1/wasm | 1.26.2 | https://github.com/universonic/go-rust-wasm-bench.git | 6d1b98c971d6206c313a6d1233d9f2687c50febe | go/cmd/json-wasi |
| llimport | wasip1/wasm | 1.27.0 | https://github.com/goplus/llcppg.git | d62a300b00d567ce2737ab085cef18c06d43f7d7 | cmd/llimport |
| path-report | wasip1/wasm | 1.26.2 | - | - | path-report |
| sha256 | wasip1/wasm | 1.26.2 | https://github.com/universonic/go-rust-wasm-bench.git | 6d1b98c971d6206c313a6d1233d9f2687c50febe | go/cmd/sha-wasi |
| word-count | wasip1/wasm | 1.26.2 | - | - | word-count |
| base64-js | js/wasm | 1.26.2 | - | - | base64 |
| checksum-js | js/wasm | 1.26.2 | - | - | checksum |
| convolution-js | js/wasm | 1.26.2 | https://github.com/universonic/go-rust-wasm-bench.git | 6d1b98c971d6206c313a6d1233d9f2687c50febe | go/cmd/conv-wasi |
| fibonacci-js | js/wasm | 1.26.2 | https://github.com/mattn/wasi-benchmark.git | c7d73b7b1e03b352791f91ed207c6b9c79559453 | main.go |
| grep-js | js/wasm | 1.26.2 | - | - | grep |
| glob-js | js/wasm | 1.26.2 | - | - | glob |
| json-roundtrip-js | js/wasm | 1.26.2 | https://github.com/universonic/go-rust-wasm-bench.git | 6d1b98c971d6206c313a6d1233d9f2687c50febe | go/cmd/json-wasi |
| llimport-js | js/wasm | 1.27.0 | https://github.com/goplus/llcppg.git | d62a300b00d567ce2737ab085cef18c06d43f7d7 | cmd/llimport |
| path-report-js | js/wasm | 1.26.2 | - | - | path-report |
| sha256-js | js/wasm | 1.26.2 | https://github.com/universonic/go-rust-wasm-bench.git | 6d1b98c971d6206c313a6d1233d9f2687c50febe | go/cmd/sha-wasi |
| word-count-js | js/wasm | 1.26.2 | - | - | word-count |

## js/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | — | 0 |
| LLGo · deadcode drop | — | 0 |
| LLGo · full LTO (GlobalDCE off) | — | 0 |
| LLGo · full LTO + GlobalDCE | — | 0 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | — | — |
| `base64` | 2322402 | LLGo · deadcode drop | — | — |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | — | — |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | — | — |
| `checksum` | 2311672 | LLGo · no LTO | — | — |
| `checksum` | 2311672 | LLGo · deadcode drop | — | — |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | — | — |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | — | — |
| `conv-wasi` | 2638493 | LLGo · no LTO | — | — |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | — | — |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | — | — |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | — | — |
| `fibonacci` | 2274375 | LLGo · no LTO | — | — |
| `fibonacci` | 2274375 | LLGo · deadcode drop | — | — |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | — | — |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | — | — |
| `grep` | 2871426 | LLGo · no LTO | — | — |
| `grep` | 2871426 | LLGo · deadcode drop | — | — |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | — | — |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | — | — |
| `glob` | 2305059 | LLGo · no LTO | — | — |
| `glob` | 2305059 | LLGo · deadcode drop | — | — |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | — | — |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | — | — |
| `json-wasi` | 3338360 | LLGo · no LTO | — | — |
| `json-wasi` | 3338360 | LLGo · deadcode drop | — | — |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | — | — |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | — | — |
| `llimport` | 8440671 | LLGo · no LTO | — | — |
| `llimport` | 8440671 | LLGo · deadcode drop | — | — |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | — | — |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | — | — |
| `path-report` | 2428068 | LLGo · no LTO | — | — |
| `path-report` | 2428068 | LLGo · deadcode drop | — | — |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | — | — |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | — | — |
| `sha-wasi` | 2811136 | LLGo · no LTO | — | — |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | — | — |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | — | — |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | — | — |
| `word-count` | 2300998 | LLGo · no LTO | — | — |
| `word-count` | 2300998 | LLGo · deadcode drop | — | — |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | — | — |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | — | — |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | — | 0 |
| LLGo · deadcode drop | — | 0 |
| LLGo · full LTO (GlobalDCE off) | — | 0 |
| LLGo · full LTO + GlobalDCE | — | 0 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | — | — |
| `base64` | 172302 | LLGo · deadcode drop | — | — |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | — | — |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | — | — |
| `checksum` | 169609 | LLGo · no LTO | — | — |
| `checksum` | 169609 | LLGo · deadcode drop | — | — |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | — | — |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | — | — |
| `conv-wasi` | 165385 | LLGo · no LTO | — | — |
| `conv-wasi` | 165385 | LLGo · deadcode drop | — | — |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | — | — |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | — | — |
| `fibonacci` | 141855 | LLGo · no LTO | — | — |
| `fibonacci` | 141855 | LLGo · deadcode drop | — | — |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | — | — |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | — | — |
| `grep` | 155984 | LLGo · no LTO | — | — |
| `grep` | 155984 | LLGo · deadcode drop | — | — |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | — | — |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | — | — |
| `glob` | 136553 | LLGo · no LTO | — | — |
| `glob` | 136553 | LLGo · deadcode drop | — | — |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | — | — |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | — | — |
| `json-wasi` | 525666 | LLGo · no LTO | — | — |
| `json-wasi` | 525666 | LLGo · deadcode drop | — | — |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | — | — |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | — | — |
| `llimport` | — | LLGo · no LTO | — | — |
| `llimport` | — | LLGo · deadcode drop | — | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | — | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | — | — |
| `path-report` | 194133 | LLGo · no LTO | — | — |
| `path-report` | 194133 | LLGo · deadcode drop | — | — |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | — | — |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | — | — |
| `sha-wasi` | 351971 | LLGo · no LTO | — | — |
| `sha-wasi` | 351971 | LLGo · deadcode drop | — | — |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | — | — |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | — | — |
| `word-count` | 164053 | LLGo · no LTO | — | — |
| `word-count` | 164053 | LLGo · deadcode drop | — | — |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | — | — |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | — | — |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | — | 0 |
| LLGo · deadcode drop | — | 0 |
| LLGo · full LTO (GlobalDCE off) | — | 0 |
| LLGo · full LTO + GlobalDCE | — | 0 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | — | — |
| `base64` | 2275731 | LLGo · deadcode drop | — | — |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | — | — |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | — | — |
| `checksum` | 2264417 | LLGo · no LTO | — | — |
| `checksum` | 2264417 | LLGo · deadcode drop | — | — |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | — | — |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | — | — |
| `conv-wasi` | 2608089 | LLGo · no LTO | — | — |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | — | — |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | — | — |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | — | — |
| `fibonacci` | 2230899 | LLGo · no LTO | — | — |
| `fibonacci` | 2230899 | LLGo · deadcode drop | — | — |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | — | — |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | — | — |
| `grep` | 2848917 | LLGo · no LTO | — | — |
| `grep` | 2848917 | LLGo · deadcode drop | — | — |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | — | — |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | — | — |
| `glob` | 2257634 | LLGo · no LTO | — | — |
| `glob` | 2257634 | LLGo · deadcode drop | — | — |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | — | — |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | — | — |
| `json-wasi` | 3314587 | LLGo · no LTO | — | — |
| `json-wasi` | 3314587 | LLGo · deadcode drop | — | — |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | — | — |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | — | — |
| `llimport` | 8423078 | LLGo · no LTO | — | — |
| `llimport` | 8423078 | LLGo · deadcode drop | — | — |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | — | — |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | — | — |
| `path-report` | 2381190 | LLGo · no LTO | — | — |
| `path-report` | 2381190 | LLGo · deadcode drop | — | — |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | — | — |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | — | — |
| `sha-wasi` | 2780972 | LLGo · no LTO | — | — |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | — | — |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | — | — |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | — | — |
| `word-count` | 2253620 | LLGo · no LTO | — | — |
| `word-count` | 2253620 | LLGo · deadcode drop | — | — |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | — | — |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | — | — |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | — | 0 |
| LLGo · deadcode drop | — | 0 |
| LLGo · full LTO (GlobalDCE off) | — | 0 |
| LLGo · full LTO + GlobalDCE | — | 0 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | — | — |
| `base64` | 96760 | LLGo · deadcode drop | — | — |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | — | — |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | — | — |
| `checksum` | 92685 | LLGo · no LTO | — | — |
| `checksum` | 92685 | LLGo · deadcode drop | — | — |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | — | — |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | — | — |
| `conv-wasi` | 201149 | LLGo · no LTO | — | — |
| `conv-wasi` | 201149 | LLGo · deadcode drop | — | — |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | — | — |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | — | — |
| `fibonacci` | 62386 | LLGo · no LTO | — | — |
| `fibonacci` | 62386 | LLGo · deadcode drop | — | — |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | — | — |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | — | — |
| `grep` | 303772 | LLGo · no LTO | — | — |
| `grep` | 303772 | LLGo · deadcode drop | — | — |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | — | — |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | — | — |
| `glob` | 93153 | LLGo · no LTO | — | — |
| `glob` | 93153 | LLGo · deadcode drop | — | — |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | — | — |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | — | — |
| `json-wasi` | 493590 | LLGo · no LTO | — | — |
| `json-wasi` | 493590 | LLGo · deadcode drop | — | — |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | — | — |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | — | — |
| `llimport` | — | LLGo · no LTO | — | — |
| `llimport` | — | LLGo · deadcode drop | — | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | — | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | — | — |
| `path-report` | 116889 | LLGo · no LTO | — | — |
| `path-report` | 116889 | LLGo · deadcode drop | — | — |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | — | — |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | — | — |
| `sha-wasi` | 287449 | LLGo · no LTO | — | — |
| `sha-wasi` | 287449 | LLGo · deadcode drop | — | — |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | — | — |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | — | — |
| `word-count` | 86834 | LLGo · no LTO | — | — |
| `word-count` | 86834 | LLGo · deadcode drop | — | — |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | — | — |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | — | — |
