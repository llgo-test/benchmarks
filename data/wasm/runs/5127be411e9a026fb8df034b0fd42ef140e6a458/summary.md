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
| LLGo · no LTO | 0.907x | 11 |
| LLGo · deadcode drop | 0.554x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.832x | 11 |
| LLGo · full LTO + GlobalDCE | 0.575x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1910813 | -17.7% |
| `base64` | 2322402 | LLGo · deadcode drop | 1076375 | -53.7% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1715097 | -26.1% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1093753 | -52.9% |
| `checksum` | 2311672 | LLGo · no LTO | 1891547 | -18.2% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1061596 | -54.1% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1679345 | -27.4% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1060434 | -54.1% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2761089 | +4.6% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1541468 | -41.6% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2571597 | -2.5% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1618535 | -38.7% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1183863 | -47.9% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 951879 | -58.1% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1000430 | -56.0% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 867919 | -61.8% |
| `grep` | 2871426 | LLGo · no LTO | 2567371 | -10.6% |
| `grep` | 2871426 | LLGo · deadcode drop | 1580284 | -45.0% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2301280 | -19.9% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1600429 | -44.3% |
| `glob` | 2305059 | LLGo · no LTO | 1942053 | -15.7% |
| `glob` | 2305059 | LLGo · deadcode drop | 1080892 | -53.1% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1818358 | -21.1% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1180634 | -48.8% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4057944 | +21.6% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2269958 | -32.0% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3859363 | +15.6% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2560645 | -23.3% |
| `llimport` | 8440671 | LLGo · no LTO | 10930649 | +29.5% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9261610 | +9.7% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10318041 | +22.2% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 9223970 | +9.3% |
| `path-report` | 2428068 | LLGo · no LTO | 2085864 | -14.1% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1212334 | -50.1% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 1954805 | -19.5% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1318063 | -45.7% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3104159 | +10.4% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1847287 | -34.3% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2922644 | +4.0% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1963064 | -30.2% |
| `word-count` | 2300998 | LLGo · no LTO | 1901129 | -17.4% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1057151 | -54.1% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1773451 | -22.9% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1146159 | -50.2% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.308x | 10 |
| LLGo · deadcode drop | 6.687x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.349x | 10 |
| LLGo · full LTO + GlobalDCE | 6.973x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1910813 | +1009.0% |
| `base64` | 172302 | LLGo · deadcode drop | 1076375 | +524.7% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1715097 | +895.4% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1093753 | +534.8% |
| `checksum` | 169609 | LLGo · no LTO | 1891547 | +1015.2% |
| `checksum` | 169609 | LLGo · deadcode drop | 1061596 | +525.9% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1679345 | +890.1% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1060434 | +525.2% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2761089 | +1569.5% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1541468 | +832.0% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2571597 | +1454.9% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1618535 | +878.6% |
| `fibonacci` | 141855 | LLGo · no LTO | 1183863 | +734.6% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 951879 | +571.0% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1000430 | +605.2% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 867919 | +511.8% |
| `grep` | 155984 | LLGo · no LTO | 2567371 | +1545.9% |
| `grep` | 155984 | LLGo · deadcode drop | 1580284 | +913.1% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2301280 | +1375.3% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1600429 | +926.0% |
| `glob` | 136553 | LLGo · no LTO | 1942053 | +1322.2% |
| `glob` | 136553 | LLGo · deadcode drop | 1080892 | +691.6% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1818358 | +1231.6% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1180634 | +764.6% |
| `json-wasi` | 525666 | LLGo · no LTO | 4057944 | +672.0% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2269958 | +331.8% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3859363 | +634.2% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2560645 | +387.1% |
| `llimport` | — | LLGo · no LTO | 10930649 | — |
| `llimport` | — | LLGo · deadcode drop | 9261610 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10318041 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 9223970 | — |
| `path-report` | 194133 | LLGo · no LTO | 2085864 | +974.5% |
| `path-report` | 194133 | LLGo · deadcode drop | 1212334 | +524.5% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 1954805 | +906.9% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1318063 | +578.9% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3104159 | +781.9% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1847287 | +424.8% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2922644 | +730.4% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1963064 | +457.7% |
| `word-count` | 164053 | LLGo · no LTO | 1901129 | +1058.9% |
| `word-count` | 164053 | LLGo · deadcode drop | 1057151 | +544.4% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1773451 | +981.0% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1146159 | +598.7% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.548x | 11 |
| LLGo · deadcode drop | 0.306x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.487x | 11 |
| LLGo · full LTO + GlobalDCE | 0.348x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1094672 | -51.9% |
| `base64` | 2275731 | LLGo · deadcode drop | 543916 | -76.1% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 885537 | -61.1% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 597647 | -73.7% |
| `checksum` | 2264417 | LLGo · no LTO | 1079363 | -52.3% |
| `checksum` | 2264417 | LLGo · deadcode drop | 530311 | -76.6% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 869695 | -61.6% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 578702 | -74.4% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 1701220 | -34.8% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 866300 | -66.8% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1607353 | -38.4% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1000121 | -61.7% |
| `fibonacci` | 2230899 | LLGo · no LTO | 580083 | -74.0% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 446930 | -80.0% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 474059 | -78.8% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 432845 | -80.6% |
| `grep` | 2848917 | LLGo · no LTO | 1532393 | -46.2% |
| `grep` | 2848917 | LLGo · deadcode drop | 880388 | -69.1% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1371957 | -51.8% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 971066 | -65.9% |
| `glob` | 2257634 | LLGo · no LTO | 1110918 | -50.8% |
| `glob` | 2257634 | LLGo · deadcode drop | 535958 | -76.3% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1017320 | -54.9% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 684346 | -69.7% |
| `json-wasi` | 3314587 | LLGo · no LTO | 2729024 | -17.7% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1408603 | -57.5% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2580121 | -22.2% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1699841 | -48.7% |
| `llimport` | 8423078 | LLGo · no LTO | 7886875 | -6.4% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6652562 | -21.0% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 7058245 | -16.2% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6783743 | -19.5% |
| `path-report` | 2381190 | LLGo · no LTO | 1229870 | -48.4% |
| `path-report` | 2381190 | LLGo · deadcode drop | 646765 | -72.8% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1131267 | -52.5% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 797824 | -66.5% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1893506 | -31.9% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1030538 | -62.9% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1787250 | -35.7% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1181255 | -57.5% |
| `word-count` | 2253620 | LLGo · no LTO | 1091499 | -51.6% |
| `word-count` | 2253620 | LLGo · deadcode drop | 529313 | -76.5% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 969213 | -57.0% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 667126 | -70.4% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 8.866x | 10 |
| LLGo · deadcode drop | 4.739x | 10 |
| LLGo · full LTO (GlobalDCE off) | 7.863x | 10 |
| LLGo · full LTO + GlobalDCE | 5.452x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1094672 | +1031.3% |
| `base64` | 96760 | LLGo · deadcode drop | 543916 | +462.1% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 885537 | +815.2% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 597647 | +517.7% |
| `checksum` | 92685 | LLGo · no LTO | 1079363 | +1064.5% |
| `checksum` | 92685 | LLGo · deadcode drop | 530311 | +472.2% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 869695 | +838.3% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 578702 | +524.4% |
| `conv-wasi` | 201149 | LLGo · no LTO | 1701220 | +745.8% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 866300 | +330.7% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1607353 | +699.1% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1000121 | +397.2% |
| `fibonacci` | 62386 | LLGo · no LTO | 580083 | +829.8% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 446930 | +616.4% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 474059 | +659.9% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 432845 | +593.8% |
| `grep` | 303772 | LLGo · no LTO | 1532393 | +404.5% |
| `grep` | 303772 | LLGo · deadcode drop | 880388 | +189.8% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1371957 | +351.6% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 971066 | +219.7% |
| `glob` | 93153 | LLGo · no LTO | 1110918 | +1092.6% |
| `glob` | 93153 | LLGo · deadcode drop | 535958 | +475.4% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1017320 | +992.1% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 684346 | +634.6% |
| `json-wasi` | 493590 | LLGo · no LTO | 2729024 | +452.9% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1408603 | +185.4% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2580121 | +422.7% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1699841 | +244.4% |
| `llimport` | — | LLGo · no LTO | 7886875 | — |
| `llimport` | — | LLGo · deadcode drop | 6652562 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 7058245 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6783743 | — |
| `path-report` | 116889 | LLGo · no LTO | 1229870 | +952.2% |
| `path-report` | 116889 | LLGo · deadcode drop | 646765 | +453.3% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1131267 | +867.8% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 797824 | +582.5% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1893506 | +558.7% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1030538 | +258.5% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1787250 | +521.8% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1181255 | +310.9% |
| `word-count` | 86834 | LLGo · no LTO | 1091499 | +1157.0% |
| `word-count` | 86834 | LLGo · deadcode drop | 529313 | +509.6% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 969213 | +1016.2% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 667126 | +668.3% |
