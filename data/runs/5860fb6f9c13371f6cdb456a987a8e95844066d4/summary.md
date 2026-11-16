# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18300816 | 15091496 | 17076392 | 13685256 | 13391784 |
| Dustin_humanize | 4999050 | 6928104 | 5190896 | 6241384 | 4179136 | 4107016 |
| Etcdctl | 25896967 | 30182400 | 27595968 | 28789032 | 27763952 | 27351536 |
| Gorm_schema | 9421675 | 9974904 | 9172448 | 9197216 | 8817216 | 6409856 |
| IXGo | 47404128 | 46705256 | 45840056 | 45301640 | 44806720 | 44665824 |
| K8s_workqueue | 10681827 | 16143664 | 14335528 | 15126672 | 14852032 | 11184728 |
| Toml | 7324966 | 8779832 | 7278840 | 8058408 | 6378800 | 6278784 |
| Uber_zap | 10025000 | 16545592 | 13209440 | 15455872 | 13055840 | 12322592 |
| XGo | 18662581 | 24604448 | 20637320 | 23463208 | 19290792 | 18911736 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12696880 | 9588528 | 11638048 | 9357472 | 9136496 |
| Dustin_humanize | 3711728 | 4711288 | 3039328 | 4243784 | 2895304 | 2838712 |
| Etcdctl | 20251432 | 21519872 | 19008200 | 20131520 | 19454184 | 19057552 |
| Gorm_schema | 7186360 | 6977064 | 6202376 | 6439160 | 6179800 | 4561952 |
| IXGo | 37601624 | 30992584 | 30174064 | 28924168 | 28647112 | 28530760 |
| K8s_workqueue | 8105040 | 11248080 | 9488016 | 10357280 | 10207344 | 7656960 |
| Toml | 5573864 | 6135400 | 4692720 | 5564856 | 4484416 | 4401320 |
| Uber_zap | 7635104 | 11487304 | 8246032 | 10589432 | 8964024 | 8422832 |
| XGo | 14015312 | 17277984 | 13460856 | 16068712 | 13146920 | 12848096 |
