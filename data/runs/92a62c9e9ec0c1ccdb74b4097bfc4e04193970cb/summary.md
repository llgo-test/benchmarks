# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18034752 | 14868248 | 17175656 | 13798808 | 13497592 |
| Dustin_humanize | 4999050 | 6710984 | 5004024 | 6115016 | 4059472 | 3988504 |
| Etcdctl | 25896967 | 29844912 | 27287808 | 29059032 | 28042200 | 27622104 |
| Gorm_schema | 9421675 | 9738400 | 8941080 | 9106440 | 8729832 | 6315936 |
| IXGo | 47404128 | — | — | — | — | — |
| K8s_workqueue | 10681827 | 15857456 | 14059328 | 15251840 | 14983136 | 11283032 |
| Toml | 7324966 | 8560256 | 7083600 | 7964288 | 6270952 | 6169600 |
| Uber_zap | 10025000 | 16260728 | 12968464 | 15564616 | 13178464 | 12430856 |
| XGo | 18662581 | 24267568 | 20370144 | 23721768 | 19510592 | 19133112 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12568760 | 9495640 | 11467088 | 9231432 | 9006112 |
| Dustin_humanize | 3711728 | 4559920 | 2913448 | 4099712 | 2763168 | 2706632 |
| Etcdctl | 20251432 | 21368456 | 18877784 | 20062280 | 19387904 | 18984440 |
| Gorm_schema | 7186360 | 6829264 | 6058392 | 6298496 | 6040544 | 4430800 |
| IXGo | 37601624 | — | — | — | — | — |
| K8s_workqueue | 8105040 | 11082640 | 9330120 | 10228224 | 10083104 | 7538024 |
| Toml | 5573864 | 5987288 | 4564960 | 5421936 | 4342904 | 4258584 |
| Uber_zap | 7635104 | 11322208 | 8117968 | 10436488 | 8851712 | 8307392 |
| XGo | 14015312 | 17111656 | 13349776 | 15952488 | 13031680 | 12731968 |

10 paired size measurements are missing; excluded from DWARF comparisons.
