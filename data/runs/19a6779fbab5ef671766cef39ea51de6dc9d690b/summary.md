# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18463760 | 15211008 | 17240088 | 13811624 | 13517944 |
| Dustin_humanize | 4999050 | 6995272 | 5245432 | 6302368 | 4228520 | 4154744 |
| Etcdctl | 25896967 | 30438592 | 27828864 | 29038056 | 28012632 | 27601248 |
| Gorm_schema | 9421675 | 10074408 | 9265576 | 9286200 | 8907912 | 6470992 |
| IXGo | 47404128 | 47122032 | 46272016 | 45696352 | 45204344 | 45075160 |
| K8s_workqueue | 10681827 | 16295416 | 14456224 | 15261232 | 14987432 | 11276184 |
| Toml | 7324966 | 8837000 | 7343856 | 8111488 | 6439624 | 6338552 |
| Uber_zap | 10025000 | 16707408 | 13316416 | 15594896 | 13162672 | 12421480 |
| XGo | 18662581 | 24940464 | 20925360 | 23770336 | 19551272 | 19175600 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12809320 | 9658656 | 11748248 | 9437808 | 9217824 |
| Dustin_humanize | 3711728 | 4756576 | 3071528 | 4288488 | 2929152 | 2871592 |
| Etcdctl | 20251432 | 21688576 | 19154352 | 20301392 | 19628984 | 19232144 |
| Gorm_schema | 7186360 | 7045176 | 6264040 | 6504808 | 6246728 | 4605824 |
| IXGo | 37601624 | 31299544 | 30490072 | 29221392 | 28947664 | 28839832 |
| K8s_workqueue | 8105040 | 11353848 | 9563480 | 10456424 | 10307784 | 7722696 |
| Toml | 5573864 | 6168384 | 4733688 | 5596272 | 4527824 | 4444456 |
| Uber_zap | 7635104 | 11593280 | 8297824 | 10688768 | 9039936 | 8495200 |
| XGo | 14015312 | 17529456 | 13665616 | 16311104 | 13354680 | 13058104 |
