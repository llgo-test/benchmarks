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
| LLGo · no LTO | 0.908x | 11 |
| LLGo · deadcode drop | 0.555x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.808x | 11 |
| LLGo · full LTO + GlobalDCE | 0.562x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1903102 | -18.1% |
| `base64` | 2322402 | LLGo · deadcode drop | 1072146 | -53.8% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1659407 | -28.5% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1066849 | -54.1% |
| `checksum` | 2311672 | LLGo · no LTO | 1883743 | -18.5% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1057274 | -54.3% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1624339 | -29.7% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1033873 | -55.3% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2804331 | +6.3% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1576784 | -40.2% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2530369 | -4.1% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1612365 | -38.9% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1183264 | -48.0% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 947995 | -58.3% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 982556 | -56.8% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 851580 | -62.6% |
| `grep` | 2871426 | LLGo · no LTO | 2557561 | -10.9% |
| `grep` | 2871426 | LLGo · deadcode drop | 1573927 | -45.2% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2218295 | -22.7% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1547849 | -46.1% |
| `glob` | 2305059 | LLGo · no LTO | 1934273 | -16.1% |
| `glob` | 2305059 | LLGo · deadcode drop | 1076643 | -53.3% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1749443 | -24.1% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1139903 | -50.5% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4097221 | +22.7% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2304111 | -31.0% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3782095 | +13.3% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2526402 | -24.3% |
| `llimport` | 8440671 | LLGo · no LTO | 10913741 | +29.3% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9265819 | +9.8% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10016805 | +18.7% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 8975154 | +6.3% |
| `path-report` | 2428068 | LLGo · no LTO | 2077609 | -14.4% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1207599 | -50.3% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 1877819 | -22.7% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1269326 | -47.7% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3151815 | +12.1% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1881076 | -33.1% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2875840 | +2.3% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1951761 | -30.6% |
| `word-count` | 2300998 | LLGo · no LTO | 1893411 | -17.7% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1053044 | -54.2% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1706362 | -25.8% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1107076 | -51.9% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.326x | 10 |
| LLGo · deadcode drop | 6.706x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.052x | 10 |
| LLGo · full LTO + GlobalDCE | 6.812x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1903102 | +1004.5% |
| `base64` | 172302 | LLGo · deadcode drop | 1072146 | +522.2% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1659407 | +863.1% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1066849 | +519.2% |
| `checksum` | 169609 | LLGo · no LTO | 1883743 | +1010.6% |
| `checksum` | 169609 | LLGo · deadcode drop | 1057274 | +523.4% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1624339 | +857.7% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1033873 | +509.6% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2804331 | +1595.6% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1576784 | +853.4% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2530369 | +1430.0% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1612365 | +874.9% |
| `fibonacci` | 141855 | LLGo · no LTO | 1183264 | +734.1% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 947995 | +568.3% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 982556 | +592.6% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 851580 | +500.3% |
| `grep` | 155984 | LLGo · no LTO | 2557561 | +1539.6% |
| `grep` | 155984 | LLGo · deadcode drop | 1573927 | +909.0% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2218295 | +1322.1% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1547849 | +892.3% |
| `glob` | 136553 | LLGo · no LTO | 1934273 | +1316.5% |
| `glob` | 136553 | LLGo · deadcode drop | 1076643 | +688.4% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1749443 | +1181.1% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1139903 | +734.8% |
| `json-wasi` | 525666 | LLGo · no LTO | 4097221 | +679.4% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2304111 | +338.3% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3782095 | +619.5% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2526402 | +380.6% |
| `llimport` | — | LLGo · no LTO | 10913741 | — |
| `llimport` | — | LLGo · deadcode drop | 9265819 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10016805 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 8975154 | — |
| `path-report` | 194133 | LLGo · no LTO | 2077609 | +970.2% |
| `path-report` | 194133 | LLGo · deadcode drop | 1207599 | +522.0% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 1877819 | +867.3% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1269326 | +553.8% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3151815 | +795.5% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1881076 | +434.4% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2875840 | +717.1% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1951761 | +454.5% |
| `word-count` | 164053 | LLGo · no LTO | 1893411 | +1054.1% |
| `word-count` | 164053 | LLGo · deadcode drop | 1053044 | +541.9% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1706362 | +940.1% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1107076 | +574.8% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.308x | 11 |
| LLGo · deadcode drop | 0.308x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.469x | 11 |
| LLGo · full LTO + GlobalDCE | 0.336x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 542998 | -76.1% |
| `base64` | 2275731 | LLGo · deadcode drop | 542998 | -76.1% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 849370 | -62.7% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 576063 | -74.7% |
| `checksum` | 2264417 | LLGo · no LTO | 529394 | -76.6% |
| `checksum` | 2264417 | LLGo · deadcode drop | 529394 | -76.6% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 833424 | -63.2% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 557164 | -75.4% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 895583 | -65.7% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 895583 | -65.7% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1566309 | -39.9% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 992405 | -61.9% |
| `fibonacci` | 2230899 | LLGo · no LTO | 445856 | -80.0% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 445856 | -80.0% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 464333 | -79.2% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 420044 | -81.2% |
| `grep` | 2848917 | LLGo · no LTO | 878867 | -69.2% |
| `grep` | 2848917 | LLGo · deadcode drop | 878867 | -69.2% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1312354 | -53.9% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 925664 | -67.5% |
| `glob` | 2257634 | LLGo · no LTO | 535100 | -76.3% |
| `glob` | 2257634 | LLGo · deadcode drop | 535100 | -76.3% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 968182 | -57.1% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 649827 | -71.2% |
| `json-wasi` | 3314587 | LLGo · no LTO | 1442108 | -56.5% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1442108 | -56.5% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2510399 | -24.3% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1671555 | -49.6% |
| `llimport` | 8423078 | LLGo · no LTO | 6720097 | -20.2% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6720097 | -20.2% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 6878482 | -18.3% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6617093 | -21.4% |
| `path-report` | 2381190 | LLGo · no LTO | 645770 | -72.9% |
| `path-report` | 2381190 | LLGo · deadcode drop | 645770 | -72.9% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1075230 | -54.8% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 756443 | -68.2% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1062364 | -61.8% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1062364 | -61.8% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1745796 | -37.2% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1172552 | -57.8% |
| `word-count` | 2253620 | LLGo · no LTO | 528496 | -76.5% |
| `word-count` | 2253620 | LLGo · deadcode drop | 528496 | -76.5% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 921724 | -59.1% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 634059 | -71.9% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 4.774x | 10 |
| LLGo · deadcode drop | 4.774x | 10 |
| LLGo · full LTO (GlobalDCE off) | 7.572x | 10 |
| LLGo · full LTO + GlobalDCE | 5.269x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 542998 | +461.2% |
| `base64` | 96760 | LLGo · deadcode drop | 542998 | +461.2% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 849370 | +777.8% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 576063 | +495.4% |
| `checksum` | 92685 | LLGo · no LTO | 529394 | +471.2% |
| `checksum` | 92685 | LLGo · deadcode drop | 529394 | +471.2% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 833424 | +799.2% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 557164 | +501.1% |
| `conv-wasi` | 201149 | LLGo · no LTO | 895583 | +345.2% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 895583 | +345.2% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1566309 | +678.7% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 992405 | +393.4% |
| `fibonacci` | 62386 | LLGo · no LTO | 445856 | +614.7% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 445856 | +614.7% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 464333 | +644.3% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 420044 | +573.3% |
| `grep` | 303772 | LLGo · no LTO | 878867 | +189.3% |
| `grep` | 303772 | LLGo · deadcode drop | 878867 | +189.3% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1312354 | +332.0% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 925664 | +204.7% |
| `glob` | 93153 | LLGo · no LTO | 535100 | +474.4% |
| `glob` | 93153 | LLGo · deadcode drop | 535100 | +474.4% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 968182 | +939.3% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 649827 | +597.6% |
| `json-wasi` | 493590 | LLGo · no LTO | 1442108 | +192.2% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1442108 | +192.2% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2510399 | +408.6% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1671555 | +238.7% |
| `llimport` | — | LLGo · no LTO | 6720097 | — |
| `llimport` | — | LLGo · deadcode drop | 6720097 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 6878482 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6617093 | — |
| `path-report` | 116889 | LLGo · no LTO | 645770 | +452.5% |
| `path-report` | 116889 | LLGo · deadcode drop | 645770 | +452.5% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1075230 | +819.9% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 756443 | +547.1% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1062364 | +269.6% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1062364 | +269.6% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1745796 | +507.3% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1172552 | +307.9% |
| `word-count` | 86834 | LLGo · no LTO | 528496 | +508.6% |
| `word-count` | 86834 | LLGo · deadcode drop | 528496 | +508.6% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 921724 | +961.5% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 634059 | +630.2% |
