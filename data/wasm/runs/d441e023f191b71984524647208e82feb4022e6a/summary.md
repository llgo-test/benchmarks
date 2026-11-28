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
| LLGo · no LTO | 0.913x | 11 |
| LLGo · deadcode drop | 0.561x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.812x | 11 |
| LLGo · full LTO + GlobalDCE | 0.566x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1911935 | -17.7% |
| `base64` | 2322402 | LLGo · deadcode drop | 1082015 | -53.4% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1666038 | -28.3% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1075131 | -53.7% |
| `checksum` | 2311672 | LLGo · no LTO | 1893475 | -18.1% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1068047 | -53.8% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1631662 | -29.4% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1042908 | -54.9% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2818361 | +6.8% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1591863 | -39.7% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2541678 | -3.7% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1625497 | -38.4% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1193519 | -47.5% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 959643 | -57.8% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 989831 | -56.5% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 858873 | -62.2% |
| `grep` | 2871426 | LLGo · no LTO | 2573087 | -10.4% |
| `grep` | 2871426 | LLGo · deadcode drop | 1588828 | -44.7% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2229367 | -22.4% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1558457 | -45.7% |
| `glob` | 2305059 | LLGo · no LTO | 1943360 | -15.7% |
| `glob` | 2305059 | LLGo · deadcode drop | 1086926 | -52.8% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1756146 | -23.8% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1148358 | -50.2% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4111734 | +23.2% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2323773 | -30.4% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3792995 | +13.6% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2540392 | -23.9% |
| `llimport` | 8440671 | LLGo · no LTO | 10951984 | +29.8% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9313120 | +10.3% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10047481 | +19.0% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 9007411 | +6.7% |
| `path-report` | 2428068 | LLGo · no LTO | 2086815 | -14.1% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1218215 | -49.8% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 1884821 | -22.4% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1277778 | -47.4% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3168170 | +12.7% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1897409 | -32.5% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2889162 | +2.8% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1967485 | -30.0% |
| `word-count` | 2300998 | LLGo · no LTO | 1903908 | -17.3% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1064564 | -53.7% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1714431 | -25.5% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1116945 | -51.5% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.386x | 10 |
| LLGo · deadcode drop | 6.771x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.097x | 10 |
| LLGo · full LTO + GlobalDCE | 6.864x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1911935 | +1009.6% |
| `base64` | 172302 | LLGo · deadcode drop | 1082015 | +528.0% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1666038 | +866.9% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1075131 | +524.0% |
| `checksum` | 169609 | LLGo · no LTO | 1893475 | +1016.4% |
| `checksum` | 169609 | LLGo · deadcode drop | 1068047 | +529.7% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1631662 | +862.0% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1042908 | +514.9% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2818361 | +1604.1% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1591863 | +862.5% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2541678 | +1436.8% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1625497 | +882.9% |
| `fibonacci` | 141855 | LLGo · no LTO | 1193519 | +741.4% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 959643 | +576.5% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 989831 | +597.8% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 858873 | +505.5% |
| `grep` | 155984 | LLGo · no LTO | 2573087 | +1549.6% |
| `grep` | 155984 | LLGo · deadcode drop | 1588828 | +918.6% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2229367 | +1329.2% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1558457 | +899.1% |
| `glob` | 136553 | LLGo · no LTO | 1943360 | +1323.2% |
| `glob` | 136553 | LLGo · deadcode drop | 1086926 | +696.0% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1756146 | +1186.1% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1148358 | +741.0% |
| `json-wasi` | 525666 | LLGo · no LTO | 4111734 | +682.2% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2323773 | +342.1% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3792995 | +621.6% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2540392 | +383.3% |
| `llimport` | — | LLGo · no LTO | 10951984 | — |
| `llimport` | — | LLGo · deadcode drop | 9313120 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10047481 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 9007411 | — |
| `path-report` | 194133 | LLGo · no LTO | 2086815 | +974.9% |
| `path-report` | 194133 | LLGo · deadcode drop | 1218215 | +527.5% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 1884821 | +870.9% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1277778 | +558.2% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3168170 | +800.1% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1897409 | +439.1% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2889162 | +720.9% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1967485 | +459.0% |
| `word-count` | 164053 | LLGo · no LTO | 1903908 | +1060.5% |
| `word-count` | 164053 | LLGo · deadcode drop | 1064564 | +548.9% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1714431 | +945.0% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1116945 | +580.8% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.311x | 11 |
| LLGo · deadcode drop | 0.311x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.467x | 11 |
| LLGo · full LTO + GlobalDCE | 0.340x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 547688 | -75.9% |
| `base64` | 2275731 | LLGo · deadcode drop | 547688 | -75.9% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 841538 | -63.0% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 580523 | -74.5% |
| `checksum` | 2264417 | LLGo · no LTO | 534717 | -76.4% |
| `checksum` | 2264417 | LLGo · deadcode drop | 534717 | -76.4% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 826364 | -63.5% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 562208 | -75.2% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 909695 | -65.1% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 909695 | -65.1% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1562660 | -40.1% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1006396 | -61.4% |
| `fibonacci` | 2230899 | LLGo · no LTO | 454562 | -79.6% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 454562 | -79.6% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 472905 | -78.8% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 426571 | -80.9% |
| `grep` | 2848917 | LLGo · no LTO | 887580 | -68.8% |
| `grep` | 2848917 | LLGo · deadcode drop | 887580 | -68.8% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1304151 | -54.2% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 933362 | -67.2% |
| `glob` | 2257634 | LLGo · no LTO | 540035 | -76.1% |
| `glob` | 2257634 | LLGo · deadcode drop | 540035 | -76.1% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 956523 | -57.6% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 654458 | -71.0% |
| `json-wasi` | 3314587 | LLGo · no LTO | 1461280 | -55.9% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1461280 | -55.9% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2498570 | -24.6% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1690583 | -49.0% |
| `llimport` | 8423078 | LLGo · no LTO | 6748514 | -19.9% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6748514 | -19.9% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 6880424 | -18.3% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6632408 | -21.3% |
| `path-report` | 2381190 | LLGo · no LTO | 651006 | -72.7% |
| `path-report` | 2381190 | LLGo · deadcode drop | 651006 | -72.7% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1063754 | -55.3% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 761233 | -68.0% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1077533 | -61.3% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1077533 | -61.3% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1743927 | -37.3% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1188495 | -57.3% |
| `word-count` | 2253620 | LLGo · no LTO | 534396 | -76.3% |
| `word-count` | 2253620 | LLGo · deadcode drop | 534396 | -76.3% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 915201 | -59.4% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 639720 | -71.6% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 4.832x | 10 |
| LLGo · deadcode drop | 4.832x | 10 |
| LLGo · full LTO (GlobalDCE off) | 7.539x | 10 |
| LLGo · full LTO + GlobalDCE | 5.323x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 547688 | +466.0% |
| `base64` | 96760 | LLGo · deadcode drop | 547688 | +466.0% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 841538 | +769.7% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 580523 | +500.0% |
| `checksum` | 92685 | LLGo · no LTO | 534717 | +476.9% |
| `checksum` | 92685 | LLGo · deadcode drop | 534717 | +476.9% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 826364 | +791.6% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 562208 | +506.6% |
| `conv-wasi` | 201149 | LLGo · no LTO | 909695 | +352.2% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 909695 | +352.2% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1562660 | +676.9% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1006396 | +400.3% |
| `fibonacci` | 62386 | LLGo · no LTO | 454562 | +628.6% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 454562 | +628.6% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 472905 | +658.0% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 426571 | +583.8% |
| `grep` | 303772 | LLGo · no LTO | 887580 | +192.2% |
| `grep` | 303772 | LLGo · deadcode drop | 887580 | +192.2% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1304151 | +329.3% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 933362 | +207.3% |
| `glob` | 93153 | LLGo · no LTO | 540035 | +479.7% |
| `glob` | 93153 | LLGo · deadcode drop | 540035 | +479.7% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 956523 | +926.8% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 654458 | +602.6% |
| `json-wasi` | 493590 | LLGo · no LTO | 1461280 | +196.1% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1461280 | +196.1% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2498570 | +406.2% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1690583 | +242.5% |
| `llimport` | — | LLGo · no LTO | 6748514 | — |
| `llimport` | — | LLGo · deadcode drop | 6748514 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 6880424 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6632408 | — |
| `path-report` | 116889 | LLGo · no LTO | 651006 | +456.9% |
| `path-report` | 116889 | LLGo · deadcode drop | 651006 | +456.9% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1063754 | +810.1% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 761233 | +551.2% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1077533 | +274.9% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1077533 | +274.9% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1743927 | +506.7% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1188495 | +313.5% |
| `word-count` | 86834 | LLGo · no LTO | 534396 | +515.4% |
| `word-count` | 86834 | LLGo · deadcode drop | 534396 | +515.4% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 915201 | +954.0% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 639720 | +636.7% |
