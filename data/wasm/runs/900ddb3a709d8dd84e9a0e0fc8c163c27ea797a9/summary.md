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
| LLGo · no LTO | 1.051x | 12 |
| LLGo · deadcode drop | 0.686x | 12 |
| LLGo · full LTO (GlobalDCE off) | 0.947x | 12 |
| LLGo · full LTO + GlobalDCE | 0.641x | 12 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1968124 | -15.3% |
| `base64` | 2322402 | LLGo · deadcode drop | 1164746 | -49.8% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1751799 | -24.6% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1073490 | -53.8% |
| `checksum` | 2311672 | LLGo · no LTO | 1947792 | -15.7% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1137336 | -50.8% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1716193 | -25.8% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1038788 | -55.1% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 3130290 | +18.6% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1804008 | -31.6% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2803810 | +6.3% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1663303 | -37.0% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1713323 | -24.7% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 1057544 | -53.5% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1505522 | -33.8% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 971639 | -57.3% |
| `glob` | 2305059 | LLGo · no LTO | 2133090 | -7.5% |
| `glob` | 2305059 | LLGo · deadcode drop | 1291169 | -44.0% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1887197 | -18.1% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1185977 | -48.5% |
| `grep` | 2871426 | LLGo · no LTO | 2689216 | -6.3% |
| `grep` | 2871426 | LLGo · deadcode drop | 1736058 | -39.5% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2374418 | -17.3% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1609337 | -44.0% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4378479 | +31.2% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2652485 | -20.5% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 4004281 | +19.9% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2616305 | -21.6% |
| `llimport` | 8440671 | LLGo · no LTO | 12310103 | +45.8% |
| `llimport` | 8440671 | LLGo · deadcode drop | 10660559 | +26.3% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 11315137 | +34.1% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 9971006 | +18.1% |
| `path-report` | 2428068 | LLGo · no LTO | 2468037 | +1.6% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1615919 | -33.4% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 2211284 | -8.9% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1501195 | -38.2% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3489093 | +24.1% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 2127630 | -24.3% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 3169290 | +12.7% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 2006179 | -28.6% |
| `tsgo` | 50367588 | LLGo · no LTO | 75762106 | +50.4% |
| `tsgo` | 50367588 | LLGo · deadcode drop | 74752286 | +48.4% |
| `tsgo` | 50367588 | LLGo · full LTO (GlobalDCE off) | 74151407 | +47.2% |
| `tsgo` | 50367588 | LLGo · full LTO + GlobalDCE | 73832749 | +46.6% |
| `word-count` | 2300998 | LLGo · no LTO | 2092811 | -9.0% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1263525 | -45.1% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1845799 | -19.8% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1152347 | -49.9% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 12.688x | 10 |
| LLGo · deadcode drop | 7.727x | 10 |
| LLGo · full LTO (GlobalDCE off) | 11.309x | 10 |
| LLGo · full LTO + GlobalDCE | 7.178x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1968124 | +1042.3% |
| `base64` | 172302 | LLGo · deadcode drop | 1164746 | +576.0% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1751799 | +916.7% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1073490 | +523.0% |
| `checksum` | 169609 | LLGo · no LTO | 1947792 | +1048.4% |
| `checksum` | 169609 | LLGo · deadcode drop | 1137336 | +570.6% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1716193 | +911.9% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1038788 | +512.5% |
| `conv-wasi` | 165385 | LLGo · no LTO | 3130290 | +1792.7% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1804008 | +990.8% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2803810 | +1595.3% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1663303 | +905.7% |
| `fibonacci` | 141855 | LLGo · no LTO | 1713323 | +1107.8% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 1057544 | +645.5% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1505522 | +961.3% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 971639 | +585.0% |
| `glob` | 136553 | LLGo · no LTO | 2133090 | +1462.1% |
| `glob` | 136553 | LLGo · deadcode drop | 1291169 | +845.5% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1887197 | +1282.0% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1185977 | +768.5% |
| `grep` | 155984 | LLGo · no LTO | 2689216 | +1624.0% |
| `grep` | 155984 | LLGo · deadcode drop | 1736058 | +1013.0% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2374418 | +1422.2% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1609337 | +931.7% |
| `json-wasi` | 525666 | LLGo · no LTO | 4378479 | +732.9% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2652485 | +404.6% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 4004281 | +661.8% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2616305 | +397.7% |
| `llimport` | — | LLGo · no LTO | 12310103 | — |
| `llimport` | — | LLGo · deadcode drop | 10660559 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 11315137 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 9971006 | — |
| `path-report` | 194133 | LLGo · no LTO | 2468037 | +1171.3% |
| `path-report` | 194133 | LLGo · deadcode drop | 1615919 | +732.4% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 2211284 | +1039.1% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1501195 | +673.3% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3489093 | +891.3% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 2127630 | +504.5% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 3169290 | +800.4% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 2006179 | +470.0% |
| `tsgo` | — | LLGo · no LTO | 75762106 | — |
| `tsgo` | — | LLGo · deadcode drop | 74752286 | — |
| `tsgo` | — | LLGo · full LTO (GlobalDCE off) | 74151407 | — |
| `tsgo` | — | LLGo · full LTO + GlobalDCE | 73832749 | — |
| `word-count` | 164053 | LLGo · no LTO | 2092811 | +1175.7% |
| `word-count` | 164053 | LLGo · deadcode drop | 1263525 | +670.2% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1845799 | +1025.1% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1152347 | +602.4% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.809x | 11 |
| LLGo · deadcode drop | 0.521x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.705x | 11 |
| LLGo · full LTO + GlobalDCE | 0.468x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1530673 | -32.7% |
| `base64` | 2275731 | LLGo · deadcode drop | 927886 | -59.2% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 1313479 | -42.3% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 816683 | -64.1% |
| `checksum` | 2264417 | LLGo · no LTO | 1517380 | -33.0% |
| `checksum` | 2264417 | LLGo · deadcode drop | 909477 | -59.8% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 1295076 | -42.8% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 797261 | -64.8% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 2428196 | -6.9% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 1441891 | -44.7% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 2129208 | -18.4% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1289220 | -50.6% |
| `fibonacci` | 2230899 | LLGo · no LTO | 1346501 | -39.6% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 850005 | -61.9% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 1141329 | -48.8% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 743408 | -66.7% |
| `glob` | 2257634 | LLGo · no LTO | 1682584 | -25.5% |
| `glob` | 2257634 | LLGo · deadcode drop | 1047871 | -53.6% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1445785 | -36.0% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 926523 | -59.0% |
| `grep` | 2848917 | LLGo · no LTO | 2075764 | -27.1% |
| `grep` | 2848917 | LLGo · deadcode drop | 1376096 | -51.7% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1818937 | -36.2% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 1259517 | -55.8% |
| `json-wasi` | 3314587 | LLGo · no LTO | 3465915 | +4.6% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 2121116 | -36.0% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 3089774 | -6.8% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 2025702 | -38.9% |
| `llimport` | 8423078 | LLGo · no LTO | 9902537 | +17.6% |
| `llimport` | 8423078 | LLGo · deadcode drop | 8739929 | +3.8% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 9012263 | +7.0% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 8127847 | -3.5% |
| `path-report` | 2381190 | LLGo · no LTO | 1933333 | -18.8% |
| `path-report` | 2381190 | LLGo · deadcode drop | 1293148 | -45.7% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1688670 | -29.1% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 1163141 | -51.2% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 2687556 | -3.4% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1682815 | -39.5% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 2364056 | -15.0% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1516590 | -45.5% |
| `word-count` | 2253620 | LLGo · no LTO | 1649657 | -26.8% |
| `word-count` | 2253620 | LLGo · deadcode drop | 1024002 | -54.6% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 1414183 | -37.2% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 900098 | -60.1% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 13.289x | 10 |
| LLGo · deadcode drop | 8.292x | 10 |
| LLGo · full LTO (GlobalDCE off) | 11.525x | 10 |
| LLGo · full LTO + GlobalDCE | 7.427x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1530673 | +1481.9% |
| `base64` | 96760 | LLGo · deadcode drop | 927886 | +859.0% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 1313479 | +1257.5% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 816683 | +744.0% |
| `checksum` | 92685 | LLGo · no LTO | 1517380 | +1537.1% |
| `checksum` | 92685 | LLGo · deadcode drop | 909477 | +881.3% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 1295076 | +1297.3% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 797261 | +760.2% |
| `conv-wasi` | 201149 | LLGo · no LTO | 2428196 | +1107.2% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 1441891 | +616.8% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 2129208 | +958.5% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1289220 | +540.9% |
| `fibonacci` | 62386 | LLGo · no LTO | 1346501 | +2058.3% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 850005 | +1262.5% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 1141329 | +1729.5% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 743408 | +1091.6% |
| `glob` | 93153 | LLGo · no LTO | 1682584 | +1706.3% |
| `glob` | 93153 | LLGo · deadcode drop | 1047871 | +1024.9% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1445785 | +1452.1% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 926523 | +894.6% |
| `grep` | 303772 | LLGo · no LTO | 2075764 | +583.3% |
| `grep` | 303772 | LLGo · deadcode drop | 1376096 | +353.0% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1818937 | +498.8% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 1259517 | +314.6% |
| `json-wasi` | 493590 | LLGo · no LTO | 3465915 | +602.2% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 2121116 | +329.7% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 3089774 | +526.0% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 2025702 | +310.4% |
| `llimport` | — | LLGo · no LTO | 9902537 | — |
| `llimport` | — | LLGo · deadcode drop | 8739929 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 9012263 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 8127847 | — |
| `path-report` | 116889 | LLGo · no LTO | 1933333 | +1554.0% |
| `path-report` | 116889 | LLGo · deadcode drop | 1293148 | +1006.3% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1688670 | +1344.7% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 1163141 | +895.1% |
| `sha-wasi` | 287449 | LLGo · no LTO | 2687556 | +835.0% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1682815 | +485.4% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 2364056 | +722.4% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1516590 | +427.6% |
| `word-count` | 86834 | LLGo · no LTO | 1649657 | +1799.8% |
| `word-count` | 86834 | LLGo · deadcode drop | 1024002 | +1079.3% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 1414183 | +1528.6% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 900098 | +936.6% |
