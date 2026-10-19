# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 17626328 | 15139944 | 17561616 | 14444744 | 14315432 |
| Dustin_humanize | 4999050 | 6766520 | 5360200 | 6379680 | 4551568 | 4500680 |
| Etcdctl | 25896967 | 29368344 | 28016176 | 29533800 | 28743360 | 28470248 |
| Gorm_schema | 9421675 | 9827600 | 9171728 | 9481992 | 9168608 | 7015168 |
| IXGo | 47404128 | 45461520 | 44704832 | 46321984 | 45695016 | 45579336 |
| K8s_workqueue | 10681827 | 15471728 | 14712600 | 15530536 | 15277344 | 12043664 |
| Toml | 7324966 | 8618064 | 7410320 | 8293168 | 6789240 | 6723752 |
| Uber_zap | 10025000 | 15879856 | 13395328 | 15877048 | 13307592 | 13157000 |
| XGo | 18662581 | 23883272 | 20919032 | 24235536 | 20559088 | 20394664 |

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
