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
| base64 | LLGoNoLTO | required | failed | [logs/base64.LLGoNoLTO.log](logs/base64.LLGoNoLTO.log) |
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
| LLGo · no LTO | 0.911x | 11 |
| LLGo · deadcode drop | 0.558x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.811x | 11 |
| LLGo · full LTO + GlobalDCE | 0.565x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1906933 | -17.9% |
| `base64` | 2322402 | LLGo · deadcode drop | 1074542 | -53.7% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1663605 | -28.4% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1071287 | -53.9% |
| `checksum` | 2311672 | LLGo · no LTO | 1888153 | -18.3% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1060212 | -54.1% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1629073 | -29.5% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1038885 | -55.1% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2815344 | +6.7% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1585876 | -39.9% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2541602 | -3.7% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1624260 | -38.4% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1187371 | -47.8% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 952337 | -58.1% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 986185 | -56.6% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 855262 | -62.4% |
| `grep` | 2871426 | LLGo · no LTO | 2568357 | -10.6% |
| `grep` | 2871426 | LLGo · deadcode drop | 1581119 | -44.9% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2228959 | -22.4% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1556568 | -45.8% |
| `glob` | 2305059 | LLGo · no LTO | 1938042 | -15.9% |
| `glob` | 2305059 | LLGo · deadcode drop | 1079044 | -53.2% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1753493 | -23.9% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1144308 | -50.4% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4111866 | +23.2% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2316839 | -30.6% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3796347 | +13.7% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2542449 | -23.8% |
| `llimport` | 8440671 | LLGo · no LTO | 10957954 | +29.8% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9311429 | +10.3% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10059361 | +19.2% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 9017851 | +6.8% |
| `path-report` | 2428068 | LLGo · no LTO | 2081677 | -14.3% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1210350 | -50.2% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 1882266 | -22.5% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1273869 | -47.5% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3164797 | +12.6% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1891272 | -32.7% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2888788 | +2.8% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1965951 | -30.1% |
| `word-count` | 2300998 | LLGo · no LTO | 1897854 | -17.5% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1056066 | -54.1% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1711090 | -25.6% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1112182 | -51.7% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.360x | 10 |
| LLGo · deadcode drop | 6.732x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.086x | 10 |
| LLGo · full LTO + GlobalDCE | 6.847x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1906933 | +1006.7% |
| `base64` | 172302 | LLGo · deadcode drop | 1074542 | +523.6% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1663605 | +865.5% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1071287 | +521.7% |
| `checksum` | 169609 | LLGo · no LTO | 1888153 | +1013.2% |
| `checksum` | 169609 | LLGo · deadcode drop | 1060212 | +525.1% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1629073 | +860.5% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1038885 | +512.5% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2815344 | +1602.3% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1585876 | +858.9% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2541602 | +1436.8% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1624260 | +882.1% |
| `fibonacci` | 141855 | LLGo · no LTO | 1187371 | +737.0% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 952337 | +571.3% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 986185 | +595.2% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 855262 | +502.9% |
| `grep` | 155984 | LLGo · no LTO | 2568357 | +1546.6% |
| `grep` | 155984 | LLGo · deadcode drop | 1581119 | +913.6% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2228959 | +1329.0% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1556568 | +897.9% |
| `glob` | 136553 | LLGo · no LTO | 1938042 | +1319.3% |
| `glob` | 136553 | LLGo · deadcode drop | 1079044 | +690.2% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1753493 | +1184.1% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1144308 | +738.0% |
| `json-wasi` | 525666 | LLGo · no LTO | 4111866 | +682.2% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2316839 | +340.7% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3796347 | +622.2% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2542449 | +383.7% |
| `llimport` | — | LLGo · no LTO | 10957954 | — |
| `llimport` | — | LLGo · deadcode drop | 9311429 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10059361 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 9017851 | — |
| `path-report` | 194133 | LLGo · no LTO | 2081677 | +972.3% |
| `path-report` | 194133 | LLGo · deadcode drop | 1210350 | +523.5% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 1882266 | +869.6% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1273869 | +556.2% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3164797 | +799.2% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1891272 | +437.3% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2888788 | +720.7% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1965951 | +458.6% |
| `word-count` | 164053 | LLGo · no LTO | 1897854 | +1056.9% |
| `word-count` | 164053 | LLGo · deadcode drop | 1056066 | +543.7% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1711090 | +943.0% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1112182 | +577.9% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.317x | 10 |
| LLGo · deadcode drop | 0.309x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.466x | 11 |
| LLGo · full LTO + GlobalDCE | 0.338x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | — | — |
| `base64` | 2275731 | LLGo · deadcode drop | 542644 | -76.2% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 839448 | -63.1% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 577831 | -74.6% |
| `checksum` | 2264417 | LLGo · no LTO | 529432 | -76.6% |
| `checksum` | 2264417 | LLGo · deadcode drop | 529432 | -76.6% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 824092 | -63.6% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 559345 | -75.3% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 905266 | -65.3% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 905266 | -65.3% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1561350 | -40.1% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1004891 | -61.5% |
| `fibonacci` | 2230899 | LLGo · no LTO | 449626 | -79.8% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 449626 | -79.8% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 468243 | -79.0% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 423922 | -81.0% |
| `grep` | 2848917 | LLGo · no LTO | 882377 | -69.0% |
| `grep` | 2848917 | LLGo · deadcode drop | 882377 | -69.0% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1302300 | -54.3% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 930851 | -67.3% |
| `glob` | 2257634 | LLGo · no LTO | 534766 | -76.3% |
| `glob` | 2257634 | LLGo · deadcode drop | 534766 | -76.3% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 954243 | -57.7% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 651592 | -71.1% |
| `json-wasi` | 3314587 | LLGo · no LTO | 1455987 | -56.1% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1455987 | -56.1% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2496726 | -24.7% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1688278 | -49.1% |
| `llimport` | 8423078 | LLGo · no LTO | 6743032 | -19.9% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6743032 | -19.9% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 6882714 | -18.3% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6636296 | -21.2% |
| `path-report` | 2381190 | LLGo · no LTO | 645636 | -72.9% |
| `path-report` | 2381190 | LLGo · deadcode drop | 645636 | -72.9% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1061422 | -55.4% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 758339 | -68.2% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1072912 | -61.4% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1072912 | -61.4% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1742398 | -37.3% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1186826 | -57.3% |
| `word-count` | 2253620 | LLGo · no LTO | 528675 | -76.5% |
| `word-count` | 2253620 | LLGo · deadcode drop | 528675 | -76.5% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 912423 | -59.5% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 636356 | -71.8% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 4.711x | 9 |
| LLGo · deadcode drop | 4.794x | 10 |
| LLGo · full LTO (GlobalDCE off) | 7.519x | 10 |
| LLGo · full LTO + GlobalDCE | 5.304x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | — | — |
| `base64` | 96760 | LLGo · deadcode drop | 542644 | +460.8% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 839448 | +767.6% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 577831 | +497.2% |
| `checksum` | 92685 | LLGo · no LTO | 529432 | +471.2% |
| `checksum` | 92685 | LLGo · deadcode drop | 529432 | +471.2% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 824092 | +789.1% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 559345 | +503.5% |
| `conv-wasi` | 201149 | LLGo · no LTO | 905266 | +350.0% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 905266 | +350.0% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1561350 | +676.2% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1004891 | +399.6% |
| `fibonacci` | 62386 | LLGo · no LTO | 449626 | +620.7% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 449626 | +620.7% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 468243 | +650.6% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 423922 | +579.5% |
| `grep` | 303772 | LLGo · no LTO | 882377 | +190.5% |
| `grep` | 303772 | LLGo · deadcode drop | 882377 | +190.5% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1302300 | +328.7% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 930851 | +206.4% |
| `glob` | 93153 | LLGo · no LTO | 534766 | +474.1% |
| `glob` | 93153 | LLGo · deadcode drop | 534766 | +474.1% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 954243 | +924.4% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 651592 | +599.5% |
| `json-wasi` | 493590 | LLGo · no LTO | 1455987 | +195.0% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1455987 | +195.0% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2496726 | +405.8% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1688278 | +242.0% |
| `llimport` | — | LLGo · no LTO | 6743032 | — |
| `llimport` | — | LLGo · deadcode drop | 6743032 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 6882714 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6636296 | — |
| `path-report` | 116889 | LLGo · no LTO | 645636 | +452.3% |
| `path-report` | 116889 | LLGo · deadcode drop | 645636 | +452.3% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1061422 | +808.1% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 758339 | +548.8% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1072912 | +273.3% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1072912 | +273.3% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1742398 | +506.2% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1186826 | +312.9% |
| `word-count` | 86834 | LLGo · no LTO | 528675 | +508.8% |
| `word-count` | 86834 | LLGo · deadcode drop | 528675 | +508.8% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 912423 | +950.8% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 636356 | +632.8% |
