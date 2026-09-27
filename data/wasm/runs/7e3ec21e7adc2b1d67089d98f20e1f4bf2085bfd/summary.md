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
| LLGo · no LTO | 1.066x | 11 |
| LLGo · deadcode drop | 0.648x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.954x | 11 |
| LLGo · full LTO + GlobalDCE | 0.602x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 2070138 | -10.9% |
| `base64` | 2322402 | LLGo · deadcode drop | 1174333 | -49.4% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1846459 | -20.5% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1083325 | -53.4% |
| `checksum` | 2311672 | LLGo · no LTO | 2050030 | -11.3% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1146265 | -50.4% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1810952 | -21.7% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1047667 | -54.7% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 3276416 | +24.2% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1823274 | -30.9% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2937970 | +11.4% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1680286 | -36.3% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1796820 | -21.0% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 1063219 | -53.3% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1581555 | -30.5% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 977219 | -57.0% |
| `grep` | 2871426 | LLGo · no LTO | 2809978 | -2.1% |
| `grep` | 2871426 | LLGo · deadcode drop | 1756596 | -38.8% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2486468 | -13.4% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1630620 | -43.2% |
| `glob` | 2305059 | LLGo · no LTO | 2237091 | -2.9% |
| `glob` | 2305059 | LLGo · deadcode drop | 1300762 | -43.6% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1982465 | -14.0% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1194368 | -48.2% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4590138 | +37.5% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2700026 | -19.1% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 4195292 | +25.7% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2664785 | -20.2% |
| `llimport` | 8440671 | LLGo · no LTO | 12811091 | +51.8% |
| `llimport` | 8440671 | LLGo · deadcode drop | 10989109 | +30.2% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 11810198 | +39.9% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 10297875 | +22.0% |
| `path-report` | 2428068 | LLGo · no LTO | 2585762 | +6.5% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1639163 | -32.5% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 2317783 | -4.5% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1521147 | -37.4% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3645871 | +29.7% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 2156202 | -23.3% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 3312257 | +17.8% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 2030684 | -27.8% |
| `word-count` | 2300998 | LLGo · no LTO | 2196446 | -4.5% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1272993 | -44.7% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1940305 | -15.7% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1160400 | -49.6% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 13.302x | 10 |
| LLGo · deadcode drop | 7.808x | 10 |
| LLGo · full LTO (GlobalDCE off) | 11.872x | 10 |
| LLGo · full LTO + GlobalDCE | 7.253x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 2070138 | +1101.5% |
| `base64` | 172302 | LLGo · deadcode drop | 1174333 | +581.6% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1846459 | +971.6% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1083325 | +528.7% |
| `checksum` | 169609 | LLGo · no LTO | 2050030 | +1108.7% |
| `checksum` | 169609 | LLGo · deadcode drop | 1146265 | +575.8% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1810952 | +967.7% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1047667 | +517.7% |
| `conv-wasi` | 165385 | LLGo · no LTO | 3276416 | +1881.1% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1823274 | +1002.4% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2937970 | +1676.4% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1680286 | +916.0% |
| `fibonacci` | 141855 | LLGo · no LTO | 1796820 | +1166.7% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 1063219 | +649.5% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1581555 | +1014.9% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 977219 | +588.9% |
| `grep` | 155984 | LLGo · no LTO | 2809978 | +1701.5% |
| `grep` | 155984 | LLGo · deadcode drop | 1756596 | +1026.1% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2486468 | +1494.1% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1630620 | +945.4% |
| `glob` | 136553 | LLGo · no LTO | 2237091 | +1538.3% |
| `glob` | 136553 | LLGo · deadcode drop | 1300762 | +852.6% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1982465 | +1351.8% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1194368 | +774.7% |
| `json-wasi` | 525666 | LLGo · no LTO | 4590138 | +773.2% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2700026 | +413.6% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 4195292 | +698.1% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2664785 | +406.9% |
| `llimport` | — | LLGo · no LTO | 12811091 | — |
| `llimport` | — | LLGo · deadcode drop | 10989109 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 11810198 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 10297875 | — |
| `path-report` | 194133 | LLGo · no LTO | 2585762 | +1232.0% |
| `path-report` | 194133 | LLGo · deadcode drop | 1639163 | +744.4% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 2317783 | +1093.9% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1521147 | +683.6% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3645871 | +935.8% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 2156202 | +512.6% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 3312257 | +841.1% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 2030684 | +476.9% |
| `word-count` | 164053 | LLGo · no LTO | 2196446 | +1238.9% |
| `word-count` | 164053 | LLGo · deadcode drop | 1272993 | +676.0% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1940305 | +1082.7% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1160400 | +607.3% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.911x | 11 |
| LLGo · deadcode drop | 0.586x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.731x | 11 |
| LLGo · full LTO + GlobalDCE | 0.523x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1668195 | -26.7% |
| `base64` | 2275731 | LLGo · deadcode drop | 1007819 | -55.7% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 1303294 | -42.7% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 909454 | -60.0% |
| `checksum` | 2264417 | LLGo · no LTO | 1645084 | -27.4% |
| `checksum` | 2264417 | LLGo · deadcode drop | 980107 | -56.7% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 1273517 | -43.8% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 876852 | -61.3% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 2796603 | +7.2% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 1629708 | -37.5% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 2347894 | -10.0% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1469554 | -43.7% |
| `fibonacci` | 2230899 | LLGo · no LTO | 1378877 | -38.2% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 905119 | -59.4% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 1108614 | -50.3% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 816311 | -63.4% |
| `grep` | 2848917 | LLGo · no LTO | 2370191 | -16.8% |
| `grep` | 2848917 | LLGo · deadcode drop | 1578505 | -44.6% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1922357 | -32.5% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 1413728 | -50.4% |
| `glob` | 2257634 | LLGo · no LTO | 1836186 | -18.7% |
| `glob` | 2257634 | LLGo · deadcode drop | 1138658 | -49.6% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1465490 | -35.1% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 1028742 | -54.4% |
| `json-wasi` | 3314587 | LLGo · no LTO | 4104106 | +23.8% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 2486437 | -25.0% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 3466649 | +4.6% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 2364574 | -28.7% |
| `llimport` | 8423078 | LLGo · no LTO | 12431400 | +47.6% |
| `llimport` | 8423078 | LLGo · deadcode drop | 10958158 | +30.1% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 8968186 | +6.5% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 8265057 | -1.9% |
| `path-report` | 2381190 | LLGo · no LTO | 2176436 | -8.6% |
| `path-report` | 2381190 | LLGo · deadcode drop | 1469891 | -38.3% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1791811 | -24.8% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 1346060 | -43.5% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 3131985 | +12.6% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1934530 | -30.4% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 2658258 | -4.4% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1764916 | -36.5% |
| `word-count` | 2253620 | LLGo · no LTO | 1796555 | -20.3% |
| `word-count` | 2253620 | LLGo · deadcode drop | 1112054 | -50.7% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 1409803 | -37.4% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 996122 | -55.8% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 14.802x | 10 |
| LLGo · deadcode drop | 9.230x | 10 |
| LLGo · full LTO (GlobalDCE off) | 11.997x | 10 |
| LLGo · full LTO + GlobalDCE | 8.375x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1668195 | +1624.1% |
| `base64` | 96760 | LLGo · deadcode drop | 1007819 | +941.6% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 1303294 | +1246.9% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 909454 | +839.9% |
| `checksum` | 92685 | LLGo · no LTO | 1645084 | +1674.9% |
| `checksum` | 92685 | LLGo · deadcode drop | 980107 | +957.5% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 1273517 | +1274.0% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 876852 | +846.1% |
| `conv-wasi` | 201149 | LLGo · no LTO | 2796603 | +1290.3% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 1629708 | +710.2% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 2347894 | +1067.2% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1469554 | +630.6% |
| `fibonacci` | 62386 | LLGo · no LTO | 1378877 | +2110.2% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 905119 | +1350.8% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 1108614 | +1677.0% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 816311 | +1208.5% |
| `grep` | 303772 | LLGo · no LTO | 2370191 | +680.3% |
| `grep` | 303772 | LLGo · deadcode drop | 1578505 | +419.6% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1922357 | +532.8% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 1413728 | +365.4% |
| `glob` | 93153 | LLGo · no LTO | 1836186 | +1871.2% |
| `glob` | 93153 | LLGo · deadcode drop | 1138658 | +1122.4% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1465490 | +1473.2% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 1028742 | +1004.4% |
| `json-wasi` | 493590 | LLGo · no LTO | 4104106 | +731.5% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 2486437 | +403.7% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 3466649 | +602.3% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 2364574 | +379.1% |
| `llimport` | — | LLGo · no LTO | 12431400 | — |
| `llimport` | — | LLGo · deadcode drop | 10958158 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 8968186 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 8265057 | — |
| `path-report` | 116889 | LLGo · no LTO | 2176436 | +1762.0% |
| `path-report` | 116889 | LLGo · deadcode drop | 1469891 | +1157.5% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1791811 | +1432.9% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 1346060 | +1051.6% |
| `sha-wasi` | 287449 | LLGo · no LTO | 3131985 | +989.6% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1934530 | +573.0% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 2658258 | +824.8% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1764916 | +514.0% |
| `word-count` | 86834 | LLGo · no LTO | 1796555 | +1969.0% |
| `word-count` | 86834 | LLGo · deadcode drop | 1112054 | +1180.7% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 1409803 | +1523.6% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 996122 | +1047.2% |
