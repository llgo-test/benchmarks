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
| LLGo · no LTO | 0.900x | 11 |
| LLGo · deadcode drop | 0.547x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.825x | 11 |
| LLGo · full LTO + GlobalDCE | 0.568x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1892993 | -18.5% |
| `base64` | 2322402 | LLGo · deadcode drop | 1059329 | -54.4% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1696306 | -27.0% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1074900 | -53.7% |
| `checksum` | 2311672 | LLGo · no LTO | 1873689 | -18.9% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1044537 | -54.8% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1661004 | -28.1% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1042025 | -54.9% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2747299 | +4.1% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1522117 | -42.3% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2556700 | -3.1% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1597925 | -39.4% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1165640 | -48.7% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 934947 | -58.9% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 981890 | -56.8% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 849528 | -62.6% |
| `grep` | 2871426 | LLGo · no LTO | 2549753 | -11.2% |
| `grep` | 2871426 | LLGo · deadcode drop | 1563882 | -45.5% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2283164 | -20.5% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1582415 | -44.9% |
| `glob` | 2305059 | LLGo · no LTO | 1924211 | -16.5% |
| `glob` | 2305059 | LLGo · deadcode drop | 1063834 | -53.8% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1800047 | -21.9% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1162258 | -49.6% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4050753 | +21.3% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2262691 | -32.2% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3851549 | +15.4% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2552582 | -23.5% |
| `llimport` | 8440671 | LLGo · no LTO | 10923548 | +29.4% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9254065 | +9.6% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10310154 | +22.1% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 9215960 | +9.2% |
| `path-report` | 2428068 | LLGo · no LTO | 2068042 | -14.8% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1195387 | -50.8% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 1936526 | -20.2% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1299687 | -46.5% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3090384 | +9.9% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1827901 | -35.0% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2907594 | +3.4% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1942292 | -30.9% |
| `word-count` | 2300998 | LLGo · no LTO | 1883225 | -18.2% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1040111 | -54.8% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1755117 | -23.7% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1127765 | -51.0% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.218x | 10 |
| LLGo · deadcode drop | 6.599x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.255x | 10 |
| LLGo · full LTO + GlobalDCE | 6.876x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1892993 | +998.6% |
| `base64` | 172302 | LLGo · deadcode drop | 1059329 | +514.8% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1696306 | +884.5% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1074900 | +523.8% |
| `checksum` | 169609 | LLGo · no LTO | 1873689 | +1004.7% |
| `checksum` | 169609 | LLGo · deadcode drop | 1044537 | +515.8% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1661004 | +879.3% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1042025 | +514.4% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2747299 | +1561.2% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1522117 | +820.3% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2556700 | +1445.9% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1597925 | +866.2% |
| `fibonacci` | 141855 | LLGo · no LTO | 1165640 | +721.7% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 934947 | +559.1% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 981890 | +592.2% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 849528 | +498.9% |
| `grep` | 155984 | LLGo · no LTO | 2549753 | +1534.6% |
| `grep` | 155984 | LLGo · deadcode drop | 1563882 | +902.6% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2283164 | +1363.7% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1582415 | +914.5% |
| `glob` | 136553 | LLGo · no LTO | 1924211 | +1309.1% |
| `glob` | 136553 | LLGo · deadcode drop | 1063834 | +679.1% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1800047 | +1218.2% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1162258 | +751.1% |
| `json-wasi` | 525666 | LLGo · no LTO | 4050753 | +670.6% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2262691 | +330.4% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3851549 | +632.7% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2552582 | +385.6% |
| `llimport` | — | LLGo · no LTO | 10923548 | — |
| `llimport` | — | LLGo · deadcode drop | 9254065 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10310154 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 9215960 | — |
| `path-report` | 194133 | LLGo · no LTO | 2068042 | +965.3% |
| `path-report` | 194133 | LLGo · deadcode drop | 1195387 | +515.8% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 1936526 | +897.5% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1299687 | +569.5% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3090384 | +778.0% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1827901 | +419.3% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2907594 | +726.1% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1942292 | +451.8% |
| `word-count` | 164053 | LLGo · no LTO | 1883225 | +1047.9% |
| `word-count` | 164053 | LLGo · deadcode drop | 1040111 | +534.0% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1755117 | +969.8% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1127765 | +587.4% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.542x | 11 |
| LLGo · deadcode drop | 0.300x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.480x | 11 |
| LLGo · full LTO + GlobalDCE | 0.340x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1080280 | -52.5% |
| `base64` | 2275731 | LLGo · deadcode drop | 530133 | -76.7% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 868397 | -61.8% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 579873 | -74.5% |
| `checksum` | 2264417 | LLGo · no LTO | 1064967 | -53.0% |
| `checksum` | 2264417 | LLGo · deadcode drop | 516556 | -77.2% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 852602 | -62.3% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 560973 | -75.2% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 1687402 | -35.3% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 848869 | -67.5% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1592669 | -38.9% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 981472 | -62.4% |
| `fibonacci` | 2230899 | LLGo · no LTO | 564351 | -74.7% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 432077 | -80.6% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 455708 | -79.6% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 413928 | -81.4% |
| `grep` | 2848917 | LLGo · no LTO | 1517997 | -46.7% |
| `grep` | 2848917 | LLGo · deadcode drop | 867031 | -69.6% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1354862 | -52.4% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 953744 | -66.5% |
| `glob` | 2257634 | LLGo · no LTO | 1096538 | -51.4% |
| `glob` | 2257634 | LLGo · deadcode drop | 522203 | -76.9% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1000217 | -55.7% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 666615 | -70.5% |
| `json-wasi` | 3314587 | LLGo · no LTO | 2719850 | -17.9% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1399134 | -57.8% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2570238 | -22.5% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1689817 | -49.0% |
| `llimport` | 8423078 | LLGo · no LTO | 7877701 | -6.5% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6643071 | -21.1% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 7048362 | -16.3% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6773853 | -19.6% |
| `path-report` | 2381190 | LLGo · no LTO | 1215490 | -49.0% |
| `path-report` | 2381190 | LLGo · deadcode drop | 633118 | -73.4% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1114172 | -53.2% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 780095 | -67.2% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1879684 | -32.4% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1013084 | -63.6% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1772634 | -36.3% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1162649 | -58.2% |
| `word-count` | 2253620 | LLGo · no LTO | 1077119 | -52.2% |
| `word-count` | 2253620 | LLGo · deadcode drop | 515558 | -77.1% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 952118 | -57.8% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 649395 | -71.2% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 8.760x | 10 |
| LLGo · deadcode drop | 4.636x | 10 |
| LLGo · full LTO (GlobalDCE off) | 7.736x | 10 |
| LLGo · full LTO + GlobalDCE | 5.322x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1080280 | +1016.5% |
| `base64` | 96760 | LLGo · deadcode drop | 530133 | +447.9% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 868397 | +797.5% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 579873 | +499.3% |
| `checksum` | 92685 | LLGo · no LTO | 1064967 | +1049.0% |
| `checksum` | 92685 | LLGo · deadcode drop | 516556 | +457.3% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 852602 | +819.9% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 560973 | +505.2% |
| `conv-wasi` | 201149 | LLGo · no LTO | 1687402 | +738.9% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 848869 | +322.0% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1592669 | +691.8% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 981472 | +387.9% |
| `fibonacci` | 62386 | LLGo · no LTO | 564351 | +804.6% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 432077 | +592.6% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 455708 | +630.5% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 413928 | +563.5% |
| `grep` | 303772 | LLGo · no LTO | 1517997 | +399.7% |
| `grep` | 303772 | LLGo · deadcode drop | 867031 | +185.4% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1354862 | +346.0% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 953744 | +214.0% |
| `glob` | 93153 | LLGo · no LTO | 1096538 | +1077.1% |
| `glob` | 93153 | LLGo · deadcode drop | 522203 | +460.6% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1000217 | +973.7% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 666615 | +615.6% |
| `json-wasi` | 493590 | LLGo · no LTO | 2719850 | +451.0% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1399134 | +183.5% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2570238 | +420.7% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1689817 | +242.4% |
| `llimport` | — | LLGo · no LTO | 7877701 | — |
| `llimport` | — | LLGo · deadcode drop | 6643071 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 7048362 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6773853 | — |
| `path-report` | 116889 | LLGo · no LTO | 1215490 | +939.9% |
| `path-report` | 116889 | LLGo · deadcode drop | 633118 | +441.6% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1114172 | +853.2% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 780095 | +567.4% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1879684 | +553.9% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1013084 | +252.4% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1772634 | +516.7% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1162649 | +304.5% |
| `word-count` | 86834 | LLGo · no LTO | 1077119 | +1140.4% |
| `word-count` | 86834 | LLGo · deadcode drop | 515558 | +493.7% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 952118 | +996.5% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 649395 | +647.9% |
