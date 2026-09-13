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
| LLGo · no LTO | 0.702x | 11 |
| LLGo · deadcode drop | 0.508x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.469x | 11 |
| LLGo · full LTO + GlobalDCE | 0.369x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1122086 | -50.7% |
| `base64` | 2275731 | LLGo · deadcode drop | 733005 | -67.8% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 784252 | -65.5% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 587742 | -74.2% |
| `checksum` | 2264417 | LLGo · no LTO | 1112627 | -50.9% |
| `checksum` | 2264417 | LLGo · deadcode drop | 722332 | -68.1% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 773768 | -65.8% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 575658 | -74.6% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 2177367 | -16.5% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 1504048 | -42.3% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1533273 | -41.2% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1074264 | -58.8% |
| `fibonacci` | 2230899 | LLGo · no LTO | 985822 | -55.8% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 681385 | -69.5% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 503006 | -77.5% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 473079 | -78.8% |
| `grep` | 2848917 | LLGo · no LTO | 1902113 | -33.2% |
| `grep` | 2848917 | LLGo · deadcode drop | 1427405 | -49.9% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1293894 | -54.6% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 1032108 | -63.8% |
| `glob` | 2257634 | LLGo · no LTO | 1531061 | -32.2% |
| `glob` | 2257634 | LLGo · deadcode drop | 1122978 | -50.3% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1000915 | -55.7% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 778184 | -65.5% |
| `json-wasi` | 3314587 | LLGo · no LTO | 3077608 | -7.1% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 2133556 | -35.6% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2207931 | -33.4% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1613621 | -51.3% |
| `llimport` | 8423078 | LLGo · no LTO | 10346885 | +22.8% |
| `llimport` | 8423078 | LLGo · deadcode drop | 9435747 | +12.0% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 7438249 | -11.7% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6828751 | -18.9% |
| `path-report` | 2381190 | LLGo · no LTO | 1811409 | -23.9% |
| `path-report` | 2381190 | LLGo · deadcode drop | 1399177 | -41.2% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1185646 | -50.2% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 957661 | -59.8% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 2430742 | -12.6% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1738813 | -37.5% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1718468 | -38.2% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1258903 | -54.7% |
| `word-count` | 2253620 | LLGo · no LTO | 1498874 | -33.5% |
| `word-count` | 2253620 | LLGo · deadcode drop | 1099378 | -51.2% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 960113 | -57.4% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 754835 | -66.5% |

## WASM binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.320x | 10 |
| LLGo · deadcode drop | 8.006x | 10 |
| LLGo · full LTO (GlobalDCE off) | 7.510x | 10 |
| LLGo · full LTO + GlobalDCE | 5.815x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1122086 | +1059.7% |
| `base64` | 96760 | LLGo · deadcode drop | 733005 | +657.5% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 784252 | +710.5% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 587742 | +507.4% |
| `checksum` | 92685 | LLGo · no LTO | 1112627 | +1100.4% |
| `checksum` | 92685 | LLGo · deadcode drop | 722332 | +679.3% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 773768 | +734.8% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 575658 | +521.1% |
| `conv-wasi` | 201149 | LLGo · no LTO | 2177367 | +982.5% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 1504048 | +647.7% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1533273 | +662.3% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1074264 | +434.1% |
| `fibonacci` | 62386 | LLGo · no LTO | 985822 | +1480.2% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 681385 | +992.2% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 503006 | +706.3% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 473079 | +658.3% |
| `grep` | 303772 | LLGo · no LTO | 1902113 | +526.2% |
| `grep` | 303772 | LLGo · deadcode drop | 1427405 | +369.9% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1293894 | +325.9% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 1032108 | +239.8% |
| `glob` | 93153 | LLGo · no LTO | 1531061 | +1543.6% |
| `glob` | 93153 | LLGo · deadcode drop | 1122978 | +1105.5% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1000915 | +974.5% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 778184 | +735.4% |
| `json-wasi` | 493590 | LLGo · no LTO | 3077608 | +523.5% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 2133556 | +332.3% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2207931 | +347.3% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1613621 | +226.9% |
| `llimport` | — | LLGo · no LTO | 10346885 | — |
| `llimport` | — | LLGo · deadcode drop | 9435747 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 7438249 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6828751 | — |
| `path-report` | 116889 | LLGo · no LTO | 1811409 | +1449.7% |
| `path-report` | 116889 | LLGo · deadcode drop | 1399177 | +1097.0% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1185646 | +914.3% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 957661 | +719.3% |
| `sha-wasi` | 287449 | LLGo · no LTO | 2430742 | +745.6% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1738813 | +504.9% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1718468 | +497.8% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1258903 | +338.0% |
| `word-count` | 86834 | LLGo · no LTO | 1498874 | +1626.1% |
| `word-count` | 86834 | LLGo · deadcode drop | 1099378 | +1166.1% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 960113 | +1005.7% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 754835 | +769.3% |
