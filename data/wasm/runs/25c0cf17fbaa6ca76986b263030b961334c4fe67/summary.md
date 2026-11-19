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
| `base64` | 2322402 | LLGo · no LTO | 1911090 | -17.7% |
| `base64` | 2322402 | LLGo · deadcode drop | 1076619 | -53.6% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1715314 | -26.1% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1093945 | -52.9% |
| `checksum` | 2311672 | LLGo · no LTO | 1891758 | -18.2% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1061829 | -54.1% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1679536 | -27.3% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1060627 | -54.1% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2761319 | +4.7% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1541692 | -41.6% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2571810 | -2.5% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1618722 | -38.6% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1184098 | -47.9% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 952114 | -58.1% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1000630 | -56.0% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 868114 | -61.8% |
| `grep` | 2871426 | LLGo · no LTO | 2567604 | -10.6% |
| `grep` | 2871426 | LLGo · deadcode drop | 1580554 | -45.0% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2301476 | -19.8% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1600630 | -44.3% |
| `glob` | 2305059 | LLGo · no LTO | 1942269 | -15.7% |
| `glob` | 2305059 | LLGo · deadcode drop | 1081095 | -53.1% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1818574 | -21.1% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1180764 | -48.8% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4058149 | +21.6% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2270176 | -32.0% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3859520 | +15.6% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2560849 | -23.3% |
| `llimport` | 8440671 | LLGo · no LTO | 10930932 | +29.5% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9261708 | +9.7% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10318357 | +22.2% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 9224132 | +9.3% |
| `path-report` | 2428068 | LLGo · no LTO | 2086095 | -14.1% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1212553 | -50.1% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 1955096 | -19.5% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1318290 | -45.7% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3104406 | +10.4% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1847529 | -34.3% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2922815 | +4.0% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1963250 | -30.2% |
| `word-count` | 2300998 | LLGo · no LTO | 1901318 | -17.4% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1057387 | -54.0% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1773649 | -22.9% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1146347 | -50.2% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.309x | 10 |
| LLGo · deadcode drop | 6.689x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.350x | 10 |
| LLGo · full LTO + GlobalDCE | 6.974x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1911090 | +1009.2% |
| `base64` | 172302 | LLGo · deadcode drop | 1076619 | +524.8% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1715314 | +895.5% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1093945 | +534.9% |
| `checksum` | 169609 | LLGo · no LTO | 1891758 | +1015.4% |
| `checksum` | 169609 | LLGo · deadcode drop | 1061829 | +526.0% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1679536 | +890.2% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1060627 | +525.3% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2761319 | +1569.6% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1541692 | +832.2% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2571810 | +1455.0% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1618722 | +878.8% |
| `fibonacci` | 141855 | LLGo · no LTO | 1184098 | +734.7% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 952114 | +571.2% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1000630 | +605.4% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 868114 | +512.0% |
| `grep` | 155984 | LLGo · no LTO | 2567604 | +1546.1% |
| `grep` | 155984 | LLGo · deadcode drop | 1580554 | +913.3% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2301476 | +1375.5% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1600630 | +926.2% |
| `glob` | 136553 | LLGo · no LTO | 1942269 | +1322.4% |
| `glob` | 136553 | LLGo · deadcode drop | 1081095 | +691.7% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1818574 | +1231.8% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1180764 | +764.7% |
| `json-wasi` | 525666 | LLGo · no LTO | 4058149 | +672.0% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2270176 | +331.9% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3859520 | +634.2% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2560849 | +387.2% |
| `llimport` | — | LLGo · no LTO | 10930932 | — |
| `llimport` | — | LLGo · deadcode drop | 9261708 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10318357 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 9224132 | — |
| `path-report` | 194133 | LLGo · no LTO | 2086095 | +974.6% |
| `path-report` | 194133 | LLGo · deadcode drop | 1212553 | +524.6% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 1955096 | +907.1% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1318290 | +579.1% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3104406 | +782.0% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1847529 | +424.9% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2922815 | +730.4% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1963250 | +457.8% |
| `word-count` | 164053 | LLGo · no LTO | 1901318 | +1059.0% |
| `word-count` | 164053 | LLGo · deadcode drop | 1057387 | +544.5% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1773649 | +981.1% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1146347 | +598.8% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.306x | 11 |
| LLGo · deadcode drop | 0.306x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.487x | 11 |
| LLGo · full LTO + GlobalDCE | 0.348x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 543985 | -76.1% |
| `base64` | 2275731 | LLGo · deadcode drop | 543985 | -76.1% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 885606 | -61.1% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 597708 | -73.7% |
| `checksum` | 2264417 | LLGo · no LTO | 530380 | -76.6% |
| `checksum` | 2264417 | LLGo · deadcode drop | 530380 | -76.6% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 869764 | -61.6% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 578763 | -74.4% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 866369 | -66.8% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 866369 | -66.8% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1607422 | -38.4% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1000182 | -61.7% |
| `fibonacci` | 2230899 | LLGo · no LTO | 446999 | -80.0% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 446999 | -80.0% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 474128 | -78.7% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 432906 | -80.6% |
| `grep` | 2848917 | LLGo · no LTO | 880457 | -69.1% |
| `grep` | 2848917 | LLGo · deadcode drop | 880457 | -69.1% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1372026 | -51.8% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 971127 | -65.9% |
| `glob` | 2257634 | LLGo · no LTO | 536027 | -76.3% |
| `glob` | 2257634 | LLGo · deadcode drop | 536027 | -76.3% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1017389 | -54.9% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 684407 | -69.7% |
| `json-wasi` | 3314587 | LLGo · no LTO | 1408936 | -57.5% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1408936 | -57.5% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2581603 | -22.1% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1700861 | -48.7% |
| `llimport` | 8423078 | LLGo · no LTO | 6653498 | -21.0% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6653498 | -21.0% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 7059783 | -16.2% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6784795 | -19.4% |
| `path-report` | 2381190 | LLGo · no LTO | 646834 | -72.8% |
| `path-report` | 2381190 | LLGo · deadcode drop | 646834 | -72.8% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1131336 | -52.5% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 797885 | -66.5% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1030607 | -62.9% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1030607 | -62.9% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1787319 | -35.7% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1181316 | -57.5% |
| `word-count` | 2253620 | LLGo · no LTO | 529382 | -76.5% |
| `word-count` | 2253620 | LLGo · deadcode drop | 529382 | -76.5% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 969282 | -57.0% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 667187 | -70.4% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 4.739x | 10 |
| LLGo · deadcode drop | 4.739x | 10 |
| LLGo · full LTO (GlobalDCE off) | 7.864x | 10 |
| LLGo · full LTO + GlobalDCE | 5.452x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 543985 | +462.2% |
| `base64` | 96760 | LLGo · deadcode drop | 543985 | +462.2% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 885606 | +815.3% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 597708 | +517.7% |
| `checksum` | 92685 | LLGo · no LTO | 530380 | +472.2% |
| `checksum` | 92685 | LLGo · deadcode drop | 530380 | +472.2% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 869764 | +838.4% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 578763 | +524.4% |
| `conv-wasi` | 201149 | LLGo · no LTO | 866369 | +330.7% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 866369 | +330.7% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1607422 | +699.1% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1000182 | +397.2% |
| `fibonacci` | 62386 | LLGo · no LTO | 446999 | +616.5% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 446999 | +616.5% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 474128 | +660.0% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 432906 | +593.9% |
| `grep` | 303772 | LLGo · no LTO | 880457 | +189.8% |
| `grep` | 303772 | LLGo · deadcode drop | 880457 | +189.8% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1372026 | +351.7% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 971127 | +219.7% |
| `glob` | 93153 | LLGo · no LTO | 536027 | +475.4% |
| `glob` | 93153 | LLGo · deadcode drop | 536027 | +475.4% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1017389 | +992.2% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 684407 | +634.7% |
| `json-wasi` | 493590 | LLGo · no LTO | 1408936 | +185.4% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1408936 | +185.4% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2581603 | +423.0% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1700861 | +244.6% |
| `llimport` | — | LLGo · no LTO | 6653498 | — |
| `llimport` | — | LLGo · deadcode drop | 6653498 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 7059783 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6784795 | — |
| `path-report` | 116889 | LLGo · no LTO | 646834 | +453.4% |
| `path-report` | 116889 | LLGo · deadcode drop | 646834 | +453.4% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1131336 | +867.9% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 797885 | +582.6% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1030607 | +258.5% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1030607 | +258.5% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1787319 | +521.8% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1181316 | +311.0% |
| `word-count` | 86834 | LLGo · no LTO | 529382 | +509.6% |
| `word-count` | 86834 | LLGo · deadcode drop | 529382 | +509.6% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 969282 | +1016.2% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 667187 | +668.3% |
