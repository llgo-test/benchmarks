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
| LLGo · no LTO | 0.924x | 11 |
| LLGo · deadcode drop | 0.526x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.831x | 11 |
| LLGo · full LTO + GlobalDCE | 0.564x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1885115 | -18.8% |
| `base64` | 2322402 | LLGo · deadcode drop | 1016622 | -56.2% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1648832 | -29.0% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1057957 | -54.4% |
| `checksum` | 2311672 | LLGo · no LTO | 1864938 | -19.3% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1002309 | -56.6% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1612495 | -30.2% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1025084 | -55.7% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2727539 | +3.4% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1463909 | -44.5% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2489020 | -5.7% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1575397 | -40.3% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1666086 | -26.7% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 895004 | -60.6% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1432609 | -37.0% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 970419 | -57.3% |
| `grep` | 2871426 | LLGo · no LTO | 2536277 | -11.7% |
| `grep` | 2871426 | LLGo · deadcode drop | 1509495 | -47.4% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2215054 | -22.9% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1552405 | -45.9% |
| `glob` | 2305059 | LLGo · no LTO | 1915013 | -16.9% |
| `glob` | 2305059 | LLGo · deadcode drop | 1023154 | -55.6% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1750889 | -24.0% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1146776 | -50.2% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4011916 | +20.2% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2172548 | -34.9% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3724398 | +11.6% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2486542 | -25.5% |
| `llimport` | 8440671 | LLGo · no LTO | 10905032 | +29.2% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9021402 | +6.9% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 9925293 | +17.6% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 8858065 | +4.9% |
| `path-report` | 2428068 | LLGo · no LTO | 2053543 | -15.4% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1146236 | -52.8% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 1878968 | -22.6% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1275690 | -47.5% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3043620 | +8.3% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1736537 | -38.2% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2803841 | -0.3% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1884404 | -33.0% |
| `word-count` | 2300998 | LLGo · no LTO | 1875244 | -18.5% |
| `word-count` | 2300998 | LLGo · deadcode drop | 998587 | -56.6% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1710214 | -25.7% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1114882 | -51.5% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.554x | 10 |
| LLGo · deadcode drop | 6.331x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.367x | 10 |
| LLGo · full LTO + GlobalDCE | 6.853x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1885115 | +994.1% |
| `base64` | 172302 | LLGo · deadcode drop | 1016622 | +490.0% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1648832 | +856.9% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1057957 | +514.0% |
| `checksum` | 169609 | LLGo · no LTO | 1864938 | +999.6% |
| `checksum` | 169609 | LLGo · deadcode drop | 1002309 | +491.0% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1612495 | +850.7% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1025084 | +504.4% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2727539 | +1549.2% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1463909 | +785.2% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2489020 | +1405.0% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1575397 | +852.6% |
| `fibonacci` | 141855 | LLGo · no LTO | 1666086 | +1074.5% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 895004 | +530.9% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1432609 | +909.9% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 970419 | +584.1% |
| `grep` | 155984 | LLGo · no LTO | 2536277 | +1526.0% |
| `grep` | 155984 | LLGo · deadcode drop | 1509495 | +867.7% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2215054 | +1320.1% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1552405 | +895.2% |
| `glob` | 136553 | LLGo · no LTO | 1915013 | +1302.4% |
| `glob` | 136553 | LLGo · deadcode drop | 1023154 | +649.3% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1750889 | +1182.2% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1146776 | +739.8% |
| `json-wasi` | 525666 | LLGo · no LTO | 4011916 | +663.2% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2172548 | +313.3% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3724398 | +608.5% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2486542 | +373.0% |
| `llimport` | — | LLGo · no LTO | 10905032 | — |
| `llimport` | — | LLGo · deadcode drop | 9021402 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 9925293 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 8858065 | — |
| `path-report` | 194133 | LLGo · no LTO | 2053543 | +957.8% |
| `path-report` | 194133 | LLGo · deadcode drop | 1146236 | +490.4% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 1878968 | +867.9% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1275690 | +557.1% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3043620 | +764.7% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1736537 | +393.4% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2803841 | +696.6% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1884404 | +435.4% |
| `word-count` | 164053 | LLGo · no LTO | 1875244 | +1043.1% |
| `word-count` | 164053 | LLGo · deadcode drop | 998587 | +508.7% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1710214 | +942.5% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1114882 | +579.6% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.560x | 11 |
| LLGo · deadcode drop | 0.283x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.481x | 11 |
| LLGo · full LTO + GlobalDCE | 0.337x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1075473 | -52.7% |
| `base64` | 2275731 | LLGo · deadcode drop | 499180 | -78.1% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 832539 | -63.4% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 563782 | -75.2% |
| `checksum` | 2264417 | LLGo · no LTO | 1059386 | -53.2% |
| `checksum` | 2264417 | LLGo · deadcode drop | 486263 | -78.5% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 816739 | -63.9% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 545634 | -75.9% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 1658536 | -36.4% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 797517 | -69.4% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1524036 | -41.6% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 952962 | -63.5% |
| `fibonacci` | 2230899 | LLGo · no LTO | 873268 | -60.9% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 403849 | -81.9% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 720404 | -67.7% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 503553 | -77.4% |
| `grep` | 2848917 | LLGo · no LTO | 1507961 | -47.1% |
| `grep` | 2848917 | LLGo · deadcode drop | 824411 | -71.1% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1307784 | -54.1% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 934869 | -67.2% |
| `glob` | 2257634 | LLGo · no LTO | 1090622 | -51.7% |
| `glob` | 2257634 | LLGo · deadcode drop | 493403 | -78.1% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 962691 | -57.4% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 652697 | -71.1% |
| `json-wasi` | 3314587 | LLGo · no LTO | 2667336 | -19.5% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1313674 | -60.4% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2438477 | -26.4% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1617406 | -51.2% |
| `llimport` | 8423078 | LLGo · no LTO | 7941002 | -5.7% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6489703 | -23.0% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 6756220 | -19.8% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6524627 | -22.5% |
| `path-report` | 2381190 | LLGo · no LTO | 1204220 | -49.4% |
| `path-report` | 2381190 | LLGo · deadcode drop | 595302 | -75.0% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1068268 | -55.1% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 758426 | -68.1% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1847755 | -33.6% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 955959 | -65.6% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1693051 | -39.1% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1122932 | -59.6% |
| `word-count` | 2253620 | LLGo · no LTO | 1071859 | -52.4% |
| `word-count` | 2253620 | LLGo · deadcode drop | 485270 | -78.5% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 919750 | -59.2% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 637865 | -71.7% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 9.069x | 10 |
| LLGo · deadcode drop | 4.366x | 10 |
| LLGo · full LTO (GlobalDCE off) | 7.798x | 10 |
| LLGo · full LTO + GlobalDCE | 5.293x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1075473 | +1011.5% |
| `base64` | 96760 | LLGo · deadcode drop | 499180 | +415.9% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 832539 | +760.4% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 563782 | +482.7% |
| `checksum` | 92685 | LLGo · no LTO | 1059386 | +1043.0% |
| `checksum` | 92685 | LLGo · deadcode drop | 486263 | +424.6% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 816739 | +781.2% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 545634 | +488.7% |
| `conv-wasi` | 201149 | LLGo · no LTO | 1658536 | +724.5% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 797517 | +296.5% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1524036 | +657.7% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 952962 | +373.8% |
| `fibonacci` | 62386 | LLGo · no LTO | 873268 | +1299.8% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 403849 | +547.3% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 720404 | +1054.8% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 503553 | +707.2% |
| `grep` | 303772 | LLGo · no LTO | 1507961 | +396.4% |
| `grep` | 303772 | LLGo · deadcode drop | 824411 | +171.4% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1307784 | +330.5% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 934869 | +207.8% |
| `glob` | 93153 | LLGo · no LTO | 1090622 | +1070.8% |
| `glob` | 93153 | LLGo · deadcode drop | 493403 | +429.7% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 962691 | +933.5% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 652697 | +600.7% |
| `json-wasi` | 493590 | LLGo · no LTO | 2667336 | +440.4% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1313674 | +166.1% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2438477 | +394.0% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1617406 | +227.7% |
| `llimport` | — | LLGo · no LTO | 7941002 | — |
| `llimport` | — | LLGo · deadcode drop | 6489703 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 6756220 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6524627 | — |
| `path-report` | 116889 | LLGo · no LTO | 1204220 | +930.2% |
| `path-report` | 116889 | LLGo · deadcode drop | 595302 | +409.3% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1068268 | +813.9% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 758426 | +548.8% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1847755 | +542.8% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 955959 | +232.6% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1693051 | +489.0% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1122932 | +290.7% |
| `word-count` | 86834 | LLGo · no LTO | 1071859 | +1134.4% |
| `word-count` | 86834 | LLGo · deadcode drop | 485270 | +458.8% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 919750 | +959.2% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 637865 | +634.6% |
