# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 17261832 | 14227528 | 17037376 | 13447424 | 13307312 |
| Dustin_humanize | 4999050 | 6557272 | 4866704 | 6077352 | 4022192 | 3966912 |
| Etcdctl | 25896967 | 28914264 | 27201040 | 28910856 | 27795048 | 27517584 |
| Gorm_schema | 9421675 | 9531200 | 8750096 | 9102672 | 8701360 | 6301432 |
| IXGo | 47404128 | 45040880 | 44091728 | 45648968 | 44894536 | 44770720 |
| K8s_workqueue | 10681827 | 15160848 | 14188200 | 15053248 | 14726688 | 11081928 |
| Toml | 7324966 | 8382264 | 6913872 | 7964968 | 6242576 | 6171512 |
| Uber_zap | 10025000 | 15537608 | 12492184 | 15364496 | 12396720 | 12234496 |
| XGo | 18662581 | 23447392 | 19693128 | 23613248 | 19190416 | 19009560 |

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
