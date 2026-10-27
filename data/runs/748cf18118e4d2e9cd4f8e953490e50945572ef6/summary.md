# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 17470032 | 14320864 | 17230520 | 13621352 | 13481096 |
| Dustin_humanize | 4999050 | 6666624 | 4970384 | 6178728 | 4078224 | 4022992 |
| Etcdctl | 25896967 | 29181592 | 26658616 | 29170960 | 28060856 | 27782464 |
| Gorm_schema | 9421675 | 9667424 | 8875496 | 9226672 | 8826320 | 6393376 |
| IXGo | 47404128 | 45676088 | 44718952 | 46421216 | 45662688 | 45538088 |
| K8s_workqueue | 10681827 | 15335328 | 13564272 | 15223776 | 14896984 | 11221968 |
| Toml | 7324966 | 8509448 | 7028688 | 8091976 | 6344424 | 6273688 |
| Uber_zap | 10025000 | 15714440 | 12449840 | 15534112 | 12545288 | 12383160 |
| XGo | 18662581 | 23662088 | 19796760 | 23840312 | 19402496 | 19222400 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12616520 | 9560864 | 11678616 | 9302736 | 9177872 |
| Dustin_humanize | 3711728 | 4574880 | 2938136 | 4134840 | 2783712 | 2734968 |
| Etcdctl | 20251432 | 21380472 | 18924312 | 20255280 | 19529024 | 19228112 |
| Gorm_schema | 7186360 | 6844704 | 6080720 | 6359232 | 6086952 | 4479640 |
| IXGo | 37601624 | 31133760 | 30216144 | 29484296 | 29035896 | 28897008 |
| K8s_workqueue | 8105040 | 11128968 | 9402480 | 10385792 | 10207392 | 7691944 |
| Toml | 5573864 | 6002984 | 4578072 | 5503944 | 4391072 | 4328784 |
| Uber_zap | 7635104 | 11347216 | 8169360 | 10572136 | 8593936 | 8446072 |
| XGo | 14015312 | 17138456 | 13403984 | 16155568 | 13098544 | 12936728 |
