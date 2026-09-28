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
| tsgo | LLGoNoLTO | required | failed | [logs/tsgo.LLGoNoLTO.log](logs/tsgo.LLGoNoLTO.log) |
| tsgo | LLGoDeadcodeDrop | required | failed | [logs/tsgo.LLGoDeadcodeDrop.log](logs/tsgo.LLGoDeadcodeDrop.log) |
| tsgo | LLGoFullLTONoGlobalDCE | required | failed | [logs/tsgo.LLGoFullLTONoGlobalDCE.log](logs/tsgo.LLGoFullLTONoGlobalDCE.log) |
| tsgo | LLGoFullLTOGlobalDCE | required | failed | [logs/tsgo.LLGoFullLTOGlobalDCE.log](logs/tsgo.LLGoFullLTOGlobalDCE.log) |

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
| LLGo · no LTO | 0.912x | 11 |
| LLGo · deadcode drop | 0.588x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.732x | 11 |
| LLGo · full LTO + GlobalDCE | 0.525x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1672035 | -26.5% |
| `base64` | 2275731 | LLGo · deadcode drop | 1011871 | -55.5% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 1306892 | -42.6% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 913088 | -59.9% |
| `checksum` | 2264417 | LLGo · no LTO | 1648944 | -27.2% |
| `checksum` | 2264417 | LLGo · deadcode drop | 984163 | -56.5% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 1277127 | -43.6% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 880502 | -61.1% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 2800441 | +7.4% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 1633748 | -37.4% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 2351477 | -9.8% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1473159 | -43.5% |
| `fibonacci` | 2230899 | LLGo · no LTO | 1382734 | -38.0% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 909171 | -59.2% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 1112213 | -50.1% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 819943 | -63.2% |
| `glob` | 2257634 | LLGo · no LTO | 1840032 | -18.5% |
| `glob` | 2257634 | LLGo · deadcode drop | 1142704 | -49.4% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1469083 | -34.9% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 1032372 | -54.3% |
| `grep` | 2848917 | LLGo · no LTO | 2374033 | -16.7% |
| `grep` | 2848917 | LLGo · deadcode drop | 1582555 | -44.5% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1925940 | -32.4% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 1417339 | -50.2% |
| `json-wasi` | 3314587 | LLGo · no LTO | 4107917 | +23.9% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 2490476 | -24.9% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 3470171 | +4.7% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 2368168 | -28.6% |
| `llimport` | 8423078 | LLGo · no LTO | 12442400 | +47.7% |
| `llimport` | 8423078 | LLGo · deadcode drop | 10969327 | +30.2% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 8978268 | +6.6% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 8275675 | -1.7% |
| `path-report` | 2381190 | LLGo · no LTO | 2180289 | -8.4% |
| `path-report` | 2381190 | LLGo · deadcode drop | 1473915 | -38.1% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1795382 | -24.6% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 1349683 | -43.3% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 3135823 | +12.8% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1938566 | -30.3% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 2661807 | -4.3% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1768512 | -36.4% |
| `word-count` | 2253620 | LLGo · no LTO | 1800402 | -20.1% |
| `word-count` | 2253620 | LLGo · deadcode drop | 1116126 | -50.5% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 1413380 | -37.3% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 999786 | -55.6% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 14.829x | 10 |
| LLGo · deadcode drop | 9.259x | 10 |
| LLGo · full LTO (GlobalDCE off) | 12.023x | 10 |
| LLGo · full LTO + GlobalDCE | 8.401x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1672035 | +1628.0% |
| `base64` | 96760 | LLGo · deadcode drop | 1011871 | +945.8% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 1306892 | +1250.7% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 913088 | +843.7% |
| `checksum` | 92685 | LLGo · no LTO | 1648944 | +1679.1% |
| `checksum` | 92685 | LLGo · deadcode drop | 984163 | +961.8% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 1277127 | +1277.9% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 880502 | +850.0% |
| `conv-wasi` | 201149 | LLGo · no LTO | 2800441 | +1292.2% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 1633748 | +712.2% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 2351477 | +1069.0% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1473159 | +632.4% |
| `fibonacci` | 62386 | LLGo · no LTO | 1382734 | +2116.4% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 909171 | +1357.3% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 1112213 | +1682.8% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 819943 | +1214.3% |
| `glob` | 93153 | LLGo · no LTO | 1840032 | +1875.3% |
| `glob` | 93153 | LLGo · deadcode drop | 1142704 | +1126.7% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1469083 | +1477.1% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 1032372 | +1008.3% |
| `grep` | 303772 | LLGo · no LTO | 2374033 | +681.5% |
| `grep` | 303772 | LLGo · deadcode drop | 1582555 | +421.0% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1925940 | +534.0% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 1417339 | +366.6% |
| `json-wasi` | 493590 | LLGo · no LTO | 4107917 | +732.3% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 2490476 | +404.6% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 3470171 | +603.0% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 2368168 | +379.8% |
| `llimport` | — | LLGo · no LTO | 12442400 | — |
| `llimport` | — | LLGo · deadcode drop | 10969327 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 8978268 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 8275675 | — |
| `path-report` | 116889 | LLGo · no LTO | 2180289 | +1765.3% |
| `path-report` | 116889 | LLGo · deadcode drop | 1473915 | +1161.0% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1795382 | +1436.0% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 1349683 | +1054.7% |
| `sha-wasi` | 287449 | LLGo · no LTO | 3135823 | +990.9% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1938566 | +574.4% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 2661807 | +826.0% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1768512 | +515.2% |
| `word-count` | 86834 | LLGo · no LTO | 1800402 | +1973.4% |
| `word-count` | 86834 | LLGo · deadcode drop | 1116126 | +1185.4% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 1413380 | +1527.7% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 999786 | +1051.4% |

