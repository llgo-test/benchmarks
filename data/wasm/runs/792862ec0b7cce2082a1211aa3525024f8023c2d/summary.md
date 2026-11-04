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
| `base64` | 2322402 | LLGo · no LTO | 1904444 | -18.0% |
| `base64` | 2322402 | LLGo · deadcode drop | 1027438 | -55.8% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1683104 | -27.5% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1072279 | -53.8% |
| `checksum` | 2311672 | LLGo · no LTO | 1883746 | -18.5% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1013065 | -56.2% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1646473 | -28.8% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1038154 | -55.1% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2751434 | +4.3% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1476301 | -44.0% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2533002 | -4.0% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1588247 | -39.8% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1684742 | -25.9% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 904585 | -60.2% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1471730 | -35.3% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 975351 | -57.1% |
| `grep` | 2871426 | LLGo · no LTO | 2561554 | -10.8% |
| `grep` | 2871426 | LLGo · deadcode drop | 1525264 | -46.9% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2257864 | -21.4% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1567288 | -45.4% |
| `glob` | 2305059 | LLGo · no LTO | 1933928 | -16.1% |
| `glob` | 2305059 | LLGo · deadcode drop | 1033229 | -55.2% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1789358 | -22.4% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1158299 | -49.7% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4042548 | +21.1% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2187520 | -34.5% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3770891 | +13.0% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2489962 | -25.4% |
| `llimport` | 8440671 | LLGo · no LTO | 11041276 | +30.8% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9062259 | +7.4% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10092193 | +19.6% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 8968105 | +6.2% |
| `path-report` | 2428068 | LLGo · no LTO | 2266859 | -6.6% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1350943 | -44.4% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 2112073 | -13.0% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1472369 | -39.4% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3068515 | +9.2% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1749695 | -37.8% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2853724 | +1.5% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1898731 | -32.5% |
| `word-count` | 2300998 | LLGo · no LTO | 1894238 | -17.7% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1008880 | -56.2% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1748609 | -24.0% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1125605 | -51.1% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.769x | 10 |
| LLGo · deadcode drop | 6.491x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.678x | 10 |
| LLGo · full LTO + GlobalDCE | 7.006x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1904444 | +1005.3% |
| `base64` | 172302 | LLGo · deadcode drop | 1027438 | +496.3% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1683104 | +876.8% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1072279 | +522.3% |
| `checksum` | 169609 | LLGo · no LTO | 1883746 | +1010.6% |
| `checksum` | 169609 | LLGo · deadcode drop | 1013065 | +497.3% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1646473 | +870.7% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1038154 | +512.1% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2751434 | +1563.7% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1476301 | +792.6% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2533002 | +1431.6% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1588247 | +860.3% |
| `fibonacci` | 141855 | LLGo · no LTO | 1684742 | +1087.7% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 904585 | +537.7% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1471730 | +937.5% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 975351 | +587.6% |
| `grep` | 155984 | LLGo · no LTO | 2561554 | +1542.2% |
| `grep` | 155984 | LLGo · deadcode drop | 1525264 | +877.8% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2257864 | +1347.5% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1567288 | +904.8% |
| `glob` | 136553 | LLGo · no LTO | 1933928 | +1316.2% |
| `glob` | 136553 | LLGo · deadcode drop | 1033229 | +656.7% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1789358 | +1210.4% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1158299 | +748.2% |
| `json-wasi` | 525666 | LLGo · no LTO | 4042548 | +669.0% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2187520 | +316.1% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3770891 | +617.4% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2489962 | +373.7% |
| `llimport` | — | LLGo · no LTO | 11041276 | — |
| `llimport` | — | LLGo · deadcode drop | 9062259 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10092193 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 8968105 | — |
| `path-report` | 194133 | LLGo · no LTO | 2266859 | +1067.7% |
| `path-report` | 194133 | LLGo · deadcode drop | 1350943 | +595.9% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 2112073 | +988.0% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1472369 | +658.4% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3068515 | +771.8% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1749695 | +397.1% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2853724 | +710.8% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1898731 | +439.5% |
| `word-count` | 164053 | LLGo · no LTO | 1894238 | +1054.7% |
| `word-count` | 164053 | LLGo · deadcode drop | 1008880 | +515.0% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1748609 | +965.9% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1125605 | +586.1% |

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
| `json-wasi` | 3314587 | LLGo · no LTO | 2676352 | -19.3% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1312717 | -60.4% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2464180 | -25.7% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1611781 | -51.4% |
| `llimport` | 8423078 | LLGo · no LTO | 8043175 | -4.5% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6506204 | -22.8% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 6884970 | -18.3% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6624957 | -21.3% |
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
| `json-wasi` | 493590 | LLGo · no LTO | 2676352 | +442.2% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1312717 | +166.0% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2464180 | +399.2% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1611781 | +226.5% |
| `llimport` | — | LLGo · no LTO | 8043175 | — |
| `llimport` | — | LLGo · deadcode drop | 6506204 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 6884970 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6624957 | — |
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
