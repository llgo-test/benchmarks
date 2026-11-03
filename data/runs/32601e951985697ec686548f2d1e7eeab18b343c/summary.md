# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 17354272 | 14205664 | 17130224 | 13521832 | 13382896 |
| Dustin_humanize | 4999050 | 6647136 | 4953056 | 6162488 | 4064840 | 4009776 |
| Etcdctl | 25896967 | 29073488 | 26549440 | 29069360 | 27958528 | 27680056 |
| Gorm_schema | 9421675 | 9647520 | 8858976 | 9210600 | 8811440 | 6381000 |
| IXGo | 47404128 | 45490472 | 44536568 | 46267280 | 45514552 | 45380776 |
| K8s_workqueue | 10681827 | 15219744 | 13448392 | 15122960 | 14795704 | 11121640 |
| Toml | 7324966 | 8490112 | 7011928 | 8077080 | 6332288 | 6261104 |
| Uber_zap | 10025000 | 15597960 | 12335480 | 15431344 | 12444216 | 12282256 |
| XGo | 18662581 | 23554888 | 19688800 | 23746128 | 19308272 | 19126160 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12506328 | 9451616 | 11579144 | 9203544 | 9078632 |
| Dustin_humanize | 3711728 | 4560256 | 2925960 | 4120968 | 2771920 | 2723256 |
| Etcdctl | 20251432 | 21279512 | 18823560 | 20161912 | 19435200 | 19134232 |
| Gorm_schema | 7186360 | 6830088 | 6068728 | 6345792 | 6073920 | 4468512 |
| IXGo | 37601624 | 30954104 | 30036472 | 29330672 | 28882008 | 28743072 |
| K8s_workqueue | 8105040 | 11018408 | 9291952 | 10285984 | 10107088 | 7591888 |
| Toml | 5573864 | 5988832 | 4566288 | 5490656 | 4380008 | 4317664 |
| Uber_zap | 7635104 | 11236608 | 8061096 | 10472224 | 8494088 | 8346192 |
| XGo | 14015312 | 17035944 | 13301528 | 16061552 | 13004456 | 12842632 |
