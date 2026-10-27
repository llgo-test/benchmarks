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
| base64-js | js/wasm | 1.26.2 | - | - | base64 |
| checksum | wasip1/wasm | 1.26.2 | - | - | checksum |
| checksum-js | js/wasm | 1.26.2 | - | - | checksum |
| convolution | wasip1/wasm | 1.26.2 | https://github.com/universonic/go-rust-wasm-bench.git | 6d1b98c971d6206c313a6d1233d9f2687c50febe | go/cmd/conv-wasi |
| convolution-js | js/wasm | 1.26.2 | https://github.com/universonic/go-rust-wasm-bench.git | 6d1b98c971d6206c313a6d1233d9f2687c50febe | go/cmd/conv-wasi |
| fibonacci | wasip1/wasm | 1.26.2 | https://github.com/mattn/wasi-benchmark.git | c7d73b7b1e03b352791f91ed207c6b9c79559453 | main.go |
| fibonacci-js | js/wasm | 1.26.2 | https://github.com/mattn/wasi-benchmark.git | c7d73b7b1e03b352791f91ed207c6b9c79559453 | main.go |
| glob | wasip1/wasm | 1.26.2 | - | - | glob |
| glob-js | js/wasm | 1.26.2 | - | - | glob |
| grep | wasip1/wasm | 1.26.2 | - | - | grep |
| grep-js | js/wasm | 1.26.2 | - | - | grep |
| json-roundtrip | wasip1/wasm | 1.26.2 | https://github.com/universonic/go-rust-wasm-bench.git | 6d1b98c971d6206c313a6d1233d9f2687c50febe | go/cmd/json-wasi |
| json-roundtrip-js | js/wasm | 1.26.2 | https://github.com/universonic/go-rust-wasm-bench.git | 6d1b98c971d6206c313a6d1233d9f2687c50febe | go/cmd/json-wasi |
| llimport | wasip1/wasm | 1.27.0 | https://github.com/goplus/llcppg.git | d62a300b00d567ce2737ab085cef18c06d43f7d7 | cmd/llimport |
| llimport-js | js/wasm | 1.27.0 | https://github.com/goplus/llcppg.git | d62a300b00d567ce2737ab085cef18c06d43f7d7 | cmd/llimport |
| path-report | wasip1/wasm | 1.26.2 | - | - | path-report |
| path-report-js | js/wasm | 1.26.2 | - | - | path-report |
| sha256 | wasip1/wasm | 1.26.2 | https://github.com/universonic/go-rust-wasm-bench.git | 6d1b98c971d6206c313a6d1233d9f2687c50febe | go/cmd/sha-wasi |
| sha256-js | js/wasm | 1.26.2 | https://github.com/universonic/go-rust-wasm-bench.git | 6d1b98c971d6206c313a6d1233d9f2687c50febe | go/cmd/sha-wasi |
| word-count | wasip1/wasm | 1.26.2 | - | - | word-count |
| word-count-js | js/wasm | 1.26.2 | - | - | word-count |

