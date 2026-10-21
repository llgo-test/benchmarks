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
| LLGo · no LTO | 1.008x | 11 |
| LLGo · deadcode drop | 0.630x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.899x | 11 |
| LLGo · full LTO + GlobalDCE | 0.584x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1988254 | -14.4% |
| `base64` | 2322402 | LLGo · deadcode drop | 1179335 | -49.2% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1768154 | -23.9% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1084878 | -53.3% |
| `checksum` | 2311672 | LLGo · no LTO | 1968680 | -14.8% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1152665 | -50.1% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1732762 | -25.0% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1050628 | -54.6% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 3082131 | +16.8% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1755867 | -33.5% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2753502 | +4.4% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1613324 | -38.9% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1733415 | -23.8% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 1072077 | -52.9% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1521477 | -33.1% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 982877 | -56.8% |
| `grep` | 2871426 | LLGo · no LTO | 2669617 | -7.0% |
| `grep` | 2871426 | LLGo · deadcode drop | 1712912 | -40.3% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2351122 | -18.1% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1582922 | -44.9% |
| `glob` | 2305059 | LLGo · no LTO | 2124437 | -7.8% |
| `glob` | 2305059 | LLGo · deadcode drop | 1276694 | -44.6% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1874294 | -18.7% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1168332 | -49.3% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4298234 | +28.8% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2565603 | -23.1% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3922712 | +17.5% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2527996 | -24.3% |
| `llimport` | 8440671 | LLGo · no LTO | 11441728 | +35.6% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9798034 | +16.1% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10457939 | +23.9% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 9121233 | +8.1% |
| `path-report` | 2428068 | LLGo · no LTO | 2459007 | +1.3% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1601355 | -34.0% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 2198279 | -9.5% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1483410 | -38.9% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3437621 | +22.3% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 2076216 | -26.1% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 3115318 | +10.8% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1952256 | -30.6% |
| `word-count` | 2300998 | LLGo · no LTO | 2084552 | -9.4% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1249722 | -45.7% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1833307 | -20.3% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1135100 | -50.7% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 12.643x | 10 |
| LLGo · deadcode drop | 7.658x | 10 |
| LLGo · full LTO (GlobalDCE off) | 11.246x | 10 |
| LLGo · full LTO + GlobalDCE | 7.094x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1988254 | +1053.9% |
| `base64` | 172302 | LLGo · deadcode drop | 1179335 | +584.5% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1768154 | +926.2% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1084878 | +529.6% |
| `checksum` | 169609 | LLGo · no LTO | 1968680 | +1060.7% |
| `checksum` | 169609 | LLGo · deadcode drop | 1152665 | +579.6% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1732762 | +921.6% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1050628 | +519.4% |
| `conv-wasi` | 165385 | LLGo · no LTO | 3082131 | +1763.6% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1755867 | +961.7% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2753502 | +1564.9% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1613324 | +875.5% |
| `fibonacci` | 141855 | LLGo · no LTO | 1733415 | +1122.0% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 1072077 | +655.8% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1521477 | +972.6% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 982877 | +592.9% |
| `grep` | 155984 | LLGo · no LTO | 2669617 | +1611.5% |
| `grep` | 155984 | LLGo · deadcode drop | 1712912 | +998.1% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2351122 | +1407.3% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1582922 | +914.8% |
| `glob` | 136553 | LLGo · no LTO | 2124437 | +1455.8% |
| `glob` | 136553 | LLGo · deadcode drop | 1276694 | +834.9% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1874294 | +1272.6% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1168332 | +755.6% |
| `json-wasi` | 525666 | LLGo · no LTO | 4298234 | +717.7% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2565603 | +388.1% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3922712 | +646.2% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2527996 | +380.9% |
| `llimport` | — | LLGo · no LTO | 11441728 | — |
| `llimport` | — | LLGo · deadcode drop | 9798034 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10457939 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 9121233 | — |
| `path-report` | 194133 | LLGo · no LTO | 2459007 | +1166.7% |
| `path-report` | 194133 | LLGo · deadcode drop | 1601355 | +724.9% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 2198279 | +1032.4% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1483410 | +664.1% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3437621 | +876.7% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 2076216 | +489.9% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 3115318 | +785.1% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1952256 | +454.7% |
| `word-count` | 164053 | LLGo · no LTO | 2084552 | +1170.7% |
| `word-count` | 164053 | LLGo · deadcode drop | 1249722 | +661.8% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1833307 | +1017.5% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1135100 | +591.9% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.818x | 11 |
| LLGo · deadcode drop | 0.529x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.712x | 11 |
| LLGo · full LTO + GlobalDCE | 0.474x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1568640 | -31.1% |
| `base64` | 2275731 | LLGo · deadcode drop | 958973 | -57.9% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 1347028 | -40.8% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 843540 | -62.9% |
| `checksum` | 2264417 | LLGo · no LTO | 1555347 | -31.3% |
| `checksum` | 2264417 | LLGo · deadcode drop | 940564 | -58.5% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 1328466 | -41.3% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 824080 | -63.6% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 2453822 | -5.9% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 1463120 | -43.9% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 2150458 | -17.5% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1306252 | -49.9% |
| `fibonacci` | 2230899 | LLGo · no LTO | 1384565 | -37.9% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 881188 | -60.5% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 1174846 | -47.3% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 770362 | -65.5% |
| `grep` | 2848917 | LLGo · no LTO | 2101193 | -26.2% |
| `grep` | 2848917 | LLGo · deadcode drop | 1396272 | -51.0% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1840291 | -35.4% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 1275423 | -55.2% |
| `glob` | 2257634 | LLGo · no LTO | 1713747 | -24.1% |
| `glob` | 2257634 | LLGo · deadcode drop | 1072154 | -52.5% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1472371 | -34.8% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 946538 | -58.1% |
| `json-wasi` | 3314587 | LLGo · no LTO | 3482869 | +5.1% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 2127857 | -35.8% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 3103121 | -6.4% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 2028314 | -38.8% |
| `llimport` | 8423078 | LLGo · no LTO | 9458950 | +12.3% |
| `llimport` | 8423078 | LLGo · deadcode drop | 8297441 | -1.5% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 8571666 | +1.8% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 7685207 | -8.8% |
| `path-report` | 2381190 | LLGo · no LTO | 1964505 | -17.5% |
| `path-report` | 2381190 | LLGo · deadcode drop | 1317415 | -44.7% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1715420 | -28.0% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 1183140 | -50.3% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 2712283 | -2.5% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1703145 | -38.8% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 2384310 | -14.3% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1532557 | -44.9% |
| `word-count` | 2253620 | LLGo · no LTO | 1680844 | -25.4% |
| `word-count` | 2253620 | LLGo · deadcode drop | 1048293 | -53.5% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 1440777 | -36.1% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 920129 | -59.2% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 13.513x | 10 |
| LLGo · deadcode drop | 8.470x | 10 |
| LLGo · full LTO (GlobalDCE off) | 11.719x | 10 |
| LLGo · full LTO + GlobalDCE | 7.576x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1568640 | +1521.2% |
| `base64` | 96760 | LLGo · deadcode drop | 958973 | +891.1% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 1347028 | +1292.1% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 843540 | +771.8% |
| `checksum` | 92685 | LLGo · no LTO | 1555347 | +1578.1% |
| `checksum` | 92685 | LLGo · deadcode drop | 940564 | +914.8% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 1328466 | +1333.3% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 824080 | +789.1% |
| `conv-wasi` | 201149 | LLGo · no LTO | 2453822 | +1119.9% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 1463120 | +627.4% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 2150458 | +969.1% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1306252 | +549.4% |
| `fibonacci` | 62386 | LLGo · no LTO | 1384565 | +2119.4% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 881188 | +1312.5% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 1174846 | +1783.2% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 770362 | +1134.8% |
| `grep` | 303772 | LLGo · no LTO | 2101193 | +591.7% |
| `grep` | 303772 | LLGo · deadcode drop | 1396272 | +359.6% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1840291 | +505.8% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 1275423 | +319.9% |
| `glob` | 93153 | LLGo · no LTO | 1713747 | +1739.7% |
| `glob` | 93153 | LLGo · deadcode drop | 1072154 | +1051.0% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1472371 | +1480.6% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 946538 | +916.1% |
| `json-wasi` | 493590 | LLGo · no LTO | 3482869 | +605.6% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 2127857 | +331.1% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 3103121 | +528.7% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 2028314 | +310.9% |
| `llimport` | — | LLGo · no LTO | 9458950 | — |
| `llimport` | — | LLGo · deadcode drop | 8297441 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 8571666 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 7685207 | — |
| `path-report` | 116889 | LLGo · no LTO | 1964505 | +1580.7% |
| `path-report` | 116889 | LLGo · deadcode drop | 1317415 | +1027.1% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1715420 | +1367.6% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 1183140 | +912.2% |
| `sha-wasi` | 287449 | LLGo · no LTO | 2712283 | +843.6% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1703145 | +492.5% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 2384310 | +729.5% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1532557 | +433.2% |
| `word-count` | 86834 | LLGo · no LTO | 1680844 | +1835.7% |
| `word-count` | 86834 | LLGo · deadcode drop | 1048293 | +1107.2% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 1440777 | +1559.2% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 920129 | +959.6% |
