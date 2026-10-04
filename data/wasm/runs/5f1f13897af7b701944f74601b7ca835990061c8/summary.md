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
| LLGo · no LTO | 1.073x | 11 |
| LLGo · deadcode drop | 0.654x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.960x | 11 |
| LLGo · full LTO + GlobalDCE | 0.608x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 2086490 | -10.2% |
| `base64` | 2322402 | LLGo · deadcode drop | 1190477 | -48.7% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1860933 | -19.9% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1097470 | -52.7% |
| `checksum` | 2311672 | LLGo · no LTO | 2066377 | -10.6% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1162388 | -49.7% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1825512 | -21.0% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1061886 | -54.1% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 3293219 | +24.8% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1839851 | -30.3% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2952407 | +11.9% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1694568 | -35.8% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1813166 | -20.3% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 1079348 | -52.5% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1596080 | -29.8% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 991401 | -56.4% |
| `grep` | 2871426 | LLGo · no LTO | 2826316 | -1.6% |
| `grep` | 2871426 | LLGo · deadcode drop | 1772725 | -38.3% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2501004 | -12.9% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1644787 | -42.7% |
| `glob` | 2305059 | LLGo · no LTO | 2253442 | -2.2% |
| `glob` | 2305059 | LLGo · deadcode drop | 1316893 | -42.9% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1996980 | -13.4% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1208543 | -47.6% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4606949 | +38.0% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2716637 | -18.6% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 4210035 | +26.1% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2679334 | -19.7% |
| `llimport` | 8440671 | LLGo · no LTO | 12836732 | +52.1% |
| `llimport` | 8440671 | LLGo · deadcode drop | 11015657 | +30.5% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 11833074 | +40.2% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 10320452 | +22.3% |
| `path-report` | 2428068 | LLGo · no LTO | 2602124 | +7.2% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1655273 | -31.8% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 2332311 | -3.9% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1535320 | -36.8% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3662685 | +30.3% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 2172805 | -22.7% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 3326748 | +18.3% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 2045011 | -27.3% |
| `word-count` | 2300998 | LLGo · no LTO | 2212772 | -3.8% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1289110 | -44.0% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1954842 | -15.0% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1174580 | -49.0% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 13.389x | 10 |
| LLGo · deadcode drop | 7.893x | 10 |
| LLGo · full LTO (GlobalDCE off) | 11.949x | 10 |
| LLGo · full LTO + GlobalDCE | 7.329x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 2086490 | +1110.9% |
| `base64` | 172302 | LLGo · deadcode drop | 1190477 | +590.9% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1860933 | +980.0% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1097470 | +536.9% |
| `checksum` | 169609 | LLGo · no LTO | 2066377 | +1118.3% |
| `checksum` | 169609 | LLGo · deadcode drop | 1162388 | +585.3% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1825512 | +976.3% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1061886 | +526.1% |
| `conv-wasi` | 165385 | LLGo · no LTO | 3293219 | +1891.2% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1839851 | +1012.5% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2952407 | +1685.2% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1694568 | +924.6% |
| `fibonacci` | 141855 | LLGo · no LTO | 1813166 | +1178.2% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 1079348 | +660.9% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1596080 | +1025.1% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 991401 | +598.9% |
| `grep` | 155984 | LLGo · no LTO | 2826316 | +1711.9% |
| `grep` | 155984 | LLGo · deadcode drop | 1772725 | +1036.5% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2501004 | +1503.4% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1644787 | +954.5% |
| `glob` | 136553 | LLGo · no LTO | 2253442 | +1550.2% |
| `glob` | 136553 | LLGo · deadcode drop | 1316893 | +864.4% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1996980 | +1362.4% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1208543 | +785.0% |
| `json-wasi` | 525666 | LLGo · no LTO | 4606949 | +776.4% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2716637 | +416.8% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 4210035 | +700.9% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2679334 | +409.7% |
| `llimport` | — | LLGo · no LTO | 12836732 | — |
| `llimport` | — | LLGo · deadcode drop | 11015657 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 11833074 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 10320452 | — |
| `path-report` | 194133 | LLGo · no LTO | 2602124 | +1240.4% |
| `path-report` | 194133 | LLGo · deadcode drop | 1655273 | +752.6% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 2332311 | +1101.4% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1535320 | +690.9% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3662685 | +940.6% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 2172805 | +517.3% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 3326748 | +845.2% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 2045011 | +481.0% |
| `word-count` | 164053 | LLGo · no LTO | 2212772 | +1248.8% |
| `word-count` | 164053 | LLGo · deadcode drop | 1289110 | +685.8% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1954842 | +1091.6% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1174580 | +616.0% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.808x | 11 |
| LLGo · deadcode drop | 0.520x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.625x | 11 |
| LLGo · full LTO + GlobalDCE | 0.444x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1528947 | -32.8% |
| `base64` | 2275731 | LLGo · deadcode drop | 926880 | -59.3% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 1166614 | -48.7% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 796572 | -65.0% |
| `checksum` | 2264417 | LLGo · no LTO | 1515654 | -33.1% |
| `checksum` | 2264417 | LLGo · deadcode drop | 908455 | -59.9% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 1148023 | -49.3% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 777092 | -65.7% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 2426295 | -7.0% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 1440797 | -44.8% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1959028 | -24.9% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1255748 | -51.9% |
| `fibonacci` | 2230899 | LLGo · no LTO | 1344835 | -39.7% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 849043 | -61.9% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 999352 | -55.2% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 727543 | -67.4% |
| `grep` | 2848917 | LLGo · no LTO | 2073989 | -27.2% |
| `grep` | 2848917 | LLGo · deadcode drop | 1375047 | -51.7% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1622695 | -43.0% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 1189522 | -58.2% |
| `glob` | 2257634 | LLGo · no LTO | 1680858 | -25.5% |
| `glob` | 2257634 | LLGo · deadcode drop | 1046865 | -53.6% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1298732 | -42.5% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 906354 | -59.9% |
| `json-wasi` | 3314587 | LLGo · no LTO | 3463527 | +4.5% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 2119847 | -36.0% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2803560 | -15.4% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1939566 | -41.5% |
| `llimport` | 8423078 | LLGo · no LTO | 9896902 | +17.5% |
| `llimport` | 8423078 | LLGo · deadcode drop | 8735259 | +3.7% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 6954448 | -17.4% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6142845 | -27.1% |
| `path-report` | 2381190 | LLGo · no LTO | 1931585 | -18.9% |
| `path-report` | 2381190 | LLGo · deadcode drop | 1292104 | -45.7% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1540302 | -35.3% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 1141657 | -52.1% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 2685611 | -3.4% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1681677 | -39.5% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 2173448 | -21.8% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1462450 | -47.4% |
| `word-count` | 2253620 | LLGo · no LTO | 1647947 | -26.9% |
| `word-count` | 2253620 | LLGo · deadcode drop | 1022996 | -54.6% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 1267138 | -43.8% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 879937 | -61.0% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 13.277x | 10 |
| LLGo · deadcode drop | 8.285x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.366x | 10 |
| LLGo · full LTO + GlobalDCE | 7.209x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1528947 | +1480.1% |
| `base64` | 96760 | LLGo · deadcode drop | 926880 | +857.9% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 1166614 | +1105.7% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 796572 | +723.2% |
| `checksum` | 92685 | LLGo · no LTO | 1515654 | +1535.3% |
| `checksum` | 92685 | LLGo · deadcode drop | 908455 | +880.2% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 1148023 | +1138.6% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 777092 | +738.4% |
| `conv-wasi` | 201149 | LLGo · no LTO | 2426295 | +1106.2% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 1440797 | +616.3% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1959028 | +873.9% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1255748 | +524.3% |
| `fibonacci` | 62386 | LLGo · no LTO | 1344835 | +2055.7% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 849043 | +1261.0% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 999352 | +1501.9% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 727543 | +1066.2% |
| `grep` | 303772 | LLGo · no LTO | 2073989 | +582.7% |
| `grep` | 303772 | LLGo · deadcode drop | 1375047 | +352.7% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1622695 | +434.2% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 1189522 | +291.6% |
| `glob` | 93153 | LLGo · no LTO | 1680858 | +1704.4% |
| `glob` | 93153 | LLGo · deadcode drop | 1046865 | +1023.8% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1298732 | +1294.2% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 906354 | +873.0% |
| `json-wasi` | 493590 | LLGo · no LTO | 3463527 | +601.7% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 2119847 | +329.5% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2803560 | +468.0% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1939566 | +293.0% |
| `llimport` | — | LLGo · no LTO | 9896902 | — |
| `llimport` | — | LLGo · deadcode drop | 8735259 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 6954448 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6142845 | — |
| `path-report` | 116889 | LLGo · no LTO | 1931585 | +1552.5% |
| `path-report` | 116889 | LLGo · deadcode drop | 1292104 | +1005.4% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1540302 | +1217.7% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 1141657 | +876.7% |
| `sha-wasi` | 287449 | LLGo · no LTO | 2685611 | +834.3% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1681677 | +485.0% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 2173448 | +656.1% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1462450 | +408.8% |
| `word-count` | 86834 | LLGo · no LTO | 1647947 | +1797.8% |
| `word-count` | 86834 | LLGo · deadcode drop | 1022996 | +1078.1% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 1267138 | +1359.3% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 879937 | +913.4% |
