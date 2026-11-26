# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18472904 | 15192104 | 17261360 | 13795840 | 13506880 |
| Dustin_humanize | 4999050 | 6973272 | 5197192 | 6281544 | 4178312 | 4104024 |
| Etcdctl | 25896967 | 30501944 | 27886416 | 29123744 | 28076896 | 27669680 |
| Gorm_schema | 9421675 | 10069920 | 9255200 | 9301632 | 8918520 | 6444416 |
| IXGo | 47404128 | 47332296 | 46479736 | 46017224 | 45505680 | 45370320 |
| K8s_workqueue | 10681827 | 16297032 | 14451024 | 15272576 | 14997344 | 11262040 |
| Toml | 7324966 | 8819656 | 7304824 | 8097712 | 6407288 | 6304816 |
| Uber_zap | 10025000 | 16705792 | 13294456 | 15608040 | 13152104 | 12412200 |
| XGo | 18662581 | 24988920 | 20949000 | 23838008 | 19590416 | 19217864 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12795904 | 9619416 | 11734816 | 9396936 | 9177184 |
| Dustin_humanize | 3711728 | 4709152 | 3000728 | 4239104 | 2854992 | 2796856 |
| Etcdctl | 20251432 | 21720672 | 19179376 | 20315288 | 19634600 | 19239864 |
| Gorm_schema | 7186360 | 7013400 | 6225800 | 6477720 | 6216368 | 4547920 |
| IXGo | 37601624 | 31272392 | 30459824 | 29268296 | 28991088 | 28885096 |
| K8s_workqueue | 8105040 | 11333472 | 9535760 | 10435360 | 10284480 | 7677192 |
| Toml | 5573864 | 6127520 | 4673440 | 5553440 | 4469216 | 4384952 |
| Uber_zap | 7635104 | 11570960 | 8256720 | 10667152 | 8999552 | 8455232 |
| XGo | 14015312 | 17548520 | 13661232 | 16326904 | 13349184 | 13052944 |
