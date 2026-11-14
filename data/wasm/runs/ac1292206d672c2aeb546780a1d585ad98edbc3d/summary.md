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
| LLGo · no LTO | 0.946x | 11 |
| LLGo · deadcode drop | 0.548x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.867x | 11 |
| LLGo · full LTO + GlobalDCE | 0.587x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1926408 | -17.1% |
| `base64` | 2322402 | LLGo · deadcode drop | 1060436 | -54.3% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1720642 | -25.9% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1099789 | -52.6% |
| `checksum` | 2311672 | LLGo · no LTO | 1906975 | -17.5% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1045862 | -54.8% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1684259 | -27.1% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1065882 | -53.9% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2791403 | +5.8% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1524871 | -42.2% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2587021 | -2.0% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1628469 | -38.3% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1704470 | -25.1% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 935876 | -58.9% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1493575 | -34.3% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 1007486 | -55.7% |
| `grep` | 2871426 | LLGo · no LTO | 2590202 | -9.8% |
| `grep` | 2871426 | LLGo · deadcode drop | 1567351 | -45.4% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2312136 | -19.5% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1612610 | -43.8% |
| `glob` | 2305059 | LLGo · no LTO | 1957434 | -15.1% |
| `glob` | 2305059 | LLGo · deadcode drop | 1064988 | -53.8% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1826162 | -20.8% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1189174 | -48.4% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4103379 | +22.9% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2269051 | -32.0% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3878658 | +16.2% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2584707 | -22.6% |
| `llimport` | 8440671 | LLGo · no LTO | 11115596 | +31.7% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9293016 | +10.1% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10439344 | +23.7% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 9321680 | +10.4% |
| `path-report` | 2428068 | LLGo · no LTO | 2103139 | -13.4% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1196806 | -50.7% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 1963803 | -19.1% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1327055 | -45.3% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3145554 | +11.9% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1830489 | -34.9% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2939684 | +4.6% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1975313 | -29.7% |
| `word-count` | 2300998 | LLGo · no LTO | 1916622 | -16.7% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1041358 | -54.7% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1781137 | -22.6% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1154557 | -49.8% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.828x | 10 |
| LLGo · deadcode drop | 6.609x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.816x | 10 |
| LLGo · full LTO + GlobalDCE | 7.121x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1926408 | +1018.0% |
| `base64` | 172302 | LLGo · deadcode drop | 1060436 | +515.5% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1720642 | +898.6% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1099789 | +538.3% |
| `checksum` | 169609 | LLGo · no LTO | 1906975 | +1024.3% |
| `checksum` | 169609 | LLGo · deadcode drop | 1045862 | +516.6% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1684259 | +893.0% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1065882 | +528.4% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2791403 | +1587.8% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1524871 | +822.0% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2587021 | +1464.2% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1628469 | +884.7% |
| `fibonacci` | 141855 | LLGo · no LTO | 1704470 | +1101.6% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 935876 | +559.7% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1493575 | +952.9% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 1007486 | +610.2% |
| `grep` | 155984 | LLGo · no LTO | 2590202 | +1560.6% |
| `grep` | 155984 | LLGo · deadcode drop | 1567351 | +904.8% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2312136 | +1382.3% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1612610 | +933.8% |
| `glob` | 136553 | LLGo · no LTO | 1957434 | +1333.5% |
| `glob` | 136553 | LLGo · deadcode drop | 1064988 | +679.9% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1826162 | +1237.3% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1189174 | +770.9% |
| `json-wasi` | 525666 | LLGo · no LTO | 4103379 | +680.6% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2269051 | +331.7% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3878658 | +637.9% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2584707 | +391.7% |
| `llimport` | — | LLGo · no LTO | 11115596 | — |
| `llimport` | — | LLGo · deadcode drop | 9293016 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10439344 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 9321680 | — |
| `path-report` | 194133 | LLGo · no LTO | 2103139 | +983.3% |
| `path-report` | 194133 | LLGo · deadcode drop | 1196806 | +516.5% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 1963803 | +911.6% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1327055 | +583.6% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3145554 | +793.7% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1830489 | +420.1% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2939684 | +735.2% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1975313 | +461.2% |
| `word-count` | 164053 | LLGo · no LTO | 1916622 | +1068.3% |
| `word-count` | 164053 | LLGo · deadcode drop | 1041358 | +534.8% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1781137 | +985.7% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1154557 | +603.8% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.579x | 11 |
| LLGo · deadcode drop | 0.300x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.510x | 11 |
| LLGo · full LTO + GlobalDCE | 0.356x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1107602 | -51.3% |
| `base64` | 2275731 | LLGo · deadcode drop | 531139 | -76.7% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 883168 | -61.2% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 597853 | -73.7% |
| `checksum` | 2264417 | LLGo · no LTO | 1092160 | -51.8% |
| `checksum` | 2264417 | LLGo · deadcode drop | 517743 | -77.1% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 866877 | -61.7% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 578494 | -74.5% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 1728188 | -33.7% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 851276 | -67.4% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1615531 | -38.1% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1005108 | -61.5% |
| `fibonacci` | 2230899 | LLGo · no LTO | 905149 | -59.4% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 432956 | -80.6% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 763946 | -65.8% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 532609 | -76.1% |
| `grep` | 2848917 | LLGo · no LTO | 1552772 | -45.5% |
| `grep` | 2848917 | LLGo · deadcode drop | 869959 | -69.5% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1375259 | -51.7% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 977938 | -65.7% |
| `glob` | 2257634 | LLGo · no LTO | 1123723 | -50.2% |
| `glob` | 2257634 | LLGo · deadcode drop | 523177 | -76.8% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1017261 | -54.9% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 686906 | -69.6% |
| `json-wasi` | 3314587 | LLGo · no LTO | 2775617 | -16.3% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1404973 | -57.6% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2591819 | -21.8% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1718200 | -48.2% |
| `llimport` | 8423078 | LLGo · no LTO | 8107681 | -3.7% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6704658 | -20.4% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 7183556 | -14.7% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6916183 | -17.9% |
| `path-report` | 2381190 | LLGo · no LTO | 1244759 | -47.7% |
| `path-report` | 2381190 | LLGo · deadcode drop | 634400 | -73.4% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1132369 | -52.4% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 801835 | -66.3% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1924637 | -30.8% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1015950 | -63.5% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1797400 | -35.4% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1188448 | -57.3% |
| `word-count` | 2253620 | LLGo · no LTO | 1104313 | -51.0% |
| `word-count` | 2253620 | LLGo · deadcode drop | 516509 | -77.1% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 969274 | -57.0% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 669854 | -70.3% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 9.383x | 10 |
| LLGo · deadcode drop | 4.648x | 10 |
| LLGo · full LTO (GlobalDCE off) | 8.257x | 10 |
| LLGo · full LTO + GlobalDCE | 5.589x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1107602 | +1044.7% |
| `base64` | 96760 | LLGo · deadcode drop | 531139 | +448.9% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 883168 | +812.7% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 597853 | +517.9% |
| `checksum` | 92685 | LLGo · no LTO | 1092160 | +1078.4% |
| `checksum` | 92685 | LLGo · deadcode drop | 517743 | +458.6% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 866877 | +835.3% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 578494 | +524.2% |
| `conv-wasi` | 201149 | LLGo · no LTO | 1728188 | +759.2% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 851276 | +323.2% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1615531 | +703.2% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1005108 | +399.7% |
| `fibonacci` | 62386 | LLGo · no LTO | 905149 | +1350.9% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 432956 | +594.0% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 763946 | +1124.5% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 532609 | +753.7% |
| `grep` | 303772 | LLGo · no LTO | 1552772 | +411.2% |
| `grep` | 303772 | LLGo · deadcode drop | 869959 | +186.4% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1375259 | +352.7% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 977938 | +221.9% |
| `glob` | 93153 | LLGo · no LTO | 1123723 | +1106.3% |
| `glob` | 93153 | LLGo · deadcode drop | 523177 | +461.6% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1017261 | +992.0% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 686906 | +637.4% |
| `json-wasi` | 493590 | LLGo · no LTO | 2775617 | +462.3% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1404973 | +184.6% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2591819 | +425.1% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1718200 | +248.1% |
| `llimport` | — | LLGo · no LTO | 8107681 | — |
| `llimport` | — | LLGo · deadcode drop | 6704658 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 7183556 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6916183 | — |
| `path-report` | 116889 | LLGo · no LTO | 1244759 | +964.9% |
| `path-report` | 116889 | LLGo · deadcode drop | 634400 | +442.7% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1132369 | +868.8% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 801835 | +586.0% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1924637 | +569.6% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1015950 | +253.4% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1797400 | +525.3% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1188448 | +313.4% |
| `word-count` | 86834 | LLGo · no LTO | 1104313 | +1171.8% |
| `word-count` | 86834 | LLGo · deadcode drop | 516509 | +494.8% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 969274 | +1016.2% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 669854 | +671.4% |
