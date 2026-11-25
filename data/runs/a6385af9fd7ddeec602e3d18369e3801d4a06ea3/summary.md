# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18514832 | 15246296 | 17301136 | 13847848 | 13553808 |
| Dustin_humanize | 4999050 | 7040904 | 5273072 | 6350712 | 4254312 | 4180792 |
| Etcdctl | 25896967 | 30496736 | 27885096 | 29132128 | 28085592 | 27674744 |
| Gorm_schema | 9421675 | 10122888 | 9309448 | 9350384 | 8964184 | 6504488 |
| IXGo | 47404128 | 47314216 | 46470648 | 45969760 | 45467184 | 45329096 |
| K8s_workqueue | 10681827 | 16344320 | 14501232 | 15321736 | 15043824 | 11312072 |
| Toml | 7324966 | 8883184 | 7373864 | 8158256 | 6466520 | 6364392 |
| Uber_zap | 10025000 | 16757128 | 13352968 | 15656360 | 13202824 | 12460424 |
| XGo | 18662581 | 25002040 | 20972136 | 23834032 | 19591424 | 19217160 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12843960 | 9679864 | 11795376 | 9465672 | 9244856 |
| Dustin_humanize | 3711728 | 4789040 | 3088672 | 4326368 | 2947936 | 2890096 |
| Etcdctl | 20251432 | 21722568 | 19185032 | 20364904 | 19682048 | 19285728 |
| Gorm_schema | 7186360 | 7078872 | 6293328 | 6548560 | 6285984 | 4627464 |
| IXGo | 37601624 | 31261424 | 30451064 | 29280456 | 29003344 | 28896176 |
| K8s_workqueue | 8105040 | 11388536 | 9593536 | 10505616 | 10354216 | 7750288 |
| Toml | 5573864 | 6201056 | 4752120 | 5633360 | 4548640 | 4464648 |
| Uber_zap | 7635104 | 11627768 | 8320848 | 10736608 | 9071616 | 8525712 |
| XGo | 14015312 | 17569128 | 13692040 | 16368776 | 13395232 | 13097704 |
