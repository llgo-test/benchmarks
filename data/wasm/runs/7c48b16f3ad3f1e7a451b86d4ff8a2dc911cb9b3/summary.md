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
| LLGo · deadcode drop | 0.537x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.855x | 11 |
| LLGo · full LTO + GlobalDCE | 0.577x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1903691 | -18.0% |
| `base64` | 2322402 | LLGo · deadcode drop | 1023497 | -55.9% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1685020 | -27.4% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1073687 | -53.8% |
| `checksum` | 2311672 | LLGo · no LTO | 1883144 | -18.5% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1009243 | -56.3% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1648560 | -28.7% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1039514 | -55.0% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2752042 | +4.3% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1473203 | -44.2% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2536581 | -3.9% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1590274 | -39.7% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1684317 | -25.9% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 900841 | -60.4% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1473751 | -35.2% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 976563 | -57.1% |
| `grep` | 2871426 | LLGo · no LTO | 2560793 | -10.8% |
| `grep` | 2871426 | LLGo · deadcode drop | 1519396 | -47.1% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2259444 | -21.3% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1566507 | -45.4% |
| `glob` | 2305059 | LLGo · no LTO | 1933219 | -16.1% |
| `glob` | 2305059 | LLGo · deadcode drop | 1029340 | -55.3% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1791293 | -22.3% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1159478 | -49.7% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4044080 | +21.1% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2185027 | -34.5% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3775177 | +13.1% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2492642 | -25.3% |
| `llimport` | 8440671 | LLGo · no LTO | 11047454 | +30.9% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9064524 | +7.4% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10099604 | +19.7% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 8973621 | +6.3% |
| `path-report` | 2428068 | LLGo · no LTO | 2266139 | -6.7% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1346906 | -44.5% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 2114007 | -12.9% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1473538 | -39.3% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3069192 | +9.2% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1746377 | -37.9% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2857279 | +1.6% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1900894 | -32.4% |
| `word-count` | 2300998 | LLGo · no LTO | 1893516 | -17.7% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1004871 | -56.3% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1750578 | -23.9% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1126776 | -51.0% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.768x | 10 |
| LLGo · deadcode drop | 6.471x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.690x | 10 |
| LLGo · full LTO + GlobalDCE | 7.013x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1903691 | +1004.9% |
| `base64` | 172302 | LLGo · deadcode drop | 1023497 | +494.0% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1685020 | +877.9% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1073687 | +523.1% |
| `checksum` | 169609 | LLGo · no LTO | 1883144 | +1010.3% |
| `checksum` | 169609 | LLGo · deadcode drop | 1009243 | +495.0% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1648560 | +872.0% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1039514 | +512.9% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2752042 | +1564.0% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1473203 | +790.8% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2536581 | +1433.7% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1590274 | +861.6% |
| `fibonacci` | 141855 | LLGo · no LTO | 1684317 | +1087.4% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 900841 | +535.0% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1473751 | +938.9% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 976563 | +588.4% |
| `grep` | 155984 | LLGo · no LTO | 2560793 | +1541.7% |
| `grep` | 155984 | LLGo · deadcode drop | 1519396 | +874.1% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2259444 | +1348.5% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1566507 | +904.3% |
| `glob` | 136553 | LLGo · no LTO | 1933219 | +1315.7% |
| `glob` | 136553 | LLGo · deadcode drop | 1029340 | +653.8% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1791293 | +1211.8% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1159478 | +749.1% |
| `json-wasi` | 525666 | LLGo · no LTO | 4044080 | +669.3% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2185027 | +315.7% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3775177 | +618.2% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2492642 | +374.2% |
| `llimport` | — | LLGo · no LTO | 11047454 | — |
| `llimport` | — | LLGo · deadcode drop | 9064524 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10099604 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 8973621 | — |
| `path-report` | 194133 | LLGo · no LTO | 2266139 | +1067.3% |
| `path-report` | 194133 | LLGo · deadcode drop | 1346906 | +593.8% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 2114007 | +988.9% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1473538 | +659.0% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3069192 | +772.0% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1746377 | +396.2% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2857279 | +711.8% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1900894 | +440.1% |
| `word-count` | 164053 | LLGo · no LTO | 1893516 | +1054.2% |
| `word-count` | 164053 | LLGo · deadcode drop | 1004871 | +512.5% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1750578 | +967.1% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1126776 | +586.8% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.575x | 11 |
| LLGo · deadcode drop | 0.288x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.504x | 11 |
| LLGo · full LTO + GlobalDCE | 0.350x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1101642 | -51.6% |
| `base64` | 2275731 | LLGo · deadcode drop | 499802 | -78.0% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 873978 | -61.6% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 585517 | -74.3% |
| `checksum` | 2264417 | LLGo · no LTO | 1085306 | -52.1% |
| `checksum` | 2264417 | LLGo · deadcode drop | 486918 | -78.5% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 857890 | -62.1% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 566461 | -75.0% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 1677284 | -35.7% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 803438 | -69.2% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1565112 | -40.0% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 970037 | -62.8% |
| `fibonacci` | 2230899 | LLGo · no LTO | 896099 | -59.8% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 401614 | -82.0% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 762684 | -65.8% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 519683 | -76.7% |
| `grep` | 2848917 | LLGo · no LTO | 1531716 | -46.2% |
| `grep` | 2848917 | LLGo · deadcode drop | 822823 | -71.1% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1354779 | -52.4% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 957292 | -66.4% |
| `glob` | 2257634 | LLGo · no LTO | 1116755 | -50.5% |
| `glob` | 2257634 | LLGo · deadcode drop | 493587 | -78.1% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1009385 | -55.3% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 672871 | -70.2% |
| `json-wasi` | 3314587 | LLGo · no LTO | 2691851 | -18.8% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1312443 | -60.4% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2480819 | -25.2% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1614653 | -51.3% |
| `llimport` | 8423078 | LLGo · no LTO | 8042342 | -4.5% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6503540 | -22.8% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 6888448 | -18.2% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6625910 | -21.3% |
| `path-report` | 2381190 | LLGo · no LTO | 1349927 | -43.3% |
| `path-report` | 2381190 | LLGo · deadcode drop | 715285 | -70.0% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1234900 | -48.1% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 892617 | -62.5% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1866459 | -32.9% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 961826 | -65.4% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1737508 | -37.5% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1140756 | -59.0% |
| `word-count` | 2253620 | LLGo · no LTO | 1098031 | -51.3% |
| `word-count` | 2253620 | LLGo · deadcode drop | 485549 | -78.5% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 964221 | -57.2% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 657483 | -70.8% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 9.329x | 10 |
| LLGo · deadcode drop | 4.451x | 10 |
| LLGo · full LTO (GlobalDCE off) | 8.197x | 10 |
| LLGo · full LTO + GlobalDCE | 5.501x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1101642 | +1038.5% |
| `base64` | 96760 | LLGo · deadcode drop | 499802 | +416.5% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 873978 | +803.2% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 585517 | +505.1% |
| `checksum` | 92685 | LLGo · no LTO | 1085306 | +1071.0% |
| `checksum` | 92685 | LLGo · deadcode drop | 486918 | +425.3% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 857890 | +825.6% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 566461 | +511.2% |
| `conv-wasi` | 201149 | LLGo · no LTO | 1677284 | +733.9% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 803438 | +299.4% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1565112 | +678.1% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 970037 | +382.2% |
| `fibonacci` | 62386 | LLGo · no LTO | 896099 | +1336.4% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 401614 | +543.8% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 762684 | +1122.5% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 519683 | +733.0% |
| `grep` | 303772 | LLGo · no LTO | 1531716 | +404.2% |
| `grep` | 303772 | LLGo · deadcode drop | 822823 | +170.9% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1354779 | +346.0% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 957292 | +215.1% |
| `glob` | 93153 | LLGo · no LTO | 1116755 | +1098.8% |
| `glob` | 93153 | LLGo · deadcode drop | 493587 | +429.9% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1009385 | +983.6% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 672871 | +622.3% |
| `json-wasi` | 493590 | LLGo · no LTO | 2691851 | +445.4% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1312443 | +165.9% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2480819 | +402.6% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1614653 | +227.1% |
| `llimport` | — | LLGo · no LTO | 8042342 | — |
| `llimport` | — | LLGo · deadcode drop | 6503540 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 6888448 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6625910 | — |
| `path-report` | 116889 | LLGo · no LTO | 1349927 | +1054.9% |
| `path-report` | 116889 | LLGo · deadcode drop | 715285 | +511.9% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1234900 | +956.5% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 892617 | +663.6% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1866459 | +549.3% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 961826 | +234.6% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1737508 | +504.5% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1140756 | +296.9% |
| `word-count` | 86834 | LLGo · no LTO | 1098031 | +1164.5% |
| `word-count` | 86834 | LLGo · deadcode drop | 485549 | +459.2% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 964221 | +1010.4% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 657483 | +657.2% |
