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
| LLGo · full LTO (GlobalDCE off) | 0.889x | 11 |
| LLGo · full LTO + GlobalDCE | 0.576x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1960567 | -15.6% |
| `base64` | 2322402 | LLGo · deadcode drop | 1157501 | -50.2% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1742213 | -25.0% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1064358 | -54.2% |
| `checksum` | 2311672 | LLGo · no LTO | 1940974 | -16.0% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1130874 | -51.1% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1707347 | -26.1% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1030364 | -55.4% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 3055795 | +15.8% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1733279 | -34.3% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2729021 | +3.4% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1592419 | -39.6% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1705713 | -25.0% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 1050268 | -53.8% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1496068 | -34.2% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 962649 | -57.7% |
| `grep` | 2871426 | LLGo · no LTO | 2643941 | -7.9% |
| `grep` | 2871426 | LLGo · deadcode drop | 1691142 | -41.1% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2327322 | -18.9% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1562666 | -45.6% |
| `glob` | 2305059 | LLGo · no LTO | 2096766 | -9.0% |
| `glob` | 2305059 | LLGo · deadcode drop | 1254891 | -45.6% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1848884 | -19.8% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1148092 | -50.2% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4265136 | +27.8% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2542902 | -23.8% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3890787 | +16.5% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2506819 | -24.9% |
| `llimport` | 8440671 | LLGo · no LTO | 11405760 | +35.1% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9764266 | +15.7% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10430079 | +23.6% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 9088038 | +7.7% |
| `path-report` | 2428068 | LLGo · no LTO | 2431326 | +0.1% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1579558 | -34.9% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 2172856 | -10.5% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1463206 | -39.7% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3411178 | +21.3% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 2053536 | -26.9% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 3090342 | +9.9% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1930997 | -31.3% |
| `word-count` | 2300998 | LLGo · no LTO | 2056861 | -10.6% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1227920 | -46.6% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1807894 | -21.4% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1114875 | -51.5% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 12.498x | 10 |
| LLGo · deadcode drop | 7.542x | 10 |
| LLGo · full LTO (GlobalDCE off) | 11.111x | 10 |
| LLGo · full LTO + GlobalDCE | 6.986x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1960567 | +1037.9% |
| `base64` | 172302 | LLGo · deadcode drop | 1157501 | +571.8% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1742213 | +911.1% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1064358 | +517.7% |
| `checksum` | 169609 | LLGo · no LTO | 1940974 | +1044.4% |
| `checksum` | 169609 | LLGo · deadcode drop | 1130874 | +566.8% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1707347 | +906.6% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1030364 | +507.5% |
| `conv-wasi` | 165385 | LLGo · no LTO | 3055795 | +1747.7% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1733279 | +948.0% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2729021 | +1550.1% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1592419 | +862.9% |
| `fibonacci` | 141855 | LLGo · no LTO | 1705713 | +1102.4% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 1050268 | +640.4% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1496068 | +954.6% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 962649 | +578.6% |
| `grep` | 155984 | LLGo · no LTO | 2643941 | +1595.0% |
| `grep` | 155984 | LLGo · deadcode drop | 1691142 | +984.2% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2327322 | +1392.0% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1562666 | +901.8% |
| `glob` | 136553 | LLGo · no LTO | 2096766 | +1435.5% |
| `glob` | 136553 | LLGo · deadcode drop | 1254891 | +819.0% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1848884 | +1254.0% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1148092 | +740.8% |
| `json-wasi` | 525666 | LLGo · no LTO | 4265136 | +711.4% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2542902 | +383.7% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3890787 | +640.2% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2506819 | +376.9% |
| `llimport` | — | LLGo · no LTO | 11405760 | — |
| `llimport` | — | LLGo · deadcode drop | 9764266 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10430079 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 9088038 | — |
| `path-report` | 194133 | LLGo · no LTO | 2431326 | +1152.4% |
| `path-report` | 194133 | LLGo · deadcode drop | 1579558 | +713.6% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 2172856 | +1019.3% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1463206 | +653.7% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3411178 | +869.2% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 2053536 | +483.4% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 3090342 | +778.0% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1930997 | +448.6% |
| `word-count` | 164053 | LLGo · no LTO | 2056861 | +1153.8% |
| `word-count` | 164053 | LLGo · deadcode drop | 1227920 | +648.5% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1807894 | +1002.0% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1114875 | +579.6% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.804x | 11 |
| LLGo · deadcode drop | 0.517x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.699x | 11 |
| LLGo · full LTO + GlobalDCE | 0.463x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1532306 | -32.7% |
| `base64` | 2275731 | LLGo · deadcode drop | 930516 | -59.1% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 1312540 | -42.3% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 816822 | -64.1% |
| `checksum` | 2264417 | LLGo · no LTO | 1519013 | -32.9% |
| `checksum` | 2264417 | LLGo · deadcode drop | 912107 | -59.7% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 1294131 | -42.8% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 797394 | -64.8% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 2422508 | -7.1% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 1434444 | -45.0% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 2119860 | -18.7% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1279292 | -50.9% |
| `fibonacci` | 2230899 | LLGo · no LTO | 1348231 | -39.6% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 852731 | -61.8% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 1140527 | -48.9% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 743684 | -66.7% |
| `grep` | 2848917 | LLGo · no LTO | 2066503 | -27.5% |
| `grep` | 2848917 | LLGo · deadcode drop | 1367815 | -52.0% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1807087 | -36.6% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 1248753 | -56.2% |
| `glob` | 2257634 | LLGo · no LTO | 1677397 | -25.7% |
| `glob` | 2257634 | LLGo · deadcode drop | 1043697 | -53.8% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1438044 | -36.3% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 919860 | -59.3% |
| `json-wasi` | 3314587 | LLGo · no LTO | 3448544 | +4.0% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 2101733 | -36.6% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 3069448 | -7.4% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 2003808 | -39.5% |
| `llimport` | 8423078 | LLGo · no LTO | 9420112 | +11.8% |
| `llimport` | 8423078 | LLGo · deadcode drop | 8259572 | -1.9% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 8539553 | +1.4% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 7647750 | -9.2% |
| `path-report` | 2381190 | LLGo · no LTO | 1928171 | -19.0% |
| `path-report` | 2381190 | LLGo · deadcode drop | 1288966 | -45.9% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1680929 | -29.4% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 1156470 | -51.4% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 2680969 | -3.6% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1674469 | -39.8% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 2353600 | -15.4% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1505557 | -45.9% |
| `word-count` | 2253620 | LLGo · no LTO | 1644510 | -27.0% |
| `word-count` | 2253620 | LLGo · deadcode drop | 1019836 | -54.7% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 1406442 | -37.6% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 893443 | -60.4% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 13.263x | 10 |
| LLGo · deadcode drop | 8.269x | 10 |
| LLGo · full LTO (GlobalDCE off) | 11.480x | 10 |
| LLGo · full LTO + GlobalDCE | 7.387x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1532306 | +1483.6% |
| `base64` | 96760 | LLGo · deadcode drop | 930516 | +861.7% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 1312540 | +1256.5% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 816822 | +744.2% |
| `checksum` | 92685 | LLGo · no LTO | 1519013 | +1538.9% |
| `checksum` | 92685 | LLGo · deadcode drop | 912107 | +884.1% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 1294131 | +1296.3% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 797394 | +760.3% |
| `conv-wasi` | 201149 | LLGo · no LTO | 2422508 | +1104.3% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 1434444 | +613.1% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 2119860 | +953.9% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1279292 | +536.0% |
| `fibonacci` | 62386 | LLGo · no LTO | 1348231 | +2061.1% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 852731 | +1266.9% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 1140527 | +1728.2% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 743684 | +1092.1% |
| `grep` | 303772 | LLGo · no LTO | 2066503 | +580.3% |
| `grep` | 303772 | LLGo · deadcode drop | 1367815 | +350.3% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1807087 | +494.9% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 1248753 | +311.1% |
| `glob` | 93153 | LLGo · no LTO | 1677397 | +1700.7% |
| `glob` | 93153 | LLGo · deadcode drop | 1043697 | +1020.4% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1438044 | +1443.7% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 919860 | +887.5% |
| `json-wasi` | 493590 | LLGo · no LTO | 3448544 | +598.7% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 2101733 | +325.8% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 3069448 | +521.9% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 2003808 | +306.0% |
| `llimport` | — | LLGo · no LTO | 9420112 | — |
| `llimport` | — | LLGo · deadcode drop | 8259572 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 8539553 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 7647750 | — |
| `path-report` | 116889 | LLGo · no LTO | 1928171 | +1549.6% |
| `path-report` | 116889 | LLGo · deadcode drop | 1288966 | +1002.7% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1680929 | +1338.1% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 1156470 | +889.4% |
| `sha-wasi` | 287449 | LLGo · no LTO | 2680969 | +832.7% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1674469 | +482.5% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 2353600 | +718.8% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1505557 | +423.8% |
| `word-count` | 86834 | LLGo · no LTO | 1644510 | +1793.9% |
| `word-count` | 86834 | LLGo · deadcode drop | 1019836 | +1074.5% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 1406442 | +1519.7% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 893443 | +928.9% |
