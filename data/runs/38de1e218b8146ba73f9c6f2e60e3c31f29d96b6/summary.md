# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18033960 | 14866488 | 17175832 | 13798224 | 13498536 |
| Dustin_humanize | 4999050 | 6716056 | 5010008 | 6119744 | 4065024 | 3992976 |
| Etcdctl | 25896967 | 29818968 | 27259416 | 29031648 | 28012296 | 27593616 |
| Gorm_schema | 9421675 | 9742560 | 8945288 | 9109416 | 8732704 | 6320224 |
| IXGo | 47404128 | 46402688 | 45552128 | 45533160 | 45026464 | 44884544 |
| K8s_workqueue | 10681827 | 15859840 | 14061416 | 15253208 | 14984728 | 11285072 |
| Toml | 7324966 | 8560768 | 7084024 | 7964456 | 6271872 | 6170544 |
| Uber_zap | 10025000 | 16263504 | 12970240 | 15566736 | 13179568 | 12433440 |
| XGo | 18662581 | 24271184 | 20373648 | 23722816 | 19513096 | 19135768 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12569416 | 9496384 | 11467896 | 9231600 | 9006480 |
| Dustin_humanize | 3711728 | 4563160 | 2917072 | 4102736 | 2766176 | 2709600 |
| Etcdctl | 20251432 | 21349152 | 18857920 | 20041040 | 19366528 | 18963144 |
| Gorm_schema | 7186360 | 6831752 | 6060864 | 6300424 | 6042608 | 4433040 |
| IXGo | 37601624 | 31092016 | 30280960 | 28838776 | 28564008 | 28442496 |
| K8s_workqueue | 8105040 | 11084792 | 9332160 | 10230040 | 10084576 | 7539720 |
| Toml | 5573864 | 5989984 | 4567688 | 5424736 | 4345344 | 4260984 |
| Uber_zap | 7635104 | 11324664 | 8120392 | 10438312 | 8852840 | 8308944 |
| XGo | 14015312 | 17113664 | 13351672 | 15954072 | 13032640 | 12733336 |
