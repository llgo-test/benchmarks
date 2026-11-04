# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 17340512 | 14197880 | 16874008 | 13334008 | 13195784 |
| Dustin_humanize | 4999050 | 6640280 | 4949056 | 6082632 | 4019424 | 3963952 |
| Etcdctl | 25896967 | 29030176 | 26519568 | 28649208 | 27542976 | 27266232 |
| Gorm_schema | 9421675 | 9637680 | 8849472 | 9078128 | 8679848 | 6296552 |
| IXGo | 47404128 | 45443152 | 44498168 | 45607904 | 44846968 | 44734824 |
| K8s_workqueue | 10681827 | 15206728 | 13435840 | 14906848 | 14583832 | 10970072 |
| Toml | 7324966 | 8482904 | 7006784 | 7958664 | 6237976 | 6168104 |
| Uber_zap | 10025000 | 15584256 | 12325040 | 15205072 | 12263464 | 12101544 |
| XGo | 18662581 | 23531960 | 19668576 | 23348320 | 18965768 | 18785232 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12491816 | 9442088 | 11482336 | 9130544 | 9006088 |
| Dustin_humanize | 3711728 | 4552968 | 2921472 | 4090368 | 2750768 | 2702136 |
| Etcdctl | 20251432 | 21237008 | 18793056 | 19993432 | 19266360 | 18965488 |
| Gorm_schema | 7186360 | 6819776 | 6058976 | 6294688 | 6022384 | 4434192 |
| IXGo | 37601624 | 30906424 | 29999048 | 29072088 | 28620832 | 28491096 |
| K8s_workqueue | 8105040 | 11004176 | 9278616 | 10200056 | 10020816 | 7530720 |
| Toml | 5573864 | 5979616 | 4559192 | 5445336 | 4343808 | 4281760 |
| Uber_zap | 7635104 | 11221720 | 8049320 | 10385728 | 8424144 | 8276608 |
| XGo | 14015312 | 17013272 | 13282080 | 15910056 | 12873232 | 12711784 |
