# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 17388136 | 14354824 | 17125200 | 13541880 | 13402928 |
| Dustin_humanize | 4999050 | 6629416 | 4943008 | 6136472 | 4067568 | 4011912 |
| Etcdctl | 25896967 | 29036808 | 27322008 | 28992128 | 27877960 | 27600392 |
| Gorm_schema | 9421675 | 9608112 | 8822832 | 9160224 | 8758440 | 6354432 |
| IXGo | 47404128 | 45452200 | 44498056 | 46120640 | 45375032 | 45246544 |
| K8s_workqueue | 10681827 | 15250224 | 14276344 | 15117344 | 14791672 | 11150616 |
| Toml | 7324966 | 8460216 | 6990568 | 8033088 | 6307008 | 6236336 |
| Uber_zap | 10025000 | 15625144 | 12580360 | 15424904 | 12461832 | 12300272 |
| XGo | 18662581 | 23543816 | 19788616 | 23683984 | 19272424 | 19091752 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12617528 | 9675600 | 11674344 | 9300104 | 9175328 |
| Dustin_humanize | 3711728 | 4573544 | 2946792 | 4133024 | 2791328 | 2742664 |
| Etcdctl | 20251432 | 21384408 | 19723312 | 20250880 | 19523656 | 19222704 |
| Gorm_schema | 7186360 | 6843424 | 6085800 | 6356744 | 6084064 | 4478872 |
| IXGo | 37601624 | 31134024 | 30216136 | 29476128 | 29026696 | 28887824 |
| K8s_workqueue | 8105040 | 11129816 | 10186464 | 10383048 | 10204472 | 7690424 |
| Toml | 5573864 | 6001016 | 4586568 | 5501072 | 4393488 | 4331232 |
| Uber_zap | 7635104 | 11348144 | 8384432 | 10569608 | 8592312 | 8444552 |
| XGo | 14015312 | 17140200 | 13513784 | 16150808 | 13095136 | 12933432 |
