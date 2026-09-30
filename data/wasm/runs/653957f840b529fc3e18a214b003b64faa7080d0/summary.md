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
| LLGo · no LTO | 1.072x | 11 |
| LLGo · deadcode drop | 0.654x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.960x | 11 |
| LLGo · full LTO + GlobalDCE | 0.608x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 2084889 | -10.2% |
| `base64` | 2322402 | LLGo · deadcode drop | 1188880 | -48.8% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1859641 | -19.9% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1096190 | -52.8% |
| `checksum` | 2311672 | LLGo · no LTO | 2064780 | -10.7% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1160788 | -49.8% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1824214 | -21.1% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1060580 | -54.1% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 3291245 | +24.7% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1837899 | -30.3% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2951143 | +11.8% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1693257 | -35.8% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1811573 | -20.3% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 1077737 | -52.6% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1594786 | -29.9% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 990101 | -56.5% |
| `grep` | 2871426 | LLGo · no LTO | 2824717 | -1.6% |
| `grep` | 2871426 | LLGo · deadcode drop | 1771119 | -38.3% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2499697 | -12.9% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1643471 | -42.8% |
| `glob` | 2305059 | LLGo · no LTO | 2251858 | -2.3% |
| `glob` | 2305059 | LLGo · deadcode drop | 1315305 | -42.9% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1995686 | -13.4% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1207239 | -47.6% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4604973 | +37.9% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2714662 | -18.7% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 4208398 | +26.1% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2677651 | -19.8% |
| `llimport` | 8440671 | LLGo · no LTO | 12833887 | +52.0% |
| `llimport` | 8440671 | LLGo · deadcode drop | 11012814 | +30.5% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 11830770 | +40.2% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 10318057 | +22.2% |
| `path-report` | 2428068 | LLGo · no LTO | 2600522 | +7.1% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1653669 | -31.9% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 2331015 | -4.0% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1534014 | -36.8% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3660705 | +30.2% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 2170821 | -22.8% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 3325378 | +18.3% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 2043640 | -27.3% |
| `word-count` | 2300998 | LLGo · no LTO | 2211178 | -3.9% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1287521 | -44.0% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1953544 | -15.1% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1173282 | -49.0% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 13.380x | 10 |
| LLGo · deadcode drop | 7.885x | 10 |
| LLGo · full LTO (GlobalDCE off) | 11.942x | 10 |
| LLGo · full LTO + GlobalDCE | 7.322x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 2084889 | +1110.0% |
| `base64` | 172302 | LLGo · deadcode drop | 1188880 | +590.0% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1859641 | +979.3% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1096190 | +536.2% |
| `checksum` | 169609 | LLGo · no LTO | 2064780 | +1117.4% |
| `checksum` | 169609 | LLGo · deadcode drop | 1160788 | +584.4% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1824214 | +975.5% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1060580 | +525.3% |
| `conv-wasi` | 165385 | LLGo · no LTO | 3291245 | +1890.1% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1837899 | +1011.3% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2951143 | +1684.4% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1693257 | +923.8% |
| `fibonacci` | 141855 | LLGo · no LTO | 1811573 | +1177.1% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 1077737 | +659.7% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1594786 | +1024.2% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 990101 | +598.0% |
| `grep` | 155984 | LLGo · no LTO | 2824717 | +1710.9% |
| `grep` | 155984 | LLGo · deadcode drop | 1771119 | +1035.4% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2499697 | +1502.5% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1643471 | +953.6% |
| `glob` | 136553 | LLGo · no LTO | 2251858 | +1549.1% |
| `glob` | 136553 | LLGo · deadcode drop | 1315305 | +863.2% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1995686 | +1361.5% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1207239 | +784.1% |
| `json-wasi` | 525666 | LLGo · no LTO | 4604973 | +776.0% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2714662 | +416.4% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 4208398 | +700.6% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2677651 | +409.4% |
| `llimport` | — | LLGo · no LTO | 12833887 | — |
| `llimport` | — | LLGo · deadcode drop | 11012814 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 11830770 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 10318057 | — |
| `path-report` | 194133 | LLGo · no LTO | 2600522 | +1239.6% |
| `path-report` | 194133 | LLGo · deadcode drop | 1653669 | +751.8% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 2331015 | +1100.7% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1534014 | +690.2% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3660705 | +940.1% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 2170821 | +516.8% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 3325378 | +844.8% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 2043640 | +480.6% |
| `word-count` | 164053 | LLGo · no LTO | 2211178 | +1247.8% |
| `word-count` | 164053 | LLGo · deadcode drop | 1287521 | +684.8% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1953544 | +1090.8% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1173282 | +615.2% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.917x | 11 |
| LLGo · deadcode drop | 0.592x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.736x | 11 |
| LLGo · full LTO + GlobalDCE | 0.528x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1682030 | -26.1% |
| `base64` | 2275731 | LLGo · deadcode drop | 1021194 | -55.1% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 1315739 | -42.2% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 921485 | -59.5% |
| `checksum` | 2264417 | LLGo · no LTO | 1658932 | -26.7% |
| `checksum` | 2264417 | LLGo · deadcode drop | 993482 | -56.1% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 1285981 | -43.2% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 888900 | -60.7% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 2810639 | +7.8% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 1643177 | -37.0% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 2360714 | -9.5% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1481672 | -43.2% |
| `fibonacci` | 2230899 | LLGo · no LTO | 1392519 | -37.6% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 918473 | -58.8% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 1120992 | -49.8% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 828304 | -62.9% |
| `grep` | 2848917 | LLGo · no LTO | 2384097 | -16.3% |
| `grep` | 2848917 | LLGo · deadcode drop | 1591933 | -44.1% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1935008 | -32.1% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 1425828 | -50.0% |
| `glob` | 2257634 | LLGo · no LTO | 1850008 | -18.1% |
| `glob` | 2257634 | LLGo · deadcode drop | 1152025 | -49.0% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1477981 | -34.5% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 1040758 | -53.9% |
| `json-wasi` | 3314587 | LLGo · no LTO | 4118709 | +24.3% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 2500109 | -24.6% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 3480065 | +5.0% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 2376883 | -28.3% |
| `llimport` | 8423078 | LLGo · no LTO | 12457108 | +47.9% |
| `llimport` | 8423078 | LLGo · deadcode drop | 10983037 | +30.4% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 8990449 | +6.7% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 8288497 | -1.6% |
| `path-report` | 2381190 | LLGo · no LTO | 2190290 | -8.0% |
| `path-report` | 2381190 | LLGo · deadcode drop | 1483272 | -37.7% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1804345 | -24.2% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 1358120 | -43.0% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 3146063 | +13.1% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1948014 | -30.0% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 2671067 | -4.0% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1777089 | -36.1% |
| `word-count` | 2253620 | LLGo · no LTO | 1810402 | -19.7% |
| `word-count` | 2253620 | LLGo · deadcode drop | 1125446 | -50.1% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 1422252 | -36.9% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 1008179 | -55.3% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 14.901x | 10 |
| LLGo · deadcode drop | 9.326x | 10 |
| LLGo · full LTO (GlobalDCE off) | 12.088x | 10 |
| LLGo · full LTO + GlobalDCE | 8.461x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1682030 | +1638.4% |
| `base64` | 96760 | LLGo · deadcode drop | 1021194 | +955.4% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 1315739 | +1259.8% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 921485 | +852.3% |
| `checksum` | 92685 | LLGo · no LTO | 1658932 | +1689.9% |
| `checksum` | 92685 | LLGo · deadcode drop | 993482 | +971.9% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 1285981 | +1287.5% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 888900 | +859.1% |
| `conv-wasi` | 201149 | LLGo · no LTO | 2810639 | +1297.3% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 1643177 | +716.9% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 2360714 | +1073.6% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1481672 | +636.6% |
| `fibonacci` | 62386 | LLGo · no LTO | 1392519 | +2132.1% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 918473 | +1372.2% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 1120992 | +1696.9% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 828304 | +1227.7% |
| `grep` | 303772 | LLGo · no LTO | 2384097 | +684.8% |
| `grep` | 303772 | LLGo · deadcode drop | 1591933 | +424.1% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1935008 | +537.0% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 1425828 | +369.4% |
| `glob` | 93153 | LLGo · no LTO | 1850008 | +1886.0% |
| `glob` | 93153 | LLGo · deadcode drop | 1152025 | +1136.7% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1477981 | +1486.6% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 1040758 | +1017.3% |
| `json-wasi` | 493590 | LLGo · no LTO | 4118709 | +734.4% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 2500109 | +406.5% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 3480065 | +605.1% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 2376883 | +381.6% |
| `llimport` | — | LLGo · no LTO | 12457108 | — |
| `llimport` | — | LLGo · deadcode drop | 10983037 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 8990449 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 8288497 | — |
| `path-report` | 116889 | LLGo · no LTO | 2190290 | +1773.8% |
| `path-report` | 116889 | LLGo · deadcode drop | 1483272 | +1169.0% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1804345 | +1443.6% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 1358120 | +1061.9% |
| `sha-wasi` | 287449 | LLGo · no LTO | 3146063 | +994.5% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1948014 | +577.7% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 2671067 | +829.2% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1777089 | +518.2% |
| `word-count` | 86834 | LLGo · no LTO | 1810402 | +1984.9% |
| `word-count` | 86834 | LLGo · deadcode drop | 1125446 | +1196.1% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 1422252 | +1537.9% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 1008179 | +1061.0% |
