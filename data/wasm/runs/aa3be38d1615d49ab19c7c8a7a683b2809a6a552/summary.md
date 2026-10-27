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
| word-count | wasip1/wasm | 1.26.2 | - | - | word-count |
| word-count-js | js/wasm | 1.26.2 | - | - | word-count |

## wasip1/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.599x | 11 |
| LLGo · deadcode drop | 0.315x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.505x | 11 |
| LLGo · full LTO + GlobalDCE | 0.351x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1103637 | -51.5% |
| `base64` | 2275731 | LLGo · deadcode drop | 508350 | -77.7% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 875875 | -61.5% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 587416 | -74.2% |
| `checksum` | 2264417 | LLGo · no LTO | 1087285 | -52.0% |
| `checksum` | 2264417 | LLGo · deadcode drop | 495493 | -78.1% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 859787 | -62.0% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 568360 | -74.9% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 1784418 | -31.6% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 920643 | -64.7% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1567009 | -39.9% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 971936 | -62.7% |
| `fibonacci` | 2230899 | LLGo · no LTO | 898094 | -59.7% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 412216 | -81.5% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 764581 | -65.7% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 521582 | -76.6% |
| `glob` | 2257634 | LLGo · no LTO | 1223353 | -45.8% |
| `glob` | 2257634 | LLGo · deadcode drop | 605803 | -73.2% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1011282 | -55.2% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 674770 | -70.1% |
| `grep` | 2848917 | LLGo · no LTO | 1549729 | -45.6% |
| `grep` | 2848917 | LLGo · deadcode drop | 849328 | -70.2% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1356676 | -52.4% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 959191 | -66.3% |
| `json-wasi` | 3314587 | LLGo · no LTO | 2799776 | -15.5% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1429508 | -56.9% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2483507 | -25.1% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1616552 | -51.2% |
| `llimport` | 8423078 | LLGo · no LTO | 8062448 | -4.3% |
| `llimport` | 8423078 | LLGo · deadcode drop | 6568325 | -22.0% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 6890437 | -18.2% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6627901 | -21.3% |
| `path-report` | 2381190 | LLGo · no LTO | 1456541 | -38.8% |
| `path-report` | 2381190 | LLGo · deadcode drop | 829054 | -65.2% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1236797 | -48.1% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 894516 | -62.4% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 1973685 | -29.0% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1078983 | -61.2% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1739497 | -37.5% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1142747 | -58.9% |
| `word-count` | 2253620 | LLGo · no LTO | 1204645 | -46.5% |
| `word-count` | 2253620 | LLGo · deadcode drop | 597764 | -73.5% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 966118 | -57.1% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 659382 | -70.7% |

## wasip1/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 9.743x | 10 |
| LLGo · deadcode drop | 4.913x | 10 |
| LLGo · full LTO (GlobalDCE off) | 8.211x | 10 |
| LLGo · full LTO + GlobalDCE | 5.515x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1103637 | +1040.6% |
| `base64` | 96760 | LLGo · deadcode drop | 508350 | +425.4% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 875875 | +805.2% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 587416 | +507.1% |
| `checksum` | 92685 | LLGo · no LTO | 1087285 | +1073.1% |
| `checksum` | 92685 | LLGo · deadcode drop | 495493 | +434.6% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 859787 | +827.6% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 568360 | +513.2% |
| `conv-wasi` | 201149 | LLGo · no LTO | 1784418 | +787.1% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 920643 | +357.7% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1567009 | +679.0% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 971936 | +383.2% |
| `fibonacci` | 62386 | LLGo · no LTO | 898094 | +1339.6% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 412216 | +560.8% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 764581 | +1125.6% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 521582 | +736.1% |
| `glob` | 93153 | LLGo · no LTO | 1223353 | +1213.3% |
| `glob` | 93153 | LLGo · deadcode drop | 605803 | +550.3% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1011282 | +985.6% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 674770 | +624.4% |
| `grep` | 303772 | LLGo · no LTO | 1549729 | +410.2% |
| `grep` | 303772 | LLGo · deadcode drop | 849328 | +179.6% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1356676 | +346.6% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 959191 | +215.8% |
| `json-wasi` | 493590 | LLGo · no LTO | 2799776 | +467.2% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1429508 | +189.6% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2483507 | +403.2% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1616552 | +227.5% |
| `llimport` | — | LLGo · no LTO | 8062448 | — |
| `llimport` | — | LLGo · deadcode drop | 6568325 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 6890437 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6627901 | — |
| `path-report` | 116889 | LLGo · no LTO | 1456541 | +1146.1% |
| `path-report` | 116889 | LLGo · deadcode drop | 829054 | +609.3% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1236797 | +958.1% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 894516 | +665.3% |
| `sha-wasi` | 287449 | LLGo · no LTO | 1973685 | +586.6% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1078983 | +275.4% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1739497 | +505.1% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1142747 | +297.5% |
| `word-count` | 86834 | LLGo · no LTO | 1204645 | +1287.3% |
| `word-count` | 86834 | LLGo · deadcode drop | 597764 | +588.4% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 966118 | +1012.6% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 659382 | +659.4% |

