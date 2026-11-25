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
| LLGo · no LTO | 0.909x | 11 |
| LLGo · deadcode drop | 0.556x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.809x | 11 |
| LLGo · full LTO + GlobalDCE | 0.562x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1904579 | -18.0% |
| `base64` | 2322402 | LLGo · deadcode drop | 1073275 | -53.8% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1660798 | -28.5% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1068171 | -54.0% |
| `checksum` | 2311672 | LLGo · no LTO | 1885225 | -18.4% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1058405 | -54.2% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1625753 | -29.7% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1035173 | -55.2% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2805785 | +6.3% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1578170 | -40.2% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2531896 | -4.0% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1613901 | -38.8% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1184731 | -47.9% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 949078 | -58.3% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 983885 | -56.7% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 852839 | -62.5% |
| `grep` | 2871426 | LLGo · no LTO | 2559047 | -10.9% |
| `grep` | 2871426 | LLGo · deadcode drop | 1575351 | -45.1% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2219802 | -22.7% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1549365 | -46.0% |
| `glob` | 2305059 | LLGo · no LTO | 1935776 | -16.0% |
| `glob` | 2305059 | LLGo · deadcode drop | 1077765 | -53.2% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1750817 | -24.0% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1141220 | -50.5% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4098702 | +22.8% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2305621 | -30.9% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3783615 | +13.3% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2527908 | -24.3% |
| `llimport` | 8440671 | LLGo · no LTO | 10915259 | +29.3% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9267290 | +9.8% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10018554 | +18.7% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 8976903 | +6.4% |
| `path-report` | 2428068 | LLGo · no LTO | 2079079 | -14.4% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1208704 | -50.2% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 1879227 | -22.6% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1270640 | -47.7% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3153200 | +12.2% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1882517 | -33.0% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2877277 | +2.4% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1953331 | -30.5% |
| `word-count` | 2300998 | LLGo · no LTO | 1894902 | -17.6% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1054148 | -54.2% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1707742 | -25.8% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1108385 | -51.8% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.334x | 10 |
| LLGo · deadcode drop | 6.712x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.060x | 10 |
| LLGo · full LTO + GlobalDCE | 6.819x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1904579 | +1005.4% |
| `base64` | 172302 | LLGo · deadcode drop | 1073275 | +522.9% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1660798 | +863.9% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1068171 | +519.9% |
| `checksum` | 169609 | LLGo · no LTO | 1885225 | +1011.5% |
| `checksum` | 169609 | LLGo · deadcode drop | 1058405 | +524.0% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1625753 | +858.5% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1035173 | +510.3% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2805785 | +1596.5% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1578170 | +854.2% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2531896 | +1430.9% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1613901 | +875.8% |
| `fibonacci` | 141855 | LLGo · no LTO | 1184731 | +735.2% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 949078 | +569.0% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 983885 | +593.6% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 852839 | +501.2% |
| `grep` | 155984 | LLGo · no LTO | 2559047 | +1540.6% |
| `grep` | 155984 | LLGo · deadcode drop | 1575351 | +909.9% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2219802 | +1323.1% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1549365 | +893.3% |
| `glob` | 136553 | LLGo · no LTO | 1935776 | +1317.6% |
| `glob` | 136553 | LLGo · deadcode drop | 1077765 | +689.3% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1750817 | +1182.2% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1141220 | +735.7% |
| `json-wasi` | 525666 | LLGo · no LTO | 4098702 | +679.7% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2305621 | +338.6% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3783615 | +619.8% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2527908 | +380.9% |
| `llimport` | — | LLGo · no LTO | 10915259 | — |
| `llimport` | — | LLGo · deadcode drop | 9267290 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10018554 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 8976903 | — |
| `path-report` | 194133 | LLGo · no LTO | 2079079 | +971.0% |
| `path-report` | 194133 | LLGo · deadcode drop | 1208704 | +522.6% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 1879227 | +868.0% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1270640 | +554.5% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3153200 | +795.9% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1882517 | +434.9% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2877277 | +717.5% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1953331 | +455.0% |
| `word-count` | 164053 | LLGo · no LTO | 1894902 | +1055.1% |
| `word-count` | 164053 | LLGo · deadcode drop | 1054148 | +542.6% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1707742 | +941.0% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1108385 | +575.6% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.308x | 11 |
| LLGo · deadcode drop | 0.308x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.470x | 11 |
| LLGo · full LTO + GlobalDCE | 0.336x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 543005 | -76.1% |
| `base64` | 2275731 | LLGo · deadcode drop | 543005 | -76.1% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 851109 | -62.6% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 576231 | -74.7% |
| `checksum` | 2264417 | LLGo · no LTO | 529403 | -76.6% |
| `checksum` | 2264417 | LLGo · deadcode drop | 529403 | -76.6% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 835149 | -63.1% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 557339 | -75.4% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 895886 | -65.6% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 895886 | -65.6% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1566839 | -39.9% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 992943 | -61.9% |
| `fibonacci` | 2230899 | LLGo · no LTO | 445865 | -80.0% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 445865 | -80.0% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 465051 | -79.2% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 420219 | -81.2% |
| `grep` | 2848917 | LLGo · no LTO | 879239 | -69.1% |
| `grep` | 2848917 | LLGo · deadcode drop | 879239 | -69.1% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1312890 | -53.9% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 926208 | -67.5% |
| `glob` | 2257634 | LLGo · no LTO | 535109 | -76.3% |
| `glob` | 2257634 | LLGo · deadcode drop | 535109 | -76.3% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 969907 | -57.0% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 650002 | -71.2% |
| `json-wasi` | 3314587 | LLGo · no LTO | 1442509 | -56.5% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1442509 | -56.5% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2510918 | -24.2% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1672086 | -49.6% |
| `llimport` | 8423078 | LLGo · no LTO | 6720695 | -20.2% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6720695 | -20.2% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 6879275 | -18.3% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6617894 | -21.4% |
| `path-report` | 2381190 | LLGo · no LTO | 645779 | -72.9% |
| `path-report` | 2381190 | LLGo · deadcode drop | 645779 | -72.9% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1076955 | -54.8% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 756618 | -68.2% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1062742 | -61.8% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1062742 | -61.8% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1746321 | -37.2% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1173085 | -57.8% |
| `word-count` | 2253620 | LLGo · no LTO | 528505 | -76.5% |
| `word-count` | 2253620 | LLGo · deadcode drop | 528505 | -76.5% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 923454 | -59.0% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 634234 | -71.9% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 4.775x | 10 |
| LLGo · deadcode drop | 4.775x | 10 |
| LLGo · full LTO (GlobalDCE off) | 7.581x | 10 |
| LLGo · full LTO + GlobalDCE | 5.271x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 543005 | +461.2% |
| `base64` | 96760 | LLGo · deadcode drop | 543005 | +461.2% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 851109 | +779.6% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 576231 | +495.5% |
| `checksum` | 92685 | LLGo · no LTO | 529403 | +471.2% |
| `checksum` | 92685 | LLGo · deadcode drop | 529403 | +471.2% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 835149 | +801.1% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 557339 | +501.3% |
| `conv-wasi` | 201149 | LLGo · no LTO | 895886 | +345.4% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 895886 | +345.4% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1566839 | +678.9% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 992943 | +393.6% |
| `fibonacci` | 62386 | LLGo · no LTO | 445865 | +614.7% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 445865 | +614.7% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 465051 | +645.4% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 420219 | +573.6% |
| `grep` | 303772 | LLGo · no LTO | 879239 | +189.4% |
| `grep` | 303772 | LLGo · deadcode drop | 879239 | +189.4% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1312890 | +332.2% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 926208 | +204.9% |
| `glob` | 93153 | LLGo · no LTO | 535109 | +474.4% |
| `glob` | 93153 | LLGo · deadcode drop | 535109 | +474.4% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 969907 | +941.2% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 650002 | +597.8% |
| `json-wasi` | 493590 | LLGo · no LTO | 1442509 | +192.2% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1442509 | +192.2% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2510918 | +408.7% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1672086 | +238.8% |
| `llimport` | — | LLGo · no LTO | 6720695 | — |
| `llimport` | — | LLGo · deadcode drop | 6720695 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 6879275 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6617894 | — |
| `path-report` | 116889 | LLGo · no LTO | 645779 | +452.5% |
| `path-report` | 116889 | LLGo · deadcode drop | 645779 | +452.5% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1076955 | +821.3% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 756618 | +547.3% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1062742 | +269.7% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1062742 | +269.7% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1746321 | +507.5% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1173085 | +308.1% |
| `word-count` | 86834 | LLGo · no LTO | 528505 | +508.6% |
| `word-count` | 86834 | LLGo · deadcode drop | 528505 | +508.6% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 923454 | +963.5% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 634234 | +630.4% |
