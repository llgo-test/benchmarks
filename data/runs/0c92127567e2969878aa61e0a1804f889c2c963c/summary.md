# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18034832 | 14868344 | 17175752 | 13799144 | 13497576 |
| Dustin_humanize | 4999050 | 6710952 | 5004024 | 6115072 | 4059488 | 3988496 |
| Etcdctl | 25896967 | 29844832 | 27288104 | 29059016 | 28042192 | 27622344 |
| Gorm_schema | 9421675 | 9738416 | 8941064 | 9106400 | 8729840 | 6315976 |
| IXGo | 47404128 | — | — | — | — | — |
| K8s_workqueue | 10681827 | 15857336 | 14059480 | 15251864 | 14983512 | 11283016 |
| Toml | 7324966 | 8560200 | 7083576 | 7964192 | 6271008 | 6169744 |
| Uber_zap | 10025000 | 16260384 | 12968360 | 15564608 | 13178400 | 12430920 |
| XGo | 18662581 | 24267496 | 20370504 | 23721288 | 19510336 | 19133056 |

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
