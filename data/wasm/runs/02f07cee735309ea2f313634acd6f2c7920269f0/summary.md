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

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.803x | 11 |
| LLGo · deadcode drop | 0.516x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.698x | 11 |
| LLGo · full LTO + GlobalDCE | 0.462x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1529793 | -32.8% |
| `base64` | 2275731 | LLGo · deadcode drop | 928019 | -59.2% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 1310314 | -42.4% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 814597 | -64.2% |
| `checksum` | 2264417 | LLGo · no LTO | 1516500 | -33.0% |
| `checksum` | 2264417 | LLGo · deadcode drop | 909594 | -59.8% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 1291913 | -42.9% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 795177 | -64.9% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 2420043 | -7.2% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 1431979 | -45.1% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 2117547 | -18.8% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1277107 | -51.0% |
| `fibonacci` | 2230899 | LLGo · no LTO | 1345734 | -39.7% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 850218 | -61.9% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 1138301 | -49.0% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 741459 | -66.8% |
| `glob` | 2257634 | LLGo · no LTO | 1674884 | -25.8% |
| `glob` | 2257634 | LLGo · deadcode drop | 1041168 | -53.9% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1435802 | -36.4% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 917611 | -59.4% |
| `grep` | 2848917 | LLGo · no LTO | 2063974 | -27.6% |
| `grep` | 2848917 | LLGo · deadcode drop | 1365286 | -52.1% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1804837 | -36.6% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 1246504 | -56.2% |
| `json-wasi` | 3314587 | LLGo · no LTO | 3446047 | +4.0% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 2099236 | -36.7% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 3067080 | -7.5% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 2001599 | -39.6% |
| `llimport` | 8423078 | LLGo · no LTO | 9416434 | +11.8% |
| `llimport` | 8423078 | LLGo · deadcode drop | 8255894 | -2.0% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 8536720 | +1.3% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 7644918 | -9.2% |
| `path-report` | 2381190 | LLGo · no LTO | 1925642 | -19.1% |
| `path-report` | 2381190 | LLGo · deadcode drop | 1286437 | -46.0% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1678679 | -29.5% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 1154221 | -51.5% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 2678472 | -3.7% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1671972 | -39.9% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 2351259 | -15.5% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1503348 | -45.9% |
| `word-count` | 2253620 | LLGo · no LTO | 1641981 | -27.1% |
| `word-count` | 2253620 | LLGo · deadcode drop | 1017307 | -54.9% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 1404192 | -37.7% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 891194 | -60.5% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 13.245x | 10 |
| LLGo · deadcode drop | 8.251x | 10 |
| LLGo · full LTO (GlobalDCE off) | 11.464x | 10 |
| LLGo · full LTO + GlobalDCE | 7.371x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1529793 | +1481.0% |
| `base64` | 96760 | LLGo · deadcode drop | 928019 | +859.1% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 1310314 | +1254.2% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 814597 | +741.9% |
| `checksum` | 92685 | LLGo · no LTO | 1516500 | +1536.2% |
| `checksum` | 92685 | LLGo · deadcode drop | 909594 | +881.4% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 1291913 | +1293.9% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 795177 | +757.9% |
| `conv-wasi` | 201149 | LLGo · no LTO | 2420043 | +1103.1% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 1431979 | +611.9% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 2117547 | +952.7% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1277107 | +534.9% |
| `fibonacci` | 62386 | LLGo · no LTO | 1345734 | +2057.1% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 850218 | +1262.8% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 1138301 | +1724.6% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 741459 | +1088.5% |
| `glob` | 93153 | LLGo · no LTO | 1674884 | +1698.0% |
| `glob` | 93153 | LLGo · deadcode drop | 1041168 | +1017.7% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1435802 | +1441.3% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 917611 | +885.1% |
| `grep` | 303772 | LLGo · no LTO | 2063974 | +579.4% |
| `grep` | 303772 | LLGo · deadcode drop | 1365286 | +349.4% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1804837 | +494.1% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 1246504 | +310.3% |
| `json-wasi` | 493590 | LLGo · no LTO | 3446047 | +598.2% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 2099236 | +325.3% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 3067080 | +521.4% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 2001599 | +305.5% |
| `llimport` | — | LLGo · no LTO | 9416434 | — |
| `llimport` | — | LLGo · deadcode drop | 8255894 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 8536720 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 7644918 | — |
| `path-report` | 116889 | LLGo · no LTO | 1925642 | +1547.4% |
| `path-report` | 116889 | LLGo · deadcode drop | 1286437 | +1000.6% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1678679 | +1336.1% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 1154221 | +887.5% |
| `sha-wasi` | 287449 | LLGo · no LTO | 2678472 | +831.8% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1671972 | +481.7% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 2351259 | +718.0% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1503348 | +423.0% |
| `word-count` | 86834 | LLGo · no LTO | 1641981 | +1790.9% |
| `word-count` | 86834 | LLGo · deadcode drop | 1017307 | +1071.6% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 1404192 | +1517.1% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 891194 | +926.3% |

