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
| LLGo · no LTO | 0.914x | 11 |
| LLGo · deadcode drop | 0.560x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.814x | 11 |
| LLGo · full LTO + GlobalDCE | 0.565x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1918235 | -17.4% |
| `base64` | 2322402 | LLGo · deadcode drop | 1081692 | -53.4% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1673205 | -28.0% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1075084 | -53.7% |
| `checksum` | 2311672 | LLGo · no LTO | 1898869 | -17.9% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1066856 | -53.8% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1637729 | -29.2% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1041911 | -54.9% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2820363 | +6.9% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1587541 | -39.8% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2543743 | -3.6% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1621426 | -38.5% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1192624 | -47.6% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 957161 | -57.9% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 990243 | -56.5% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 859226 | -62.2% |
| `grep` | 2871426 | LLGo · no LTO | 2573196 | -10.4% |
| `grep` | 2871426 | LLGo · deadcode drop | 1584266 | -44.8% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2231053 | -22.3% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1555353 | -45.8% |
| `glob` | 2305059 | LLGo · no LTO | 1949413 | -15.4% |
| `glob` | 2305059 | LLGo · deadcode drop | 1086206 | -52.9% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1762798 | -23.5% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1147932 | -50.2% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4118279 | +23.4% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2319105 | -30.5% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3800905 | +13.9% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2537509 | -24.0% |
| `llimport` | 8440671 | LLGo · no LTO | 10963912 | +29.9% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9309846 | +10.3% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10063171 | +19.2% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 9015871 | +6.8% |
| `path-report` | 2428068 | LLGo · no LTO | 2092832 | -13.8% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1217341 | -49.9% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 1891394 | -22.1% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1277546 | -47.4% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3169124 | +12.7% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1892402 | -32.7% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2890793 | +2.8% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1961533 | -30.2% |
| `word-count` | 2300998 | LLGo · no LTO | 1908541 | -17.1% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1062611 | -53.8% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1719690 | -25.3% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1115108 | -51.5% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.405x | 10 |
| LLGo · deadcode drop | 6.759x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.121x | 10 |
| LLGo · full LTO + GlobalDCE | 6.856x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1918235 | +1013.3% |
| `base64` | 172302 | LLGo · deadcode drop | 1081692 | +527.8% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1673205 | +871.1% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1075084 | +524.0% |
| `checksum` | 169609 | LLGo · no LTO | 1898869 | +1019.6% |
| `checksum` | 169609 | LLGo · deadcode drop | 1066856 | +529.0% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1637729 | +865.6% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1041911 | +514.3% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2820363 | +1605.3% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1587541 | +859.9% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2543743 | +1438.1% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1621426 | +880.4% |
| `fibonacci` | 141855 | LLGo · no LTO | 1192624 | +740.7% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 957161 | +574.7% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 990243 | +598.1% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 859226 | +505.7% |
| `grep` | 155984 | LLGo · no LTO | 2573196 | +1549.7% |
| `grep` | 155984 | LLGo · deadcode drop | 1584266 | +915.7% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2231053 | +1330.3% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1555353 | +897.1% |
| `glob` | 136553 | LLGo · no LTO | 1949413 | +1327.6% |
| `glob` | 136553 | LLGo · deadcode drop | 1086206 | +695.4% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1762798 | +1190.9% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1147932 | +740.6% |
| `json-wasi` | 525666 | LLGo · no LTO | 4118279 | +683.4% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2319105 | +341.2% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3800905 | +623.1% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2537509 | +382.7% |
| `llimport` | — | LLGo · no LTO | 10963912 | — |
| `llimport` | — | LLGo · deadcode drop | 9309846 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10063171 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 9015871 | — |
| `path-report` | 194133 | LLGo · no LTO | 2092832 | +978.0% |
| `path-report` | 194133 | LLGo · deadcode drop | 1217341 | +527.1% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 1891394 | +874.3% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1277546 | +558.1% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3169124 | +800.4% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1892402 | +437.7% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2890793 | +721.3% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1961533 | +457.3% |
| `word-count` | 164053 | LLGo · no LTO | 1908541 | +1063.4% |
| `word-count` | 164053 | LLGo · deadcode drop | 1062611 | +547.7% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1719690 | +948.3% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1115108 | +579.7% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.308x | 11 |
| LLGo · deadcode drop | 0.308x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.470x | 11 |
| LLGo · full LTO + GlobalDCE | 0.336x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 544465 | -76.1% |
| `base64` | 2275731 | LLGo · deadcode drop | 544465 | -76.1% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 852217 | -62.6% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 577423 | -74.6% |
| `checksum` | 2264417 | LLGo · no LTO | 530863 | -76.6% |
| `checksum` | 2264417 | LLGo · deadcode drop | 530863 | -76.6% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 836264 | -63.1% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 558532 | -75.3% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 897089 | -65.6% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 897089 | -65.6% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1566785 | -39.9% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 993768 | -61.9% |
| `fibonacci` | 2230899 | LLGo · no LTO | 447449 | -79.9% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 447449 | -79.9% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 466312 | -79.1% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 421498 | -81.1% |
| `grep` | 2848917 | LLGo · no LTO | 879951 | -69.1% |
| `grep` | 2848917 | LLGo · deadcode drop | 879951 | -69.1% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1311057 | -54.0% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 925071 | -67.5% |
| `glob` | 2257634 | LLGo · no LTO | 536585 | -76.2% |
| `glob` | 2257634 | LLGo · deadcode drop | 536585 | -76.2% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 970794 | -57.0% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 651195 | -71.2% |
| `json-wasi` | 3314587 | LLGo · no LTO | 1442856 | -56.5% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1442856 | -56.5% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2508787 | -24.3% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1671939 | -49.6% |
| `llimport` | 8423078 | LLGo · no LTO | 6665039 | -20.9% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6665039 | -20.9% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 6824994 | -19.0% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6559641 | -22.1% |
| `path-report` | 2381190 | LLGo · no LTO | 647226 | -72.8% |
| `path-report` | 2381190 | LLGo · deadcode drop | 647226 | -72.8% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1077823 | -54.7% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 757792 | -68.2% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1060734 | -61.9% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1060734 | -61.9% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1743053 | -37.3% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1170697 | -57.9% |
| `word-count` | 2253620 | LLGo · no LTO | 529965 | -76.5% |
| `word-count` | 2253620 | LLGo · deadcode drop | 529965 | -76.5% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 924569 | -59.0% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 635427 | -71.8% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 4.783x | 10 |
| LLGo · deadcode drop | 4.783x | 10 |
| LLGo · full LTO (GlobalDCE off) | 7.584x | 10 |
| LLGo · full LTO + GlobalDCE | 5.276x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 544465 | +462.7% |
| `base64` | 96760 | LLGo · deadcode drop | 544465 | +462.7% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 852217 | +780.8% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 577423 | +496.8% |
| `checksum` | 92685 | LLGo · no LTO | 530863 | +472.8% |
| `checksum` | 92685 | LLGo · deadcode drop | 530863 | +472.8% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 836264 | +802.3% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 558532 | +502.6% |
| `conv-wasi` | 201149 | LLGo · no LTO | 897089 | +346.0% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 897089 | +346.0% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1566785 | +678.9% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 993768 | +394.0% |
| `fibonacci` | 62386 | LLGo · no LTO | 447449 | +617.2% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 447449 | +617.2% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 466312 | +647.5% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 421498 | +575.6% |
| `grep` | 303772 | LLGo · no LTO | 879951 | +189.7% |
| `grep` | 303772 | LLGo · deadcode drop | 879951 | +189.7% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1311057 | +331.6% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 925071 | +204.5% |
| `glob` | 93153 | LLGo · no LTO | 536585 | +476.0% |
| `glob` | 93153 | LLGo · deadcode drop | 536585 | +476.0% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 970794 | +942.2% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 651195 | +599.1% |
| `json-wasi` | 493590 | LLGo · no LTO | 1442856 | +192.3% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1442856 | +192.3% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2508787 | +408.3% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1671939 | +238.7% |
| `llimport` | — | LLGo · no LTO | 6665039 | — |
| `llimport` | — | LLGo · deadcode drop | 6665039 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 6824994 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6559641 | — |
| `path-report` | 116889 | LLGo · no LTO | 647226 | +453.7% |
| `path-report` | 116889 | LLGo · deadcode drop | 647226 | +453.7% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1077823 | +822.1% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 757792 | +548.3% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1060734 | +269.0% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1060734 | +269.0% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1743053 | +506.4% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1170697 | +307.3% |
| `word-count` | 86834 | LLGo · no LTO | 529965 | +510.3% |
| `word-count` | 86834 | LLGo · deadcode drop | 529965 | +510.3% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 924569 | +964.8% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 635427 | +631.8% |
