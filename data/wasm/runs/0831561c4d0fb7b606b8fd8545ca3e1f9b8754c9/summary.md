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
| LLGo · no LTO | 1.030x | 12 |
| LLGo · deadcode drop | 0.667x | 12 |
| LLGo · full LTO (GlobalDCE off) | 0.925x | 12 |
| LLGo · full LTO + GlobalDCE | 0.621x | 12 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1959462 | -15.6% |
| `base64` | 2322402 | LLGo · deadcode drop | 1156415 | -50.2% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1741143 | -25.0% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1063304 | -54.2% |
| `checksum` | 2311672 | LLGo · no LTO | 1939885 | -16.1% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1129729 | -51.1% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1706253 | -26.2% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1029277 | -55.5% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 3074614 | +16.5% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1751714 | -33.6% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2746195 | +4.1% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1609295 | -39.0% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1704607 | -25.1% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 1049147 | -53.9% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1494944 | -34.3% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 961556 | -57.7% |
| `glob` | 2305059 | LLGo · no LTO | 2095618 | -9.1% |
| `glob` | 2305059 | LLGo · deadcode drop | 1253757 | -45.6% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1847770 | -19.8% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1146983 | -50.2% |
| `grep` | 2871426 | LLGo · no LTO | 2642827 | -8.0% |
| `grep` | 2871426 | LLGo · deadcode drop | 1689992 | -41.1% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2326211 | -19.0% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1561577 | -45.6% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4282919 | +28.3% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2560253 | -23.3% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3907234 | +17.0% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2522933 | -24.4% |
| `llimport` | 8440671 | LLGo · no LTO | 11423724 | +35.3% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9782481 | +15.9% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10447202 | +23.8% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 9104524 | +7.9% |
| `path-report` | 2428068 | LLGo · no LTO | 2430187 | +0.1% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1578401 | -35.0% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 2171753 | -10.6% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1462072 | -39.8% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3430052 | +22.0% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 2071965 | -26.3% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 3107865 | +10.6% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1948300 | -30.7% |
| `tsgo` | 50367588 | LLGo · no LTO | 73147140 | +45.2% |
| `tsgo` | 50367588 | LLGo · deadcode drop | 72135222 | +43.2% |
| `tsgo` | 50367588 | LLGo · full LTO (GlobalDCE off) | 71545513 | +42.0% |
| `tsgo` | 50367588 | LLGo · full LTO + GlobalDCE | 71218615 | +41.4% |
| `word-count` | 2300998 | LLGo · no LTO | 2055719 | -10.7% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1226788 | -46.7% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1806763 | -21.5% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1113762 | -51.6% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 12.513x | 10 |
| LLGo · deadcode drop | 7.557x | 10 |
| LLGo · full LTO (GlobalDCE off) | 11.125x | 10 |
| LLGo · full LTO + GlobalDCE | 6.999x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1959462 | +1037.2% |
| `base64` | 172302 | LLGo · deadcode drop | 1156415 | +571.2% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1741143 | +910.5% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1063304 | +517.1% |
| `checksum` | 169609 | LLGo · no LTO | 1939885 | +1043.7% |
| `checksum` | 169609 | LLGo · deadcode drop | 1129729 | +566.1% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1706253 | +906.0% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1029277 | +506.9% |
| `conv-wasi` | 165385 | LLGo · no LTO | 3074614 | +1759.1% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1751714 | +959.2% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2746195 | +1560.5% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1609295 | +873.1% |
| `fibonacci` | 141855 | LLGo · no LTO | 1704607 | +1101.7% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 1049147 | +639.6% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1494944 | +953.9% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 961556 | +577.8% |
| `glob` | 136553 | LLGo · no LTO | 2095618 | +1434.7% |
| `glob` | 136553 | LLGo · deadcode drop | 1253757 | +818.1% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1847770 | +1253.2% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1146983 | +740.0% |
| `grep` | 155984 | LLGo · no LTO | 2642827 | +1594.3% |
| `grep` | 155984 | LLGo · deadcode drop | 1689992 | +983.4% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2326211 | +1391.3% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1561577 | +901.1% |
| `json-wasi` | 525666 | LLGo · no LTO | 4282919 | +714.8% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2560253 | +387.0% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3907234 | +643.3% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2522933 | +379.9% |
| `llimport` | — | LLGo · no LTO | 11423724 | — |
| `llimport` | — | LLGo · deadcode drop | 9782481 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10447202 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 9104524 | — |
| `path-report` | 194133 | LLGo · no LTO | 2430187 | +1151.8% |
| `path-report` | 194133 | LLGo · deadcode drop | 1578401 | +713.1% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 2171753 | +1018.7% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1462072 | +653.1% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3430052 | +874.5% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 2071965 | +488.7% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 3107865 | +783.0% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1948300 | +453.5% |
| `tsgo` | — | LLGo · no LTO | 73147140 | — |
| `tsgo` | — | LLGo · deadcode drop | 72135222 | — |
| `tsgo` | — | LLGo · full LTO (GlobalDCE off) | 71545513 | — |
| `tsgo` | — | LLGo · full LTO + GlobalDCE | 71218615 | — |
| `word-count` | 164053 | LLGo · no LTO | 2055719 | +1153.1% |
| `word-count` | 164053 | LLGo · deadcode drop | 1226788 | +647.8% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1806763 | +1001.3% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1113762 | +578.9% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.804x | 11 |
| LLGo · deadcode drop | 0.517x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.698x | 11 |
| LLGo · full LTO + GlobalDCE | 0.463x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1531481 | -32.7% |
| `base64` | 2275731 | LLGo · deadcode drop | 929707 | -59.1% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 1311940 | -42.4% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 816222 | -64.1% |
| `checksum` | 2264417 | LLGo · no LTO | 1518188 | -33.0% |
| `checksum` | 2264417 | LLGo · deadcode drop | 911282 | -59.8% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 1293539 | -42.9% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 796802 | -64.8% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 2421731 | -7.1% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 1433667 | -45.0% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 2119173 | -18.7% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1278740 | -51.0% |
| `fibonacci` | 2230899 | LLGo · no LTO | 1347422 | -39.6% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 851906 | -61.8% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 1139927 | -48.9% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 743084 | -66.7% |
| `glob` | 2257634 | LLGo · no LTO | 1676572 | -25.7% |
| `glob` | 2257634 | LLGo · deadcode drop | 1042856 | -53.8% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1437428 | -36.3% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 919244 | -59.3% |
| `grep` | 2848917 | LLGo · no LTO | 2065662 | -27.5% |
| `grep` | 2848917 | LLGo · deadcode drop | 1366974 | -52.0% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1806463 | -36.6% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 1248129 | -56.2% |
| `json-wasi` | 3314587 | LLGo · no LTO | 3447751 | +4.0% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 2100940 | -36.6% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 3068706 | -7.4% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 2003224 | -39.6% |
| `llimport` | 8423078 | LLGo · no LTO | 9418122 | +11.8% |
| `llimport` | 8423078 | LLGo · deadcode drop | 8257582 | -2.0% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 8538346 | +1.4% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 7646543 | -9.2% |
| `path-report` | 2381190 | LLGo · no LTO | 1927330 | -19.1% |
| `path-report` | 2381190 | LLGo · deadcode drop | 1288125 | -45.9% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1680313 | -29.4% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 1155854 | -51.5% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 2680160 | -3.6% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1673660 | -39.8% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 2352885 | -15.4% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1504981 | -45.9% |
| `word-count` | 2253620 | LLGo · no LTO | 1643669 | -27.1% |
| `word-count` | 2253620 | LLGo · deadcode drop | 1018995 | -54.8% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 1405826 | -37.6% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 892827 | -60.4% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 13.257x | 10 |
| LLGo · deadcode drop | 8.263x | 10 |
| LLGo · full LTO (GlobalDCE off) | 11.475x | 10 |
| LLGo · full LTO + GlobalDCE | 7.383x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1531481 | +1482.8% |
| `base64` | 96760 | LLGo · deadcode drop | 929707 | +860.8% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 1311940 | +1255.9% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 816222 | +743.6% |
| `checksum` | 92685 | LLGo · no LTO | 1518188 | +1538.0% |
| `checksum` | 92685 | LLGo · deadcode drop | 911282 | +883.2% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 1293539 | +1295.6% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 796802 | +759.7% |
| `conv-wasi` | 201149 | LLGo · no LTO | 2421731 | +1103.9% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 1433667 | +612.7% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 2119173 | +953.5% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1278740 | +535.7% |
| `fibonacci` | 62386 | LLGo · no LTO | 1347422 | +2059.8% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 851906 | +1265.5% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 1139927 | +1727.2% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 743084 | +1091.1% |
| `glob` | 93153 | LLGo · no LTO | 1676572 | +1699.8% |
| `glob` | 93153 | LLGo · deadcode drop | 1042856 | +1019.5% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1437428 | +1443.1% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 919244 | +886.8% |
| `grep` | 303772 | LLGo · no LTO | 2065662 | +580.0% |
| `grep` | 303772 | LLGo · deadcode drop | 1366974 | +350.0% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1806463 | +494.7% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 1248129 | +310.9% |
| `json-wasi` | 493590 | LLGo · no LTO | 3447751 | +598.5% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 2100940 | +325.6% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 3068706 | +521.7% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 2003224 | +305.8% |
| `llimport` | — | LLGo · no LTO | 9418122 | — |
| `llimport` | — | LLGo · deadcode drop | 8257582 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 8538346 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 7646543 | — |
| `path-report` | 116889 | LLGo · no LTO | 1927330 | +1548.9% |
| `path-report` | 116889 | LLGo · deadcode drop | 1288125 | +1002.0% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1680313 | +1337.5% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 1155854 | +888.8% |
| `sha-wasi` | 287449 | LLGo · no LTO | 2680160 | +832.4% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1673660 | +482.2% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 2352885 | +718.5% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1504981 | +423.6% |
| `word-count` | 86834 | LLGo · no LTO | 1643669 | +1792.9% |
| `word-count` | 86834 | LLGo · deadcode drop | 1018995 | +1073.5% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 1405826 | +1519.0% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 892827 | +928.2% |
