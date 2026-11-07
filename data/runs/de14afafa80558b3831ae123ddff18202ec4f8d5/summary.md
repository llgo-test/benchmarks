# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18032296 | 14865256 | 17173944 | 13797632 | 13496512 |
| Dustin_humanize | 4999050 | 6711440 | 5005200 | 6116024 | 4061232 | 3989688 |
| Etcdctl | 25896967 | 29840232 | 27280344 | 29055160 | 28035608 | 27617080 |
| Gorm_schema | 9421675 | 9738784 | 8941712 | 9106232 | 8729896 | 6316616 |
| IXGo | 47404128 | 46595304 | 45742880 | 45738752 | 45232960 | 45054448 |
| K8s_workqueue | 10681827 | 15856832 | 14058312 | 15250528 | 14982288 | 11282104 |
| Toml | 7324966 | 8556256 | 7079608 | 7960888 | 6268048 | 6167104 |
| Uber_zap | 10025000 | 16260792 | 12967376 | 15564056 | 13177208 | 12430488 |
| XGo | 18662581 | 24268464 | 20370640 | 23721400 | 19510696 | 19133440 |

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
