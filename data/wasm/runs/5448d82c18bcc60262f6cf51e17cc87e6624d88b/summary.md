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
| LLGo · no LTO | 0.934x | 11 |
| LLGo · deadcode drop | 0.537x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.844x | 11 |
| LLGo · full LTO + GlobalDCE | 0.577x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1890379 | -18.6% |
| `base64` | 2322402 | LLGo · deadcode drop | 1023735 | -55.9% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1659443 | -28.5% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1067596 | -54.0% |
| `checksum` | 2311672 | LLGo · no LTO | 1870204 | -19.1% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1009451 | -56.3% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1623087 | -29.8% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1034682 | -55.2% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2732935 | +3.6% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1471195 | -44.2% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2505788 | -5.0% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1590087 | -39.7% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1671631 | -26.5% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 902267 | -60.3% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1443214 | -36.5% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 979983 | -56.9% |
| `grep` | 2871426 | LLGo · no LTO | 2545940 | -11.3% |
| `grep` | 2871426 | LLGo · deadcode drop | 1521439 | -47.0% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2231841 | -22.3% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1567813 | -45.4% |
| `glob` | 2305059 | LLGo · no LTO | 1920314 | -16.7% |
| `glob` | 2305059 | LLGo · deadcode drop | 1030297 | -55.3% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1765931 | -23.4% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1160894 | -49.6% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4017357 | +20.3% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2179914 | -34.7% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3743994 | +12.2% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2504086 | -25.0% |
| `llimport` | 8440671 | LLGo · no LTO | 10913361 | +29.3% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9033926 | +7.0% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 9969063 | +18.1% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 8899403 | +5.4% |
| `path-report` | 2428068 | LLGo · no LTO | 2253210 | -7.2% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1347809 | -44.5% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 2088677 | -14.0% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1484468 | -38.9% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3049055 | +8.5% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1743894 | -38.0% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2822475 | +0.4% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1900884 | -32.4% |
| `word-count` | 2300998 | LLGo · no LTO | 1880523 | -18.3% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1005849 | -56.3% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1725160 | -25.0% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1128879 | -50.9% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.689x | 10 |
| LLGo · deadcode drop | 6.471x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.544x | 10 |
| LLGo · full LTO + GlobalDCE | 7.019x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1890379 | +997.1% |
| `base64` | 172302 | LLGo · deadcode drop | 1023735 | +494.2% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1659443 | +863.1% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1067596 | +519.6% |
| `checksum` | 169609 | LLGo · no LTO | 1870204 | +1002.7% |
| `checksum` | 169609 | LLGo · deadcode drop | 1009451 | +495.2% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1623087 | +857.0% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1034682 | +510.0% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2732935 | +1552.5% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1471195 | +789.6% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2505788 | +1415.1% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1590087 | +861.4% |
| `fibonacci` | 141855 | LLGo · no LTO | 1671631 | +1078.4% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 902267 | +536.0% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1443214 | +917.4% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 979983 | +590.8% |
| `grep` | 155984 | LLGo · no LTO | 2545940 | +1532.2% |
| `grep` | 155984 | LLGo · deadcode drop | 1521439 | +875.4% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2231841 | +1330.8% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1567813 | +905.1% |
| `glob` | 136553 | LLGo · no LTO | 1920314 | +1306.3% |
| `glob` | 136553 | LLGo · deadcode drop | 1030297 | +654.5% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1765931 | +1193.2% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1160894 | +750.1% |
| `json-wasi` | 525666 | LLGo · no LTO | 4017357 | +664.2% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2179914 | +314.7% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3743994 | +612.2% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2504086 | +376.4% |
| `llimport` | — | LLGo · no LTO | 10913361 | — |
| `llimport` | — | LLGo · deadcode drop | 9033926 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 9969063 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 8899403 | — |
| `path-report` | 194133 | LLGo · no LTO | 2253210 | +1060.7% |
| `path-report` | 194133 | LLGo · deadcode drop | 1347809 | +594.3% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 2088677 | +975.9% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1484468 | +664.7% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3049055 | +766.3% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1743894 | +395.5% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2822475 | +701.9% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1900884 | +440.1% |
| `word-count` | 164053 | LLGo · no LTO | 1880523 | +1046.3% |
| `word-count` | 164053 | LLGo · deadcode drop | 1005849 | +513.1% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1725160 | +951.6% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1128879 | +588.1% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.563x | 11 |
| LLGo · deadcode drop | 0.287x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.488x | 11 |
| LLGo · full LTO + GlobalDCE | 0.343x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1070968 | -52.9% |
| `base64` | 2275731 | LLGo · deadcode drop | 496423 | -78.2% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 834466 | -63.3% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 564492 | -75.2% |
| `checksum` | 2264417 | LLGo · no LTO | 1054874 | -53.4% |
| `checksum` | 2264417 | LLGo · deadcode drop | 483497 | -78.6% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 818701 | -63.8% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 546289 | -75.9% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 1653966 | -36.6% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 794813 | -69.5% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1530762 | -41.3% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 957403 | -63.3% |
| `fibonacci` | 2230899 | LLGo · no LTO | 868895 | -61.1% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 401183 | -82.0% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 722378 | -67.6% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 504125 | -77.4% |
| `grep` | 2848917 | LLGo · no LTO | 1506714 | -47.1% |
| `grep` | 2848917 | LLGo · deadcode drop | 825180 | -71.0% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1314829 | -53.8% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 940384 | -67.0% |
| `glob` | 2257634 | LLGo · no LTO | 1086109 | -51.9% |
| `glob` | 2257634 | LLGo · deadcode drop | 490626 | -78.3% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 967844 | -57.1% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 656623 | -70.9% |
| `json-wasi` | 3314587 | LLGo · no LTO | 2662853 | -19.7% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1311034 | -60.4% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2447891 | -26.1% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1624418 | -51.0% |
| `llimport` | 8423078 | LLGo · no LTO | 7939766 | -5.7% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6490472 | -22.9% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 6786920 | -19.4% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6556836 | -22.2% |
| `path-report` | 2381190 | LLGo · no LTO | 1319374 | -44.6% |
| `path-report` | 2381190 | LLGo · deadcode drop | 712291 | -70.1% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1193374 | -49.9% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 882306 | -62.9% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1843196 | -33.7% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 953283 | -65.7% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1700711 | -38.8% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1128313 | -59.4% |
| `word-count` | 2253620 | LLGo · no LTO | 1067347 | -52.6% |
| `word-count` | 2253620 | LLGo · deadcode drop | 482604 | -78.6% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 924829 | -59.0% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 641725 | -71.5% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 9.125x | 10 |
| LLGo · deadcode drop | 4.429x | 10 |
| LLGo · full LTO (GlobalDCE off) | 7.914x | 10 |
| LLGo · full LTO + GlobalDCE | 5.393x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1070968 | +1006.8% |
| `base64` | 96760 | LLGo · deadcode drop | 496423 | +413.0% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 834466 | +762.4% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 564492 | +483.4% |
| `checksum` | 92685 | LLGo · no LTO | 1054874 | +1038.1% |
| `checksum` | 92685 | LLGo · deadcode drop | 483497 | +421.7% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 818701 | +783.3% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 546289 | +489.4% |
| `conv-wasi` | 201149 | LLGo · no LTO | 1653966 | +722.3% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 794813 | +295.1% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1530762 | +661.0% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 957403 | +376.0% |
| `fibonacci` | 62386 | LLGo · no LTO | 868895 | +1292.8% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 401183 | +543.1% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 722378 | +1057.9% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 504125 | +708.1% |
| `grep` | 303772 | LLGo · no LTO | 1506714 | +396.0% |
| `grep` | 303772 | LLGo · deadcode drop | 825180 | +171.6% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1314829 | +332.8% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 940384 | +209.6% |
| `glob` | 93153 | LLGo · no LTO | 1086109 | +1065.9% |
| `glob` | 93153 | LLGo · deadcode drop | 490626 | +426.7% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 967844 | +939.0% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 656623 | +604.9% |
| `json-wasi` | 493590 | LLGo · no LTO | 2662853 | +439.5% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1311034 | +165.6% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2447891 | +395.9% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1624418 | +229.1% |
| `llimport` | — | LLGo · no LTO | 7939766 | — |
| `llimport` | — | LLGo · deadcode drop | 6490472 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 6786920 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6556836 | — |
| `path-report` | 116889 | LLGo · no LTO | 1319374 | +1028.7% |
| `path-report` | 116889 | LLGo · deadcode drop | 712291 | +509.4% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1193374 | +920.9% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 882306 | +654.8% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1843196 | +541.2% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 953283 | +231.6% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1700711 | +491.7% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1128313 | +292.5% |
| `word-count` | 86834 | LLGo · no LTO | 1067347 | +1129.2% |
| `word-count` | 86834 | LLGo · deadcode drop | 482604 | +455.8% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 924829 | +965.1% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 641725 | +639.0% |
