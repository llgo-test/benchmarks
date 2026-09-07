# Go, TinyGo, and LLGo WASM application size

`wasip1/wasm`; smaller is better. All three compilers use the same pinned Go toolchain.
Go uses `-trimpath -ldflags='-s -w'`; TinyGo uses `-opt=z -no-debug`; LLGo uses `-Oz`.
LLGo uses the `wasm-opt` bundled with pinned Emscripten for Asyncify and exception
translation; TinyGo continues to use its separately pinned Binaryen release.

Geometric-mean TinyGo/Go size ratio: **0.059x**.
Geometric-mean LLGo/Go size ratio: **0.658x**.

| Application | Kind | Go bytes | TinyGo bytes | LLGo bytes | TinyGo vs Go | LLGo vs Go |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| `base64` | streaming codec | 2275731 | 97341 | 1120970 | -95.7% | -50.7% |
| `checksum` | streaming checksum | 2264417 | 93266 | 1098641 | -95.9% | -51.5% |
| `conv-wasi` | image processing | 2608055 | 202369 | 2147320 | -92.2% | -17.7% |
| `fibonacci` | recursive computation | 2230980 | 62846 | 976102 | -97.2% | -56.2% |
| `grep` | text search | 2848917 | 305182 | 1887235 | -89.3% | -33.8% |
| `glob` | text search | 2257634 | 93733 | 1516228 | -95.8% | -32.8% |
| `json-wasi` | structured data | 3314554 | 496712 | 3046232 | -85.0% | -8.1% |
| `path-report` | report generator | 2381190 | 117553 | 1796846 | -95.1% | -24.5% |
| `sha-wasi` | cryptographic hash | 2780938 | 289085 | 2411185 | -89.6% | -13.3% |
| `word-count` | text analysis | 2253620 | 87389 | 1483903 | -96.1% | -34.2% |
