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
| `base64` | 2322402 | LLGo · no LTO | 1902881 | -18.1% |
| `base64` | 2322402 | LLGo · deadcode drop | 1071939 | -53.8% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1659290 | -28.6% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1066726 | -54.1% |
| `checksum` | 2311672 | LLGo · no LTO | 1883470 | -18.5% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1057028 | -54.3% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1624238 | -29.7% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1033754 | -55.3% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2804081 | +6.3% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1576572 | -40.2% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2530275 | -4.1% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1612247 | -38.9% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1183034 | -48.0% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 947772 | -58.3% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 982440 | -56.8% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 851465 | -62.6% |
| `grep` | 2871426 | LLGo · no LTO | 2557337 | -10.9% |
| `grep` | 2871426 | LLGo · deadcode drop | 1573698 | -45.2% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2218190 | -22.7% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1547709 | -46.1% |
| `glob` | 2305059 | LLGo · no LTO | 1934068 | -16.1% |
| `glob` | 2305059 | LLGo · deadcode drop | 1076428 | -53.3% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1749284 | -24.1% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1139784 | -50.6% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4096991 | +22.7% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2303892 | -31.0% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3781984 | +13.3% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2526342 | -24.3% |
| `llimport` | 8440671 | LLGo · no LTO | 10913541 | +29.3% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9265581 | +9.8% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10016701 | +18.7% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 8975094 | +6.3% |
| `path-report` | 2428068 | LLGo · no LTO | 2077369 | -14.4% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1207334 | -50.3% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 1877751 | -22.7% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1269218 | -47.7% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3151573 | +12.1% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1880849 | -33.1% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2875694 | +2.3% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1951682 | -30.6% |
| `word-count` | 2300998 | LLGo · no LTO | 1893187 | -17.7% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1052829 | -54.2% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1706248 | -25.8% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1106939 | -51.9% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.325x | 10 |
| LLGo · deadcode drop | 6.705x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.051x | 10 |
| LLGo · full LTO + GlobalDCE | 6.811x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1902881 | +1004.4% |
| `base64` | 172302 | LLGo · deadcode drop | 1071939 | +522.1% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1659290 | +863.0% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1066726 | +519.1% |
| `checksum` | 169609 | LLGo · no LTO | 1883470 | +1010.5% |
| `checksum` | 169609 | LLGo · deadcode drop | 1057028 | +523.2% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1624238 | +857.6% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1033754 | +509.5% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2804081 | +1595.5% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1576572 | +853.3% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2530275 | +1429.9% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1612247 | +874.8% |
| `fibonacci` | 141855 | LLGo · no LTO | 1183034 | +734.0% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 947772 | +568.1% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 982440 | +592.6% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 851465 | +500.2% |
| `grep` | 155984 | LLGo · no LTO | 2557337 | +1539.5% |
| `grep` | 155984 | LLGo · deadcode drop | 1573698 | +908.9% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2218190 | +1322.1% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1547709 | +892.2% |
| `glob` | 136553 | LLGo · no LTO | 1934068 | +1316.3% |
| `glob` | 136553 | LLGo · deadcode drop | 1076428 | +688.3% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1749284 | +1181.0% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1139784 | +734.7% |
| `json-wasi` | 525666 | LLGo · no LTO | 4096991 | +679.4% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2303892 | +338.3% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3781984 | +619.5% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2526342 | +380.6% |
| `llimport` | — | LLGo · no LTO | 10913541 | — |
| `llimport` | — | LLGo · deadcode drop | 9265581 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10016701 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 8975094 | — |
| `path-report` | 194133 | LLGo · no LTO | 2077369 | +970.1% |
| `path-report` | 194133 | LLGo · deadcode drop | 1207334 | +521.9% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 1877751 | +867.2% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1269218 | +553.8% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3151573 | +795.4% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1880849 | +434.4% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2875694 | +717.0% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1951682 | +454.5% |
| `word-count` | 164053 | LLGo · no LTO | 1893187 | +1054.0% |
| `word-count` | 164053 | LLGo · deadcode drop | 1052829 | +541.8% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1706248 | +940.1% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1106939 | +574.7% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.308x | 11 |
| LLGo · deadcode drop | 0.308x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.469x | 11 |
| LLGo · full LTO + GlobalDCE | 0.336x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 542851 | -76.1% |
| `base64` | 2275731 | LLGo · deadcode drop | 542851 | -76.1% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 849381 | -62.7% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 576074 | -74.7% |
| `checksum` | 2264417 | LLGo · no LTO | 529247 | -76.6% |
| `checksum` | 2264417 | LLGo · deadcode drop | 529247 | -76.6% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 833435 | -63.2% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 557175 | -75.4% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 895436 | -65.7% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 895436 | -65.7% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1566316 | -39.9% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 992412 | -61.9% |
| `fibonacci` | 2230899 | LLGo · no LTO | 445709 | -80.0% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 445709 | -80.0% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 464344 | -79.2% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 420055 | -81.2% |
| `grep` | 2848917 | LLGo · no LTO | 878720 | -69.2% |
| `grep` | 2848917 | LLGo · deadcode drop | 878720 | -69.2% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1312365 | -53.9% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 925675 | -67.5% |
| `glob` | 2257634 | LLGo · no LTO | 534953 | -76.3% |
| `glob` | 2257634 | LLGo · deadcode drop | 534953 | -76.3% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 968193 | -57.1% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 649838 | -71.2% |
| `json-wasi` | 3314587 | LLGo · no LTO | 1441945 | -56.5% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1441945 | -56.5% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2510406 | -24.3% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1671562 | -49.6% |
| `llimport` | 8423078 | LLGo · no LTO | 6719930 | -20.2% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6719930 | -20.2% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 6878489 | -18.3% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6617100 | -21.4% |
| `path-report` | 2381190 | LLGo · no LTO | 645607 | -72.9% |
| `path-report` | 2381190 | LLGo · deadcode drop | 645607 | -72.9% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1075241 | -54.8% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 756454 | -68.2% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1062217 | -61.8% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1062217 | -61.8% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1745803 | -37.2% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1172559 | -57.8% |
| `word-count` | 2253620 | LLGo · no LTO | 528333 | -76.6% |
| `word-count` | 2253620 | LLGo · deadcode drop | 528333 | -76.6% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 921735 | -59.1% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 634070 | -71.9% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 4.773x | 10 |
| LLGo · deadcode drop | 4.773x | 10 |
| LLGo · full LTO (GlobalDCE off) | 7.572x | 10 |
| LLGo · full LTO + GlobalDCE | 5.269x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 542851 | +461.0% |
| `base64` | 96760 | LLGo · deadcode drop | 542851 | +461.0% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 849381 | +777.8% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 576074 | +495.4% |
| `checksum` | 92685 | LLGo · no LTO | 529247 | +471.0% |
| `checksum` | 92685 | LLGo · deadcode drop | 529247 | +471.0% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 833435 | +799.2% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 557175 | +501.1% |
| `conv-wasi` | 201149 | LLGo · no LTO | 895436 | +345.2% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 895436 | +345.2% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1566316 | +678.7% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 992412 | +393.4% |
| `fibonacci` | 62386 | LLGo · no LTO | 445709 | +614.4% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 445709 | +614.4% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 464344 | +644.3% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 420055 | +573.3% |
| `grep` | 303772 | LLGo · no LTO | 878720 | +189.3% |
| `grep` | 303772 | LLGo · deadcode drop | 878720 | +189.3% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1312365 | +332.0% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 925675 | +204.7% |
| `glob` | 93153 | LLGo · no LTO | 534953 | +474.3% |
| `glob` | 93153 | LLGo · deadcode drop | 534953 | +474.3% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 968193 | +939.4% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 649838 | +597.6% |
| `json-wasi` | 493590 | LLGo · no LTO | 1441945 | +192.1% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1441945 | +192.1% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2510406 | +408.6% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1671562 | +238.7% |
| `llimport` | — | LLGo · no LTO | 6719930 | — |
| `llimport` | — | LLGo · deadcode drop | 6719930 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 6878489 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6617100 | — |
| `path-report` | 116889 | LLGo · no LTO | 645607 | +452.3% |
| `path-report` | 116889 | LLGo · deadcode drop | 645607 | +452.3% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1075241 | +819.9% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 756454 | +547.2% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1062217 | +269.5% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1062217 | +269.5% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1745803 | +507.3% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1172559 | +307.9% |
| `word-count` | 86834 | LLGo · no LTO | 528333 | +508.4% |
| `word-count` | 86834 | LLGo · deadcode drop | 528333 | +508.4% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 921735 | +961.5% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 634070 | +630.2% |
