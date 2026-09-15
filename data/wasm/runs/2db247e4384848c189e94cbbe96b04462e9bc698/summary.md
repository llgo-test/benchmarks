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
| LLGo · no LTO | 0.658x | 11 |
| LLGo · deadcode drop | 0.465x | 11 |
| LLGo · full LTO (GlobalDCE off) | 0.450x | 11 |
| LLGo · full LTO + GlobalDCE | 0.349x | 11 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1120806 | -50.7% |
| `base64` | 2275731 | LLGo · deadcode drop | 731885 | -67.8% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 781994 | -65.6% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 585648 | -74.3% |
| `checksum` | 2264417 | LLGo · no LTO | 1111358 | -50.9% |
| `checksum` | 2264417 | LLGo · deadcode drop | 721217 | -68.1% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 771520 | -65.9% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 573570 | -74.7% |
| `conv-wasi` | 2608089 | LLGo · no LTO | 1998260 | -23.4% |
| `conv-wasi` | 2608089 | LLGo · deadcode drop | 1322712 | -49.3% |
| `conv-wasi` | 2608089 | LLGo · full LTO (GlobalDCE off) | 1457656 | -44.1% |
| `conv-wasi` | 2608089 | LLGo · full LTO + GlobalDCE | 999254 | -61.7% |
| `fibonacci` | 2230899 | LLGo · no LTO | 984530 | -55.9% |
| `fibonacci` | 2230899 | LLGo · deadcode drop | 680255 | -69.5% |
| `fibonacci` | 2230899 | LLGo · full LTO (GlobalDCE off) | 500974 | -77.5% |
| `fibonacci` | 2230899 | LLGo · full LTO + GlobalDCE | 471033 | -78.9% |
| `grep` | 2848917 | LLGo · no LTO | 1716944 | -39.7% |
| `grep` | 2848917 | LLGo · deadcode drop | 1242390 | -56.4% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1215452 | -57.3% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 953798 | -66.5% |
| `glob` | 2257634 | LLGo · no LTO | 1347780 | -40.3% |
| `glob` | 2257634 | LLGo · deadcode drop | 939850 | -58.4% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 923241 | -59.1% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 700680 | -69.0% |
| `json-wasi` | 3314587 | LLGo · no LTO | 2902295 | -12.4% |
| `json-wasi` | 3314587 | LLGo · deadcode drop | 1956559 | -41.0% |
| `json-wasi` | 3314587 | LLGo · full LTO (GlobalDCE off) | 2133177 | -35.6% |
| `json-wasi` | 3314587 | LLGo · full LTO + GlobalDCE | 1540184 | -53.5% |
| `llimport` | 8423078 | LLGo · no LTO | 10249152 | +21.7% |
| `llimport` | 8423078 | LLGo · deadcode drop | 9335674 | +10.8% |
| `llimport` | 8423078 | LLGo · full LTO (GlobalDCE off) | 7315958 | -13.1% |
| `llimport` | 8423078 | LLGo · full LTO + GlobalDCE | 6704015 | -20.4% |
| `path-report` | 2381190 | LLGo · no LTO | 1621421 | -31.9% |
| `path-report` | 2381190 | LLGo · deadcode drop | 1208034 | -49.3% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1101565 | -53.7% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 873461 | -63.3% |
| `sha-wasi` | 2780972 | LLGo · no LTO | 2251619 | -19.0% |
| `sha-wasi` | 2780972 | LLGo · deadcode drop | 1557467 | -44.0% |
| `sha-wasi` | 2780972 | LLGo · full LTO (GlobalDCE off) | 1641495 | -41.0% |
| `sha-wasi` | 2780972 | LLGo · full LTO + GlobalDCE | 1182503 | -57.5% |
| `word-count` | 2253620 | LLGo · no LTO | 1315605 | -41.6% |
| `word-count` | 2253620 | LLGo · deadcode drop | 916261 | -59.3% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 882440 | -60.8% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 677319 | -69.9% |

## WASM binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 10.560x | 10 |
| LLGo · deadcode drop | 7.262x | 10 |
| LLGo · full LTO (GlobalDCE off) | 7.186x | 10 |
| LLGo · full LTO + GlobalDCE | 5.489x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1120806 | +1058.3% |
| `base64` | 96760 | LLGo · deadcode drop | 731885 | +656.4% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 781994 | +708.2% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 585648 | +505.3% |
| `checksum` | 92685 | LLGo · no LTO | 1111358 | +1099.1% |
| `checksum` | 92685 | LLGo · deadcode drop | 721217 | +678.1% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 771520 | +732.4% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 573570 | +518.8% |
| `conv-wasi` | 201149 | LLGo · no LTO | 1998260 | +893.4% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 1322712 | +557.6% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1457656 | +624.7% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 999254 | +396.8% |
| `fibonacci` | 62386 | LLGo · no LTO | 984530 | +1478.1% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 680255 | +990.4% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 500974 | +703.0% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 471033 | +655.0% |
| `grep` | 303772 | LLGo · no LTO | 1716944 | +465.2% |
| `grep` | 303772 | LLGo · deadcode drop | 1242390 | +309.0% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1215452 | +300.1% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 953798 | +214.0% |
| `glob` | 93153 | LLGo · no LTO | 1347780 | +1346.8% |
| `glob` | 93153 | LLGo · deadcode drop | 939850 | +908.9% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 923241 | +891.1% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 700680 | +652.2% |
| `json-wasi` | 493590 | LLGo · no LTO | 2902295 | +488.0% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 1956559 | +296.4% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2133177 | +332.2% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1540184 | +212.0% |
| `llimport` | — | LLGo · no LTO | 10249152 | — |
| `llimport` | — | LLGo · deadcode drop | 9335674 | — |
| `llimport` | — | LLGo · full LTO (GlobalDCE off) | 7315958 | — |
| `llimport` | — | LLGo · full LTO + GlobalDCE | 6704015 | — |
| `path-report` | 116889 | LLGo · no LTO | 1621421 | +1287.1% |
| `path-report` | 116889 | LLGo · deadcode drop | 1208034 | +933.5% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1101565 | +842.4% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 873461 | +647.3% |
| `sha-wasi` | 287449 | LLGo · no LTO | 2251619 | +683.3% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1557467 | +441.8% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1641495 | +471.1% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1182503 | +311.4% |
| `word-count` | 86834 | LLGo · no LTO | 1315605 | +1415.1% |
| `word-count` | 86834 | LLGo · deadcode drop | 916261 | +955.2% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 882440 | +916.2% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 677319 | +680.0% |
