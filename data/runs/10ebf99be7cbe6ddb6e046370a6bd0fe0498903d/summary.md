# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 17358112 | 14209880 | 17134056 | 13524928 | 13385616 |
| Dustin_humanize | 4999050 | 6651088 | 4956792 | 6166024 | 4067552 | 4012776 |
| Etcdctl | 25896967 | 29077576 | 26553960 | 29073336 | 27961896 | 27684192 |
| Gorm_schema | 9421675 | 9651864 | 8862992 | 9214720 | 8815088 | 6384040 |
| IXGo | 47404128 | 45496480 | 44542680 | 46279576 | 45514968 | 45392776 |
| K8s_workqueue | 10681827 | 15223856 | 13452608 | 15126304 | 14798848 | 11124856 |
| Toml | 7324966 | 8494448 | 7015656 | 8080688 | 6335264 | 6263920 |
| Uber_zap | 10025000 | 15601920 | 12339440 | 15435600 | 12447280 | 12285312 |
| XGo | 18662581 | 23558664 | 19692792 | 23748192 | 19311544 | 19129264 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12508288 | 9453536 | 11580048 | 9204312 | 9079392 |
| Dustin_humanize | 3711728 | 4562264 | 2927872 | 4121872 | 2772688 | 2723992 |
| Etcdctl | 20251432 | 21281248 | 18825264 | 20162672 | 19435984 | 19135024 |
| Gorm_schema | 7186360 | 6832104 | 6070728 | 6346688 | 6074784 | 4469280 |
| IXGo | 37601624 | 30955656 | 30038008 | 29331744 | 28883112 | 28744192 |
| K8s_workqueue | 8105040 | 11020480 | 9293944 | 10286896 | 10107968 | 7592624 |
| Toml | 5573864 | 5990896 | 4568168 | 5491560 | 4380744 | 4318440 |
| Uber_zap | 7635104 | 11238624 | 8063040 | 10473104 | 8494808 | 8346952 |
| XGo | 14015312 | 17037664 | 13303160 | 16062312 | 13005104 | 12843280 |
