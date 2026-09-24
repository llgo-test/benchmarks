# WASM binary size

`wasip1/wasm`; smaller is better.
Each application uses the same pinned Go toolchain across compilers; per-application versions are recorded below.

- Go: `build -trimpath '-ldflags=-s -w'`
- TinyGo: `build -opt=z -no-debug`
- LLGo · no LTO: `build -a -Oz`
- LLGo · deadcode drop: `build -a -Oz -deadcodedrop`
- LLGo · full LTO (GlobalDCE off): `CCFLAGS='-flto=full' LDFLAGS='-Wl,--lto-O2' build -a -Oz -lto=full -globaldce=false`
- LLGo · full LTO + GlobalDCE: `CCFLAGS='-flto=full -fvirtual-function-elimination -fwhole-program-vtables' LDFLAGS='-Wl,--lto-O2' build -a -Oz -lto=full -globaldce=true`

LLGo uses Emscripten wasm-opt for Asyncify and exception translation;
TinyGo uses its separately pinned Binaryen release.
Failed builds are shown as — and excluded from comparisons; logs are included in the CI artifact.

## Failed builds

| Application | Configuration | Policy | Log |
| --- | --- | --- | --- |
| llimport | TinyGo | optional | [logs/llimport.TinyGo.log](logs/llimport.TinyGo.log) |

| Application | Go toolchain | Source repository | Commit | Entry |
| --- | --- | --- | --- | --- |
| base64 | 1.26.2 | - | - | base64 |
| checksum | 1.26.2 | - | - | checksum |
| convolution | 1.26.2 | https://github.com/universonic/go-rust-wasm-bench.git | 6d1b98c971d6206c313a6d1233d9f2687c50febe | go/cmd/conv-wasi |
| fibonacci | 1.26.2 | https://github.com/mattn/wasi-benchmark.git | c7d73b7b1e03b352791f91ed207c6b9c79559453 | main.go |
| grep | 1.26.2 | - | - | grep |
| glob | 1.26.2 | - | - | glob |
| json-roundtrip | 1.26.2 | https://github.com/universonic/go-rust-wasm-bench.git | 6d1b98c971d6206c313a6d1233d9f2687c50febe | go/cmd/json-wasi |
| llimport | 1.27.0 | https://github.com/goplus/llcppg.git | d62a300b00d567ce2737ab085cef18c06d43f7d7 | cmd/llimport |
| path-report | 1.26.2 | - | - | path-report |
| sha256 | 1.26.2 | https://github.com/universonic/go-rust-wasm-bench.git | 6d1b98c971d6206c313a6d1233d9f2687c50febe | go/cmd/sha-wasi |
| word-count | 1.26.2 | - | - | word-count |

## WASM binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.911x | 11 |
| LLGo · deadcode drop | 0.586x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.731x | 11 |
| LLGo · full LTO + GlobalDCE | 0.523x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1668145 | -26.7% |
| `base64` | 2275731 | LLGo · deadcode drop | 1007570 | -55.7% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 1303233 | -42.7% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 909205 | -60.0% |
| `checksum` | 2264417 | LLGo · no LTO | 1645034 | -27.4% |
| `checksum` | 2264417 | LLGo · deadcode drop | 979858 | -56.7% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 1273456 | -43.8% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 876603 | -61.3% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 2796598 | +7.2% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 1629691 | -37.5% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 2347878 | -10.0% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1469538 | -43.7% |
| `fibonacci` | 2230899 | LLGo · no LTO | 1378827 | -38.2% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 904882 | -59.4% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 1108569 | -50.3% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 816078 | -63.4% |
| `grep` | 2848917 | LLGo · no LTO | 2370153 | -16.8% |
| `grep` | 2848917 | LLGo · deadcode drop | 1578268 | -44.6% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1922330 | -32.5% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 1413511 | -50.4% |
| `glob` | 2257634 | LLGo · no LTO | 1836136 | -18.7% |
| `glob` | 2257634 | LLGo · deadcode drop | 1138409 | -49.6% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1465429 | -35.1% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 1028492 | -54.4% |
| `json-wasi` | 3314587 | LLGo · no LTO | 4104101 | +23.8% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 2486420 | -25.0% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 3466633 | +4.6% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 2364558 | -28.7% |
| `llimport` | 8423078 | LLGo · no LTO | 12431404 | +47.6% |
| `llimport` | 8423078 | LLGo · deadcode drop | 10958162 | +30.1% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 8968165 | +6.5% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 8265036 | -1.9% |
| `path-report` | 2381190 | LLGo · no LTO | 2176386 | -8.6% |
| `path-report` | 2381190 | LLGo · deadcode drop | 1469642 | -38.3% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1791750 | -24.8% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 1345795 | -43.5% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 3131980 | +12.6% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1934513 | -30.4% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 2658242 | -4.4% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1764900 | -36.5% |
| `word-count` | 2253620 | LLGo · no LTO | 1796505 | -20.3% |
| `word-count` | 2253620 | LLGo · deadcode drop | 1111805 | -50.7% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 1409742 | -37.4% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 995872 | -55.8% |

## WASM binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 14.801x | 10 |
| LLGo · deadcode drop | 9.229x | 10 |
| LLGo · full LTO (GlobalDCE off) | 11.997x | 10 |
| LLGo · full LTO + GlobalDCE | 8.374x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1668145 | +1624.0% |
| `base64` | 96760 | LLGo · deadcode drop | 1007570 | +941.3% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 1303233 | +1246.9% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 909205 | +839.6% |
| `checksum` | 92685 | LLGo · no LTO | 1645034 | +1674.9% |
| `checksum` | 92685 | LLGo · deadcode drop | 979858 | +957.2% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 1273456 | +1274.0% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 876603 | +845.8% |
| `conv-wasi` | 201149 | LLGo · no LTO | 2796598 | +1290.3% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 1629691 | +710.2% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 2347878 | +1067.2% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1469538 | +630.6% |
| `fibonacci` | 62386 | LLGo · no LTO | 1378827 | +2110.2% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 904882 | +1350.5% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 1108569 | +1677.0% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 816078 | +1208.1% |
| `grep` | 303772 | LLGo · no LTO | 2370153 | +680.2% |
| `grep` | 303772 | LLGo · deadcode drop | 1578268 | +419.6% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1922330 | +532.8% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 1413511 | +365.3% |
| `glob` | 93153 | LLGo · no LTO | 1836136 | +1871.1% |
| `glob` | 93153 | LLGo · deadcode drop | 1138409 | +1122.1% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1465429 | +1473.1% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 1028492 | +1004.1% |
| `json-wasi` | 493590 | LLGo · no LTO | 4104101 | +731.5% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 2486420 | +403.7% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 3466633 | +602.3% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 2364558 | +379.1% |
| `llimport` | — | LLGo · no LTO | 12431404 | — |
| `llimport` | — | LLGo · deadcode drop | 10958162 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 8968165 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 8265036 | — |
| `path-report` | 116889 | LLGo · no LTO | 2176386 | +1761.9% |
| `path-report` | 116889 | LLGo · deadcode drop | 1469642 | +1157.3% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1791750 | +1432.9% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 1345795 | +1051.3% |
| `sha-wasi` | 287449 | LLGo · no LTO | 3131980 | +989.6% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1934513 | +573.0% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 2658242 | +824.8% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1764900 | +514.0% |
| `word-count` | 86834 | LLGo · no LTO | 1796505 | +1968.9% |
| `word-count` | 86834 | LLGo · deadcode drop | 1111805 | +1180.4% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 1409742 | +1523.5% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 995872 | +1046.9% |
