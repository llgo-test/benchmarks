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
| LLGo · no LTO | 0.942x | 11 |
| LLGo · deadcode drop | 0.539x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.855x | 11 |
| LLGo · full LTO + GlobalDCE | 0.577x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1905434 | -18.0% |
| `base64` | 2322402 | LLGo · deadcode drop | 1027758 | -55.7% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1684107 | -27.5% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1072959 | -53.8% |
| `checksum` | 2311672 | LLGo · no LTO | 1884890 | -18.5% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1013519 | -56.2% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1647614 | -28.7% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1038999 | -55.1% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2754365 | +4.4% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1478589 | -44.0% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2536201 | -3.9% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1591638 | -39.7% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1686049 | -25.9% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 905264 | -60.2% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1472795 | -35.2% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 976152 | -57.1% |
| `grep` | 2871426 | LLGo · no LTO | 2563297 | -10.7% |
| `grep` | 2871426 | LLGo · deadcode drop | 1526276 | -46.8% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2259568 | -21.3% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1568678 | -45.4% |
| `glob` | 2305059 | LLGo · no LTO | 1934937 | -16.1% |
| `glob` | 2305059 | LLGo · deadcode drop | 1033562 | -55.2% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1790338 | -22.3% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1158967 | -49.7% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4046062 | +21.2% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2190263 | -34.4% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3774392 | +13.1% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2493579 | -25.3% |
| `llimport` | 8440671 | LLGo · no LTO | 11047275 | +30.9% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9067695 | +7.4% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10098546 | +19.6% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 8974151 | +6.3% |
| `path-report` | 2428068 | LLGo · no LTO | 2267881 | -6.6% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1351255 | -44.3% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 2113078 | -13.0% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1473033 | -39.3% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3071587 | +9.3% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1752067 | -37.7% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2856924 | +1.6% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1902207 | -32.3% |
| `word-count` | 2300998 | LLGo · no LTO | 1895274 | -17.6% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1009230 | -56.1% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1749628 | -24.0% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1126294 | -51.1% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.778x | 10 |
| LLGo · deadcode drop | 6.496x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.687x | 10 |
| LLGo · full LTO + GlobalDCE | 7.014x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1905434 | +1005.9% |
| `base64` | 172302 | LLGo · deadcode drop | 1027758 | +496.5% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1684107 | +877.4% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1072959 | +522.7% |
| `checksum` | 169609 | LLGo · no LTO | 1884890 | +1011.3% |
| `checksum` | 169609 | LLGo · deadcode drop | 1013519 | +497.6% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1647614 | +871.4% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1038999 | +512.6% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2754365 | +1565.4% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1478589 | +794.0% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2536201 | +1433.5% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1591638 | +862.4% |
| `fibonacci` | 141855 | LLGo · no LTO | 1686049 | +1088.6% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 905264 | +538.2% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1472795 | +938.2% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 976152 | +588.1% |
| `grep` | 155984 | LLGo · no LTO | 2563297 | +1543.3% |
| `grep` | 155984 | LLGo · deadcode drop | 1526276 | +878.5% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2259568 | +1348.6% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1568678 | +905.7% |
| `glob` | 136553 | LLGo · no LTO | 1934937 | +1317.0% |
| `glob` | 136553 | LLGo · deadcode drop | 1033562 | +656.9% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1790338 | +1211.1% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1158967 | +748.7% |
| `json-wasi` | 525666 | LLGo · no LTO | 4046062 | +669.7% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2190263 | +316.7% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3774392 | +618.0% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2493579 | +374.4% |
| `llimport` | — | LLGo · no LTO | 11047275 | — |
| `llimport` | — | LLGo · deadcode drop | 9067695 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10098546 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 8974151 | — |
| `path-report` | 194133 | LLGo · no LTO | 2267881 | +1068.2% |
| `path-report` | 194133 | LLGo · deadcode drop | 1351255 | +596.0% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 2113078 | +988.5% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1473033 | +658.8% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3071587 | +772.7% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1752067 | +397.8% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2856924 | +711.7% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1902207 | +440.4% |
| `word-count` | 164053 | LLGo · no LTO | 1895274 | +1055.3% |
| `word-count` | 164053 | LLGo · deadcode drop | 1009230 | +515.2% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1749628 | +966.5% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1126294 | +586.5% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.567x | 11 |
| LLGo · deadcode drop | 0.287x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.495x | 11 |
| LLGo · full LTO + GlobalDCE | 0.342x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1077378 | -52.7% |
| `base64` | 2275731 | LLGo · deadcode drop | 497174 | -78.2% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 848900 | -62.7% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 564938 | -75.2% |
| `checksum` | 2264417 | LLGo · no LTO | 1061056 | -53.1% |
| `checksum` | 2264417 | LLGo · deadcode drop | 484288 | -78.6% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 832946 | -63.2% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 545956 | -75.9% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 1662323 | -36.3% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 795719 | -69.5% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1548242 | -40.6% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 954634 | -63.4% |
| `fibonacci` | 2230899 | LLGo · no LTO | 871737 | -60.9% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 401161 | -82.0% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 737627 | -66.9% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 499080 | -77.6% |
| `grep` | 2848917 | LLGo · no LTO | 1513996 | -46.9% |
| `grep` | 2848917 | LLGo · deadcode drop | 825958 | -71.0% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1335151 | -53.1% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 942496 | -66.9% |
| `glob` | 2257634 | LLGo · no LTO | 1092505 | -51.6% |
| `glob` | 2257634 | LLGo · deadcode drop | 490975 | -78.3% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 984438 | -56.4% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 652390 | -71.1% |
| `json-wasi` | 3314587 | LLGo · no LTO | 2676949 | -19.2% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1313073 | -60.4% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2464831 | -25.6% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1612543 | -51.4% |
| `llimport` | 8423078 | LLGo · no LTO | 8044506 | -4.5% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6506854 | -22.7% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 6886767 | -18.2% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6626447 | -21.3% |
| `path-report` | 2381190 | LLGo · no LTO | 1325693 | -44.3% |
| `path-report` | 2381190 | LLGo · deadcode drop | 712708 | -70.1% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1209791 | -49.2% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 872152 | -63.4% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1851533 | -33.4% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 954372 | -65.7% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1720547 | -38.1% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1125282 | -59.5% |
| `word-count` | 2253620 | LLGo · no LTO | 1073797 | -52.4% |
| `word-count` | 2253620 | LLGo · deadcode drop | 482968 | -78.6% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 939262 | -58.3% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 637002 | -71.7% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 9.172x | 10 |
| LLGo · deadcode drop | 4.433x | 10 |
| LLGo · full LTO (GlobalDCE off) | 8.030x | 10 |
| LLGo · full LTO + GlobalDCE | 5.368x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1077378 | +1013.5% |
| `base64` | 96760 | LLGo · deadcode drop | 497174 | +413.8% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 848900 | +777.3% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 564938 | +483.9% |
| `checksum` | 92685 | LLGo · no LTO | 1061056 | +1044.8% |
| `checksum` | 92685 | LLGo · deadcode drop | 484288 | +422.5% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 832946 | +798.7% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 545956 | +489.0% |
| `conv-wasi` | 201149 | LLGo · no LTO | 1662323 | +726.4% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 795719 | +295.6% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1548242 | +669.7% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 954634 | +374.6% |
| `fibonacci` | 62386 | LLGo · no LTO | 871737 | +1297.3% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 401161 | +543.0% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 737627 | +1082.4% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 499080 | +700.0% |
| `grep` | 303772 | LLGo · no LTO | 1513996 | +398.4% |
| `grep` | 303772 | LLGo · deadcode drop | 825958 | +171.9% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1335151 | +339.5% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 942496 | +210.3% |
| `glob` | 93153 | LLGo · no LTO | 1092505 | +1072.8% |
| `glob` | 93153 | LLGo · deadcode drop | 490975 | +427.1% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 984438 | +956.8% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 652390 | +600.3% |
| `json-wasi` | 493590 | LLGo · no LTO | 2676949 | +442.3% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1313073 | +166.0% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2464831 | +399.4% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1612543 | +226.7% |
| `llimport` | — | LLGo · no LTO | 8044506 | — |
| `llimport` | — | LLGo · deadcode drop | 6506854 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 6886767 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6626447 | — |
| `path-report` | 116889 | LLGo · no LTO | 1325693 | +1034.1% |
| `path-report` | 116889 | LLGo · deadcode drop | 712708 | +509.7% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1209791 | +935.0% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 872152 | +646.1% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1851533 | +544.1% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 954372 | +232.0% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1720547 | +498.6% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1125282 | +291.5% |
| `word-count` | 86834 | LLGo · no LTO | 1073797 | +1136.6% |
| `word-count` | 86834 | LLGo · deadcode drop | 482968 | +456.2% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 939262 | +981.7% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 637002 | +633.6% |
