# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18300656 | 15091584 | 17076160 | 13684936 | 13391400 |
| Dustin_humanize | 4999050 | 6928096 | 5190896 | 6241384 | 4179136 | 4107016 |
| Etcdctl | 25896967 | 30182488 | 27596416 | 28789152 | 27764336 | 27351480 |
| Gorm_schema | 9421675 | 9974904 | 9172456 | 9197208 | 8817216 | 6409856 |
| IXGo | 47404128 | 46706720 | 45838024 | 45300624 | 44808224 | 44666232 |
| K8s_workqueue | 10681827 | 16143544 | 14335560 | 15126816 | 14851816 | 11184576 |
| Toml | 7324966 | 8780128 | 7278872 | 8058440 | 6378512 | 6278720 |
| Uber_zap | 10025000 | 16545864 | 13209552 | 15455688 | 13055832 | 12322216 |
| XGo | 18662581 | 24604448 | 20637184 | 23463352 | 19290880 | 18911960 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12696880 | 9588512 | 11638048 | 9357472 | 9136496 |
| Dustin_humanize | 3711728 | 4711288 | 3039328 | 4243784 | 2895304 | 2838712 |
| Etcdctl | 20251432 | 21519872 | 19008200 | 20131520 | 19454184 | 19057552 |
| Gorm_schema | 7186360 | 6977064 | 6202376 | 6439160 | 6179800 | 4561952 |
| IXGo | 37601624 | 30992584 | 30174064 | 28924168 | 28647112 | 28530760 |
| K8s_workqueue | 8105040 | 11248080 | 9488016 | 10357280 | 10207344 | 7656960 |
| Toml | 5573864 | 6135400 | 4692720 | 5564856 | 4484416 | 4401320 |
| Uber_zap | 7635104 | 11487304 | 8246032 | 10589432 | 8964024 | 8422832 |
| XGo | 14015312 | 17277984 | 13460856 | 16068712 | 13146920 | 12848096 |
