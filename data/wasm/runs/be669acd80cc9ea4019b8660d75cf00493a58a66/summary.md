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
| LLGo · no LTO | 0.811x | 11 |
| LLGo · deadcode drop | 0.523x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.706x | 11 |
| LLGo · full LTO + GlobalDCE | 0.470x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1536691 | -32.5% |
| `base64` | 2275731 | LLGo · deadcode drop | 933929 | -59.0% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 1317526 | -42.1% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 820730 | -63.9% |
| `checksum` | 2264417 | LLGo · no LTO | 1523414 | -32.7% |
| `checksum` | 2264417 | LLGo · deadcode drop | 915520 | -59.6% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 1299123 | -42.6% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 801308 | -64.6% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 2434222 | -6.7% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 1447925 | -44.5% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 2133233 | -18.2% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1293252 | -50.4% |
| `fibonacci` | 2230899 | LLGo · no LTO | 1352543 | -39.4% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 856040 | -61.6% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 1145384 | -48.7% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 747463 | -66.5% |
| `glob` | 2257634 | LLGo · no LTO | 1688602 | -25.2% |
| `glob` | 2257634 | LLGo · deadcode drop | 1053914 | -53.3% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1449832 | -35.8% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 930578 | -58.8% |
| `grep` | 2848917 | LLGo · no LTO | 2081807 | -26.9% |
| `grep` | 2848917 | LLGo · deadcode drop | 1382131 | -51.5% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1822996 | -36.0% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 1263584 | -55.6% |
| `json-wasi` | 3314587 | LLGo · no LTO | 3471958 | +4.7% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 2127158 | -35.8% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 3093790 | -6.7% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 2029719 | -38.8% |
| `llimport` | 8423078 | LLGo · no LTO | 9908595 | +17.6% |
| `llimport` | 8423078 | LLGo · deadcode drop | 8745971 | +3.8% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 9016306 | +7.0% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 8131890 | -3.5% |
| `path-report` | 2381190 | LLGo · no LTO | 1939360 | -18.6% |
| `path-report` | 2381190 | LLGo · deadcode drop | 1299167 | -45.4% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1692717 | -28.9% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 1167196 | -51.0% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 2693599 | -3.1% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1688850 | -39.3% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 2368080 | -14.8% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1520623 | -45.3% |
| `word-count` | 2253620 | LLGo · no LTO | 1655699 | -26.5% |
| `word-count` | 2253620 | LLGo · deadcode drop | 1030037 | -54.3% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 1418230 | -37.1% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 904153 | -59.9% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 13.332x | 10 |
| LLGo · deadcode drop | 8.335x | 10 |
| LLGo · full LTO (GlobalDCE off) | 11.554x | 10 |
| LLGo · full LTO + GlobalDCE | 7.456x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1536691 | +1488.1% |
| `base64` | 96760 | LLGo · deadcode drop | 933929 | +865.2% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 1317526 | +1261.6% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 820730 | +748.2% |
| `checksum` | 92685 | LLGo · no LTO | 1523414 | +1543.6% |
| `checksum` | 92685 | LLGo · deadcode drop | 915520 | +887.8% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 1299123 | +1301.7% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 801308 | +764.5% |
| `conv-wasi` | 201149 | LLGo · no LTO | 2434222 | +1110.2% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 1447925 | +619.8% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 2133233 | +960.5% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1293252 | +542.9% |
| `fibonacci` | 62386 | LLGo · no LTO | 1352543 | +2068.0% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 856040 | +1272.2% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 1145384 | +1736.0% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 747463 | +1098.1% |
| `glob` | 93153 | LLGo · no LTO | 1688602 | +1712.7% |
| `glob` | 93153 | LLGo · deadcode drop | 1053914 | +1031.4% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1449832 | +1456.4% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 930578 | +899.0% |
| `grep` | 303772 | LLGo · no LTO | 2081807 | +585.3% |
| `grep` | 303772 | LLGo · deadcode drop | 1382131 | +355.0% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1822996 | +500.1% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 1263584 | +316.0% |
| `json-wasi` | 493590 | LLGo · no LTO | 3471958 | +603.4% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 2127158 | +331.0% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 3093790 | +526.8% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 2029719 | +311.2% |
| `llimport` | — | LLGo · no LTO | 9908595 | — |
| `llimport` | — | LLGo · deadcode drop | 8745971 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 9016306 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 8131890 | — |
| `path-report` | 116889 | LLGo · no LTO | 1939360 | +1559.1% |
| `path-report` | 116889 | LLGo · deadcode drop | 1299167 | +1011.5% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1692717 | +1348.1% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 1167196 | +898.6% |
| `sha-wasi` | 287449 | LLGo · no LTO | 2693599 | +837.1% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1688850 | +487.5% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 2368080 | +723.8% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1520623 | +429.0% |
| `word-count` | 86834 | LLGo · no LTO | 1655699 | +1806.7% |
| `word-count` | 86834 | LLGo · deadcode drop | 1030037 | +1086.2% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 1418230 | +1533.3% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 904153 | +941.2% |

