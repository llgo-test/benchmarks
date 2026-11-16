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
| base64 | LLGoFullLTOGlobalDCE | required | failed | [logs/base64.LLGoFullLTOGlobalDCE.log](logs/base64.LLGoFullLTOGlobalDCE.log) |
| checksum | LLGoFullLTOGlobalDCE | required | failed | [logs/checksum.LLGoFullLTOGlobalDCE.log](logs/checksum.LLGoFullLTOGlobalDCE.log) |
| convolution | LLGoFullLTOGlobalDCE | required | failed | [logs/convolution.LLGoFullLTOGlobalDCE.log](logs/convolution.LLGoFullLTOGlobalDCE.log) |
| fibonacci | LLGoFullLTOGlobalDCE | required | failed | [logs/fibonacci.LLGoFullLTOGlobalDCE.log](logs/fibonacci.LLGoFullLTOGlobalDCE.log) |
| grep | LLGoFullLTOGlobalDCE | required | failed | [logs/grep.LLGoFullLTOGlobalDCE.log](logs/grep.LLGoFullLTOGlobalDCE.log) |
| glob | LLGoFullLTOGlobalDCE | required | failed | [logs/glob.LLGoFullLTOGlobalDCE.log](logs/glob.LLGoFullLTOGlobalDCE.log) |
| json-roundtrip | LLGoFullLTOGlobalDCE | required | failed | [logs/json-roundtrip.LLGoFullLTOGlobalDCE.log](logs/json-roundtrip.LLGoFullLTOGlobalDCE.log) |
| llimport | TinyGo | optional | failed | [logs/llimport.TinyGo.log](logs/llimport.TinyGo.log) |
| llimport | LLGoFullLTOGlobalDCE | required | failed | [logs/llimport.LLGoFullLTOGlobalDCE.log](logs/llimport.LLGoFullLTOGlobalDCE.log) |
| path-report | LLGoFullLTOGlobalDCE | required | failed | [logs/path-report.LLGoFullLTOGlobalDCE.log](logs/path-report.LLGoFullLTOGlobalDCE.log) |
| sha256 | LLGoFullLTOGlobalDCE | required | failed | [logs/sha256.LLGoFullLTOGlobalDCE.log](logs/sha256.LLGoFullLTOGlobalDCE.log) |
| word-count | LLGoFullLTOGlobalDCE | required | failed | [logs/word-count.LLGoFullLTOGlobalDCE.log](logs/word-count.LLGoFullLTOGlobalDCE.log) |
| base64-js | LLGoFullLTOGlobalDCE | required | failed | [logs/base64-js.LLGoFullLTOGlobalDCE.log](logs/base64-js.LLGoFullLTOGlobalDCE.log) |
| checksum-js | LLGoFullLTOGlobalDCE | required | failed | [logs/checksum-js.LLGoFullLTOGlobalDCE.log](logs/checksum-js.LLGoFullLTOGlobalDCE.log) |
| convolution-js | LLGoFullLTOGlobalDCE | required | failed | [logs/convolution-js.LLGoFullLTOGlobalDCE.log](logs/convolution-js.LLGoFullLTOGlobalDCE.log) |
| fibonacci-js | LLGoFullLTOGlobalDCE | required | failed | [logs/fibonacci-js.LLGoFullLTOGlobalDCE.log](logs/fibonacci-js.LLGoFullLTOGlobalDCE.log) |
| grep-js | LLGoFullLTOGlobalDCE | required | failed | [logs/grep-js.LLGoFullLTOGlobalDCE.log](logs/grep-js.LLGoFullLTOGlobalDCE.log) |
| glob-js | LLGoFullLTOGlobalDCE | required | failed | [logs/glob-js.LLGoFullLTOGlobalDCE.log](logs/glob-js.LLGoFullLTOGlobalDCE.log) |
| json-roundtrip-js | LLGoFullLTOGlobalDCE | required | failed | [logs/json-roundtrip-js.LLGoFullLTOGlobalDCE.log](logs/json-roundtrip-js.LLGoFullLTOGlobalDCE.log) |
| llimport-js | TinyGo | optional | failed | [logs/llimport-js.TinyGo.log](logs/llimport-js.TinyGo.log) |
| llimport-js | LLGoFullLTOGlobalDCE | required | failed | [logs/llimport-js.LLGoFullLTOGlobalDCE.log](logs/llimport-js.LLGoFullLTOGlobalDCE.log) |
| path-report-js | LLGoFullLTOGlobalDCE | required | failed | [logs/path-report-js.LLGoFullLTOGlobalDCE.log](logs/path-report-js.LLGoFullLTOGlobalDCE.log) |
| sha256-js | LLGoFullLTOGlobalDCE | required | failed | [logs/sha256-js.LLGoFullLTOGlobalDCE.log](logs/sha256-js.LLGoFullLTOGlobalDCE.log) |
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
| LLGo · no LTO | 0.902x | 11 |
| LLGo · deadcode drop | 0.549x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.823x | 11 |
| LLGo · full LTO + GlobalDCE | — | 0 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1895516 | -18.4% |
| `base64` | 2322402 | LLGo · deadcode drop | 1061682 | -54.3% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1690443 | -27.2% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | — | — |
| `checksum` | 2311672 | LLGo · no LTO | 1876441 | -18.8% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1047094 | -54.7% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1655048 | -28.4% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | — | — |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2753117 | +4.3% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1526297 | -42.2% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2549013 | -3.4% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | — | — |
| `fibonacci` | 2274375 | LLGo · no LTO | 1166991 | -48.7% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 937130 | -58.8% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 978488 | -57.0% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | — | — |
| `grep` | 2871426 | LLGo · no LTO | 2553887 | -11.1% |
| `grep` | 2871426 | LLGo · deadcode drop | 1567654 | -45.4% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2276874 | -20.7% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | — | — |
| `glob` | 2305059 | LLGo · no LTO | 1926933 | -16.4% |
| `glob` | 2305059 | LLGo · deadcode drop | 1066251 | -53.7% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1795231 | -22.1% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | — | — |
| `json-wasi` | 3338360 | LLGo · no LTO | 4060774 | +21.6% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2270510 | -32.0% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3837331 | +14.9% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | — | — |
| `llimport` | 8440671 | LLGo · no LTO | 10956254 | +29.8% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9285819 | +10.0% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10283340 | +21.8% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | — | — |
| `path-report` | 2428068 | LLGo · no LTO | 2070845 | -14.7% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1198038 | -50.7% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 1931160 | -20.5% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | — | — |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3101631 | +10.3% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1831861 | -34.8% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2897413 | +3.1% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | — | — |
| `word-count` | 2300998 | LLGo · no LTO | 1885903 | -18.0% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1042444 | -54.7% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1750250 | -23.9% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | — | — |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.239x | 10 |
| LLGo · deadcode drop | 6.615x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.222x | 10 |
| LLGo · full LTO + GlobalDCE | — | 0 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1895516 | +1000.1% |
| `base64` | 172302 | LLGo · deadcode drop | 1061682 | +516.2% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1690443 | +881.1% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | — | — |
| `checksum` | 169609 | LLGo · no LTO | 1876441 | +1006.3% |
| `checksum` | 169609 | LLGo · deadcode drop | 1047094 | +517.4% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1655048 | +875.8% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | — | — |
| `conv-wasi` | 165385 | LLGo · no LTO | 2753117 | +1564.7% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1526297 | +822.9% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2549013 | +1441.3% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | — | — |
| `fibonacci` | 141855 | LLGo · no LTO | 1166991 | +722.7% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 937130 | +560.6% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 978488 | +589.8% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | — | — |
| `grep` | 155984 | LLGo · no LTO | 2553887 | +1537.3% |
| `grep` | 155984 | LLGo · deadcode drop | 1567654 | +905.0% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2276874 | +1359.7% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | — | — |
| `glob` | 136553 | LLGo · no LTO | 1926933 | +1311.1% |
| `glob` | 136553 | LLGo · deadcode drop | 1066251 | +680.8% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1795231 | +1214.7% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | — | — |
| `json-wasi` | 525666 | LLGo · no LTO | 4060774 | +672.5% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2270510 | +331.9% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3837331 | +630.0% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | — | — |
| `llimport` | — | LLGo · no LTO | 10956254 | — |
| `llimport` | — | LLGo · deadcode drop | 9285819 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10283340 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | — | — |
| `path-report` | 194133 | LLGo · no LTO | 2070845 | +966.7% |
| `path-report` | 194133 | LLGo · deadcode drop | 1198038 | +517.1% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 1931160 | +894.8% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | — | — |
| `sha-wasi` | 351971 | LLGo · no LTO | 3101631 | +781.2% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1831861 | +420.5% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2897413 | +723.2% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | — | — |
| `word-count` | 164053 | LLGo · no LTO | 1885903 | +1049.6% |
| `word-count` | 164053 | LLGo · deadcode drop | 1042444 | +535.4% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1750250 | +966.9% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | — | — |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.544x | 11 |
| LLGo · deadcode drop | 0.301x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.476x | 11 |
| LLGo · full LTO + GlobalDCE | — | 0 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1082220 | -52.4% |
| `base64` | 2275731 | LLGo · deadcode drop | 531997 | -76.6% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 861483 | -62.1% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | — | — |
| `checksum` | 2264417 | LLGo · no LTO | 1067072 | -52.9% |
| `checksum` | 2264417 | LLGo · deadcode drop | 518583 | -77.1% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 845750 | -62.7% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | — | — |
| `conv-wasi` | 2608089 | LLGo · no LTO | 1692837 | -35.1% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 852131 | -67.3% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1582883 | -39.3% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | — | — |
| `fibonacci` | 2230899 | LLGo · no LTO | 565250 | -74.7% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 433796 | -80.6% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 452757 | -79.7% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | — | — |
| `grep` | 2848917 | LLGo · no LTO | 1521209 | -46.6% |
| `grep` | 2848917 | LLGo · deadcode drop | 870024 | -69.5% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1346596 | -52.7% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | — | — |
| `glob` | 2257634 | LLGo · no LTO | 1098549 | -51.3% |
| `glob` | 2257634 | LLGo · deadcode drop | 524017 | -76.8% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 994228 | -56.0% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | — | — |
| `json-wasi` | 3314587 | LLGo · no LTO | 2730513 | -17.6% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1406439 | -57.6% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2550533 | -23.1% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | — | — |
| `llimport` | 8423078 | LLGo · no LTO | 7908144 | -6.1% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6671872 | -20.8% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 6995705 | -16.9% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | — | — |
| `path-report` | 2381190 | LLGo · no LTO | 1217650 | -48.9% |
| `path-report` | 2381190 | LLGo · deadcode drop | 635256 | -73.3% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1107459 | -53.5% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | — | — |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1885483 | -32.2% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1016802 | -63.4% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1760851 | -36.7% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | — | — |
| `word-count` | 2253620 | LLGo · no LTO | 1079098 | -52.1% |
| `word-count` | 2253620 | LLGo · deadcode drop | 517331 | -77.0% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 946147 | -58.0% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | — | — |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 8.780x | 10 |
| LLGo · deadcode drop | 4.654x | 10 |
| LLGo · full LTO (GlobalDCE off) | 7.684x | 10 |
| LLGo · full LTO + GlobalDCE | — | 0 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1082220 | +1018.5% |
| `base64` | 96760 | LLGo · deadcode drop | 531997 | +449.8% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 861483 | +790.3% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | — | — |
| `checksum` | 92685 | LLGo · no LTO | 1067072 | +1051.3% |
| `checksum` | 92685 | LLGo · deadcode drop | 518583 | +459.5% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 845750 | +812.5% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | — | — |
| `conv-wasi` | 201149 | LLGo · no LTO | 1692837 | +741.6% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 852131 | +323.6% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1582883 | +686.9% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | — | — |
| `fibonacci` | 62386 | LLGo · no LTO | 565250 | +806.1% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 433796 | +595.3% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 452757 | +625.7% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | — | — |
| `grep` | 303772 | LLGo · no LTO | 1521209 | +400.8% |
| `grep` | 303772 | LLGo · deadcode drop | 870024 | +186.4% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1346596 | +343.3% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | — | — |
| `glob` | 93153 | LLGo · no LTO | 1098549 | +1079.3% |
| `glob` | 93153 | LLGo · deadcode drop | 524017 | +462.5% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 994228 | +967.3% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | — | — |
| `json-wasi` | 493590 | LLGo · no LTO | 2730513 | +453.2% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1406439 | +184.9% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2550533 | +416.7% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | — | — |
| `llimport` | — | LLGo · no LTO | 7908144 | — |
| `llimport` | — | LLGo · deadcode drop | 6671872 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 6995705 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | — | — |
| `path-report` | 116889 | LLGo · no LTO | 1217650 | +941.7% |
| `path-report` | 116889 | LLGo · deadcode drop | 635256 | +443.5% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1107459 | +847.4% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | — | — |
| `sha-wasi` | 287449 | LLGo · no LTO | 1885483 | +555.9% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1016802 | +253.7% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1760851 | +512.6% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | — | — |
| `word-count` | 86834 | LLGo · no LTO | 1079098 | +1142.7% |
| `word-count` | 86834 | LLGo · deadcode drop | 517331 | +495.8% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 946147 | +989.6% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | — | — |
