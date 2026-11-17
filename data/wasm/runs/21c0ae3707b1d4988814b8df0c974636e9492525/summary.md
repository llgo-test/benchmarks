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
| LLGo · no LTO | 0.900x | 11 |
| LLGo · deadcode drop | 0.547x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.825x | 11 |
| LLGo · full LTO + GlobalDCE | 0.568x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1892799 | -18.5% |
| `base64` | 2322402 | LLGo · deadcode drop | 1059215 | -54.4% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1696197 | -27.0% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1074791 | -53.7% |
| `checksum` | 2311672 | LLGo · no LTO | 1873603 | -19.0% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1044515 | -54.8% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1661000 | -28.1% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1042021 | -54.9% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2747123 | +4.1% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1522058 | -42.3% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2556724 | -3.1% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1597939 | -39.4% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1165612 | -48.8% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 934925 | -58.9% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 981884 | -56.8% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 849531 | -62.6% |
| `grep` | 2871426 | LLGo · no LTO | 2549646 | -11.2% |
| `grep` | 2871426 | LLGo · deadcode drop | 1563745 | -45.5% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2283108 | -20.5% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1582369 | -44.9% |
| `glob` | 2305059 | LLGo · no LTO | 1924145 | -16.5% |
| `glob` | 2305059 | LLGo · deadcode drop | 1063813 | -53.8% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1800093 | -21.9% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1162297 | -49.6% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4051550 | +21.4% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2263688 | -32.2% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3852170 | +15.4% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2553033 | -23.5% |
| `llimport` | 8440671 | LLGo · no LTO | 10932951 | +29.5% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9263041 | +9.7% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10319069 | +22.3% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 9225735 | +9.3% |
| `path-report` | 2428068 | LLGo · no LTO | 2067908 | -14.8% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1195298 | -50.8% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 1936487 | -20.2% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1299641 | -46.5% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3089339 | +9.9% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1826859 | -35.0% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2906926 | +3.4% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1941286 | -30.9% |
| `word-count` | 2300998 | LLGo · no LTO | 1883139 | -18.2% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1040089 | -54.8% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1755113 | -23.7% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1127772 | -51.0% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.218x | 10 |
| LLGo · deadcode drop | 6.598x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.254x | 10 |
| LLGo · full LTO + GlobalDCE | 6.875x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1892799 | +998.5% |
| `base64` | 172302 | LLGo · deadcode drop | 1059215 | +514.7% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1696197 | +884.4% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1074791 | +523.8% |
| `checksum` | 169609 | LLGo · no LTO | 1873603 | +1004.7% |
| `checksum` | 169609 | LLGo · deadcode drop | 1044515 | +515.8% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1661000 | +879.3% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1042021 | +514.4% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2747123 | +1561.0% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1522058 | +820.3% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2556724 | +1445.9% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1597939 | +866.2% |
| `fibonacci` | 141855 | LLGo · no LTO | 1165612 | +721.7% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 934925 | +559.1% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 981884 | +592.2% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 849531 | +498.9% |
| `grep` | 155984 | LLGo · no LTO | 2549646 | +1534.6% |
| `grep` | 155984 | LLGo · deadcode drop | 1563745 | +902.5% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2283108 | +1363.7% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1582369 | +914.4% |
| `glob` | 136553 | LLGo · no LTO | 1924145 | +1309.1% |
| `glob` | 136553 | LLGo · deadcode drop | 1063813 | +679.0% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1800093 | +1218.2% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1162297 | +751.2% |
| `json-wasi` | 525666 | LLGo · no LTO | 4051550 | +670.7% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2263688 | +330.6% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3852170 | +632.8% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2553033 | +385.7% |
| `llimport` | — | LLGo · no LTO | 10932951 | — |
| `llimport` | — | LLGo · deadcode drop | 9263041 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10319069 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 9225735 | — |
| `path-report` | 194133 | LLGo · no LTO | 2067908 | +965.2% |
| `path-report` | 194133 | LLGo · deadcode drop | 1195298 | +515.7% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 1936487 | +897.5% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1299641 | +569.5% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3089339 | +777.7% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1826859 | +419.0% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2906926 | +725.9% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1941286 | +451.5% |
| `word-count` | 164053 | LLGo · no LTO | 1883139 | +1047.9% |
| `word-count` | 164053 | LLGo · deadcode drop | 1040089 | +534.0% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1755113 | +969.8% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1127772 | +587.4% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.543x | 11 |
| LLGo · deadcode drop | 0.300x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.480x | 11 |
| LLGo · full LTO + GlobalDCE | 0.340x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1080205 | -52.5% |
| `base64` | 2275731 | LLGo · deadcode drop | 530079 | -76.7% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 868341 | -61.8% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 579817 | -74.5% |
| `checksum` | 2264417 | LLGo · no LTO | 1064945 | -53.0% |
| `checksum` | 2264417 | LLGo · deadcode drop | 516553 | -77.2% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 852609 | -62.3% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 560976 | -75.2% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 1687420 | -35.3% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 848907 | -67.5% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1592729 | -38.9% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 981526 | -62.4% |
| `fibonacci` | 2230899 | LLGo · no LTO | 564347 | -74.7% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 432077 | -80.6% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 455711 | -79.6% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 413933 | -81.4% |
| `grep` | 2848917 | LLGo · no LTO | 1517953 | -46.7% |
| `grep` | 2848917 | LLGo · deadcode drop | 867001 | -69.6% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1354852 | -52.4% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 953732 | -66.5% |
| `glob` | 2257634 | LLGo · no LTO | 1096492 | -51.4% |
| `glob` | 2257634 | LLGo · deadcode drop | 522185 | -76.9% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1000222 | -55.7% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 666615 | -70.5% |
| `json-wasi` | 3314587 | LLGo · no LTO | 2720917 | -17.9% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1400235 | -57.8% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2571279 | -22.4% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1690773 | -49.0% |
| `llimport` | 8423078 | LLGo · no LTO | 7887431 | -6.4% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6652475 | -21.0% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 7057812 | -16.2% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6783856 | -19.5% |
| `path-report` | 2381190 | LLGo · no LTO | 1215425 | -49.0% |
| `path-report` | 2381190 | LLGo · deadcode drop | 633088 | -73.4% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1114171 | -53.2% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 780089 | -67.2% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1879468 | -32.4% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1012866 | -63.6% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1772490 | -36.3% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1162427 | -58.2% |
| `word-count` | 2253620 | LLGo · no LTO | 1077097 | -52.2% |
| `word-count` | 2253620 | LLGo · deadcode drop | 515555 | -77.1% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 952125 | -57.8% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 649400 | -71.2% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 8.760x | 10 |
| LLGo · deadcode drop | 4.636x | 10 |
| LLGo · full LTO (GlobalDCE off) | 7.736x | 10 |
| LLGo · full LTO + GlobalDCE | 5.322x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1080205 | +1016.4% |
| `base64` | 96760 | LLGo · deadcode drop | 530079 | +447.8% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 868341 | +797.4% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 579817 | +499.2% |
| `checksum` | 92685 | LLGo · no LTO | 1064945 | +1049.0% |
| `checksum` | 92685 | LLGo · deadcode drop | 516553 | +457.3% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 852609 | +819.9% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 560976 | +505.3% |
| `conv-wasi` | 201149 | LLGo · no LTO | 1687420 | +738.9% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 848907 | +322.0% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1592729 | +691.8% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 981526 | +388.0% |
| `fibonacci` | 62386 | LLGo · no LTO | 564347 | +804.6% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 432077 | +592.6% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 455711 | +630.5% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 413933 | +563.5% |
| `grep` | 303772 | LLGo · no LTO | 1517953 | +399.7% |
| `grep` | 303772 | LLGo · deadcode drop | 867001 | +185.4% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1354852 | +346.0% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 953732 | +214.0% |
| `glob` | 93153 | LLGo · no LTO | 1096492 | +1077.1% |
| `glob` | 93153 | LLGo · deadcode drop | 522185 | +460.6% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1000222 | +973.7% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 666615 | +615.6% |
| `json-wasi` | 493590 | LLGo · no LTO | 2720917 | +451.3% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1400235 | +183.7% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2571279 | +420.9% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1690773 | +242.5% |
| `llimport` | — | LLGo · no LTO | 7887431 | — |
| `llimport` | — | LLGo · deadcode drop | 6652475 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 7057812 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6783856 | — |
| `path-report` | 116889 | LLGo · no LTO | 1215425 | +939.8% |
| `path-report` | 116889 | LLGo · deadcode drop | 633088 | +441.6% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1114171 | +853.2% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 780089 | +567.4% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1879468 | +553.8% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1012866 | +252.4% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1772490 | +516.6% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1162427 | +304.4% |
| `word-count` | 86834 | LLGo · no LTO | 1077097 | +1140.4% |
| `word-count` | 86834 | LLGo · deadcode drop | 515555 | +493.7% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 952125 | +996.5% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 649400 | +647.9% |
