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
| tsgo | TinyGo | optional | failed | [logs/tsgo.TinyGo.log](logs/tsgo.TinyGo.log) |

| Application | Target | Go toolchain | Source repository | Commit | Entry |
| --- | --- | --- | --- | --- | --- |
| base64 | wasip1/wasm | 1.26.2 | - | - | base64 |
| base64-js | js/wasm | 1.26.2 | - | - | base64 |
| checksum | wasip1/wasm | 1.26.2 | - | - | checksum |
| checksum-js | js/wasm | 1.26.2 | - | - | checksum |
| convolution | wasip1/wasm | 1.26.2 | https://github.com/universonic/go-rust-wasm-bench.git | 6d1b98c971d6206c313a6d1233d9f2687c50febe | go/cmd/conv-wasi |
| convolution-js | js/wasm | 1.26.2 | https://github.com/universonic/go-rust-wasm-bench.git | 6d1b98c971d6206c313a6d1233d9f2687c50febe | go/cmd/conv-wasi |
| fibonacci | wasip1/wasm | 1.26.2 | https://github.com/mattn/wasi-benchmark.git | c7d73b7b1e03b352791f91ed207c6b9c79559453 | main.go |
| fibonacci-js | js/wasm | 1.26.2 | https://github.com/mattn/wasi-benchmark.git | c7d73b7b1e03b352791f91ed207c6b9c79559453 | main.go |
| glob | wasip1/wasm | 1.26.2 | - | - | glob |
| glob-js | js/wasm | 1.26.2 | - | - | glob |
| grep | wasip1/wasm | 1.26.2 | - | - | grep |
| grep-js | js/wasm | 1.26.2 | - | - | grep |
| json-roundtrip | wasip1/wasm | 1.26.2 | https://github.com/universonic/go-rust-wasm-bench.git | 6d1b98c971d6206c313a6d1233d9f2687c50febe | go/cmd/json-wasi |
| json-roundtrip-js | js/wasm | 1.26.2 | https://github.com/universonic/go-rust-wasm-bench.git | 6d1b98c971d6206c313a6d1233d9f2687c50febe | go/cmd/json-wasi |
| llimport | wasip1/wasm | 1.27.0 | https://github.com/goplus/llcppg.git | d62a300b00d567ce2737ab085cef18c06d43f7d7 | cmd/llimport |
| llimport-js | js/wasm | 1.27.0 | https://github.com/goplus/llcppg.git | d62a300b00d567ce2737ab085cef18c06d43f7d7 | cmd/llimport |
| path-report | wasip1/wasm | 1.26.2 | - | - | path-report |
| path-report-js | js/wasm | 1.26.2 | - | - | path-report |
| sha256 | wasip1/wasm | 1.26.2 | https://github.com/universonic/go-rust-wasm-bench.git | 6d1b98c971d6206c313a6d1233d9f2687c50febe | go/cmd/sha-wasi |
| sha256-js | js/wasm | 1.26.2 | https://github.com/universonic/go-rust-wasm-bench.git | 6d1b98c971d6206c313a6d1233d9f2687c50febe | go/cmd/sha-wasi |
| tsgo | js/wasm | 1.27.0 | https://github.com/microsoft/TypeScript.git | c975de5011fb7dfb32a491cf3fcf02d4f811f50e | tsc/cmd/tsc |
| word-count | wasip1/wasm | 1.26.2 | - | - | word-count |
| word-count-js | js/wasm | 1.26.2 | - | - | word-count |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.802x | 11 |
| LLGo · deadcode drop | 0.516x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.698x | 11 |
| LLGo · full LTO + GlobalDCE | 0.462x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1528896 | -32.8% |
| `base64` | 2275731 | LLGo · deadcode drop | 927106 | -59.3% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 1309682 | -42.5% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 813920 | -64.2% |
| `checksum` | 2264417 | LLGo · no LTO | 1515603 | -33.1% |
| `checksum` | 2264417 | LLGo · deadcode drop | 908697 | -59.9% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 1291281 | -43.0% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 794500 | -64.9% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 2419012 | -7.2% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 1430948 | -45.1% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 2116759 | -18.8% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1276274 | -51.1% |
| `fibonacci` | 2230899 | LLGo · no LTO | 1344703 | -39.7% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 849188 | -61.9% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 1137513 | -49.0% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 740626 | -66.8% |
| `glob` | 2257634 | LLGo · no LTO | 1673971 | -25.9% |
| `glob` | 2257634 | LLGo · deadcode drop | 1040271 | -53.9% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1435170 | -36.4% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 916934 | -59.4% |
| `grep` | 2848917 | LLGo · no LTO | 2063077 | -27.6% |
| `grep` | 2848917 | LLGo · deadcode drop | 1364389 | -52.1% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1804205 | -36.7% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 1245827 | -56.3% |
| `json-wasi` | 3314587 | LLGo · no LTO | 3445017 | +3.9% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 2098205 | -36.7% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 3066284 | -7.5% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 2000758 | -39.6% |
| `llimport` | 8423078 | LLGo · no LTO | 9415558 | +11.8% |
| `llimport` | 8423078 | LLGo · deadcode drop | 8255018 | -2.0% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 8536104 | +1.3% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 7644247 | -9.2% |
| `path-report` | 2381190 | LLGo · no LTO | 1924729 | -19.2% |
| `path-report` | 2381190 | LLGo · deadcode drop | 1285524 | -46.0% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1678055 | -29.5% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 1153552 | -51.6% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 2677458 | -3.7% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1670942 | -39.9% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 2350471 | -15.5% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1502521 | -46.0% |
| `word-count` | 2253620 | LLGo · no LTO | 1641084 | -27.2% |
| `word-count` | 2253620 | LLGo · deadcode drop | 1016410 | -54.9% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 1403568 | -37.7% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 890525 | -60.5% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 13.239x | 10 |
| LLGo · deadcode drop | 8.245x | 10 |
| LLGo · full LTO (GlobalDCE off) | 11.459x | 10 |
| LLGo · full LTO + GlobalDCE | 7.366x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1528896 | +1480.1% |
| `base64` | 96760 | LLGo · deadcode drop | 927106 | +858.2% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 1309682 | +1253.5% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 813920 | +741.2% |
| `checksum` | 92685 | LLGo · no LTO | 1515603 | +1535.2% |
| `checksum` | 92685 | LLGo · deadcode drop | 908697 | +880.4% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 1291281 | +1293.2% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 794500 | +757.2% |
| `conv-wasi` | 201149 | LLGo · no LTO | 2419012 | +1102.6% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 1430948 | +611.4% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 2116759 | +952.3% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1276274 | +534.5% |
| `fibonacci` | 62386 | LLGo · no LTO | 1344703 | +2055.5% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 849188 | +1261.2% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 1137513 | +1723.3% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 740626 | +1087.2% |
| `glob` | 93153 | LLGo · no LTO | 1673971 | +1697.0% |
| `glob` | 93153 | LLGo · deadcode drop | 1040271 | +1016.7% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1435170 | +1440.7% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 916934 | +884.3% |
| `grep` | 303772 | LLGo · no LTO | 2063077 | +579.2% |
| `grep` | 303772 | LLGo · deadcode drop | 1364389 | +349.1% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1804205 | +493.9% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 1245827 | +310.1% |
| `json-wasi` | 493590 | LLGo · no LTO | 3445017 | +598.0% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 2098205 | +325.1% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 3066284 | +521.2% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 2000758 | +305.3% |
| `llimport` | — | LLGo · no LTO | 9415558 | — |
| `llimport` | — | LLGo · deadcode drop | 8255018 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 8536104 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 7644247 | — |
| `path-report` | 116889 | LLGo · no LTO | 1924729 | +1546.6% |
| `path-report` | 116889 | LLGo · deadcode drop | 1285524 | +999.8% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1678055 | +1335.6% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 1153552 | +886.9% |
| `sha-wasi` | 287449 | LLGo · no LTO | 2677458 | +831.5% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1670942 | +481.3% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 2350471 | +717.7% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1502521 | +422.7% |
| `word-count` | 86834 | LLGo · no LTO | 1641084 | +1789.9% |
| `word-count` | 86834 | LLGo · deadcode drop | 1016410 | +1070.5% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 1403568 | +1516.4% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 890525 | +925.5% |

