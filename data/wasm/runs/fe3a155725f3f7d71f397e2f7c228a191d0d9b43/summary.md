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
| LLGo · no LTO | 1.069x | 11 |
| LLGo · deadcode drop | 0.650x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.957x | 11 |
| LLGo · full LTO + GlobalDCE | 0.604x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 2076666 | -10.6% |
| `base64` | 2322402 | LLGo · deadcode drop | 1180647 | -49.2% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1852055 | -20.3% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1088572 | -53.1% |
| `checksum` | 2311672 | LLGo · no LTO | 2056546 | -11.0% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1152556 | -50.1% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1816608 | -21.4% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1052976 | -54.4% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 3283043 | +24.4% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1829673 | -30.7% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2943692 | +11.6% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1685643 | -36.1% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1803348 | -20.7% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 1069516 | -53.0% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1587194 | -30.2% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 982509 | -56.8% |
| `grep` | 2871426 | LLGo · no LTO | 2816492 | -1.9% |
| `grep` | 2871426 | LLGo · deadcode drop | 1762875 | -38.6% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2492111 | -13.2% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1635881 | -43.0% |
| `glob` | 2305059 | LLGo · no LTO | 2243625 | -2.7% |
| `glob` | 2305059 | LLGo · deadcode drop | 1307061 | -43.3% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1988093 | -13.8% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1199660 | -48.0% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4596719 | +37.7% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2706422 | -18.9% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 4200995 | +25.8% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2670097 | -20.0% |
| `llimport` | 8440671 | LLGo · no LTO | 12825617 | +52.0% |
| `llimport` | 8440671 | LLGo · deadcode drop | 11004268 | +30.4% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 11822877 | +40.1% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 10310460 | +22.2% |
| `path-report` | 2428068 | LLGo · no LTO | 2592299 | +6.8% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1645438 | -32.2% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 2323425 | -4.3% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1526409 | -37.1% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3652516 | +29.9% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 2162618 | -23.1% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 3317960 | +18.0% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 2036035 | -27.6% |
| `word-count` | 2300998 | LLGo · no LTO | 2202953 | -4.3% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1279286 | -44.4% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1945956 | -15.4% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1165697 | -49.3% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 13.337x | 10 |
| LLGo · deadcode drop | 7.841x | 10 |
| LLGo · full LTO (GlobalDCE off) | 11.902x | 10 |
| LLGo · full LTO + GlobalDCE | 7.281x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 2076666 | +1105.2% |
| `base64` | 172302 | LLGo · deadcode drop | 1180647 | +585.2% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1852055 | +974.9% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1088572 | +531.8% |
| `checksum` | 169609 | LLGo · no LTO | 2056546 | +1112.5% |
| `checksum` | 169609 | LLGo · deadcode drop | 1152556 | +579.5% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1816608 | +971.1% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1052976 | +520.8% |
| `conv-wasi` | 165385 | LLGo · no LTO | 3283043 | +1885.1% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1829673 | +1006.3% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2943692 | +1679.9% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1685643 | +919.2% |
| `fibonacci` | 141855 | LLGo · no LTO | 1803348 | +1171.3% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 1069516 | +654.0% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1587194 | +1018.9% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 982509 | +592.6% |
| `grep` | 155984 | LLGo · no LTO | 2816492 | +1705.6% |
| `grep` | 155984 | LLGo · deadcode drop | 1762875 | +1030.2% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2492111 | +1497.7% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1635881 | +948.7% |
| `glob` | 136553 | LLGo · no LTO | 2243625 | +1543.0% |
| `glob` | 136553 | LLGo · deadcode drop | 1307061 | +857.2% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1988093 | +1355.9% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1199660 | +778.5% |
| `json-wasi` | 525666 | LLGo · no LTO | 4596719 | +774.5% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2706422 | +414.9% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 4200995 | +699.2% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2670097 | +407.9% |
| `llimport` | — | LLGo · no LTO | 12825617 | — |
| `llimport` | — | LLGo · deadcode drop | 11004268 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 11822877 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 10310460 | — |
| `path-report` | 194133 | LLGo · no LTO | 2592299 | +1235.3% |
| `path-report` | 194133 | LLGo · deadcode drop | 1645438 | +747.6% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 2323425 | +1096.8% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1526409 | +686.3% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3652516 | +937.7% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 2162618 | +514.4% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 3317960 | +842.7% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 2036035 | +478.5% |
| `word-count` | 164053 | LLGo · no LTO | 2202953 | +1242.8% |
| `word-count` | 164053 | LLGo · deadcode drop | 1279286 | +679.8% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1945956 | +1086.2% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1165697 | +610.6% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.914x | 11 |
| LLGo · deadcode drop | 0.589x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.733x | 11 |
| LLGo · full LTO + GlobalDCE | 0.525x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1674703 | -26.4% |
| `base64` | 2275731 | LLGo · deadcode drop | 1013878 | -55.4% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 1309025 | -42.5% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 914768 | -59.8% |
| `checksum` | 2264417 | LLGo · no LTO | 1651589 | -27.1% |
| `checksum` | 2264417 | LLGo · deadcode drop | 986144 | -56.5% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 1279244 | -43.5% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 882168 | -61.0% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 2803310 | +7.5% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 1635856 | -37.3% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 2354017 | -9.7% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1474965 | -43.4% |
| `fibonacci` | 2230899 | LLGo · no LTO | 1385206 | -37.9% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 911145 | -59.2% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 1114276 | -50.1% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 821596 | -63.2% |
| `grep` | 2848917 | LLGo · no LTO | 2376774 | -16.6% |
| `grep` | 2848917 | LLGo · deadcode drop | 1584607 | -44.4% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1928290 | -32.3% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 1419110 | -50.2% |
| `glob` | 2257634 | LLGo · no LTO | 1842684 | -18.4% |
| `glob` | 2257634 | LLGo · deadcode drop | 1144700 | -49.3% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1471267 | -34.8% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 1034046 | -54.2% |
| `json-wasi` | 3314587 | LLGo · no LTO | 4111381 | +24.0% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 2492772 | -24.8% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 3473351 | +4.8% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 2370150 | -28.5% |
| `llimport` | 8423078 | LLGo · no LTO | 12449754 | +47.8% |
| `llimport` | 8423078 | LLGo · deadcode drop | 10975688 | +30.3% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 8983707 | +6.7% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 8281862 | -1.7% |
| `path-report` | 2381190 | LLGo · no LTO | 2182978 | -8.3% |
| `path-report` | 2381190 | LLGo · deadcode drop | 1475950 | -38.0% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1797629 | -24.5% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 1351400 | -43.2% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 3138740 | +12.9% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1940711 | -30.2% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 2664405 | -4.2% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1770369 | -36.3% |
| `word-count` | 2253620 | LLGo · no LTO | 1803075 | -20.0% |
| `word-count` | 2253620 | LLGo · deadcode drop | 1118133 | -50.4% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 1415542 | -37.2% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 1001445 | -55.6% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 14.848x | 10 |
| LLGo · deadcode drop | 9.274x | 10 |
| LLGo · full LTO (GlobalDCE off) | 12.040x | 10 |
| LLGo · full LTO + GlobalDCE | 8.413x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1674703 | +1630.8% |
| `base64` | 96760 | LLGo · deadcode drop | 1013878 | +947.8% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 1309025 | +1252.9% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 914768 | +845.4% |
| `checksum` | 92685 | LLGo · no LTO | 1651589 | +1681.9% |
| `checksum` | 92685 | LLGo · deadcode drop | 986144 | +964.0% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 1279244 | +1280.2% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 882168 | +851.8% |
| `conv-wasi` | 201149 | LLGo · no LTO | 2803310 | +1293.6% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 1635856 | +713.3% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 2354017 | +1070.3% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1474965 | +633.3% |
| `fibonacci` | 62386 | LLGo · no LTO | 1385206 | +2120.4% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 911145 | +1360.5% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 1114276 | +1686.1% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 821596 | +1217.0% |
| `grep` | 303772 | LLGo · no LTO | 2376774 | +682.4% |
| `grep` | 303772 | LLGo · deadcode drop | 1584607 | +421.6% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1928290 | +534.8% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 1419110 | +367.2% |
| `glob` | 93153 | LLGo · no LTO | 1842684 | +1878.1% |
| `glob` | 93153 | LLGo · deadcode drop | 1144700 | +1128.8% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1471267 | +1479.4% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 1034046 | +1010.1% |
| `json-wasi` | 493590 | LLGo · no LTO | 4111381 | +733.0% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 2492772 | +405.0% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 3473351 | +603.7% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 2370150 | +380.2% |
| `llimport` | — | LLGo · no LTO | 12449754 | — |
| `llimport` | — | LLGo · deadcode drop | 10975688 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 8983707 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 8281862 | — |
| `path-report` | 116889 | LLGo · no LTO | 2182978 | +1767.6% |
| `path-report` | 116889 | LLGo · deadcode drop | 1475950 | +1162.7% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1797629 | +1437.9% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 1351400 | +1056.1% |
| `sha-wasi` | 287449 | LLGo · no LTO | 3138740 | +991.9% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1940711 | +575.1% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 2664405 | +826.9% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1770369 | +515.9% |
| `word-count` | 86834 | LLGo · no LTO | 1803075 | +1976.5% |
| `word-count` | 86834 | LLGo · deadcode drop | 1118133 | +1187.7% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 1415542 | +1530.2% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 1001445 | +1053.3% |