## js/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 1.068x | 11 |
| LLGo · deadcode drop | 0.650x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.956x | 11 |
| LLGo · full LTO + GlobalDCE | 0.604x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 2074005 | -10.7% |
| `base64` | 2322402 | LLGo · deadcode drop | 1178429 | -49.3% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1849956 | -20.3% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1086927 | -53.2% |
| `checksum` | 2311672 | LLGo · no LTO | 2053906 | -11.2% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1150347 | -50.2% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1814475 | -21.5% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1051259 | -54.5% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 3280239 | +24.3% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1827312 | -30.7% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2941464 | +11.5% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1683835 | -36.2% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1800690 | -20.8% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 1067284 | -53.1% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1585045 | -30.3% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 980794 | -56.9% |
| `glob` | 2305059 | LLGo · no LTO | 2240983 | -2.8% |
| `glob` | 2305059 | LLGo · deadcode drop | 1304822 | -43.4% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1985955 | -13.8% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1197957 | -48.0% |
| `grep` | 2871426 | LLGo · no LTO | 2813834 | -2.0% |
| `grep` | 2871426 | LLGo · deadcode drop | 1760662 | -38.7% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2489978 | -13.3% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1634185 | -43.1% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4593976 | +37.6% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2704078 | -19.0% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 4198786 | +25.8% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2668310 | -20.1% |
| `llimport` | 8440671 | LLGo · no LTO | 12822827 | +51.9% |
| `llimport` | 8440671 | LLGo · deadcode drop | 11001726 | +30.3% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 11820566 | +40.0% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 10308655 | +22.1% |
| `path-report` | 2428068 | LLGo · no LTO | 2589653 | +6.7% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1643215 | -32.3% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 2321281 | -4.4% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1524701 | -37.2% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3649732 | +29.8% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 2160275 | -23.2% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 3315739 | +18.0% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 2034265 | -27.6% |
| `tsgo` | 50367588 | LLGo · no LTO | — | — |
| `tsgo` | 50367588 | LLGo · deadcode drop | — | — |
| `tsgo` | 50367588 | LLGo · full LTO (GlobalDCE off) | — | — |
| `tsgo` | 50367588 | LLGo · full LTO + GlobalDCE | — | — |
| `word-count` | 2300998 | LLGo · no LTO | 2200310 | -4.4% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1277069 | -44.5% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1943822 | -15.5% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1163996 | -49.4% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 13.323x | 10 |
| LLGo · deadcode drop | 7.829x | 10 |
| LLGo · full LTO (GlobalDCE off) | 11.891x | 10 |
| LLGo · full LTO + GlobalDCE | 7.272x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 2074005 | +1103.7% |
| `base64` | 172302 | LLGo · deadcode drop | 1178429 | +583.9% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1849956 | +973.7% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1086927 | +530.8% |
| `checksum` | 169609 | LLGo · no LTO | 2053906 | +1111.0% |
| `checksum` | 169609 | LLGo · deadcode drop | 1150347 | +578.2% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1814475 | +969.8% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1051259 | +519.8% |
| `conv-wasi` | 165385 | LLGo · no LTO | 3280239 | +1883.4% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1827312 | +1004.9% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2941464 | +1678.6% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1683835 | +918.1% |
| `fibonacci` | 141855 | LLGo · no LTO | 1800690 | +1169.4% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 1067284 | +652.4% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1585045 | +1017.4% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 980794 | +591.4% |
| `glob` | 136553 | LLGo · no LTO | 2240983 | +1541.1% |
| `glob` | 136553 | LLGo · deadcode drop | 1304822 | +855.5% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1985955 | +1354.3% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1197957 | +777.3% |
| `grep` | 155984 | LLGo · no LTO | 2813834 | +1703.9% |
| `grep` | 155984 | LLGo · deadcode drop | 1760662 | +1028.7% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2489978 | +1496.3% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1634185 | +947.7% |
| `json-wasi` | 525666 | LLGo · no LTO | 4593976 | +773.9% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2704078 | +414.4% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 4198786 | +698.8% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2668310 | +407.6% |
| `llimport` | — | LLGo · no LTO | 12822827 | — |
| `llimport` | — | LLGo · deadcode drop | 11001726 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 11820566 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 10308655 | — |
| `path-report` | 194133 | LLGo · no LTO | 2589653 | +1234.0% |
| `path-report` | 194133 | LLGo · deadcode drop | 1643215 | +746.4% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 2321281 | +1095.7% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1524701 | +685.4% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3649732 | +936.9% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 2160275 | +513.8% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 3315739 | +842.0% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 2034265 | +478.0% |
| `tsgo` | — | LLGo · no LTO | — | — |
| `tsgo` | — | LLGo · deadcode drop | — | — |
| `tsgo` | — | LLGo · full LTO (GlobalDCE off) | — | — |
| `tsgo` | — | LLGo · full LTO + GlobalDCE | — | — |
| `word-count` | 164053 | LLGo · no LTO | 2200310 | +1241.2% |
| `word-count` | 164053 | LLGo · deadcode drop | 1277069 | +678.4% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1943822 | +1084.9% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1163996 | +609.5% |
