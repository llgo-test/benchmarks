# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18139248 | 14972184 | 17268216 | 13889904 | 13587800 |
| Dustin_humanize | 4999050 | 6852448 | 5141264 | 6229248 | 4178224 | 4105392 |
| Etcdctl | 25896967 | 29957736 | 27399864 | 29005368 | 27971448 | 27555536 |
| Gorm_schema | 9421675 | 9871976 | 9072424 | 9186288 | 8805248 | 6408864 |
| IXGo | 47404128 | 46562416 | 45706128 | 45532504 | 45046184 | 44893304 |
| K8s_workqueue | 10681827 | 15988832 | 14191312 | 15303272 | 15031792 | 11372024 |
| Toml | 7324966 | 8696192 | 7219056 | 8047464 | 6373536 | 6272600 |
| Uber_zap | 10025000 | 16395024 | 13107176 | 15597368 | 13239408 | 12502944 |
| XGo | 18662581 | 24390296 | 20496224 | 23662552 | 19500112 | 19117368 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12663344 | 9590320 | 11630968 | 9358920 | 9137080 |
| Dustin_humanize | 3711728 | 4688912 | 3038952 | 4226312 | 2885304 | 2828880 |
| Etcdctl | 20251432 | 21480072 | 18990712 | 20152768 | 19468584 | 19071208 |
| Gorm_schema | 7186360 | 6952672 | 6180176 | 6418352 | 6158168 | 4549976 |
| IXGo | 37601624 | 31193056 | 30377864 | 28929040 | 28652104 | 28537616 |
| K8s_workqueue | 8105040 | 11205344 | 9454000 | 10344560 | 10194128 | 7656272 |
| Toml | 5573864 | 6115352 | 4692416 | 5548528 | 4471720 | 4388712 |
| Uber_zap | 7635104 | 11447208 | 8249408 | 10549240 | 8964680 | 8425152 |
| XGo | 14015312 | 17227552 | 13467712 | 16063520 | 13148912 | 12850928 |