## js/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 1.054x | 12 |
| LLGo · deadcode drop | 0.690x | 12 |
| LLGo · full LTO (GlobalDCE off) | 0.949x | 12 |
| LLGo · full LTO + GlobalDCE | 0.643x | 12 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1975975 | -14.9% |
| `base64` | 2322402 | LLGo · deadcode drop | 1172612 | -49.5% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1756903 | -24.3% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1078570 | -53.6% |
| `checksum` | 2311672 | LLGo · no LTO | 1955649 | -15.4% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1145200 | -50.5% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1721308 | -25.5% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1043908 | -54.8% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 3138169 | +18.9% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1811838 | -31.3% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2808896 | +6.5% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1668421 | -36.8% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1721176 | -24.3% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 1065385 | -53.2% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1510621 | -33.6% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 976750 | -57.1% |
| `glob` | 2305059 | LLGo · no LTO | 2140934 | -7.1% |
| `glob` | 2305059 | LLGo · deadcode drop | 1299016 | -43.6% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1892287 | -17.9% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1191083 | -48.3% |
| `grep` | 2871426 | LLGo · no LTO | 2697070 | -6.1% |
| `grep` | 2871426 | LLGo · deadcode drop | 1743936 | -39.3% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2379550 | -17.1% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1614452 | -43.8% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4386347 | +31.4% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2660339 | -20.3% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 4009394 | +20.1% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2621425 | -21.5% |
| `llimport` | 8440671 | LLGo · no LTO | 12318047 | +45.9% |
| `llimport` | 8440671 | LLGo · deadcode drop | 10668540 | +26.4% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 11320420 | +34.1% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 9975801 | +18.2% |
| `path-report` | 2428068 | LLGo · no LTO | 2475883 | +2.0% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1623781 | -33.1% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 2216396 | -8.7% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1506309 | -38.0% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3496995 | +24.4% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 2135501 | -24.0% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 3174357 | +12.9% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 2011250 | -28.5% |
| `tsgo` | 50367588 | LLGo · no LTO | 75770164 | +50.4% |
| `tsgo` | 50367588 | LLGo · deadcode drop | 74760267 | +48.4% |
| `tsgo` | 50367588 | LLGo · full LTO (GlobalDCE off) | 74156794 | +47.2% |
| `tsgo` | 50367588 | LLGo · full LTO + GlobalDCE | 73838012 | +46.6% |
| `word-count` | 2300998 | LLGo · no LTO | 2100650 | -8.7% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1271356 | -44.7% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1850890 | -19.6% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1157411 | -49.7% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 12.730x | 10 |
| LLGo · deadcode drop | 7.768x | 10 |
| LLGo · full LTO (GlobalDCE off) | 11.336x | 10 |
| LLGo · full LTO + GlobalDCE | 7.205x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1975975 | +1046.8% |
| `base64` | 172302 | LLGo · deadcode drop | 1172612 | +580.6% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1756903 | +919.7% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1078570 | +526.0% |
| `checksum` | 169609 | LLGo · no LTO | 1955649 | +1053.0% |
| `checksum` | 169609 | LLGo · deadcode drop | 1145200 | +575.2% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1721308 | +914.9% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1043908 | +515.5% |
| `conv-wasi` | 165385 | LLGo · no LTO | 3138169 | +1797.5% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1811838 | +995.5% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2808896 | +1598.4% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1668421 | +908.8% |
| `fibonacci` | 141855 | LLGo · no LTO | 1721176 | +1113.3% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 1065385 | +651.0% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1510621 | +964.9% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 976750 | +588.6% |
| `glob` | 136553 | LLGo · no LTO | 2140934 | +1467.8% |
| `glob` | 136553 | LLGo · deadcode drop | 1299016 | +851.3% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1892287 | +1285.8% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1191083 | +772.2% |
| `grep` | 155984 | LLGo · no LTO | 2697070 | +1629.1% |
| `grep` | 155984 | LLGo · deadcode drop | 1743936 | +1018.0% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2379550 | +1425.5% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1614452 | +935.0% |
| `json-wasi` | 525666 | LLGo · no LTO | 4386347 | +734.4% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2660339 | +406.1% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 4009394 | +662.7% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2621425 | +398.7% |
| `llimport` | — | LLGo · no LTO | 12318047 | — |
| `llimport` | — | LLGo · deadcode drop | 10668540 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 11320420 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 9975801 | — |
| `path-report` | 194133 | LLGo · no LTO | 2475883 | +1175.4% |
| `path-report` | 194133 | LLGo · deadcode drop | 1623781 | +736.4% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 2216396 | +1041.7% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1506309 | +675.9% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3496995 | +893.5% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 2135501 | +506.7% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 3174357 | +801.9% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 2011250 | +471.4% |
| `tsgo` | — | LLGo · no LTO | 75770164 | — |
| `tsgo` | — | LLGo · deadcode drop | 74760267 | — |
| `tsgo` | — | LLGo · full LTO (GlobalDCE off) | 74156794 | — |
| `tsgo` | — | LLGo · full LTO + GlobalDCE | 73838012 | — |
| `word-count` | 164053 | LLGo · no LTO | 2100650 | +1180.5% |
| `word-count` | 164053 | LLGo · deadcode drop | 1271356 | +675.0% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1850890 | +1028.2% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1157411 | +605.5% |
