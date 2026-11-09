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
| LLGo · no LTO | 0.926x | 11 |
| LLGo · deadcode drop | 0.527x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.832x | 11 |
| LLGo · full LTO + GlobalDCE | 0.566x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1886672 | -18.8% |
| `base64` | 2322402 | LLGo · deadcode drop | 1017402 | -56.2% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1651810 | -28.9% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1061738 | -54.3% |
| `checksum` | 2311672 | LLGo · no LTO | 1867047 | -19.2% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1003120 | -56.6% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1615974 | -30.1% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1028923 | -55.5% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2730877 | +3.5% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1466151 | -44.4% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2492696 | -5.5% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1579215 | -40.1% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1668241 | -26.7% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 896397 | -60.6% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1435140 | -36.9% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 974317 | -57.2% |
| `grep` | 2871426 | LLGo · no LTO | 2540657 | -11.5% |
| `grep` | 2871426 | LLGo · deadcode drop | 1512271 | -47.3% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2220992 | -22.7% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1557247 | -45.8% |
| `glob` | 2305059 | LLGo · no LTO | 1917665 | -16.8% |
| `glob` | 2305059 | LLGo · deadcode drop | 1023938 | -55.6% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1754316 | -23.9% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1150530 | -50.1% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4027064 | +20.6% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2186300 | -34.5% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3741573 | +12.1% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2503154 | -25.0% |
| `llimport` | 8440671 | LLGo · no LTO | 10912187 | +29.3% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9027848 | +7.0% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 9937210 | +17.7% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 8870279 | +5.1% |
| `path-report` | 2428068 | LLGo · no LTO | 2056399 | -15.3% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1147519 | -52.7% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 1882993 | -22.4% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1279581 | -47.3% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3047542 | +8.4% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1739260 | -38.1% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2809463 | -0.1% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1889220 | -32.8% |
| `word-count` | 2300998 | LLGo · no LTO | 1877186 | -18.4% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1000341 | -56.5% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1713487 | -25.5% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1118876 | -51.4% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.572x | 10 |
| LLGo · deadcode drop | 6.343x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.390x | 10 |
| LLGo · full LTO + GlobalDCE | 6.878x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1886672 | +995.0% |
| `base64` | 172302 | LLGo · deadcode drop | 1017402 | +490.5% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1651810 | +858.7% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1061738 | +516.2% |
| `checksum` | 169609 | LLGo · no LTO | 1867047 | +1000.8% |
| `checksum` | 169609 | LLGo · deadcode drop | 1003120 | +491.4% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1615974 | +852.8% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1028923 | +506.6% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2730877 | +1551.2% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1466151 | +786.5% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2492696 | +1407.2% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1579215 | +854.9% |
| `fibonacci` | 141855 | LLGo · no LTO | 1668241 | +1076.0% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 896397 | +531.9% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1435140 | +911.7% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 974317 | +586.8% |
| `grep` | 155984 | LLGo · no LTO | 2540657 | +1528.8% |
| `grep` | 155984 | LLGo · deadcode drop | 1512271 | +869.5% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2220992 | +1323.9% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1557247 | +898.3% |
| `glob` | 136553 | LLGo · no LTO | 1917665 | +1304.3% |
| `glob` | 136553 | LLGo · deadcode drop | 1023938 | +649.8% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1754316 | +1184.7% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1150530 | +742.6% |
| `json-wasi` | 525666 | LLGo · no LTO | 4027064 | +666.1% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2186300 | +315.9% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3741573 | +611.8% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2503154 | +376.2% |
| `llimport` | — | LLGo · no LTO | 10912187 | — |
| `llimport` | — | LLGo · deadcode drop | 9027848 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 9937210 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 8870279 | — |
| `path-report` | 194133 | LLGo · no LTO | 2056399 | +959.3% |
| `path-report` | 194133 | LLGo · deadcode drop | 1147519 | +491.1% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 1882993 | +869.9% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1279581 | +559.1% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3047542 | +765.9% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1739260 | +394.1% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2809463 | +698.2% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1889220 | +436.8% |
| `word-count` | 164053 | LLGo · no LTO | 1877186 | +1044.3% |
| `word-count` | 164053 | LLGo · deadcode drop | 1000341 | +509.8% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1713487 | +944.5% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1118876 | +582.0% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.562x | 11 |
| LLGo · deadcode drop | 0.284x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.483x | 11 |
| LLGo · full LTO + GlobalDCE | 0.339x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1077838 | -52.6% |
| `base64` | 2275731 | LLGo · deadcode drop | 500383 | -78.0% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 834832 | -63.3% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 566892 | -75.1% |
| `checksum` | 2264417 | LLGo · no LTO | 1062248 | -53.1% |
| `checksum` | 2264417 | LLGo · deadcode drop | 487448 | -78.5% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 819620 | -63.8% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 548749 | -75.8% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 1662417 | -36.3% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 799773 | -69.3% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1527869 | -41.4% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 956047 | -63.3% |
| `fibonacci` | 2230899 | LLGo · no LTO | 875926 | -60.7% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 405346 | -81.8% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 722417 | -67.6% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 506363 | -77.3% |
| `grep` | 2848917 | LLGo · no LTO | 1512479 | -46.9% |
| `grep` | 2848917 | LLGo · deadcode drop | 827376 | -71.0% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1312665 | -53.9% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 939417 | -67.0% |
| `glob` | 2257634 | LLGo · no LTO | 1093943 | -51.5% |
| `glob` | 2257634 | LLGo · deadcode drop | 494604 | -78.1% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 965688 | -57.2% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 655814 | -71.0% |
| `json-wasi` | 3314587 | LLGo · no LTO | 2671319 | -19.4% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1316081 | -60.3% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2444025 | -26.3% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1622502 | -51.0% |
| `llimport` | 8423078 | LLGo · no LTO | 7948743 | -5.6% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6495863 | -22.9% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 6767355 | -19.7% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6536095 | -22.4% |
| `path-report` | 2381190 | LLGo · no LTO | 1207480 | -49.3% |
| `path-report` | 2381190 | LLGo · deadcode drop | 596903 | -74.9% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1071664 | -55.0% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 761657 | -68.0% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1852397 | -33.4% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 959340 | -65.5% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1698549 | -38.9% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1127977 | -59.4% |
| `word-count` | 2253620 | LLGo · no LTO | 1074739 | -52.3% |
| `word-count` | 2253620 | LLGo · deadcode drop | 487472 | -78.4% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 922456 | -59.1% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 641208 | -71.5% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 9.093x | 10 |
| LLGo · deadcode drop | 4.379x | 10 |
| LLGo · full LTO (GlobalDCE off) | 7.821x | 10 |
| LLGo · full LTO + GlobalDCE | 5.318x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1077838 | +1013.9% |
| `base64` | 96760 | LLGo · deadcode drop | 500383 | +417.1% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 834832 | +762.8% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 566892 | +485.9% |
| `checksum` | 92685 | LLGo · no LTO | 1062248 | +1046.1% |
| `checksum` | 92685 | LLGo · deadcode drop | 487448 | +425.9% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 819620 | +784.3% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 548749 | +492.1% |
| `conv-wasi` | 201149 | LLGo · no LTO | 1662417 | +726.5% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 799773 | +297.6% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1527869 | +659.6% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 956047 | +375.3% |
| `fibonacci` | 62386 | LLGo · no LTO | 875926 | +1304.0% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 405346 | +549.7% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 722417 | +1058.0% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 506363 | +711.7% |
| `grep` | 303772 | LLGo · no LTO | 1512479 | +397.9% |
| `grep` | 303772 | LLGo · deadcode drop | 827376 | +172.4% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1312665 | +332.1% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 939417 | +209.3% |
| `glob` | 93153 | LLGo · no LTO | 1093943 | +1074.4% |
| `glob` | 93153 | LLGo · deadcode drop | 494604 | +431.0% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 965688 | +936.7% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 655814 | +604.0% |
| `json-wasi` | 493590 | LLGo · no LTO | 2671319 | +441.2% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1316081 | +166.6% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2444025 | +395.2% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1622502 | +228.7% |
| `llimport` | — | LLGo · no LTO | 7948743 | — |
| `llimport` | — | LLGo · deadcode drop | 6495863 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 6767355 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6536095 | — |
| `path-report` | 116889 | LLGo · no LTO | 1207480 | +933.0% |
| `path-report` | 116889 | LLGo · deadcode drop | 596903 | +410.7% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1071664 | +816.8% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 761657 | +551.6% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1852397 | +544.4% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 959340 | +233.7% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1698549 | +490.9% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1127977 | +292.4% |
| `word-count` | 86834 | LLGo · no LTO | 1074739 | +1137.7% |
| `word-count` | 86834 | LLGo · deadcode drop | 487472 | +461.4% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 922456 | +962.3% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 641208 | +638.4% |
