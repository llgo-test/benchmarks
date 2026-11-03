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
| LLGo · full LTO (GlobalDCE off) | 0.855x | 11 |
| LLGo · full LTO + GlobalDCE | 0.576x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1904466 | -18.0% |
| `base64` | 2322402 | LLGo · deadcode drop | 1027481 | -55.8% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1683132 | -27.5% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1072338 | -53.8% |
| `checksum` | 2311672 | LLGo · no LTO | 1883789 | -18.5% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1013101 | -56.2% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1646505 | -28.8% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1038217 | -55.1% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2751484 | +4.3% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1476359 | -44.0% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2533074 | -4.0% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1588274 | -39.8% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1684786 | -25.9% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 904635 | -60.2% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1471757 | -35.3% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 975369 | -57.1% |
| `grep` | 2871426 | LLGo · no LTO | 2561603 | -10.8% |
| `grep` | 2871426 | LLGo · deadcode drop | 1525316 | -46.9% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2257908 | -21.4% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1567337 | -45.4% |
| `glob` | 2305059 | LLGo · no LTO | 1933981 | -16.1% |
| `glob` | 2305059 | LLGo · deadcode drop | 1033280 | -55.2% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1789410 | -22.4% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1158342 | -49.7% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4042583 | +21.1% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2187585 | -34.5% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3770917 | +13.0% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2490037 | -25.4% |
| `llimport` | 8440671 | LLGo · no LTO | 11041328 | +30.8% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9062302 | +7.4% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10092223 | +19.6% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 8968156 | +6.2% |
| `path-report` | 2428068 | LLGo · no LTO | 2266914 | -6.6% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1350995 | -44.4% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 2112125 | -13.0% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1472420 | -39.4% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3068553 | +9.2% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1749737 | -37.8% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2853759 | +1.5% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1898776 | -32.5% |
| `word-count` | 2300998 | LLGo · no LTO | 1894292 | -17.7% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1008927 | -56.2% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1748654 | -24.0% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1125647 | -51.1% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.770x | 10 |
| LLGo · deadcode drop | 6.491x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.679x | 10 |
| LLGo · full LTO + GlobalDCE | 7.007x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1904466 | +1005.3% |
| `base64` | 172302 | LLGo · deadcode drop | 1027481 | +496.3% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1683132 | +876.8% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1072338 | +522.4% |
| `checksum` | 169609 | LLGo · no LTO | 1883789 | +1010.7% |
| `checksum` | 169609 | LLGo · deadcode drop | 1013101 | +497.3% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1646505 | +870.8% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1038217 | +512.1% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2751484 | +1563.7% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1476359 | +792.7% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2533074 | +1431.6% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1588274 | +860.3% |
| `fibonacci` | 141855 | LLGo · no LTO | 1684786 | +1087.7% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 904635 | +537.7% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1471757 | +937.5% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 975369 | +587.6% |
| `grep` | 155984 | LLGo · no LTO | 2561603 | +1542.2% |
| `grep` | 155984 | LLGo · deadcode drop | 1525316 | +877.9% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2257908 | +1347.5% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1567337 | +904.8% |
| `glob` | 136553 | LLGo · no LTO | 1933981 | +1316.3% |
| `glob` | 136553 | LLGo · deadcode drop | 1033280 | +656.7% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1789410 | +1210.4% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1158342 | +748.3% |
| `json-wasi` | 525666 | LLGo · no LTO | 4042583 | +669.0% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2187585 | +316.2% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3770917 | +617.4% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2490037 | +373.7% |
| `llimport` | — | LLGo · no LTO | 11041328 | — |
| `llimport` | — | LLGo · deadcode drop | 9062302 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10092223 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 8968156 | — |
| `path-report` | 194133 | LLGo · no LTO | 2266914 | +1067.7% |
| `path-report` | 194133 | LLGo · deadcode drop | 1350995 | +595.9% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 2112125 | +988.0% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1472420 | +658.5% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3068553 | +771.8% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1749737 | +397.1% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2853759 | +710.8% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1898776 | +439.5% |
| `word-count` | 164053 | LLGo · no LTO | 1894292 | +1054.7% |
| `word-count` | 164053 | LLGo · deadcode drop | 1008927 | +515.0% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1748654 | +965.9% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1125647 | +586.1% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.567x | 11 |
| LLGo · deadcode drop | 0.287x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.495x | 11 |
| LLGo · full LTO + GlobalDCE | 0.342x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1077385 | -52.7% |
| `base64` | 2275731 | LLGo · deadcode drop | 497226 | -78.2% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 848959 | -62.7% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 564992 | -75.2% |
| `checksum` | 2264417 | LLGo · no LTO | 1061064 | -53.1% |
| `checksum` | 2264417 | LLGo · deadcode drop | 484335 | -78.6% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 832990 | -63.2% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 545996 | -75.9% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 1662163 | -36.3% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 795532 | -69.5% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1547840 | -40.7% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 954149 | -63.4% |
| `fibonacci` | 2230899 | LLGo · no LTO | 871769 | -60.9% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 401239 | -82.0% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 737743 | -66.9% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 499182 | -77.6% |
| `grep` | 2848917 | LLGo · no LTO | 1514082 | -46.9% |
| `grep` | 2848917 | LLGo · deadcode drop | 826078 | -71.0% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1335020 | -53.1% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 942337 | -66.9% |
| `glob` | 2257634 | LLGo · no LTO | 1092528 | -51.6% |
| `glob` | 2257634 | LLGo · deadcode drop | 491011 | -78.3% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 984497 | -56.4% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 652444 | -71.1% |
| `json-wasi` | 3314587 | LLGo · no LTO | 2676416 | -19.3% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1312797 | -60.4% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2464244 | -25.7% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1611845 | -51.4% |
| `llimport` | 8423078 | LLGo · no LTO | 8043239 | -4.5% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6506268 | -22.8% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 6885034 | -18.3% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6625021 | -21.3% |
| `path-report` | 2381190 | LLGo · no LTO | 1325724 | -44.3% |
| `path-report` | 2381190 | LLGo · deadcode drop | 712768 | -70.1% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1209850 | -49.2% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 872198 | -63.4% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1851351 | -33.4% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 954179 | -65.7% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1720144 | -38.1% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1124643 | -59.6% |
| `word-count` | 2253620 | LLGo · no LTO | 1073819 | -52.4% |
| `word-count` | 2253620 | LLGo · deadcode drop | 483019 | -78.6% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 939310 | -58.3% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 637050 | -71.7% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 9.172x | 10 |
| LLGo · deadcode drop | 4.433x | 10 |
| LLGo · full LTO (GlobalDCE off) | 8.030x | 10 |
| LLGo · full LTO + GlobalDCE | 5.367x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1077385 | +1013.5% |
| `base64` | 96760 | LLGo · deadcode drop | 497226 | +413.9% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 848959 | +777.4% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 564992 | +483.9% |
| `checksum` | 92685 | LLGo · no LTO | 1061064 | +1044.8% |
| `checksum` | 92685 | LLGo · deadcode drop | 484335 | +422.6% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 832990 | +798.7% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 545996 | +489.1% |
| `conv-wasi` | 201149 | LLGo · no LTO | 1662163 | +726.3% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 795532 | +295.5% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1547840 | +669.5% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 954149 | +374.3% |
| `fibonacci` | 62386 | LLGo · no LTO | 871769 | +1297.4% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 401239 | +543.2% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 737743 | +1082.5% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 499182 | +700.2% |
| `grep` | 303772 | LLGo · no LTO | 1514082 | +398.4% |
| `grep` | 303772 | LLGo · deadcode drop | 826078 | +171.9% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1335020 | +339.5% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 942337 | +210.2% |
| `glob` | 93153 | LLGo · no LTO | 1092528 | +1072.8% |
| `glob` | 93153 | LLGo · deadcode drop | 491011 | +427.1% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 984497 | +956.9% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 652444 | +600.4% |
| `json-wasi` | 493590 | LLGo · no LTO | 2676416 | +442.2% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1312797 | +166.0% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2464244 | +399.2% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1611845 | +226.6% |
| `llimport` | — | LLGo · no LTO | 8043239 | — |
| `llimport` | — | LLGo · deadcode drop | 6506268 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 6885034 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6625021 | — |
| `path-report` | 116889 | LLGo · no LTO | 1325724 | +1034.2% |
| `path-report` | 116889 | LLGo · deadcode drop | 712768 | +509.8% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1209850 | +935.0% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 872198 | +646.2% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1851351 | +544.1% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 954179 | +231.9% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1720144 | +498.4% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1124643 | +291.2% |
| `word-count` | 86834 | LLGo · no LTO | 1073819 | +1136.6% |
| `word-count` | 86834 | LLGo · deadcode drop | 483019 | +456.3% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 939310 | +981.7% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 637050 | +633.6% |
