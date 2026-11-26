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
| LLGo · no LTO | 0.912x | 11 |
| LLGo · deadcode drop | 0.558x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.812x | 11 |
| LLGo · full LTO + GlobalDCE | 0.566x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1909050 | -17.8% |
| `base64` | 2322402 | LLGo · deadcode drop | 1076388 | -53.7% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1665811 | -28.3% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1073155 | -53.8% |
| `checksum` | 2311672 | LLGo · no LTO | 1890269 | -18.2% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1061996 | -54.1% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1631414 | -29.4% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1040875 | -55.0% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2817531 | +6.8% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1587766 | -39.8% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2544102 | -3.6% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1626391 | -38.4% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1189413 | -47.7% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 954105 | -58.0% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 988232 | -56.5% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 857200 | -62.3% |
| `grep` | 2871426 | LLGo · no LTO | 2570456 | -10.5% |
| `grep` | 2871426 | LLGo · deadcode drop | 1583002 | -44.9% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2231297 | -22.3% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1558885 | -45.7% |
| `glob` | 2305059 | LLGo · no LTO | 1940126 | -15.8% |
| `glob` | 2305059 | LLGo · deadcode drop | 1080850 | -53.1% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1755815 | -23.8% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1146273 | -50.3% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4114066 | +23.2% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2318756 | -30.5% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3798891 | +13.8% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2544513 | -23.8% |
| `llimport` | 8440671 | LLGo · no LTO | 10960196 | +29.8% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9313489 | +10.3% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10061758 | +19.2% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 9020108 | +6.9% |
| `path-report` | 2428068 | LLGo · no LTO | 2083776 | -14.2% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1212163 | -50.1% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 1884560 | -22.4% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1276044 | -47.4% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3166972 | +12.7% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1893182 | -32.7% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2891136 | +2.8% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1968050 | -30.0% |
| `word-count` | 2300998 | LLGo · no LTO | 1899975 | -17.4% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1057877 | -54.0% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1713384 | -25.5% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1114134 | -51.6% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.371x | 10 |
| LLGo · deadcode drop | 6.741x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.099x | 10 |
| LLGo · full LTO + GlobalDCE | 6.858x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1909050 | +1008.0% |
| `base64` | 172302 | LLGo · deadcode drop | 1076388 | +524.7% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1665811 | +866.8% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1073155 | +522.8% |
| `checksum` | 169609 | LLGo · no LTO | 1890269 | +1014.5% |
| `checksum` | 169609 | LLGo · deadcode drop | 1061996 | +526.1% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1631414 | +861.9% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1040875 | +513.7% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2817531 | +1603.6% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1587766 | +860.0% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2544102 | +1438.3% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1626391 | +883.4% |
| `fibonacci` | 141855 | LLGo · no LTO | 1189413 | +738.5% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 954105 | +572.6% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 988232 | +596.6% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 857200 | +504.3% |
| `grep` | 155984 | LLGo · no LTO | 2570456 | +1547.9% |
| `grep` | 155984 | LLGo · deadcode drop | 1583002 | +914.8% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2231297 | +1330.5% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1558885 | +899.4% |
| `glob` | 136553 | LLGo · no LTO | 1940126 | +1320.8% |
| `glob` | 136553 | LLGo · deadcode drop | 1080850 | +691.5% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1755815 | +1185.8% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1146273 | +739.4% |
| `json-wasi` | 525666 | LLGo · no LTO | 4114066 | +682.6% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2318756 | +341.1% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3798891 | +622.7% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2544513 | +384.1% |
| `llimport` | — | LLGo · no LTO | 10960196 | — |
| `llimport` | — | LLGo · deadcode drop | 9313489 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10061758 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 9020108 | — |
| `path-report` | 194133 | LLGo · no LTO | 2083776 | +973.4% |
| `path-report` | 194133 | LLGo · deadcode drop | 1212163 | +524.4% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 1884560 | +870.8% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1276044 | +557.3% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3166972 | +799.8% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1893182 | +437.9% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2891136 | +721.4% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1968050 | +459.2% |
| `word-count` | 164053 | LLGo · no LTO | 1899975 | +1058.1% |
| `word-count` | 164053 | LLGo · deadcode drop | 1057877 | +544.8% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1713384 | +944.4% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1114134 | +579.1% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.309x | 11 |
| LLGo · deadcode drop | 0.309x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.466x | 11 |
| LLGo · full LTO + GlobalDCE | 0.338x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 542576 | -76.2% |
| `base64` | 2275731 | LLGo · deadcode drop | 542576 | -76.2% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 839149 | -63.1% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 577532 | -74.6% |
| `checksum` | 2264417 | LLGo · no LTO | 529362 | -76.6% |
| `checksum` | 2264417 | LLGo · deadcode drop | 529362 | -76.6% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 823783 | -63.6% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 559036 | -75.3% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 905165 | -65.3% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 905165 | -65.3% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1561092 | -40.1% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1004638 | -61.5% |
| `fibonacci` | 2230899 | LLGo · no LTO | 449540 | -79.8% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 449540 | -79.8% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 467998 | -79.0% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 423677 | -81.0% |
| `grep` | 2848917 | LLGo · no LTO | 882268 | -69.0% |
| `grep` | 2848917 | LLGo · deadcode drop | 882268 | -69.0% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1302040 | -54.3% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 930599 | -67.3% |
| `glob` | 2257634 | LLGo · no LTO | 534696 | -76.3% |
| `glob` | 2257634 | LLGo · deadcode drop | 534696 | -76.3% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 953932 | -57.7% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 651281 | -71.2% |
| `json-wasi` | 3314587 | LLGo · no LTO | 1455859 | -56.1% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1455859 | -56.1% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2496462 | -24.7% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1688005 | -49.1% |
| `llimport` | 8423078 | LLGo · no LTO | 6742902 | -19.9% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6742902 | -19.9% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 6882446 | -18.3% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6636021 | -21.2% |
| `path-report` | 2381190 | LLGo · no LTO | 645566 | -72.9% |
| `path-report` | 2381190 | LLGo · deadcode drop | 645566 | -72.9% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1061200 | -55.4% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 758117 | -68.2% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1072797 | -61.4% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1072797 | -61.4% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1742144 | -37.4% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1186582 | -57.3% |
| `word-count` | 2253620 | LLGo · no LTO | 528605 | -76.5% |
| `word-count` | 2253620 | LLGo · deadcode drop | 528605 | -76.5% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 912112 | -59.5% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 636045 | -71.8% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 4.794x | 10 |
| LLGo · deadcode drop | 4.794x | 10 |
| LLGo · full LTO (GlobalDCE off) | 7.517x | 10 |
| LLGo · full LTO + GlobalDCE | 5.302x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 542576 | +460.7% |
| `base64` | 96760 | LLGo · deadcode drop | 542576 | +460.7% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 839149 | +767.2% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 577532 | +496.9% |
| `checksum` | 92685 | LLGo · no LTO | 529362 | +471.1% |
| `checksum` | 92685 | LLGo · deadcode drop | 529362 | +471.1% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 823783 | +788.8% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 559036 | +503.2% |
| `conv-wasi` | 201149 | LLGo · no LTO | 905165 | +350.0% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 905165 | +350.0% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1561092 | +676.1% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1004638 | +399.4% |
| `fibonacci` | 62386 | LLGo · no LTO | 449540 | +620.6% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 449540 | +620.6% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 467998 | +650.2% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 423677 | +579.1% |
| `grep` | 303772 | LLGo · no LTO | 882268 | +190.4% |
| `grep` | 303772 | LLGo · deadcode drop | 882268 | +190.4% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1302040 | +328.6% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 930599 | +206.3% |
| `glob` | 93153 | LLGo · no LTO | 534696 | +474.0% |
| `glob` | 93153 | LLGo · deadcode drop | 534696 | +474.0% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 953932 | +924.0% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 651281 | +599.2% |
| `json-wasi` | 493590 | LLGo · no LTO | 1455859 | +195.0% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1455859 | +195.0% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2496462 | +405.8% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1688005 | +242.0% |
| `llimport` | — | LLGo · no LTO | 6742902 | — |
| `llimport` | — | LLGo · deadcode drop | 6742902 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 6882446 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6636021 | — |
| `path-report` | 116889 | LLGo · no LTO | 645566 | +452.3% |
| `path-report` | 116889 | LLGo · deadcode drop | 645566 | +452.3% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1061200 | +807.9% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 758117 | +548.6% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1072797 | +273.2% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1072797 | +273.2% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1742144 | +506.1% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1186582 | +312.8% |
| `word-count` | 86834 | LLGo · no LTO | 528605 | +508.8% |
| `word-count` | 86834 | LLGo · deadcode drop | 528605 | +508.8% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 912112 | +950.4% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 636045 | +632.5% |
