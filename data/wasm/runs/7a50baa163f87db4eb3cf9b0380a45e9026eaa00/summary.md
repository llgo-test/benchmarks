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
| LLGo · no LTO | 0.907x | 11 |
| LLGo · deadcode drop | 0.554x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.832x | 11 |
| LLGo · full LTO + GlobalDCE | 0.575x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1911124 | -17.7% |
| `base64` | 2322402 | LLGo · deadcode drop | 1077750 | -53.6% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1715417 | -26.1% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1094631 | -52.9% |
| `checksum` | 2311672 | LLGo · no LTO | 1891822 | -18.2% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1062925 | -54.0% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1679999 | -27.3% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1061366 | -54.1% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2760453 | +4.6% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1542325 | -41.5% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2571237 | -2.5% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1618531 | -38.7% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1184809 | -47.9% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 953258 | -58.1% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1001697 | -56.0% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 869265 | -61.8% |
| `grep` | 2871426 | LLGo · no LTO | 2567196 | -10.6% |
| `grep` | 2871426 | LLGo · deadcode drop | 1580747 | -44.9% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2302291 | -19.8% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1600852 | -44.2% |
| `glob` | 2305059 | LLGo · no LTO | 1942385 | -15.7% |
| `glob` | 2305059 | LLGo · deadcode drop | 1082320 | -53.0% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1818859 | -21.1% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1181573 | -48.7% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4057114 | +21.5% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2269608 | -32.0% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3856122 | +15.5% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2559194 | -23.3% |
| `llimport` | 8440671 | LLGo · no LTO | 10915871 | +29.3% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9252320 | +9.6% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10302580 | +22.1% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 9213754 | +9.2% |
| `path-report` | 2428068 | LLGo · no LTO | 2086236 | -14.1% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1213799 | -50.0% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 1955198 | -19.5% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1318966 | -45.7% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3102912 | +10.4% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1847360 | -34.3% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2921434 | +3.9% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1962231 | -30.2% |
| `word-count` | 2300998 | LLGo · no LTO | 1901482 | -17.4% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1058606 | -54.0% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1774107 | -22.9% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1147061 | -50.1% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.309x | 10 |
| LLGo · deadcode drop | 6.693x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.351x | 10 |
| LLGo · full LTO + GlobalDCE | 6.976x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1911124 | +1009.2% |
| `base64` | 172302 | LLGo · deadcode drop | 1077750 | +525.5% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1715417 | +895.6% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1094631 | +535.3% |
| `checksum` | 169609 | LLGo · no LTO | 1891822 | +1015.4% |
| `checksum` | 169609 | LLGo · deadcode drop | 1062925 | +526.7% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1679999 | +890.5% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1061366 | +525.8% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2760453 | +1569.1% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1542325 | +832.6% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2571237 | +1454.7% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1618531 | +878.6% |
| `fibonacci` | 141855 | LLGo · no LTO | 1184809 | +735.2% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 953258 | +572.0% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1001697 | +606.1% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 869265 | +512.8% |
| `grep` | 155984 | LLGo · no LTO | 2567196 | +1545.8% |
| `grep` | 155984 | LLGo · deadcode drop | 1580747 | +913.4% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2302291 | +1376.0% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1600852 | +926.3% |
| `glob` | 136553 | LLGo · no LTO | 1942385 | +1322.4% |
| `glob` | 136553 | LLGo · deadcode drop | 1082320 | +692.6% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1818859 | +1232.0% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1181573 | +765.3% |
| `json-wasi` | 525666 | LLGo · no LTO | 4057114 | +671.8% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2269608 | +331.8% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3856122 | +633.6% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2559194 | +386.8% |
| `llimport` | — | LLGo · no LTO | 10915871 | — |
| `llimport` | — | LLGo · deadcode drop | 9252320 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10302580 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 9213754 | — |
| `path-report` | 194133 | LLGo · no LTO | 2086236 | +974.6% |
| `path-report` | 194133 | LLGo · deadcode drop | 1213799 | +525.2% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 1955198 | +907.1% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1318966 | +579.4% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3102912 | +781.6% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1847360 | +424.9% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2921434 | +730.0% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1962231 | +457.5% |
| `word-count` | 164053 | LLGo · no LTO | 1901482 | +1059.1% |
| `word-count` | 164053 | LLGo · deadcode drop | 1058606 | +545.3% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1774107 | +981.4% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1147061 | +599.2% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.306x | 11 |
| LLGo · deadcode drop | 0.306x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.487x | 11 |
| LLGo · full LTO + GlobalDCE | 0.348x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 544661 | -76.1% |
| `base64` | 2275731 | LLGo · deadcode drop | 544661 | -76.1% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 885655 | -61.1% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 598324 | -73.7% |
| `checksum` | 2264417 | LLGo · no LTO | 531064 | -76.5% |
| `checksum` | 2264417 | LLGo · deadcode drop | 531064 | -76.5% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 869794 | -61.6% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 579388 | -74.4% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 866838 | -66.8% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 866838 | -66.8% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1606770 | -38.4% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1000059 | -61.7% |
| `fibonacci` | 2230899 | LLGo · no LTO | 447731 | -79.9% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 447731 | -79.9% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 474686 | -78.7% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 433768 | -80.6% |
| `grep` | 2848917 | LLGo · no LTO | 880510 | -69.1% |
| `grep` | 2848917 | LLGo · deadcode drop | 880510 | -69.1% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1372609 | -51.8% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 971193 | -65.9% |
| `glob` | 2257634 | LLGo · no LTO | 536817 | -76.2% |
| `glob` | 2257634 | LLGo · deadcode drop | 536817 | -76.2% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1017396 | -54.9% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 685030 | -69.7% |
| `json-wasi` | 3314587 | LLGo · no LTO | 1409057 | -57.5% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1409057 | -57.5% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2580040 | -22.2% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1700309 | -48.7% |
| `llimport` | 8423078 | LLGo · no LTO | 6623507 | -21.4% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6623507 | -21.4% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 7022889 | -16.6% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6760270 | -19.7% |
| `path-report` | 2381190 | LLGo · no LTO | 647623 | -72.8% |
| `path-report` | 2381190 | LLGo · deadcode drop | 647623 | -72.8% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1131347 | -52.5% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 798512 | -66.5% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1030494 | -62.9% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1030494 | -62.9% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1786415 | -35.8% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1180719 | -57.5% |
| `word-count` | 2253620 | LLGo · no LTO | 530167 | -76.5% |
| `word-count` | 2253620 | LLGo · deadcode drop | 530167 | -76.5% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 969286 | -57.0% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 667774 | -70.4% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 4.744x | 10 |
| LLGo · deadcode drop | 4.744x | 10 |
| LLGo · full LTO (GlobalDCE off) | 7.864x | 10 |
| LLGo · full LTO + GlobalDCE | 5.455x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 544661 | +462.9% |
| `base64` | 96760 | LLGo · deadcode drop | 544661 | +462.9% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 885655 | +815.3% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 598324 | +518.4% |
| `checksum` | 92685 | LLGo · no LTO | 531064 | +473.0% |
| `checksum` | 92685 | LLGo · deadcode drop | 531064 | +473.0% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 869794 | +838.4% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 579388 | +525.1% |
| `conv-wasi` | 201149 | LLGo · no LTO | 866838 | +330.9% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 866838 | +330.9% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1606770 | +698.8% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1000059 | +397.2% |
| `fibonacci` | 62386 | LLGo · no LTO | 447731 | +617.7% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 447731 | +617.7% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 474686 | +660.9% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 433768 | +595.3% |
| `grep` | 303772 | LLGo · no LTO | 880510 | +189.9% |
| `grep` | 303772 | LLGo · deadcode drop | 880510 | +189.9% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1372609 | +351.9% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 971193 | +219.7% |
| `glob` | 93153 | LLGo · no LTO | 536817 | +476.3% |
| `glob` | 93153 | LLGo · deadcode drop | 536817 | +476.3% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1017396 | +992.2% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 685030 | +635.4% |
| `json-wasi` | 493590 | LLGo · no LTO | 1409057 | +185.5% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1409057 | +185.5% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2580040 | +422.7% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1700309 | +244.5% |
| `llimport` | — | LLGo · no LTO | 6623507 | — |
| `llimport` | — | LLGo · deadcode drop | 6623507 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 7022889 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6760270 | — |
| `path-report` | 116889 | LLGo · no LTO | 647623 | +454.0% |
| `path-report` | 116889 | LLGo · deadcode drop | 647623 | +454.0% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1131347 | +867.9% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 798512 | +583.1% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1030494 | +258.5% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1030494 | +258.5% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1786415 | +521.5% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1180719 | +310.8% |
| `word-count` | 86834 | LLGo · no LTO | 530167 | +510.6% |
| `word-count` | 86834 | LLGo · deadcode drop | 530167 | +510.6% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 969286 | +1016.3% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 667774 | +669.0% |
