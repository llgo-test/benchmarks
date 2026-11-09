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
| LLGo · no LTO | 0.940x | 11 |
| LLGo · deadcode drop | 0.544x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.862x | 11 |
| LLGo · full LTO + GlobalDCE | 0.582x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1913074 | -17.6% |
| `base64` | 2322402 | LLGo · deadcode drop | 1051930 | -54.7% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1708399 | -26.4% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1090341 | -53.1% |
| `checksum` | 2311672 | LLGo · no LTO | 1893616 | -18.1% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1037337 | -55.1% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1672031 | -27.7% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1056441 | -54.3% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2776204 | +5.2% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1514916 | -42.6% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2573995 | -2.4% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1617911 | -38.7% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1691156 | -25.6% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 927321 | -59.2% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1481426 | -34.9% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 998123 | -56.1% |
| `grep` | 2871426 | LLGo · no LTO | 2576513 | -10.3% |
| `grep` | 2871426 | LLGo · deadcode drop | 1558290 | -45.7% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2299793 | -19.9% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1603028 | -44.2% |
| `glob` | 2305059 | LLGo · no LTO | 1944064 | -15.7% |
| `glob` | 2305059 | LLGo · deadcode drop | 1056471 | -54.2% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1813957 | -21.3% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1179681 | -48.8% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4089275 | +22.5% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2259909 | -32.3% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3867752 | +15.9% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2576564 | -22.8% |
| `llimport` | 8440671 | LLGo · no LTO | 11073513 | +31.2% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9251185 | +9.6% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10399267 | +23.2% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 9282809 | +10.0% |
| `path-report` | 2428068 | LLGo · no LTO | 2089748 | -13.9% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1188156 | -51.1% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 1951590 | -19.6% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1317525 | -45.7% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3110720 | +10.7% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1801689 | -35.9% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2907768 | +3.4% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1945998 | -30.8% |
| `word-count` | 2300998 | LLGo · no LTO | 1903500 | -17.3% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1033174 | -55.1% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1769026 | -23.1% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1145205 | -50.2% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.748x | 10 |
| LLGo · deadcode drop | 6.556x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.744x | 10 |
| LLGo · full LTO + GlobalDCE | 7.064x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1913074 | +1010.3% |
| `base64` | 172302 | LLGo · deadcode drop | 1051930 | +510.5% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1708399 | +891.5% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1090341 | +532.8% |
| `checksum` | 169609 | LLGo · no LTO | 1893616 | +1016.5% |
| `checksum` | 169609 | LLGo · deadcode drop | 1037337 | +511.6% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1672031 | +885.8% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1056441 | +522.9% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2776204 | +1578.6% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1514916 | +816.0% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2573995 | +1456.4% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1617911 | +878.3% |
| `fibonacci` | 141855 | LLGo · no LTO | 1691156 | +1092.2% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 927321 | +553.7% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1481426 | +944.3% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 998123 | +603.6% |
| `grep` | 155984 | LLGo · no LTO | 2576513 | +1551.8% |
| `grep` | 155984 | LLGo · deadcode drop | 1558290 | +899.0% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2299793 | +1374.4% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1603028 | +927.7% |
| `glob` | 136553 | LLGo · no LTO | 1944064 | +1323.7% |
| `glob` | 136553 | LLGo · deadcode drop | 1056471 | +673.7% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1813957 | +1228.4% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1179681 | +763.9% |
| `json-wasi` | 525666 | LLGo · no LTO | 4089275 | +677.9% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2259909 | +329.9% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3867752 | +635.8% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2576564 | +390.2% |
| `llimport` | — | LLGo · no LTO | 11073513 | — |
| `llimport` | — | LLGo · deadcode drop | 9251185 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10399267 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 9282809 | — |
| `path-report` | 194133 | LLGo · no LTO | 2089748 | +976.5% |
| `path-report` | 194133 | LLGo · deadcode drop | 1188156 | +512.0% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 1951590 | +905.3% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1317525 | +578.7% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3110720 | +783.8% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1801689 | +411.9% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2907768 | +726.1% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1945998 | +452.9% |
| `word-count` | 164053 | LLGo · no LTO | 1903500 | +1060.3% |
| `word-count` | 164053 | LLGo · deadcode drop | 1033174 | +529.8% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1769026 | +978.3% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1145205 | +598.1% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.578x | 11 |
| LLGo · deadcode drop | 0.300x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.509x | 11 |
| LLGo · full LTO + GlobalDCE | 0.356x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1104312 | -51.5% |
| `base64` | 2275731 | LLGo · deadcode drop | 530277 | -76.7% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 880737 | -61.3% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 595678 | -73.8% |
| `checksum` | 2264417 | LLGo · no LTO | 1088882 | -51.9% |
| `checksum` | 2264417 | LLGo · deadcode drop | 516887 | -77.2% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 864466 | -61.8% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 576319 | -74.5% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 1723267 | -33.9% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 849722 | -67.4% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1612672 | -38.2% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1002524 | -61.6% |
| `fibonacci` | 2230899 | LLGo · no LTO | 900887 | -59.6% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 432096 | -80.6% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 760588 | -65.9% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 530590 | -76.2% |
| `grep` | 2848917 | LLGo · no LTO | 1552266 | -45.5% |
| `grep` | 2848917 | LLGo · deadcode drop | 871597 | -69.4% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1380060 | -51.6% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 982749 | -65.5% |
| `glob` | 2257634 | LLGo · no LTO | 1120442 | -50.4% |
| `glob` | 2257634 | LLGo · deadcode drop | 522326 | -76.9% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1014842 | -55.0% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 684725 | -69.7% |
| `json-wasi` | 3314587 | LLGo · no LTO | 2764110 | -16.6% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1400141 | -57.8% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2583350 | -22.1% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1711256 | -48.4% |
| `llimport` | 8423078 | LLGo · no LTO | 8202356 | -2.6% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6827253 | -18.9% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 7279762 | -13.6% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 7017187 | -16.7% |
| `path-report` | 2381190 | LLGo · no LTO | 1241437 | -47.9% |
| `path-report` | 2381190 | LLGo · deadcode drop | 633369 | -73.4% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1129887 | -52.5% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 799613 | -66.4% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1916528 | -31.1% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1011080 | -63.6% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1791189 | -35.6% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1182559 | -57.5% |
| `word-count` | 2253620 | LLGo · no LTO | 1101058 | -51.1% |
| `word-count` | 2253620 | LLGo · deadcode drop | 515528 | -77.1% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 966840 | -57.1% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 667650 | -70.4% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 9.354x | 10 |
| LLGo · deadcode drop | 4.639x | 10 |
| LLGo · full LTO (GlobalDCE off) | 8.239x | 10 |
| LLGo · full LTO + GlobalDCE | 5.574x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1104312 | +1041.3% |
| `base64` | 96760 | LLGo · deadcode drop | 530277 | +448.0% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 880737 | +810.2% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 595678 | +515.6% |
| `checksum` | 92685 | LLGo · no LTO | 1088882 | +1074.8% |
| `checksum` | 92685 | LLGo · deadcode drop | 516887 | +457.7% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 864466 | +832.7% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 576319 | +521.8% |
| `conv-wasi` | 201149 | LLGo · no LTO | 1723267 | +756.7% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 849722 | +322.4% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1612672 | +701.7% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1002524 | +398.4% |
| `fibonacci` | 62386 | LLGo · no LTO | 900887 | +1344.1% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 432096 | +592.6% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 760588 | +1119.2% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 530590 | +750.5% |
| `grep` | 303772 | LLGo · no LTO | 1552266 | +411.0% |
| `grep` | 303772 | LLGo · deadcode drop | 871597 | +186.9% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1380060 | +354.3% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 982749 | +223.5% |
| `glob` | 93153 | LLGo · no LTO | 1120442 | +1102.8% |
| `glob` | 93153 | LLGo · deadcode drop | 522326 | +460.7% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1014842 | +989.4% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 684725 | +635.1% |
| `json-wasi` | 493590 | LLGo · no LTO | 2764110 | +460.0% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1400141 | +183.7% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2583350 | +423.4% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1711256 | +246.7% |
| `llimport` | — | LLGo · no LTO | 8202356 | — |
| `llimport` | — | LLGo · deadcode drop | 6827253 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 7279762 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 7017187 | — |
| `path-report` | 116889 | LLGo · no LTO | 1241437 | +962.1% |
| `path-report` | 116889 | LLGo · deadcode drop | 633369 | +441.9% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1129887 | +866.6% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 799613 | +584.1% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1916528 | +566.7% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1011080 | +251.7% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1791189 | +523.1% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1182559 | +311.4% |
| `word-count` | 86834 | LLGo · no LTO | 1101058 | +1168.0% |
| `word-count` | 86834 | LLGo · deadcode drop | 515528 | +493.7% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 966840 | +1013.4% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 667650 | +668.9% |
