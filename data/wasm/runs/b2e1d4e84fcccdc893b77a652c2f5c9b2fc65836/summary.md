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
| `base64` | 2322402 | LLGo · no LTO | 1903144 | -18.1% |
| `base64` | 2322402 | LLGo · deadcode drop | 1025820 | -55.8% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1682478 | -27.6% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1071247 | -53.9% |
| `checksum` | 2311672 | LLGo · no LTO | 1882591 | -18.6% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1011569 | -56.2% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1645920 | -28.8% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1037206 | -55.1% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2751326 | +4.3% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1476575 | -44.0% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2533910 | -4.0% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1589632 | -39.8% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1683761 | -26.0% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 903177 | -60.3% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1471104 | -35.3% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 974293 | -57.2% |
| `grep` | 2871426 | LLGo · no LTO | 2561000 | -10.8% |
| `grep` | 2871426 | LLGo · deadcode drop | 1524326 | -46.9% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2257886 | -21.4% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1566878 | -45.4% |
| `glob` | 2305059 | LLGo · no LTO | 1932653 | -16.2% |
| `glob` | 2305059 | LLGo · deadcode drop | 1031623 | -55.2% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1788655 | -22.4% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1157165 | -49.8% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4042830 | +21.1% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2188040 | -34.5% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3771934 | +13.0% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2491463 | -25.4% |
| `llimport` | 8440671 | LLGo · no LTO | 11045216 | +30.9% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9066415 | +7.4% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10097084 | +19.6% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 8972958 | +6.3% |
| `path-report` | 2428068 | LLGo · no LTO | 2265565 | -6.7% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1349311 | -44.4% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 2111405 | -13.0% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1471228 | -39.4% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3068562 | +9.2% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1750017 | -37.7% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2854780 | +1.6% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1900378 | -32.4% |
| `word-count` | 2300998 | LLGo · no LTO | 1892950 | -17.7% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1007289 | -56.2% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1747951 | -24.0% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1124501 | -51.1% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.765x | 10 |
| LLGo · deadcode drop | 6.485x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.677x | 10 |
| LLGo · full LTO + GlobalDCE | 7.004x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1903144 | +1004.5% |
| `base64` | 172302 | LLGo · deadcode drop | 1025820 | +495.4% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1682478 | +876.5% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1071247 | +521.7% |
| `checksum` | 169609 | LLGo · no LTO | 1882591 | +1010.0% |
| `checksum` | 169609 | LLGo · deadcode drop | 1011569 | +496.4% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1645920 | +870.4% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1037206 | +511.5% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2751326 | +1563.6% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1476575 | +792.8% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2533910 | +1432.1% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1589632 | +861.2% |
| `fibonacci` | 141855 | LLGo · no LTO | 1683761 | +1087.0% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 903177 | +536.7% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1471104 | +937.0% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 974293 | +586.8% |
| `grep` | 155984 | LLGo · no LTO | 2561000 | +1541.8% |
| `grep` | 155984 | LLGo · deadcode drop | 1524326 | +877.2% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2257886 | +1347.5% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1566878 | +904.5% |
| `glob` | 136553 | LLGo · no LTO | 1932653 | +1315.3% |
| `glob` | 136553 | LLGo · deadcode drop | 1031623 | +655.5% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1788655 | +1209.9% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1157165 | +747.4% |
| `json-wasi` | 525666 | LLGo · no LTO | 4042830 | +669.1% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2188040 | +316.2% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3771934 | +617.6% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2491463 | +374.0% |
| `llimport` | — | LLGo · no LTO | 11045216 | — |
| `llimport` | — | LLGo · deadcode drop | 9066415 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10097084 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 8972958 | — |
| `path-report` | 194133 | LLGo · no LTO | 2265565 | +1067.0% |
| `path-report` | 194133 | LLGo · deadcode drop | 1349311 | +595.0% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 2111405 | +987.6% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1471228 | +657.8% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3068562 | +771.8% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1750017 | +397.2% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2854780 | +711.1% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1900378 | +439.9% |
| `word-count` | 164053 | LLGo · no LTO | 1892950 | +1053.9% |
| `word-count` | 164053 | LLGo · deadcode drop | 1007289 | +514.0% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1747951 | +965.5% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1124501 | +585.4% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.566x | 11 |
| LLGo · deadcode drop | 0.286x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.495x | 11 |
| LLGo · full LTO + GlobalDCE | 0.342x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1076379 | -52.7% |
| `base64` | 2275731 | LLGo · deadcode drop | 496328 | -78.2% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 848160 | -62.7% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 564198 | -75.2% |
| `checksum` | 2264417 | LLGo · no LTO | 1060073 | -53.2% |
| `checksum` | 2264417 | LLGo · deadcode drop | 483458 | -78.6% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 832206 | -63.2% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 545224 | -75.9% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 1660251 | -36.3% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 794539 | -69.5% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1546719 | -40.7% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 953627 | -63.4% |
| `fibonacci` | 2230899 | LLGo · no LTO | 870754 | -61.0% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 398267 | -82.1% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 736887 | -67.0% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 498340 | -77.7% |
| `grep` | 2848917 | LLGo · no LTO | 1513013 | -46.9% |
| `grep` | 2848917 | LLGo · deadcode drop | 825112 | -71.0% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1334419 | -53.2% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 941764 | -66.9% |
| `glob` | 2257634 | LLGo · no LTO | 1091506 | -51.7% |
| `glob` | 2257634 | LLGo · deadcode drop | 490129 | -78.3% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 983706 | -56.4% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 651658 | -71.1% |
| `json-wasi` | 3314587 | LLGo · no LTO | 2674875 | -19.3% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1311878 | -60.4% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2463356 | -25.7% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1611533 | -51.4% |
| `llimport` | 8423078 | LLGo · no LTO | 8043540 | -4.5% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6506403 | -22.8% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 6886263 | -18.2% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6626196 | -21.3% |
| `path-report` | 2381190 | LLGo · no LTO | 1324694 | -44.4% |
| `path-report` | 2381190 | LLGo · deadcode drop | 711862 | -70.1% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1209051 | -49.2% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 871412 | -63.4% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1849449 | -33.5% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 953114 | -65.7% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1719076 | -38.2% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1124326 | -59.6% |
| `word-count` | 2253620 | LLGo · no LTO | 1072798 | -52.4% |
| `word-count` | 2253620 | LLGo · deadcode drop | 482138 | -78.6% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 938530 | -58.4% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 636262 | -71.8% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 9.164x | 10 |
| LLGo · deadcode drop | 4.424x | 10 |
| LLGo · full LTO (GlobalDCE off) | 8.024x | 10 |
| LLGo · full LTO + GlobalDCE | 5.362x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1076379 | +1012.4% |
| `base64` | 96760 | LLGo · deadcode drop | 496328 | +412.9% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 848160 | +776.6% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 564198 | +483.1% |
| `checksum` | 92685 | LLGo · no LTO | 1060073 | +1043.7% |
| `checksum` | 92685 | LLGo · deadcode drop | 483458 | +421.6% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 832206 | +797.9% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 545224 | +488.3% |
| `conv-wasi` | 201149 | LLGo · no LTO | 1660251 | +725.4% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 794539 | +295.0% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1546719 | +668.9% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 953627 | +374.1% |
| `fibonacci` | 62386 | LLGo · no LTO | 870754 | +1295.8% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 398267 | +538.4% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 736887 | +1081.2% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 498340 | +698.8% |
| `grep` | 303772 | LLGo · no LTO | 1513013 | +398.1% |
| `grep` | 303772 | LLGo · deadcode drop | 825112 | +171.6% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1334419 | +339.3% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 941764 | +210.0% |
| `glob` | 93153 | LLGo · no LTO | 1091506 | +1071.7% |
| `glob` | 93153 | LLGo · deadcode drop | 490129 | +426.2% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 983706 | +956.0% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 651658 | +599.6% |
| `json-wasi` | 493590 | LLGo · no LTO | 2674875 | +441.9% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1311878 | +165.8% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2463356 | +399.1% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1611533 | +226.5% |
| `llimport` | — | LLGo · no LTO | 8043540 | — |
| `llimport` | — | LLGo · deadcode drop | 6506403 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 6886263 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6626196 | — |
| `path-report` | 116889 | LLGo · no LTO | 1324694 | +1033.3% |
| `path-report` | 116889 | LLGo · deadcode drop | 711862 | +509.0% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1209051 | +934.4% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 871412 | +645.5% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1849449 | +543.4% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 953114 | +231.6% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1719076 | +498.0% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1124326 | +291.1% |
| `word-count` | 86834 | LLGo · no LTO | 1072798 | +1135.5% |
| `word-count` | 86834 | LLGo · deadcode drop | 482138 | +455.2% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 938530 | +980.8% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 636262 | +632.7% |
