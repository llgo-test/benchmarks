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
| LLGo · no LTO | 0.913x | 11 |
| LLGo · deadcode drop | 0.560x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.813x | 11 |
| LLGo · full LTO + GlobalDCE | 0.566x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1912375 | -17.7% |
| `base64` | 2322402 | LLGo · deadcode drop | 1079662 | -53.5% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1667653 | -28.2% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1075309 | -53.7% |
| `checksum` | 2311672 | LLGo · no LTO | 1893598 | -18.1% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1065283 | -53.9% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1633128 | -29.4% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1042924 | -54.9% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2821450 | +6.9% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1590951 | -39.7% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2546217 | -3.5% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1628278 | -38.3% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1192789 | -47.6% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 957411 | -57.9% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 990199 | -56.5% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 859259 | -62.2% |
| `grep` | 2871426 | LLGo · no LTO | 2573797 | -10.4% |
| `grep` | 2871426 | LLGo · deadcode drop | 1586201 | -44.8% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2233018 | -22.2% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1560590 | -45.7% |
| `glob` | 2305059 | LLGo · no LTO | 1943476 | -15.7% |
| `glob` | 2305059 | LLGo · deadcode drop | 1084114 | -53.0% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1757546 | -23.8% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1148333 | -50.2% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4117994 | +23.4% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2321940 | -30.4% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3800992 | +13.9% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2546475 | -23.7% |
| `llimport` | 8440671 | LLGo · no LTO | 10964154 | +29.9% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9317272 | +10.4% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10064656 | +19.2% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 9023034 | +6.9% |
| `path-report` | 2428068 | LLGo · no LTO | 2087105 | -14.0% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1215452 | -49.9% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 1886298 | -22.3% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1277889 | -47.4% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3171037 | +12.8% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1896388 | -32.5% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2893410 | +2.9% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1970014 | -29.9% |
| `word-count` | 2300998 | LLGo · no LTO | 1903288 | -17.3% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1061148 | -53.9% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1715109 | -25.5% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1116191 | -51.5% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.390x | 10 |
| LLGo · deadcode drop | 6.758x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.109x | 10 |
| LLGo · full LTO + GlobalDCE | 6.869x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1912375 | +1009.9% |
| `base64` | 172302 | LLGo · deadcode drop | 1079662 | +526.6% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1667653 | +867.9% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1075309 | +524.1% |
| `checksum` | 169609 | LLGo · no LTO | 1893598 | +1016.4% |
| `checksum` | 169609 | LLGo · deadcode drop | 1065283 | +528.1% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1633128 | +862.9% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1042924 | +514.9% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2821450 | +1606.0% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1590951 | +862.0% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2546217 | +1439.6% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1628278 | +884.5% |
| `fibonacci` | 141855 | LLGo · no LTO | 1192789 | +740.9% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 957411 | +574.9% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 990199 | +598.0% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 859259 | +505.7% |
| `grep` | 155984 | LLGo · no LTO | 2573797 | +1550.0% |
| `grep` | 155984 | LLGo · deadcode drop | 1586201 | +916.9% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2233018 | +1331.6% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1560590 | +900.5% |
| `glob` | 136553 | LLGo · no LTO | 1943476 | +1323.2% |
| `glob` | 136553 | LLGo · deadcode drop | 1084114 | +693.9% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1757546 | +1187.1% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1148333 | +740.9% |
| `json-wasi` | 525666 | LLGo · no LTO | 4117994 | +683.4% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2321940 | +341.7% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3800992 | +623.1% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2546475 | +384.4% |
| `llimport` | — | LLGo · no LTO | 10964154 | — |
| `llimport` | — | LLGo · deadcode drop | 9317272 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10064656 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 9023034 | — |
| `path-report` | 194133 | LLGo · no LTO | 2087105 | +975.1% |
| `path-report` | 194133 | LLGo · deadcode drop | 1215452 | +526.1% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 1886298 | +871.7% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1277889 | +558.3% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3171037 | +800.9% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1896388 | +438.8% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2893410 | +722.1% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1970014 | +459.7% |
| `word-count` | 164053 | LLGo · no LTO | 1903288 | +1060.2% |
| `word-count` | 164053 | LLGo · deadcode drop | 1061148 | +546.8% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1715109 | +945.5% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1116191 | +580.4% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.310x | 11 |
| LLGo · deadcode drop | 0.310x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.467x | 11 |
| LLGo · full LTO + GlobalDCE | 0.339x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 545255 | -76.0% |
| `base64` | 2275731 | LLGo · deadcode drop | 545255 | -76.0% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 841462 | -63.0% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 579873 | -74.5% |
| `checksum` | 2264417 | LLGo · no LTO | 532037 | -76.5% |
| `checksum` | 2264417 | LLGo · deadcode drop | 532037 | -76.5% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 826107 | -63.5% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 561364 | -75.2% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 907855 | -65.2% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 907855 | -65.2% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1563762 | -40.0% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1006926 | -61.4% |
| `fibonacci` | 2230899 | LLGo · no LTO | 452231 | -79.7% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 452231 | -79.7% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 470241 | -78.9% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 425957 | -80.9% |
| `grep` | 2848917 | LLGo · no LTO | 884982 | -68.9% |
| `grep` | 2848917 | LLGo · deadcode drop | 884982 | -68.9% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1304323 | -54.2% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 932886 | -67.3% |
| `glob` | 2257634 | LLGo · no LTO | 537371 | -76.2% |
| `glob` | 2257634 | LLGo · deadcode drop | 537371 | -76.2% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 956258 | -57.6% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 653619 | -71.0% |
| `json-wasi` | 3314587 | LLGo · no LTO | 1460325 | -55.9% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1460325 | -55.9% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2501696 | -24.5% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1692914 | -48.9% |
| `llimport` | 8423078 | LLGo · no LTO | 6748250 | -19.9% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6748250 | -19.9% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 6888056 | -18.2% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6641085 | -21.2% |
| `path-report` | 2381190 | LLGo · no LTO | 648241 | -72.8% |
| `path-report` | 2381190 | LLGo · deadcode drop | 648241 | -72.8% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1063437 | -55.3% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 760358 | -68.1% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1075507 | -61.3% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1075507 | -61.3% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1744818 | -37.3% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1188860 | -57.3% |
| `word-count` | 2253620 | LLGo · no LTO | 531280 | -76.4% |
| `word-count` | 2253620 | LLGo · deadcode drop | 531280 | -76.4% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 914438 | -59.4% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 638383 | -71.7% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 4.814x | 10 |
| LLGo · deadcode drop | 4.814x | 10 |
| LLGo · full LTO (GlobalDCE off) | 7.535x | 10 |
| LLGo · full LTO + GlobalDCE | 5.319x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 545255 | +463.5% |
| `base64` | 96760 | LLGo · deadcode drop | 545255 | +463.5% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 841462 | +769.6% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 579873 | +499.3% |
| `checksum` | 92685 | LLGo · no LTO | 532037 | +474.0% |
| `checksum` | 92685 | LLGo · deadcode drop | 532037 | +474.0% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 826107 | +791.3% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 561364 | +505.7% |
| `conv-wasi` | 201149 | LLGo · no LTO | 907855 | +351.3% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 907855 | +351.3% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1563762 | +677.4% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1006926 | +400.6% |
| `fibonacci` | 62386 | LLGo · no LTO | 452231 | +624.9% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 452231 | +624.9% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 470241 | +653.8% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 425957 | +582.8% |
| `grep` | 303772 | LLGo · no LTO | 884982 | +191.3% |
| `grep` | 303772 | LLGo · deadcode drop | 884982 | +191.3% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1304323 | +329.4% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 932886 | +207.1% |
| `glob` | 93153 | LLGo · no LTO | 537371 | +476.9% |
| `glob` | 93153 | LLGo · deadcode drop | 537371 | +476.9% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 956258 | +926.5% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 653619 | +601.7% |
| `json-wasi` | 493590 | LLGo · no LTO | 1460325 | +195.9% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1460325 | +195.9% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2501696 | +406.8% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1692914 | +243.0% |
| `llimport` | — | LLGo · no LTO | 6748250 | — |
| `llimport` | — | LLGo · deadcode drop | 6748250 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 6888056 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6641085 | — |
| `path-report` | 116889 | LLGo · no LTO | 648241 | +454.6% |
| `path-report` | 116889 | LLGo · deadcode drop | 648241 | +454.6% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1063437 | +809.8% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 760358 | +550.5% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1075507 | +274.2% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1075507 | +274.2% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1744818 | +507.0% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1188860 | +313.6% |
| `word-count` | 86834 | LLGo · no LTO | 531280 | +511.8% |
| `word-count` | 86834 | LLGo · deadcode drop | 531280 | +511.8% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 914438 | +953.1% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 638383 | +635.2% |
