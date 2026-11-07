# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18033376 | 14867624 | 17175208 | 13798360 | 13496824 |
| Dustin_humanize | 4999050 | 6709920 | 5003560 | 6114744 | 4059096 | 3987696 |
| Etcdctl | 25896967 | 29844384 | 27287256 | 29058608 | 28042128 | 27621400 |
| Gorm_schema | 9421675 | 9737616 | 8940480 | 9105728 | 8729544 | 6315160 |
| IXGo | 47404128 | — | — | — | — | — |
| K8s_workqueue | 10681827 | 15855816 | 14058520 | 15250968 | 14982496 | 11282016 |
| Toml | 7324966 | 8559520 | 7082856 | 7963728 | 6270568 | 6168784 |
| Uber_zap | 10025000 | 16259792 | 12967440 | 15564168 | 13177872 | 12430376 |
| XGo | 18662581 | 24266408 | 20369528 | 23721032 | 19509952 | 19132064 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12568632 | 9495608 | 11466944 | 9231224 | 9005904 |
| Dustin_humanize | 3711728 | 4559792 | 2913416 | 4099568 | 2762944 | 2706408 |
| Etcdctl | 20251432 | 21368424 | 18877752 | 20062248 | 19387872 | 18984392 |
| Gorm_schema | 7186360 | 6829136 | 6058296 | 6298352 | 6040320 | 4430592 |
| IXGo | 37601624 | — | — | — | — | — |
| K8s_workqueue | 8105040 | 11082512 | 9329976 | 10228096 | 10082864 | 7537800 |
| Toml | 5573864 | 5987160 | 4564864 | 5421808 | 4342648 | 4258360 |
| Uber_zap | 7635104 | 11322080 | 8117872 | 10436344 | 8851472 | 8307184 |
| XGo | 14015312 | 17111576 | 13349728 | 15952456 | 13031648 | 12731936 |

10 paired size measurements are missing; excluded from DWARF comparisons.
