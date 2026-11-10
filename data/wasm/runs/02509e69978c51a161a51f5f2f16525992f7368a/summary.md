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
| `base64` | 2322402 | LLGo · no LTO | 1920475 | -17.3% |
| `base64` | 2322402 | LLGo · deadcode drop | 1056870 | -54.5% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1716231 | -26.1% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1095900 | -52.8% |
| `checksum` | 2311672 | LLGo · no LTO | 1901016 | -17.8% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1042263 | -54.9% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1679759 | -27.3% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1061937 | -54.1% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2783193 | +5.5% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1519858 | -42.4% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2581476 | -2.2% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1623441 | -38.5% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1698549 | -25.3% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 932247 | -59.0% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1489155 | -34.5% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 1003629 | -55.9% |
| `grep` | 2871426 | LLGo · no LTO | 2583910 | -10.0% |
| `grep` | 2871426 | LLGo · deadcode drop | 1563232 | -45.6% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2307549 | -19.6% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1608565 | -44.0% |
| `glob` | 2305059 | LLGo · no LTO | 1951461 | -15.3% |
| `glob` | 2305059 | LLGo · deadcode drop | 1061409 | -54.0% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1821682 | -21.0% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1185184 | -48.6% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4096325 | +22.7% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2264910 | -32.2% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3875347 | +16.1% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2582127 | -22.7% |
| `llimport` | 8440671 | LLGo · no LTO | 11080622 | +31.3% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9256254 | +9.7% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10406714 | +23.3% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 9288718 | +10.0% |
| `path-report` | 2428068 | LLGo · no LTO | 2097148 | -13.6% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1193097 | -50.9% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 1959319 | -19.3% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1323059 | -45.5% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3117790 | +10.9% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1806631 | -35.7% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2915291 | +3.7% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1951578 | -30.6% |
| `word-count` | 2300998 | LLGo · no LTO | 1910897 | -17.0% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1038125 | -54.9% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1776763 | -22.8% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1150714 | -50.0% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.787x | 10 |
| LLGo · deadcode drop | 6.582x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.785x | 10 |
| LLGo · full LTO + GlobalDCE | 7.093x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1920475 | +1014.6% |
| `base64` | 172302 | LLGo · deadcode drop | 1056870 | +513.4% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1716231 | +896.1% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1095900 | +536.0% |
| `checksum` | 169609 | LLGo · no LTO | 1901016 | +1020.8% |
| `checksum` | 169609 | LLGo · deadcode drop | 1042263 | +514.5% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1679759 | +890.4% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1061937 | +526.1% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2783193 | +1582.9% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1519858 | +819.0% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2581476 | +1460.9% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1623441 | +881.6% |
| `fibonacci` | 141855 | LLGo · no LTO | 1698549 | +1097.4% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 932247 | +557.2% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1489155 | +949.8% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 1003629 | +607.5% |
| `grep` | 155984 | LLGo · no LTO | 2583910 | +1556.5% |
| `grep` | 155984 | LLGo · deadcode drop | 1563232 | +902.2% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2307549 | +1379.3% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1608565 | +931.2% |
| `glob` | 136553 | LLGo · no LTO | 1951461 | +1329.1% |
| `glob` | 136553 | LLGo · deadcode drop | 1061409 | +677.3% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1821682 | +1234.0% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1185184 | +767.9% |
| `json-wasi` | 525666 | LLGo · no LTO | 4096325 | +679.3% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2264910 | +330.9% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3875347 | +637.2% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2582127 | +391.2% |
| `llimport` | — | LLGo · no LTO | 11080622 | — |
| `llimport` | — | LLGo · deadcode drop | 9256254 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10406714 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 9288718 | — |
| `path-report` | 194133 | LLGo · no LTO | 2097148 | +980.3% |
| `path-report` | 194133 | LLGo · deadcode drop | 1193097 | +514.6% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 1959319 | +909.3% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1323059 | +581.5% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3117790 | +785.8% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1806631 | +413.3% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2915291 | +728.3% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1951578 | +454.5% |
| `word-count` | 164053 | LLGo · no LTO | 1910897 | +1064.8% |
| `word-count` | 164053 | LLGo · deadcode drop | 1038125 | +532.8% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1776763 | +983.0% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1150714 | +601.4% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.578x | 11 |
| LLGo · deadcode drop | 0.301x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.510x | 11 |
| LLGo · full LTO + GlobalDCE | 0.356x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1104312 | -51.5% |
| `base64` | 2275731 | LLGo · deadcode drop | 530277 | -76.7% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 880737 | -61.3% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 595678 | -73.8% |
| `checksum` | 2264417 | LLGo · no LTO | 1088882 | -51.9% |
| `checksum` | 2264417 | LLGo · deadcode drop | 516887 | -77.2% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 864466 | -61.8% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 576319 | -74.5% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 1723342 | -33.9% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 849722 | -67.4% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1612754 | -38.2% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1002524 | -61.6% |
| `fibonacci` | 2230899 | LLGo · no LTO | 900887 | -59.6% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 432096 | -80.6% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 760588 | -65.9% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 530590 | -76.2% |
| `grep` | 2848917 | LLGo · no LTO | 1552266 | -45.5% |
| `grep` | 2848917 | LLGo · deadcode drop | 871597 | -69.4% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1380060 | -51.6% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 982749 | -65.5% |
| `glob` | 2257634 | LLGo · no LTO | 1120442 | -50.4% |
| `glob` | 2257634 | LLGo · deadcode drop | 522326 | -76.9% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1014842 | -55.0% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 684725 | -69.7% |
| `json-wasi` | 3314587 | LLGo · no LTO | 2771891 | -16.4% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1403741 | -57.6% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2591319 | -21.8% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1717342 | -48.2% |
| `llimport` | 8423078 | LLGo · no LTO | 8210520 | -2.5% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6831293 | -18.9% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 7287992 | -13.5% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 7023974 | -16.6% |
| `path-report` | 2381190 | LLGo · no LTO | 1241437 | -47.9% |
| `path-report` | 2381190 | LLGo · deadcode drop | 633369 | -73.4% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1129887 | -52.5% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 799613 | -66.4% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1916603 | -31.1% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1011080 | -63.6% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1791264 | -35.6% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1182559 | -57.5% |
| `word-count` | 2253620 | LLGo · no LTO | 1101058 | -51.1% |
| `word-count` | 2253620 | LLGo · deadcode drop | 515528 | -77.1% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 966840 | -57.1% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 667650 | -70.4% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 9.356x | 10 |
| LLGo · deadcode drop | 4.640x | 10 |
| LLGo · full LTO (GlobalDCE off) | 8.242x | 10 |
| LLGo · full LTO + GlobalDCE | 5.576x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1104312 | +1041.3% |
| `base64` | 96760 | LLGo · deadcode drop | 530277 | +448.0% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 880737 | +810.2% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 595678 | +515.6% |
| `checksum` | 92685 | LLGo · no LTO | 1088882 | +1074.8% |
| `checksum` | 92685 | LLGo · deadcode drop | 516887 | +457.7% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 864466 | +832.7% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 576319 | +521.8% |
| `conv-wasi` | 201149 | LLGo · no LTO | 1723342 | +756.7% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 849722 | +322.4% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1612754 | +701.8% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1002524 | +398.4% |
| `fibonacci` | 62386 | LLGo · no LTO | 900887 | +1344.1% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 432096 | +592.6% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 760588 | +1119.2% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 530590 | +750.5% |
| `grep` | 303772 | LLGo · no LTO | 1552266 | +411.0% |
| `grep` | 303772 | LLGo · deadcode drop | 871597 | +186.9% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1380060 | +354.3% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 982749 | +223.5% |
| `glob` | 93153 | LLGo · no LTO | 1120442 | +1102.8% |
| `glob` | 93153 | LLGo · deadcode drop | 522326 | +460.7% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1014842 | +989.4% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 684725 | +635.1% |
| `json-wasi` | 493590 | LLGo · no LTO | 2771891 | +461.6% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1403741 | +184.4% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2591319 | +425.0% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1717342 | +247.9% |
| `llimport` | — | LLGo · no LTO | 8210520 | — |
| `llimport` | — | LLGo · deadcode drop | 6831293 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 7287992 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 7023974 | — |
| `path-report` | 116889 | LLGo · no LTO | 1241437 | +962.1% |
| `path-report` | 116889 | LLGo · deadcode drop | 633369 | +441.9% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1129887 | +866.6% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 799613 | +584.1% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1916603 | +566.8% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1011080 | +251.7% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1791264 | +523.2% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1182559 | +311.4% |
| `word-count` | 86834 | LLGo · no LTO | 1101058 | +1168.0% |
| `word-count` | 86834 | LLGo · deadcode drop | 515528 | +493.7% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 966840 | +1013.4% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 667650 | +668.9% |
