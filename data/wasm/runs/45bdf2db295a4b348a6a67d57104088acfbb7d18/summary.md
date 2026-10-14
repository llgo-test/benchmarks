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
| tsgo | TinyGo | optional | failed | [logs/tsgo.TinyGo.log](logs/tsgo.TinyGo.log) |

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
| tsgo | js/wasm | 1.27.0 | https://github.com/microsoft/TypeScript.git | c975de5011fb7dfb32a491cf3fcf02d4f811f50e | tsc/cmd/tsc |
| word-count | wasip1/wasm | 1.26.2 | - | - | word-count |
| word-count-js | js/wasm | 1.26.2 | - | - | word-count |

## js/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 1.030x | 12 |
| LLGo · deadcode drop | 0.667x | 12 |
| LLGo · full LTO (GlobalDCE off) | 0.925x | 12 |
| LLGo · full LTO + GlobalDCE | 0.622x | 12 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1960269 | -15.6% |
| `base64` | 2322402 | LLGo · deadcode drop | 1157202 | -50.2% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1741738 | -25.0% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1063864 | -54.2% |
| `checksum` | 2311672 | LLGo · no LTO | 1940686 | -16.0% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1130533 | -51.1% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1706824 | -26.2% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1029868 | -55.4% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 3075396 | +16.6% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1752497 | -33.6% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2746736 | +4.1% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1609847 | -39.0% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1705429 | -25.0% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 1049963 | -53.8% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1495557 | -34.2% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 962142 | -57.7% |
| `glob` | 2305059 | LLGo · no LTO | 2096431 | -9.1% |
| `glob` | 2305059 | LLGo · deadcode drop | 1254555 | -45.6% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1848352 | -19.8% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1147581 | -50.2% |
| `grep` | 2871426 | LLGo · no LTO | 2643615 | -7.9% |
| `grep` | 2871426 | LLGo · deadcode drop | 1690799 | -41.1% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2326790 | -19.0% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1562154 | -45.6% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4283688 | +28.3% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2561012 | -23.3% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3907758 | +17.1% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2523488 | -24.4% |
| `llimport` | 8440671 | LLGo · no LTO | 11424485 | +35.4% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9783191 | +15.9% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10447765 | +23.8% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 9105377 | +7.9% |
| `path-report` | 2428068 | LLGo · no LTO | 2431011 | +0.1% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1579219 | -35.0% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 2172330 | -10.5% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1462670 | -39.8% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3430812 | +22.0% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 2072724 | -26.3% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 3108417 | +10.6% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1948840 | -30.7% |
| `tsgo` | 50367588 | LLGo · no LTO | 73147974 | +45.2% |
| `tsgo` | 50367588 | LLGo · deadcode drop | 72136026 | +43.2% |
| `tsgo` | 50367588 | LLGo · full LTO (GlobalDCE off) | 71545695 | +42.0% |
| `tsgo` | 50367588 | LLGo · full LTO + GlobalDCE | 71219381 | +41.4% |
| `word-count` | 2300998 | LLGo · no LTO | 2056535 | -10.6% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1227582 | -46.7% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1807348 | -21.5% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1114344 | -51.6% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 12.517x | 10 |
| LLGo · deadcode drop | 7.561x | 10 |
| LLGo · full LTO (GlobalDCE off) | 11.128x | 10 |
| LLGo · full LTO + GlobalDCE | 7.002x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1960269 | +1037.7% |
| `base64` | 172302 | LLGo · deadcode drop | 1157202 | +571.6% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1741738 | +910.9% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1063864 | +517.4% |
| `checksum` | 169609 | LLGo · no LTO | 1940686 | +1044.2% |
| `checksum` | 169609 | LLGo · deadcode drop | 1130533 | +566.6% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1706824 | +906.3% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1029868 | +507.2% |
| `conv-wasi` | 165385 | LLGo · no LTO | 3075396 | +1759.5% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1752497 | +959.6% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2746736 | +1560.8% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1609847 | +873.4% |
| `fibonacci` | 141855 | LLGo · no LTO | 1705429 | +1102.2% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 1049963 | +640.2% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1495557 | +954.3% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 962142 | +578.3% |
| `glob` | 136553 | LLGo · no LTO | 2096431 | +1435.3% |
| `glob` | 136553 | LLGo · deadcode drop | 1254555 | +818.7% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1848352 | +1253.6% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1147581 | +740.4% |
| `grep` | 155984 | LLGo · no LTO | 2643615 | +1594.8% |
| `grep` | 155984 | LLGo · deadcode drop | 1690799 | +984.0% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2326790 | +1391.7% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1562154 | +901.5% |
| `json-wasi` | 525666 | LLGo · no LTO | 4283688 | +714.9% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2561012 | +387.2% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3907758 | +643.4% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2523488 | +380.1% |
| `llimport` | — | LLGo · no LTO | 11424485 | — |
| `llimport` | — | LLGo · deadcode drop | 9783191 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10447765 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 9105377 | — |
| `path-report` | 194133 | LLGo · no LTO | 2431011 | +1152.2% |
| `path-report` | 194133 | LLGo · deadcode drop | 1579219 | +713.5% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 2172330 | +1019.0% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1462670 | +653.4% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3430812 | +874.7% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 2072724 | +488.9% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 3108417 | +783.1% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1948840 | +453.7% |
| `tsgo` | — | LLGo · no LTO | 73147974 | — |
| `tsgo` | — | LLGo · deadcode drop | 72136026 | — |
| `tsgo` | — | LLGo · full LTO (GlobalDCE off) | 71545695 | — |
| `tsgo` | — | LLGo · full LTO + GlobalDCE | 71219381 | — |
| `word-count` | 164053 | LLGo · no LTO | 2056535 | +1153.6% |
| `word-count` | 164053 | LLGo · deadcode drop | 1227582 | +648.3% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1807348 | +1001.7% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1114344 | +579.3% |

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
