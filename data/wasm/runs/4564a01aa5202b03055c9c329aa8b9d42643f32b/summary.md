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
Optional TinyGo failures are shown as —; logs are included in the CI artifact.

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
| LLGo · no LTO | 0.703x | 11 |
| LLGo · deadcode drop | 0.509x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.470x | 11 |
| LLGo · full LTO + GlobalDCE | 0.370x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1122784 | -50.7% |
| `base64` | 2275731 | LLGo · deadcode drop | 733689 | -67.8% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 784503 | -65.5% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 587977 | -74.2% |
| `checksum` | 2264417 | LLGo · no LTO | 1113327 | -50.8% |
| `checksum` | 2264417 | LLGo · deadcode drop | 723022 | -68.1% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 774025 | -65.8% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 575901 | -74.6% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 2181619 | -16.4% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 1505961 | -42.3% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1534914 | -41.1% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1075052 | -58.8% |
| `fibonacci` | 2230899 | LLGo · no LTO | 986521 | -55.8% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 682068 | -69.4% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 503253 | -77.4% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 473326 | -78.8% |
| `grep` | 2848917 | LLGo · no LTO | 1903319 | -33.2% |
| `grep` | 2848917 | LLGo · deadcode drop | 1428597 | -49.9% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1294473 | -54.6% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 1032677 | -63.8% |
| `glob` | 2257634 | LLGo · no LTO | 1531761 | -32.2% |
| `glob` | 2257634 | LLGo · deadcode drop | 1123660 | -50.2% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1001162 | -55.7% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 778437 | -65.5% |
| `json-wasi` | 3314587 | LLGo · no LTO | 3085186 | -6.9% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 2138813 | -35.5% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2210577 | -33.3% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1615529 | -51.3% |
| `llimport` | 8423078 | LLGo · no LTO | 10461998 | +24.2% |
| `llimport` | 8423078 | LLGo · deadcode drop | 9547568 | +13.4% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 7531629 | -10.6% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6919860 | -17.8% |
| `path-report` | 2381190 | LLGo · no LTO | 1812131 | -23.9% |
| `path-report` | 2381190 | LLGo · deadcode drop | 1399880 | -41.2% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1186066 | -50.2% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 958060 | -59.8% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 2434995 | -12.4% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1740729 | -37.4% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1720131 | -38.1% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1259689 | -54.7% |
| `word-count` | 2253620 | LLGo · no LTO | 1499572 | -33.5% |
| `word-count` | 2253620 | LLGo · deadcode drop | 1100063 | -51.2% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 960366 | -57.4% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 755076 | -66.5% |

## WASM binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.332x | 10 |
| LLGo · deadcode drop | 8.015x | 10 |
| LLGo · full LTO (GlobalDCE off) | 7.514x | 10 |
| LLGo · full LTO + GlobalDCE | 5.818x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1122784 | +1060.4% |
| `base64` | 96760 | LLGo · deadcode drop | 733689 | +658.3% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 784503 | +710.8% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 587977 | +507.7% |
| `checksum` | 92685 | LLGo · no LTO | 1113327 | +1101.2% |
| `checksum` | 92685 | LLGo · deadcode drop | 723022 | +680.1% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 774025 | +735.1% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 575901 | +521.4% |
| `conv-wasi` | 201149 | LLGo · no LTO | 2181619 | +984.6% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 1505961 | +648.7% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1534914 | +663.1% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1075052 | +434.5% |
| `fibonacci` | 62386 | LLGo · no LTO | 986521 | +1481.3% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 682068 | +993.3% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 503253 | +706.7% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 473326 | +658.7% |
| `grep` | 303772 | LLGo · no LTO | 1903319 | +526.6% |
| `grep` | 303772 | LLGo · deadcode drop | 1428597 | +370.3% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1294473 | +326.1% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 1032677 | +240.0% |
| `glob` | 93153 | LLGo · no LTO | 1531761 | +1544.3% |
| `glob` | 93153 | LLGo · deadcode drop | 1123660 | +1106.3% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1001162 | +974.8% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 778437 | +735.7% |
| `json-wasi` | 493590 | LLGo · no LTO | 3085186 | +525.1% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 2138813 | +333.3% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2210577 | +347.9% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1615529 | +227.3% |
| `llimport` | — | LLGo · no LTO | 10461998 | — |
| `llimport` | — | LLGo · deadcode drop | 9547568 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 7531629 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6919860 | — |
| `path-report` | 116889 | LLGo · no LTO | 1812131 | +1450.3% |
| `path-report` | 116889 | LLGo · deadcode drop | 1399880 | +1097.6% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1186066 | +914.7% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 958060 | +719.6% |
| `sha-wasi` | 287449 | LLGo · no LTO | 2434995 | +747.1% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1740729 | +505.6% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1720131 | +498.4% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1259689 | +338.2% |
| `word-count` | 86834 | LLGo · no LTO | 1499572 | +1626.9% |
| `word-count` | 86834 | LLGo · deadcode drop | 1100063 | +1166.9% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 960366 | +1006.0% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 755076 | +769.6% |
