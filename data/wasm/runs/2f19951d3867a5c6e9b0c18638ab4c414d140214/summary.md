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
| LLGo · deadcode drop | 0.622x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.889x | 11 |
| LLGo · full LTO + GlobalDCE | 0.576x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1957626 | -15.7% |
| `base64` | 2322402 | LLGo · deadcode drop | 1154557 | -50.3% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1739379 | -25.1% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1061500 | -54.3% |
| `checksum` | 2311672 | LLGo · no LTO | 1938043 | -16.2% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1127902 | -51.2% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1704485 | -26.3% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1027529 | -55.6% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 3072815 | +16.5% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1749900 | -33.7% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2744453 | +4.0% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1607544 | -39.1% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1702768 | -25.1% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 1047322 | -54.0% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1493215 | -34.3% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 959809 | -57.8% |
| `grep` | 2871426 | LLGo · no LTO | 2640988 | -8.0% |
| `grep` | 2871426 | LLGo · deadcode drop | 1688160 | -41.2% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2324453 | -19.0% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1559818 | -45.7% |
| `glob` | 2305059 | LLGo · no LTO | 2093799 | -9.2% |
| `glob` | 2305059 | LLGo · deadcode drop | 1251922 | -45.7% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1846027 | -19.9% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1145236 | -50.3% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4281117 | +28.2% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2558418 | -23.4% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3905433 | +17.0% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2521144 | -24.5% |
| `llimport` | 8440671 | LLGo · no LTO | 11421862 | +35.3% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9780625 | +15.9% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10445035 | +23.7% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 9102770 | +7.8% |
| `path-report` | 2428068 | LLGo · no LTO | 2428358 | +0.0% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1576581 | -35.1% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 2169992 | -10.6% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1460344 | -39.9% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3428216 | +22.0% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 2070135 | -26.4% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 3106057 | +10.5% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1946495 | -30.8% |
| `word-count` | 2300998 | LLGo · no LTO | 2053907 | -10.7% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1224943 | -46.8% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1805029 | -21.6% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1112007 | -51.7% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 12.503x | 10 |
| LLGo · deadcode drop | 7.547x | 10 |
| LLGo · full LTO (GlobalDCE off) | 11.115x | 10 |
| LLGo · full LTO + GlobalDCE | 6.990x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1957626 | +1036.2% |
| `base64` | 172302 | LLGo · deadcode drop | 1154557 | +570.1% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1739379 | +909.5% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1061500 | +516.1% |
| `checksum` | 169609 | LLGo · no LTO | 1938043 | +1042.7% |
| `checksum` | 169609 | LLGo · deadcode drop | 1127902 | +565.0% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1704485 | +904.9% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1027529 | +505.8% |
| `conv-wasi` | 165385 | LLGo · no LTO | 3072815 | +1758.0% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1749900 | +958.1% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2744453 | +1559.4% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1607544 | +872.0% |
| `fibonacci` | 141855 | LLGo · no LTO | 1702768 | +1100.4% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 1047322 | +638.3% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1493215 | +952.6% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 959809 | +576.6% |
| `grep` | 155984 | LLGo · no LTO | 2640988 | +1593.1% |
| `grep` | 155984 | LLGo · deadcode drop | 1688160 | +982.3% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2324453 | +1390.2% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1559818 | +900.0% |
| `glob` | 136553 | LLGo · no LTO | 2093799 | +1433.3% |
| `glob` | 136553 | LLGo · deadcode drop | 1251922 | +816.8% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1846027 | +1251.9% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1145236 | +738.7% |
| `json-wasi` | 525666 | LLGo · no LTO | 4281117 | +714.4% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2558418 | +386.7% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3905433 | +642.9% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2521144 | +379.6% |
| `llimport` | — | LLGo · no LTO | 11421862 | — |
| `llimport` | — | LLGo · deadcode drop | 9780625 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10445035 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 9102770 | — |
| `path-report` | 194133 | LLGo · no LTO | 2428358 | +1150.9% |
| `path-report` | 194133 | LLGo · deadcode drop | 1576581 | +712.1% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 2169992 | +1017.8% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1460344 | +652.2% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3428216 | +874.0% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 2070135 | +488.2% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 3106057 | +782.5% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1946495 | +453.0% |
| `word-count` | 164053 | LLGo · no LTO | 2053907 | +1152.0% |
| `word-count` | 164053 | LLGo · deadcode drop | 1224943 | +646.7% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1805029 | +1000.3% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1112007 | +577.8% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.803x | 11 |
| LLGo · deadcode drop | 0.516x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.698x | 11 |
| LLGo · full LTO + GlobalDCE | 0.462x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1529742 | -32.8% |
| `base64` | 2275731 | LLGo · deadcode drop | 927968 | -59.2% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 1310282 | -42.4% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 814565 | -64.2% |
| `checksum` | 2264417 | LLGo · no LTO | 1516449 | -33.0% |
| `checksum` | 2264417 | LLGo · deadcode drop | 909543 | -59.8% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 1291881 | -42.9% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 795145 | -64.9% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 2419992 | -7.2% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 1431928 | -45.1% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 2117515 | -18.8% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1277075 | -51.0% |
| `fibonacci` | 2230899 | LLGo · no LTO | 1345683 | -39.7% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 850167 | -61.9% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 1138269 | -49.0% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 741427 | -66.8% |
| `grep` | 2848917 | LLGo · no LTO | 2063923 | -27.6% |
| `grep` | 2848917 | LLGo · deadcode drop | 1365235 | -52.1% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1804805 | -36.6% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 1246472 | -56.2% |
| `glob` | 2257634 | LLGo · no LTO | 1674833 | -25.8% |
| `glob` | 2257634 | LLGo · deadcode drop | 1041117 | -53.9% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1435770 | -36.4% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 917579 | -59.4% |
| `json-wasi` | 3314587 | LLGo · no LTO | 3445996 | +4.0% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 2099185 | -36.7% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 3067048 | -7.5% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 2001567 | -39.6% |
| `llimport` | 8423078 | LLGo · no LTO | 9416383 | +11.8% |
| `llimport` | 8423078 | LLGo · deadcode drop | 8255843 | -2.0% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 8536688 | +1.3% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 7644886 | -9.2% |
| `path-report` | 2381190 | LLGo · no LTO | 1925591 | -19.1% |
| `path-report` | 2381190 | LLGo · deadcode drop | 1286386 | -46.0% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1678647 | -29.5% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 1154189 | -51.5% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 2678421 | -3.7% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1671921 | -39.9% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 2351227 | -15.5% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1503316 | -45.9% |
| `word-count` | 2253620 | LLGo · no LTO | 1641930 | -27.1% |
| `word-count` | 2253620 | LLGo · deadcode drop | 1017256 | -54.9% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 1404160 | -37.7% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 891162 | -60.5% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 13.245x | 10 |
| LLGo · deadcode drop | 8.251x | 10 |
| LLGo · full LTO (GlobalDCE off) | 11.463x | 10 |
| LLGo · full LTO + GlobalDCE | 7.371x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1529742 | +1481.0% |
| `base64` | 96760 | LLGo · deadcode drop | 927968 | +859.0% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 1310282 | +1254.2% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 814565 | +741.8% |
| `checksum` | 92685 | LLGo · no LTO | 1516449 | +1536.1% |
| `checksum` | 92685 | LLGo · deadcode drop | 909543 | +881.3% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 1291881 | +1293.8% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 795145 | +757.9% |
| `conv-wasi` | 201149 | LLGo · no LTO | 2419992 | +1103.1% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 1431928 | +611.9% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 2117515 | +952.7% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1277075 | +534.9% |
| `fibonacci` | 62386 | LLGo · no LTO | 1345683 | +2057.0% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 850167 | +1262.8% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 1138269 | +1724.6% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 741427 | +1088.5% |
| `grep` | 303772 | LLGo · no LTO | 2063923 | +579.4% |
| `grep` | 303772 | LLGo · deadcode drop | 1365235 | +349.4% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1804805 | +494.1% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 1246472 | +310.3% |
| `glob` | 93153 | LLGo · no LTO | 1674833 | +1697.9% |
| `glob` | 93153 | LLGo · deadcode drop | 1041117 | +1017.6% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1435770 | +1441.3% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 917579 | +885.0% |
| `json-wasi` | 493590 | LLGo · no LTO | 3445996 | +598.1% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 2099185 | +325.3% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 3067048 | +521.4% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 2001567 | +305.5% |
| `llimport` | — | LLGo · no LTO | 9416383 | — |
| `llimport` | — | LLGo · deadcode drop | 8255843 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 8536688 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 7644886 | — |
| `path-report` | 116889 | LLGo · no LTO | 1925591 | +1547.4% |
| `path-report` | 116889 | LLGo · deadcode drop | 1286386 | +1000.5% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1678647 | +1336.1% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 1154189 | +887.4% |
| `sha-wasi` | 287449 | LLGo · no LTO | 2678421 | +831.8% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1671921 | +481.6% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 2351227 | +718.0% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1503316 | +423.0% |
| `word-count` | 86834 | LLGo · no LTO | 1641930 | +1790.9% |
| `word-count` | 86834 | LLGo · deadcode drop | 1017256 | +1071.5% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 1404160 | +1517.1% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 891162 | +926.3% |
