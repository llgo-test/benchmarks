# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18032072 | 14865040 | 17173856 | 13797600 | 13496640 |
| Dustin_humanize | 4999050 | 6711440 | 5005200 | 6116016 | 4061232 | 3989688 |
| Etcdctl | 25896967 | 29839864 | 27280064 | 29055864 | 28036216 | 27617312 |
| Gorm_schema | 9421675 | 9738784 | 8941704 | 9106248 | 8729896 | 6316616 |
| IXGo | 47404128 | 46595320 | 45744256 | 45739440 | 45231104 | 45049384 |
| K8s_workqueue | 10681827 | 15856704 | 14058272 | 15250656 | 14982408 | 11282208 |
| Toml | 7324966 | 8556256 | 7079448 | 7960856 | 6268136 | 6167000 |
| Uber_zap | 10025000 | 16260672 | 12967320 | 15564464 | 13177096 | 12430608 |
| XGo | 18662581 | 24268104 | 20370880 | 23721312 | 19510320 | 19133200 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12569288 | 9496192 | 11467976 | 9231712 | 9006560 |
| Dustin_humanize | 3711728 | 4560024 | 2913920 | 4100528 | 2764032 | 2707392 |
| Etcdctl | 20251432 | 21369584 | 18878368 | 20063632 | 19389136 | 18985672 |
| Gorm_schema | 7186360 | 6829432 | 6058592 | 6299160 | 6041280 | 4431664 |
| IXGo | 37601624 | 31283560 | 30468336 | 29038888 | 28764288 | 28607376 |
| K8s_workqueue | 8105040 | 11083048 | 9330448 | 10229160 | 10083696 | 7538760 |
| Toml | 5573864 | 5987280 | 4564984 | 5422720 | 4343472 | 4259080 |
| Uber_zap | 7635104 | 11322952 | 8118664 | 10437448 | 8852072 | 8307984 |
| XGo | 14015312 | 17112416 | 13350440 | 15953640 | 13032304 | 12732888 |
