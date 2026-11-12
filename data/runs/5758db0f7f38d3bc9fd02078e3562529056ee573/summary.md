# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18140088 | 14972704 | 17269392 | 13891152 | 13589456 |
| Dustin_humanize | 4999050 | 6852688 | 5141368 | 6229256 | 4178488 | 4105456 |
| Etcdctl | 25896967 | 29958912 | 27402008 | 29007464 | 27976352 | 27560664 |
| Gorm_schema | 9421675 | 9872880 | 9073800 | 9187144 | 8806768 | 6410536 |
| IXGo | 47404128 | 46567200 | 45713920 | 45541128 | 45048088 | 44898056 |
| K8s_workqueue | 10681827 | 15989640 | 14192480 | 15304424 | 15033592 | 11373416 |
| Toml | 7324966 | 8696832 | 7219408 | 8047952 | 6374656 | 6273312 |
| Uber_zap | 10025000 | 16395584 | 13108440 | 15598456 | 13241072 | 12504080 |
| XGo | 18662581 | 24393264 | 20498616 | 23665904 | 19503768 | 19121408 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12663304 | 9590272 | 11631208 | 9359160 | 9137304 |
| Dustin_humanize | 3711728 | 4688888 | 3038752 | 4226376 | 2885384 | 2828928 |
| Etcdctl | 20251432 | 21480312 | 18990952 | 20153120 | 19468888 | 19071512 |
| Gorm_schema | 7186360 | 6952656 | 6180144 | 6418400 | 6158216 | 4550136 |
| IXGo | 37601624 | 31193296 | 30378112 | 28929344 | 28652392 | 28537888 |
| K8s_workqueue | 8105040 | 11205304 | 9453960 | 10344816 | 10194416 | 7656336 |
| Toml | 5573864 | 6115320 | 4692408 | 5548736 | 4471976 | 4388984 |
| Uber_zap | 7635104 | 11447184 | 8249384 | 10549480 | 8964680 | 8425184 |
| XGo | 14015312 | 17227792 | 13467984 | 16063904 | 13149264 | 12851232 |
