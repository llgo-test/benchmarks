# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 17255760 | 14221944 | 17029752 | 13446080 | 13307640 |
| Dustin_humanize | 4999050 | 6553856 | 4863336 | 6074856 | 4022024 | 3966728 |
| Etcdctl | 25896967 | 28901552 | 27187632 | 28900816 | 27791008 | 27512072 |
| Gorm_schema | 9421675 | 9526944 | 8746056 | 9098904 | 8699552 | 6301256 |
| IXGo | 47404128 | 45044120 | 44088560 | 45643168 | 44896440 | 44772856 |
| K8s_workqueue | 10681827 | 15154920 | 14181856 | 15048344 | 14723248 | 11080624 |
| Toml | 7324966 | 8377824 | 6909584 | 7961648 | 6242048 | 6171136 |
| Uber_zap | 10025000 | 15531776 | 12486904 | 15357992 | 12395320 | 12234040 |
| XGo | 18662581 | 23431496 | 19675984 | 23598928 | 19188208 | 19009000 |

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
