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
| LLGo · full LTO + GlobalDCE | 0.524x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1669591 | -26.6% |
| `base64` | 2275731 | LLGo · deadcode drop | 1008562 | -55.7% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 1304475 | -42.7% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 910131 | -60.0% |
| `checksum` | 2264417 | LLGo · no LTO | 1646715 | -27.3% |
| `checksum` | 2264417 | LLGo · deadcode drop | 981026 | -56.7% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 1275017 | -43.7% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 877777 | -61.2% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 2798938 | +7.3% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 1631473 | -37.4% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 2349817 | -9.9% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1471067 | -43.6% |
| `fibonacci` | 2230899 | LLGo · no LTO | 1380344 | -38.1% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 905889 | -59.4% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 1109991 | -50.2% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 817183 | -63.4% |
| `grep` | 2848917 | LLGo · no LTO | 2374075 | -16.7% |
| `grep` | 2848917 | LLGo · deadcode drop | 1581224 | -44.5% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1925314 | -32.4% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 1415809 | -50.3% |
| `glob` | 2257634 | LLGo · no LTO | 1837661 | -18.6% |
| `glob` | 2257634 | LLGo · deadcode drop | 1139481 | -49.5% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1466852 | -35.0% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 1029586 | -54.4% |
| `json-wasi` | 3314587 | LLGo · no LTO | 4109588 | +24.0% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 2489965 | -24.9% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 3471378 | +4.7% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 2367923 | -28.6% |
| `llimport` | 8423078 | LLGo · no LTO | 12449463 | +47.8% |
| `llimport` | 8423078 | LLGo · deadcode drop | 10974717 | +30.3% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 8983296 | +6.7% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 8280240 | -1.7% |
| `path-report` | 2381190 | LLGo · no LTO | 2178267 | -8.5% |
| `path-report` | 2381190 | LLGo · deadcode drop | 1471075 | -38.2% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1793662 | -24.7% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 1347254 | -43.4% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 3134390 | +12.7% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1936383 | -30.4% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 2660107 | -4.3% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1766317 | -36.5% |
| `word-count` | 2253620 | LLGo · no LTO | 1798109 | -20.2% |
| `word-count` | 2253620 | LLGo · deadcode drop | 1112994 | -50.6% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 1411077 | -37.4% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 996877 | -55.8% |

## WASM binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 14.816x | 10 |
| LLGo · deadcode drop | 9.240x | 10 |
| LLGo · full LTO (GlobalDCE off) | 12.010x | 10 |
| LLGo · full LTO + GlobalDCE | 8.383x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1669591 | +1625.5% |
| `base64` | 96760 | LLGo · deadcode drop | 1008562 | +942.3% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 1304475 | +1248.2% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 910131 | +840.6% |
| `checksum` | 92685 | LLGo · no LTO | 1646715 | +1676.7% |
| `checksum` | 92685 | LLGo · deadcode drop | 981026 | +958.5% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 1275017 | +1275.6% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 877777 | +847.1% |
| `conv-wasi` | 201149 | LLGo · no LTO | 2798938 | +1291.5% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 1631473 | +711.1% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 2349817 | +1068.2% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1471067 | +631.3% |
| `fibonacci` | 62386 | LLGo · no LTO | 1380344 | +2112.6% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 905889 | +1352.1% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 1109991 | +1679.2% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 817183 | +1209.9% |
| `grep` | 303772 | LLGo · no LTO | 2374075 | +681.5% |
| `grep` | 303772 | LLGo · deadcode drop | 1581224 | +420.5% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1925314 | +533.8% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 1415809 | +366.1% |
| `glob` | 93153 | LLGo · no LTO | 1837661 | +1872.7% |
| `glob` | 93153 | LLGo · deadcode drop | 1139481 | +1123.2% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1466852 | +1474.7% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 1029586 | +1005.3% |
| `json-wasi` | 493590 | LLGo · no LTO | 4109588 | +732.6% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 2489965 | +404.5% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 3471378 | +603.3% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 2367923 | +379.7% |
| `llimport` | — | LLGo · no LTO | 12449463 | — |
| `llimport` | — | LLGo · deadcode drop | 10974717 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 8983296 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 8280240 | — |
| `path-report` | 116889 | LLGo · no LTO | 2178267 | +1763.5% |
| `path-report` | 116889 | LLGo · deadcode drop | 1471075 | +1158.5% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1793662 | +1434.5% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 1347254 | +1052.6% |
| `sha-wasi` | 287449 | LLGo · no LTO | 3134390 | +990.4% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1936383 | +573.6% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 2660107 | +825.4% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1766317 | +514.5% |
| `word-count` | 86834 | LLGo · no LTO | 1798109 | +1970.7% |
| `word-count` | 86834 | LLGo · deadcode drop | 1112994 | +1181.7% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 1411077 | +1525.0% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 996877 | +1048.0% |
