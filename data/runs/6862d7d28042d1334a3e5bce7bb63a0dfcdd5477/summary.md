# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 17261728 | 14227824 | 17037432 | 13447424 | 13307224 |
| Dustin_humanize | 4999050 | 6557280 | 4866704 | 6077352 | 4022192 | 3966912 |
| Etcdctl | 25896967 | 28914280 | 27200656 | 28910600 | 27795296 | 27517664 |
| Gorm_schema | 9421675 | 9531216 | 8750096 | 9102672 | 8701368 | 6301432 |
| IXGo | 47404128 | 45040504 | 44090152 | 45647960 | 44894120 | 44771336 |
| K8s_workqueue | 10681827 | 15160760 | 14187976 | 15053216 | 14726584 | 11081968 |
| Toml | 7324966 | 8382272 | 6913928 | 7964832 | 6242616 | 6171528 |
| Uber_zap | 10025000 | 15537584 | 12491992 | 15364464 | 12396680 | 12234408 |
| XGo | 18662581 | 23447456 | 19693336 | 23613136 | 19190560 | 19009744 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12586680 | 9644240 | 11649368 | 9274704 | 9149800 |
| Dustin_humanize | 3711728 | 4540568 | 2909344 | 4105000 | 2768856 | 2720112 |
| Etcdctl | 20251432 | 21355112 | 19694984 | 20228912 | 19502792 | 19202112 |
| Gorm_schema | 7186360 | 6811328 | 6057384 | 6329824 | 6058728 | 4455544 |
| IXGo | 37601624 | 31096848 | 30179472 | 29451968 | 29003248 | 28864256 |
| K8s_workqueue | 8105040 | 11098112 | 10155920 | 10357288 | 10180096 | 7663360 |
| Toml | 5573864 | 5969432 | 4556064 | 5472824 | 4366464 | 4304208 |
| Uber_zap | 7635104 | 11316368 | 8351880 | 10543656 | 8565456 | 8417584 |
| XGo | 14015312 | 17114168 | 13487920 | 16133112 | 13077688 | 12915952 |
