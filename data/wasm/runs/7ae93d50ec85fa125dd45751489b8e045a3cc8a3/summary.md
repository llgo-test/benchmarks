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
| LLGo · no LTO | 0.914x | 11 |
| LLGo · deadcode drop | 0.560x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.814x | 11 |
| LLGo · full LTO + GlobalDCE | 0.565x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1918248 | -17.4% |
| `base64` | 2322402 | LLGo · deadcode drop | 1081705 | -53.4% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1673218 | -28.0% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1075097 | -53.7% |
| `checksum` | 2311672 | LLGo · no LTO | 1898882 | -17.9% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1066869 | -53.8% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1637742 | -29.2% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1041924 | -54.9% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2819889 | +6.9% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1587041 | -39.9% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2543479 | -3.6% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1621072 | -38.6% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1192637 | -47.6% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 957174 | -57.9% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 990256 | -56.5% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 859239 | -62.2% |
| `grep` | 2871426 | LLGo · no LTO | 2573209 | -10.4% |
| `grep` | 2871426 | LLGo · deadcode drop | 1584279 | -44.8% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2231066 | -22.3% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1555366 | -45.8% |
| `glob` | 2305059 | LLGo · no LTO | 1949426 | -15.4% |
| `glob` | 2305059 | LLGo · deadcode drop | 1086219 | -52.9% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1762811 | -23.5% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1147945 | -50.2% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4117755 | +23.3% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2318558 | -30.5% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3800655 | +13.8% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2537270 | -24.0% |
| `llimport` | 8440671 | LLGo · no LTO | 10963434 | +29.9% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9309304 | +10.3% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10062862 | +19.2% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 9015606 | +6.8% |
| `path-report` | 2428068 | LLGo · no LTO | 2092845 | -13.8% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1217354 | -49.9% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 1891407 | -22.1% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1277559 | -47.4% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3168597 | +12.7% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1891872 | -32.7% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2890508 | +2.8% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1961249 | -30.2% |
| `word-count` | 2300998 | LLGo · no LTO | 1908554 | -17.1% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1062624 | -53.8% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1719703 | -25.3% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1115121 | -51.5% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.404x | 10 |
| LLGo · deadcode drop | 6.759x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.120x | 10 |
| LLGo · full LTO + GlobalDCE | 6.856x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1918248 | +1013.3% |
| `base64` | 172302 | LLGo · deadcode drop | 1081705 | +527.8% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1673218 | +871.1% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1075097 | +524.0% |
| `checksum` | 169609 | LLGo · no LTO | 1898882 | +1019.6% |
| `checksum` | 169609 | LLGo · deadcode drop | 1066869 | +529.0% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1637742 | +865.6% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1041924 | +514.3% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2819889 | +1605.0% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1587041 | +859.6% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2543479 | +1437.9% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1621072 | +880.2% |
| `fibonacci` | 141855 | LLGo · no LTO | 1192637 | +740.7% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 957174 | +574.8% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 990256 | +598.1% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 859239 | +505.7% |
| `grep` | 155984 | LLGo · no LTO | 2573209 | +1549.7% |
| `grep` | 155984 | LLGo · deadcode drop | 1584279 | +915.7% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2231066 | +1330.3% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1555366 | +897.1% |
| `glob` | 136553 | LLGo · no LTO | 1949426 | +1327.6% |
| `glob` | 136553 | LLGo · deadcode drop | 1086219 | +695.5% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1762811 | +1190.9% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1147945 | +740.7% |
| `json-wasi` | 525666 | LLGo · no LTO | 4117755 | +683.3% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2318558 | +341.1% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3800655 | +623.0% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2537270 | +382.7% |
| `llimport` | — | LLGo · no LTO | 10963434 | — |
| `llimport` | — | LLGo · deadcode drop | 9309304 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10062862 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 9015606 | — |
| `path-report` | 194133 | LLGo · no LTO | 2092845 | +978.0% |
| `path-report` | 194133 | LLGo · deadcode drop | 1217354 | +527.1% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 1891407 | +874.3% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1277559 | +558.1% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3168597 | +800.2% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1891872 | +437.5% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2890508 | +721.2% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1961249 | +457.2% |
| `word-count` | 164053 | LLGo · no LTO | 1908554 | +1063.4% |
| `word-count` | 164053 | LLGo · deadcode drop | 1062624 | +547.7% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1719703 | +948.3% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1115121 | +579.7% |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.308x | 11 |
| LLGo · deadcode drop | 0.308x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.470x | 11 |
| LLGo · full LTO + GlobalDCE | 0.336x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 544478 | -76.1% |
| `base64` | 2275731 | LLGo · deadcode drop | 544478 | -76.1% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 852230 | -62.6% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 577436 | -74.6% |
| `checksum` | 2264417 | LLGo · no LTO | 530876 | -76.6% |
| `checksum` | 2264417 | LLGo · deadcode drop | 530876 | -76.6% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 836277 | -63.1% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 558545 | -75.3% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 896677 | -65.6% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 896677 | -65.6% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1566562 | -39.9% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 993545 | -61.9% |
| `fibonacci` | 2230899 | LLGo · no LTO | 447462 | -79.9% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 447462 | -79.9% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 466325 | -79.1% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 421511 | -81.1% |
| `grep` | 2848917 | LLGo · no LTO | 879964 | -69.1% |
| `grep` | 2848917 | LLGo · deadcode drop | 879964 | -69.1% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1311070 | -54.0% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 925084 | -67.5% |
| `glob` | 2257634 | LLGo · no LTO | 536598 | -76.2% |
| `glob` | 2257634 | LLGo · deadcode drop | 536598 | -76.2% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 970807 | -57.0% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 651208 | -71.2% |
| `json-wasi` | 3314587 | LLGo · no LTO | 1442422 | -56.5% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1442422 | -56.5% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2508567 | -24.3% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1671719 | -49.6% |
| `llimport` | 8423078 | LLGo · no LTO | 6664611 | -20.9% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6664611 | -20.9% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 6824771 | -19.0% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6559418 | -22.1% |
| `path-report` | 2381190 | LLGo · no LTO | 647239 | -72.8% |
| `path-report` | 2381190 | LLGo · deadcode drop | 647239 | -72.8% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1077836 | -54.7% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 757805 | -68.2% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1060306 | -61.9% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1060306 | -61.9% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1742830 | -37.3% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1170474 | -57.9% |
| `word-count` | 2253620 | LLGo · no LTO | 529978 | -76.5% |
| `word-count` | 2253620 | LLGo · deadcode drop | 529978 | -76.5% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 924582 | -59.0% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 635440 | -71.8% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 4.783x | 10 |
| LLGo · deadcode drop | 4.783x | 10 |
| LLGo · full LTO (GlobalDCE off) | 7.584x | 10 |
| LLGo · full LTO + GlobalDCE | 5.276x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 544478 | +462.7% |
| `base64` | 96760 | LLGo · deadcode drop | 544478 | +462.7% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 852230 | +780.8% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 577436 | +496.8% |
| `checksum` | 92685 | LLGo · no LTO | 530876 | +472.8% |
| `checksum` | 92685 | LLGo · deadcode drop | 530876 | +472.8% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 836277 | +802.3% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 558545 | +502.6% |
| `conv-wasi` | 201149 | LLGo · no LTO | 896677 | +345.8% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 896677 | +345.8% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1566562 | +678.8% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 993545 | +393.9% |
| `fibonacci` | 62386 | LLGo · no LTO | 447462 | +617.2% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 447462 | +617.2% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 466325 | +647.5% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 421511 | +575.6% |
| `grep` | 303772 | LLGo · no LTO | 879964 | +189.7% |
| `grep` | 303772 | LLGo · deadcode drop | 879964 | +189.7% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1311070 | +331.6% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 925084 | +204.5% |
| `glob` | 93153 | LLGo · no LTO | 536598 | +476.0% |
| `glob` | 93153 | LLGo · deadcode drop | 536598 | +476.0% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 970807 | +942.2% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 651208 | +599.1% |
| `json-wasi` | 493590 | LLGo · no LTO | 1442422 | +192.2% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1442422 | +192.2% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2508567 | +408.2% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1671719 | +238.7% |
| `llimport` | — | LLGo · no LTO | 6664611 | — |
| `llimport` | — | LLGo · deadcode drop | 6664611 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 6824771 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6559418 | — |
| `path-report` | 116889 | LLGo · no LTO | 647239 | +453.7% |
| `path-report` | 116889 | LLGo · deadcode drop | 647239 | +453.7% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1077836 | +822.1% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 757805 | +548.3% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1060306 | +268.9% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1060306 | +268.9% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1742830 | +506.3% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1170474 | +307.2% |
| `word-count` | 86834 | LLGo · no LTO | 529978 | +510.3% |
| `word-count` | 86834 | LLGo · deadcode drop | 529978 | +510.3% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 924582 | +964.8% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 635440 | +631.8% |
