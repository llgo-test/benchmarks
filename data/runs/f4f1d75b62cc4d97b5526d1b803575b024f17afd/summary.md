# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18058576 | 14887856 | 17128648 | 13770840 | 13470256 |
| Dustin_humanize | 4999050 | 6735688 | 5024024 | 6107856 | 4056072 | 3983144 |
| Etcdctl | 25896967 | 29870568 | 27313336 | 28908952 | 27883888 | 27467576 |
| Gorm_schema | 9421675 | 9760872 | 8964632 | 9072264 | 8693248 | 6292048 |
| IXGo | 47404128 | 46471184 | 45621288 | 45398640 | 44910480 | 44756776 |
| K8s_workqueue | 10681827 | 15885960 | 14089800 | 15184240 | 14916248 | 11247104 |
| Toml | 7324966 | 8582688 | 7106168 | 7931528 | 6255840 | 6154472 |
| Uber_zap | 10025000 | 16293424 | 13002184 | 15482256 | 13116976 | 12378152 |
| XGo | 18662581 | 24309952 | 20415048 | 23577064 | 19401080 | 19019936 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12584440 | 9508512 | 11538400 | 9296968 | 9074976 |
| Dustin_humanize | 3711728 | 4573192 | 2922944 | 4119184 | 2776528 | 2720040 |
| Etcdctl | 20251432 | 21390808 | 18900520 | 20088208 | 19408192 | 19009896 |
| Gorm_schema | 7186360 | 6841840 | 6071880 | 6317024 | 6058192 | 4445768 |
| IXGo | 37601624 | 31147960 | 30335760 | 28917784 | 28642576 | 28523336 |
| K8s_workqueue | 8105040 | 11101568 | 9351080 | 10259584 | 10112920 | 7567560 |
| Toml | 5573864 | 6002864 | 4580040 | 5443376 | 4364104 | 4280848 |
| Uber_zap | 7635104 | 11344392 | 8142128 | 10467240 | 8879848 | 8337784 |
| XGo | 14015312 | 17138312 | 13376648 | 15999128 | 13077240 | 12779696 |