## js/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.965x | 11 |
| LLGo · deadcode drop | 0.564x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.856x | 11 |
| LLGo · full LTO + GlobalDCE | 0.578x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2322402 | LLGo · no LTO | 1906083 | -17.9% |
| `base64` | 2322402 | LLGo · deadcode drop | 1033920 | -55.5% |
| `base64` | 2322402 | LLGo · full LTO (GlobalDCE off) | 1687307 | -27.3% |
| `base64` | 2322402 | LLGo · full LTO + GlobalDCE | 1076012 | -53.7% |
| `checksum` | 2311672 | LLGo · no LTO | 1885533 | -18.4% |
| `checksum` | 2311672 | LLGo · deadcode drop | 1019664 | -55.9% |
| `checksum` | 2311672 | LLGo · full LTO (GlobalDCE off) | 1650882 | -28.6% |
| `checksum` | 2311672 | LLGo · full LTO + GlobalDCE | 1041829 | -54.9% |
| `conv-wasi` | 2638493 | LLGo · no LTO | 2861380 | +8.4% |
| `conv-wasi` | 2638493 | LLGo · deadcode drop | 1593930 | -39.6% |
| `conv-wasi` | 2638493 | LLGo · full LTO (GlobalDCE off) | 2538689 | -3.8% |
| `conv-wasi` | 2638493 | LLGo · full LTO + GlobalDCE | 1592385 | -39.6% |
| `fibonacci` | 2274375 | LLGo · no LTO | 1686709 | -25.8% |
| `fibonacci` | 2274375 | LLGo · deadcode drop | 911270 | -59.9% |
| `fibonacci` | 2274375 | LLGo · full LTO (GlobalDCE off) | 1476073 | -35.1% |
| `fibonacci` | 2274375 | LLGo · full LTO + GlobalDCE | 978886 | -57.0% |
| `glob` | 2305059 | LLGo · no LTO | 2042275 | -11.4% |
| `glob` | 2305059 | LLGo · deadcode drop | 1145986 | -50.3% |
| `glob` | 2305059 | LLGo · full LTO (GlobalDCE off) | 1793640 | -22.2% |
| `glob` | 2305059 | LLGo · full LTO + GlobalDCE | 1161784 | -49.6% |
| `grep` | 2871426 | LLGo · no LTO | 2579613 | -10.2% |
| `grep` | 2871426 | LLGo · deadcode drop | 1547690 | -46.1% |
| `grep` | 2871426 | LLGo · full LTO (GlobalDCE off) | 2261763 | -21.2% |
| `grep` | 2871426 | LLGo · full LTO + GlobalDCE | 1568809 | -45.4% |
| `json-wasi` | 3338360 | LLGo · no LTO | 4154459 | +24.4% |
| `json-wasi` | 3338360 | LLGo · deadcode drop | 2302438 | -31.0% |
| `json-wasi` | 3338360 | LLGo · full LTO (GlobalDCE off) | 3778255 | +13.2% |
| `json-wasi` | 3338360 | LLGo · full LTO + GlobalDCE | 2494781 | -25.3% |
| `llimport` | 8440671 | LLGo · no LTO | 11068594 | +31.1% |
| `llimport` | 8440671 | LLGo · deadcode drop | 9120779 | +8.1% |
| `llimport` | 8440671 | LLGo · full LTO (GlobalDCE off) | 10101709 | +19.7% |
| `llimport` | 8440671 | LLGo · full LTO + GlobalDCE | 8975790 | +6.3% |
| `path-report` | 2428068 | LLGo · no LTO | 2375727 | -2.2% |
| `path-report` | 2428068 | LLGo · deadcode drop | 1464300 | -39.7% |
| `path-report` | 2428068 | LLGo · full LTO (GlobalDCE off) | 2116382 | -12.8% |
| `path-report` | 2428068 | LLGo · full LTO + GlobalDCE | 1475841 | -39.2% |
| `sha-wasi` | 2811136 | LLGo · no LTO | 3184845 | +13.3% |
| `sha-wasi` | 2811136 | LLGo · deadcode drop | 1867028 | -33.6% |
| `sha-wasi` | 2811136 | LLGo · full LTO (GlobalDCE off) | 2859487 | +1.7% |
| `sha-wasi` | 2811136 | LLGo · full LTO + GlobalDCE | 1903106 | -32.3% |
| `word-count` | 2300998 | LLGo · no LTO | 2002600 | -13.0% |
| `word-count` | 2300998 | LLGo · deadcode drop | 1121545 | -51.3% |
| `word-count` | 2300998 | LLGo · full LTO (GlobalDCE off) | 1752909 | -23.8% |
| `word-count` | 2300998 | LLGo · full LTO + GlobalDCE | 1129094 | -50.9% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 12.092x | 10 |
| LLGo · deadcode drop | 6.836x | 10 |
| LLGo · full LTO (GlobalDCE off) | 10.703x | 10 |
| LLGo · full LTO + GlobalDCE | 7.025x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 172302 | LLGo · no LTO | 1906083 | +1006.2% |
| `base64` | 172302 | LLGo · deadcode drop | 1033920 | +500.1% |
| `base64` | 172302 | LLGo · full LTO (GlobalDCE off) | 1687307 | +879.3% |
| `base64` | 172302 | LLGo · full LTO + GlobalDCE | 1076012 | +524.5% |
| `checksum` | 169609 | LLGo · no LTO | 1885533 | +1011.7% |
| `checksum` | 169609 | LLGo · deadcode drop | 1019664 | +501.2% |
| `checksum` | 169609 | LLGo · full LTO (GlobalDCE off) | 1650882 | +873.3% |
| `checksum` | 169609 | LLGo · full LTO + GlobalDCE | 1041829 | +514.3% |
| `conv-wasi` | 165385 | LLGo · no LTO | 2861380 | +1630.1% |
| `conv-wasi` | 165385 | LLGo · deadcode drop | 1593930 | +863.8% |
| `conv-wasi` | 165385 | LLGo · full LTO (GlobalDCE off) | 2538689 | +1435.0% |
| `conv-wasi` | 165385 | LLGo · full LTO + GlobalDCE | 1592385 | +862.8% |
| `fibonacci` | 141855 | LLGo · no LTO | 1686709 | +1089.0% |
| `fibonacci` | 141855 | LLGo · deadcode drop | 911270 | +542.4% |
| `fibonacci` | 141855 | LLGo · full LTO (GlobalDCE off) | 1476073 | +940.6% |
| `fibonacci` | 141855 | LLGo · full LTO + GlobalDCE | 978886 | +590.1% |
| `glob` | 136553 | LLGo · no LTO | 2042275 | +1395.6% |
| `glob` | 136553 | LLGo · deadcode drop | 1145986 | +739.2% |
| `glob` | 136553 | LLGo · full LTO (GlobalDCE off) | 1793640 | +1213.5% |
| `glob` | 136553 | LLGo · full LTO + GlobalDCE | 1161784 | +750.8% |
| `grep` | 155984 | LLGo · no LTO | 2579613 | +1553.8% |
| `grep` | 155984 | LLGo · deadcode drop | 1547690 | +892.2% |
| `grep` | 155984 | LLGo · full LTO (GlobalDCE off) | 2261763 | +1350.0% |
| `grep` | 155984 | LLGo · full LTO + GlobalDCE | 1568809 | +905.7% |
| `json-wasi` | 525666 | LLGo · no LTO | 4154459 | +690.3% |
| `json-wasi` | 525666 | LLGo · deadcode drop | 2302438 | +338.0% |
| `json-wasi` | 525666 | LLGo · full LTO (GlobalDCE off) | 3778255 | +618.8% |
| `json-wasi` | 525666 | LLGo · full LTO + GlobalDCE | 2494781 | +374.6% |
| `llimport` | — | LLGo · no LTO | 11068594 | — |
| `llimport` | — | LLGo · deadcode drop | 9120779 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 10101709 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 8975790 | — |
| `path-report` | 194133 | LLGo · no LTO | 2375727 | +1123.8% |
| `path-report` | 194133 | LLGo · deadcode drop | 1464300 | +654.3% |
| `path-report` | 194133 | LLGo · full LTO (GlobalDCE off) | 2116382 | +990.2% |
| `path-report` | 194133 | LLGo · full LTO + GlobalDCE | 1475841 | +660.2% |
| `sha-wasi` | 351971 | LLGo · no LTO | 3184845 | +804.9% |
| `sha-wasi` | 351971 | LLGo · deadcode drop | 1867028 | +430.4% |
| `sha-wasi` | 351971 | LLGo · full LTO (GlobalDCE off) | 2859487 | +712.4% |
| `sha-wasi` | 351971 | LLGo · full LTO + GlobalDCE | 1903106 | +440.7% |
| `word-count` | 164053 | LLGo · no LTO | 2002600 | +1120.7% |
| `word-count` | 164053 | LLGo · deadcode drop | 1121545 | +583.6% |
| `word-count` | 164053 | LLGo · full LTO (GlobalDCE off) | 1752909 | +968.5% |
| `word-count` | 164053 | LLGo · full LTO + GlobalDCE | 1129094 | +588.2% |
