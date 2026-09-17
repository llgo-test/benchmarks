# WASM binary size

`wasip1/wasm`; smaller is better.
Each application uses the same pinned Go toolchain across compilers; per-application versions are recorded below.

- Go: `build -trimpath '-ldflags=-s -w'`
- TinyGo: `build -opt=z -no-debug`
- LLGo · no LTO: `build -a -Oz`
- LLGo · deadcode drop: `build -a -Oz -deadcodedrop`
- LLGo · full LTO (GlobalDCE off): `CCFLAGS='-flto=full' LDFLAGS='-Wl,--lto-O2' build -a -Oz -lto=full -globaldce=false`
- LLGo · full LTO + GlobalDCE: `CCFLAGS='-flto=full -fvirtual-function-elimination -fwhole-program-vtables' LDFLAGS='-Wl,--lto-O2' build -a -Oz -lto=full -globaldce=true`

LLGo uses Emscripten wasm-opt for Asyncify and exception translation;
TinyGo uses its separately pinned Binaryen release.
Failed builds are shown as — and excluded from comparisons; logs are included in the CI artifact.

## Failed builds

| Application | Configuration | Policy | Log |
| --- | --- | --- | --- |
| llimport | TinyGo | optional | [logs/llimport.TinyGo.log](logs/llimport.TinyGo.log) |

| Application | Go toolchain | Source repository | Commit | Entry |
| --- | --- | --- | --- | --- |
| base64 | 1.26.2 | - | - | base64 |
| checksum | 1.26.2 | - | - | checksum |
| convolution | 1.26.2 | https://github.com/universonic/go-rust-wasm-bench.git | 6d1b98c971d6206c313a6d1233d9f2687c50febe | go/cmd/conv-wasi |
| fibonacci | 1.26.2 | https://github.com/mattn/wasi-benchmark.git | c7d73b7b1e03b352791f91ed207c6b9c79559453 | main.go |
| grep | 1.26.2 | - | - | grep |
| glob | 1.26.2 | - | - | glob |
| json-roundtrip | 1.26.2 | https://github.com/universonic/go-rust-wasm-bench.git | 6d1b98c971d6206c313a6d1233d9f2687c50febe | go/cmd/json-wasi |
| llimport | 1.27.0 | https://github.com/goplus/llcppg.git | d62a300b00d567ce2737ab085cef18c06d43f7d7 | cmd/llimport |
| path-report | 1.26.2 | - | - | path-report |
| sha256 | 1.26.2 | https://github.com/universonic/go-rust-wasm-bench.git | 6d1b98c971d6206c313a6d1233d9f2687c50febe | go/cmd/sha-wasi |
| word-count | 1.26.2 | - | - | word-count |

## WASM binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.912x | 11 |
| LLGo · deadcode drop | 0.587x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.731x | 11 |
| LLGo · full LTO + GlobalDCE | 0.523x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1669625 | -26.6% |
| `base64` | 2275731 | LLGo · deadcode drop | 1008596 | -55.7% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 1304509 | -42.7% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 910165 | -60.0% |
| `checksum` | 2264417 | LLGo · no LTO | 1646749 | -27.3% |
| `checksum` | 2264417 | LLGo · deadcode drop | 981060 | -56.7% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 1275051 | -43.7% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 877811 | -61.2% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 2799006 | +7.3% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 1631541 | -37.4% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 2349885 | -9.9% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1464423 | -43.9% |
| `fibonacci` | 2230899 | LLGo · no LTO | 1380378 | -38.1% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 905923 | -59.4% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 1110025 | -50.2% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 816931 | -63.4% |
| `grep` | 2848917 | LLGo · no LTO | 2374109 | -16.7% |
| `grep` | 2848917 | LLGo · deadcode drop | 1581258 | -44.5% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1925348 | -32.4% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 1415555 | -50.3% |
| `glob` | 2257634 | LLGo · no LTO | 1837695 | -18.6% |
| `glob` | 2257634 | LLGo · deadcode drop | 1139515 | -49.5% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1466886 | -35.0% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 1029313 | -54.4% |
| `json-wasi` | 3314587 | LLGo · no LTO | 4109676 | +24.0% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 2490053 | -24.9% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 3471466 | +4.7% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 2367602 | -28.6% |
| `llimport` | 8423078 | LLGo · no LTO | 12449016 | +47.8% |
| `llimport` | 8423078 | LLGo · deadcode drop | 10974270 | +30.3% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 8982064 | +6.6% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 8270687 | -1.8% |
| `path-report` | 2381190 | LLGo · no LTO | 2178301 | -8.5% |
| `path-report` | 2381190 | LLGo · deadcode drop | 1471109 | -38.2% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1793696 | -24.7% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 1347023 | -43.4% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 3134422 | +12.7% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1936415 | -30.4% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 2639698 | -5.1% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1743352 | -37.3% |
| `word-count` | 2253620 | LLGo · no LTO | 1798143 | -20.2% |
| `word-count` | 2253620 | LLGo · deadcode drop | 1113028 | -50.6% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 1411111 | -37.4% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 996644 | -55.8% |

## WASM binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 14.817x | 10 |
| LLGo · deadcode drop | 9.240x | 10 |
| LLGo · full LTO (GlobalDCE off) | 12.001x | 10 |
| LLGo · full LTO + GlobalDCE | 8.368x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1669625 | +1625.5% |
| `base64` | 96760 | LLGo · deadcode drop | 1008596 | +942.4% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 1304509 | +1248.2% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 910165 | +840.6% |
| `checksum` | 92685 | LLGo · no LTO | 1646749 | +1676.7% |
| `checksum` | 92685 | LLGo · deadcode drop | 981060 | +958.5% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 1275051 | +1275.7% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 877811 | +847.1% |
| `conv-wasi` | 201149 | LLGo · no LTO | 2799006 | +1291.5% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 1631541 | +711.1% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 2349885 | +1068.2% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1464423 | +628.0% |
| `fibonacci` | 62386 | LLGo · no LTO | 1380378 | +2112.6% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 905923 | +1352.1% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 1110025 | +1679.3% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 816931 | +1209.5% |
| `grep` | 303772 | LLGo · no LTO | 2374109 | +681.5% |
| `grep` | 303772 | LLGo · deadcode drop | 1581258 | +420.5% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1925348 | +533.8% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 1415555 | +366.0% |
| `glob` | 93153 | LLGo · no LTO | 1837695 | +1872.8% |
| `glob` | 93153 | LLGo · deadcode drop | 1139515 | +1123.3% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1466886 | +1474.7% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 1029313 | +1005.0% |
| `json-wasi` | 493590 | LLGo · no LTO | 4109676 | +732.6% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 2490053 | +404.5% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 3471466 | +603.3% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 2367602 | +379.7% |
| `llimport` | — | LLGo · no LTO | 12449016 | — |
| `llimport` | — | LLGo · deadcode drop | 10974270 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 8982064 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 8270687 | — |
| `path-report` | 116889 | LLGo · no LTO | 2178301 | +1763.6% |
| `path-report` | 116889 | LLGo · deadcode drop | 1471109 | +1158.6% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1793696 | +1434.5% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 1347023 | +1052.4% |
| `sha-wasi` | 287449 | LLGo · no LTO | 3134422 | +990.4% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1936415 | +573.7% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 2639698 | +818.3% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1743352 | +506.5% |
| `word-count` | 86834 | LLGo · no LTO | 1798143 | +1970.8% |
| `word-count` | 86834 | LLGo · deadcode drop | 1113028 | +1181.8% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 1411111 | +1525.1% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 996644 | +1047.8% |
