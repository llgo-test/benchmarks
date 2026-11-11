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
| LLGo · no LTO | 0.943x | 11 |
| LLGo · deadcode drop | 0.546x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.865x | 11 |
| LLGo · full LTO + GlobalDCE | 0.585x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1921085 | -17.3% |
| `base64` | 2322402 | LLGo · deadcode drop | 1057603 | -54.5% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1716762 | -26.1% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1096498 | -52.8% |
| `checksum` | 2311672 | LLGo · no LTO | 1901643 | -17.7% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1043030 | -54.9% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1680353 | -27.3% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1062622 | -54.0% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2783892 | +5.5% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1520629 | -42.4% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2582140 | -2.1% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1624222 | -38.4% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1699149 | -25.3% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 933044 | -59.0% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1489705 | -34.5% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 1004194 | -55.8% |
| `grep` | 2871426 | LLGo · no LTO | 2584720 | -10.0% |
| `grep` | 2871426 | LLGo · deadcode drop | 1564312 | -45.5% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2308201 | -19.6% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1609290 | -44.0% |
| `glob` | 2305059 | LLGo · no LTO | 1952084 | -15.3% |
| `glob` | 2305059 | LLGo · deadcode drop | 1062169 | -53.9% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1822266 | -20.9% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1185854 | -48.6% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4096235 | +22.7% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2265242 | -32.1% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3875390 | +16.1% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2582270 | -22.6% |
| `llimport` | 8440671 | LLGo · no LTO | 11091062 | +31.4% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9270988 | +9.8% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10417037 | +23.4% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 9299253 | +10.2% |
| `path-report` | 2428068 | LLGo · no LTO | 2097814 | -13.6% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1193971 | -50.8% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 1959948 | -19.3% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1323768 | -45.5% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3118641 | +10.9% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1807647 | -35.7% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2916075 | +3.7% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1952326 | -30.6% |
| `word-count` | 2300998 | LLGo · no LTO | 1911529 | -16.9% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1038787 | -54.9% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1777510 | -22.8% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1151519 | -50.0% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.790x | 10 |
| LLGo · deadcode drop | 6.586x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.788x | 10 |
| LLGo · full LTO + GlobalDCE | 7.096x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1921085 | +1015.0% |
| `base64` | 172302 | LLGo · deadcode drop | 1057603 | +513.8% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1716762 | +896.4% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1096498 | +536.4% |
| `checksum` | 169609 | LLGo · no LTO | 1901643 | +1021.2% |
| `checksum` | 169609 | LLGo · deadcode drop | 1043030 | +515.0% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1680353 | +890.7% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1062622 | +526.5% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2783892 | +1583.3% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1520629 | +819.4% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2582140 | +1461.3% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1624222 | +882.1% |
| `fibonacci` | 141855 | LLGo · no LTO | 1699149 | +1097.8% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 933044 | +557.7% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1489705 | +950.2% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 1004194 | +607.9% |
| `grep` | 155984 | LLGo · no LTO | 2584720 | +1557.0% |
| `grep` | 155984 | LLGo · deadcode drop | 1564312 | +902.9% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2308201 | +1379.8% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1609290 | +931.7% |
| `glob` | 136553 | LLGo · no LTO | 1952084 | +1329.5% |
| `glob` | 136553 | LLGo · deadcode drop | 1062169 | +677.8% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1822266 | +1234.5% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1185854 | +768.4% |
| `json-wasi` | 525666 | LLGo · no LTO | 4096235 | +679.2% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2265242 | +330.9% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3875390 | +637.2% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2582270 | +391.2% |
| `llimport` | — | LLGo · no LTO | 11091062 | — |
| `llimport` | — | LLGo · deadcode drop | 9270988 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10417037 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 9299253 | — |
| `path-report` | 194133 | LLGo · no LTO | 2097814 | +980.6% |
| `path-report` | 194133 | LLGo · deadcode drop | 1193971 | +515.0% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 1959948 | +909.6% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1323768 | +581.9% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3118641 | +786.1% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1807647 | +413.6% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2916075 | +728.5% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1952326 | +454.7% |
| `word-count` | 164053 | LLGo · no LTO | 1911529 | +1065.2% |
| `word-count` | 164053 | LLGo · deadcode drop | 1038787 | +533.2% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1777510 | +983.5% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1151519 | +601.9% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.579x | 11 |
| LLGo · deadcode drop | 0.301x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.510x | 11 |
| LLGo · full LTO + GlobalDCE | 0.356x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1105185 | -51.4% |
| `base64` | 2275731 | LLGo · deadcode drop | 530631 | -76.7% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 881523 | -61.3% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 596245 | -73.8% |
| `checksum` | 2264417 | LLGo · no LTO | 1089755 | -51.9% |
| `checksum` | 2264417 | LLGo · deadcode drop | 517241 | -77.2% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 865258 | -61.8% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 576900 | -74.5% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 1724653 | -33.9% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 850463 | -67.4% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1613669 | -38.1% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1003317 | -61.5% |
| `fibonacci` | 2230899 | LLGo · no LTO | 901641 | -59.6% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 432450 | -80.6% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 761215 | -65.9% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 530998 | -76.2% |
| `grep` | 2848917 | LLGo · no LTO | 1553518 | -45.5% |
| `grep` | 2848917 | LLGo · deadcode drop | 872701 | -69.4% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1381113 | -51.5% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 983571 | -65.5% |
| `glob` | 2257634 | LLGo · no LTO | 1121315 | -50.3% |
| `glob` | 2257634 | LLGo · deadcode drop | 522680 | -76.8% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1015638 | -55.0% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 685306 | -69.6% |
| `json-wasi` | 3314587 | LLGo · no LTO | 2772778 | -16.3% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1404312 | -57.6% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2591639 | -21.8% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1717446 | -48.2% |
| `llimport` | 8423078 | LLGo · no LTO | 8226608 | -2.3% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6850694 | -18.7% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 7303252 | -13.3% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 7039212 | -16.4% |
| `path-report` | 2381190 | LLGo · no LTO | 1242379 | -47.8% |
| `path-report` | 2381190 | LLGo · deadcode drop | 633915 | -73.4% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1130766 | -52.5% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 800247 | -66.4% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1918110 | -31.0% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1012148 | -63.6% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1792328 | -35.6% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1183471 | -57.4% |
| `word-count` | 2253620 | LLGo · no LTO | 1102054 | -51.1% |
| `word-count` | 2253620 | LLGo · deadcode drop | 516151 | -77.1% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 967798 | -57.1% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 668401 | -70.3% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 9.363x | 10 |
| LLGo · deadcode drop | 4.644x | 10 |
| LLGo · full LTO (GlobalDCE off) | 8.248x | 10 |
| LLGo · full LTO + GlobalDCE | 5.580x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1105185 | +1042.2% |
| `base64` | 96760 | LLGo · deadcode drop | 530631 | +448.4% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 881523 | +811.0% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 596245 | +516.2% |
| `checksum` | 92685 | LLGo · no LTO | 1089755 | +1075.8% |
| `checksum` | 92685 | LLGo · deadcode drop | 517241 | +458.1% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 865258 | +833.5% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 576900 | +522.4% |
| `conv-wasi` | 201149 | LLGo · no LTO | 1724653 | +757.4% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 850463 | +322.8% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1613669 | +702.2% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1003317 | +398.8% |
| `fibonacci` | 62386 | LLGo · no LTO | 901641 | +1345.3% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 432450 | +593.2% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 761215 | +1120.2% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 530998 | +751.1% |
| `grep` | 303772 | LLGo · no LTO | 1553518 | +411.4% |
| `grep` | 303772 | LLGo · deadcode drop | 872701 | +187.3% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1381113 | +354.7% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 983571 | +223.8% |
| `glob` | 93153 | LLGo · no LTO | 1121315 | +1103.7% |
| `glob` | 93153 | LLGo · deadcode drop | 522680 | +461.1% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1015638 | +990.3% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 685306 | +635.7% |
| `json-wasi` | 493590 | LLGo · no LTO | 2772778 | +461.8% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1404312 | +184.5% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2591639 | +425.1% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1717446 | +247.9% |
| `llimport` | — | LLGo · no LTO | 8226608 | — |
| `llimport` | — | LLGo · deadcode drop | 6850694 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 7303252 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 7039212 | — |
| `path-report` | 116889 | LLGo · no LTO | 1242379 | +962.9% |
| `path-report` | 116889 | LLGo · deadcode drop | 633915 | +442.3% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1130766 | +867.4% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 800247 | +584.6% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1918110 | +567.3% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1012148 | +252.1% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1792328 | +523.5% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1183471 | +311.7% |
| `word-count` | 86834 | LLGo · no LTO | 1102054 | +1169.2% |
| `word-count` | 86834 | LLGo · deadcode drop | 516151 | +494.4% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 967798 | +1014.5% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 668401 | +669.7% |
