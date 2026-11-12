# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18140288 | 14973016 | 17269720 | 13891456 | 13589176 |
| Dustin_humanize | 4999050 | 6853088 | 5141800 | 6229656 | 4178576 | 4105832 |
| Etcdctl | 25896967 | 29959264 | 27401624 | 29006920 | 27976480 | 27560416 |
| Gorm_schema | 9421675 | 9873488 | 9073880 | 9187280 | 8807008 | 6409912 |
| IXGo | 47404128 | 46568152 | 45714896 | 45542440 | 45050104 | 44896432 |
| K8s_workqueue | 10681827 | 15989312 | 14192248 | 15304376 | 15033416 | 11373560 |
| Toml | 7324966 | 8696848 | 7219744 | 8048160 | 6374440 | 6273264 |
| Uber_zap | 10025000 | 16395832 | 13108384 | 15598552 | 13241280 | 12504320 |
| XGo | 18662581 | 24393384 | 20498472 | 23664424 | 19503848 | 19120240 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12663328 | 9590320 | 11630952 | 9358904 | 9137064 |
| Dustin_humanize | 3711728 | 4688912 | 3038952 | 4226296 | 2885304 | 2828864 |
| Etcdctl | 20251432 | 21480056 | 18990696 | 20152800 | 19468584 | 19071192 |
| Gorm_schema | 7186360 | 6952688 | 6180176 | 6418336 | 6158136 | 4549960 |
| IXGo | 37601624 | 31193056 | 30377864 | 28929056 | 28652104 | 28537600 |
| K8s_workqueue | 8105040 | 11205312 | 9453984 | 10344560 | 10194128 | 7656272 |
| Toml | 5573864 | 6115352 | 4692416 | 5548496 | 4471704 | 4388712 |
| Uber_zap | 7635104 | 11447192 | 8249408 | 10549240 | 8964600 | 8425120 |
| XGo | 14015312 | 17227536 | 13467728 | 16063584 | 13148912 | 12850928 |
