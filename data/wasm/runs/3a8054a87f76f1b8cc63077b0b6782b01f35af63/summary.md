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

## js/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 1.126x | 12 |
| LLGo · deadcode drop | 0.715x | 12 |
| LLGo · full LTO (GlobalDCE off) | 1.015x | 12 |
| LLGo · full LTO + GlobalDCE | 0.667x | 12 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 2086537 | -10.2% |
| `base64` | 2322402 | LLGo · deadcode drop | 1190518 | -48.7% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1860989 | -19.9% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1097530 | -52.7% |
| `checksum` | 2311672 | LLGo · no LTO | 2066435 | -10.6% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1162446 | -49.7% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1825540 | -21.0% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1061918 | -54.1% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 3293259 | +24.8% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1839934 | -30.3% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2952496 | +11.9% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1694607 | -35.8% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1813223 | -20.3% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 1079404 | -52.5% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1596118 | -29.8% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 991431 | -56.4% |
| `glob` | 2305059 | LLGo · no LTO | 2253509 | -2.2% |
| `glob` | 2305059 | LLGo · deadcode drop | 1316957 | -42.9% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1997029 | -13.4% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1208583 | -47.6% |
| `grep` | 2871426 | LLGo · no LTO | 2826387 | -1.6% |
| `grep` | 2871426 | LLGo · deadcode drop | 1772755 | -38.3% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2501036 | -12.9% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1644817 | -42.7% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4607004 | +38.0% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2716685 | -18.6% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 4210062 | +26.1% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2679364 | -19.7% |
| `llimport` | 8440671 | LLGo · no LTO | 12836774 | +52.1% |
| `llimport` | 8440671 | LLGo · deadcode drop | 11015704 | +30.5% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 11833078 | +40.2% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 10320497 | +22.3% |
| `path-report` | 2428068 | LLGo · no LTO | 2602183 | +7.2% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1655315 | -31.8% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 2332346 | -3.9% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1535347 | -36.8% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3662733 | +30.3% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 2172863 | -22.7% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 3326789 | +18.3% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 2045057 | -27.3% |
| `tsgo` | 50367588 | LLGo · no LTO | 96072444 | +90.7% |
| `tsgo` | 50367588 | LLGo · deadcode drop | 94938540 | +88.5% |
| `tsgo` | 50367588 | LLGo · full LTO (GlobalDCE off) | 93885379 | +86.4% |
| `tsgo` | 50367588 | LLGo · full LTO + GlobalDCE | 93533111 | +85.7% |
| `word-count` | 2300998 | LLGo · no LTO | 2212848 | -3.8% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1289175 | -44.0% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1954901 | -15.0% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1174648 | -49.0% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 13.389x | 10 |
| LLGo · deadcode drop | 7.894x | 10 |
| LLGo · full LTO (GlobalDCE off) | 11.949x | 10 |
| LLGo · full LTO + GlobalDCE | 7.329x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 2086537 | +1111.0% |
| `base64` | 172302 | LLGo · deadcode drop | 1190518 | +590.9% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1860989 | +980.1% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1097530 | +537.0% |
| `checksum` | 169609 | LLGo · no LTO | 2066435 | +1118.4% |
| `checksum` | 169609 | LLGo · deadcode drop | 1162446 | +585.4% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1825540 | +976.3% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1061918 | +526.1% |
| `conv-wasi` | 165385 | LLGo · no LTO | 3293259 | +1891.3% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1839934 | +1012.5% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2952496 | +1685.2% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1694607 | +924.6% |
| `fibonacci` | 141855 | LLGo · no LTO | 1813223 | +1178.2% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 1079404 | +660.9% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1596118 | +1025.2% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 991431 | +598.9% |
| `glob` | 136553 | LLGo · no LTO | 2253509 | +1550.3% |
| `glob` | 136553 | LLGo · deadcode drop | 1316957 | +864.4% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1997029 | +1362.5% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1208583 | +785.1% |
| `grep` | 155984 | LLGo · no LTO | 2826387 | +1712.0% |
| `grep` | 155984 | LLGo · deadcode drop | 1772755 | +1036.5% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2501036 | +1503.4% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1644817 | +954.5% |
| `json-wasi` | 525666 | LLGo · no LTO | 4607004 | +776.4% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2716685 | +416.8% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 4210062 | +700.9% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2679364 | +409.7% |
| `llimport` | — | LLGo · no LTO | 12836774 | — |
| `llimport` | — | LLGo · deadcode drop | 11015704 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 11833078 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 10320497 | — |
| `path-report` | 194133 | LLGo · no LTO | 2602183 | +1240.4% |
| `path-report` | 194133 | LLGo · deadcode drop | 1655315 | +752.7% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 2332346 | +1101.4% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1535347 | +690.9% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3662733 | +940.6% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 2172863 | +517.3% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 3326789 | +845.2% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 2045057 | +481.0% |
| `tsgo` | — | LLGo · no LTO | 96072444 | — |
| `tsgo` | — | LLGo · deadcode drop | 94938540 | — |
| `tsgo` | — | LLGo · full LTO (GlobalDCE off) | 93885379 | — |
| `tsgo` | — | LLGo · full LTO + GlobalDCE | 93533111 | — |
| `word-count` | 164053 | LLGo · no LTO | 2212848 | +1248.9% |
| `word-count` | 164053 | LLGo · deadcode drop | 1289175 | +685.8% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1954901 | +1091.6% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1174648 | +616.0% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.809x | 11 |
| LLGo · deadcode drop | 0.521x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.625x | 11 |
| LLGo · full LTO + GlobalDCE | 0.445x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1530673 | -32.7% |
| `base64` | 2275731 | LLGo · deadcode drop | 927886 | -59.2% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 1167488 | -48.7% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 797446 | -65.0% |
| `checksum` | 2264417 | LLGo · no LTO | 1517380 | -33.0% |
| `checksum` | 2264417 | LLGo · deadcode drop | 909477 | -59.8% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 1148897 | -49.3% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 777966 | -65.6% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 2428196 | -6.9% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 1441891 | -44.7% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1959902 | -24.9% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1256622 | -51.8% |
| `fibonacci` | 2230899 | LLGo · no LTO | 1346501 | -39.6% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 850005 | -61.9% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 1000226 | -55.2% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 728417 | -67.3% |
| `glob` | 2257634 | LLGo · no LTO | 1682584 | -25.5% |
| `glob` | 2257634 | LLGo · deadcode drop | 1047871 | -53.6% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1299606 | -42.4% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 907228 | -59.8% |
| `grep` | 2848917 | LLGo · no LTO | 2075764 | -27.1% |
| `grep` | 2848917 | LLGo · deadcode drop | 1376096 | -51.7% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1623569 | -43.0% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 1190396 | -58.2% |
| `json-wasi` | 3314587 | LLGo · no LTO | 3465915 | +4.6% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 2121116 | -36.0% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2804434 | -15.4% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1940440 | -41.5% |
| `llimport` | 8423078 | LLGo · no LTO | 9902537 | +17.6% |
| `llimport` | 8423078 | LLGo · deadcode drop | 8739929 | +3.8% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 6955322 | -17.4% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6143719 | -27.1% |
| `path-report` | 2381190 | LLGo · no LTO | 1933333 | -18.8% |
| `path-report` | 2381190 | LLGo · deadcode drop | 1293148 | -45.7% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1541168 | -35.3% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 1142523 | -52.0% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 2687556 | -3.4% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1682815 | -39.5% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 2174322 | -21.8% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1463316 | -47.4% |
| `word-count` | 2253620 | LLGo · no LTO | 1649657 | -26.8% |
| `word-count` | 2253620 | LLGo · deadcode drop | 1024002 | -54.6% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 1268004 | -43.7% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 880803 | -60.9% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 13.289x | 10 |
| LLGo · deadcode drop | 8.292x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.373x | 10 |
| LLGo · full LTO + GlobalDCE | 7.215x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1530673 | +1481.9% |
| `base64` | 96760 | LLGo · deadcode drop | 927886 | +859.0% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 1167488 | +1106.6% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 797446 | +724.1% |
| `checksum` | 92685 | LLGo · no LTO | 1517380 | +1537.1% |
| `checksum` | 92685 | LLGo · deadcode drop | 909477 | +881.3% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 1148897 | +1139.6% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 777966 | +739.4% |
| `conv-wasi` | 201149 | LLGo · no LTO | 2428196 | +1107.2% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 1441891 | +616.8% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1959902 | +874.4% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1256622 | +524.7% |
| `fibonacci` | 62386 | LLGo · no LTO | 1346501 | +2058.3% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 850005 | +1262.5% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 1000226 | +1503.3% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 728417 | +1067.6% |
| `glob` | 93153 | LLGo · no LTO | 1682584 | +1706.3% |
| `glob` | 93153 | LLGo · deadcode drop | 1047871 | +1024.9% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1299606 | +1295.1% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 907228 | +873.9% |
| `grep` | 303772 | LLGo · no LTO | 2075764 | +583.3% |
| `grep` | 303772 | LLGo · deadcode drop | 1376096 | +353.0% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1623569 | +434.5% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 1190396 | +291.9% |
| `json-wasi` | 493590 | LLGo · no LTO | 3465915 | +602.2% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 2121116 | +329.7% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2804434 | +468.2% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1940440 | +293.1% |
| `llimport` | — | LLGo · no LTO | 9902537 | — |
| `llimport` | — | LLGo · deadcode drop | 8739929 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 6955322 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6143719 | — |
| `path-report` | 116889 | LLGo · no LTO | 1933333 | +1554.0% |
| `path-report` | 116889 | LLGo · deadcode drop | 1293148 | +1006.3% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1541168 | +1218.5% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 1142523 | +877.4% |
| `sha-wasi` | 287449 | LLGo · no LTO | 2687556 | +835.0% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1682815 | +485.4% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 2174322 | +656.4% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1463316 | +409.1% |
| `word-count` | 86834 | LLGo · no LTO | 1649657 | +1799.8% |
| `word-count` | 86834 | LLGo · deadcode drop | 1024002 | +1079.3% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 1268004 | +1360.3% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 880803 | +914.4% |
