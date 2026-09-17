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
| base64 | LLGoDeadcodeDrop | required | [logs/base64.LLGoDeadcodeDrop.log](logs/base64.LLGoDeadcodeDrop.log) |
| checksum | LLGoDeadcodeDrop | required | [logs/checksum.LLGoDeadcodeDrop.log](logs/checksum.LLGoDeadcodeDrop.log) |
| convolution | LLGoDeadcodeDrop | required | [logs/convolution.LLGoDeadcodeDrop.log](logs/convolution.LLGoDeadcodeDrop.log) |
| fibonacci | LLGoDeadcodeDrop | required | [logs/fibonacci.LLGoDeadcodeDrop.log](logs/fibonacci.LLGoDeadcodeDrop.log) |
| grep | LLGoDeadcodeDrop | required | [logs/grep.LLGoDeadcodeDrop.log](logs/grep.LLGoDeadcodeDrop.log) |
| glob | LLGoDeadcodeDrop | required | [logs/glob.LLGoDeadcodeDrop.log](logs/glob.LLGoDeadcodeDrop.log) |
| json-roundtrip | LLGoDeadcodeDrop | required | [logs/json-roundtrip.LLGoDeadcodeDrop.log](logs/json-roundtrip.LLGoDeadcodeDrop.log) |
| llimport | TinyGo | optional | [logs/llimport.TinyGo.log](logs/llimport.TinyGo.log) |
| llimport | LLGoDeadcodeDrop | required | [logs/llimport.LLGoDeadcodeDrop.log](logs/llimport.LLGoDeadcodeDrop.log) |
| path-report | LLGoDeadcodeDrop | required | [logs/path-report.LLGoDeadcodeDrop.log](logs/path-report.LLGoDeadcodeDrop.log) |
| sha256 | LLGoDeadcodeDrop | required | [logs/sha256.LLGoDeadcodeDrop.log](logs/sha256.LLGoDeadcodeDrop.log) |
| word-count | LLGoDeadcodeDrop | required | [logs/word-count.LLGoDeadcodeDrop.log](logs/word-count.LLGoDeadcodeDrop.log) |

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
| LLGo · no LTO | 1.073x | 11 |
| LLGo · deadcode drop | — | 0 |
| LLGo · full LTO (GlobalDCE off) | 0.786x | 11 |
| LLGo · full LTO + GlobalDCE | 0.577x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1754176 | -22.9% |
| `base64` | 2275731 | LLGo · deadcode drop | — | — |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 1329279 | -41.6% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 939793 | -58.7% |
| `checksum` | 2264417 | LLGo · no LTO | 1732281 | -23.5% |
| `checksum` | 2264417 | LLGo · deadcode drop | — | — |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 1307085 | -42.3% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 911307 | -59.8% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 3042069 | +16.6% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | — | — |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 2527006 | -3.1% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1641465 | -37.1% |
| `fibonacci` | 2230899 | LLGo · no LTO | 1429326 | -35.9% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | — | — |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 1142711 | -48.8% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 851088 | -61.8% |
| `grep` | 2848917 | LLGo · no LTO | 2582908 | -9.3% |
| `grep` | 2848917 | LLGo · deadcode drop | — | — |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 2062959 | -27.6% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 1556218 | -45.4% |
| `glob` | 2257634 | LLGo · no LTO | 2013777 | -10.8% |
| `glob` | 2257634 | LLGo · deadcode drop | — | — |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1590410 | -29.6% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 1153635 | -48.9% |
| `json-wasi` | 3314587 | LLGo · no LTO | 4548364 | +37.2% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | — | — |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 3698831 | +11.6% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 2613227 | -21.2% |
| `llimport` | 8423078 | LLGo · no LTO | 35205474 | +318.0% |
| `llimport` | 8423078 | LLGo · deadcode drop | — | — |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 11290697 | +34.0% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 10570282 | +25.5% |
| `path-report` | 2381190 | LLGo · no LTO | 2366448 | -0.6% |
| `path-report` | 2381190 | LLGo · deadcode drop | — | — |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1930714 | -18.9% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 1484984 | -37.6% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 3384307 | +21.7% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | — | — |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 2805486 | +0.9% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1919402 | -31.0% |
| `word-count` | 2253620 | LLGo · no LTO | 1972982 | -12.5% |
| `word-count` | 2253620 | LLGo · deadcode drop | — | — |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 1532977 | -32.0% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 1119783 | -50.3% |

## WASM binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 15.967x | 10 |
| LLGo · deadcode drop | — | 0 |
| LLGo · full LTO (GlobalDCE off) | 12.713x | 10 |
| LLGo · full LTO + GlobalDCE | 9.103x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1754176 | +1712.9% |
| `base64` | 96760 | LLGo · deadcode drop | — | — |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 1329279 | +1273.8% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 939793 | +871.3% |
| `checksum` | 92685 | LLGo · no LTO | 1732281 | +1769.0% |
| `checksum` | 92685 | LLGo · deadcode drop | — | — |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 1307085 | +1310.2% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 911307 | +883.2% |
| `conv-wasi` | 201149 | LLGo · no LTO | 3042069 | +1412.3% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | — | — |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 2527006 | +1156.3% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1641465 | +716.0% |
| `fibonacci` | 62386 | LLGo · no LTO | 1429326 | +2191.1% |
| `fibonacci` | 62386 | LLGo · deadcode drop | — | — |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 1142711 | +1731.7% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 851088 | +1264.2% |
| `grep` | 303772 | LLGo · no LTO | 2582908 | +750.3% |
| `grep` | 303772 | LLGo · deadcode drop | — | — |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 2062959 | +579.1% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 1556218 | +412.3% |
| `glob` | 93153 | LLGo · no LTO | 2013777 | +2061.8% |
| `glob` | 93153 | LLGo · deadcode drop | — | — |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1590410 | +1607.3% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 1153635 | +1138.4% |
| `json-wasi` | 493590 | LLGo · no LTO | 4548364 | +821.5% |
| `json-wasi` | 493590 | LLGo · deadcode drop | — | — |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 3698831 | +649.4% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 2613227 | +429.4% |
| `llimport` | — | LLGo · no LTO | 35205474 | — |
| `llimport` | — | LLGo · deadcode drop | — | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 11290697 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 10570282 | — |
| `path-report` | 116889 | LLGo · no LTO | 2366448 | +1924.5% |
| `path-report` | 116889 | LLGo · deadcode drop | — | — |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1930714 | +1551.7% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 1484984 | +1170.4% |
| `sha-wasi` | 287449 | LLGo · no LTO | 3384307 | +1077.4% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | — | — |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 2805486 | +876.0% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1919402 | +567.7% |
| `word-count` | 86834 | LLGo · no LTO | 1972982 | +2172.1% |
| `word-count` | 86834 | LLGo · deadcode drop | — | — |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 1532977 | +1665.4% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 1119783 | +1189.6% |
