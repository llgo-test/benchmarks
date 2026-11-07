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
| `base64` | 2322402 | LLGo · no LTO | 1891052 | -18.6% |
| `base64` | 2322402 | LLGo · deadcode drop | 1023653 | -55.9% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1660084 | -28.5% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1068297 | -54.0% |
| `checksum` | 2311672 | LLGo · no LTO | 1870857 | -19.1% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1009335 | -56.3% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1623714 | -29.8% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1035353 | -55.2% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2733493 | +3.6% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1471068 | -44.2% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2506445 | -5.0% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1590727 | -39.7% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1672249 | -26.5% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 902163 | -60.3% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1443864 | -36.5% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 980661 | -56.9% |
| `grep` | 2871426 | LLGo · no LTO | 2546575 | -11.3% |
| `grep` | 2871426 | LLGo · deadcode drop | 1521272 | -47.0% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2232413 | -22.3% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1568373 | -45.4% |
| `glob` | 2305059 | LLGo · no LTO | 1920947 | -16.7% |
| `glob` | 2305059 | LLGo · deadcode drop | 1030184 | -55.3% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1766570 | -23.4% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1161549 | -49.6% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4017818 | +20.4% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2179749 | -34.7% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3744612 | +12.2% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2504725 | -25.0% |
| `llimport` | 8440671 | LLGo · no LTO | 10914140 | +29.3% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9033984 | +7.0% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 9969034 | +18.1% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 8899402 | +5.4% |
| `path-report` | 2428068 | LLGo · no LTO | 2253795 | -7.2% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1347686 | -44.5% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 2089290 | -14.0% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1485090 | -38.8% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3049622 | +8.5% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1743742 | -38.0% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2822470 | +0.4% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1900962 | -32.4% |
| `word-count` | 2300998 | LLGo · no LTO | 1881161 | -18.2% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1005715 | -56.3% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1725799 | -25.0% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1129564 | -50.9% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.692x | 10 |
| LLGo · deadcode drop | 6.471x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.547x | 10 |
| LLGo · full LTO + GlobalDCE | 7.023x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1891052 | +997.5% |
| `base64` | 172302 | LLGo · deadcode drop | 1023653 | +494.1% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1660084 | +863.5% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1068297 | +520.0% |
| `checksum` | 169609 | LLGo · no LTO | 1870857 | +1003.0% |
| `checksum` | 169609 | LLGo · deadcode drop | 1009335 | +495.1% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1623714 | +857.3% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1035353 | +510.4% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2733493 | +1552.8% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1471068 | +789.5% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2506445 | +1415.5% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1590727 | +861.8% |
| `fibonacci` | 141855 | LLGo · no LTO | 1672249 | +1078.8% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 902163 | +536.0% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1443864 | +917.8% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 980661 | +591.3% |
| `grep` | 155984 | LLGo · no LTO | 2546575 | +1532.6% |
| `grep` | 155984 | LLGo · deadcode drop | 1521272 | +875.3% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2232413 | +1331.2% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1568373 | +905.5% |
| `glob` | 136553 | LLGo · no LTO | 1920947 | +1306.7% |
| `glob` | 136553 | LLGo · deadcode drop | 1030184 | +654.4% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1766570 | +1193.7% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1161549 | +750.6% |
| `json-wasi` | 525666 | LLGo · no LTO | 4017818 | +664.3% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2179749 | +314.7% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3744612 | +612.4% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2504725 | +376.5% |
| `llimport` | — | LLGo · no LTO | 10914140 | — |
| `llimport` | — | LLGo · deadcode drop | 9033984 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 9969034 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 8899402 | — |
| `path-report` | 194133 | LLGo · no LTO | 2253795 | +1061.0% |
| `path-report` | 194133 | LLGo · deadcode drop | 1347686 | +594.2% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 2089290 | +976.2% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1485090 | +665.0% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3049622 | +766.4% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1743742 | +395.4% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2822470 | +701.9% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1900962 | +440.1% |
| `word-count` | 164053 | LLGo · no LTO | 1881161 | +1046.7% |
| `word-count` | 164053 | LLGo · deadcode drop | 1005715 | +513.0% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1725799 | +952.0% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1129564 | +588.5% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.564x | 11 |
| LLGo · deadcode drop | 0.287x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.488x | 11 |
| LLGo · full LTO + GlobalDCE | 0.343x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1071467 | -52.9% |
| `base64` | 2275731 | LLGo · deadcode drop | 496477 | -78.2% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 834924 | -63.3% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 564965 | -75.2% |
| `checksum` | 2264417 | LLGo · no LTO | 1055380 | -53.4% |
| `checksum` | 2264417 | LLGo · deadcode drop | 483544 | -78.6% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 819168 | -63.8% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 546779 | -75.9% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 1654540 | -36.6% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 794889 | -69.5% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1531236 | -41.3% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 957899 | -63.3% |
| `fibonacci` | 2230899 | LLGo · no LTO | 869416 | -61.0% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 401231 | -82.0% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 722845 | -67.6% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 504615 | -77.4% |
| `grep` | 2848917 | LLGo · no LTO | 1507213 | -47.1% |
| `grep` | 2848917 | LLGo · deadcode drop | 825192 | -71.0% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1315284 | -53.8% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 940862 | -67.0% |
| `glob` | 2257634 | LLGo · no LTO | 1086616 | -51.9% |
| `glob` | 2257634 | LLGo · deadcode drop | 490690 | -78.3% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 968314 | -57.1% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 657116 | -70.9% |
| `json-wasi` | 3314587 | LLGo · no LTO | 2663420 | -19.6% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1311134 | -60.4% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2448345 | -26.1% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1624909 | -51.0% |
| `llimport` | 8423078 | LLGo · no LTO | 7940215 | -5.7% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6490482 | -22.9% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 6787490 | -19.4% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6557682 | -22.1% |
| `path-report` | 2381190 | LLGo · no LTO | 1319878 | -44.6% |
| `path-report` | 2381190 | LLGo · deadcode drop | 712318 | -70.1% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1193836 | -49.9% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 882795 | -62.9% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1843743 | -33.7% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 953331 | -65.7% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1701272 | -38.8% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1128914 | -59.4% |
| `word-count` | 2253620 | LLGo · no LTO | 1067853 | -52.6% |
| `word-count` | 2253620 | LLGo · deadcode drop | 482668 | -78.6% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 925296 | -58.9% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 642215 | -71.5% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 9.129x | 10 |
| LLGo · deadcode drop | 4.429x | 10 |
| LLGo · full LTO (GlobalDCE off) | 7.917x | 10 |
| LLGo · full LTO + GlobalDCE | 5.396x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1071467 | +1007.3% |
| `base64` | 96760 | LLGo · deadcode drop | 496477 | +413.1% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 834924 | +762.9% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 564965 | +483.9% |
| `checksum` | 92685 | LLGo · no LTO | 1055380 | +1038.7% |
| `checksum` | 92685 | LLGo · deadcode drop | 483544 | +421.7% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 819168 | +783.8% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 546779 | +489.9% |
| `conv-wasi` | 201149 | LLGo · no LTO | 1654540 | +722.5% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 794889 | +295.2% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1531236 | +661.2% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 957899 | +376.2% |
| `fibonacci` | 62386 | LLGo · no LTO | 869416 | +1293.6% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 401231 | +543.1% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 722845 | +1058.7% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 504615 | +708.9% |
| `grep` | 303772 | LLGo · no LTO | 1507213 | +396.2% |
| `grep` | 303772 | LLGo · deadcode drop | 825192 | +171.6% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1315284 | +333.0% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 940862 | +209.7% |
| `glob` | 93153 | LLGo · no LTO | 1086616 | +1066.5% |
| `glob` | 93153 | LLGo · deadcode drop | 490690 | +426.8% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 968314 | +939.5% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 657116 | +605.4% |
| `json-wasi` | 493590 | LLGo · no LTO | 2663420 | +439.6% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1311134 | +165.6% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2448345 | +396.0% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1624909 | +229.2% |
| `llimport` | — | LLGo · no LTO | 7940215 | — |
| `llimport` | — | LLGo · deadcode drop | 6490482 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 6787490 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6557682 | — |
| `path-report` | 116889 | LLGo · no LTO | 1319878 | +1029.2% |
| `path-report` | 116889 | LLGo · deadcode drop | 712318 | +509.4% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1193836 | +921.3% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 882795 | +655.2% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1843743 | +541.4% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 953331 | +231.7% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1701272 | +491.9% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1128914 | +292.7% |
| `word-count` | 86834 | LLGo · no LTO | 1067853 | +1129.8% |
| `word-count` | 86834 | LLGo · deadcode drop | 482668 | +455.9% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 925296 | +965.6% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 642215 | +639.6% |
