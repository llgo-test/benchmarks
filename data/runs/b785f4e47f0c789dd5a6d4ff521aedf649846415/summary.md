# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 17386832 | 14238872 | 17124152 | 13539248 | 13399328 |
| Dustin_humanize | 4999050 | 6629704 | 4934656 | 6137864 | 4059328 | 4004168 |
| Etcdctl | 25896967 | 29032152 | 26508208 | 28985560 | 27871920 | 27594472 |
| Gorm_schema | 9421675 | 9608496 | 8818312 | 9160944 | 8759136 | 6355240 |
| IXGo | 47404128 | 45451760 | 44496496 | 46122080 | 45365104 | 45241232 |
| K8s_workqueue | 10681827 | 15249000 | 13477432 | 15115952 | 14789248 | 11148336 |
| Toml | 7324966 | 8461536 | 6980536 | 8034744 | 6298952 | 6228704 |
| Uber_zap | 10025000 | 15623632 | 12358704 | 15422888 | 12458656 | 12297600 |
| XGo | 18662581 | 23541616 | 19676728 | 23683136 | 19269016 | 19088712 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12614696 | 9560400 | 11671736 | 9296432 | 9171624 |
| Dustin_humanize | 3711728 | 4573008 | 2937808 | 4133200 | 2786672 | 2737912 |
| Etcdctl | 20251432 | 21378472 | 18922016 | 20244752 | 19517528 | 19216456 |
| Gorm_schema | 7186360 | 6842928 | 6080296 | 6356672 | 6083672 | 4478664 |
| IXGo | 37601624 | 31131496 | 30213440 | 29473080 | 29023784 | 28884880 |
| K8s_workqueue | 8105040 | 11127224 | 9400200 | 10380560 | 10201552 | 7687264 |
| Toml | 5573864 | 6001088 | 4575712 | 5501448 | 4388568 | 4326376 |
| Uber_zap | 7635104 | 11345408 | 8167048 | 10567032 | 8589064 | 8441240 |
| XGo | 14015312 | 17136616 | 13401656 | 16148080 | 13091480 | 12929736 |
