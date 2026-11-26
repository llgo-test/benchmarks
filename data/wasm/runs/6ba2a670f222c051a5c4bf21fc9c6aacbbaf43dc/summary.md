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
| `base64` | 2322402 | LLGo · no LTO | 1909522 | -17.8% |
| `base64` | 2322402 | LLGo · deadcode drop | 1074721 | -53.7% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1665669 | -28.3% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1071462 | -53.9% |
| `checksum` | 2311672 | LLGo · no LTO | 1890753 | -18.2% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1060364 | -54.1% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1631248 | -29.4% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1039097 | -55.0% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2818148 | +6.8% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1586251 | -39.9% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2543951 | -3.6% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1624934 | -38.4% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1187522 | -47.8% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 952222 | -58.1% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 986271 | -56.6% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 855219 | -62.4% |
| `grep` | 2871426 | LLGo · no LTO | 2571033 | -10.5% |
| `grep` | 2871426 | LLGo · deadcode drop | 1581430 | -44.9% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2231204 | -22.3% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1557163 | -45.8% |
| `glob` | 2305059 | LLGo · no LTO | 1940606 | -15.8% |
| `glob` | 2305059 | LLGo · deadcode drop | 1079218 | -53.2% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1755689 | -23.8% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1144520 | -50.3% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4115344 | +23.3% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2317392 | -30.6% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3799664 | +13.8% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2543372 | -23.8% |
| `llimport` | 8440671 | LLGo · no LTO | 10958705 | +29.8% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9308976 | +10.3% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10059343 | +19.2% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 9016558 | +6.8% |
| `path-report` | 2428068 | LLGo · no LTO | 2084278 | -14.2% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1210524 | -50.1% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 1884407 | -22.4% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1274285 | -47.5% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3167587 | +12.7% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1891670 | -32.7% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2891223 | +2.8% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1966360 | -30.1% |
| `word-count` | 2300998 | LLGo · no LTO | 1900439 | -17.4% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1056231 | -54.1% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1713263 | -25.5% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1112381 | -51.7% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.372x | 10 |
| LLGo · deadcode drop | 6.733x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.096x | 10 |
| LLGo · full LTO + GlobalDCE | 6.849x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1909522 | +1008.2% |
| `base64` | 172302 | LLGo · deadcode drop | 1074721 | +523.7% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1665669 | +866.7% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1071462 | +521.9% |
| `checksum` | 169609 | LLGo · no LTO | 1890753 | +1014.8% |
| `checksum` | 169609 | LLGo · deadcode drop | 1060364 | +525.2% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1631248 | +861.8% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1039097 | +512.6% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2818148 | +1604.0% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1586251 | +859.1% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2543951 | +1438.2% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1624934 | +882.5% |
| `fibonacci` | 141855 | LLGo · no LTO | 1187522 | +737.1% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 952222 | +571.3% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 986271 | +595.3% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 855219 | +502.9% |
| `grep` | 155984 | LLGo · no LTO | 2571033 | +1548.3% |
| `grep` | 155984 | LLGo · deadcode drop | 1581430 | +913.8% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2231204 | +1330.4% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1557163 | +898.3% |
| `glob` | 136553 | LLGo · no LTO | 1940606 | +1321.1% |
| `glob` | 136553 | LLGo · deadcode drop | 1079218 | +690.3% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1755689 | +1185.7% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1144520 | +738.2% |
| `json-wasi` | 525666 | LLGo · no LTO | 4115344 | +682.9% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2317392 | +340.8% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3799664 | +622.8% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2543372 | +383.8% |
| `llimport` | — | LLGo · no LTO | 10958705 | — |
| `llimport` | — | LLGo · deadcode drop | 9308976 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10059343 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 9016558 | — |
| `path-report` | 194133 | LLGo · no LTO | 2084278 | +973.6% |
| `path-report` | 194133 | LLGo · deadcode drop | 1210524 | +523.6% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 1884407 | +870.7% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1274285 | +556.4% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3167587 | +800.0% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1891670 | +437.5% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2891223 | +721.4% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1966360 | +458.7% |
| `word-count` | 164053 | LLGo · no LTO | 1900439 | +1058.4% |
| `word-count` | 164053 | LLGo · deadcode drop | 1056231 | +543.8% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1713263 | +944.3% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1112381 | +578.1% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.310x | 11 |
| LLGo · deadcode drop | 0.310x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.472x | 11 |
| LLGo · full LTO + GlobalDCE | 0.339x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 544693 | -76.1% |
| `base64` | 2275731 | LLGo · deadcode drop | 544693 | -76.1% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 853862 | -62.5% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 579440 | -74.5% |
| `checksum` | 2264417 | LLGo · no LTO | 531489 | -76.5% |
| `checksum` | 2264417 | LLGo · deadcode drop | 531489 | -76.5% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 838412 | -63.0% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 560944 | -75.2% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 902284 | -65.4% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 902284 | -65.4% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1575957 | -39.6% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1001474 | -61.6% |
| `fibonacci` | 2230899 | LLGo · no LTO | 448798 | -79.9% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 448798 | -79.9% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 467086 | -79.1% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 422805 | -81.0% |
| `grep` | 2848917 | LLGo · no LTO | 884394 | -69.0% |
| `grep` | 2848917 | LLGo · deadcode drop | 884394 | -69.0% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1321804 | -53.6% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 932533 | -67.3% |
| `glob` | 2257634 | LLGo · no LTO | 536795 | -76.2% |
| `glob` | 2257634 | LLGo · deadcode drop | 536795 | -76.2% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 972618 | -56.9% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 653197 | -71.1% |
| `json-wasi` | 3314587 | LLGo · no LTO | 1451560 | -56.2% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1451560 | -56.2% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2522830 | -23.9% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1683537 | -49.2% |
| `llimport` | 8423078 | LLGo · no LTO | 6764617 | -19.7% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6764617 | -19.7% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 6919419 | -17.9% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6660917 | -20.9% |
| `path-report` | 2381190 | LLGo · no LTO | 647681 | -72.8% |
| `path-report` | 2381190 | LLGo · deadcode drop | 647681 | -72.8% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1079878 | -54.6% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 760025 | -68.1% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1069919 | -61.5% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1069919 | -61.5% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1757111 | -36.8% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1183393 | -57.4% |
| `word-count` | 2253620 | LLGo · no LTO | 530720 | -76.5% |
| `word-count` | 2253620 | LLGo · deadcode drop | 530720 | -76.5% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 926741 | -58.9% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 637961 | -71.7% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 4.799x | 10 |
| LLGo · deadcode drop | 4.799x | 10 |
| LLGo · full LTO (GlobalDCE off) | 7.615x | 10 |
| LLGo · full LTO + GlobalDCE | 5.305x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 544693 | +462.9% |
| `base64` | 96760 | LLGo · deadcode drop | 544693 | +462.9% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 853862 | +782.5% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 579440 | +498.8% |
| `checksum` | 92685 | LLGo · no LTO | 531489 | +473.4% |
| `checksum` | 92685 | LLGo · deadcode drop | 531489 | +473.4% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 838412 | +804.6% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 560944 | +505.2% |
| `conv-wasi` | 201149 | LLGo · no LTO | 902284 | +348.6% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 902284 | +348.6% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1575957 | +683.5% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1001474 | +397.9% |
| `fibonacci` | 62386 | LLGo · no LTO | 448798 | +619.4% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 448798 | +619.4% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 467086 | +648.7% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 422805 | +577.7% |
| `grep` | 303772 | LLGo · no LTO | 884394 | +191.1% |
| `grep` | 303772 | LLGo · deadcode drop | 884394 | +191.1% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1321804 | +335.1% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 932533 | +207.0% |
| `glob` | 93153 | LLGo · no LTO | 536795 | +476.3% |
| `glob` | 93153 | LLGo · deadcode drop | 536795 | +476.3% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 972618 | +944.1% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 653197 | +601.2% |
| `json-wasi` | 493590 | LLGo · no LTO | 1451560 | +194.1% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1451560 | +194.1% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2522830 | +411.1% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1683537 | +241.1% |
| `llimport` | — | LLGo · no LTO | 6764617 | — |
| `llimport` | — | LLGo · deadcode drop | 6764617 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 6919419 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6660917 | — |
| `path-report` | 116889 | LLGo · no LTO | 647681 | +454.1% |
| `path-report` | 116889 | LLGo · deadcode drop | 647681 | +454.1% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1079878 | +823.8% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 760025 | +550.2% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1069919 | +272.2% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1069919 | +272.2% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1757111 | +511.3% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1183393 | +311.7% |
| `word-count` | 86834 | LLGo · no LTO | 530720 | +511.2% |
| `word-count` | 86834 | LLGo · deadcode drop | 530720 | +511.2% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 926741 | +967.3% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 637961 | +634.7% |
