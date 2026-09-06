# Go, TinyGo, and LLGo WASM application size

`wasip1/wasm`; smaller is better. All three compilers use the same pinned Go toolchain.
Go uses `-trimpath -ldflags='-s -w'`; TinyGo uses `-opt=z -no-debug`; LLGo uses `-Oz`.
LLGo uses the `wasm-opt` bundled with pinned Emscripten for Asyncify and exception
translation; TinyGo continues to use its separately pinned Binaryen release.

Geometric-mean TinyGo/Go size ratio: **0.059x**.
Geometric-mean LLGo/Go size ratio: **0.650x**.

| Application | Kind | Go bytes | TinyGo bytes | LLGo bytes | TinyGo vs Go | LLGo vs Go |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| `base64` | streaming codec | 2275731 | 97341 | 1108313 | -95.7% | -51.3% |
| `checksum` | streaming checksum | 2264417 | 93266 | 1086584 | -95.9% | -52.0% |
| `conv-wasi` | image processing | 2608055 | 202369 | 2118426 | -92.2% | -18.8% |
| `fibonacci` | recursive computation | 2230980 | 62846 | 964655 | -97.2% | -56.8% |
| `grep` | text search | 2848917 | 305182 | 1864543 | -89.3% | -34.6% |
| `glob` | text search | 2257634 | 93733 | 1499443 | -95.8% | -33.6% |
| `json-wasi` | structured data | 3314554 | 496712 | 3003973 | -85.0% | -9.4% |
| `path-report` | report generator | 2381190 | 117553 | 1779662 | -95.1% | -25.3% |
| `sha-wasi` | cryptographic hash | 2780938 | 289085 | 2379672 | -89.6% | -14.4% |
| `word-count` | text analysis | 2253620 | 87389 | 1466979 | -96.1% | -34.9% |
