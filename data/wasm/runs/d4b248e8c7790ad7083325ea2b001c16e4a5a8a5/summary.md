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
| LLGo · no LTO | 0.935x | 11 |
| LLGo · deadcode drop | 0.537x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.844x | 11 |
| LLGo · full LTO + GlobalDCE | 0.577x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1890941 | -18.6% |
| `base64` | 2322402 | LLGo · deadcode drop | 1024308 | -55.9% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1659934 | -28.5% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1068187 | -54.0% |
| `checksum` | 2311672 | LLGo · no LTO | 1870728 | -19.1% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1009986 | -56.3% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1623664 | -29.8% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1035291 | -55.2% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2733704 | +3.6% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1471236 | -44.2% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2507126 | -5.0% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1590071 | -39.7% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1671567 | -26.5% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 902261 | -60.3% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1443196 | -36.5% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 980014 | -56.9% |
| `grep` | 2871426 | LLGo · no LTO | 2546479 | -11.3% |
| `grep` | 2871426 | LLGo · deadcode drop | 1521473 | -47.0% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2232452 | -22.3% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1567866 | -45.4% |
| `glob` | 2305059 | LLGo · no LTO | 1920787 | -16.7% |
| `glob` | 2305059 | LLGo · deadcode drop | 1030240 | -55.3% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1766484 | -23.4% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1160906 | -49.6% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4018189 | +20.4% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2179899 | -34.7% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3744737 | +12.2% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2504004 | -25.0% |
| `llimport` | 8440671 | LLGo · no LTO | 10922409 | +29.4% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9041941 | +7.1% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 9971227 | +18.1% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 8901251 | +5.5% |
| `path-report` | 2428068 | LLGo · no LTO | 2253695 | -7.2% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1347760 | -44.5% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 2089213 | -14.0% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1484463 | -38.9% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3049895 | +8.5% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1743931 | -38.0% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2823165 | +0.4% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1900805 | -32.4% |
| `word-count` | 2300998 | LLGo · no LTO | 1881047 | -18.3% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1005841 | -56.3% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1725732 | -25.0% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1128910 | -50.9% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.692x | 10 |
| LLGo · deadcode drop | 6.472x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.547x | 10 |
| LLGo · full LTO + GlobalDCE | 7.020x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1890941 | +997.5% |
| `base64` | 172302 | LLGo · deadcode drop | 1024308 | +494.5% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1659934 | +863.4% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1068187 | +520.0% |
| `checksum` | 169609 | LLGo · no LTO | 1870728 | +1003.0% |
| `checksum` | 169609 | LLGo · deadcode drop | 1009986 | +495.5% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1623664 | +857.3% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1035291 | +510.4% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2733704 | +1552.9% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1471236 | +789.6% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2507126 | +1415.9% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1590071 | +861.4% |
| `fibonacci` | 141855 | LLGo · no LTO | 1671567 | +1078.4% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 902261 | +536.0% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1443196 | +917.4% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 980014 | +590.9% |
| `grep` | 155984 | LLGo · no LTO | 2546479 | +1532.5% |
| `grep` | 155984 | LLGo · deadcode drop | 1521473 | +875.4% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2232452 | +1331.2% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1567866 | +905.1% |
| `glob` | 136553 | LLGo · no LTO | 1920787 | +1306.6% |
| `glob` | 136553 | LLGo · deadcode drop | 1030240 | +654.5% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1766484 | +1193.6% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1160906 | +750.2% |
| `json-wasi` | 525666 | LLGo · no LTO | 4018189 | +664.4% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2179899 | +314.7% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3744737 | +612.4% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2504004 | +376.3% |
| `llimport` | — | LLGo · no LTO | 10922409 | — |
| `llimport` | — | LLGo · deadcode drop | 9041941 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 9971227 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 8901251 | — |
| `path-report` | 194133 | LLGo · no LTO | 2253695 | +1060.9% |
| `path-report` | 194133 | LLGo · deadcode drop | 1347760 | +594.2% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 2089213 | +976.2% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1484463 | +664.7% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3049895 | +766.5% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1743931 | +395.5% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2823165 | +702.1% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1900805 | +440.0% |
| `word-count` | 164053 | LLGo · no LTO | 1881047 | +1046.6% |
| `word-count` | 164053 | LLGo · deadcode drop | 1005841 | +513.1% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1725732 | +951.9% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1128910 | +588.1% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.564x | 11 |
| LLGo · deadcode drop | 0.287x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.488x | 11 |
| LLGo · full LTO + GlobalDCE | 0.343x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1071296 | -52.9% |
| `base64` | 2275731 | LLGo · deadcode drop | 496746 | -78.2% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 834806 | -63.3% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 564826 | -75.2% |
| `checksum` | 2264417 | LLGo · no LTO | 1055199 | -53.4% |
| `checksum` | 2264417 | LLGo · deadcode drop | 483820 | -78.6% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 819057 | -63.8% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 546639 | -75.9% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 1654750 | -36.6% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 794767 | -69.5% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1531473 | -41.3% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 957395 | -63.3% |
| `fibonacci` | 2230899 | LLGo · no LTO | 868849 | -61.1% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 401087 | -82.0% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 722348 | -67.6% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 504089 | -77.4% |
| `grep` | 2848917 | LLGo · no LTO | 1507203 | -47.1% |
| `grep` | 2848917 | LLGo · deadcode drop | 825215 | -71.0% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1315334 | -53.8% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 940462 | -67.0% |
| `glob` | 2257634 | LLGo · no LTO | 1086425 | -51.9% |
| `glob` | 2257634 | LLGo · deadcode drop | 490521 | -78.3% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 968197 | -57.1% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 656557 | -70.9% |
| `json-wasi` | 3314587 | LLGo · no LTO | 2663777 | -19.6% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1311019 | -60.4% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2448672 | -26.1% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1624396 | -51.0% |
| `llimport` | 8423078 | LLGo · no LTO | 7946868 | -5.7% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6496537 | -22.9% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 6788796 | -19.4% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6558647 | -22.1% |
| `path-report` | 2381190 | LLGo · no LTO | 1319706 | -44.6% |
| `path-report` | 2381190 | LLGo · deadcode drop | 712202 | -70.1% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1193705 | -49.9% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 882218 | -63.0% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1843973 | -33.7% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 953225 | -65.7% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1701402 | -38.8% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1128273 | -59.4% |
| `word-count` | 2253620 | LLGo · no LTO | 1067672 | -52.6% |
| `word-count` | 2253620 | LLGo · deadcode drop | 482508 | -78.6% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 925180 | -58.9% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 641657 | -71.5% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 9.128x | 10 |
| LLGo · deadcode drop | 4.429x | 10 |
| LLGo · full LTO (GlobalDCE off) | 7.916x | 10 |
| LLGo · full LTO + GlobalDCE | 5.393x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1071296 | +1007.2% |
| `base64` | 96760 | LLGo · deadcode drop | 496746 | +413.4% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 834806 | +762.8% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 564826 | +483.7% |
| `checksum` | 92685 | LLGo · no LTO | 1055199 | +1038.5% |
| `checksum` | 92685 | LLGo · deadcode drop | 483820 | +422.0% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 819057 | +783.7% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 546639 | +489.8% |
| `conv-wasi` | 201149 | LLGo · no LTO | 1654750 | +722.6% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 794767 | +295.1% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1531473 | +661.4% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 957395 | +376.0% |
| `fibonacci` | 62386 | LLGo · no LTO | 868849 | +1292.7% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 401087 | +542.9% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 722348 | +1057.9% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 504089 | +708.0% |
| `grep` | 303772 | LLGo · no LTO | 1507203 | +396.2% |
| `grep` | 303772 | LLGo · deadcode drop | 825215 | +171.7% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1315334 | +333.0% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 940462 | +209.6% |
| `glob` | 93153 | LLGo · no LTO | 1086425 | +1066.3% |
| `glob` | 93153 | LLGo · deadcode drop | 490521 | +426.6% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 968197 | +939.4% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 656557 | +604.8% |
| `json-wasi` | 493590 | LLGo · no LTO | 2663777 | +439.7% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1311019 | +165.6% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2448672 | +396.1% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1624396 | +229.1% |
| `llimport` | — | LLGo · no LTO | 7946868 | — |
| `llimport` | — | LLGo · deadcode drop | 6496537 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 6788796 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6558647 | — |
| `path-report` | 116889 | LLGo · no LTO | 1319706 | +1029.0% |
| `path-report` | 116889 | LLGo · deadcode drop | 712202 | +509.3% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1193705 | +921.2% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 882218 | +654.7% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1843973 | +541.5% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 953225 | +231.6% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1701402 | +491.9% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1128273 | +292.5% |
| `word-count` | 86834 | LLGo · no LTO | 1067672 | +1129.6% |
| `word-count` | 86834 | LLGo · deadcode drop | 482508 | +455.7% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 925180 | +965.5% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 641657 | +638.9% |
