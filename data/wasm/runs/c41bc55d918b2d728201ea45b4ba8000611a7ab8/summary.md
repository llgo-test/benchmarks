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
| base64-js | js/wasm | 1.26.2 | - | - | base64 |
| checksum | wasip1/wasm | 1.26.2 | - | - | checksum |
| checksum-js | js/wasm | 1.26.2 | - | - | checksum |
| convolution | wasip1/wasm | 1.26.2 | https://github.com/universonic/go-rust-wasm-bench.git | 6d1b98c971d6206c313a6d1233d9f2687c50febe | go/cmd/conv-wasi |
| convolution-js | js/wasm | 1.26.2 | https://github.com/universonic/go-rust-wasm-bench.git | 6d1b98c971d6206c313a6d1233d9f2687c50febe | go/cmd/conv-wasi |
| fibonacci | wasip1/wasm | 1.26.2 | https://github.com/mattn/wasi-benchmark.git | c7d73b7b1e03b352791f91ed207c6b9c79559453 | main.go |
| fibonacci-js | js/wasm | 1.26.2 | https://github.com/mattn/wasi-benchmark.git | c7d73b7b1e03b352791f91ed207c6b9c79559453 | main.go |
| glob | wasip1/wasm | 1.26.2 | - | - | glob |
| glob-js | js/wasm | 1.26.2 | - | - | glob |
| grep | wasip1/wasm | 1.26.2 | - | - | grep |
| grep-js | js/wasm | 1.26.2 | - | - | grep |
| json-roundtrip | wasip1/wasm | 1.26.2 | https://github.com/universonic/go-rust-wasm-bench.git | 6d1b98c971d6206c313a6d1233d9f2687c50febe | go/cmd/json-wasi |
| json-roundtrip-js | js/wasm | 1.26.2 | https://github.com/universonic/go-rust-wasm-bench.git | 6d1b98c971d6206c313a6d1233d9f2687c50febe | go/cmd/json-wasi |
| llimport | wasip1/wasm | 1.27.0 | https://github.com/goplus/llcppg.git | d62a300b00d567ce2737ab085cef18c06d43f7d7 | cmd/llimport |
| llimport-js | js/wasm | 1.27.0 | https://github.com/goplus/llcppg.git | d62a300b00d567ce2737ab085cef18c06d43f7d7 | cmd/llimport |
| path-report | wasip1/wasm | 1.26.2 | - | - | path-report |
| path-report-js | js/wasm | 1.26.2 | - | - | path-report |
| sha256 | wasip1/wasm | 1.26.2 | https://github.com/universonic/go-rust-wasm-bench.git | 6d1b98c971d6206c313a6d1233d9f2687c50febe | go/cmd/sha-wasi |
| sha256-js | js/wasm | 1.26.2 | https://github.com/universonic/go-rust-wasm-bench.git | 6d1b98c971d6206c313a6d1233d9f2687c50febe | go/cmd/sha-wasi |
| word-count | wasip1/wasm | 1.26.2 | - | - | word-count |
| word-count-js | js/wasm | 1.26.2 | - | - | word-count |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.804x | 11 |
| LLGo · deadcode drop | 0.517x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.699x | 11 |
| LLGo · full LTO + GlobalDCE | 0.463x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1532281 | -32.7% |
| `base64` | 2275731 | LLGo · deadcode drop | 930507 | -59.1% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 1312516 | -42.3% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 816798 | -64.1% |
| `checksum` | 2264417 | LLGo · no LTO | 1518988 | -32.9% |
| `checksum` | 2264417 | LLGo · deadcode drop | 912082 | -59.7% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 1294115 | -42.8% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 797378 | -64.8% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 2422483 | -7.1% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 1434419 | -45.0% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 2119836 | -18.7% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1279268 | -50.9% |
| `fibonacci` | 2230899 | LLGo · no LTO | 1348222 | -39.6% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 852706 | -61.8% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 1140503 | -48.9% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 743660 | -66.7% |
| `glob` | 2257634 | LLGo · no LTO | 1677372 | -25.7% |
| `glob` | 2257634 | LLGo · deadcode drop | 1043656 | -53.8% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1438004 | -36.3% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 919812 | -59.3% |
| `grep` | 2848917 | LLGo · no LTO | 2066462 | -27.5% |
| `grep` | 2848917 | LLGo · deadcode drop | 1367774 | -52.0% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1807039 | -36.6% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 1248705 | -56.2% |
| `json-wasi` | 3314587 | LLGo · no LTO | 3448503 | +4.0% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 2101692 | -36.6% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 3069400 | -7.4% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 2003760 | -39.5% |
| `llimport` | 8423078 | LLGo · no LTO | 9418890 | +11.8% |
| `llimport` | 8423078 | LLGo · deadcode drop | 8258350 | -2.0% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 8539040 | +1.4% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 7647237 | -9.2% |
| `path-report` | 2381190 | LLGo · no LTO | 1928130 | -19.0% |
| `path-report` | 2381190 | LLGo · deadcode drop | 1288925 | -45.9% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1680881 | -29.4% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 1156422 | -51.4% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 2680928 | -3.6% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1674428 | -39.8% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 2353552 | -15.4% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1505517 | -45.9% |
| `word-count` | 2253620 | LLGo · no LTO | 1644469 | -27.0% |
| `word-count` | 2253620 | LLGo · deadcode drop | 1019795 | -54.7% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 1406394 | -37.6% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 893395 | -60.4% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 13.263x | 10 |
| LLGo · deadcode drop | 8.269x | 10 |
| LLGo · full LTO (GlobalDCE off) | 11.479x | 10 |
| LLGo · full LTO + GlobalDCE | 7.387x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1532281 | +1483.6% |
| `base64` | 96760 | LLGo · deadcode drop | 930507 | +861.7% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 1312516 | +1256.5% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 816798 | +744.1% |
| `checksum` | 92685 | LLGo · no LTO | 1518988 | +1538.9% |
| `checksum` | 92685 | LLGo · deadcode drop | 912082 | +884.1% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 1294115 | +1296.3% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 797378 | +760.3% |
| `conv-wasi` | 201149 | LLGo · no LTO | 2422483 | +1104.3% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 1434419 | +613.1% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 2119836 | +953.9% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1279268 | +536.0% |
| `fibonacci` | 62386 | LLGo · no LTO | 1348222 | +2061.1% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 852706 | +1266.8% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 1140503 | +1728.1% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 743660 | +1092.0% |
| `glob` | 93153 | LLGo · no LTO | 1677372 | +1700.7% |
| `glob` | 93153 | LLGo · deadcode drop | 1043656 | +1020.4% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1438004 | +1443.7% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 919812 | +887.4% |
| `grep` | 303772 | LLGo · no LTO | 2066462 | +580.3% |
| `grep` | 303772 | LLGo · deadcode drop | 1367774 | +350.3% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1807039 | +494.9% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 1248705 | +311.1% |
| `json-wasi` | 493590 | LLGo · no LTO | 3448503 | +598.7% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 2101692 | +325.8% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 3069400 | +521.9% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 2003760 | +306.0% |
| `llimport` | — | LLGo · no LTO | 9418890 | — |
| `llimport` | — | LLGo · deadcode drop | 8258350 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 8539040 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 7647237 | — |
| `path-report` | 116889 | LLGo · no LTO | 1928130 | +1549.5% |
| `path-report` | 116889 | LLGo · deadcode drop | 1288925 | +1002.7% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1680881 | +1338.0% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 1156422 | +889.3% |
| `sha-wasi` | 287449 | LLGo · no LTO | 2680928 | +832.7% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1674428 | +482.5% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 2353552 | +718.8% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1505517 | +423.8% |
| `word-count` | 86834 | LLGo · no LTO | 1644469 | +1793.8% |
| `word-count` | 86834 | LLGo · deadcode drop | 1019795 | +1074.4% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 1406394 | +1519.6% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 893395 | +928.9% |

