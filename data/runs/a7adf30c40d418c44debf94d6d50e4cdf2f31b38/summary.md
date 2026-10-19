# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 17255984 | 14221960 | 17029944 | 13445896 | 13307560 |
| Dustin_humanize | 4999050 | 6553848 | 4863336 | 6074856 | 4022024 | 3966728 |
| Etcdctl | 25896967 | 28901968 | 27187624 | 28900856 | 27791032 | 27512096 |
| Gorm_schema | 9421675 | 9526936 | 8746216 | 9098912 | 8699552 | 6301240 |
| IXGo | 47404128 | 45046944 | 44089144 | 45644424 | 44892752 | 44772456 |
| K8s_workqueue | 10681827 | 15154920 | 14182256 | 15048328 | 14723232 | 11080664 |
| Toml | 7324966 | 8377768 | 6909616 | 7961616 | 6242224 | 6171112 |
| Uber_zap | 10025000 | 15531792 | 12487208 | 15358016 | 12395424 | 12234288 |
| XGo | 18662581 | 23431568 | 19676416 | 23599096 | 19188648 | 19008760 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12586760 | 9644336 | 11649400 | 9274744 | 9149896 |
| Dustin_humanize | 3711728 | 4540600 | 2909368 | 4105000 | 2768856 | 2720112 |
| Etcdctl | 20251432 | 21355744 | 19695576 | 20229504 | 19503384 | 19202704 |
| Gorm_schema | 7186360 | 6811408 | 6057448 | 6329912 | 6058744 | 4455544 |
| IXGo | 37601624 | 31103712 | 30186352 | 29452496 | 29003840 | 28864784 |
| K8s_workqueue | 8105040 | 11098440 | 10156176 | 10357624 | 10180432 | 7663504 |
| Toml | 5573864 | 5969464 | 4556088 | 5472824 | 4366464 | 4304208 |
| Uber_zap | 7635104 | 11316592 | 8352120 | 10543864 | 8565704 | 8417800 |
| XGo | 14015312 | 17114368 | 13488112 | 16133280 | 13077864 | 12916120 |
