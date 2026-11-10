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
| `base64` | 2322402 | LLGo · no LTO | 1920561 | -17.3% |
| `base64` | 2322402 | LLGo · deadcode drop | 1057206 | -54.5% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1716162 | -26.1% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1095883 | -52.8% |
| `checksum` | 2311672 | LLGo · no LTO | 1901115 | -17.8% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1042622 | -54.9% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1679766 | -27.3% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1061971 | -54.1% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2783422 | +5.5% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1520219 | -42.4% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2581557 | -2.2% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1623613 | -38.5% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1698619 | -25.3% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 932574 | -59.0% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1489049 | -34.5% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 1003553 | -55.9% |
| `grep` | 2871426 | LLGo · no LTO | 2584280 | -10.0% |
| `grep` | 2871426 | LLGo · deadcode drop | 1564052 | -45.5% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2307695 | -19.6% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1608753 | -44.0% |
| `glob` | 2305059 | LLGo · no LTO | 1951559 | -15.3% |
| `glob` | 2305059 | LLGo · deadcode drop | 1061757 | -53.9% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1821644 | -21.0% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1185206 | -48.6% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4095822 | +22.7% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2264793 | -32.2% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3875003 | +16.1% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2581720 | -22.7% |
| `llimport` | 8440671 | LLGo · no LTO | 11090637 | +31.4% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9270649 | +9.8% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10416657 | +23.4% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 9298842 | +10.2% |
| `path-report` | 2428068 | LLGo · no LTO | 2097276 | -13.6% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1193551 | -50.8% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 1959321 | -19.3% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1323111 | -45.5% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3118151 | +10.9% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1807249 | -35.7% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2915516 | +3.7% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1951778 | -30.6% |
| `word-count` | 2300998 | LLGo · no LTO | 1911036 | -16.9% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1038370 | -54.9% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1776901 | -22.8% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1150873 | -50.0% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.788x | 10 |
| LLGo · deadcode drop | 6.584x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.785x | 10 |
| LLGo · full LTO + GlobalDCE | 7.093x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1920561 | +1014.6% |
| `base64` | 172302 | LLGo · deadcode drop | 1057206 | +513.6% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1716162 | +896.0% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1095883 | +536.0% |
| `checksum` | 169609 | LLGo · no LTO | 1901115 | +1020.9% |
| `checksum` | 169609 | LLGo · deadcode drop | 1042622 | +514.7% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1679766 | +890.4% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1061971 | +526.1% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2783422 | +1583.0% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1520219 | +819.2% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2581557 | +1460.9% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1623613 | +881.7% |
| `fibonacci` | 141855 | LLGo · no LTO | 1698619 | +1097.4% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 932574 | +557.4% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1489049 | +949.7% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 1003553 | +607.4% |
| `grep` | 155984 | LLGo · no LTO | 2584280 | +1556.8% |
| `grep` | 155984 | LLGo · deadcode drop | 1564052 | +902.7% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2307695 | +1379.4% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1608753 | +931.4% |
| `glob` | 136553 | LLGo · no LTO | 1951559 | +1329.2% |
| `glob` | 136553 | LLGo · deadcode drop | 1061757 | +677.5% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1821644 | +1234.0% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1185206 | +767.9% |
| `json-wasi` | 525666 | LLGo · no LTO | 4095822 | +679.2% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2264793 | +330.8% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3875003 | +637.2% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2581720 | +391.1% |
| `llimport` | — | LLGo · no LTO | 11090637 | — |
| `llimport` | — | LLGo · deadcode drop | 9270649 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10416657 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 9298842 | — |
| `path-report` | 194133 | LLGo · no LTO | 2097276 | +980.3% |
| `path-report` | 194133 | LLGo · deadcode drop | 1193551 | +514.8% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 1959321 | +909.3% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1323111 | +581.5% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3118151 | +785.9% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1807249 | +413.5% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2915516 | +728.3% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1951778 | +454.5% |
| `word-count` | 164053 | LLGo · no LTO | 1911036 | +1064.9% |
| `word-count` | 164053 | LLGo · deadcode drop | 1038370 | +532.9% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1776901 | +983.1% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1150873 | +601.5% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.578x | 11 |
| LLGo · deadcode drop | 0.301x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.510x | 11 |
| LLGo · full LTO + GlobalDCE | 0.356x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1104756 | -51.5% |
| `base64` | 2275731 | LLGo · deadcode drop | 530277 | -76.7% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 881059 | -61.3% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 595775 | -73.8% |
| `checksum` | 2264417 | LLGo · no LTO | 1089326 | -51.9% |
| `checksum` | 2264417 | LLGo · deadcode drop | 516887 | -77.2% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 864788 | -61.8% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 576416 | -74.5% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 1724225 | -33.9% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 850109 | -67.4% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1613405 | -38.1% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1003033 | -61.5% |
| `fibonacci` | 2230899 | LLGo · no LTO | 901212 | -59.6% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 432096 | -80.6% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 760745 | -65.9% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 530522 | -76.2% |
| `grep` | 2848917 | LLGo · no LTO | 1553151 | -45.5% |
| `grep` | 2848917 | LLGo · deadcode drop | 872424 | -69.4% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1380697 | -51.5% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 983130 | -65.5% |
| `glob` | 2257634 | LLGo · no LTO | 1120886 | -50.4% |
| `glob` | 2257634 | LLGo · deadcode drop | 522326 | -76.9% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1015168 | -55.0% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 684830 | -69.7% |
| `json-wasi` | 3314587 | LLGo · no LTO | 2772408 | -16.4% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1403952 | -57.6% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2591512 | -21.8% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1717230 | -48.2% |
| `llimport` | 8423078 | LLGo · no LTO | 8226254 | -2.3% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6850417 | -18.7% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 7303125 | -13.3% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 7039037 | -16.4% |
| `path-report` | 2381190 | LLGo · no LTO | 1241950 | -47.8% |
| `path-report` | 2381190 | LLGo · deadcode drop | 633561 | -73.4% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1130296 | -52.5% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 799793 | -66.4% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1917682 | -31.0% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1011816 | -63.6% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1792078 | -35.6% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1183207 | -57.5% |
| `word-count` | 2253620 | LLGo · no LTO | 1101625 | -51.1% |
| `word-count` | 2253620 | LLGo · deadcode drop | 515797 | -77.1% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 967328 | -57.1% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 667925 | -70.4% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 9.360x | 10 |
| LLGo · deadcode drop | 4.642x | 10 |
| LLGo · full LTO (GlobalDCE off) | 8.245x | 10 |
| LLGo · full LTO + GlobalDCE | 5.577x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1104756 | +1041.7% |
| `base64` | 96760 | LLGo · deadcode drop | 530277 | +448.0% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 881059 | +810.6% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 595775 | +515.7% |
| `checksum` | 92685 | LLGo · no LTO | 1089326 | +1075.3% |
| `checksum` | 92685 | LLGo · deadcode drop | 516887 | +457.7% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 864788 | +833.0% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 576416 | +521.9% |
| `conv-wasi` | 201149 | LLGo · no LTO | 1724225 | +757.2% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 850109 | +322.6% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1613405 | +702.1% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1003033 | +398.7% |
| `fibonacci` | 62386 | LLGo · no LTO | 901212 | +1344.6% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 432096 | +592.6% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 760745 | +1119.4% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 530522 | +750.4% |
| `grep` | 303772 | LLGo · no LTO | 1553151 | +411.3% |
| `grep` | 303772 | LLGo · deadcode drop | 872424 | +187.2% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1380697 | +354.5% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 983130 | +223.6% |
| `glob` | 93153 | LLGo · no LTO | 1120886 | +1103.3% |
| `glob` | 93153 | LLGo · deadcode drop | 522326 | +460.7% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1015168 | +989.8% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 684830 | +635.2% |
| `json-wasi` | 493590 | LLGo · no LTO | 2772408 | +461.7% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1403952 | +184.4% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2591512 | +425.0% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1717230 | +247.9% |
| `llimport` | — | LLGo · no LTO | 8226254 | — |
| `llimport` | — | LLGo · deadcode drop | 6850417 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 7303125 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 7039037 | — |
| `path-report` | 116889 | LLGo · no LTO | 1241950 | +962.5% |
| `path-report` | 116889 | LLGo · deadcode drop | 633561 | +442.0% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1130296 | +867.0% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 799793 | +584.2% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1917682 | +567.1% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1011816 | +252.0% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1792078 | +523.4% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1183207 | +311.6% |
| `word-count` | 86834 | LLGo · no LTO | 1101625 | +1168.7% |
| `word-count` | 86834 | LLGo · deadcode drop | 515797 | +494.0% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 967328 | +1014.0% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 667925 | +669.2% |