## js/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.963x | 11 |
| LLGo · deadcode drop | 0.563x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.855x | 11 |
| LLGo · full LTO + GlobalDCE | 0.576x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1902485 | -18.1% |
| `base64` | 2322402 | LLGo · deadcode drop | 1030894 | -55.6% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1683991 | -27.5% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1072632 | -53.8% |
| `checksum` | 2311672 | LLGo · no LTO | 1881946 | -18.6% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1016651 | -56.0% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1647520 | -28.7% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1038506 | -55.1% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2857758 | +8.3% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1590890 | -39.7% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2535101 | -3.9% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1588987 | -39.8% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1683115 | -26.0% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 908268 | -60.1% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1472714 | -35.2% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 975341 | -57.1% |
| `glob` | 2305059 | LLGo · no LTO | 2038698 | -11.6% |
| `glob` | 2305059 | LLGo · deadcode drop | 1142970 | -50.4% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1790286 | -22.3% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1158450 | -49.7% |
| `grep` | 2871426 | LLGo · no LTO | 2576023 | -10.3% |
| `grep` | 2871426 | LLGo · deadcode drop | 1544680 | -46.2% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2258432 | -21.3% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1565502 | -45.5% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4150822 | +24.3% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2299390 | -31.1% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3774597 | +13.1% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2491282 | -25.4% |
| `llimport` | 8440671 | LLGo · no LTO | 11064744 | +31.1% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9117549 | +8.0% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10098391 | +19.6% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 8972509 | +6.3% |
| `path-report` | 2428068 | LLGo · no LTO | 2372158 | -2.3% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1461279 | -39.8% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 2113022 | -13.0% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1472537 | -39.4% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3181218 | +13.2% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1864009 | -33.7% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2855915 | +1.6% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1899730 | -32.4% |
| `word-count` | 2300998 | LLGo · no LTO | 1998980 | -13.1% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1118534 | -51.4% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1749551 | -24.0% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1125752 | -51.1% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 12.073x | 10 |
| LLGo · deadcode drop | 6.820x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.685x | 10 |
| LLGo · full LTO + GlobalDCE | 7.007x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1902485 | +1004.2% |
| `base64` | 172302 | LLGo · deadcode drop | 1030894 | +498.3% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1683991 | +877.3% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1072632 | +522.5% |
| `checksum` | 169609 | LLGo · no LTO | 1881946 | +1009.6% |
| `checksum` | 169609 | LLGo · deadcode drop | 1016651 | +499.4% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1647520 | +871.4% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1038506 | +512.3% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2857758 | +1627.9% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1590890 | +861.9% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2535101 | +1432.8% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1588987 | +860.8% |
| `fibonacci` | 141855 | LLGo · no LTO | 1683115 | +1086.5% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 908268 | +540.3% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1472714 | +938.2% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 975341 | +587.6% |
| `glob` | 136553 | LLGo · no LTO | 2038698 | +1393.0% |
| `glob` | 136553 | LLGo · deadcode drop | 1142970 | +737.0% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1790286 | +1211.1% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1158450 | +748.4% |
| `grep` | 155984 | LLGo · no LTO | 2576023 | +1551.5% |
| `grep` | 155984 | LLGo · deadcode drop | 1544680 | +890.3% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2258432 | +1347.9% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1565502 | +903.6% |
| `json-wasi` | 525666 | LLGo · no LTO | 4150822 | +689.6% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2299390 | +337.4% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3774597 | +618.1% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2491282 | +373.9% |
| `llimport` | — | LLGo · no LTO | 11064744 | — |
| `llimport` | — | LLGo · deadcode drop | 9117549 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10098391 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 8972509 | — |
| `path-report` | 194133 | LLGo · no LTO | 2372158 | +1121.9% |
| `path-report` | 194133 | LLGo · deadcode drop | 1461279 | +652.7% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 2113022 | +988.4% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1472537 | +658.5% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3181218 | +803.8% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1864009 | +429.6% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2855915 | +711.4% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1899730 | +439.7% |
| `word-count` | 164053 | LLGo · no LTO | 1998980 | +1118.5% |
| `word-count` | 164053 | LLGo · deadcode drop | 1118534 | +581.8% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1749551 | +966.5% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1125752 | +586.2% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.598x | 11 |
| LLGo · deadcode drop | 0.315x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.505x | 11 |
| LLGo · full LTO + GlobalDCE | 0.350x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1101381 | -51.6% |
| `base64` | 2275731 | LLGo · deadcode drop | 506662 | -77.7% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 874190 | -61.6% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 585698 | -74.3% |
| `checksum` | 2264417 | LLGo · no LTO | 1085045 | -52.1% |
| `checksum` | 2264417 | LLGo · deadcode drop | 493789 | -78.2% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 858102 | -62.1% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 566634 | -75.0% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 1782156 | -31.7% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 918929 | -64.8% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1565110 | -40.0% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 970144 | -62.8% |
| `fibonacci` | 2230899 | LLGo · no LTO | 895838 | -59.8% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 410528 | -81.6% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 762896 | -65.8% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 519864 | -76.7% |
| `glob` | 2257634 | LLGo · no LTO | 1221113 | -45.9% |
| `glob` | 2257634 | LLGo · deadcode drop | 604099 | -73.2% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1009596 | -55.3% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 673051 | -70.2% |
| `grep` | 2848917 | LLGo · no LTO | 1547489 | -45.7% |
| `grep` | 2848917 | LLGo · deadcode drop | 847640 | -70.2% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1354998 | -52.4% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 957472 | -66.4% |
| `json-wasi` | 3314587 | LLGo · no LTO | 2797521 | -15.6% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1427787 | -56.9% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2481553 | -25.1% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1614699 | -51.3% |
| `llimport` | 8423078 | LLGo · no LTO | 8060045 | -4.3% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6566460 | -22.0% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 6888388 | -18.2% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6625905 | -21.3% |
| `path-report` | 2381190 | LLGo · no LTO | 1454296 | -38.9% |
| `path-report` | 2381190 | LLGo · deadcode drop | 827353 | -65.3% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1235111 | -48.1% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 892789 | -62.5% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1971407 | -29.1% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1077269 | -61.3% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1737598 | -37.5% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1140955 | -59.0% |
| `word-count` | 2253620 | LLGo · no LTO | 1202405 | -46.6% |
| `word-count` | 2253620 | LLGo · deadcode drop | 596076 | -73.6% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 964432 | -57.2% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 657655 | -70.8% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 9.727x | 10 |
| LLGo · deadcode drop | 4.901x | 10 |
| LLGo · full LTO (GlobalDCE off) | 8.199x | 10 |
| LLGo · full LTO + GlobalDCE | 5.502x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1101381 | +1038.3% |
| `base64` | 96760 | LLGo · deadcode drop | 506662 | +423.6% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 874190 | +803.5% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 585698 | +505.3% |
| `checksum` | 92685 | LLGo · no LTO | 1085045 | +1070.7% |
| `checksum` | 92685 | LLGo · deadcode drop | 493789 | +432.8% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 858102 | +825.8% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 566634 | +511.4% |
| `conv-wasi` | 201149 | LLGo · no LTO | 1782156 | +786.0% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 918929 | +356.8% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1565110 | +678.1% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 970144 | +382.3% |
| `fibonacci` | 62386 | LLGo · no LTO | 895838 | +1336.0% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 410528 | +558.0% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 762896 | +1122.9% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 519864 | +733.3% |
| `glob` | 93153 | LLGo · no LTO | 1221113 | +1210.9% |
| `glob` | 93153 | LLGo · deadcode drop | 604099 | +548.5% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1009596 | +983.8% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 673051 | +622.5% |
| `grep` | 303772 | LLGo · no LTO | 1547489 | +409.4% |
| `grep` | 303772 | LLGo · deadcode drop | 847640 | +179.0% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1354998 | +346.1% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 957472 | +215.2% |
| `json-wasi` | 493590 | LLGo · no LTO | 2797521 | +466.8% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1427787 | +189.3% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2481553 | +402.8% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1614699 | +227.1% |
| `llimport` | — | LLGo · no LTO | 8060045 | — |
| `llimport` | — | LLGo · deadcode drop | 6566460 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 6888388 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6625905 | — |
| `path-report` | 116889 | LLGo · no LTO | 1454296 | +1144.2% |
| `path-report` | 116889 | LLGo · deadcode drop | 827353 | +607.8% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1235111 | +956.7% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 892789 | +663.8% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1971407 | +585.8% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1077269 | +274.8% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1737598 | +504.5% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1140955 | +296.9% |
| `word-count` | 86834 | LLGo · no LTO | 1202405 | +1284.7% |
| `word-count` | 86834 | LLGo · deadcode drop | 596076 | +586.5% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 964432 | +1010.7% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 657655 | +657.4% |
