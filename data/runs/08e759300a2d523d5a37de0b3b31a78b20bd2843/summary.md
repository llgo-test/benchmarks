# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 17354320 | 14205632 | 17128968 | 13521120 | 13381136 |
| Dustin_humanize | 4999050 | 6647200 | 4952824 | 6161736 | 4063904 | 4009016 |
| Etcdctl | 25896967 | 29073720 | 26550072 | 29068840 | 27957952 | 27679192 |
| Gorm_schema | 9421675 | 9647480 | 8858608 | 9209808 | 8810672 | 6380136 |
| IXGo | 47404128 | 45489600 | 44535800 | 46264520 | 45508984 | 45380432 |
| K8s_workqueue | 10681827 | 15219016 | 13447984 | 15121832 | 14794304 | 11120520 |
| Toml | 7324966 | 8490560 | 7011456 | 8076672 | 6331640 | 6260680 |
| Uber_zap | 10025000 | 15598072 | 12335280 | 15430768 | 12443600 | 12281392 |
| XGo | 18662581 | 23554216 | 19688368 | 23744544 | 19308232 | 19125656 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12506160 | 9451296 | 11578968 | 9203240 | 9078336 |
| Dustin_humanize | 3711728 | 4560104 | 2925680 | 4120968 | 2771824 | 2723080 |
| Etcdctl | 20251432 | 21279560 | 18823536 | 20161976 | 19435200 | 19134232 |
| Gorm_schema | 7186360 | 6829912 | 6068536 | 6345696 | 6073856 | 4468336 |
| IXGo | 37601624 | 30954120 | 30036536 | 29331224 | 28882280 | 28743344 |
| K8s_workqueue | 8105040 | 11018224 | 9291784 | 10285872 | 10106976 | 7591728 |
| Toml | 5573864 | 5988672 | 4565992 | 5490656 | 4379864 | 4317600 |
| Uber_zap | 7635104 | 11236448 | 8060800 | 10472096 | 8493928 | 8346048 |
| XGo | 14015312 | 17035968 | 13301448 | 16062184 | 13004680 | 12842840 |
