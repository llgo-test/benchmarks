# Go, TinyGo, and LLGo WASM application size

`wasip1/wasm`; smaller is better. All three compilers use the same pinned Go toolchain.
Go uses `-trimpath -ldflags='-s -w'`; TinyGo uses `-opt=z -no-debug`; LLGo uses `-Oz`.
LLGo uses the `wasm-opt` bundled with pinned Emscripten for Asyncify and exception
translation; TinyGo continues to use its separately pinned Binaryen release.

Geometric-mean TinyGo/Go size ratio: **0.059x**.
Geometric-mean LLGo/Go size ratio: **0.651x**.

| Application | Kind | Go bytes | TinyGo bytes | LLGo bytes | TinyGo vs Go | LLGo vs Go |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| `base64` | streaming codec | 2275731 | 97341 | 1109656 | -95.7% | -51.2% |
| `checksum` | streaming checksum | 2264417 | 93266 | 1087919 | -95.9% | -52.0% |
| `conv-wasi` | image processing | 2608055 | 202369 | 2119759 | -92.2% | -18.7% |
| `fibonacci` | recursive computation | 2230980 | 62846 | 965998 | -97.2% | -56.7% |
| `grep` | text search | 2848917 | 305182 | 1865888 | -89.3% | -34.5% |
| `glob` | text search | 2257634 | 93733 | 1500787 | -95.8% | -33.5% |
| `json-wasi` | structured data | 3314554 | 496712 | 3005330 | -85.0% | -9.3% |
| `path-report` | report generator | 2381190 | 117553 | 1780991 | -95.1% | -25.2% |
| `sha-wasi` | cryptographic hash | 2780938 | 289085 | 2381000 | -89.6% | -14.4% |
| `word-count` | text analysis | 2253620 | 87389 | 1468320 | -96.1% | -34.8% |
