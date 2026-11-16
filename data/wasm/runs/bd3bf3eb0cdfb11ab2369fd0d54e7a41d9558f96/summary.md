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
| LLGo · no LTO | 0.901x | 11 |
| LLGo · deadcode drop | 0.548x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.823x | 11 |
| LLGo · full LTO + GlobalDCE | 0.567x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1894097 | -18.4% |
| `base64` | 2322402 | LLGo · deadcode drop | 1060332 | -54.3% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1690047 | -27.2% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1072981 | -53.8% |
| `checksum` | 2311672 | LLGo · no LTO | 1875035 | -18.9% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1045741 | -54.8% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1654643 | -28.4% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1040009 | -55.0% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2751698 | +4.3% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1524918 | -42.2% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2548620 | -3.4% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1596303 | -39.5% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1165536 | -48.8% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 935769 | -58.9% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 978156 | -57.0% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 847923 | -62.7% |
| `grep` | 2871426 | LLGo · no LTO | 2552633 | -11.1% |
| `grep` | 2871426 | LLGo · deadcode drop | 1567405 | -45.4% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2277163 | -20.7% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1581561 | -44.9% |
| `glob` | 2305059 | LLGo · no LTO | 1925489 | -16.5% |
| `glob` | 2305059 | LLGo · deadcode drop | 1064888 | -53.8% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1794835 | -22.1% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1161532 | -49.6% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4059377 | +21.6% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2269149 | -32.0% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3836963 | +14.9% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2550569 | -23.6% |
| `llimport` | 8440671 | LLGo · no LTO | 10954908 | +29.8% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9284539 | +10.0% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10284086 | +21.8% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 9189543 | +8.9% |
| `path-report` | 2428068 | LLGo · no LTO | 2069453 | -14.8% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1196666 | -50.7% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 1930779 | -20.5% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1297766 | -46.6% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3100242 | +10.3% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1830548 | -34.9% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2897665 | +3.1% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1939363 | -31.0% |
| `word-count` | 2300998 | LLGo · no LTO | 1884646 | -18.1% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1041241 | -54.7% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1749853 | -24.0% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1126961 | -51.0% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.231x | 10 |
| LLGo · deadcode drop | 6.608x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.221x | 10 |
| LLGo · full LTO + GlobalDCE | 6.867x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1894097 | +999.3% |
| `base64` | 172302 | LLGo · deadcode drop | 1060332 | +515.4% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1690047 | +880.9% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1072981 | +522.7% |
| `checksum` | 169609 | LLGo · no LTO | 1875035 | +1005.5% |
| `checksum` | 169609 | LLGo · deadcode drop | 1045741 | +516.6% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1654643 | +875.6% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1040009 | +513.2% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2751698 | +1563.8% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1524918 | +822.0% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2548620 | +1441.0% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1596303 | +865.2% |
| `fibonacci` | 141855 | LLGo · no LTO | 1165536 | +721.6% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 935769 | +559.7% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 978156 | +589.5% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 847923 | +497.7% |
| `grep` | 155984 | LLGo · no LTO | 2552633 | +1536.5% |
| `grep` | 155984 | LLGo · deadcode drop | 1567405 | +904.8% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2277163 | +1359.9% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1581561 | +913.9% |
| `glob` | 136553 | LLGo · no LTO | 1925489 | +1310.1% |
| `glob` | 136553 | LLGo · deadcode drop | 1064888 | +679.8% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1794835 | +1214.4% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1161532 | +750.6% |
| `json-wasi` | 525666 | LLGo · no LTO | 4059377 | +672.2% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2269149 | +331.7% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3836963 | +629.9% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2550569 | +385.2% |
| `llimport` | — | LLGo · no LTO | 10954908 | — |
| `llimport` | — | LLGo · deadcode drop | 9284539 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10284086 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 9189543 | — |
| `path-report` | 194133 | LLGo · no LTO | 2069453 | +966.0% |
| `path-report` | 194133 | LLGo · deadcode drop | 1196666 | +516.4% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 1930779 | +894.6% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1297766 | +568.5% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3100242 | +780.8% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1830548 | +420.1% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2897665 | +723.3% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1939363 | +451.0% |
| `word-count` | 164053 | LLGo · no LTO | 1884646 | +1048.8% |
| `word-count` | 164053 | LLGo · deadcode drop | 1041241 | +534.7% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1749853 | +966.6% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1126961 | +586.9% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.543x | 11 |
| LLGo · deadcode drop | 0.300x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.476x | 11 |
| LLGo · full LTO + GlobalDCE | 0.339x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1081235 | -52.5% |
| `base64` | 2275731 | LLGo · deadcode drop | 531096 | -76.7% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 861187 | -62.2% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 577020 | -74.6% |
| `checksum` | 2264417 | LLGo · no LTO | 1066089 | -52.9% |
| `checksum` | 2264417 | LLGo · deadcode drop | 517700 | -77.1% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 845461 | -62.7% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 558265 | -75.3% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 1691854 | -35.1% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 851232 | -67.4% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1582738 | -39.3% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 978587 | -62.5% |
| `fibonacci` | 2230899 | LLGo · no LTO | 564267 | -74.7% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 432913 | -80.6% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 452684 | -79.7% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 412018 | -81.5% |
| `grep` | 2848917 | LLGo · no LTO | 1520244 | -46.6% |
| `grep` | 2848917 | LLGo · deadcode drop | 869900 | -69.5% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1346764 | -52.7% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 951643 | -66.6% |
| `glob` | 2257634 | LLGo · no LTO | 1097566 | -51.4% |
| `glob` | 2257634 | LLGo · deadcode drop | 523118 | -76.8% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 993939 | -56.0% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 664844 | -70.6% |
| `json-wasi` | 3314587 | LLGo · no LTO | 2728608 | -17.7% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1404930 | -57.6% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2549438 | -23.1% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1683129 | -49.2% |
| `llimport` | 8423078 | LLGo · no LTO | 7906778 | -6.1% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6670904 | -20.8% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 6996142 | -16.9% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6744518 | -19.9% |
| `path-report` | 2381190 | LLGo · no LTO | 1216667 | -48.9% |
| `path-report` | 2381190 | LLGo · deadcode drop | 634357 | -73.4% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1107170 | -53.5% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 777847 | -67.3% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1884504 | -32.2% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1015907 | -63.5% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1761291 | -36.7% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1158313 | -58.3% |
| `word-count` | 2253620 | LLGo · no LTO | 1078133 | -52.2% |
| `word-count` | 2253620 | LLGo · deadcode drop | 516450 | -77.1% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 945858 | -58.0% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 647613 | -71.3% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 8.773x | 10 |
| LLGo · deadcode drop | 4.647x | 10 |
| LLGo · full LTO (GlobalDCE off) | 7.682x | 10 |
| LLGo · full LTO + GlobalDCE | 5.303x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1081235 | +1017.4% |
| `base64` | 96760 | LLGo · deadcode drop | 531096 | +448.9% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 861187 | +790.0% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 577020 | +496.3% |
| `checksum` | 92685 | LLGo · no LTO | 1066089 | +1050.2% |
| `checksum` | 92685 | LLGo · deadcode drop | 517700 | +458.6% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 845461 | +812.2% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 558265 | +502.3% |
| `conv-wasi` | 201149 | LLGo · no LTO | 1691854 | +741.1% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 851232 | +323.2% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1582738 | +686.8% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 978587 | +386.5% |
| `fibonacci` | 62386 | LLGo · no LTO | 564267 | +804.5% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 432913 | +593.9% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 452684 | +625.6% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 412018 | +560.4% |
| `grep` | 303772 | LLGo · no LTO | 1520244 | +400.5% |
| `grep` | 303772 | LLGo · deadcode drop | 869900 | +186.4% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1346764 | +343.3% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 951643 | +213.3% |
| `glob` | 93153 | LLGo · no LTO | 1097566 | +1078.2% |
| `glob` | 93153 | LLGo · deadcode drop | 523118 | +461.6% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 993939 | +967.0% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 664844 | +613.7% |
| `json-wasi` | 493590 | LLGo · no LTO | 2728608 | +452.8% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1404930 | +184.6% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2549438 | +416.5% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1683129 | +241.0% |
| `llimport` | — | LLGo · no LTO | 7906778 | — |
| `llimport` | — | LLGo · deadcode drop | 6670904 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 6996142 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6744518 | — |
| `path-report` | 116889 | LLGo · no LTO | 1216667 | +940.9% |
| `path-report` | 116889 | LLGo · deadcode drop | 634357 | +442.7% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1107170 | +847.2% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 777847 | +565.5% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1884504 | +555.6% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1015907 | +253.4% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1761291 | +512.7% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1158313 | +303.0% |
| `word-count` | 86834 | LLGo · no LTO | 1078133 | +1141.6% |
| `word-count` | 86834 | LLGo · deadcode drop | 516450 | +494.8% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 945858 | +989.3% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 647613 | +645.8% |
