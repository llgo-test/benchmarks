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
| LLGo · no LTO | 1.009x | 11 |
| LLGo · deadcode drop | 0.631x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.900x | 11 |
| LLGo · full LTO + GlobalDCE | 0.585x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1991086 | -14.3% |
| `base64` | 2322402 | LLGo · deadcode drop | 1183857 | -49.0% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1771417 | -23.7% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1089350 | -53.1% |
| `checksum` | 2311672 | LLGo · no LTO | 1971488 | -14.7% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1157174 | -49.9% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1736069 | -24.9% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1055010 | -54.4% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 3084452 | +16.9% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1758161 | -33.4% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2756172 | +4.5% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1616018 | -38.8% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1736240 | -23.7% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 1076517 | -52.7% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1524792 | -33.0% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 987277 | -56.6% |
| `grep` | 2871426 | LLGo · no LTO | 2671671 | -7.0% |
| `grep` | 2871426 | LLGo · deadcode drop | 1714974 | -40.3% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2353356 | -18.0% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1585145 | -44.8% |
| `glob` | 2305059 | LLGo · no LTO | 2127257 | -7.7% |
| `glob` | 2305059 | LLGo · deadcode drop | 1281121 | -44.4% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1877590 | -18.5% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1172709 | -49.1% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4300469 | +28.8% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2567933 | -23.1% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3925288 | +17.6% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2530664 | -24.2% |
| `llimport` | 8440671 | LLGo · no LTO | 11443447 | +35.6% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9799744 | +16.1% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10459952 | +23.9% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 9123065 | +8.1% |
| `path-report` | 2428068 | LLGo · no LTO | 2461837 | +1.4% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1605805 | -33.9% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 2201596 | -9.3% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1487819 | -38.7% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3439981 | +22.4% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 2078532 | -26.1% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 3118026 | +10.9% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1954964 | -30.5% |
| `word-count` | 2300998 | LLGo · no LTO | 2087386 | -9.3% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1254133 | -45.5% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1836613 | -20.2% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1139492 | -50.5% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 12.657x | 10 |
| LLGo · deadcode drop | 7.678x | 10 |
| LLGo · full LTO (GlobalDCE off) | 11.263x | 10 |
| LLGo · full LTO + GlobalDCE | 7.114x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1991086 | +1055.6% |
| `base64` | 172302 | LLGo · deadcode drop | 1183857 | +587.1% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1771417 | +928.1% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1089350 | +532.2% |
| `checksum` | 169609 | LLGo · no LTO | 1971488 | +1062.4% |
| `checksum` | 169609 | LLGo · deadcode drop | 1157174 | +582.3% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1736069 | +923.6% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1055010 | +522.0% |
| `conv-wasi` | 165385 | LLGo · no LTO | 3084452 | +1765.0% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1758161 | +963.1% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2756172 | +1566.5% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1616018 | +877.1% |
| `fibonacci` | 141855 | LLGo · no LTO | 1736240 | +1124.0% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 1076517 | +658.9% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1524792 | +974.9% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 987277 | +596.0% |
| `grep` | 155984 | LLGo · no LTO | 2671671 | +1612.8% |
| `grep` | 155984 | LLGo · deadcode drop | 1714974 | +999.5% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2353356 | +1408.7% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1585145 | +916.2% |
| `glob` | 136553 | LLGo · no LTO | 2127257 | +1457.8% |
| `glob` | 136553 | LLGo · deadcode drop | 1281121 | +838.2% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1877590 | +1275.0% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1172709 | +758.8% |
| `json-wasi` | 525666 | LLGo · no LTO | 4300469 | +718.1% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2567933 | +388.5% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3925288 | +646.7% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2530664 | +381.4% |
| `llimport` | — | LLGo · no LTO | 11443447 | — |
| `llimport` | — | LLGo · deadcode drop | 9799744 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10459952 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 9123065 | — |
| `path-report` | 194133 | LLGo · no LTO | 2461837 | +1168.1% |
| `path-report` | 194133 | LLGo · deadcode drop | 1605805 | +727.2% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 2201596 | +1034.1% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1487819 | +666.4% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3439981 | +877.3% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 2078532 | +490.5% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 3118026 | +785.9% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1954964 | +455.4% |
| `word-count` | 164053 | LLGo · no LTO | 2087386 | +1172.4% |
| `word-count` | 164053 | LLGo · deadcode drop | 1254133 | +664.5% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1836613 | +1019.5% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1139492 | +594.6% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.820x | 11 |
| LLGo · deadcode drop | 0.531x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.714x | 11 |
| LLGo · full LTO + GlobalDCE | 0.477x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1574897 | -30.8% |
| `base64` | 2275731 | LLGo · deadcode drop | 967109 | -57.5% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 1352825 | -40.6% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 850659 | -62.6% |
| `checksum` | 2264417 | LLGo · no LTO | 1561604 | -31.0% |
| `checksum` | 2264417 | LLGo · deadcode drop | 948684 | -58.1% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 1334261 | -41.1% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 831161 | -63.3% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 2456288 | -5.8% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 1465578 | -43.8% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 2152788 | -17.5% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1308725 | -49.8% |
| `fibonacci` | 2230899 | LLGo · no LTO | 1390830 | -37.7% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 889308 | -60.1% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 1180641 | -47.1% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 777409 | -65.2% |
| `grep` | 2848917 | LLGo · no LTO | 2103010 | -26.2% |
| `grep` | 2848917 | LLGo · deadcode drop | 1398097 | -50.9% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1842541 | -35.3% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 1277670 | -55.2% |
| `glob` | 2257634 | LLGo · no LTO | 1720004 | -23.8% |
| `glob` | 2257634 | LLGo · deadcode drop | 1080290 | -52.1% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1478166 | -34.5% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 953585 | -57.8% |
| `json-wasi` | 3314587 | LLGo · no LTO | 3485215 | +5.1% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 2130315 | -35.7% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 3105339 | -6.3% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 2030801 | -38.7% |
| `llimport` | 8423078 | LLGo · no LTO | 9460439 | +12.3% |
| `llimport` | 8423078 | LLGo · deadcode drop | 8298938 | -1.5% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 8573468 | +1.8% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 7686894 | -8.7% |
| `path-report` | 2381190 | LLGo · no LTO | 1970754 | -17.2% |
| `path-report` | 2381190 | LLGo · deadcode drop | 1325543 | -44.3% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1721215 | -27.7% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 1190187 | -50.0% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 2714749 | -2.4% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1705603 | -38.7% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 2386640 | -14.2% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1535044 | -44.8% |
| `word-count` | 2253620 | LLGo · no LTO | 1687109 | -25.1% |
| `word-count` | 2253620 | LLGo · deadcode drop | 1056437 | -53.1% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 1446572 | -35.8% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 927176 | -58.9% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 13.549x | 10 |
| LLGo · deadcode drop | 8.515x | 10 |
| LLGo · full LTO (GlobalDCE off) | 11.753x | 10 |
| LLGo · full LTO + GlobalDCE | 7.617x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1574897 | +1527.6% |
| `base64` | 96760 | LLGo · deadcode drop | 967109 | +899.5% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 1352825 | +1298.1% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 850659 | +779.1% |
| `checksum` | 92685 | LLGo · no LTO | 1561604 | +1584.9% |
| `checksum` | 92685 | LLGo · deadcode drop | 948684 | +923.6% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 1334261 | +1339.6% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 831161 | +796.8% |
| `conv-wasi` | 201149 | LLGo · no LTO | 2456288 | +1121.1% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 1465578 | +628.6% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 2152788 | +970.2% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1308725 | +550.6% |
| `fibonacci` | 62386 | LLGo · no LTO | 1390830 | +2129.4% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 889308 | +1325.5% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 1180641 | +1792.5% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 777409 | +1146.1% |
| `grep` | 303772 | LLGo · no LTO | 2103010 | +592.3% |
| `grep` | 303772 | LLGo · deadcode drop | 1398097 | +360.2% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1842541 | +506.6% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 1277670 | +320.6% |
| `glob` | 93153 | LLGo · no LTO | 1720004 | +1746.4% |
| `glob` | 93153 | LLGo · deadcode drop | 1080290 | +1059.7% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1478166 | +1486.8% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 953585 | +923.7% |
| `json-wasi` | 493590 | LLGo · no LTO | 3485215 | +606.1% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 2130315 | +331.6% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 3105339 | +529.1% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 2030801 | +311.4% |
| `llimport` | — | LLGo · no LTO | 9460439 | — |
| `llimport` | — | LLGo · deadcode drop | 8298938 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 8573468 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 7686894 | — |
| `path-report` | 116889 | LLGo · no LTO | 1970754 | +1586.0% |
| `path-report` | 116889 | LLGo · deadcode drop | 1325543 | +1034.0% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1721215 | +1372.5% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 1190187 | +918.2% |
| `sha-wasi` | 287449 | LLGo · no LTO | 2714749 | +844.4% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1705603 | +493.4% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 2386640 | +730.3% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1535044 | +434.0% |
| `word-count` | 86834 | LLGo · no LTO | 1687109 | +1842.9% |
| `word-count` | 86834 | LLGo · deadcode drop | 1056437 | +1116.6% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 1446572 | +1565.9% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 927176 | +967.8% |
