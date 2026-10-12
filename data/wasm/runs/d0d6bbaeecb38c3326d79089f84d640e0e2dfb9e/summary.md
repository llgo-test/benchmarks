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
| `base64` | 2322402 | LLGo · no LTO | 1957156 | -15.7% |
| `base64` | 2322402 | LLGo · deadcode drop | 1154100 | -50.3% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1738924 | -25.1% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1061057 | -54.3% |
| `checksum` | 2311672 | LLGo · no LTO | 1937573 | -16.2% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1127443 | -51.2% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1704044 | -26.3% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1027077 | -55.6% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 3072337 | +16.4% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1749432 | -33.7% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2744002 | +4.0% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1607105 | -39.1% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1702308 | -25.2% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 1046855 | -54.0% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1492780 | -34.4% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 959362 | -57.8% |
| `grep` | 2871426 | LLGo · no LTO | 2640518 | -8.0% |
| `grep` | 2871426 | LLGo · deadcode drop | 1687724 | -41.2% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2323999 | -19.1% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1559371 | -45.7% |
| `glob` | 2305059 | LLGo · no LTO | 2093320 | -9.2% |
| `glob` | 2305059 | LLGo · deadcode drop | 1251451 | -45.7% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1845566 | -19.9% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1144803 | -50.3% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4280659 | +28.2% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2557965 | -23.4% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3904995 | +17.0% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2520713 | -24.5% |
| `llimport` | 8440671 | LLGo · no LTO | 11421415 | +35.3% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9780168 | +15.9% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10444603 | +23.7% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 9102324 | +7.8% |
| `path-report` | 2428068 | LLGo · no LTO | 2427896 | -0.0% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1576119 | -35.1% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 2169549 | -10.6% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1459901 | -39.9% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3427734 | +21.9% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 2069671 | -26.4% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 3105608 | +10.5% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1945997 | -30.8% |
| `word-count` | 2300998 | LLGo · no LTO | 2053435 | -10.8% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1224496 | -46.8% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1804576 | -21.6% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1111567 | -51.7% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 12.501x | 10 |
| LLGo · deadcode drop | 7.545x | 10 |
| LLGo · full LTO (GlobalDCE off) | 11.113x | 10 |
| LLGo · full LTO + GlobalDCE | 6.987x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1957156 | +1035.9% |
| `base64` | 172302 | LLGo · deadcode drop | 1154100 | +569.8% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1738924 | +909.2% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1061057 | +515.8% |
| `checksum` | 169609 | LLGo · no LTO | 1937573 | +1042.4% |
| `checksum` | 169609 | LLGo · deadcode drop | 1127443 | +564.7% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1704044 | +904.7% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1027077 | +505.6% |
| `conv-wasi` | 165385 | LLGo · no LTO | 3072337 | +1757.7% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1749432 | +957.8% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2744002 | +1559.2% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1607105 | +871.7% |
| `fibonacci` | 141855 | LLGo · no LTO | 1702308 | +1100.0% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 1046855 | +638.0% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1492780 | +952.3% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 959362 | +576.3% |
| `grep` | 155984 | LLGo · no LTO | 2640518 | +1592.8% |
| `grep` | 155984 | LLGo · deadcode drop | 1687724 | +982.0% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2323999 | +1389.9% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1559371 | +899.7% |
| `glob` | 136553 | LLGo · no LTO | 2093320 | +1433.0% |
| `glob` | 136553 | LLGo · deadcode drop | 1251451 | +816.5% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1845566 | +1251.5% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1144803 | +738.4% |
| `json-wasi` | 525666 | LLGo · no LTO | 4280659 | +714.3% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2557965 | +386.6% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3904995 | +642.9% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2520713 | +379.5% |
| `llimport` | — | LLGo · no LTO | 11421415 | — |
| `llimport` | — | LLGo · deadcode drop | 9780168 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10444603 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 9102324 | — |
| `path-report` | 194133 | LLGo · no LTO | 2427896 | +1150.6% |
| `path-report` | 194133 | LLGo · deadcode drop | 1576119 | +711.9% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 2169549 | +1017.6% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1459901 | +652.0% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3427734 | +873.9% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 2069671 | +488.0% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 3105608 | +782.3% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1945997 | +452.9% |
| `word-count` | 164053 | LLGo · no LTO | 2053435 | +1151.7% |
| `word-count` | 164053 | LLGo · deadcode drop | 1224496 | +646.4% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1804576 | +1000.0% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1111567 | +577.6% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.803x | 11 |
| LLGo · deadcode drop | 0.516x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.698x | 11 |
| LLGo · full LTO + GlobalDCE | 0.462x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1528973 | -32.8% |
| `base64` | 2275731 | LLGo · deadcode drop | 927199 | -59.3% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 1309742 | -42.4% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 814027 | -64.2% |
| `checksum` | 2264417 | LLGo · no LTO | 1515680 | -33.1% |
| `checksum` | 2264417 | LLGo · deadcode drop | 908774 | -59.9% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 1291341 | -43.0% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 794607 | -64.9% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 2419223 | -7.2% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 1431159 | -45.1% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 2116975 | -18.8% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1276537 | -51.1% |
| `fibonacci` | 2230899 | LLGo · no LTO | 1344914 | -39.7% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 849398 | -61.9% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 1137729 | -49.0% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 740889 | -66.8% |
| `grep` | 2848917 | LLGo · no LTO | 2063154 | -27.6% |
| `grep` | 2848917 | LLGo · deadcode drop | 1364466 | -52.1% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1804265 | -36.7% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 1245934 | -56.3% |
| `glob` | 2257634 | LLGo · no LTO | 1674064 | -25.8% |
| `glob` | 2257634 | LLGo · deadcode drop | 1040348 | -53.9% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1435230 | -36.4% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 917041 | -59.4% |
| `json-wasi` | 3314587 | LLGo · no LTO | 3445227 | +3.9% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 2098416 | -36.7% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 3066508 | -7.5% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 2001029 | -39.6% |
| `llimport` | 8423078 | LLGo · no LTO | 9415635 | +11.8% |
| `llimport` | 8423078 | LLGo · deadcode drop | 8255095 | -2.0% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 8536156 | +1.3% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 7644354 | -9.2% |
| `path-report` | 2381190 | LLGo · no LTO | 1924822 | -19.2% |
| `path-report` | 2381190 | LLGo · deadcode drop | 1285617 | -46.0% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1678107 | -29.5% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 1153651 | -51.6% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 2677652 | -3.7% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1671152 | -39.9% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 2350687 | -15.5% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1502784 | -46.0% |
| `word-count` | 2253620 | LLGo · no LTO | 1641161 | -27.2% |
| `word-count` | 2253620 | LLGo · deadcode drop | 1016487 | -54.9% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 1403620 | -37.7% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 890624 | -60.5% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 13.240x | 10 |
| LLGo · deadcode drop | 8.246x | 10 |
| LLGo · full LTO (GlobalDCE off) | 11.460x | 10 |
| LLGo · full LTO + GlobalDCE | 7.367x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1528973 | +1480.2% |
| `base64` | 96760 | LLGo · deadcode drop | 927199 | +858.2% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 1309742 | +1253.6% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 814027 | +741.3% |
| `checksum` | 92685 | LLGo · no LTO | 1515680 | +1535.3% |
| `checksum` | 92685 | LLGo · deadcode drop | 908774 | +880.5% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 1291341 | +1293.3% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 794607 | +757.3% |
| `conv-wasi` | 201149 | LLGo · no LTO | 2419223 | +1102.7% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 1431159 | +611.5% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 2116975 | +952.4% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1276537 | +534.6% |
| `fibonacci` | 62386 | LLGo · no LTO | 1344914 | +2055.8% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 849398 | +1261.5% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 1137729 | +1723.7% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 740889 | +1087.6% |
| `grep` | 303772 | LLGo · no LTO | 2063154 | +579.2% |
| `grep` | 303772 | LLGo · deadcode drop | 1364466 | +349.2% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1804265 | +494.0% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 1245934 | +310.2% |
| `glob` | 93153 | LLGo · no LTO | 1674064 | +1697.1% |
| `glob` | 93153 | LLGo · deadcode drop | 1040348 | +1016.8% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1435230 | +1440.7% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 917041 | +884.4% |
| `json-wasi` | 493590 | LLGo · no LTO | 3445227 | +598.0% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 2098416 | +325.1% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 3066508 | +521.3% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 2001029 | +305.4% |
| `llimport` | — | LLGo · no LTO | 9415635 | — |
| `llimport` | — | LLGo · deadcode drop | 8255095 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 8536156 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 7644354 | — |
| `path-report` | 116889 | LLGo · no LTO | 1924822 | +1546.7% |
| `path-report` | 116889 | LLGo · deadcode drop | 1285617 | +999.9% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1678107 | +1335.6% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 1153651 | +887.0% |
| `sha-wasi` | 287449 | LLGo · no LTO | 2677652 | +831.5% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1671152 | +481.4% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 2350687 | +717.8% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1502784 | +422.8% |
| `word-count` | 86834 | LLGo · no LTO | 1641161 | +1790.0% |
| `word-count` | 86834 | LLGo · deadcode drop | 1016487 | +1070.6% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 1403620 | +1516.4% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 890624 | +925.7% |
