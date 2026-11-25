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
| LLGo · no LTO | 0.912x | 11 |
| LLGo · deadcode drop | 0.558x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.812x | 11 |
| LLGo · full LTO + GlobalDCE | 0.565x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1909459 | -17.8% |
| `base64` | 2322402 | LLGo · deadcode drop | 1074648 | -53.7% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1665624 | -28.3% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1071415 | -53.9% |
| `checksum` | 2311672 | LLGo · no LTO | 1890690 | -18.2% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1060291 | -54.1% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1631203 | -29.4% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1039050 | -55.1% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2818083 | +6.8% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1586178 | -39.9% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2543906 | -3.6% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1624887 | -38.4% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1187453 | -47.8% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 952161 | -58.1% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 986226 | -56.6% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 855172 | -62.4% |
| `grep` | 2871426 | LLGo · no LTO | 2570970 | -10.5% |
| `grep` | 2871426 | LLGo · deadcode drop | 1581357 | -44.9% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2231159 | -22.3% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1557116 | -45.8% |
| `glob` | 2305059 | LLGo · no LTO | 1940543 | -15.8% |
| `glob` | 2305059 | LLGo · deadcode drop | 1079145 | -53.2% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1755644 | -23.8% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1144473 | -50.3% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4115279 | +23.3% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2317321 | -30.6% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3799619 | +13.8% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2543325 | -23.8% |
| `llimport` | 8440671 | LLGo · no LTO | 10958640 | +29.8% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9308905 | +10.3% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10059300 | +19.2% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 9016513 | +6.8% |
| `path-report` | 2428068 | LLGo · no LTO | 2084215 | -14.2% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1210451 | -50.1% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 1884362 | -22.4% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1274238 | -47.5% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3167522 | +12.7% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1891597 | -32.7% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2891178 | +2.8% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1966313 | -30.1% |
| `word-count` | 2300998 | LLGo · no LTO | 1900376 | -17.4% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1056158 | -54.1% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1713218 | -25.5% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1112334 | -51.7% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.372x | 10 |
| LLGo · deadcode drop | 6.732x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.096x | 10 |
| LLGo · full LTO + GlobalDCE | 6.849x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1909459 | +1008.2% |
| `base64` | 172302 | LLGo · deadcode drop | 1074648 | +523.7% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1665624 | +866.7% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1071415 | +521.8% |
| `checksum` | 169609 | LLGo · no LTO | 1890690 | +1014.7% |
| `checksum` | 169609 | LLGo · deadcode drop | 1060291 | +525.1% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1631203 | +861.7% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1039050 | +512.6% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2818083 | +1604.0% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1586178 | +859.1% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2543906 | +1438.2% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1624887 | +882.5% |
| `fibonacci` | 141855 | LLGo · no LTO | 1187453 | +737.1% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 952161 | +571.2% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 986226 | +595.2% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 855172 | +502.8% |
| `grep` | 155984 | LLGo · no LTO | 2570970 | +1548.2% |
| `grep` | 155984 | LLGo · deadcode drop | 1581357 | +913.8% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2231159 | +1330.4% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1557116 | +898.3% |
| `glob` | 136553 | LLGo · no LTO | 1940543 | +1321.1% |
| `glob` | 136553 | LLGo · deadcode drop | 1079145 | +690.3% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1755644 | +1185.7% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1144473 | +738.1% |
| `json-wasi` | 525666 | LLGo · no LTO | 4115279 | +682.9% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2317321 | +340.8% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3799619 | +622.8% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2543325 | +383.8% |
| `llimport` | — | LLGo · no LTO | 10958640 | — |
| `llimport` | — | LLGo · deadcode drop | 9308905 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10059300 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 9016513 | — |
| `path-report` | 194133 | LLGo · no LTO | 2084215 | +973.6% |
| `path-report` | 194133 | LLGo · deadcode drop | 1210451 | +523.5% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 1884362 | +870.7% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1274238 | +556.4% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3167522 | +799.9% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1891597 | +437.4% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2891178 | +721.4% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1966313 | +458.7% |
| `word-count` | 164053 | LLGo · no LTO | 1900376 | +1058.4% |
| `word-count` | 164053 | LLGo · deadcode drop | 1056158 | +543.8% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1713218 | +944.3% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1112334 | +578.0% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.310x | 11 |
| LLGo · deadcode drop | 0.310x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.472x | 11 |
| LLGo · full LTO + GlobalDCE | 0.339x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 544654 | -76.1% |
| `base64` | 2275731 | LLGo · deadcode drop | 544654 | -76.1% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 853823 | -62.5% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 579401 | -74.5% |
| `checksum` | 2264417 | LLGo · no LTO | 531450 | -76.5% |
| `checksum` | 2264417 | LLGo · deadcode drop | 531450 | -76.5% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 838373 | -63.0% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 560905 | -75.2% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 902245 | -65.4% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 902245 | -65.4% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1575918 | -39.6% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1001435 | -61.6% |
| `fibonacci` | 2230899 | LLGo · no LTO | 448759 | -79.9% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 448759 | -79.9% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 467047 | -79.1% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 422766 | -81.0% |
| `grep` | 2848917 | LLGo · no LTO | 884355 | -69.0% |
| `grep` | 2848917 | LLGo · deadcode drop | 884355 | -69.0% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1321765 | -53.6% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 932494 | -67.3% |
| `glob` | 2257634 | LLGo · no LTO | 536756 | -76.2% |
| `glob` | 2257634 | LLGo · deadcode drop | 536756 | -76.2% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 972579 | -56.9% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 653158 | -71.1% |
| `json-wasi` | 3314587 | LLGo · no LTO | 1451521 | -56.2% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1451521 | -56.2% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2522791 | -23.9% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1683498 | -49.2% |
| `llimport` | 8423078 | LLGo · no LTO | 6764578 | -19.7% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6764578 | -19.7% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 6919380 | -17.9% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6660878 | -20.9% |
| `path-report` | 2381190 | LLGo · no LTO | 647642 | -72.8% |
| `path-report` | 2381190 | LLGo · deadcode drop | 647642 | -72.8% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1079839 | -54.7% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 759986 | -68.1% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1069880 | -61.5% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1069880 | -61.5% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1757072 | -36.8% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1183354 | -57.4% |
| `word-count` | 2253620 | LLGo · no LTO | 530681 | -76.5% |
| `word-count` | 2253620 | LLGo · deadcode drop | 530681 | -76.5% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 926702 | -58.9% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 637922 | -71.7% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 4.799x | 10 |
| LLGo · deadcode drop | 4.799x | 10 |
| LLGo · full LTO (GlobalDCE off) | 7.614x | 10 |
| LLGo · full LTO + GlobalDCE | 5.305x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 544654 | +462.9% |
| `base64` | 96760 | LLGo · deadcode drop | 544654 | +462.9% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 853823 | +782.4% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 579401 | +498.8% |
| `checksum` | 92685 | LLGo · no LTO | 531450 | +473.4% |
| `checksum` | 92685 | LLGo · deadcode drop | 531450 | +473.4% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 838373 | +804.5% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 560905 | +505.2% |
| `conv-wasi` | 201149 | LLGo · no LTO | 902245 | +348.5% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 902245 | +348.5% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1575918 | +683.5% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1001435 | +397.9% |
| `fibonacci` | 62386 | LLGo · no LTO | 448759 | +619.3% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 448759 | +619.3% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 467047 | +648.6% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 422766 | +577.7% |
| `grep` | 303772 | LLGo · no LTO | 884355 | +191.1% |
| `grep` | 303772 | LLGo · deadcode drop | 884355 | +191.1% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1321765 | +335.1% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 932494 | +207.0% |
| `glob` | 93153 | LLGo · no LTO | 536756 | +476.2% |
| `glob` | 93153 | LLGo · deadcode drop | 536756 | +476.2% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 972579 | +944.1% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 653158 | +601.2% |
| `json-wasi` | 493590 | LLGo · no LTO | 1451521 | +194.1% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1451521 | +194.1% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2522791 | +411.1% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1683498 | +241.1% |
| `llimport` | — | LLGo · no LTO | 6764578 | — |
| `llimport` | — | LLGo · deadcode drop | 6764578 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 6919380 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6660878 | — |
| `path-report` | 116889 | LLGo · no LTO | 647642 | +454.1% |
| `path-report` | 116889 | LLGo · deadcode drop | 647642 | +454.1% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1079839 | +823.8% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 759986 | +550.2% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1069880 | +272.2% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1069880 | +272.2% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1757072 | +511.3% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1183354 | +311.7% |
| `word-count` | 86834 | LLGo · no LTO | 530681 | +511.1% |
| `word-count` | 86834 | LLGo · deadcode drop | 530681 | +511.1% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 926702 | +967.2% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 637922 | +634.6% |
