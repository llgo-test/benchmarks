# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 17354168 | 14205512 | 17128800 | 13520768 | 13381112 |
| Dustin_humanize | 4999050 | 6647208 | 4952824 | 6161752 | 4063904 | 4009000 |
| Etcdctl | 25896967 | 29074072 | 26550008 | 29069032 | 27958408 | 27679600 |
| Gorm_schema | 9421675 | 9647480 | 8858616 | 9209824 | 8810672 | 6380136 |
| IXGo | 47404128 | 45491008 | 44536176 | — | — | — |
| K8s_workqueue | 10681827 | 15219136 | 13448352 | 15121656 | 14794256 | 11120656 |
| Toml | 7324966 | 8490616 | 7011528 | 8076624 | 6331544 | 6260736 |
| Uber_zap | 10025000 | 15597856 | 12335384 | 15430512 | 12443632 | 12281456 |
| XGo | 18662581 | 23554304 | 19688888 | 23745056 | 19308128 | 19125504 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12506160 | 9451296 | 11578968 | 9203240 | 9078336 |
| Dustin_humanize | 3711728 | 4560104 | 2925680 | 4120968 | 2771824 | 2723080 |
| Etcdctl | 20251432 | 21279560 | 18823536 | 20161976 | 19435200 | 19134232 |
| Gorm_schema | 7186360 | 6829912 | 6068536 | 6345696 | 6073856 | 4468336 |
| IXGo | 37601624 | 30954120 | 30036536 | — | — | — |
| K8s_workqueue | 8105040 | 11018224 | 9291784 | 10285872 | 10106976 | 7591728 |
| Toml | 5573864 | 5988672 | 4565992 | 5490656 | 4379864 | 4317600 |
| Uber_zap | 7635104 | 11236448 | 8060800 | 10472096 | 8493928 | 8346048 |
| XGo | 14015312 | 17035968 | 13301448 | 16062184 | 13004680 | 12842840 |

6 paired size measurements are missing; excluded from DWARF comparisons.
