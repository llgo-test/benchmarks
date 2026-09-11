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
| LLGo · no LTO | 0.664x | 10 |
| LLGo · deadcode drop | 0.470x | 10 |
| LLGo · full LTO (GlobalDCE off) | 0.440x | 10 |
| LLGo · full LTO + GlobalDCE | 0.341x | 10 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `base64` | 2275731 | LLGo · no LTO | 1122588 | -50.7% |
| `base64` | 2275731 | LLGo · deadcode drop | 733382 | -67.8% |
| `base64` | 2275731 | LLGo · full LTO (GlobalDCE off) | 784224 | -65.5% |
| `base64` | 2275731 | LLGo · full LTO + GlobalDCE | 587841 | -74.2% |
| `checksum` | 2264417 | LLGo · no LTO | 1113118 | -50.8% |
| `checksum` | 2264417 | LLGo · deadcode drop | 722821 | -68.1% |
| `checksum` | 2264417 | LLGo · full LTO (GlobalDCE off) | 773733 | -65.8% |
| `checksum` | 2264417 | LLGo · full LTO + GlobalDCE | 575765 | -74.6% |
| `conv-wasi` | 2608055 | LLGo · no LTO | 2178231 | -16.5% |
| `conv-wasi` | 2608055 | LLGo · deadcode drop | 1504694 | -42.3% |
| `conv-wasi` | 2608055 | LLGo · full LTO (GlobalDCE off) | 1533636 | -41.2% |
| `conv-wasi` | 2608055 | LLGo · full LTO + GlobalDCE | 1074391 | -58.8% |
| `fibonacci` | 2230980 | LLGo · no LTO | 986224 | -55.8% |
| `fibonacci` | 2230980 | LLGo · deadcode drop | 681793 | -69.4% |
| `fibonacci` | 2230980 | LLGo · full LTO (GlobalDCE off) | 502888 | -77.5% |
| `fibonacci` | 2230980 | LLGo · full LTO + GlobalDCE | 473117 | -78.8% |
| `grep` | 2848917 | LLGo · no LTO | 1902618 | -33.2% |
| `grep` | 2848917 | LLGo · deadcode drop | 1427912 | -49.9% |
| `grep` | 2848917 | LLGo · full LTO (GlobalDCE off) | 1293915 | -54.6% |
| `grep` | 2848917 | LLGo · full LTO + GlobalDCE | 1032119 | -63.8% |
| `glob` | 2257634 | LLGo · no LTO | 1531562 | -32.2% |
| `glob` | 2257634 | LLGo · deadcode drop | 1123458 | -50.2% |
| `glob` | 2257634 | LLGo · full LTO (GlobalDCE off) | 1000935 | -55.7% |
| `glob` | 2257634 | LLGo · full LTO + GlobalDCE | 778219 | -65.5% |
| `json-wasi` | 3314554 | LLGo · no LTO | 3078248 | -7.1% |
| `json-wasi` | 3314554 | LLGo · deadcode drop | 2134184 | -35.6% |
| `json-wasi` | 3314554 | LLGo · full LTO (GlobalDCE off) | 2208023 | -33.4% |
| `json-wasi` | 3314554 | LLGo · full LTO + GlobalDCE | 1613730 | -51.3% |
| `path-report` | 2381190 | LLGo · no LTO | 1811908 | -23.9% |
| `path-report` | 2381190 | LLGo · deadcode drop | 1399675 | -41.2% |
| `path-report` | 2381190 | LLGo · full LTO (GlobalDCE off) | 1185674 | -50.2% |
| `path-report` | 2381190 | LLGo · full LTO + GlobalDCE | 957684 | -59.8% |
| `sha-wasi` | 2780938 | LLGo · no LTO | 2431609 | -12.6% |
| `sha-wasi` | 2780938 | LLGo · deadcode drop | 1739588 | -37.4% |
| `sha-wasi` | 2780938 | LLGo · full LTO (GlobalDCE off) | 1718743 | -38.2% |
| `sha-wasi` | 2780938 | LLGo · full LTO + GlobalDCE | 1258950 | -54.7% |
| `word-count` | 2253620 | LLGo · no LTO | 1499362 | -33.5% |
| `word-count` | 2253620 | LLGo · deadcode drop | 1099870 | -51.2% |
| `word-count` | 2253620 | LLGo · full LTO (GlobalDCE off) | 960142 | -57.4% |
| `word-count` | 2253620 | LLGo · full LTO + GlobalDCE | 754849 | -66.5% |

