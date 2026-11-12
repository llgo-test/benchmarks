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
| LLGo · deadcode drop | 0.547x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.865x | 11 |
| LLGo · full LTO + GlobalDCE | 0.585x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1921351 | -17.3% |
| `base64` | 2322402 | LLGo · deadcode drop | 1057891 | -54.4% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1717224 | -26.1% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1096899 | -52.8% |
| `checksum` | 2311672 | LLGo · no LTO | 1901885 | -17.7% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1043289 | -54.9% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1680821 | -27.3% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1062993 | -54.0% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2783888 | +5.5% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1520625 | -42.4% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2582342 | -2.1% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1624377 | -38.4% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1699405 | -25.3% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 933310 | -59.0% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1490142 | -34.5% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 1004575 | -55.8% |
| `grep` | 2871426 | LLGo · no LTO | 2584946 | -10.0% |
| `grep` | 2871426 | LLGo · deadcode drop | 1564640 | -45.5% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2308674 | -19.6% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1609720 | -43.9% |
| `glob` | 2305059 | LLGo · no LTO | 1952364 | -15.3% |
| `glob` | 2305059 | LLGo · deadcode drop | 1062448 | -53.9% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1822750 | -20.9% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1186257 | -48.5% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4095718 | +22.7% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2264691 | -32.2% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3874867 | +16.1% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2581689 | -22.7% |
| `llimport` | 8440671 | LLGo · no LTO | 11090957 | +31.4% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9270889 | +9.8% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10416218 | +23.4% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 9298383 | +10.2% |
| `path-report` | 2428068 | LLGo · no LTO | 2098088 | -13.6% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1194225 | -50.8% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 1960432 | -19.3% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1324134 | -45.5% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3118723 | +10.9% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1807683 | -35.7% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2916248 | +3.7% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1952554 | -30.5% |
| `word-count` | 2300998 | LLGo · no LTO | 1911570 | -16.9% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1038795 | -54.9% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1777718 | -22.7% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1151667 | -49.9% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.791x | 10 |
| LLGo · deadcode drop | 6.587x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.790x | 10 |
| LLGo · full LTO + GlobalDCE | 7.098x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1921351 | +1015.1% |
| `base64` | 172302 | LLGo · deadcode drop | 1057891 | +514.0% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1717224 | +896.6% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1096899 | +536.6% |
| `checksum` | 169609 | LLGo · no LTO | 1901885 | +1021.3% |
| `checksum` | 169609 | LLGo · deadcode drop | 1043289 | +515.1% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1680821 | +891.0% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1062993 | +526.7% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2783888 | +1583.3% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1520625 | +819.4% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2582342 | +1461.4% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1624377 | +882.2% |
| `fibonacci` | 141855 | LLGo · no LTO | 1699405 | +1098.0% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 933310 | +557.9% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1490142 | +950.5% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 1004575 | +608.2% |
| `grep` | 155984 | LLGo · no LTO | 2584946 | +1557.2% |
| `grep` | 155984 | LLGo · deadcode drop | 1564640 | +903.1% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2308674 | +1380.1% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1609720 | +932.0% |
| `glob` | 136553 | LLGo · no LTO | 1952364 | +1329.7% |
| `glob` | 136553 | LLGo · deadcode drop | 1062448 | +678.0% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1822750 | +1234.8% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1186257 | +768.7% |
| `json-wasi` | 525666 | LLGo · no LTO | 4095718 | +679.1% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2264691 | +330.8% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3874867 | +637.1% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2581689 | +391.1% |
| `llimport` | — | LLGo · no LTO | 11090957 | — |
| `llimport` | — | LLGo · deadcode drop | 9270889 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10416218 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 9298383 | — |
| `path-report` | 194133 | LLGo · no LTO | 2098088 | +980.7% |
| `path-report` | 194133 | LLGo · deadcode drop | 1194225 | +515.2% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 1960432 | +909.8% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1324134 | +582.1% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3118723 | +786.1% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1807683 | +413.6% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2916248 | +728.5% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1952554 | +454.7% |
| `word-count` | 164053 | LLGo · no LTO | 1911570 | +1065.2% |
| `word-count` | 164053 | LLGo · deadcode drop | 1038795 | +533.2% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1777718 | +983.6% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1151667 | +602.0% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.579x | 11 |
| LLGo · deadcode drop | 0.301x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.510x | 11 |
| LLGo · full LTO + GlobalDCE | 0.356x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1105192 | -51.4% |
| `base64` | 2275731 | LLGo · deadcode drop | 530683 | -76.7% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 881569 | -61.3% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 596291 | -73.8% |
| `checksum` | 2264417 | LLGo · no LTO | 1089762 | -51.9% |
| `checksum` | 2264417 | LLGo · deadcode drop | 517293 | -77.2% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 865304 | -61.8% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 576946 | -74.5% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 1724509 | -33.9% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 850357 | -67.4% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1613564 | -38.1% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1003211 | -61.5% |
| `fibonacci` | 2230899 | LLGo · no LTO | 901648 | -59.6% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 432502 | -80.6% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 761261 | -65.9% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 531049 | -76.2% |
| `grep` | 2848917 | LLGo · no LTO | 1553521 | -45.5% |
| `grep` | 2848917 | LLGo · deadcode drop | 872769 | -69.4% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1381166 | -51.5% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 983620 | -65.5% |
| `glob` | 2257634 | LLGo · no LTO | 1121325 | -50.3% |
| `glob` | 2257634 | LLGo · deadcode drop | 522725 | -76.8% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1015680 | -55.0% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 685348 | -69.6% |
| `json-wasi` | 3314587 | LLGo · no LTO | 2772440 | -16.4% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1404038 | -57.6% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2591357 | -21.8% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1717175 | -48.2% |
| `llimport` | 8423078 | LLGo · no LTO | 8226281 | -2.3% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6850392 | -18.7% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 7303126 | -13.3% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 7038608 | -16.4% |
| `path-report` | 2381190 | LLGo · no LTO | 1242373 | -47.8% |
| `path-report` | 2381190 | LLGo · deadcode drop | 633960 | -73.4% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1130808 | -52.5% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 800289 | -66.4% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1917966 | -31.0% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1012042 | -63.6% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1792219 | -35.6% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1183361 | -57.4% |
| `word-count` | 2253620 | LLGo · no LTO | 1101915 | -51.1% |
| `word-count` | 2253620 | LLGo · deadcode drop | 516057 | -77.1% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 967693 | -57.1% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 668296 | -70.3% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 9.363x | 10 |
| LLGo · deadcode drop | 4.644x | 10 |
| LLGo · full LTO (GlobalDCE off) | 8.248x | 10 |
| LLGo · full LTO + GlobalDCE | 5.580x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1105192 | +1042.2% |
| `base64` | 96760 | LLGo · deadcode drop | 530683 | +448.5% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 881569 | +811.1% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 596291 | +516.3% |
| `checksum` | 92685 | LLGo · no LTO | 1089762 | +1075.8% |
| `checksum` | 92685 | LLGo · deadcode drop | 517293 | +458.1% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 865304 | +833.6% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 576946 | +522.5% |
| `conv-wasi` | 201149 | LLGo · no LTO | 1724509 | +757.3% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 850357 | +322.7% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1613564 | +702.2% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1003211 | +398.7% |
| `fibonacci` | 62386 | LLGo · no LTO | 901648 | +1345.3% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 432502 | +593.3% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 761261 | +1120.2% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 531049 | +751.2% |
| `grep` | 303772 | LLGo · no LTO | 1553521 | +411.4% |
| `grep` | 303772 | LLGo · deadcode drop | 872769 | +187.3% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1381166 | +354.7% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 983620 | +223.8% |
| `glob` | 93153 | LLGo · no LTO | 1121325 | +1103.7% |
| `glob` | 93153 | LLGo · deadcode drop | 522725 | +461.1% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1015680 | +990.3% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 685348 | +635.7% |
| `json-wasi` | 493590 | LLGo · no LTO | 2772440 | +461.7% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1404038 | +184.5% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2591357 | +425.0% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1717175 | +247.9% |
| `llimport` | — | LLGo · no LTO | 8226281 | — |
| `llimport` | — | LLGo · deadcode drop | 6850392 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 7303126 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 7038608 | — |
| `path-report` | 116889 | LLGo · no LTO | 1242373 | +962.9% |
| `path-report` | 116889 | LLGo · deadcode drop | 633960 | +442.4% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1130808 | +867.4% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 800289 | +584.7% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1917966 | +567.2% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1012042 | +252.1% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1792219 | +523.5% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1183361 | +311.7% |
| `word-count` | 86834 | LLGo · no LTO | 1101915 | +1169.0% |
| `word-count` | 86834 | LLGo · deadcode drop | 516057 | +494.3% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 967693 | +1014.4% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 668296 | +669.6% |