## js/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 1.029x | 12 |
| LLGo · deadcode drop | 0.666x | 12 |
| LLGo · full LTO (GlobalDCE off) | 0.924x | 12 |
| LLGo · full LTO + GlobalDCE | 0.621x | 12 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1957665 | -15.7% |
| `base64` | 2322402 | LLGo · deadcode drop | 1154596 | -50.3% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1739399 | -25.1% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1061520 | -54.3% |
| `checksum` | 2311672 | LLGo · no LTO | 1938082 | -16.2% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1127941 | -51.2% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1704505 | -26.3% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1027549 | -55.5% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 3072854 | +16.5% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1749939 | -33.7% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2744473 | +4.0% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1607564 | -39.1% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1702807 | -25.1% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 1047361 | -53.9% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1493235 | -34.3% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 959829 | -57.8% |
| `glob` | 2305059 | LLGo · no LTO | 2093838 | -9.2% |
| `glob` | 2305059 | LLGo · deadcode drop | 1251961 | -45.7% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1846047 | -19.9% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1145256 | -50.3% |
| `grep` | 2871426 | LLGo · no LTO | 2641027 | -8.0% |
| `grep` | 2871426 | LLGo · deadcode drop | 1688199 | -41.2% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2324473 | -19.0% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1559838 | -45.7% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4281158 | +28.2% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2558459 | -23.4% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3905453 | +17.0% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2521164 | -24.5% |
| `llimport` | 8440671 | LLGo · no LTO | 11421905 | +35.3% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9780668 | +15.9% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10445057 | +23.7% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 9102792 | +7.8% |
| `path-report` | 2428068 | LLGo · no LTO | 2428397 | +0.0% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1576620 | -35.1% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 2170012 | -10.6% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1460364 | -39.9% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3428257 | +22.0% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 2070176 | -26.4% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 3106077 | +10.5% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1946515 | -30.8% |
| `tsgo` | 50367588 | LLGo · no LTO | 73144159 | +45.2% |
| `tsgo` | 50367588 | LLGo · deadcode drop | 72132207 | +43.2% |
| `tsgo` | 50367588 | LLGo · full LTO (GlobalDCE off) | 71542522 | +42.0% |
| `tsgo` | 50367588 | LLGo · full LTO + GlobalDCE | 71215386 | +41.4% |
| `word-count` | 2300998 | LLGo · no LTO | 2053946 | -10.7% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1224982 | -46.8% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1805049 | -21.6% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1112027 | -51.7% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 12.503x | 10 |
| LLGo · deadcode drop | 7.547x | 10 |
| LLGo · full LTO (GlobalDCE off) | 11.115x | 10 |
| LLGo · full LTO + GlobalDCE | 6.990x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1957665 | +1036.2% |
| `base64` | 172302 | LLGo · deadcode drop | 1154596 | +570.1% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1739399 | +909.5% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1061520 | +516.1% |
| `checksum` | 169609 | LLGo · no LTO | 1938082 | +1042.7% |
| `checksum` | 169609 | LLGo · deadcode drop | 1127941 | +565.0% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1704505 | +905.0% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1027549 | +505.8% |
| `conv-wasi` | 165385 | LLGo · no LTO | 3072854 | +1758.0% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1749939 | +958.1% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2744473 | +1559.4% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1607564 | +872.0% |
| `fibonacci` | 141855 | LLGo · no LTO | 1702807 | +1100.4% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 1047361 | +638.3% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1493235 | +952.6% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 959829 | +576.6% |
| `glob` | 136553 | LLGo · no LTO | 2093838 | +1433.4% |
| `glob` | 136553 | LLGo · deadcode drop | 1251961 | +816.8% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1846047 | +1251.9% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1145256 | +738.7% |
| `grep` | 155984 | LLGo · no LTO | 2641027 | +1593.1% |
| `grep` | 155984 | LLGo · deadcode drop | 1688199 | +982.3% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2324473 | +1390.2% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1559838 | +900.0% |
| `json-wasi` | 525666 | LLGo · no LTO | 4281158 | +714.4% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2558459 | +386.7% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3905453 | +643.0% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2521164 | +379.6% |
| `llimport` | — | LLGo · no LTO | 11421905 | — |
| `llimport` | — | LLGo · deadcode drop | 9780668 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10445057 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 9102792 | — |
| `path-report` | 194133 | LLGo · no LTO | 2428397 | +1150.9% |
| `path-report` | 194133 | LLGo · deadcode drop | 1576620 | +712.1% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 2170012 | +1017.8% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1460364 | +652.2% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3428257 | +874.0% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 2070176 | +488.2% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 3106077 | +782.5% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1946515 | +453.0% |
| `tsgo` | — | LLGo · no LTO | 73144159 | — |
| `tsgo` | — | LLGo · deadcode drop | 72132207 | — |
| `tsgo` | — | LLGo · full LTO (GlobalDCE off) | 71542522 | — |
| `tsgo` | — | LLGo · full LTO + GlobalDCE | 71215386 | — |
| `word-count` | 164053 | LLGo · no LTO | 2053946 | +1152.0% |
| `word-count` | 164053 | LLGo · deadcode drop | 1224982 | +646.7% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1805049 | +1000.3% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1112027 | +577.8% |
