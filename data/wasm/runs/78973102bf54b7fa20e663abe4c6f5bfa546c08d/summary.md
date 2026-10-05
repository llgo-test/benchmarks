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
| LLGo · no LTO | 1.018x | 11 |
| LLGo · deadcode drop | 0.640x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.910x | 11 |
| LLGo · full LTO + GlobalDCE | 0.595x | 11 |

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
| `grep` | 2871426 | LLGo · no LTO | 2689216 | -6.3% |
| `grep` | 2871426 | LLGo · deadcode drop | 1736058 | -39.5% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2374418 | -17.3% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1609337 | -44.0% |
| `glob` | 2305059 | LLGo · no LTO | 2133090 | -7.5% |
| `glob` | 2305059 | LLGo · deadcode drop | 1291169 | -44.0% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1887197 | -18.1% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1185977 | -48.5% |
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
| `grep` | 155984 | LLGo · no LTO | 2689216 | +1624.0% |
| `grep` | 155984 | LLGo · deadcode drop | 1736058 | +1013.0% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2374418 | +1422.2% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1609337 | +931.7% |
| `glob` | 136553 | LLGo · no LTO | 2133090 | +1462.1% |
| `glob` | 136553 | LLGo · deadcode drop | 1291169 | +845.5% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1887197 | +1282.0% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1185977 | +768.5% |
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
| `base64` | 2275731 | LLGo · no LTO | 1531130 | -32.7% |
| `base64` | 2275731 | LLGo · deadcode drop | 928344 | -59.2% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 1313937 | -42.3% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 817141 | -64.1% |
| `checksum` | 2264417 | LLGo · no LTO | 1517837 | -33.0% |
| `checksum` | 2264417 | LLGo · deadcode drop | 909935 | -59.8% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 1295534 | -42.8% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 797719 | -64.8% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 2428653 | -6.9% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 1442348 | -44.7% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 2129666 | -18.3% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1289677 | -50.6% |
| `fibonacci` | 2230899 | LLGo · no LTO | 1346958 | -39.6% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 850463 | -61.9% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 1141787 | -48.8% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 743866 | -66.7% |
| `grep` | 2848917 | LLGo · no LTO | 2076222 | -27.1% |
| `grep` | 2848917 | LLGo · deadcode drop | 1376554 | -51.7% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1819395 | -36.1% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 1259975 | -55.8% |
| `glob` | 2257634 | LLGo · no LTO | 1683041 | -25.5% |
| `glob` | 2257634 | LLGo · deadcode drop | 1048329 | -53.6% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1446243 | -35.9% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 926981 | -58.9% |
| `json-wasi` | 3314587 | LLGo · no LTO | 3466373 | +4.6% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 2121573 | -36.0% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 3090231 | -6.8% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 2026160 | -38.9% |
| `llimport` | 8423078 | LLGo · no LTO | 9902994 | +17.6% |
| `llimport` | 8423078 | LLGo · deadcode drop | 8740386 | +3.8% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 9012721 | +7.0% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 8128305 | -3.5% |
| `path-report` | 2381190 | LLGo · no LTO | 1933791 | -18.8% |
| `path-report` | 2381190 | LLGo · deadcode drop | 1293606 | -45.7% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1689128 | -29.1% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 1163599 | -51.1% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 2688014 | -3.3% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1683273 | -39.5% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 2364513 | -15.0% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1517048 | -45.4% |
| `word-count` | 2253620 | LLGo · no LTO | 1650114 | -26.8% |
| `word-count` | 2253620 | LLGo · deadcode drop | 1024460 | -54.5% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 1414641 | -37.2% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 900556 | -60.0% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 13.293x | 10 |
| LLGo · deadcode drop | 8.295x | 10 |
| LLGo · full LTO (GlobalDCE off) | 11.528x | 10 |
| LLGo · full LTO + GlobalDCE | 7.430x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1531130 | +1482.4% |
| `base64` | 96760 | LLGo · deadcode drop | 928344 | +859.4% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 1313937 | +1257.9% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 817141 | +744.5% |
| `checksum` | 92685 | LLGo · no LTO | 1517837 | +1537.6% |
| `checksum` | 92685 | LLGo · deadcode drop | 909935 | +881.8% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 1295534 | +1297.8% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 797719 | +760.7% |
| `conv-wasi` | 201149 | LLGo · no LTO | 2428653 | +1107.4% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 1442348 | +617.1% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 2129666 | +958.8% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1289677 | +541.2% |
| `fibonacci` | 62386 | LLGo · no LTO | 1346958 | +2059.1% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 850463 | +1263.2% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 1141787 | +1730.2% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 743866 | +1092.4% |
| `grep` | 303772 | LLGo · no LTO | 2076222 | +583.5% |
| `grep` | 303772 | LLGo · deadcode drop | 1376554 | +353.2% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1819395 | +498.9% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 1259975 | +314.8% |
| `glob` | 93153 | LLGo · no LTO | 1683041 | +1706.7% |
| `glob` | 93153 | LLGo · deadcode drop | 1048329 | +1025.4% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1446243 | +1452.5% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 926981 | +895.1% |
| `json-wasi` | 493590 | LLGo · no LTO | 3466373 | +602.3% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 2121573 | +329.8% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 3090231 | +526.1% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 2026160 | +310.5% |
| `llimport` | — | LLGo · no LTO | 9902994 | — |
| `llimport` | — | LLGo · deadcode drop | 8740386 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 9012721 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 8128305 | — |
| `path-report` | 116889 | LLGo · no LTO | 1933791 | +1554.4% |
| `path-report` | 116889 | LLGo · deadcode drop | 1293606 | +1006.7% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1689128 | +1345.1% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 1163599 | +895.5% |
| `sha-wasi` | 287449 | LLGo · no LTO | 2688014 | +835.1% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1683273 | +485.6% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 2364513 | +722.6% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1517048 | +427.8% |
| `word-count` | 86834 | LLGo · no LTO | 1650114 | +1800.3% |
| `word-count` | 86834 | LLGo · deadcode drop | 1024460 | +1079.8% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 1414641 | +1529.1% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 900556 | +937.1% |