## WASM binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 11.324x | 10 |
| LLGo · deadcode drop | 8.010x | 10 |
| LLGo · full LTO (GlobalDCE off) | 7.510x | 10 |
| LLGo · full LTO + GlobalDCE | 5.816x | 10 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `base64` | 96760 | LLGo · no LTO | 1122588 | +1060.2% |
| `base64` | 96760 | LLGo · deadcode drop | 733382 | +657.9% |
| `base64` | 96760 | LLGo · full LTO (GlobalDCE off) | 784224 | +710.5% |
| `base64` | 96760 | LLGo · full LTO + GlobalDCE | 587841 | +507.5% |
| `checksum` | 92685 | LLGo · no LTO | 1113118 | +1101.0% |
| `checksum` | 92685 | LLGo · deadcode drop | 722821 | +679.9% |
| `checksum` | 92685 | LLGo · full LTO (GlobalDCE off) | 773733 | +734.8% |
| `checksum` | 92685 | LLGo · full LTO + GlobalDCE | 575765 | +521.2% |
| `conv-wasi` | 201149 | LLGo · no LTO | 2178231 | +982.9% |
| `conv-wasi` | 201149 | LLGo · deadcode drop | 1504694 | +648.0% |
| `conv-wasi` | 201149 | LLGo · full LTO (GlobalDCE off) | 1533636 | +662.4% |
| `conv-wasi` | 201149 | LLGo · full LTO + GlobalDCE | 1074391 | +434.1% |
| `fibonacci` | 62386 | LLGo · no LTO | 986224 | +1480.8% |
| `fibonacci` | 62386 | LLGo · deadcode drop | 681793 | +992.9% |
| `fibonacci` | 62386 | LLGo · full LTO (GlobalDCE off) | 502888 | +706.1% |
| `fibonacci` | 62386 | LLGo · full LTO + GlobalDCE | 473117 | +658.4% |
| `grep` | 303772 | LLGo · no LTO | 1902618 | +526.3% |
| `grep` | 303772 | LLGo · deadcode drop | 1427912 | +370.1% |
| `grep` | 303772 | LLGo · full LTO (GlobalDCE off) | 1293915 | +325.9% |
| `grep` | 303772 | LLGo · full LTO + GlobalDCE | 1032119 | +239.8% |
| `glob` | 93153 | LLGo · no LTO | 1531562 | +1544.1% |
| `glob` | 93153 | LLGo · deadcode drop | 1123458 | +1106.0% |
| `glob` | 93153 | LLGo · full LTO (GlobalDCE off) | 1000935 | +974.5% |
| `glob` | 93153 | LLGo · full LTO + GlobalDCE | 778219 | +735.4% |
| `json-wasi` | 493590 | LLGo · no LTO | 3078248 | +523.6% |
| `json-wasi` | 493590 | LLGo · deadcode drop | 2134184 | +332.4% |
| `json-wasi` | 493590 | LLGo · full LTO (GlobalDCE off) | 2208023 | +347.3% |
| `json-wasi` | 493590 | LLGo · full LTO + GlobalDCE | 1613730 | +226.9% |
| `path-report` | 116889 | LLGo · no LTO | 1811908 | +1450.1% |
| `path-report` | 116889 | LLGo · deadcode drop | 1399675 | +1097.4% |
| `path-report` | 116889 | LLGo · full LTO (GlobalDCE off) | 1185674 | +914.4% |
| `path-report` | 116889 | LLGo · full LTO + GlobalDCE | 957684 | +719.3% |
| `sha-wasi` | 287449 | LLGo · no LTO | 2431609 | +745.9% |
| `sha-wasi` | 287449 | LLGo · deadcode drop | 1739588 | +505.2% |
| `sha-wasi` | 287449 | LLGo · full LTO (GlobalDCE off) | 1718743 | +497.9% |
| `sha-wasi` | 287449 | LLGo · full LTO + GlobalDCE | 1258950 | +338.0% |
| `word-count` | 86834 | LLGo · no LTO | 1499362 | +1626.7% |
| `word-count` | 86834 | LLGo · deadcode drop | 1099870 | +1166.6% |
| `word-count` | 86834 | LLGo · full LTO (GlobalDCE off) | 960142 | +1005.7% |
| `word-count` | 86834 | LLGo · full LTO + GlobalDCE | 754849 | +769.3% |
