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
| llimport | TinyGo | optional | failed | [logs/llimport.TinyGo.log](logs/llimport.TinyGo.log) |
| llimport-js | TinyGo | optional | failed | [logs/llimport-js.TinyGo.log](logs/llimport-js.TinyGo.log) |

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
| LLGo · no LTO | 0.941x | 11 |
| LLGo · deadcode drop | 0.538x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.854x | 11 |
| LLGo · full LTO + GlobalDCE | 0.576x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1902891 | -18.1% |
| `base64` | 2322402 | LLGo · deadcode drop | 1025562 | -55.8% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1682304 | -27.6% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1071086 | -53.9% |
| `checksum` | 2311672 | LLGo · no LTO | 1882315 | -18.6% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1011321 | -56.3% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1645771 | -28.8% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1037064 | -55.1% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2751724 | +4.3% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1476827 | -44.0% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2534377 | -3.9% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1589765 | -39.7% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1683500 | -26.0% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 902926 | -60.3% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1470960 | -35.3% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 974142 | -57.2% |
| `grep` | 2871426 | LLGo · no LTO | 2560706 | -10.8% |
| `grep` | 2871426 | LLGo · deadcode drop | 1524074 | -46.9% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2257728 | -21.4% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1566713 | -45.4% |
| `glob` | 2305059 | LLGo · no LTO | 1932391 | -16.2% |
| `glob` | 2305059 | LLGo · deadcode drop | 1031370 | -55.3% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1788515 | -22.4% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1157025 | -49.8% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4043810 | +21.1% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2188608 | -34.4% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3773094 | +13.0% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2492122 | -25.3% |
| `llimport` | 8440671 | LLGo · no LTO | 11047998 | +30.9% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9069057 | +7.4% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10100258 | +19.7% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 8976282 | +6.3% |
| `path-report` | 2428068 | LLGo · no LTO | 2265316 | -6.7% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1349058 | -44.4% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 2111223 | -13.0% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1471092 | -39.4% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3068852 | +9.2% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1749990 | -37.7% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2855140 | +1.6% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1900381 | -32.4% |
| `word-count` | 2300998 | LLGo · no LTO | 1892716 | -17.7% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1007034 | -56.2% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1747798 | -24.0% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1124348 | -51.1% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.764x | 10 |
| LLGo · deadcode drop | 6.485x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.677x | 10 |
| LLGo · full LTO + GlobalDCE | 7.003x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1902891 | +1004.4% |
| `base64` | 172302 | LLGo · deadcode drop | 1025562 | +495.2% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1682304 | +876.4% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1071086 | +521.6% |
| `checksum` | 169609 | LLGo · no LTO | 1882315 | +1009.8% |
| `checksum` | 169609 | LLGo · deadcode drop | 1011321 | +496.3% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1645771 | +870.3% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1037064 | +511.4% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2751724 | +1563.8% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1476827 | +793.0% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2534377 | +1432.4% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1589765 | +861.3% |
| `fibonacci` | 141855 | LLGo · no LTO | 1683500 | +1086.8% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 902926 | +536.5% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1470960 | +936.9% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 974142 | +586.7% |
| `grep` | 155984 | LLGo · no LTO | 2560706 | +1541.6% |
| `grep` | 155984 | LLGo · deadcode drop | 1524074 | +877.1% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2257728 | +1347.4% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1566713 | +904.4% |
| `glob` | 136553 | LLGo · no LTO | 1932391 | +1315.1% |
| `glob` | 136553 | LLGo · deadcode drop | 1031370 | +655.3% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1788515 | +1209.8% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1157025 | +747.3% |
| `json-wasi` | 525666 | LLGo · no LTO | 4043810 | +669.3% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2188608 | +316.3% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3773094 | +617.8% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2492122 | +374.1% |
| `llimport` | — | LLGo · no LTO | 11047998 | — |
| `llimport` | — | LLGo · deadcode drop | 9069057 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10100258 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 8976282 | — |
| `path-report` | 194133 | LLGo · no LTO | 2265316 | +1066.9% |
| `path-report` | 194133 | LLGo · deadcode drop | 1349058 | +594.9% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 2111223 | +987.5% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1471092 | +657.8% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3068852 | +771.9% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1749990 | +397.2% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2855140 | +711.2% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1900381 | +439.9% |
| `word-count` | 164053 | LLGo · no LTO | 1892716 | +1053.7% |
| `word-count` | 164053 | LLGo · deadcode drop | 1007034 | +513.8% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1747798 | +965.4% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1124348 | +585.4% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.566x | 11 |
| LLGo · deadcode drop | 0.286x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.495x | 11 |
| LLGo · full LTO + GlobalDCE | 0.342x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1076263 | -52.7% |
| `base64` | 2275731 | LLGo · deadcode drop | 496164 | -78.2% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 848141 | -62.7% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 564179 | -75.2% |
| `checksum` | 2264417 | LLGo · no LTO | 1059957 | -53.2% |
| `checksum` | 2264417 | LLGo · deadcode drop | 483294 | -78.7% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 832187 | -63.2% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 545205 | -75.9% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 1660348 | -36.3% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 794619 | -69.5% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1546880 | -40.7% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 953634 | -63.4% |
| `fibonacci` | 2230899 | LLGo · no LTO | 870638 | -61.0% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 398103 | -82.2% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 736868 | -67.0% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 498321 | -77.7% |
| `grep` | 2848917 | LLGo · no LTO | 1512897 | -46.9% |
| `grep` | 2848917 | LLGo · deadcode drop | 825012 | -71.0% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1334400 | -53.2% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 941745 | -66.9% |
| `glob` | 2257634 | LLGo · no LTO | 1091406 | -51.7% |
| `glob` | 2257634 | LLGo · deadcode drop | 489965 | -78.3% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 983687 | -56.4% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 651639 | -71.1% |
| `json-wasi` | 3314587 | LLGo · no LTO | 2675183 | -19.3% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1312001 | -60.4% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2463695 | -25.7% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1611797 | -51.4% |
| `llimport` | 8423078 | LLGo · no LTO | 8044147 | -4.5% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6507005 | -22.7% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 6887166 | -18.2% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6627275 | -21.3% |
| `path-report` | 2381190 | LLGo · no LTO | 1324578 | -44.4% |
| `path-report` | 2381190 | LLGo · deadcode drop | 711762 | -70.1% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1209032 | -49.2% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 871393 | -63.4% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1849511 | -33.5% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 952998 | -65.7% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1719239 | -38.2% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1124307 | -59.6% |
| `word-count` | 2253620 | LLGo · no LTO | 1072682 | -52.4% |
| `word-count` | 2253620 | LLGo · deadcode drop | 482022 | -78.6% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 938511 | -58.4% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 636243 | -71.8% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 9.163x | 10 |
| LLGo · deadcode drop | 4.423x | 10 |
| LLGo · full LTO (GlobalDCE off) | 8.024x | 10 |
| LLGo · full LTO + GlobalDCE | 5.362x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1076263 | +1012.3% |
| `base64` | 96760 | LLGo · deadcode drop | 496164 | +412.8% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 848141 | +776.5% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 564179 | +483.1% |
| `checksum` | 92685 | LLGo · no LTO | 1059957 | +1043.6% |
| `checksum` | 92685 | LLGo · deadcode drop | 483294 | +421.4% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 832187 | +797.9% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 545205 | +488.2% |
| `conv-wasi` | 201149 | LLGo · no LTO | 1660348 | +725.4% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 794619 | +295.0% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1546880 | +669.0% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 953634 | +374.1% |
| `fibonacci` | 62386 | LLGo · no LTO | 870638 | +1295.6% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 398103 | +538.1% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 736868 | +1081.1% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 498321 | +698.8% |
| `grep` | 303772 | LLGo · no LTO | 1512897 | +398.0% |
| `grep` | 303772 | LLGo · deadcode drop | 825012 | +171.6% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1334400 | +339.3% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 941745 | +210.0% |
| `glob` | 93153 | LLGo · no LTO | 1091406 | +1071.6% |
| `glob` | 93153 | LLGo · deadcode drop | 489965 | +426.0% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 983687 | +956.0% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 651639 | +599.5% |
| `json-wasi` | 493590 | LLGo · no LTO | 2675183 | +442.0% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1312001 | +165.8% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2463695 | +399.1% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1611797 | +226.5% |
| `llimport` | — | LLGo · no LTO | 8044147 | — |
| `llimport` | — | LLGo · deadcode drop | 6507005 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 6887166 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6627275 | — |
| `path-report` | 116889 | LLGo · no LTO | 1324578 | +1033.2% |
| `path-report` | 116889 | LLGo · deadcode drop | 711762 | +508.9% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1209032 | +934.3% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 871393 | +645.5% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1849511 | +543.4% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 952998 | +231.5% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1719239 | +498.1% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1124307 | +291.1% |
| `word-count` | 86834 | LLGo · no LTO | 1072682 | +1135.3% |
| `word-count` | 86834 | LLGo · deadcode drop | 482022 | +455.1% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 938511 | +980.8% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 636243 | +632.7% |
