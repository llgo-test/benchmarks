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
| LLGo · no LTO | 0.944x | 11 |
| LLGo · deadcode drop | 0.548x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.866x | 11 |
| LLGo · full LTO + GlobalDCE | 0.586x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1922421 | -17.2% |
| `base64` | 2322402 | LLGo · deadcode drop | 1059102 | -54.4% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1717400 | -26.1% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1097724 | -52.7% |
| `checksum` | 2311672 | LLGo · no LTO | 1902966 | -17.7% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1044510 | -54.8% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1681012 | -27.3% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1063876 | -54.0% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2786583 | +5.6% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1523021 | -42.3% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2583305 | -2.1% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1626027 | -38.4% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1700475 | -25.2% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 934533 | -58.9% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1490325 | -34.5% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 1005453 | -55.8% |
| `grep` | 2871426 | LLGo · no LTO | 2586199 | -9.9% |
| `grep` | 2871426 | LLGo · deadcode drop | 1565995 | -45.5% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2308858 | -19.6% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1610589 | -43.9% |
| `glob` | 2305059 | LLGo · no LTO | 1953450 | -15.3% |
| `glob` | 2305059 | LLGo · deadcode drop | 1063667 | -53.9% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1822918 | -20.9% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1187123 | -48.5% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4098409 | +22.8% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2267144 | -32.1% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3876413 | +16.1% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2583716 | -22.6% |
| `llimport` | 8440671 | LLGo · no LTO | 11110371 | +31.6% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9291071 | +10.1% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10435519 | +23.6% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 9319040 | +10.4% |
| `path-report` | 2428068 | LLGo · no LTO | 2099154 | -13.5% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1195439 | -50.8% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 1960546 | -19.3% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1325025 | -45.4% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3140721 | +11.7% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1828611 | -35.0% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2935963 | +4.4% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1972837 | -29.8% |
| `word-count` | 2300998 | LLGo · no LTO | 1912626 | -16.9% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1040011 | -54.8% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1777892 | -22.7% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1152533 | -49.9% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.806x | 10 |
| LLGo · deadcode drop | 6.601x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.799x | 10 |
| LLGo · full LTO + GlobalDCE | 7.110x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1922421 | +1015.7% |
| `base64` | 172302 | LLGo · deadcode drop | 1059102 | +514.7% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1717400 | +896.7% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1097724 | +537.1% |
| `checksum` | 169609 | LLGo · no LTO | 1902966 | +1022.0% |
| `checksum` | 169609 | LLGo · deadcode drop | 1044510 | +515.8% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1681012 | +891.1% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1063876 | +527.3% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2786583 | +1584.9% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1523021 | +820.9% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2583305 | +1462.0% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1626027 | +883.2% |
| `fibonacci` | 141855 | LLGo · no LTO | 1700475 | +1098.7% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 934533 | +558.8% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1490325 | +950.6% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 1005453 | +608.8% |
| `grep` | 155984 | LLGo · no LTO | 2586199 | +1558.0% |
| `grep` | 155984 | LLGo · deadcode drop | 1565995 | +903.9% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2308858 | +1380.2% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1610589 | +932.5% |
| `glob` | 136553 | LLGo · no LTO | 1953450 | +1330.5% |
| `glob` | 136553 | LLGo · deadcode drop | 1063667 | +678.9% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1822918 | +1235.0% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1187123 | +769.3% |
| `json-wasi` | 525666 | LLGo · no LTO | 4098409 | +679.7% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2267144 | +331.3% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3876413 | +637.4% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2583716 | +391.5% |
| `llimport` | — | LLGo · no LTO | 11110371 | — |
| `llimport` | — | LLGo · deadcode drop | 9291071 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10435519 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 9319040 | — |
| `path-report` | 194133 | LLGo · no LTO | 2099154 | +981.3% |
| `path-report` | 194133 | LLGo · deadcode drop | 1195439 | +515.8% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 1960546 | +909.9% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1325025 | +582.5% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3140721 | +792.3% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1828611 | +419.5% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2935963 | +734.1% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1972837 | +460.5% |
| `word-count` | 164053 | LLGo · no LTO | 1912626 | +1065.9% |
| `word-count` | 164053 | LLGo · deadcode drop | 1040011 | +533.9% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1777892 | +983.7% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1152533 | +602.5% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.578x | 11 |
| LLGo · deadcode drop | 0.300x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.509x | 11 |
| LLGo · full LTO + GlobalDCE | 0.356x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1104570 | -51.5% |
| `base64` | 2275731 | LLGo · deadcode drop | 531011 | -76.7% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 880715 | -61.3% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 596606 | -73.8% |
| `checksum` | 2264417 | LLGo · no LTO | 1089134 | -51.9% |
| `checksum` | 2264417 | LLGo · deadcode drop | 517599 | -77.1% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 864438 | -61.8% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 577247 | -74.5% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 1724748 | -33.9% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 851148 | -67.4% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1612892 | -38.2% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1003869 | -61.5% |
| `fibonacci` | 2230899 | LLGo · no LTO | 902107 | -59.6% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 432828 | -80.6% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 761499 | -65.9% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 531362 | -76.2% |
| `grep` | 2848917 | LLGo · no LTO | 1549746 | -45.6% |
| `grep` | 2848917 | LLGo · deadcode drop | 869815 | -69.5% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1372820 | -51.8% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 976699 | -65.7% |
| `glob` | 2257634 | LLGo · no LTO | 1120681 | -50.4% |
| `glob` | 2257634 | LLGo · deadcode drop | 523033 | -76.8% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1014814 | -55.0% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 685659 | -69.6% |
| `json-wasi` | 3314587 | LLGo · no LTO | 2772086 | -16.4% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1404758 | -57.6% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2590028 | -21.9% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1717783 | -48.2% |
| `llimport` | 8423078 | LLGo · no LTO | 8104186 | -3.8% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6704507 | -20.4% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 7180885 | -14.7% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6914918 | -17.9% |
| `path-report` | 2381190 | LLGo · no LTO | 1241733 | -47.9% |
| `path-report` | 2381190 | LLGo · deadcode drop | 634256 | -73.4% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1129930 | -52.5% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 800588 | -66.4% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1921207 | -30.9% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1015822 | -63.5% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1794747 | -35.5% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1187209 | -57.3% |
| `word-count` | 2253620 | LLGo · no LTO | 1101287 | -51.1% |
| `word-count` | 2253620 | LLGo · deadcode drop | 516365 | -77.1% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 966835 | -57.1% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 668607 | -70.3% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 9.360x | 10 |
| LLGo · deadcode drop | 4.647x | 10 |
| LLGo · full LTO (GlobalDCE off) | 8.240x | 10 |
| LLGo · full LTO + GlobalDCE | 5.580x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1104570 | +1041.6% |
| `base64` | 96760 | LLGo · deadcode drop | 531011 | +448.8% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 880715 | +810.2% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 596606 | +516.6% |
| `checksum` | 92685 | LLGo · no LTO | 1089134 | +1075.1% |
| `checksum` | 92685 | LLGo · deadcode drop | 517599 | +458.4% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 864438 | +832.7% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 577247 | +522.8% |
| `conv-wasi` | 201149 | LLGo · no LTO | 1724748 | +757.4% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 851148 | +323.1% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1612892 | +701.8% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1003869 | +399.1% |
| `fibonacci` | 62386 | LLGo · no LTO | 902107 | +1346.0% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 432828 | +593.8% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 761499 | +1120.6% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 531362 | +751.7% |
| `grep` | 303772 | LLGo · no LTO | 1549746 | +410.2% |
| `grep` | 303772 | LLGo · deadcode drop | 869815 | +186.3% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1372820 | +351.9% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 976699 | +221.5% |
| `glob` | 93153 | LLGo · no LTO | 1120681 | +1103.1% |
| `glob` | 93153 | LLGo · deadcode drop | 523033 | +461.5% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1014814 | +989.4% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 685659 | +636.1% |
| `json-wasi` | 493590 | LLGo · no LTO | 2772086 | +461.6% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1404758 | +184.6% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2590028 | +424.7% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1717783 | +248.0% |
| `llimport` | — | LLGo · no LTO | 8104186 | — |
| `llimport` | — | LLGo · deadcode drop | 6704507 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 7180885 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6914918 | — |
| `path-report` | 116889 | LLGo · no LTO | 1241733 | +962.3% |
| `path-report` | 116889 | LLGo · deadcode drop | 634256 | +442.6% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1129930 | +866.7% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 800588 | +584.9% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1921207 | +568.4% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1015822 | +253.4% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1794747 | +524.4% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1187209 | +313.0% |
| `word-count` | 86834 | LLGo · no LTO | 1101287 | +1168.3% |
| `word-count` | 86834 | LLGo · deadcode drop | 516365 | +494.7% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 966835 | +1013.4% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 668607 | +670.0% |
