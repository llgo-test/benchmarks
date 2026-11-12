# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18140264 | 14972776 | 17269760 | 13891352 | 13589016 |
| Dustin_humanize | 4999050 | 6852696 | 5141368 | 6229256 | 4178488 | 4105456 |
| Etcdctl | 25896967 | 29959304 | 27401600 | 29007552 | 27975920 | 27560248 |
| Gorm_schema | 9421675 | 9872880 | 9073792 | 9187144 | 8806768 | 6410536 |
| IXGo | 47404128 | 46567560 | 45712792 | 45540512 | 45048432 | 44894136 |
| K8s_workqueue | 10681827 | 15989808 | 14192096 | 15304392 | 15033712 | 11373504 |
| Toml | 7324966 | 8696808 | 7219448 | 8047976 | 6374744 | 6273448 |
| Uber_zap | 10025000 | 16395448 | 13108456 | 15598272 | 13241272 | 12504080 |
| XGo | 18662581 | 24393568 | 20498736 | 23665728 | 19503392 | 19120968 |

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
