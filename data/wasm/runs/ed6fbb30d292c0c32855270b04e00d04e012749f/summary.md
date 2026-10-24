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
| LLGo · deadcode drop | 0.632x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.900x | 11 |
| LLGo · full LTO + GlobalDCE | 0.586x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1992089 | -14.2% |
| `base64` | 2322402 | LLGo · deadcode drop | 1184564 | -49.0% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1772186 | -23.7% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1090036 | -53.1% |
| `checksum` | 2311672 | LLGo · no LTO | 1972503 | -14.7% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1157894 | -49.9% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1736839 | -24.9% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1055660 | -54.3% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 3084020 | +16.9% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1759174 | -33.3% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2756938 | +4.5% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1616761 | -38.7% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1737248 | -23.6% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 1077236 | -52.6% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1525551 | -32.9% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 987939 | -56.6% |
| `grep` | 2871426 | LLGo · no LTO | 2671523 | -7.0% |
| `grep` | 2871426 | LLGo · deadcode drop | 1715403 | -40.3% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2352772 | -18.1% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1584872 | -44.8% |
| `glob` | 2305059 | LLGo · no LTO | 2128249 | -7.7% |
| `glob` | 2305059 | LLGo · deadcode drop | 1281820 | -44.4% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1878364 | -18.5% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1173376 | -49.1% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4299656 | +28.8% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2568917 | -23.0% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3926051 | +17.6% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2531426 | -24.2% |
| `llimport` | 8440671 | LLGo · no LTO | 11441981 | +35.6% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9798652 | +16.1% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10458205 | +23.9% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 9121683 | +8.1% |
| `path-report` | 2428068 | LLGo · no LTO | 2462815 | +1.4% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1606769 | -33.8% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 2202349 | -9.3% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1488513 | -38.7% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3439543 | +22.4% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 2079556 | -26.0% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 3118803 | +10.9% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1955739 | -30.4% |
| `word-count` | 2300998 | LLGo · no LTO | 2088392 | -9.2% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1255172 | -45.5% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1837360 | -20.1% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1140149 | -50.4% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 12.660x | 10 |
| LLGo · deadcode drop | 7.682x | 10 |
| LLGo · full LTO (GlobalDCE off) | 11.266x | 10 |
| LLGo · full LTO + GlobalDCE | 7.118x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1992089 | +1056.2% |
| `base64` | 172302 | LLGo · deadcode drop | 1184564 | +587.5% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1772186 | +928.5% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1090036 | +532.6% |
| `checksum` | 169609 | LLGo · no LTO | 1972503 | +1063.0% |
| `checksum` | 169609 | LLGo · deadcode drop | 1157894 | +582.7% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1736839 | +924.0% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1055660 | +522.4% |
| `conv-wasi` | 165385 | LLGo · no LTO | 3084020 | +1764.8% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1759174 | +963.7% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2756938 | +1567.0% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1616761 | +877.6% |
| `fibonacci` | 141855 | LLGo · no LTO | 1737248 | +1124.7% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 1077236 | +659.4% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1525551 | +975.4% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 987939 | +596.4% |
| `grep` | 155984 | LLGo · no LTO | 2671523 | +1612.7% |
| `grep` | 155984 | LLGo · deadcode drop | 1715403 | +999.7% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2352772 | +1408.3% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1584872 | +916.0% |
| `glob` | 136553 | LLGo · no LTO | 2128249 | +1458.6% |
| `glob` | 136553 | LLGo · deadcode drop | 1281820 | +838.7% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1878364 | +1275.6% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1173376 | +759.3% |
| `json-wasi` | 525666 | LLGo · no LTO | 4299656 | +717.9% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2568917 | +388.7% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3926051 | +646.9% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2531426 | +381.6% |
| `llimport` | — | LLGo · no LTO | 11441981 | — |
| `llimport` | — | LLGo · deadcode drop | 9798652 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10458205 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 9121683 | — |
| `path-report` | 194133 | LLGo · no LTO | 2462815 | +1168.6% |
| `path-report` | 194133 | LLGo · deadcode drop | 1606769 | +727.7% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 2202349 | +1034.5% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1488513 | +666.7% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3439543 | +877.2% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 2079556 | +490.8% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 3118803 | +786.1% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1955739 | +455.7% |
| `word-count` | 164053 | LLGo · no LTO | 2088392 | +1173.0% |
| `word-count` | 164053 | LLGo · deadcode drop | 1255172 | +665.1% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1837360 | +1020.0% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1140149 | +595.0% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.820x | 11 |
| LLGo · deadcode drop | 0.531x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.714x | 11 |
| LLGo · full LTO + GlobalDCE | 0.477x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1575057 | -30.8% |
| `base64` | 2275731 | LLGo · deadcode drop | 967609 | -57.5% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 1353516 | -40.5% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 851335 | -62.6% |
| `checksum` | 2264417 | LLGo · no LTO | 1561764 | -31.0% |
| `checksum` | 2264417 | LLGo · deadcode drop | 949200 | -58.1% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 1334944 | -41.0% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 831829 | -63.3% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 2456168 | -5.8% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 1466382 | -43.8% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 2153553 | -17.4% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1309416 | -49.8% |
| `fibonacci` | 2230899 | LLGo · no LTO | 1390970 | -37.6% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 889800 | -60.1% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 1181332 | -47.0% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 778085 | -65.1% |
| `grep` | 2848917 | LLGo · no LTO | 2103276 | -26.2% |
| `grep` | 2848917 | LLGo · deadcode drop | 1398657 | -50.9% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1842225 | -35.3% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 1277724 | -55.2% |
| `glob` | 2257634 | LLGo · no LTO | 1720112 | -23.8% |
| `glob` | 2257634 | LLGo · deadcode drop | 1080754 | -52.1% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1478849 | -34.5% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 954253 | -57.7% |
| `json-wasi` | 3314587 | LLGo · no LTO | 3484787 | +5.1% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 2130831 | -35.7% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 3106104 | -6.3% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 2031492 | -38.7% |
| `llimport` | 8423078 | LLGo · no LTO | 9459317 | +12.3% |
| `llimport` | 8423078 | LLGo · deadcode drop | 8298180 | -1.5% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 8572057 | +1.8% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 7685741 | -8.8% |
| `path-report` | 2381190 | LLGo · no LTO | 1970762 | -17.2% |
| `path-report` | 2381190 | LLGo · deadcode drop | 1326287 | -44.3% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1721898 | -27.7% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 1190852 | -50.0% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 2714625 | -2.4% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1706403 | -38.6% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 2387405 | -14.2% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1535727 | -44.8% |
| `word-count` | 2253620 | LLGo · no LTO | 1687253 | -25.1% |
| `word-count` | 2253620 | LLGo · deadcode drop | 1057289 | -53.1% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 1447255 | -35.8% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 927844 | -58.8% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 13.549x | 10 |
| LLGo · deadcode drop | 8.519x | 10 |
| LLGo · full LTO (GlobalDCE off) | 11.757x | 10 |
| LLGo · full LTO + GlobalDCE | 7.621x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1575057 | +1527.8% |
| `base64` | 96760 | LLGo · deadcode drop | 967609 | +900.0% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 1353516 | +1298.8% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 851335 | +779.8% |
| `checksum` | 92685 | LLGo · no LTO | 1561764 | +1585.0% |
| `checksum` | 92685 | LLGo · deadcode drop | 949200 | +924.1% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 1334944 | +1340.3% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 831829 | +797.5% |
| `conv-wasi` | 201149 | LLGo · no LTO | 2456168 | +1121.1% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 1466382 | +629.0% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 2153553 | +970.6% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1309416 | +551.0% |
| `fibonacci` | 62386 | LLGo · no LTO | 1390970 | +2129.6% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 889800 | +1326.3% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 1181332 | +1793.6% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 778085 | +1147.2% |
| `grep` | 303772 | LLGo · no LTO | 2103276 | +592.4% |
| `grep` | 303772 | LLGo · deadcode drop | 1398657 | +360.4% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1842225 | +506.4% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 1277724 | +320.6% |
| `glob` | 93153 | LLGo · no LTO | 1720112 | +1746.5% |
| `glob` | 93153 | LLGo · deadcode drop | 1080754 | +1060.2% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1478849 | +1487.5% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 954253 | +924.4% |
| `json-wasi` | 493590 | LLGo · no LTO | 3484787 | +606.0% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 2130831 | +331.7% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 3106104 | +529.3% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 2031492 | +311.6% |
| `llimport` | — | LLGo · no LTO | 9459317 | — |
| `llimport` | — | LLGo · deadcode drop | 8298180 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 8572057 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 7685741 | — |
| `path-report` | 116889 | LLGo · no LTO | 1970762 | +1586.0% |
| `path-report` | 116889 | LLGo · deadcode drop | 1326287 | +1034.7% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1721898 | +1373.1% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 1190852 | +918.8% |
| `sha-wasi` | 287449 | LLGo · no LTO | 2714625 | +844.4% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1706403 | +493.6% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 2387405 | +730.5% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1535727 | +434.3% |
| `word-count` | 86834 | LLGo · no LTO | 1687253 | +1843.1% |
| `word-count` | 86834 | LLGo · deadcode drop | 1057289 | +1117.6% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 1447255 | +1566.7% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 927844 | +968.5% |
