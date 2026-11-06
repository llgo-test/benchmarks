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
| LLGo · deadcode drop | 0.536x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.844x | 11 |
| LLGo · full LTO + GlobalDCE | 0.577x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1891030 | -18.6% |
| `base64` | 2322402 | LLGo · deadcode drop | 1023577 | -55.9% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1660028 | -28.5% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1068177 | -54.0% |
| `checksum` | 2311672 | LLGo · no LTO | 1870858 | -19.1% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1009305 | -56.3% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1623659 | -29.8% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1035272 | -55.2% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2733554 | +3.6% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1471032 | -44.2% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2506379 | -5.0% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1590636 | -39.7% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1672267 | -26.5% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 902115 | -60.3% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1443810 | -36.5% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 980568 | -56.9% |
| `grep` | 2871426 | LLGo · no LTO | 2546587 | -11.3% |
| `grep` | 2871426 | LLGo · deadcode drop | 1521287 | -47.0% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2232404 | -22.3% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1568399 | -45.4% |
| `glob` | 2305059 | LLGo · no LTO | 1920947 | -16.7% |
| `glob` | 2305059 | LLGo · deadcode drop | 1030142 | -55.3% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1766509 | -23.4% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1161474 | -49.6% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4018005 | +20.4% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2179770 | -34.7% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3744626 | +12.2% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2504676 | -25.0% |
| `llimport` | 8440671 | LLGo · no LTO | 10913994 | +29.3% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9033781 | +7.0% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 9969694 | +18.1% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 8900013 | +5.4% |
| `path-report` | 2428068 | LLGo · no LTO | 2253847 | -7.2% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1347642 | -44.5% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 2089261 | -14.0% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1485037 | -38.8% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3049679 | +8.5% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1743734 | -38.0% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2823060 | +0.4% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1901479 | -32.4% |
| `word-count` | 2300998 | LLGo · no LTO | 1881150 | -18.2% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1005680 | -56.3% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1725756 | -25.0% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1129476 | -50.9% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.693x | 10 |
| LLGo · deadcode drop | 6.470x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.547x | 10 |
| LLGo · full LTO + GlobalDCE | 7.022x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1891030 | +997.5% |
| `base64` | 172302 | LLGo · deadcode drop | 1023577 | +494.1% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1660028 | +863.4% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1068177 | +519.9% |
| `checksum` | 169609 | LLGo · no LTO | 1870858 | +1003.0% |
| `checksum` | 169609 | LLGo · deadcode drop | 1009305 | +495.1% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1623659 | +857.3% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1035272 | +510.4% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2733554 | +1552.8% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1471032 | +789.5% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2506379 | +1415.5% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1590636 | +861.8% |
| `fibonacci` | 141855 | LLGo · no LTO | 1672267 | +1078.9% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 902115 | +535.9% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1443810 | +917.8% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 980568 | +591.2% |
| `grep` | 155984 | LLGo · no LTO | 2546587 | +1532.6% |
| `grep` | 155984 | LLGo · deadcode drop | 1521287 | +875.3% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2232404 | +1331.2% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1568399 | +905.5% |
| `glob` | 136553 | LLGo · no LTO | 1920947 | +1306.7% |
| `glob` | 136553 | LLGo · deadcode drop | 1030142 | +654.4% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1766509 | +1193.6% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1161474 | +750.6% |
| `json-wasi` | 525666 | LLGo · no LTO | 4018005 | +664.4% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2179770 | +314.7% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3744626 | +612.4% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2504676 | +376.5% |
| `llimport` | — | LLGo · no LTO | 10913994 | — |
| `llimport` | — | LLGo · deadcode drop | 9033781 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 9969694 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 8900013 | — |
| `path-report` | 194133 | LLGo · no LTO | 2253847 | +1061.0% |
| `path-report` | 194133 | LLGo · deadcode drop | 1347642 | +594.2% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 2089261 | +976.2% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1485037 | +665.0% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3049679 | +766.5% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1743734 | +395.4% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2823060 | +702.1% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1901479 | +440.2% |
| `word-count` | 164053 | LLGo · no LTO | 1881150 | +1046.7% |
| `word-count` | 164053 | LLGo · deadcode drop | 1005680 | +513.0% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1725756 | +952.0% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1129476 | +588.5% |

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
| `conv-wasi` | 2608089 | LLGo · no LTO | 1654467 | -36.6% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 794823 | -69.5% |
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
| `json-wasi` | 3314587 | LLGo · no LTO | 2663346 | -19.6% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1311068 | -60.4% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2448348 | -26.1% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1624914 | -51.0% |
| `llimport` | 8423078 | LLGo · no LTO | 7940267 | -5.7% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6490490 | -22.9% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 6787393 | -19.4% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6557324 | -22.2% |
| `path-report` | 2381190 | LLGo · no LTO | 1319875 | -44.6% |
| `path-report` | 2381190 | LLGo · deadcode drop | 712321 | -70.1% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1193839 | -49.9% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 882794 | -62.9% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1843697 | -33.7% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 953293 | -65.7% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1701168 | -38.8% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1128809 | -59.4% |
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
| `conv-wasi` | 201149 | LLGo · no LTO | 1654467 | +722.5% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 794823 | +295.1% |
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
| `json-wasi` | 493590 | LLGo · no LTO | 2663346 | +439.6% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1311068 | +165.6% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2448348 | +396.0% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1624914 | +229.2% |
| `llimport` | — | LLGo · no LTO | 7940267 | — |
| `llimport` | — | LLGo · deadcode drop | 6490490 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 6787393 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6557324 | — |
| `path-report` | 116889 | LLGo · no LTO | 1319875 | +1029.2% |
| `path-report` | 116889 | LLGo · deadcode drop | 712321 | +509.4% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1193839 | +921.3% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 882794 | +655.2% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1843697 | +541.4% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 953293 | +231.6% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1701168 | +491.8% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1128809 | +292.7% |
| `word-count` | 86834 | LLGo · no LTO | 1067848 | +1129.8% |
| `word-count` | 86834 | LLGo · deadcode drop | 482668 | +455.9% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 925294 | +965.6% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 642213 | +639.6% |
