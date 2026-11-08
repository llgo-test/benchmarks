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
| LLGo · no LTO | 0.924x | 11 |
| LLGo · deadcode drop | 0.526x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.833x | 11 |
| LLGo · full LTO + GlobalDCE | 0.566x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1884454 | -18.9% |
| `base64` | 2322402 | LLGo · deadcode drop | 1016159 | -56.2% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1653121 | -28.8% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1061175 | -54.3% |
| `checksum` | 2311672 | LLGo · no LTO | 1864272 | -19.4% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1001831 | -56.7% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1616755 | -30.1% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1028264 | -55.5% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2726870 | +3.3% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1463528 | -44.5% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2494979 | -5.4% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1579172 | -40.1% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1665526 | -26.8% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 894666 | -60.7% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1436742 | -36.8% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 973626 | -57.2% |
| `grep` | 2871426 | LLGo · no LTO | 2535489 | -11.7% |
| `grep` | 2871426 | LLGo · deadcode drop | 1509112 | -47.4% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2220806 | -22.7% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1556676 | -45.8% |
| `glob` | 2305059 | LLGo · no LTO | 1914344 | -17.0% |
| `glob` | 2305059 | LLGo · deadcode drop | 1022691 | -55.6% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1755165 | -23.9% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1149998 | -50.1% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4011286 | +20.2% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2172164 | -34.9% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3732989 | +11.8% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2493119 | -25.3% |
| `llimport` | 8440671 | LLGo · no LTO | 10902277 | +29.2% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9020999 | +6.9% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 9956907 | +18.0% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 8887405 | +5.3% |
| `path-report` | 2428068 | LLGo · no LTO | 2052897 | -15.5% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1145882 | -52.8% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 1883648 | -22.4% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1279297 | -47.3% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3042996 | +8.2% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1736146 | -38.2% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2810908 | -0.0% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1889283 | -32.8% |
| `word-count` | 2300998 | LLGo · no LTO | 1874571 | -18.5% |
| `word-count` | 2300998 | LLGo · deadcode drop | 998235 | -56.6% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1714388 | -25.5% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1118023 | -51.4% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.551x | 10 |
| LLGo · deadcode drop | 6.329x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.393x | 10 |
| LLGo · full LTO + GlobalDCE | 6.873x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1884454 | +993.7% |
| `base64` | 172302 | LLGo · deadcode drop | 1016159 | +489.8% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1653121 | +859.4% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1061175 | +515.9% |
| `checksum` | 169609 | LLGo · no LTO | 1864272 | +999.2% |
| `checksum` | 169609 | LLGo · deadcode drop | 1001831 | +490.7% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1616755 | +853.2% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1028264 | +506.3% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2726870 | +1548.8% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1463528 | +784.9% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2494979 | +1408.6% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1579172 | +854.8% |
| `fibonacci` | 141855 | LLGo · no LTO | 1665526 | +1074.1% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 894666 | +530.7% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1436742 | +912.8% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 973626 | +586.4% |
| `grep` | 155984 | LLGo · no LTO | 2535489 | +1525.5% |
| `grep` | 155984 | LLGo · deadcode drop | 1509112 | +867.5% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2220806 | +1323.7% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1556676 | +898.0% |
| `glob` | 136553 | LLGo · no LTO | 1914344 | +1301.9% |
| `glob` | 136553 | LLGo · deadcode drop | 1022691 | +648.9% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1755165 | +1185.3% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1149998 | +742.2% |
| `json-wasi` | 525666 | LLGo · no LTO | 4011286 | +663.1% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2172164 | +313.2% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3732989 | +610.1% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2493119 | +374.3% |
| `llimport` | — | LLGo · no LTO | 10902277 | — |
| `llimport` | — | LLGo · deadcode drop | 9020999 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 9956907 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 8887405 | — |
| `path-report` | 194133 | LLGo · no LTO | 2052897 | +957.5% |
| `path-report` | 194133 | LLGo · deadcode drop | 1145882 | +490.3% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 1883648 | +870.3% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1279297 | +559.0% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3042996 | +764.6% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1736146 | +393.3% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2810908 | +698.6% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1889283 | +436.8% |
| `word-count` | 164053 | LLGo · no LTO | 1874571 | +1042.7% |
| `word-count` | 164053 | LLGo · deadcode drop | 998235 | +508.5% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1714388 | +945.0% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1118023 | +581.5% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.560x | 11 |
| LLGo · deadcode drop | 0.283x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.484x | 11 |
| LLGo · full LTO + GlobalDCE | 0.339x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1074814 | -52.8% |
| `base64` | 2275731 | LLGo · deadcode drop | 498616 | -78.1% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 837095 | -63.2% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 567084 | -75.1% |
| `checksum` | 2264417 | LLGo · no LTO | 1058727 | -53.2% |
| `checksum` | 2264417 | LLGo · deadcode drop | 485699 | -78.6% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 821339 | -63.7% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 548890 | -75.8% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 1657877 | -36.4% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 797038 | -69.4% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1530203 | -41.3% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 956794 | -63.3% |
| `fibonacci` | 2230899 | LLGo · no LTO | 872609 | -60.9% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 403396 | -81.9% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 724875 | -67.5% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 506800 | -77.3% |
| `grep` | 2848917 | LLGo · no LTO | 1507302 | -47.1% |
| `grep` | 2848917 | LLGo · deadcode drop | 823931 | -71.1% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1314262 | -53.9% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 939772 | -67.0% |
| `glob` | 2257634 | LLGo · no LTO | 1089963 | -51.7% |
| `glob` | 2257634 | LLGo · deadcode drop | 492839 | -78.2% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 967278 | -57.2% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 656030 | -70.9% |
| `json-wasi` | 3314587 | LLGo · no LTO | 2666677 | -19.5% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1313179 | -60.4% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2447302 | -26.2% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1623971 | -51.0% |
| `llimport` | 8423078 | LLGo · no LTO | 7940343 | -5.7% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6489224 | -23.0% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 6786507 | -19.4% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6556841 | -22.2% |
| `path-report` | 2381190 | LLGo · no LTO | 1203561 | -49.5% |
| `path-report` | 2381190 | LLGo · deadcode drop | 594845 | -75.0% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1073224 | -54.9% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 762125 | -68.0% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1847096 | -33.6% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 955480 | -65.6% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1700239 | -38.9% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1127817 | -59.4% |
| `word-count` | 2253620 | LLGo · no LTO | 1071184 | -52.5% |
| `word-count` | 2253620 | LLGo · deadcode drop | 484817 | -78.5% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 924260 | -59.0% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 641121 | -71.6% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 9.065x | 10 |
| LLGo · deadcode drop | 4.362x | 10 |
| LLGo · full LTO (GlobalDCE off) | 7.836x | 10 |
| LLGo · full LTO + GlobalDCE | 5.320x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1074814 | +1010.8% |
| `base64` | 96760 | LLGo · deadcode drop | 498616 | +415.3% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 837095 | +765.1% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 567084 | +486.1% |
| `checksum` | 92685 | LLGo · no LTO | 1058727 | +1042.3% |
| `checksum` | 92685 | LLGo · deadcode drop | 485699 | +424.0% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 821339 | +786.2% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 548890 | +492.2% |
| `conv-wasi` | 201149 | LLGo · no LTO | 1657877 | +724.2% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 797038 | +296.2% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1530203 | +660.7% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 956794 | +375.7% |
| `fibonacci` | 62386 | LLGo · no LTO | 872609 | +1298.7% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 403396 | +546.6% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 724875 | +1061.9% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 506800 | +712.4% |
| `grep` | 303772 | LLGo · no LTO | 1507302 | +396.2% |
| `grep` | 303772 | LLGo · deadcode drop | 823931 | +171.2% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1314262 | +332.6% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 939772 | +209.4% |
| `glob` | 93153 | LLGo · no LTO | 1089963 | +1070.1% |
| `glob` | 93153 | LLGo · deadcode drop | 492839 | +429.1% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 967278 | +938.4% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 656030 | +604.2% |
| `json-wasi` | 493590 | LLGo · no LTO | 2666677 | +440.3% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1313179 | +166.0% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2447302 | +395.8% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1623971 | +229.0% |
| `llimport` | — | LLGo · no LTO | 7940343 | — |
| `llimport` | — | LLGo · deadcode drop | 6489224 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 6786507 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6556841 | — |
| `path-report` | 116889 | LLGo · no LTO | 1203561 | +929.7% |
| `path-report` | 116889 | LLGo · deadcode drop | 594845 | +408.9% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1073224 | +818.2% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 762125 | +552.0% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1847096 | +542.6% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 955480 | +232.4% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1700239 | +491.5% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1127817 | +292.4% |
| `word-count` | 86834 | LLGo · no LTO | 1071184 | +1133.6% |
| `word-count` | 86834 | LLGo · deadcode drop | 484817 | +458.3% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 924260 | +964.4% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 641121 | +638.3% |
