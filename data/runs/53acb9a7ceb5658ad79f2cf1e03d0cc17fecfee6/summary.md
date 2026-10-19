# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 17626296 | 15139928 | 17561608 | 14444496 | 14315656 |
| Dustin_humanize | 4999050 | 6766520 | 5360184 | 6379680 | 4551568 | 4500680 |
| Etcdctl | 25896967 | 29367880 | 28016112 | 29533544 | 28743328 | 28470488 |
| Gorm_schema | 9421675 | 9827592 | 9171728 | 9481992 | 9168608 | 7015168 |
| IXGo | 47404128 | 45458928 | 44703672 | 46320232 | 45695424 | 45578776 |
| K8s_workqueue | 10681827 | 15471720 | 14712824 | 15530496 | 15277080 | 12043648 |
| Toml | 7324966 | 8618040 | 7410264 | 8293056 | 6789096 | 6723864 |
| Uber_zap | 10025000 | 15880008 | 13395264 | 15877112 | 13307488 | 13156992 |
| XGo | 18662581 | 23883624 | 20919120 | 24235168 | 20559328 | 20394672 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12951080 | 10555856 | 12173848 | 10272048 | 10158440 |
| Dustin_humanize | 3711728 | 4750072 | 3402896 | 4407784 | 3297352 | 3253120 |
| Etcdctl | 20251432 | 21807848 | 20510344 | 20853376 | 20450520 | 20154752 |
| Gorm_schema | 7186360 | 7106736 | 6479192 | 6709520 | 6525736 | 5169848 |
| IXGo | 37601624 | 31513144 | 30797048 | 30124080 | 29806832 | 29671472 |
| K8s_workqueue | 8105040 | 11409328 | 10679888 | 10834568 | 10730752 | 8624672 |
| Toml | 5573864 | 6204856 | 5052384 | 5800952 | 4913088 | 4856720 |
| Uber_zap | 7635104 | 11658608 | 9255672 | 11057128 | 9475952 | 9339312 |
| XGo | 14015312 | 17550864 | 14713320 | 16754744 | 14445832 | 14300448 |
