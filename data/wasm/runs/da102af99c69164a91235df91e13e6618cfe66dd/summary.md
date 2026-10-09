# WASM binary size

Per-application WASM host (wasip1 or js); smaller is better. JS glue is excluded.
Each application uses the same pinned Go toolchain across compilers; per-application versions are recorded below.

- Go: `build -trimpath '-ldflags=-s -w'`
- TinyGo: `build -opt=z -no-debug`
- LLGo · no LTO: `build -a -Oz`
- LLGo · deadcode drop: `build -a -Oz -deadcodedrop`
- LLGo · full LTO (GlobalDCE off): `CCFLAGS='-flto=full' LDFLAGS='-Wl,--lto-O2' build -a -Oz -lto=full -globaldce=false`
- LLGo · full LTO + GlobalDCE: `CCFLAGS='-flto=full -fvirtual-function-elimination -fwhole-program-vtables' LDFLAGS='-Wl,--lto-O2' build -a -Oz -lto=full -globaldce=true`

LLGo uses target-specific upstream Emscripten/Binaryen processing; see the recorded protocol.
TinyGo uses its separately pinned Binaryen release.
Failed builds are shown as — and excluded from comparisons; logs are included in the CI artifact.

## Failed builds

| Application | Configuration | Policy | Status | Log |
| --- | --- | --- | --- | --- |
| tsgo | TinyGo | optional | failed | [logs/tsgo.TinyGo.log](logs/tsgo.TinyGo.log) |

| Application | Target | Go toolchain | Source repository | Commit | Entry |
| --- | --- | --- | --- | --- | --- |
| tsgo | js/wasm | 1.27.0 | https://github.com/microsoft/TypeScript.git | c975de5011fb7dfb32a491cf3fcf02d4f811f50e | tsc/cmd/tsc |

## js/wasm binary size (vs. Go)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | 1.473x | 1 |
| LLGo · deadcode drop | 1.453x | 1 |
| LLGo · full LTO (GlobalDCE off) | 1.441x | 1 |
| LLGo · full LTO + GlobalDCE | 1.435x | 1 |

| Application | Go bytes | LLGo mode | LLGo bytes | vs. Go |
| --- | ---: | --- | ---: | ---: |
| `tsgo` | 50367588 | LLGo · no LTO | 74170788 | +47.3% |
| `tsgo` | 50367588 | LLGo · deadcode drop | 73161014 | +45.3% |
| `tsgo` | 50367588 | LLGo · full LTO (GlobalDCE off) | 72571567 | +44.1% |
| `tsgo` | 50367588 | LLGo · full LTO + GlobalDCE | 72253306 | +43.5% |

## js/wasm binary size (vs. TinyGo)

| LLGo mode | Geometric mean / baseline | Valid samples |
| --- | ---: | ---: |
| LLGo · no LTO | — | 0 |
| LLGo · deadcode drop | — | 0 |
| LLGo · full LTO (GlobalDCE off) | — | 0 |
| LLGo · full LTO + GlobalDCE | — | 0 |

| Application | TinyGo bytes | LLGo mode | LLGo bytes | vs. TinyGo |
| --- | ---: | --- | ---: | ---: |
| `tsgo` | — | LLGo · no LTO | 74170788 | — |
| `tsgo` | — | LLGo · deadcode drop | 73161014 | — |
| `tsgo` | — | LLGo · full LTO (GlobalDCE off) | 72571567 | — |
| `tsgo` | — | LLGo · full LTO + GlobalDCE | 72253306 | — |
