# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 17255864 | 14221912 | 17029880 | 13446136 | 13307560 |
| Dustin_humanize | 4999050 | 6553856 | 4863336 | 6074856 | 4022024 | 3966728 |
| Etcdctl | 25896967 | 28901720 | 27187632 | 28901208 | 27790720 | 27512080 |
| Gorm_schema | 9421675 | 9526936 | 8746056 | 9098912 | 8699552 | 6301256 |
| IXGo | 47404128 | 45046888 | 44091840 | 45644144 | 44892624 | 44774224 |
| K8s_workqueue | 10681827 | 15154888 | 14182192 | 15048248 | 14723320 | 11080504 |
| Toml | 7324966 | 8377848 | 6909648 | 7961520 | 6242264 | 6171128 |
| Uber_zap | 10025000 | 15531816 | 12486904 | 15357880 | 12395328 | 12234168 |
| XGo | 18662581 | 23431536 | 19676184 | 23599248 | 19188592 | 19008760 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12586760 | 9644336 | 11649400 | 9274744 | 9149896 |
| Dustin_humanize | 3711728 | 4540600 | 2909368 | 4105000 | 2768856 | 2720112 |
| Etcdctl | 20251432 | 21355744 | 19695576 | 20229504 | 19503384 | 19202704 |
| Gorm_schema | 7186360 | 6811408 | 6057464 | 6329912 | 6058744 | 4455544 |
| IXGo | 37601624 | 31103712 | 30186352 | 29452496 | 29003840 | 28864784 |
| K8s_workqueue | 8105040 | 11098440 | 10156176 | 10357624 | 10180432 | 7663504 |
| Toml | 5573864 | 5969464 | 4556088 | 5472824 | 4366464 | 4304208 |
| Uber_zap | 7635104 | 11316592 | 8352120 | 10543864 | 8565704 | 8417800 |
| XGo | 14015312 | 17114368 | 13488112 | 16133280 | 13077864 | 12916120 |
