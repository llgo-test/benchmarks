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
| `base64` | 2322402 | LLGo · no LTO | 1909513 | -17.8% |
| `base64` | 2322402 | LLGo · deadcode drop | 1076237 | -53.7% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1714230 | -26.2% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1093644 | -52.9% |
| `checksum` | 2311672 | LLGo · no LTO | 1890233 | -18.2% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1061388 | -54.1% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1678483 | -27.4% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1060287 | -54.1% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2759143 | +4.6% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1541012 | -41.6% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2570196 | -2.6% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1618102 | -38.7% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1183645 | -48.0% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 951825 | -58.2% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1000316 | -56.0% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 867918 | -61.8% |
| `grep` | 2871426 | LLGo · no LTO | 2565190 | -10.7% |
| `grep` | 2871426 | LLGo · deadcode drop | 1579851 | -45.0% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2299792 | -19.9% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1599935 | -44.3% |
| `glob` | 2305059 | LLGo · no LTO | 1940828 | -15.8% |
| `glob` | 2305059 | LLGo · deadcode drop | 1080802 | -53.1% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1817584 | -21.1% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1180580 | -48.8% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4054624 | +21.5% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2268823 | -32.0% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3856902 | +15.5% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2559173 | -23.3% |
| `llimport` | 8440671 | LLGo · no LTO | 10918517 | +29.4% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9253885 | +9.6% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10308120 | +22.1% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 9217100 | +9.2% |
| `path-report` | 2428068 | LLGo · no LTO | 2084645 | -14.1% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1212206 | -50.1% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 1954089 | -19.5% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1318016 | -45.7% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3101508 | +10.3% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1846132 | -34.3% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2920961 | +3.9% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1962232 | -30.2% |
| `word-count` | 2300998 | LLGo · no LTO | 1899783 | -17.4% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1056933 | -54.1% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1772676 | -23.0% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1146097 | -50.2% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.301x | 10 |
| LLGo · deadcode drop | 6.686x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.344x | 10 |
| LLGo · full LTO + GlobalDCE | 6.971x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1909513 | +1008.2% |
| `base64` | 172302 | LLGo · deadcode drop | 1076237 | +524.6% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1714230 | +894.9% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1093644 | +534.7% |
| `checksum` | 169609 | LLGo · no LTO | 1890233 | +1014.5% |
| `checksum` | 169609 | LLGo · deadcode drop | 1061388 | +525.8% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1678483 | +889.6% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1060287 | +525.1% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2759143 | +1568.3% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1541012 | +831.8% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2570196 | +1454.1% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1618102 | +878.4% |
| `fibonacci` | 141855 | LLGo · no LTO | 1183645 | +734.4% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 951825 | +571.0% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1000316 | +605.2% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 867918 | +511.8% |
| `grep` | 155984 | LLGo · no LTO | 2565190 | +1544.5% |
| `grep` | 155984 | LLGo · deadcode drop | 1579851 | +912.8% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2299792 | +1374.4% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1599935 | +925.7% |
| `glob` | 136553 | LLGo · no LTO | 1940828 | +1321.3% |
| `glob` | 136553 | LLGo · deadcode drop | 1080802 | +691.5% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1817584 | +1231.0% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1180580 | +764.6% |
| `json-wasi` | 525666 | LLGo · no LTO | 4054624 | +671.3% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2268823 | +331.6% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3856902 | +633.7% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2559173 | +386.8% |
| `llimport` | — | LLGo · no LTO | 10918517 | — |
| `llimport` | — | LLGo · deadcode drop | 9253885 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10308120 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 9217100 | — |
| `path-report` | 194133 | LLGo · no LTO | 2084645 | +973.8% |
| `path-report` | 194133 | LLGo · deadcode drop | 1212206 | +524.4% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 1954089 | +906.6% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1318016 | +578.9% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3101508 | +781.2% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1846132 | +424.5% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2920961 | +729.9% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1962232 | +457.5% |
| `word-count` | 164053 | LLGo · no LTO | 1899783 | +1058.0% |
| `word-count` | 164053 | LLGo · deadcode drop | 1056933 | +544.3% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1772676 | +980.6% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1146097 | +598.6% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.305x | 11 |
| LLGo · deadcode drop | 0.305x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.487x | 11 |
| LLGo · full LTO + GlobalDCE | 0.348x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 543789 | -76.1% |
| `base64` | 2275731 | LLGo · deadcode drop | 543789 | -76.1% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 885139 | -61.1% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 597512 | -73.7% |
| `checksum` | 2264417 | LLGo · no LTO | 530165 | -76.6% |
| `checksum` | 2264417 | LLGo · deadcode drop | 530165 | -76.6% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 869269 | -61.6% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 578553 | -74.5% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 866008 | -66.8% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 866008 | -66.8% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1606698 | -38.4% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 999888 | -61.7% |
| `fibonacci` | 2230899 | LLGo · no LTO | 446875 | -80.0% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 446875 | -80.0% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 474042 | -78.8% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 432820 | -80.6% |
| `grep` | 2848917 | LLGo · no LTO | 880028 | -69.1% |
| `grep` | 2848917 | LLGo · deadcode drop | 880028 | -69.1% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1371207 | -51.9% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 970718 | -65.9% |
| `glob` | 2257634 | LLGo · no LTO | 535866 | -76.3% |
| `glob` | 2257634 | LLGo · deadcode drop | 535866 | -76.3% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1016909 | -55.0% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 684236 | -69.7% |
| `json-wasi` | 3314587 | LLGo · no LTO | 1408105 | -57.5% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1408105 | -57.5% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2580379 | -22.2% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1700121 | -48.7% |
| `llimport` | 8423078 | LLGo · no LTO | 6634183 | -21.2% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6634183 | -21.2% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 7041136 | -16.4% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6767923 | -19.7% |
| `path-report` | 2381190 | LLGo · no LTO | 646682 | -72.8% |
| `path-report` | 2381190 | LLGo · deadcode drop | 646682 | -72.8% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1130856 | -52.5% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 797714 | -66.5% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1029752 | -63.0% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1029752 | -63.0% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1786398 | -35.8% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1180814 | -57.5% |
| `word-count` | 2253620 | LLGo · no LTO | 529192 | -76.5% |
| `word-count` | 2253620 | LLGo · deadcode drop | 529192 | -76.5% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 968836 | -57.0% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 667022 | -70.4% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 4.737x | 10 |
| LLGo · deadcode drop | 4.737x | 10 |
| LLGo · full LTO (GlobalDCE off) | 7.860x | 10 |
| LLGo · full LTO + GlobalDCE | 5.451x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 543789 | +462.0% |
| `base64` | 96760 | LLGo · deadcode drop | 543789 | +462.0% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 885139 | +814.8% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 597512 | +517.5% |
| `checksum` | 92685 | LLGo · no LTO | 530165 | +472.0% |
| `checksum` | 92685 | LLGo · deadcode drop | 530165 | +472.0% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 869269 | +837.9% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 578553 | +524.2% |
| `conv-wasi` | 201149 | LLGo · no LTO | 866008 | +330.5% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 866008 | +330.5% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1606698 | +698.8% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 999888 | +397.1% |
| `fibonacci` | 62386 | LLGo · no LTO | 446875 | +616.3% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 446875 | +616.3% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 474042 | +659.9% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 432820 | +593.8% |
| `grep` | 303772 | LLGo · no LTO | 880028 | +189.7% |
| `grep` | 303772 | LLGo · deadcode drop | 880028 | +189.7% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1371207 | +351.4% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 970718 | +219.6% |
| `glob` | 93153 | LLGo · no LTO | 535866 | +475.3% |
| `glob` | 93153 | LLGo · deadcode drop | 535866 | +475.3% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1016909 | +991.7% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 684236 | +634.5% |
| `json-wasi` | 493590 | LLGo · no LTO | 1408105 | +185.3% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1408105 | +185.3% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2580379 | +422.8% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1700121 | +244.4% |
| `llimport` | — | LLGo · no LTO | 6634183 | — |
| `llimport` | — | LLGo · deadcode drop | 6634183 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 7041136 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6767923 | — |
| `path-report` | 116889 | LLGo · no LTO | 646682 | +453.2% |
| `path-report` | 116889 | LLGo · deadcode drop | 646682 | +453.2% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1130856 | +867.5% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 797714 | +582.5% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1029752 | +258.2% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1029752 | +258.2% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1786398 | +521.5% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1180814 | +310.8% |
| `word-count` | 86834 | LLGo · no LTO | 529192 | +509.4% |
| `word-count` | 86834 | LLGo · deadcode drop | 529192 | +509.4% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 968836 | +1015.7% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 667022 | +668.2% |
