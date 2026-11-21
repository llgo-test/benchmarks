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
| `base64` | 2322402 | LLGo · no LTO | 1910867 | -17.7% |
| `base64` | 2322402 | LLGo · deadcode drop | 1077529 | -53.6% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1715243 | -26.1% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1094444 | -52.9% |
| `checksum` | 2311672 | LLGo · no LTO | 1891585 | -18.2% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1062678 | -54.0% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1679788 | -27.3% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1061183 | -54.1% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2760199 | +4.6% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1542078 | -41.6% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2571061 | -2.6% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1618311 | -38.7% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1184602 | -47.9% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 953027 | -58.1% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1001524 | -56.0% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 869078 | -61.8% |
| `grep` | 2871426 | LLGo · no LTO | 2566971 | -10.6% |
| `grep` | 2871426 | LLGo · deadcode drop | 1580531 | -45.0% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2302107 | -19.8% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1600673 | -44.3% |
| `glob` | 2305059 | LLGo · no LTO | 1942191 | -15.7% |
| `glob` | 2305059 | LLGo · deadcode drop | 1082112 | -53.1% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1818649 | -21.1% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1181395 | -48.7% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4056854 | +21.5% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2269387 | -32.0% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3855943 | +15.5% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2559000 | -23.3% |
| `llimport` | 8440671 | LLGo · no LTO | 10915420 | +29.3% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9251836 | +9.6% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10302482 | +22.1% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 9213568 | +9.2% |
| `path-report` | 2428068 | LLGo · no LTO | 2086019 | -14.1% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1213546 | -50.0% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 1955087 | -19.5% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1318702 | -45.7% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3102621 | +10.4% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1847099 | -34.3% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2921232 | +3.9% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1962080 | -30.2% |
| `word-count` | 2300998 | LLGo · no LTO | 1901206 | -17.4% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1058380 | -54.0% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1773917 | -22.9% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1146887 | -50.2% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.308x | 10 |
| LLGo · deadcode drop | 6.692x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.350x | 10 |
| LLGo · full LTO + GlobalDCE | 6.975x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1910867 | +1009.0% |
| `base64` | 172302 | LLGo · deadcode drop | 1077529 | +525.4% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1715243 | +895.5% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1094444 | +535.2% |
| `checksum` | 169609 | LLGo · no LTO | 1891585 | +1015.3% |
| `checksum` | 169609 | LLGo · deadcode drop | 1062678 | +526.5% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1679788 | +890.4% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1061183 | +525.7% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2760199 | +1569.0% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1542078 | +832.4% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2571061 | +1454.6% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1618311 | +878.5% |
| `fibonacci` | 141855 | LLGo · no LTO | 1184602 | +735.1% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 953027 | +571.8% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1001524 | +606.0% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 869078 | +512.7% |
| `grep` | 155984 | LLGo · no LTO | 2566971 | +1545.7% |
| `grep` | 155984 | LLGo · deadcode drop | 1580531 | +913.3% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2302107 | +1375.9% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1600673 | +926.2% |
| `glob` | 136553 | LLGo · no LTO | 1942191 | +1322.3% |
| `glob` | 136553 | LLGo · deadcode drop | 1082112 | +692.4% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1818649 | +1231.8% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1181395 | +765.2% |
| `json-wasi` | 525666 | LLGo · no LTO | 4056854 | +671.8% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2269387 | +331.7% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3855943 | +633.5% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2559000 | +386.8% |
| `llimport` | — | LLGo · no LTO | 10915420 | — |
| `llimport` | — | LLGo · deadcode drop | 9251836 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10302482 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 9213568 | — |
| `path-report` | 194133 | LLGo · no LTO | 2086019 | +974.5% |
| `path-report` | 194133 | LLGo · deadcode drop | 1213546 | +525.1% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 1955087 | +907.1% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1318702 | +579.3% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3102621 | +781.5% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1847099 | +424.8% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2921232 | +730.0% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1962080 | +457.5% |
| `word-count` | 164053 | LLGo · no LTO | 1901206 | +1058.9% |
| `word-count` | 164053 | LLGo · deadcode drop | 1058380 | +545.1% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1773917 | +981.3% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1146887 | +599.1% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.306x | 11 |
| LLGo · deadcode drop | 0.306x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.487x | 11 |
| LLGo · full LTO + GlobalDCE | 0.348x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 544631 | -76.1% |
| `base64` | 2275731 | LLGo · deadcode drop | 544631 | -76.1% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 885629 | -61.1% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 598298 | -73.7% |
| `checksum` | 2264417 | LLGo · no LTO | 531034 | -76.5% |
| `checksum` | 2264417 | LLGo · deadcode drop | 531034 | -76.5% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 869768 | -61.6% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 579362 | -74.4% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 866808 | -66.8% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 866808 | -66.8% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1606744 | -38.4% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1000033 | -61.7% |
| `fibonacci` | 2230899 | LLGo · no LTO | 447701 | -79.9% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 447701 | -79.9% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 474660 | -78.7% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 433742 | -80.6% |
| `grep` | 2848917 | LLGo · no LTO | 880480 | -69.1% |
| `grep` | 2848917 | LLGo · deadcode drop | 880480 | -69.1% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1372583 | -51.8% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 971167 | -65.9% |
| `glob` | 2257634 | LLGo · no LTO | 536787 | -76.2% |
| `glob` | 2257634 | LLGo · deadcode drop | 536787 | -76.2% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1017370 | -54.9% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 685004 | -69.7% |
| `json-wasi` | 3314587 | LLGo · no LTO | 1409027 | -57.5% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1409027 | -57.5% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2580014 | -22.2% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1700283 | -48.7% |
| `llimport` | 8423078 | LLGo · no LTO | 6623130 | -21.4% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6623130 | -21.4% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 7022863 | -16.6% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6760244 | -19.7% |
| `path-report` | 2381190 | LLGo · no LTO | 647593 | -72.8% |
| `path-report` | 2381190 | LLGo · deadcode drop | 647593 | -72.8% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1131321 | -52.5% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 798486 | -66.5% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1030464 | -62.9% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1030464 | -62.9% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1786389 | -35.8% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1180693 | -57.5% |
| `word-count` | 2253620 | LLGo · no LTO | 530137 | -76.5% |
| `word-count` | 2253620 | LLGo · deadcode drop | 530137 | -76.5% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 969260 | -57.0% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 667748 | -70.4% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 4.743x | 10 |
| LLGo · deadcode drop | 4.743x | 10 |
| LLGo · full LTO (GlobalDCE off) | 7.864x | 10 |
| LLGo · full LTO + GlobalDCE | 5.455x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 544631 | +462.9% |
| `base64` | 96760 | LLGo · deadcode drop | 544631 | +462.9% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 885629 | +815.3% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 598298 | +518.3% |
| `checksum` | 92685 | LLGo · no LTO | 531034 | +472.9% |
| `checksum` | 92685 | LLGo · deadcode drop | 531034 | +472.9% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 869768 | +838.4% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 579362 | +525.1% |
| `conv-wasi` | 201149 | LLGo · no LTO | 866808 | +330.9% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 866808 | +330.9% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1606744 | +698.8% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1000033 | +397.2% |
| `fibonacci` | 62386 | LLGo · no LTO | 447701 | +617.6% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 447701 | +617.6% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 474660 | +660.8% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 433742 | +595.3% |
| `grep` | 303772 | LLGo · no LTO | 880480 | +189.8% |
| `grep` | 303772 | LLGo · deadcode drop | 880480 | +189.8% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1372583 | +351.8% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 971167 | +219.7% |
| `glob` | 93153 | LLGo · no LTO | 536787 | +476.2% |
| `glob` | 93153 | LLGo · deadcode drop | 536787 | +476.2% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1017370 | +992.1% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 685004 | +635.4% |
| `json-wasi` | 493590 | LLGo · no LTO | 1409027 | +185.5% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1409027 | +185.5% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2580014 | +422.7% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1700283 | +244.5% |
| `llimport` | — | LLGo · no LTO | 6623130 | — |
| `llimport` | — | LLGo · deadcode drop | 6623130 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 7022863 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6760244 | — |
| `path-report` | 116889 | LLGo · no LTO | 647593 | +454.0% |
| `path-report` | 116889 | LLGo · deadcode drop | 647593 | +454.0% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1131321 | +867.9% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 798486 | +583.1% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1030464 | +258.5% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1030464 | +258.5% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1786389 | +521.5% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1180693 | +310.7% |
| `word-count` | 86834 | LLGo · no LTO | 530137 | +510.5% |
| `word-count` | 86834 | LLGo · deadcode drop | 530137 | +510.5% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 969260 | +1016.2% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 667748 | +669.0% |
