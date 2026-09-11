# WASM binary size

`wasip1/wasm`; smaller is better.
All application builds use the same pinned Go toolchain.

- Go: `build -trimpath '-ldflags=-s -w'`
- TinyGo: `build -opt=z -no-debug`
- LLGo · no LTO: `build -a -Oz`
- LLGo · deadcode drop: `build -a -Oz -deadcodedrop`
- LLGo · full LTO (GlobalDCE off): `CCFLAGS='-flto=full' LDFLAGS='-Wl,--lto-O2' build -a -Oz -lto=full -globaldce=false`
- LLGo · full LTO + GlobalDCE: `CCFLAGS='-flto=full -fvirtual-function-elimination -fwhole-program-vtables' LDFLAGS='-Wl,--lto-O2' build -a -Oz -lto=full -globaldce=true`

LLGo uses Emscripten wasm-opt for Asyncify and exception translation;
TinyGo uses its separately pinned Binaryen release.
Optional TinyGo failures are shown as —; logs are included in the CI artifact.

## WASM binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 0.658x | 10 |
| LLGo · deadcode drop | 0.469x | 10 |
| LLGo · full LTO (GlobalDCE off) | 0.437x | 10 |
| LLGo · full LTO + GlobalDCE | 0.342x | 10 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1120973 | -50.7% |
| `base64` | 2275731 | LLGo · deadcode drop | 744537 | -67.3% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 782276 | -65.6% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 596297 | -73.8% |
| `checksum` | 2264417 | LLGo · no LTO | 1098650 | -51.5% |
| `checksum` | 2264417 | LLGo · deadcode drop | 720721 | -68.2% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 766733 | -66.1% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 577229 | -74.5% |
| `conv-wasi` | 2608055 | LLGo · no LTO | 2147194 | -17.7% |
| `conv-wasi` | 2608055 | LLGo · deadcode drop | 1491184 | -42.8% |
| `conv-wasi` | 2608055 | LLGo · full LTO (GlobalDCE off) | 1518230 | -41.8% |
| `conv-wasi` | 2608055 | LLGo · full LTO + GlobalDCE | 1069497 | -59.0% |
| `fibonacci` | 2230980 | LLGo · no LTO | 976098 | -56.2% |
| `fibonacci` | 2230980 | LLGo · deadcode drop | 680003 | -69.5% |
| `fibonacci` | 2230980 | LLGo · full LTO (GlobalDCE off) | 499202 | -77.6% |
| `fibonacci` | 2230980 | LLGo · full LTO + GlobalDCE | 474570 | -78.7% |
| `grep` | 2848917 | LLGo · no LTO | 1887234 | -33.8% |
| `grep` | 2848917 | LLGo · deadcode drop | 1425676 | -50.0% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1285643 | -54.9% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 1033734 | -63.7% |
| `glob` | 2257634 | LLGo · no LTO | 1516226 | -32.8% |
| `glob` | 2257634 | LLGo · deadcode drop | 1121124 | -50.3% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 992478 | -56.0% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 779639 | -65.5% |
| `json-wasi` | 3314554 | LLGo · no LTO | 3046152 | -8.1% |
| `json-wasi` | 3314554 | LLGo · deadcode drop | 2126748 | -35.8% |
| `json-wasi` | 3314554 | LLGo · full LTO (GlobalDCE off) | 2184586 | -34.1% |
| `json-wasi` | 3314554 | LLGo · full LTO + GlobalDCE | 1609178 | -51.5% |
| `path-report` | 2381190 | LLGo · no LTO | 1796861 | -24.5% |
| `path-report` | 2381190 | LLGo · deadcode drop | 1397655 | -41.3% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1177742 | -50.5% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 959554 | -59.7% |
| `sha-wasi` | 2780938 | LLGo · no LTO | 2411124 | -13.3% |
| `sha-wasi` | 2780938 | LLGo · deadcode drop | 1736847 | -37.5% |
| `sha-wasi` | 2780938 | LLGo · full LTO (GlobalDCE off) | 1704091 | -38.7% |
| `sha-wasi` | 2780938 | LLGo · full LTO + GlobalDCE | 1258745 | -54.7% |
| `word-count` | 2253620 | LLGo · no LTO | 1483899 | -34.2% |
| `word-count` | 2253620 | LLGo · deadcode drop | 1097516 | -51.3% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 952427 | -57.7% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 755860 | -66.5% |

## WASM binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.217x | 10 |
| LLGo · deadcode drop | 8.001x | 10 |
| LLGo · full LTO (GlobalDCE off) | 7.452x | 10 |
| LLGo · full LTO + GlobalDCE | 5.827x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1120973 | +1058.5% |
| `base64` | 96760 | LLGo · deadcode drop | 744537 | +669.5% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 782276 | +708.5% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 596297 | +516.3% |
| `checksum` | 92685 | LLGo · no LTO | 1098650 | +1085.4% |
| `checksum` | 92685 | LLGo · deadcode drop | 720721 | +677.6% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 766733 | +727.2% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 577229 | +522.8% |
| `conv-wasi` | 201149 | LLGo · no LTO | 2147194 | +967.5% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 1491184 | +641.3% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1518230 | +654.8% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1069497 | +431.7% |
| `fibonacci` | 62386 | LLGo · no LTO | 976098 | +1464.6% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 680003 | +990.0% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 499202 | +700.2% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 474570 | +660.7% |
| `grep` | 303772 | LLGo · no LTO | 1887234 | +521.3% |
| `grep` | 303772 | LLGo · deadcode drop | 1425676 | +369.3% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1285643 | +323.2% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 1033734 | +240.3% |
| `glob` | 93153 | LLGo · no LTO | 1516226 | +1527.7% |
| `glob` | 93153 | LLGo · deadcode drop | 1121124 | +1103.5% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 992478 | +965.4% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 779639 | +736.9% |
| `json-wasi` | 493590 | LLGo · no LTO | 3046152 | +517.1% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 2126748 | +330.9% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2184586 | +342.6% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1609178 | +226.0% |
| `path-report` | 116889 | LLGo · no LTO | 1796861 | +1437.2% |
| `path-report` | 116889 | LLGo · deadcode drop | 1397655 | +1095.7% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1177742 | +907.6% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 959554 | +720.9% |
| `sha-wasi` | 287449 | LLGo · no LTO | 2411124 | +738.8% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1736847 | +504.2% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1704091 | +492.8% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1258745 | +337.9% |
| `word-count` | 86834 | LLGo · no LTO | 1483899 | +1608.9% |
| `word-count` | 86834 | LLGo · deadcode drop | 1097516 | +1163.9% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 952427 | +996.8% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 755860 | +770.5% |
