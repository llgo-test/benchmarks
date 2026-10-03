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
| tsgo | LLGoFullLTONoGlobalDCE | required | timeout | [logs/tsgo.LLGoFullLTONoGlobalDCE.log](logs/tsgo.LLGoFullLTONoGlobalDCE.log) |
| tsgo | LLGoFullLTOGlobalDCE | required | timeout | [logs/tsgo.LLGoFullLTOGlobalDCE.log](logs/tsgo.LLGoFullLTOGlobalDCE.log) |

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
| LLGo · no LTO | 1.125x | 12 |
| LLGo · deadcode drop | 0.715x | 12 |
| LLGo · full LTO (GlobalDCE off) | 0.960x | 11 |
| LLGo · full LTO + GlobalDCE | 0.608x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 2086348 | -10.2% |
| `base64` | 2322402 | LLGo · deadcode drop | 1190333 | -48.7% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1860835 | -19.9% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1097356 | -52.7% |
| `checksum` | 2311672 | LLGo · no LTO | 2066233 | -10.6% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1162256 | -49.7% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1825406 | -21.0% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1061778 | -54.1% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 3293098 | +24.8% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1839714 | -30.3% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2952337 | +11.9% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1694459 | -35.8% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1813019 | -20.3% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 1079192 | -52.5% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1595970 | -29.8% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 991277 | -56.4% |
| `glob` | 2305059 | LLGo · no LTO | 2253304 | -2.2% |
| `glob` | 2305059 | LLGo · deadcode drop | 1316742 | -42.9% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1996876 | -13.4% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1208446 | -47.6% |
| `grep` | 2871426 | LLGo · no LTO | 2826173 | -1.6% |
| `grep` | 2871426 | LLGo · deadcode drop | 1772547 | -38.3% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2500882 | -12.9% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1644668 | -42.7% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4606801 | +38.0% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2716495 | -18.6% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 4209931 | +26.1% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2679197 | -19.7% |
| `llimport` | 8440671 | LLGo · no LTO | 12836571 | +52.1% |
| `llimport` | 8440671 | LLGo · deadcode drop | 11015551 | +30.5% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 11832919 | +40.2% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 10320363 | +22.3% |
| `path-report` | 2428068 | LLGo · no LTO | 2601986 | +7.2% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1655136 | -31.8% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 2332203 | -3.9% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1535200 | -36.8% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3662559 | +30.3% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 2172658 | -22.7% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 3326620 | +18.3% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 2044910 | -27.3% |
| `tsgo` | 50367588 | LLGo · no LTO | 96072004 | +90.7% |
| `tsgo` | 50367588 | LLGo · deadcode drop | 94938211 | +88.5% |
| `tsgo` | 50367588 | LLGo · full LTO (GlobalDCE off) | — | — |
| `tsgo` | 50367588 | LLGo · full LTO + GlobalDCE | — | — |
| `word-count` | 2300998 | LLGo · no LTO | 2212645 | -3.8% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1288978 | -44.0% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1954724 | -15.0% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1174472 | -49.0% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 13.388x | 10 |
| LLGo · deadcode drop | 7.893x | 10 |
| LLGo · full LTO (GlobalDCE off) | 11.948x | 10 |
| LLGo · full LTO + GlobalDCE | 7.328x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 2086348 | +1110.9% |
| `base64` | 172302 | LLGo · deadcode drop | 1190333 | +590.8% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1860835 | +980.0% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1097356 | +536.9% |
| `checksum` | 169609 | LLGo · no LTO | 2066233 | +1118.2% |
| `checksum` | 169609 | LLGo · deadcode drop | 1162256 | +585.3% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1825406 | +976.2% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1061778 | +526.0% |
| `conv-wasi` | 165385 | LLGo · no LTO | 3293098 | +1891.2% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1839714 | +1012.4% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2952337 | +1685.1% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1694459 | +924.6% |
| `fibonacci` | 141855 | LLGo · no LTO | 1813019 | +1178.1% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 1079192 | +660.8% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1595970 | +1025.1% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 991277 | +598.8% |
| `glob` | 136553 | LLGo · no LTO | 2253304 | +1550.1% |
| `glob` | 136553 | LLGo · deadcode drop | 1316742 | +864.3% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1996876 | +1362.3% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1208446 | +785.0% |
| `grep` | 155984 | LLGo · no LTO | 2826173 | +1711.8% |
| `grep` | 155984 | LLGo · deadcode drop | 1772547 | +1036.4% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2500882 | +1503.3% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1644668 | +954.4% |
| `json-wasi` | 525666 | LLGo · no LTO | 4606801 | +776.4% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2716495 | +416.8% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 4209931 | +700.9% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2679197 | +409.7% |
| `llimport` | — | LLGo · no LTO | 12836571 | — |
| `llimport` | — | LLGo · deadcode drop | 11015551 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 11832919 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 10320363 | — |
| `path-report` | 194133 | LLGo · no LTO | 2601986 | +1240.3% |
| `path-report` | 194133 | LLGo · deadcode drop | 1655136 | +752.6% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 2332203 | +1101.3% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1535200 | +690.8% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3662559 | +940.6% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 2172658 | +517.3% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 3326620 | +845.1% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 2044910 | +481.0% |
| `tsgo` | — | LLGo · no LTO | 96072004 | — |
| `tsgo` | — | LLGo · deadcode drop | 94938211 | — |
| `tsgo` | — | LLGo · full LTO (GlobalDCE off) | — | — |
| `tsgo` | — | LLGo · full LTO + GlobalDCE | — | — |
| `word-count` | 164053 | LLGo · no LTO | 2212645 | +1248.7% |
| `word-count` | 164053 | LLGo · deadcode drop | 1288978 | +685.7% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1954724 | +1091.5% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1174472 | +615.9% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.808x | 11 |
| LLGo · deadcode drop | 0.520x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.625x | 11 |
| LLGo · full LTO + GlobalDCE | 0.444x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1528819 | -32.8% |
| `base64` | 2275731 | LLGo · deadcode drop | 926736 | -59.3% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 1166510 | -48.7% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 796468 | -65.0% |
| `checksum` | 2264417 | LLGo · no LTO | 1515526 | -33.1% |
| `checksum` | 2264417 | LLGo · deadcode drop | 908327 | -59.9% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 1147919 | -49.3% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 776988 | -65.7% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 2426167 | -7.0% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 1440653 | -44.8% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1958924 | -24.9% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1255644 | -51.9% |
| `fibonacci` | 2230899 | LLGo · no LTO | 1344691 | -39.7% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 848899 | -61.9% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 999248 | -55.2% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 727439 | -67.4% |
| `glob` | 2257634 | LLGo · no LTO | 1680730 | -25.6% |
| `glob` | 2257634 | LLGo · deadcode drop | 1046721 | -53.6% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1298628 | -42.5% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 906250 | -59.9% |
| `grep` | 2848917 | LLGo · no LTO | 2073845 | -27.2% |
| `grep` | 2848917 | LLGo · deadcode drop | 1374903 | -51.7% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1622591 | -43.0% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 1189418 | -58.3% |
| `json-wasi` | 3314587 | LLGo · no LTO | 3463383 | +4.5% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 2119703 | -36.0% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2803456 | -15.4% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1939462 | -41.5% |
| `llimport` | 8423078 | LLGo · no LTO | 9896758 | +17.5% |
| `llimport` | 8423078 | LLGo · deadcode drop | 8735115 | +3.7% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 6954344 | -17.4% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6142741 | -27.1% |
| `path-report` | 2381190 | LLGo · no LTO | 1931457 | -18.9% |
| `path-report` | 2381190 | LLGo · deadcode drop | 1291976 | -45.7% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1540190 | -35.3% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 1141545 | -52.1% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 2685483 | -3.4% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1681533 | -39.5% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 2173344 | -21.8% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1462338 | -47.4% |
| `word-count` | 2253620 | LLGo · no LTO | 1647803 | -26.9% |
| `word-count` | 2253620 | LLGo · deadcode drop | 1022852 | -54.6% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 1267026 | -43.8% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 879825 | -61.0% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 13.276x | 10 |
| LLGo · deadcode drop | 8.284x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.366x | 10 |
| LLGo · full LTO + GlobalDCE | 7.208x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1528819 | +1480.0% |
| `base64` | 96760 | LLGo · deadcode drop | 926736 | +857.8% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 1166510 | +1105.6% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 796468 | +723.1% |
| `checksum` | 92685 | LLGo · no LTO | 1515526 | +1535.1% |
| `checksum` | 92685 | LLGo · deadcode drop | 908327 | +880.0% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 1147919 | +1138.5% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 776988 | +738.3% |
| `conv-wasi` | 201149 | LLGo · no LTO | 2426167 | +1106.2% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 1440653 | +616.2% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1958924 | +873.9% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1255644 | +524.2% |
| `fibonacci` | 62386 | LLGo · no LTO | 1344691 | +2055.4% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 848899 | +1260.7% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 999248 | +1501.7% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 727439 | +1066.0% |
| `glob` | 93153 | LLGo · no LTO | 1680730 | +1704.3% |
| `glob` | 93153 | LLGo · deadcode drop | 1046721 | +1023.7% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1298628 | +1294.1% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 906250 | +872.9% |
| `grep` | 303772 | LLGo · no LTO | 2073845 | +582.7% |
| `grep` | 303772 | LLGo · deadcode drop | 1374903 | +352.6% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1622591 | +434.1% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 1189418 | +291.5% |
| `json-wasi` | 493590 | LLGo · no LTO | 3463383 | +601.7% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 2119703 | +329.4% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2803456 | +468.0% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1939462 | +292.9% |
| `llimport` | — | LLGo · no LTO | 9896758 | — |
| `llimport` | — | LLGo · deadcode drop | 8735115 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 6954344 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6142741 | — |
| `path-report` | 116889 | LLGo · no LTO | 1931457 | +1552.4% |
| `path-report` | 116889 | LLGo · deadcode drop | 1291976 | +1005.3% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1540190 | +1217.7% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 1141545 | +876.6% |
| `sha-wasi` | 287449 | LLGo · no LTO | 2685483 | +834.2% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1681533 | +485.0% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 2173344 | +656.1% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1462338 | +408.7% |
| `word-count` | 86834 | LLGo · no LTO | 1647803 | +1797.6% |
| `word-count` | 86834 | LLGo · deadcode drop | 1022852 | +1077.9% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 1267026 | +1359.1% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 879825 | +913.2% |
