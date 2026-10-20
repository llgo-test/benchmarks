# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 17255896 | 14222040 | 17030176 | 13446056 | 13307376 |
| Dustin_humanize | 4999050 | 6553856 | 4863336 | 6074856 | 4022024 | 3966728 |
| Etcdctl | 25896967 | 28901368 | 27187592 | 28901040 | 27790888 | 27512096 |
| Gorm_schema | 9421675 | 9526936 | 8746216 | 9098912 | 8699552 | 6301256 |
| IXGo | 47404128 | 45043920 | 44090112 | 45642768 | 44892848 | 44772608 |
| K8s_workqueue | 10681827 | 15154960 | 14182200 | 15048328 | 14723416 | 11080688 |
| Toml | 7324966 | 8377808 | 6909576 | 7961496 | 6242088 | 6171184 |
| Uber_zap | 10025000 | 15531824 | 12487048 | 15357880 | 12395432 | 12234280 |
| XGo | 18662581 | 23431552 | 19676192 | 23599200 | 19188640 | 19008792 |

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
