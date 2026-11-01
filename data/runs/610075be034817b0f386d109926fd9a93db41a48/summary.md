# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 17354088 | 14205400 | 17129000 | 13520816 | 13380840 |
| Dustin_humanize | 4999050 | 6647208 | 4952816 | 6161752 | 4063904 | 4009000 |
| Etcdctl | 25896967 | 29073736 | 26549968 | 29069040 | 27957928 | 27679744 |
| Gorm_schema | 9421675 | 9647480 | 8858616 | 9209824 | 8810680 | 6380136 |
| IXGo | 47404128 | 45491416 | 44536952 | — | — | — |
| K8s_workqueue | 10681827 | 15218984 | 13448224 | 15121712 | 14794264 | 11120832 |
| Toml | 7324966 | 8490480 | 7011496 | 8076680 | 6331704 | 6260592 |
| Uber_zap | 10025000 | 15598048 | 12335232 | 15430552 | 12443600 | 12281344 |
| XGo | 18662581 | 23554368 | 19688816 | 23744824 | 19308352 | 19125840 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12506160 | 9451312 | 11578968 | 9203240 | 9078336 |
| Dustin_humanize | 3711728 | 4560104 | 2925680 | 4120968 | 2771824 | 2723080 |
| Etcdctl | 20251432 | 21279560 | 18823536 | 20161976 | 19435200 | 19134232 |
| Gorm_schema | 7186360 | 6829912 | 6068536 | 6345696 | 6073856 | 4468336 |
| IXGo | 37601624 | 30954120 | 30036520 | — | — | — |
| K8s_workqueue | 8105040 | 11018224 | 9291784 | 10285872 | 10106976 | 7591728 |
| Toml | 5573864 | 5988672 | 4565992 | 5490656 | 4379864 | 4317536 |
| Uber_zap | 7635104 | 11236448 | 8060800 | 10472096 | 8493928 | 8346048 |
| XGo | 14015312 | 17035968 | 13301448 | 16062184 | 13004680 | 12842840 |

6 paired size measurements are missing; excluded from DWARF comparisons.
