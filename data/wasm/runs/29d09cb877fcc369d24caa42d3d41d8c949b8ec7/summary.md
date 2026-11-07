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
| LLGo · no LTO | 0.936x | 11 |
| LLGo · deadcode drop | 0.538x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.845x | 11 |
| LLGo · full LTO + GlobalDCE | 0.579x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1895059 | -18.4% |
| `base64` | 2322402 | LLGo · deadcode drop | 1026740 | -55.8% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1663809 | -28.4% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1071810 | -53.8% |
| `checksum` | 2311672 | LLGo · no LTO | 1874878 | -18.9% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1012450 | -56.2% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1627477 | -29.6% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1038867 | -55.1% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2737506 | +3.8% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1474154 | -44.1% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2510156 | -4.9% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1594237 | -39.6% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1676119 | -26.3% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 905268 | -60.2% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1447444 | -36.4% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 984235 | -56.7% |
| `grep` | 2871426 | LLGo · no LTO | 2550552 | -11.2% |
| `grep` | 2871426 | LLGo · deadcode drop | 1524363 | -46.9% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2236155 | -22.1% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1571899 | -45.3% |
| `glob` | 2305059 | LLGo · no LTO | 1924959 | -16.5% |
| `glob` | 2305059 | LLGo · deadcode drop | 1033289 | -55.2% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1770300 | -23.2% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1165048 | -49.5% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4021876 | +20.5% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2182759 | -34.6% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3748308 | +12.3% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2508360 | -24.9% |
| `llimport` | 8440671 | LLGo · no LTO | 10918189 | +29.4% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9037091 | +7.1% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 9973113 | +18.2% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 8903494 | +5.5% |
| `path-report` | 2428068 | LLGo · no LTO | 2257722 | -7.0% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1350720 | -44.4% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 2093016 | -13.8% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1488585 | -38.7% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3053605 | +8.6% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1746846 | -37.9% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2826190 | +0.5% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1904482 | -32.3% |
| `word-count` | 2300998 | LLGo · no LTO | 1885177 | -18.1% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1008838 | -56.2% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1729552 | -24.8% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1133067 | -50.8% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.713x | 10 |
| LLGo · deadcode drop | 6.487x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.567x | 10 |
| LLGo · full LTO + GlobalDCE | 7.041x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1895059 | +999.8% |
| `base64` | 172302 | LLGo · deadcode drop | 1026740 | +495.9% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1663809 | +865.6% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1071810 | +522.1% |
| `checksum` | 169609 | LLGo · no LTO | 1874878 | +1005.4% |
| `checksum` | 169609 | LLGo · deadcode drop | 1012450 | +496.9% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1627477 | +859.5% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1038867 | +512.5% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2737506 | +1555.2% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1474154 | +791.3% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2510156 | +1417.8% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1594237 | +864.0% |
| `fibonacci` | 141855 | LLGo · no LTO | 1676119 | +1081.6% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 905268 | +538.2% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1447444 | +920.4% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 984235 | +593.8% |
| `grep` | 155984 | LLGo · no LTO | 2550552 | +1535.1% |
| `grep` | 155984 | LLGo · deadcode drop | 1524363 | +877.3% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2236155 | +1333.6% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1571899 | +907.7% |
| `glob` | 136553 | LLGo · no LTO | 1924959 | +1309.7% |
| `glob` | 136553 | LLGo · deadcode drop | 1033289 | +656.7% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1770300 | +1196.4% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1165048 | +753.2% |
| `json-wasi` | 525666 | LLGo · no LTO | 4021876 | +665.1% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2182759 | +315.2% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3748308 | +613.1% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2508360 | +377.2% |
| `llimport` | — | LLGo · no LTO | 10918189 | — |
| `llimport` | — | LLGo · deadcode drop | 9037091 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 9973113 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 8903494 | — |
| `path-report` | 194133 | LLGo · no LTO | 2257722 | +1063.0% |
| `path-report` | 194133 | LLGo · deadcode drop | 1350720 | +595.8% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 2093016 | +978.1% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1488585 | +666.8% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3053605 | +767.6% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1746846 | +396.3% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2826190 | +703.0% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1904482 | +441.1% |
| `word-count` | 164053 | LLGo · no LTO | 1885177 | +1049.1% |
| `word-count` | 164053 | LLGo · deadcode drop | 1008838 | +514.9% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1729552 | +954.3% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1133067 | +590.7% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.565x | 11 |
| LLGo · deadcode drop | 0.287x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.489x | 11 |
| LLGo · full LTO + GlobalDCE | 0.344x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1074402 | -52.8% |
| `base64` | 2275731 | LLGo · deadcode drop | 498266 | -78.1% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 837168 | -63.2% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 567080 | -75.1% |
| `checksum` | 2264417 | LLGo · no LTO | 1058315 | -53.3% |
| `checksum` | 2264417 | LLGo · deadcode drop | 485349 | -78.6% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 821412 | -63.7% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 548886 | -75.8% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 1657485 | -36.4% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 796692 | -69.5% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1533461 | -41.2% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 959975 | -63.2% |
| `fibonacci` | 2230899 | LLGo · no LTO | 872197 | -60.9% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 403046 | -81.9% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 724948 | -67.5% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 506796 | -77.3% |
| `grep` | 2848917 | LLGo · no LTO | 1510138 | -47.0% |
| `grep` | 2848917 | LLGo · deadcode drop | 826997 | -71.0% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1317534 | -53.8% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 942967 | -66.9% |
| `glob` | 2257634 | LLGo · no LTO | 1089551 | -51.7% |
| `glob` | 2257634 | LLGo · deadcode drop | 492505 | -78.2% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 970550 | -57.0% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 659225 | -70.8% |
| `json-wasi` | 3314587 | LLGo · no LTO | 2666269 | -19.6% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1312849 | -60.4% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2450570 | -26.1% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1627162 | -50.9% |
| `llimport` | 8423078 | LLGo · no LTO | 7943240 | -5.7% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6492266 | -22.9% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 6789806 | -19.4% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6560063 | -22.1% |
| `path-report` | 2381190 | LLGo · no LTO | 1322741 | -44.5% |
| `path-report` | 2381190 | LLGo · deadcode drop | 714045 | -70.0% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1196080 | -49.8% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 884904 | -62.8% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1846688 | -33.6% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 955134 | -65.7% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1703497 | -38.7% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1130998 | -59.3% |
| `word-count` | 2253620 | LLGo · no LTO | 1070788 | -52.5% |
| `word-count` | 2253620 | LLGo · deadcode drop | 484483 | -78.5% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 927532 | -58.8% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 644316 | -71.4% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 9.150x | 10 |
| LLGo · deadcode drop | 4.442x | 10 |
| LLGo · full LTO (GlobalDCE off) | 7.933x | 10 |
| LLGo · full LTO + GlobalDCE | 5.412x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1074402 | +1010.4% |
| `base64` | 96760 | LLGo · deadcode drop | 498266 | +415.0% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 837168 | +765.2% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 567080 | +486.1% |
| `checksum` | 92685 | LLGo · no LTO | 1058315 | +1041.8% |
| `checksum` | 92685 | LLGo · deadcode drop | 485349 | +423.7% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 821412 | +786.2% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 548886 | +492.2% |
| `conv-wasi` | 201149 | LLGo · no LTO | 1657485 | +724.0% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 796692 | +296.1% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1533461 | +662.4% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 959975 | +377.2% |
| `fibonacci` | 62386 | LLGo · no LTO | 872197 | +1298.1% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 403046 | +546.1% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 724948 | +1062.0% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 506796 | +712.4% |
| `grep` | 303772 | LLGo · no LTO | 1510138 | +397.1% |
| `grep` | 303772 | LLGo · deadcode drop | 826997 | +172.2% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1317534 | +333.7% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 942967 | +210.4% |
| `glob` | 93153 | LLGo · no LTO | 1089551 | +1069.6% |
| `glob` | 93153 | LLGo · deadcode drop | 492505 | +428.7% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 970550 | +941.9% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 659225 | +607.7% |
| `json-wasi` | 493590 | LLGo · no LTO | 2666269 | +440.2% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1312849 | +166.0% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2450570 | +396.5% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1627162 | +229.7% |
| `llimport` | — | LLGo · no LTO | 7943240 | — |
| `llimport` | — | LLGo · deadcode drop | 6492266 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 6789806 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6560063 | — |
| `path-report` | 116889 | LLGo · no LTO | 1322741 | +1031.6% |
| `path-report` | 116889 | LLGo · deadcode drop | 714045 | +510.9% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1196080 | +923.3% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 884904 | +657.0% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1846688 | +542.4% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 955134 | +232.3% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1703497 | +492.6% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1130998 | +293.5% |
| `word-count` | 86834 | LLGo · no LTO | 1070788 | +1133.1% |
| `word-count` | 86834 | LLGo · deadcode drop | 484483 | +457.9% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 927532 | +968.2% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 644316 | +642.0% |
