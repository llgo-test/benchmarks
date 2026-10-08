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
| LLGo · no LTO | 1.003x | 11 |
| LLGo · deadcode drop | 0.626x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.894x | 11 |
| LLGo · full LTO + GlobalDCE | 0.580x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1958183 | -15.7% |
| `base64` | 2322402 | LLGo · deadcode drop | 1155124 | -50.3% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1739833 | -25.1% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1061924 | -54.3% |
| `checksum` | 2311672 | LLGo · no LTO | 1938593 | -16.1% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1128467 | -51.2% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1704937 | -26.2% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1027968 | -55.5% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 3080851 | +16.8% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1757859 | -33.4% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2752241 | +4.3% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1615231 | -38.8% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1703282 | -25.1% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 1047814 | -53.9% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1493579 | -34.3% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 960148 | -57.8% |
| `grep` | 2871426 | LLGo · no LTO | 2649677 | -7.7% |
| `grep` | 2871426 | LLGo · deadcode drop | 1696879 | -40.9% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2332978 | -18.8% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1568319 | -45.4% |
| `glob` | 2305059 | LLGo · no LTO | 2099135 | -8.9% |
| `glob` | 2305059 | LLGo · deadcode drop | 1257538 | -45.4% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1851262 | -19.7% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1150472 | -50.1% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4302518 | +28.9% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2579780 | -22.7% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3926286 | +17.6% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2541847 | -23.9% |
| `llimport` | 8440671 | LLGo · no LTO | 11834787 | +40.2% |
| `llimport` | 8440671 | LLGo · deadcode drop | 10194984 | +20.8% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10837507 | +28.4% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 9502928 | +12.6% |
| `path-report` | 2428068 | LLGo · no LTO | 2433968 | +0.2% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1582200 | -34.8% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 2175243 | -10.4% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1465549 | -39.6% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3436944 | +22.3% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 2078791 | -26.1% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 3114787 | +10.8% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1955118 | -30.5% |
| `word-count` | 2300998 | LLGo · no LTO | 2059260 | -10.5% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1230292 | -46.5% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1810267 | -21.3% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1117236 | -51.4% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 12.531x | 10 |
| LLGo · deadcode drop | 7.574x | 10 |
| LLGo · full LTO (GlobalDCE off) | 11.141x | 10 |
| LLGo · full LTO + GlobalDCE | 7.016x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1958183 | +1036.5% |
| `base64` | 172302 | LLGo · deadcode drop | 1155124 | +570.4% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1739833 | +909.8% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1061924 | +516.3% |
| `checksum` | 169609 | LLGo · no LTO | 1938593 | +1043.0% |
| `checksum` | 169609 | LLGo · deadcode drop | 1128467 | +565.3% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1704937 | +905.2% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1027968 | +506.1% |
| `conv-wasi` | 165385 | LLGo · no LTO | 3080851 | +1762.8% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1757859 | +962.9% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2752241 | +1564.1% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1615231 | +876.6% |
| `fibonacci` | 141855 | LLGo · no LTO | 1703282 | +1100.7% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 1047814 | +638.7% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1493579 | +952.9% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 960148 | +576.9% |
| `grep` | 155984 | LLGo · no LTO | 2649677 | +1598.7% |
| `grep` | 155984 | LLGo · deadcode drop | 1696879 | +987.9% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2332978 | +1395.7% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1568319 | +905.4% |
| `glob` | 136553 | LLGo · no LTO | 2099135 | +1437.2% |
| `glob` | 136553 | LLGo · deadcode drop | 1257538 | +820.9% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1851262 | +1255.7% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1150472 | +742.5% |
| `json-wasi` | 525666 | LLGo · no LTO | 4302518 | +718.5% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2579780 | +390.8% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3926286 | +646.9% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2541847 | +383.5% |
| `llimport` | — | LLGo · no LTO | 11834787 | — |
| `llimport` | — | LLGo · deadcode drop | 10194984 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10837507 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 9502928 | — |
| `path-report` | 194133 | LLGo · no LTO | 2433968 | +1153.8% |
| `path-report` | 194133 | LLGo · deadcode drop | 1582200 | +715.0% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 2175243 | +1020.5% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1465549 | +654.9% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3436944 | +876.5% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 2078791 | +490.6% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 3114787 | +785.0% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1955118 | +455.5% |
| `word-count` | 164053 | LLGo · no LTO | 2059260 | +1155.2% |
| `word-count` | 164053 | LLGo · deadcode drop | 1230292 | +649.9% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1810267 | +1003.5% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1117236 | +581.0% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.809x | 11 |
| LLGo · deadcode drop | 0.522x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.704x | 11 |
| LLGo · full LTO + GlobalDCE | 0.468x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1530728 | -32.7% |
| `base64` | 2275731 | LLGo · deadcode drop | 928938 | -59.2% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 1311291 | -42.4% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 815519 | -64.2% |
| `checksum` | 2264417 | LLGo · no LTO | 1517435 | -33.0% |
| `checksum` | 2264417 | LLGo · deadcode drop | 910529 | -59.8% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 1292890 | -42.9% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 796099 | -64.8% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 2431106 | -6.8% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 1442934 | -44.7% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 2128630 | -18.4% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1288027 | -50.6% |
| `fibonacci` | 2230899 | LLGo · no LTO | 1346564 | -39.6% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 851049 | -61.9% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 1139151 | -48.9% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 742254 | -66.7% |
| `grep` | 2848917 | LLGo · no LTO | 2075828 | -27.1% |
| `grep` | 2848917 | LLGo · deadcode drop | 1377140 | -51.7% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1816665 | -36.2% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 1258277 | -55.8% |
| `glob` | 2257634 | LLGo · no LTO | 1682623 | -25.5% |
| `glob` | 2257634 | LLGo · deadcode drop | 1048923 | -53.5% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1443599 | -36.1% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 925353 | -59.0% |
| `json-wasi` | 3314587 | LLGo · no LTO | 3473031 | +4.8% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 2126111 | -35.9% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 3094057 | -6.7% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 2028391 | -38.8% |
| `llimport` | 8423078 | LLGo · no LTO | 9913647 | +17.7% |
| `llimport` | 8423078 | LLGo · deadcode drop | 8751268 | +3.9% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 9019474 | +7.1% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 8135660 | -3.4% |
| `path-report` | 2381190 | LLGo · no LTO | 1933381 | -18.8% |
| `path-report` | 2381190 | LLGo · deadcode drop | 1294176 | -45.7% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1686484 | -29.2% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 1161971 | -51.2% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 2690483 | -3.3% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1683859 | -39.5% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 2363471 | -15.0% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1515403 | -45.5% |
| `word-count` | 2253620 | LLGo · no LTO | 1649736 | -26.8% |
| `word-count` | 2253620 | LLGo · deadcode drop | 1025062 | -54.5% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 1411997 | -37.3% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 898944 | -60.1% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 13.295x | 10 |
| LLGo · deadcode drop | 8.301x | 10 |
| LLGo · full LTO (GlobalDCE off) | 11.514x | 10 |
| LLGo · full LTO + GlobalDCE | 7.420x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1530728 | +1482.0% |
| `base64` | 96760 | LLGo · deadcode drop | 928938 | +860.0% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 1311291 | +1255.2% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 815519 | +742.8% |
| `checksum` | 92685 | LLGo · no LTO | 1517435 | +1537.2% |
| `checksum` | 92685 | LLGo · deadcode drop | 910529 | +882.4% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 1292890 | +1294.9% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 796099 | +758.9% |
| `conv-wasi` | 201149 | LLGo · no LTO | 2431106 | +1108.6% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 1442934 | +617.3% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 2128630 | +958.2% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1288027 | +540.3% |
| `fibonacci` | 62386 | LLGo · no LTO | 1346564 | +2058.4% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 851049 | +1264.2% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 1139151 | +1726.0% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 742254 | +1089.8% |
| `grep` | 303772 | LLGo · no LTO | 2075828 | +583.4% |
| `grep` | 303772 | LLGo · deadcode drop | 1377140 | +353.3% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1816665 | +498.0% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 1258277 | +314.2% |
| `glob` | 93153 | LLGo · no LTO | 1682623 | +1706.3% |
| `glob` | 93153 | LLGo · deadcode drop | 1048923 | +1026.0% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1443599 | +1449.7% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 925353 | +893.4% |
| `json-wasi` | 493590 | LLGo · no LTO | 3473031 | +603.6% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 2126111 | +330.7% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 3094057 | +526.8% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 2028391 | +310.9% |
| `llimport` | — | LLGo · no LTO | 9913647 | — |
| `llimport` | — | LLGo · deadcode drop | 8751268 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 9019474 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 8135660 | — |
| `path-report` | 116889 | LLGo · no LTO | 1933381 | +1554.0% |
| `path-report` | 116889 | LLGo · deadcode drop | 1294176 | +1007.2% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1686484 | +1342.8% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 1161971 | +894.1% |
| `sha-wasi` | 287449 | LLGo · no LTO | 2690483 | +836.0% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1683859 | +485.8% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 2363471 | +722.2% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1515403 | +427.2% |
| `word-count` | 86834 | LLGo · no LTO | 1649736 | +1799.9% |
| `word-count` | 86834 | LLGo · deadcode drop | 1025062 | +1080.5% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 1411997 | +1526.1% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 898944 | +935.2% |