## js/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 1.029x | 12 |
| LLGo · deadcode drop | 0.666x | 12 |
| LLGo · full LTO (GlobalDCE off) | 0.924x | 12 |
| LLGo · full LTO + GlobalDCE | 0.620x | 12 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1957073 | -15.7% |
| `base64` | 2322402 | LLGo · deadcode drop | 1154014 | -50.3% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1738883 | -25.1% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1060974 | -54.3% |
| `checksum` | 2311672 | LLGo · no LTO | 1937483 | -16.2% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1127357 | -51.2% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1703987 | -26.3% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1027018 | -55.6% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 3072172 | +16.4% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1749250 | -33.7% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2743825 | +4.0% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1606904 | -39.1% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1702151 | -25.2% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 1046683 | -54.0% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1492608 | -34.4% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 959177 | -57.8% |
| `glob` | 2305059 | LLGo · no LTO | 2093237 | -9.2% |
| `glob` | 2305059 | LLGo · deadcode drop | 1251386 | -45.7% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1845524 | -19.9% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1144734 | -50.3% |
| `grep` | 2871426 | LLGo · no LTO | 2640447 | -8.0% |
| `grep` | 2871426 | LLGo · deadcode drop | 1687643 | -41.2% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2323968 | -19.1% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1559304 | -45.7% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4280480 | +28.2% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2557775 | -23.4% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3904809 | +17.0% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2520514 | -24.5% |
| `llimport` | 8440671 | LLGo · no LTO | 11421303 | +35.3% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9780098 | +15.9% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10444563 | +23.7% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 9102261 | +7.8% |
| `path-report` | 2428068 | LLGo · no LTO | 2427816 | -0.0% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1576048 | -35.1% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 2169505 | -10.6% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1459811 | -39.9% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3427578 | +21.9% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 2069501 | -26.4% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 3105434 | +10.5% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1945843 | -30.8% |
| `tsgo` | 50367588 | LLGo · no LTO | 73143230 | +45.2% |
| `tsgo` | 50367588 | LLGo · deadcode drop | 72131176 | +43.2% |
| `tsgo` | 50367588 | LLGo · full LTO (GlobalDCE off) | 71541299 | +42.0% |
| `tsgo` | 50367588 | LLGo · full LTO + GlobalDCE | 71214546 | +41.4% |
| `word-count` | 2300998 | LLGo · no LTO | 2053362 | -10.8% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1224394 | -46.8% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1804529 | -21.6% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1111498 | -51.7% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 12.500x | 10 |
| LLGo · deadcode drop | 7.544x | 10 |
| LLGo · full LTO (GlobalDCE off) | 11.112x | 10 |
| LLGo · full LTO + GlobalDCE | 6.987x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1957073 | +1035.8% |
| `base64` | 172302 | LLGo · deadcode drop | 1154014 | +569.8% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1738883 | +909.2% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1060974 | +515.8% |
| `checksum` | 169609 | LLGo · no LTO | 1937483 | +1042.3% |
| `checksum` | 169609 | LLGo · deadcode drop | 1127357 | +564.7% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1703987 | +904.7% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1027018 | +505.5% |
| `conv-wasi` | 165385 | LLGo · no LTO | 3072172 | +1757.6% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1749250 | +957.7% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2743825 | +1559.1% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1606904 | +871.6% |
| `fibonacci` | 141855 | LLGo · no LTO | 1702151 | +1099.9% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 1046683 | +637.9% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1492608 | +952.2% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 959177 | +576.2% |
| `glob` | 136553 | LLGo · no LTO | 2093237 | +1432.9% |
| `glob` | 136553 | LLGo · deadcode drop | 1251386 | +816.4% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1845524 | +1251.5% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1144734 | +738.3% |
| `grep` | 155984 | LLGo · no LTO | 2640447 | +1592.8% |
| `grep` | 155984 | LLGo · deadcode drop | 1687643 | +981.9% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2323968 | +1389.9% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1559304 | +899.7% |
| `json-wasi` | 525666 | LLGo · no LTO | 4280480 | +714.3% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2557775 | +386.6% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3904809 | +642.8% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2520514 | +379.5% |
| `llimport` | — | LLGo · no LTO | 11421303 | — |
| `llimport` | — | LLGo · deadcode drop | 9780098 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10444563 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 9102261 | — |
| `path-report` | 194133 | LLGo · no LTO | 2427816 | +1150.6% |
| `path-report` | 194133 | LLGo · deadcode drop | 1576048 | +711.8% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 2169505 | +1017.5% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1459811 | +652.0% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3427578 | +873.8% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 2069501 | +488.0% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 3105434 | +782.3% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1945843 | +452.8% |
| `tsgo` | — | LLGo · no LTO | 73143230 | — |
| `tsgo` | — | LLGo · deadcode drop | 72131176 | — |
| `tsgo` | — | LLGo · full LTO (GlobalDCE off) | 71541299 | — |
| `tsgo` | — | LLGo · full LTO + GlobalDCE | 71214546 | — |
| `word-count` | 164053 | LLGo · no LTO | 2053362 | +1151.6% |
| `word-count` | 164053 | LLGo · deadcode drop | 1224394 | +646.3% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1804529 | +1000.0% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1111498 | +577.5% |
