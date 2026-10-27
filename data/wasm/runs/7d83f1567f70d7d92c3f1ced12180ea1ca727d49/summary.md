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
| LLGo · no LTO | 0.997x | 11 |
| LLGo · deadcode drop | 0.621x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.888x | 11 |
| LLGo · full LTO + GlobalDCE | 0.575x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1960295 | -15.6% |
| `base64` | 2322402 | LLGo · deadcode drop | 1157242 | -50.2% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1741787 | -25.0% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1063948 | -54.2% |
| `checksum` | 2311672 | LLGo · no LTO | 1940705 | -16.0% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1130568 | -51.1% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1706880 | -26.2% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1029928 | -55.4% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 3055469 | +15.8% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1733013 | -34.3% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2728540 | +3.4% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1591955 | -39.7% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1705451 | -25.0% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 1050017 | -53.8% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1495614 | -34.2% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 962197 | -57.7% |
| `grep` | 2871426 | LLGo · no LTO | 2643618 | -7.9% |
| `grep` | 2871426 | LLGo · deadcode drop | 1690818 | -41.1% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2326810 | -19.0% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1562166 | -45.6% |
| `glob` | 2305059 | LLGo · no LTO | 2096463 | -9.0% |
| `glob` | 2305059 | LLGo · deadcode drop | 1254604 | -45.6% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1848404 | -19.8% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1147640 | -50.2% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4264748 | +27.7% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2542517 | -23.8% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3890235 | +16.5% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2506228 | -24.9% |
| `llimport` | 8440671 | LLGo · no LTO | 11404113 | +35.1% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9762603 | +15.7% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10428962 | +23.6% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 9086978 | +7.7% |
| `path-report` | 2428068 | LLGo · no LTO | 2431026 | +0.1% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1579255 | -35.0% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 2172370 | -10.5% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1462734 | -39.8% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3410890 | +21.3% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 2053236 | -27.0% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 3089878 | +9.9% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1930573 | -31.3% |
| `word-count` | 2300998 | LLGo · no LTO | 2056566 | -10.6% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1227621 | -46.6% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1807423 | -21.5% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1114413 | -51.6% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 12.496x | 10 |
| LLGo · deadcode drop | 7.540x | 10 |
| LLGo · full LTO (GlobalDCE off) | 11.109x | 10 |
| LLGo · full LTO + GlobalDCE | 6.983x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1960295 | +1037.7% |
| `base64` | 172302 | LLGo · deadcode drop | 1157242 | +571.6% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1741787 | +910.9% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1063948 | +517.5% |
| `checksum` | 169609 | LLGo · no LTO | 1940705 | +1044.2% |
| `checksum` | 169609 | LLGo · deadcode drop | 1130568 | +566.6% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1706880 | +906.4% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1029928 | +507.2% |
| `conv-wasi` | 165385 | LLGo · no LTO | 3055469 | +1747.5% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1733013 | +947.9% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2728540 | +1549.8% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1591955 | +862.6% |
| `fibonacci` | 141855 | LLGo · no LTO | 1705451 | +1102.2% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 1050017 | +640.2% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1495614 | +954.3% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 962197 | +578.3% |
| `grep` | 155984 | LLGo · no LTO | 2643618 | +1594.8% |
| `grep` | 155984 | LLGo · deadcode drop | 1690818 | +984.0% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2326810 | +1391.7% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1562166 | +901.5% |
| `glob` | 136553 | LLGo · no LTO | 2096463 | +1435.3% |
| `glob` | 136553 | LLGo · deadcode drop | 1254604 | +818.8% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1848404 | +1253.6% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1147640 | +740.4% |
| `json-wasi` | 525666 | LLGo · no LTO | 4264748 | +711.3% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2542517 | +383.7% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3890235 | +640.1% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2506228 | +376.8% |
| `llimport` | — | LLGo · no LTO | 11404113 | — |
| `llimport` | — | LLGo · deadcode drop | 9762603 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10428962 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 9086978 | — |
| `path-report` | 194133 | LLGo · no LTO | 2431026 | +1152.2% |
| `path-report` | 194133 | LLGo · deadcode drop | 1579255 | +713.5% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 2172370 | +1019.0% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1462734 | +653.5% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3410890 | +869.1% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 2053236 | +483.4% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 3089878 | +777.9% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1930573 | +448.5% |
| `word-count` | 164053 | LLGo · no LTO | 2056566 | +1153.6% |
| `word-count` | 164053 | LLGo · deadcode drop | 1227621 | +648.3% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1807423 | +1001.7% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1114413 | +579.3% |

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
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 2119709 | -18.7% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1279268 | -50.9% |
| `fibonacci` | 2230899 | LLGo · no LTO | 1348222 | -39.6% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 852706 | -61.8% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 1140503 | -48.9% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 743660 | -66.7% |
| `grep` | 2848917 | LLGo · no LTO | 2066462 | -27.5% |
| `grep` | 2848917 | LLGo · deadcode drop | 1367774 | -52.0% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1807039 | -36.6% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 1248705 | -56.2% |
| `glob` | 2257634 | LLGo · no LTO | 1677372 | -25.7% |
| `glob` | 2257634 | LLGo · deadcode drop | 1043656 | -53.8% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1438004 | -36.3% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 919812 | -59.3% |
| `json-wasi` | 3314587 | LLGo · no LTO | 3448503 | +4.0% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 2101692 | -36.6% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 3069242 | -7.4% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 2003760 | -39.5% |
| `llimport` | 8423078 | LLGo · no LTO | 9418890 | +11.8% |
| `llimport` | 8423078 | LLGo · deadcode drop | 8258350 | -2.0% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 8538882 | +1.4% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 7647079 | -9.2% |
| `path-report` | 2381190 | LLGo · no LTO | 1928130 | -19.0% |
| `path-report` | 2381190 | LLGo · deadcode drop | 1288925 | -45.9% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1680881 | -29.4% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 1156422 | -51.4% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 2680928 | -3.6% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1674428 | -39.8% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 2353421 | -15.4% |
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
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 2119709 | +953.8% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1279268 | +536.0% |
| `fibonacci` | 62386 | LLGo · no LTO | 1348222 | +2061.1% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 852706 | +1266.8% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 1140503 | +1728.1% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 743660 | +1092.0% |
| `grep` | 303772 | LLGo · no LTO | 2066462 | +580.3% |
| `grep` | 303772 | LLGo · deadcode drop | 1367774 | +350.3% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1807039 | +494.9% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 1248705 | +311.1% |
| `glob` | 93153 | LLGo · no LTO | 1677372 | +1700.7% |
| `glob` | 93153 | LLGo · deadcode drop | 1043656 | +1020.4% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1438004 | +1443.7% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 919812 | +887.4% |
| `json-wasi` | 493590 | LLGo · no LTO | 3448503 | +598.7% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 2101692 | +325.8% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 3069242 | +521.8% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 2003760 | +306.0% |
| `llimport` | — | LLGo · no LTO | 9418890 | — |
| `llimport` | — | LLGo · deadcode drop | 8258350 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 8538882 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 7647079 | — |
| `path-report` | 116889 | LLGo · no LTO | 1928130 | +1549.5% |
| `path-report` | 116889 | LLGo · deadcode drop | 1288925 | +1002.7% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1680881 | +1338.0% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 1156422 | +889.3% |
| `sha-wasi` | 287449 | LLGo · no LTO | 2680928 | +832.7% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1674428 | +482.5% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 2353421 | +718.7% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1505517 | +423.8% |
| `word-count` | 86834 | LLGo · no LTO | 1644469 | +1793.8% |
| `word-count` | 86834 | LLGo · deadcode drop | 1019795 | +1074.4% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 1406394 | +1519.6% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 893395 | +928.9% |
