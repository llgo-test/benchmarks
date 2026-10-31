# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 17354216 | 14205264 | 17128648 | 13521368 | 13381128 |
| Dustin_humanize | 4999050 | 6647208 | 4952816 | 6161752 | 4063904 | 4009016 |
| Etcdctl | 25896967 | 29073776 | 26550272 | 29069160 | 27957864 | 27679448 |
| Gorm_schema | 9421675 | 9647496 | 8858616 | 9209816 | 8810672 | 6380136 |
| IXGo | 47404128 | 45489704 | 44534480 | — | — | — |
| K8s_workqueue | 10681827 | 15219200 | 13448240 | 15121712 | 14794224 | 11120536 |
| Toml | 7324966 | 8490496 | 7011512 | 8076616 | 6331776 | 6260576 |
| Uber_zap | 10025000 | 15597744 | 12335520 | 15430608 | 12443816 | 12281504 |
| XGo | 18662581 | 23554272 | 19688704 | 23744840 | 19308048 | 19125544 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12506160 | 9451312 | 11578968 | 9203240 | 9078336 |
| Dustin_humanize | 3711728 | 4560104 | 2925680 | 4120968 | 2771824 | 2723080 |
| Etcdctl | 20251432 | 21279560 | 18823536 | 20161976 | 19435200 | 19134232 |
| Gorm_schema | 7186360 | 6829912 | 6068536 | 6345696 | 6073856 | 4468336 |
| IXGo | 37601624 | 30954120 | 30036536 | — | — | — |
| K8s_workqueue | 8105040 | 11018224 | 9291784 | 10285872 | 10106976 | 7591728 |
| Toml | 5573864 | 5988672 | 4565992 | 5490656 | 4379864 | 4317600 |
| Uber_zap | 7635104 | 11236448 | 8060800 | 10472096 | 8493928 | 8346048 |
| XGo | 14015312 | 17035968 | 13301448 | 16062184 | 13004680 | 12842840 |

6 paired size measurements are missing; excluded from DWARF comparisons.
