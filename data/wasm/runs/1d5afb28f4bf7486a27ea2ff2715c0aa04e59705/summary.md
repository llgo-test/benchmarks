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
| LLGo · no LTO | 0.946x | 11 |
| LLGo · deadcode drop | 0.548x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.867x | 11 |
| LLGo · full LTO + GlobalDCE | 0.587x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1926396 | -17.1% |
| `base64` | 2322402 | LLGo · deadcode drop | 1060332 | -54.3% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1720368 | -25.9% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1099734 | -52.6% |
| `checksum` | 2311672 | LLGo · no LTO | 1906937 | -17.5% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1045741 | -54.8% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1684027 | -27.2% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1065904 | -53.9% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2791395 | +5.8% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1524918 | -42.2% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2586867 | -2.0% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1628382 | -38.3% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1704456 | -25.1% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 935769 | -58.9% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1493365 | -34.3% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 1007502 | -55.7% |
| `grep` | 2871426 | LLGo · no LTO | 2590169 | -9.8% |
| `grep` | 2871426 | LLGo · deadcode drop | 1567405 | -45.4% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2311901 | -19.5% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1612643 | -43.8% |
| `glob` | 2305059 | LLGo · no LTO | 1957422 | -15.1% |
| `glob` | 2305059 | LLGo · deadcode drop | 1064888 | -53.8% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1825945 | -20.8% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1189192 | -48.4% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4103343 | +22.9% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2269149 | -32.0% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3878549 | +16.2% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2584567 | -22.6% |
| `llimport` | 8440671 | LLGo · no LTO | 11107491 | +31.6% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9284539 | +10.0% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10430515 | +23.6% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 9312888 | +10.3% |
| `path-report` | 2428068 | LLGo · no LTO | 2103133 | -13.4% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1196666 | -50.7% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 1963567 | -19.1% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1327077 | -45.3% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3145537 | +11.9% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1830548 | -34.9% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2939602 | +4.6% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1975194 | -29.7% |
| `word-count` | 2300998 | LLGo · no LTO | 1916585 | -16.7% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1041241 | -54.7% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1780913 | -22.6% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1154586 | -49.8% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.828x | 10 |
| LLGo · deadcode drop | 6.608x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.815x | 10 |
| LLGo · full LTO + GlobalDCE | 7.121x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1926396 | +1018.0% |
| `base64` | 172302 | LLGo · deadcode drop | 1060332 | +515.4% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1720368 | +898.5% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1099734 | +538.3% |
| `checksum` | 169609 | LLGo · no LTO | 1906937 | +1024.3% |
| `checksum` | 169609 | LLGo · deadcode drop | 1045741 | +516.6% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1684027 | +892.9% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1065904 | +528.4% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2791395 | +1587.8% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1524918 | +822.0% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2586867 | +1464.1% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1628382 | +884.6% |
| `fibonacci` | 141855 | LLGo · no LTO | 1704456 | +1101.5% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 935769 | +559.7% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1493365 | +952.7% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 1007502 | +610.2% |
| `grep` | 155984 | LLGo · no LTO | 2590169 | +1560.5% |
| `grep` | 155984 | LLGo · deadcode drop | 1567405 | +904.8% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2311901 | +1382.1% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1612643 | +933.9% |
| `glob` | 136553 | LLGo · no LTO | 1957422 | +1333.5% |
| `glob` | 136553 | LLGo · deadcode drop | 1064888 | +679.8% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1825945 | +1237.2% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1189192 | +770.9% |
| `json-wasi` | 525666 | LLGo · no LTO | 4103343 | +680.6% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2269149 | +331.7% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3878549 | +637.8% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2584567 | +391.7% |
| `llimport` | — | LLGo · no LTO | 11107491 | — |
| `llimport` | — | LLGo · deadcode drop | 9284539 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10430515 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 9312888 | — |
| `path-report` | 194133 | LLGo · no LTO | 2103133 | +983.3% |
| `path-report` | 194133 | LLGo · deadcode drop | 1196666 | +516.4% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 1963567 | +911.5% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1327077 | +583.6% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3145537 | +793.7% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1830548 | +420.1% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2939602 | +735.2% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1975194 | +461.2% |
| `word-count` | 164053 | LLGo · no LTO | 1916585 | +1068.3% |
| `word-count` | 164053 | LLGo · deadcode drop | 1041241 | +534.7% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1780913 | +985.6% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1154586 | +603.8% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.579x | 11 |
| LLGo · deadcode drop | 0.300x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.510x | 11 |
| LLGo · full LTO + GlobalDCE | 0.356x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1107559 | -51.3% |
| `base64` | 2275731 | LLGo · deadcode drop | 531096 | -76.7% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 883263 | -61.2% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 597948 | -73.7% |
| `checksum` | 2264417 | LLGo · no LTO | 1092117 | -51.8% |
| `checksum` | 2264417 | LLGo · deadcode drop | 517700 | -77.1% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 866972 | -61.7% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 578589 | -74.4% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 1728129 | -33.7% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 851232 | -67.4% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1615474 | -38.1% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1005051 | -61.5% |
| `fibonacci` | 2230899 | LLGo · no LTO | 905090 | -59.4% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 432913 | -80.6% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 764041 | -65.8% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 532704 | -76.1% |
| `grep` | 2848917 | LLGo · no LTO | 1552729 | -45.5% |
| `grep` | 2848917 | LLGo · deadcode drop | 869900 | -69.5% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1375354 | -51.7% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 978033 | -65.7% |
| `glob` | 2257634 | LLGo · no LTO | 1123664 | -50.2% |
| `glob` | 2257634 | LLGo · deadcode drop | 523118 | -76.8% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1017356 | -54.9% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 687001 | -69.6% |
| `json-wasi` | 3314587 | LLGo · no LTO | 2775443 | -16.3% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1404930 | -57.6% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2591491 | -21.8% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1718143 | -48.2% |
| `llimport` | 8423078 | LLGo · no LTO | 8076033 | -4.1% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6670904 | -20.8% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 7151909 | -15.1% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6884217 | -18.3% |
| `path-report` | 2381190 | LLGo · no LTO | 1244716 | -47.7% |
| `path-report` | 2381190 | LLGo · deadcode drop | 634357 | -73.4% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1132464 | -52.4% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 801930 | -66.3% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1924594 | -30.8% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1015907 | -63.5% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1797343 | -35.4% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1188391 | -57.3% |
| `word-count` | 2253620 | LLGo · no LTO | 1104270 | -51.0% |
| `word-count` | 2253620 | LLGo · deadcode drop | 516450 | -77.1% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 969369 | -57.0% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 669949 | -70.3% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 9.382x | 10 |
| LLGo · deadcode drop | 4.647x | 10 |
| LLGo · full LTO (GlobalDCE off) | 8.258x | 10 |
| LLGo · full LTO + GlobalDCE | 5.590x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1107559 | +1044.6% |
| `base64` | 96760 | LLGo · deadcode drop | 531096 | +448.9% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 883263 | +812.8% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 597948 | +518.0% |
| `checksum` | 92685 | LLGo · no LTO | 1092117 | +1078.3% |
| `checksum` | 92685 | LLGo · deadcode drop | 517700 | +458.6% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 866972 | +835.4% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 578589 | +524.3% |
| `conv-wasi` | 201149 | LLGo · no LTO | 1728129 | +759.1% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 851232 | +323.2% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1615474 | +703.1% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1005051 | +399.7% |
| `fibonacci` | 62386 | LLGo · no LTO | 905090 | +1350.8% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 432913 | +593.9% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 764041 | +1124.7% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 532704 | +753.9% |
| `grep` | 303772 | LLGo · no LTO | 1552729 | +411.1% |
| `grep` | 303772 | LLGo · deadcode drop | 869900 | +186.4% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1375354 | +352.8% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 978033 | +222.0% |
| `glob` | 93153 | LLGo · no LTO | 1123664 | +1106.3% |
| `glob` | 93153 | LLGo · deadcode drop | 523118 | +461.6% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1017356 | +992.1% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 687001 | +637.5% |
| `json-wasi` | 493590 | LLGo · no LTO | 2775443 | +462.3% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1404930 | +184.6% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2591491 | +425.0% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1718143 | +248.1% |
| `llimport` | — | LLGo · no LTO | 8076033 | — |
| `llimport` | — | LLGo · deadcode drop | 6670904 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 7151909 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6884217 | — |
| `path-report` | 116889 | LLGo · no LTO | 1244716 | +964.9% |
| `path-report` | 116889 | LLGo · deadcode drop | 634357 | +442.7% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1132464 | +868.8% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 801930 | +586.1% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1924594 | +569.5% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1015907 | +253.4% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1797343 | +525.3% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1188391 | +313.4% |
| `word-count` | 86834 | LLGo · no LTO | 1104270 | +1171.7% |
| `word-count` | 86834 | LLGo · deadcode drop | 516450 | +494.8% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 969369 | +1016.3% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 669949 | +671.5% |
