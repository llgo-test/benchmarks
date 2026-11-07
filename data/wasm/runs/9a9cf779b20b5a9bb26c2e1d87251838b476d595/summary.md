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
| `base64` | 2322402 | LLGo · no LTO | 1891122 | -18.6% |
| `base64` | 2322402 | LLGo · deadcode drop | 1023687 | -55.9% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1660130 | -28.5% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1068268 | -54.0% |
| `checksum` | 2311672 | LLGo · no LTO | 1870956 | -19.1% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1009396 | -56.3% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1623761 | -29.8% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1035366 | -55.2% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2733650 | +3.6% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1471118 | -44.2% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2506514 | -5.0% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1590762 | -39.7% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1672376 | -26.5% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 902224 | -60.3% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1443911 | -36.5% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 980674 | -56.9% |
| `grep` | 2871426 | LLGo · no LTO | 2546685 | -11.3% |
| `grep` | 2871426 | LLGo · deadcode drop | 1521387 | -47.0% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2232541 | -22.2% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1568467 | -45.4% |
| `glob` | 2305059 | LLGo · no LTO | 1921057 | -16.7% |
| `glob` | 2305059 | LLGo · deadcode drop | 1030245 | -55.3% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1766627 | -23.4% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1161572 | -49.6% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4017919 | +20.4% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2179845 | -34.7% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3744743 | +12.2% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2504811 | -25.0% |
| `llimport` | 8440671 | LLGo · no LTO | 10914067 | +29.3% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9033856 | +7.0% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 9969196 | +18.1% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 8899473 | +5.4% |
| `path-report` | 2428068 | LLGo · no LTO | 2253936 | -7.2% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1347742 | -44.5% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 2089363 | -13.9% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1485123 | -38.8% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3049770 | +8.5% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1743794 | -38.0% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2822628 | +0.4% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1901045 | -32.4% |
| `word-count` | 2300998 | LLGo · no LTO | 1881260 | -18.2% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1005776 | -56.3% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1725846 | -25.0% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1129577 | -50.9% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.693x | 10 |
| LLGo · deadcode drop | 6.471x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.548x | 10 |
| LLGo · full LTO + GlobalDCE | 7.023x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1891122 | +997.6% |
| `base64` | 172302 | LLGo · deadcode drop | 1023687 | +494.1% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1660130 | +863.5% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1068268 | +520.0% |
| `checksum` | 169609 | LLGo · no LTO | 1870956 | +1003.1% |
| `checksum` | 169609 | LLGo · deadcode drop | 1009396 | +495.1% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1623761 | +857.4% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1035366 | +510.4% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2733650 | +1552.9% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1471118 | +789.5% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2506514 | +1415.6% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1590762 | +861.9% |
| `fibonacci` | 141855 | LLGo · no LTO | 1672376 | +1078.9% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 902224 | +536.0% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1443911 | +917.9% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 980674 | +591.3% |
| `grep` | 155984 | LLGo · no LTO | 2546685 | +1532.7% |
| `grep` | 155984 | LLGo · deadcode drop | 1521387 | +875.3% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2232541 | +1331.3% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1568467 | +905.5% |
| `glob` | 136553 | LLGo · no LTO | 1921057 | +1306.8% |
| `glob` | 136553 | LLGo · deadcode drop | 1030245 | +654.5% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1766627 | +1193.7% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1161572 | +750.6% |
| `json-wasi` | 525666 | LLGo · no LTO | 4017919 | +664.3% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2179845 | +314.7% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3744743 | +612.4% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2504811 | +376.5% |
| `llimport` | — | LLGo · no LTO | 10914067 | — |
| `llimport` | — | LLGo · deadcode drop | 9033856 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 9969196 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 8899473 | — |
| `path-report` | 194133 | LLGo · no LTO | 2253936 | +1061.0% |
| `path-report` | 194133 | LLGo · deadcode drop | 1347742 | +594.2% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 2089363 | +976.3% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1485123 | +665.0% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3049770 | +766.5% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1743794 | +395.4% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2822628 | +701.9% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1901045 | +440.1% |
| `word-count` | 164053 | LLGo · no LTO | 1881260 | +1046.7% |
| `word-count` | 164053 | LLGo · deadcode drop | 1005776 | +513.1% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1725846 | +952.0% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1129577 | +588.5% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.564x | 11 |
| LLGo · deadcode drop | 0.287x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.488x | 11 |
| LLGo · full LTO + GlobalDCE | 0.343x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1071469 | -52.9% |
| `base64` | 2275731 | LLGo · deadcode drop | 496487 | -78.2% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 834931 | -63.3% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 564972 | -75.2% |
| `checksum` | 2264417 | LLGo · no LTO | 1055375 | -53.4% |
| `checksum` | 2264417 | LLGo · deadcode drop | 483544 | -78.6% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 819166 | -63.8% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 546777 | -75.9% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 1654542 | -36.6% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 794898 | -69.5% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1531227 | -41.3% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 957891 | -63.3% |
| `fibonacci` | 2230899 | LLGo · no LTO | 869412 | -61.0% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 401231 | -82.0% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 722843 | -67.6% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 504613 | -77.4% |
| `grep` | 2848917 | LLGo · no LTO | 1507215 | -47.1% |
| `grep` | 2848917 | LLGo · deadcode drop | 825194 | -71.0% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1315294 | -53.8% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 940872 | -67.0% |
| `glob` | 2257634 | LLGo · no LTO | 1086610 | -51.9% |
| `glob` | 2257634 | LLGo · deadcode drop | 490690 | -78.3% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 968309 | -57.1% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 657111 | -70.9% |
| `json-wasi` | 3314587 | LLGo · no LTO | 2663421 | -19.6% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1311143 | -60.4% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2448348 | -26.1% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1624914 | -51.0% |
| `llimport` | 8423078 | LLGo · no LTO | 7940334 | -5.7% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6490541 | -22.9% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 6787513 | -19.4% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6557444 | -22.1% |
| `path-report` | 2381190 | LLGo · no LTO | 1319875 | -44.6% |
| `path-report` | 2381190 | LLGo · deadcode drop | 712321 | -70.1% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1193839 | -49.9% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 882794 | -62.9% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1843748 | -33.7% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 953344 | -65.7% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1701271 | -38.8% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1128912 | -59.4% |
| `word-count` | 2253620 | LLGo · no LTO | 1067848 | -52.6% |
| `word-count` | 2253620 | LLGo · deadcode drop | 482668 | -78.6% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 925294 | -58.9% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 642213 | -71.5% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 9.129x | 10 |
| LLGo · deadcode drop | 4.429x | 10 |
| LLGo · full LTO (GlobalDCE off) | 7.917x | 10 |
| LLGo · full LTO + GlobalDCE | 5.396x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1071469 | +1007.3% |
| `base64` | 96760 | LLGo · deadcode drop | 496487 | +413.1% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 834931 | +762.9% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 564972 | +483.9% |
| `checksum` | 92685 | LLGo · no LTO | 1055375 | +1038.7% |
| `checksum` | 92685 | LLGo · deadcode drop | 483544 | +421.7% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 819166 | +783.8% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 546777 | +489.9% |
| `conv-wasi` | 201149 | LLGo · no LTO | 1654542 | +722.5% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 794898 | +295.2% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1531227 | +661.2% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 957891 | +376.2% |
| `fibonacci` | 62386 | LLGo · no LTO | 869412 | +1293.6% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 401231 | +543.1% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 722843 | +1058.7% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 504613 | +708.9% |
| `grep` | 303772 | LLGo · no LTO | 1507215 | +396.2% |
| `grep` | 303772 | LLGo · deadcode drop | 825194 | +171.6% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1315294 | +333.0% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 940872 | +209.7% |
| `glob` | 93153 | LLGo · no LTO | 1086610 | +1066.5% |
| `glob` | 93153 | LLGo · deadcode drop | 490690 | +426.8% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 968309 | +939.5% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 657111 | +605.4% |
| `json-wasi` | 493590 | LLGo · no LTO | 2663421 | +439.6% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1311143 | +165.6% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2448348 | +396.0% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1624914 | +229.2% |
| `llimport` | — | LLGo · no LTO | 7940334 | — |
| `llimport` | — | LLGo · deadcode drop | 6490541 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 6787513 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6557444 | — |
| `path-report` | 116889 | LLGo · no LTO | 1319875 | +1029.2% |
| `path-report` | 116889 | LLGo · deadcode drop | 712321 | +509.4% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1193839 | +921.3% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 882794 | +655.2% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1843748 | +541.4% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 953344 | +231.7% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1701271 | +491.9% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1128912 | +292.7% |
| `word-count` | 86834 | LLGo · no LTO | 1067848 | +1129.8% |
| `word-count` | 86834 | LLGo · deadcode drop | 482668 | +455.9% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 925294 | +965.6% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 642213 | +639.6% |
