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
| `grep` | 2871426 | LLGo · no LTO | 2826173 | -1.6% |
| `grep` | 2871426 | LLGo · deadcode drop | 1772547 | -38.3% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2500882 | -12.9% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1644668 | -42.7% |
| `glob` | 2305059 | LLGo · no LTO | 2253304 | -2.2% |
| `glob` | 2305059 | LLGo · deadcode drop | 1316742 | -42.9% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1996876 | -13.4% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1208446 | -47.6% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4606801 | +38.0% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2716495 | -18.6% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 4209931 | +26.1% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2679197 | -19.7% |
| `llimport` | 8440671 | LLGo · no LTO | 12835765 | +52.1% |
| `llimport` | 8440671 | LLGo · deadcode drop | 11014750 | +30.5% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 11832072 | +40.2% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 10319552 | +22.3% |
| `path-report` | 2428068 | LLGo · no LTO | 2601986 | +7.2% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1655136 | -31.8% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 2332203 | -3.9% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1535200 | -36.8% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3662559 | +30.3% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 2172658 | -22.7% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 3326620 | +18.3% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 2044910 | -27.3% |
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
| `grep` | 155984 | LLGo · no LTO | 2826173 | +1711.8% |
| `grep` | 155984 | LLGo · deadcode drop | 1772547 | +1036.4% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2500882 | +1503.3% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1644668 | +954.4% |
| `glob` | 136553 | LLGo · no LTO | 2253304 | +1550.1% |
| `glob` | 136553 | LLGo · deadcode drop | 1316742 | +864.3% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1996876 | +1362.3% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1208446 | +785.0% |
| `json-wasi` | 525666 | LLGo · no LTO | 4606801 | +776.4% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2716495 | +416.8% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 4209931 | +700.9% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2679197 | +409.7% |
| `llimport` | — | LLGo · no LTO | 12835765 | — |
| `llimport` | — | LLGo · deadcode drop | 11014750 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 11832072 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 10319552 | — |
| `path-report` | 194133 | LLGo · no LTO | 2601986 | +1240.3% |
| `path-report` | 194133 | LLGo · deadcode drop | 1655136 | +752.6% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 2332203 | +1101.3% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1535200 | +690.8% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3662559 | +940.6% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 2172658 | +517.3% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 3326620 | +845.1% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 2044910 | +481.0% |
| `word-count` | 164053 | LLGo · no LTO | 2212645 | +1248.7% |
| `word-count` | 164053 | LLGo · deadcode drop | 1288978 | +685.7% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1954724 | +1091.5% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1174472 | +615.9% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.917x | 11 |
| LLGo · deadcode drop | 0.592x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.736x | 11 |
| LLGo · full LTO + GlobalDCE | 0.529x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1683218 | -26.0% |
| `base64` | 2275731 | LLGo · deadcode drop | 1022388 | -55.1% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 1316978 | -42.1% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 922717 | -59.5% |
| `checksum` | 2264417 | LLGo · no LTO | 1660121 | -26.7% |
| `checksum` | 2264417 | LLGo · deadcode drop | 994684 | -56.1% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 1287221 | -43.2% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 890121 | -60.7% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 2812214 | +7.8% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 1644747 | -36.9% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 2361898 | -9.4% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1482897 | -43.1% |
| `fibonacci` | 2230899 | LLGo · no LTO | 1393729 | -37.5% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 919662 | -58.8% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 1122215 | -49.7% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 829546 | -62.8% |
| `grep` | 2848917 | LLGo · no LTO | 2385293 | -16.3% |
| `grep` | 2848917 | LLGo · deadcode drop | 1593125 | -44.1% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1936231 | -32.0% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 1427040 | -49.9% |
| `glob` | 2257634 | LLGo · no LTO | 1851218 | -18.0% |
| `glob` | 2257634 | LLGo · deadcode drop | 1153223 | -48.9% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1479212 | -34.5% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 1041990 | -53.8% |
| `json-wasi` | 3314587 | LLGo · no LTO | 4120299 | +24.3% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 2501670 | -24.5% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 3481689 | +5.0% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 2378495 | -28.2% |
| `llimport` | 8423078 | LLGo · no LTO | 12458692 | +47.9% |
| `llimport` | 8423078 | LLGo · deadcode drop | 10984638 | +30.4% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 8991729 | +6.8% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 8289752 | -1.6% |
| `path-report` | 2381190 | LLGo · no LTO | 2191501 | -8.0% |
| `path-report` | 2381190 | LLGo · deadcode drop | 1484460 | -37.7% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1805574 | -24.2% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 1359294 | -42.9% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 3147661 | +13.2% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1949611 | -29.9% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 2672365 | -3.9% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1778334 | -36.1% |
| `word-count` | 2253620 | LLGo · no LTO | 1811589 | -19.6% |
| `word-count` | 2253620 | LLGo · deadcode drop | 1126638 | -50.0% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 1423478 | -36.8% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 1009418 | -55.2% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 14.910x | 10 |
| LLGo · deadcode drop | 9.335x | 10 |
| LLGo · full LTO (GlobalDCE off) | 12.097x | 10 |
| LLGo · full LTO + GlobalDCE | 8.470x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1683218 | +1639.6% |
| `base64` | 96760 | LLGo · deadcode drop | 1022388 | +956.6% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 1316978 | +1261.1% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 922717 | +853.6% |
| `checksum` | 92685 | LLGo · no LTO | 1660121 | +1691.1% |
| `checksum` | 92685 | LLGo · deadcode drop | 994684 | +973.2% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 1287221 | +1288.8% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 890121 | +860.4% |
| `conv-wasi` | 201149 | LLGo · no LTO | 2812214 | +1298.1% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 1644747 | +717.7% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 2361898 | +1074.2% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1482897 | +637.2% |
| `fibonacci` | 62386 | LLGo · no LTO | 1393729 | +2134.0% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 919662 | +1374.1% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 1122215 | +1698.8% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 829546 | +1229.7% |
| `grep` | 303772 | LLGo · no LTO | 2385293 | +685.2% |
| `grep` | 303772 | LLGo · deadcode drop | 1593125 | +424.4% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1936231 | +537.4% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 1427040 | +369.8% |
| `glob` | 93153 | LLGo · no LTO | 1851218 | +1887.3% |
| `glob` | 93153 | LLGo · deadcode drop | 1153223 | +1138.0% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1479212 | +1487.9% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 1041990 | +1018.6% |
| `json-wasi` | 493590 | LLGo · no LTO | 4120299 | +734.8% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 2501670 | +406.8% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 3481689 | +605.4% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 2378495 | +381.9% |
| `llimport` | — | LLGo · no LTO | 12458692 | — |
| `llimport` | — | LLGo · deadcode drop | 10984638 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 8991729 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 8289752 | — |
| `path-report` | 116889 | LLGo · no LTO | 2191501 | +1774.9% |
| `path-report` | 116889 | LLGo · deadcode drop | 1484460 | +1170.0% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1805574 | +1444.7% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 1359294 | +1062.9% |
| `sha-wasi` | 287449 | LLGo · no LTO | 3147661 | +995.0% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1949611 | +578.2% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 2672365 | +829.7% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1778334 | +518.7% |
| `word-count` | 86834 | LLGo · no LTO | 1811589 | +1986.3% |
| `word-count` | 86834 | LLGo · deadcode drop | 1126638 | +1197.5% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 1423478 | +1539.3% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 1009418 | +1062.5% |
