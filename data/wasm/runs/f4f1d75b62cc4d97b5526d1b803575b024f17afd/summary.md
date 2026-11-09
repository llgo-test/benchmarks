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
| LLGo · no LTO | 0.927x | 11 |
| LLGo · deadcode drop | 0.528x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.834x | 11 |
| LLGo · full LTO + GlobalDCE | 0.567x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1888652 | -18.7% |
| `base64` | 2322402 | LLGo · deadcode drop | 1018828 | -56.1% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1653420 | -28.8% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1063258 | -54.2% |
| `checksum` | 2311672 | LLGo · no LTO | 1869074 | -19.1% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1004541 | -56.5% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1617655 | -30.0% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1030448 | -55.4% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2735142 | +3.7% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1469468 | -44.3% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2496378 | -5.4% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1582758 | -40.0% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1670222 | -26.6% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 897811 | -60.5% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1436800 | -36.8% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 975657 | -57.1% |
| `grep` | 2871426 | LLGo · no LTO | 2542969 | -11.4% |
| `grep` | 2871426 | LLGo · deadcode drop | 1513927 | -47.3% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2222979 | -22.6% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1558980 | -45.7% |
| `glob` | 2305059 | LLGo · no LTO | 1919638 | -16.7% |
| `glob` | 2305059 | LLGo · deadcode drop | 1025325 | -55.5% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1755997 | -23.8% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1152042 | -50.0% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4031044 | +20.7% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2189499 | -34.4% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3745008 | +12.2% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2506312 | -24.9% |
| `llimport` | 8440671 | LLGo · no LTO | 10920904 | +29.4% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9035586 | +7.0% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 9944812 | +17.8% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 8877282 | +5.2% |
| `path-report` | 2428068 | LLGo · no LTO | 2058392 | -15.2% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1148925 | -52.7% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 1884655 | -22.4% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1281093 | -47.2% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3063523 | +9.0% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1754235 | -37.6% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2825473 | +0.5% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1904635 | -32.2% |
| `word-count` | 2300998 | LLGo · no LTO | 1879180 | -18.3% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1001767 | -56.5% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1715154 | -25.5% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1120432 | -51.3% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.589x | 10 |
| LLGo · deadcode drop | 6.356x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.406x | 10 |
| LLGo · full LTO + GlobalDCE | 6.892x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1888652 | +996.1% |
| `base64` | 172302 | LLGo · deadcode drop | 1018828 | +491.3% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1653420 | +859.6% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1063258 | +517.1% |
| `checksum` | 169609 | LLGo · no LTO | 1869074 | +1002.0% |
| `checksum` | 169609 | LLGo · deadcode drop | 1004541 | +492.3% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1617655 | +853.8% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1030448 | +507.5% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2735142 | +1553.8% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1469468 | +788.5% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2496378 | +1409.4% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1582758 | +857.0% |
| `fibonacci` | 141855 | LLGo · no LTO | 1670222 | +1077.4% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 897811 | +532.9% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1436800 | +912.9% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 975657 | +587.8% |
| `grep` | 155984 | LLGo · no LTO | 2542969 | +1530.3% |
| `grep` | 155984 | LLGo · deadcode drop | 1513927 | +870.6% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2222979 | +1325.1% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1558980 | +899.4% |
| `glob` | 136553 | LLGo · no LTO | 1919638 | +1305.8% |
| `glob` | 136553 | LLGo · deadcode drop | 1025325 | +650.9% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1755997 | +1185.9% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1152042 | +743.7% |
| `json-wasi` | 525666 | LLGo · no LTO | 4031044 | +666.8% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2189499 | +316.5% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3745008 | +612.4% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2506312 | +376.8% |
| `llimport` | — | LLGo · no LTO | 10920904 | — |
| `llimport` | — | LLGo · deadcode drop | 9035586 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 9944812 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 8877282 | — |
| `path-report` | 194133 | LLGo · no LTO | 2058392 | +960.3% |
| `path-report` | 194133 | LLGo · deadcode drop | 1148925 | +491.8% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 1884655 | +870.8% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1281093 | +559.9% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3063523 | +770.4% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1754235 | +398.4% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2825473 | +702.8% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1904635 | +441.1% |
| `word-count` | 164053 | LLGo · no LTO | 1879180 | +1045.5% |
| `word-count` | 164053 | LLGo · deadcode drop | 1001767 | +510.6% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1715154 | +945.5% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1120432 | +583.0% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.562x | 11 |
| LLGo · deadcode drop | 0.284x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.483x | 11 |
| LLGo · full LTO + GlobalDCE | 0.339x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1079070 | -52.6% |
| `base64` | 2275731 | LLGo · deadcode drop | 501357 | -78.0% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 835897 | -63.3% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 567844 | -75.0% |
| `checksum` | 2264417 | LLGo · no LTO | 1063573 | -53.0% |
| `checksum` | 2264417 | LLGo · deadcode drop | 488455 | -78.4% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 820756 | -63.8% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 549742 | -75.7% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 1665484 | -36.1% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 802328 | -69.2% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1530718 | -41.3% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 958820 | -63.2% |
| `fibonacci` | 2230899 | LLGo · no LTO | 877198 | -60.7% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 406364 | -81.8% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 723514 | -67.6% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 507359 | -77.3% |
| `grep` | 2848917 | LLGo · no LTO | 1514051 | -46.9% |
| `grep` | 2848917 | LLGo · deadcode drop | 828595 | -70.9% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1314042 | -53.9% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 940613 | -67.0% |
| `glob` | 2257634 | LLGo · no LTO | 1095202 | -51.5% |
| `glob` | 2257634 | LLGo · deadcode drop | 495572 | -78.0% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 966758 | -57.2% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 656768 | -70.9% |
| `json-wasi` | 3314587 | LLGo · no LTO | 2674385 | -19.3% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1318560 | -60.2% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2446802 | -26.2% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1625216 | -51.0% |
| `llimport` | 8423078 | LLGo · no LTO | 7955928 | -5.5% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6502577 | -22.8% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 6772975 | -19.6% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6542720 | -22.3% |
| `path-report` | 2381190 | LLGo · no LTO | 1208759 | -49.2% |
| `path-report` | 2381190 | LLGo · deadcode drop | 597891 | -74.9% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1072762 | -54.9% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 762631 | -68.0% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1855874 | -33.3% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 962238 | -65.4% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1701922 | -38.8% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1131188 | -59.3% |
| `word-count` | 2253620 | LLGo · no LTO | 1076016 | -52.3% |
| `word-count` | 2253620 | LLGo · deadcode drop | 488473 | -78.3% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 923536 | -59.0% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 642183 | -71.5% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 9.105x | 10 |
| LLGo · deadcode drop | 4.388x | 10 |
| LLGo · full LTO (GlobalDCE off) | 7.832x | 10 |
| LLGo · full LTO + GlobalDCE | 5.328x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1079070 | +1015.2% |
| `base64` | 96760 | LLGo · deadcode drop | 501357 | +418.1% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 835897 | +763.9% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 567844 | +486.9% |
| `checksum` | 92685 | LLGo · no LTO | 1063573 | +1047.5% |
| `checksum` | 92685 | LLGo · deadcode drop | 488455 | +427.0% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 820756 | +785.5% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 549742 | +493.1% |
| `conv-wasi` | 201149 | LLGo · no LTO | 1665484 | +728.0% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 802328 | +298.9% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1530718 | +661.0% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 958820 | +376.7% |
| `fibonacci` | 62386 | LLGo · no LTO | 877198 | +1306.1% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 406364 | +551.4% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 723514 | +1059.7% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 507359 | +713.3% |
| `grep` | 303772 | LLGo · no LTO | 1514051 | +398.4% |
| `grep` | 303772 | LLGo · deadcode drop | 828595 | +172.8% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1314042 | +332.6% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 940613 | +209.6% |
| `glob` | 93153 | LLGo · no LTO | 1095202 | +1075.7% |
| `glob` | 93153 | LLGo · deadcode drop | 495572 | +432.0% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 966758 | +937.8% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 656768 | +605.0% |
| `json-wasi` | 493590 | LLGo · no LTO | 2674385 | +441.8% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1318560 | +167.1% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2446802 | +395.7% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1625216 | +229.3% |
| `llimport` | — | LLGo · no LTO | 7955928 | — |
| `llimport` | — | LLGo · deadcode drop | 6502577 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 6772975 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6542720 | — |
| `path-report` | 116889 | LLGo · no LTO | 1208759 | +934.1% |
| `path-report` | 116889 | LLGo · deadcode drop | 597891 | +411.5% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1072762 | +817.8% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 762631 | +552.4% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1855874 | +545.6% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 962238 | +234.8% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1701922 | +492.1% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1131188 | +293.5% |
| `word-count` | 86834 | LLGo · no LTO | 1076016 | +1139.2% |
| `word-count` | 86834 | LLGo · deadcode drop | 488473 | +462.5% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 923536 | +963.6% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 642183 | +639.6% |