## js/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.997x | 11 |
| LLGo · deadcode drop | 0.621x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.889x | 11 |
| LLGo · full LTO + GlobalDCE | 0.575x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1960519 | -15.6% |
| `base64` | 2322402 | LLGo · deadcode drop | 1157466 | -50.2% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1742154 | -25.0% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1064315 | -54.2% |
| `checksum` | 2311672 | LLGo · no LTO | 1940929 | -16.0% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1130792 | -51.1% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1707273 | -26.1% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1030321 | -55.4% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 3055693 | +15.8% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1733237 | -34.3% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2728933 | +3.4% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1592348 | -39.6% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1705675 | -25.0% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 1050241 | -53.8% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1496007 | -34.2% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 962590 | -57.7% |
| `glob` | 2305059 | LLGo · no LTO | 2096687 | -9.0% |
| `glob` | 2305059 | LLGo · deadcode drop | 1254828 | -45.6% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1848797 | -19.8% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1148033 | -50.2% |
| `grep` | 2871426 | LLGo · no LTO | 2643842 | -7.9% |
| `grep` | 2871426 | LLGo · deadcode drop | 1691042 | -41.1% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2327203 | -19.0% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1562559 | -45.6% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4264972 | +27.8% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2542741 | -23.8% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3890602 | +16.5% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2506595 | -24.9% |
| `llimport` | 8440671 | LLGo · no LTO | 11404337 | +35.1% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9762827 | +15.7% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10429325 | +23.6% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 9087341 | +7.7% |
| `path-report` | 2428068 | LLGo · no LTO | 2431250 | +0.1% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1579479 | -34.9% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 2172763 | -10.5% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1463127 | -39.7% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3411114 | +21.3% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 2053460 | -27.0% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 3090249 | +9.9% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1930944 | -31.3% |
| `word-count` | 2300998 | LLGo · no LTO | 2056790 | -10.6% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1227845 | -46.6% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1807816 | -21.4% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1114806 | -51.6% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 12.497x | 10 |
| LLGo · deadcode drop | 7.541x | 10 |
| LLGo · full LTO (GlobalDCE off) | 11.111x | 10 |
| LLGo · full LTO + GlobalDCE | 6.985x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1960519 | +1037.8% |
| `base64` | 172302 | LLGo · deadcode drop | 1157466 | +571.8% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1742154 | +911.1% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1064315 | +517.7% |
| `checksum` | 169609 | LLGo · no LTO | 1940929 | +1044.4% |
| `checksum` | 169609 | LLGo · deadcode drop | 1130792 | +566.7% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1707273 | +906.6% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1030321 | +507.5% |
| `conv-wasi` | 165385 | LLGo · no LTO | 3055693 | +1747.6% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1733237 | +948.0% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2728933 | +1550.0% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1592348 | +862.8% |
| `fibonacci` | 141855 | LLGo · no LTO | 1705675 | +1102.4% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 1050241 | +640.4% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1496007 | +954.6% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 962590 | +578.6% |
| `glob` | 136553 | LLGo · no LTO | 2096687 | +1435.4% |
| `glob` | 136553 | LLGo · deadcode drop | 1254828 | +818.9% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1848797 | +1253.9% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1148033 | +740.7% |
| `grep` | 155984 | LLGo · no LTO | 2643842 | +1594.9% |
| `grep` | 155984 | LLGo · deadcode drop | 1691042 | +984.1% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2327203 | +1391.9% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1562559 | +901.7% |
| `json-wasi` | 525666 | LLGo · no LTO | 4264972 | +711.3% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2542741 | +383.7% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3890602 | +640.1% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2506595 | +376.8% |
| `llimport` | — | LLGo · no LTO | 11404337 | — |
| `llimport` | — | LLGo · deadcode drop | 9762827 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10429325 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 9087341 | — |
| `path-report` | 194133 | LLGo · no LTO | 2431250 | +1152.4% |
| `path-report` | 194133 | LLGo · deadcode drop | 1579479 | +713.6% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 2172763 | +1019.2% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1463127 | +653.7% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3411114 | +869.1% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 2053460 | +483.4% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 3090249 | +778.0% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1930944 | +448.6% |
| `word-count` | 164053 | LLGo · no LTO | 2056790 | +1153.7% |
| `word-count` | 164053 | LLGo · deadcode drop | 1227845 | +648.4% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1807816 | +1002.0% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1114806 | +579.5% |
