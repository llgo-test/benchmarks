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
| LLGo · no LTO | 1.074x | 11 |
| LLGo · deadcode drop | — | 0 |
| LLGo · full LTO (GlobalDCE off) | 0.787x | 11 |
| LLGo · full LTO + GlobalDCE | 0.577x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1754437 | -22.9% |
| `base64` | 2275731 | LLGo · deadcode drop | — | — |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 1329535 | -41.6% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 940039 | -58.7% |
| `checksum` | 2264417 | LLGo · no LTO | 1732544 | -23.5% |
| `checksum` | 2264417 | LLGo · deadcode drop | — | — |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 1307374 | -42.3% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 911581 | -59.7% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 3061370 | +17.4% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | — | — |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 2531864 | -2.9% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 1637769 | -37.2% |
| `fibonacci` | 2230899 | LLGo · no LTO | 1429553 | -35.9% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | — | — |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 1142954 | -48.8% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 851340 | -61.8% |
| `grep` | 2848917 | LLGo · no LTO | 2583183 | -9.3% |
| `grep` | 2848917 | LLGo · deadcode drop | — | — |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 2063262 | -27.6% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 1556509 | -45.4% |
| `glob` | 2257634 | LLGo · no LTO | 2014025 | -10.8% |
| `glob` | 2257634 | LLGo · deadcode drop | — | — |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1590677 | -29.5% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 1153862 | -48.9% |
| `json-wasi` | 3314587 | LLGo · no LTO | 4569322 | +37.9% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | — | — |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 3705440 | +11.8% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 2610646 | -21.2% |
| `llimport` | 8423078 | LLGo · no LTO | 35192152 | +317.8% |
| `llimport` | 8423078 | LLGo · deadcode drop | — | — |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 11287502 | +34.0% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 10566732 | +25.4% |
| `path-report` | 2381190 | LLGo · no LTO | 2366682 | -0.6% |
| `path-report` | 2381190 | LLGo · deadcode drop | — | — |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1930985 | -18.9% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 1485257 | -37.6% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 3403623 | +22.4% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | — | — |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 2810672 | +1.1% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1915973 | -31.1% |
| `word-count` | 2253620 | LLGo · no LTO | 1973231 | -12.4% |
| `word-count` | 2253620 | LLGo · deadcode drop | — | — |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 1533238 | -32.0% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 1120036 | -50.3% |

## WASM binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 15.995x | 10 |
| LLGo · deadcode drop | — | 0 |
| LLGo · full LTO (GlobalDCE off) | 12.721x | 10 |
| LLGo · full LTO + GlobalDCE | 9.100x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1754437 | +1713.2% |
| `base64` | 96760 | LLGo · deadcode drop | — | — |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 1329535 | +1274.1% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 940039 | +871.5% |
| `checksum` | 92685 | LLGo · no LTO | 1732544 | +1769.3% |
| `checksum` | 92685 | LLGo · deadcode drop | — | — |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 1307374 | +1310.6% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 911581 | +883.5% |
| `conv-wasi` | 201149 | LLGo · no LTO | 3061370 | +1421.9% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | — | — |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 2531864 | +1158.7% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1637769 | +714.2% |
| `fibonacci` | 62386 | LLGo · no LTO | 1429553 | +2191.5% |
| `fibonacci` | 62386 | LLGo · deadcode drop | — | — |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 1142954 | +1732.1% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 851340 | +1264.6% |
| `grep` | 303772 | LLGo · no LTO | 2583183 | +750.4% |
| `grep` | 303772 | LLGo · deadcode drop | — | — |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 2063262 | +579.2% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 1556509 | +412.4% |
| `glob` | 93153 | LLGo · no LTO | 2014025 | +2062.1% |
| `glob` | 93153 | LLGo · deadcode drop | — | — |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1590677 | +1607.6% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 1153862 | +1138.7% |
| `json-wasi` | 493590 | LLGo · no LTO | 4569322 | +825.7% |
| `json-wasi` | 493590 | LLGo · deadcode drop | — | — |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 3705440 | +650.7% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 2610646 | +428.9% |
| `llimport` | — | LLGo · no LTO | 35192152 | — |
| `llimport` | — | LLGo · deadcode drop | — | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 11287502 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 10566732 | — |
| `path-report` | 116889 | LLGo · no LTO | 2366682 | +1924.7% |
| `path-report` | 116889 | LLGo · deadcode drop | — | — |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1930985 | +1552.0% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 1485257 | +1170.7% |
| `sha-wasi` | 287449 | LLGo · no LTO | 3403623 | +1084.1% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | — | — |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 2810672 | +877.8% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1915973 | +566.5% |
| `word-count` | 86834 | LLGo · no LTO | 1973231 | +2172.4% |
| `word-count` | 86834 | LLGo · deadcode drop | — | — |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 1533238 | +1665.7% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 1120036 | +1189.9% |
