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
| LLGo · full LTO + GlobalDCE | 0.586x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1920345 | -17.3% |
| `base64` | 2322402 | LLGo · deadcode drop | 1057888 | -54.4% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1716134 | -26.1% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1096703 | -52.8% |
| `checksum` | 2311672 | LLGo · no LTO | 1900884 | -17.8% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1043291 | -54.9% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1679739 | -27.3% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1062762 | -54.0% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2782955 | +5.5% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1520651 | -42.4% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2581165 | -2.2% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1624120 | -38.4% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1698409 | -25.3% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 933314 | -59.0% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1489038 | -34.5% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 1004382 | -55.8% |
| `grep` | 2871426 | LLGo · no LTO | 2584126 | -10.0% |
| `grep` | 2871426 | LLGo · deadcode drop | 1564787 | -45.5% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2307607 | -19.6% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1609526 | -43.9% |
| `glob` | 2305059 | LLGo · no LTO | 1951351 | -15.3% |
| `glob` | 2305059 | LLGo · deadcode drop | 1062421 | -53.9% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1821648 | -21.0% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1186056 | -48.5% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4094700 | +22.7% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2264709 | -32.2% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3874123 | +16.0% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2581666 | -22.7% |
| `llimport` | 8440671 | LLGo · no LTO | 11106549 | +31.6% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9288680 | +10.0% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10433329 | +23.6% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 9317090 | +10.4% |
| `path-report` | 2428068 | LLGo · no LTO | 2097072 | -13.6% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1194237 | -50.8% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 1959289 | -19.3% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1323948 | -45.5% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3136701 | +11.6% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1826219 | -35.0% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2933740 | +4.4% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1970885 | -29.9% |
| `word-count` | 2300998 | LLGo · no LTO | 1910569 | -17.0% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1038790 | -54.9% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1776611 | -22.8% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1151451 | -50.0% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.793x | 10 |
| LLGo · deadcode drop | 6.593x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.791x | 10 |
| LLGo · full LTO + GlobalDCE | 7.104x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1920345 | +1014.5% |
| `base64` | 172302 | LLGo · deadcode drop | 1057888 | +514.0% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1716134 | +896.0% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1096703 | +536.5% |
| `checksum` | 169609 | LLGo · no LTO | 1900884 | +1020.7% |
| `checksum` | 169609 | LLGo · deadcode drop | 1043291 | +515.1% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1679739 | +890.4% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1062762 | +526.6% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2782955 | +1582.7% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1520651 | +819.5% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2581165 | +1460.7% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1624120 | +882.0% |
| `fibonacci` | 141855 | LLGo · no LTO | 1698409 | +1097.3% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 933314 | +557.9% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1489038 | +949.7% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 1004382 | +608.0% |
| `grep` | 155984 | LLGo · no LTO | 2584126 | +1556.7% |
| `grep` | 155984 | LLGo · deadcode drop | 1564787 | +903.2% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2307607 | +1379.4% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1609526 | +931.9% |
| `glob` | 136553 | LLGo · no LTO | 1951351 | +1329.0% |
| `glob` | 136553 | LLGo · deadcode drop | 1062421 | +678.0% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1821648 | +1234.0% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1186056 | +768.6% |
| `json-wasi` | 525666 | LLGo · no LTO | 4094700 | +679.0% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2264709 | +330.8% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3874123 | +637.0% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2581666 | +391.1% |
| `llimport` | — | LLGo · no LTO | 11106549 | — |
| `llimport` | — | LLGo · deadcode drop | 9288680 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10433329 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 9317090 | — |
| `path-report` | 194133 | LLGo · no LTO | 2097072 | +980.2% |
| `path-report` | 194133 | LLGo · deadcode drop | 1194237 | +515.2% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 1959289 | +909.3% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1323948 | +582.0% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3136701 | +791.2% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1826219 | +418.9% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2933740 | +733.5% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1970885 | +460.0% |
| `word-count` | 164053 | LLGo · no LTO | 1910569 | +1064.6% |
| `word-count` | 164053 | LLGo · deadcode drop | 1038790 | +533.2% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1776611 | +982.9% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1151451 | +601.9% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.577x | 11 |
| LLGo · deadcode drop | 0.300x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.508x | 11 |
| LLGo · full LTO + GlobalDCE | 0.356x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1102974 | -51.5% |
| `base64` | 2275731 | LLGo · deadcode drop | 530851 | -76.7% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 879599 | -61.3% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 596294 | -73.8% |
| `checksum` | 2264417 | LLGo · no LTO | 1087540 | -52.0% |
| `checksum` | 2264417 | LLGo · deadcode drop | 517455 | -77.1% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 863330 | -61.9% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 576935 | -74.5% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 1722252 | -34.0% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 850494 | -67.4% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1611171 | -38.2% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1003185 | -61.5% |
| `fibonacci` | 2230899 | LLGo · no LTO | 900529 | -59.6% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 432668 | -80.6% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 760391 | -65.9% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 531050 | -76.2% |
| `grep` | 2848917 | LLGo · no LTO | 1548152 | -45.7% |
| `grep` | 2848917 | LLGo · deadcode drop | 869671 | -69.5% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1371712 | -51.9% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 976395 | -65.7% |
| `glob` | 2257634 | LLGo · no LTO | 1119103 | -50.4% |
| `glob` | 2257634 | LLGo · deadcode drop | 522889 | -76.8% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1013706 | -55.1% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 685347 | -69.6% |
| `json-wasi` | 3314587 | LLGo · no LTO | 2769520 | -16.4% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1404022 | -57.6% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2588255 | -21.9% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1716999 | -48.2% |
| `llimport` | 8423078 | LLGo · no LTO | 8101700 | -3.8% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6703899 | -20.4% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 7179152 | -14.8% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6914222 | -17.9% |
| `path-report` | 2381190 | LLGo · no LTO | 1240139 | -47.9% |
| `path-report` | 2381190 | LLGo · deadcode drop | 634112 | -73.4% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1128822 | -52.6% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 800276 | -66.4% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1918705 | -31.0% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1015166 | -63.5% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1793022 | -35.5% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1186513 | -57.3% |
| `word-count` | 2253620 | LLGo · no LTO | 1099693 | -51.2% |
| `word-count` | 2253620 | LLGo · deadcode drop | 516221 | -77.1% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 965719 | -57.1% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 668295 | -70.3% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 9.348x | 10 |
| LLGo · deadcode drop | 4.645x | 10 |
| LLGo · full LTO (GlobalDCE off) | 8.231x | 10 |
| LLGo · full LTO + GlobalDCE | 5.578x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1102974 | +1039.9% |
| `base64` | 96760 | LLGo · deadcode drop | 530851 | +448.6% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 879599 | +809.1% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 596294 | +516.3% |
| `checksum` | 92685 | LLGo · no LTO | 1087540 | +1073.4% |
| `checksum` | 92685 | LLGo · deadcode drop | 517455 | +458.3% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 863330 | +831.5% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 576935 | +522.5% |
| `conv-wasi` | 201149 | LLGo · no LTO | 1722252 | +756.2% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 850494 | +322.8% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1611171 | +701.0% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1003185 | +398.7% |
| `fibonacci` | 62386 | LLGo · no LTO | 900529 | +1343.5% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 432668 | +593.5% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 760391 | +1118.8% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 531050 | +751.2% |
| `grep` | 303772 | LLGo · no LTO | 1548152 | +409.6% |
| `grep` | 303772 | LLGo · deadcode drop | 869671 | +186.3% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1371712 | +351.6% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 976395 | +221.4% |
| `glob` | 93153 | LLGo · no LTO | 1119103 | +1101.4% |
| `glob` | 93153 | LLGo · deadcode drop | 522889 | +461.3% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1013706 | +988.2% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 685347 | +635.7% |
| `json-wasi` | 493590 | LLGo · no LTO | 2769520 | +461.1% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1404022 | +184.5% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2588255 | +424.4% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1716999 | +247.9% |
| `llimport` | — | LLGo · no LTO | 8101700 | — |
| `llimport` | — | LLGo · deadcode drop | 6703899 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 7179152 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6914222 | — |
| `path-report` | 116889 | LLGo · no LTO | 1240139 | +961.0% |
| `path-report` | 116889 | LLGo · deadcode drop | 634112 | +442.5% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1128822 | +865.7% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 800276 | +584.6% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1918705 | +567.5% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1015166 | +253.2% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1793022 | +523.8% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1186513 | +312.8% |
| `word-count` | 86834 | LLGo · no LTO | 1099693 | +1166.4% |
| `word-count` | 86834 | LLGo · deadcode drop | 516221 | +494.5% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 965719 | +1012.1% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 668295 | +669.6% |
