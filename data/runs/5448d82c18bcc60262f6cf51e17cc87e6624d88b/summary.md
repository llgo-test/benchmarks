# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 17374384 | 14201400 | 16813648 | 13446976 | 13155640 |
| Dustin_humanize | 4999050 | 6660088 | 4957312 | 6089240 | 4037688 | 3966544 |
| Etcdctl | 25896967 | 29118672 | 26548360 | 28671136 | 27651616 | 27237832 |
| Gorm_schema | 9421675 | 9660760 | 8857712 | 9071104 | 8694704 | 6286312 |
| IXGo | 47404128 | — | — | — | — | — |
| K8s_workqueue | 10681827 | 15248552 | 13446840 | 14901416 | 14631968 | 10948192 |
| Toml | 7324966 | 8501016 | 7020032 | 7930800 | 6240648 | 6141456 |
| Uber_zap | 10025000 | 15648936 | 12355944 | 15218152 | 12838488 | 12098176 |
| XGo | 18662581 | 23594800 | 19695664 | 23347752 | 19147152 | 18772128 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12546624 | 9462504 | 11436608 | 9202816 | 8979000 |
| Dustin_humanize | 3711728 | 4584032 | 2939576 | 4100144 | 2763888 | 2707128 |
| Etcdctl | 20251432 | 21343848 | 18839296 | 20021056 | 19346136 | 18943400 |
| Gorm_schema | 7186360 | 6855672 | 6078544 | 6297960 | 6040744 | 4430584 |
| IXGo | 37601624 | — | — | — | — | — |
| K8s_workqueue | 8105040 | 11062896 | 9303856 | 10199136 | 10052808 | 7509824 |
| Toml | 5573864 | 6012536 | 4584072 | 5421376 | 4343024 | 4258712 |
| Uber_zap | 7635104 | 11304152 | 8095128 | 10405296 | 8820848 | 8278144 |
| XGo | 14015312 | 17096096 | 13325280 | 15923200 | 13002808 | 12703984 |

10 paired size measurements are missing; excluded from DWARF comparisons.
