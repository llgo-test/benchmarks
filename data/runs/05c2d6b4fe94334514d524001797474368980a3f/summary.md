# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 17386712 | 14238720 | 17124000 | 13539224 | 13399240 |
| Dustin_humanize | 4999050 | 6629696 | 4934656 | 6137864 | 4059328 | 4004168 |
| Etcdctl | 25896967 | 29032248 | 26508352 | 28985480 | 27871880 | 27594552 |
| Gorm_schema | 9421675 | 9608480 | 8818312 | 9160944 | 8759136 | 6355240 |
| IXGo | 47404128 | 45452080 | 44495096 | 46123072 | 45362824 | 45242800 |
| K8s_workqueue | 10681827 | 15248968 | 13477512 | 15115720 | 14789424 | 11148400 |
| Toml | 7324966 | 8461624 | 6980560 | 8034744 | 6298976 | 6228576 |
| Uber_zap | 10025000 | 15623640 | 12358688 | 15422872 | 12458552 | 12297768 |
| XGo | 18662581 | 23541416 | 19676752 | 23683216 | 19269136 | 19088736 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12614696 | 9560400 | 11671736 | 9296432 | 9171624 |
| Dustin_humanize | 3711728 | 4573008 | 2937808 | 4133200 | 2786672 | 2737912 |
| Etcdctl | 20251432 | 21378472 | 18922016 | 20244752 | 19517528 | 19216456 |
| Gorm_schema | 7186360 | 6842928 | 6080296 | 6356672 | 6083672 | 4478664 |
| IXGo | 37601624 | 31131520 | 30213440 | 29473080 | 29023784 | 28884880 |
| K8s_workqueue | 8105040 | 11127224 | 9400200 | 10380560 | 10201552 | 7687264 |
| Toml | 5573864 | 6001088 | 4575712 | 5501448 | 4388568 | 4326376 |
| Uber_zap | 7635104 | 11345408 | 8167048 | 10567032 | 8589064 | 8441240 |
| XGo | 14015312 | 17136616 | 13401656 | 16148080 | 13091480 | 12929736 |
