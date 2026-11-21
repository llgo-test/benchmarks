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
| LLGo · no LTO | 0.906x | 11 |
| LLGo · deadcode drop | 0.554x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.832x | 11 |
| LLGo · full LTO + GlobalDCE | 0.575x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1909670 | -17.8% |
| `base64` | 2322402 | LLGo · deadcode drop | 1076359 | -53.7% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1714327 | -26.2% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1093731 | -52.9% |
| `checksum` | 2311672 | LLGo · no LTO | 1890320 | -18.2% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1061505 | -54.1% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1678560 | -27.4% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1060375 | -54.1% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2759272 | +4.6% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1541142 | -41.6% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2570265 | -2.6% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1618183 | -38.7% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1183751 | -48.0% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 951949 | -58.1% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1000372 | -56.0% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 867999 | -61.8% |
| `grep` | 2871426 | LLGo · no LTO | 2565325 | -10.7% |
| `grep` | 2871426 | LLGo · deadcode drop | 1579968 | -45.0% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2299857 | -19.9% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1600051 | -44.3% |
| `glob` | 2305059 | LLGo · no LTO | 1940961 | -15.8% |
| `glob` | 2305059 | LLGo · deadcode drop | 1080924 | -53.1% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1817684 | -21.1% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1180654 | -48.8% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4054720 | +21.5% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2268943 | -32.0% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3856975 | +15.5% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2559271 | -23.3% |
| `llimport` | 8440671 | LLGo · no LTO | 10918688 | +29.4% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9253947 | +9.6% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10308177 | +22.1% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 9217192 | +9.2% |
| `path-report` | 2428068 | LLGo · no LTO | 2084744 | -14.1% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1212334 | -50.1% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 1954075 | -19.5% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1318089 | -45.7% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3101623 | +10.3% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1846243 | -34.3% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2921020 | +3.9% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1962301 | -30.2% |
| `word-count` | 2300998 | LLGo · no LTO | 1899925 | -17.4% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1057057 | -54.1% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1772728 | -23.0% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1146167 | -50.2% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.301x | 10 |
| LLGo · deadcode drop | 6.686x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.344x | 10 |
| LLGo · full LTO + GlobalDCE | 6.972x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1909670 | +1008.3% |
| `base64` | 172302 | LLGo · deadcode drop | 1076359 | +524.7% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1714327 | +895.0% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1093731 | +534.8% |
| `checksum` | 169609 | LLGo · no LTO | 1890320 | +1014.5% |
| `checksum` | 169609 | LLGo · deadcode drop | 1061505 | +525.9% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1678560 | +889.7% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1060375 | +525.2% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2759272 | +1568.4% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1541142 | +831.9% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2570265 | +1454.1% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1618183 | +878.4% |
| `fibonacci` | 141855 | LLGo · no LTO | 1183751 | +734.5% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 951949 | +571.1% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1000372 | +605.2% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 867999 | +511.9% |
| `grep` | 155984 | LLGo · no LTO | 2565325 | +1544.6% |
| `grep` | 155984 | LLGo · deadcode drop | 1579968 | +912.9% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2299857 | +1374.4% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1600051 | +925.8% |
| `glob` | 136553 | LLGo · no LTO | 1940961 | +1321.4% |
| `glob` | 136553 | LLGo · deadcode drop | 1080924 | +691.6% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1817684 | +1231.1% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1180654 | +764.6% |
| `json-wasi` | 525666 | LLGo · no LTO | 4054720 | +671.3% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2268943 | +331.6% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3856975 | +633.7% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2559271 | +386.9% |
| `llimport` | — | LLGo · no LTO | 10918688 | — |
| `llimport` | — | LLGo · deadcode drop | 9253947 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10308177 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 9217192 | — |
| `path-report` | 194133 | LLGo · no LTO | 2084744 | +973.9% |
| `path-report` | 194133 | LLGo · deadcode drop | 1212334 | +524.5% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 1954075 | +906.6% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1318089 | +579.0% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3101623 | +781.2% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1846243 | +424.5% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2921020 | +729.9% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1962301 | +457.5% |
| `word-count` | 164053 | LLGo · no LTO | 1899925 | +1058.1% |
| `word-count` | 164053 | LLGo · deadcode drop | 1057057 | +544.3% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1772728 | +980.6% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1146167 | +598.7% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.305x | 11 |
| LLGo · deadcode drop | 0.305x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.487x | 11 |
| LLGo · full LTO + GlobalDCE | 0.348x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 543832 | -76.1% |
| `base64` | 2275731 | LLGo · deadcode drop | 543832 | -76.1% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 885162 | -61.1% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 597535 | -73.7% |
| `checksum` | 2264417 | LLGo · no LTO | 530208 | -76.6% |
| `checksum` | 2264417 | LLGo · deadcode drop | 530208 | -76.6% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 869292 | -61.6% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 578576 | -74.4% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 866051 | -66.8% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 866051 | -66.8% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1606721 | -38.4% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 999911 | -61.7% |
| `fibonacci` | 2230899 | LLGo · no LTO | 446918 | -80.0% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 446918 | -80.0% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 474065 | -78.8% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 432843 | -80.6% |
| `grep` | 2848917 | LLGo · no LTO | 880071 | -69.1% |
| `grep` | 2848917 | LLGo · deadcode drop | 880071 | -69.1% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1371230 | -51.9% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 970741 | -65.9% |
| `glob` | 2257634 | LLGo · no LTO | 535909 | -76.3% |
| `glob` | 2257634 | LLGo · deadcode drop | 535909 | -76.3% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1016932 | -55.0% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 684259 | -69.7% |
| `json-wasi` | 3314587 | LLGo · no LTO | 1408148 | -57.5% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1408148 | -57.5% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2580402 | -22.2% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1700144 | -48.7% |
| `llimport` | 8423078 | LLGo · no LTO | 6634226 | -21.2% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6634226 | -21.2% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 7041159 | -16.4% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6767946 | -19.6% |
| `path-report` | 2381190 | LLGo · no LTO | 646725 | -72.8% |
| `path-report` | 2381190 | LLGo · deadcode drop | 646725 | -72.8% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1130879 | -52.5% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 797737 | -66.5% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1029795 | -63.0% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1029795 | -63.0% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1786421 | -35.8% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1180837 | -57.5% |
| `word-count` | 2253620 | LLGo · no LTO | 529235 | -76.5% |
| `word-count` | 2253620 | LLGo · deadcode drop | 529235 | -76.5% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 968859 | -57.0% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 667045 | -70.4% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 4.738x | 10 |
| LLGo · deadcode drop | 4.738x | 10 |
| LLGo · full LTO (GlobalDCE off) | 7.860x | 10 |
| LLGo · full LTO + GlobalDCE | 5.451x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 543832 | +462.0% |
| `base64` | 96760 | LLGo · deadcode drop | 543832 | +462.0% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 885162 | +814.8% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 597535 | +517.5% |
| `checksum` | 92685 | LLGo · no LTO | 530208 | +472.1% |
| `checksum` | 92685 | LLGo · deadcode drop | 530208 | +472.1% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 869292 | +837.9% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 578576 | +524.2% |
| `conv-wasi` | 201149 | LLGo · no LTO | 866051 | +330.6% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 866051 | +330.6% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1606721 | +698.8% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 999911 | +397.1% |
| `fibonacci` | 62386 | LLGo · no LTO | 446918 | +616.4% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 446918 | +616.4% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 474065 | +659.9% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 432843 | +593.8% |
| `grep` | 303772 | LLGo · no LTO | 880071 | +189.7% |
| `grep` | 303772 | LLGo · deadcode drop | 880071 | +189.7% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1371230 | +351.4% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 970741 | +219.6% |
| `glob` | 93153 | LLGo · no LTO | 535909 | +475.3% |
| `glob` | 93153 | LLGo · deadcode drop | 535909 | +475.3% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1016932 | +991.7% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 684259 | +634.6% |
| `json-wasi` | 493590 | LLGo · no LTO | 1408148 | +185.3% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1408148 | +185.3% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2580402 | +422.8% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1700144 | +244.4% |
| `llimport` | — | LLGo · no LTO | 6634226 | — |
| `llimport` | — | LLGo · deadcode drop | 6634226 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 7041159 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6767946 | — |
| `path-report` | 116889 | LLGo · no LTO | 646725 | +453.3% |
| `path-report` | 116889 | LLGo · deadcode drop | 646725 | +453.3% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1130879 | +867.5% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 797737 | +582.5% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1029795 | +258.3% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1029795 | +258.3% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1786421 | +521.5% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1180837 | +310.8% |
| `word-count` | 86834 | LLGo · no LTO | 529235 | +509.5% |
| `word-count` | 86834 | LLGo · deadcode drop | 529235 | +509.5% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 968859 | +1015.8% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 667045 | +668.2% |
