# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18032144 | 14865144 | 17038904 | 13691392 | 13393592 |
| Dustin_humanize | 4999050 | 6714768 | 5008520 | 6080776 | 4038872 | 3968592 |
| Etcdctl | 25896967 | 29817288 | 27258104 | 28848616 | 27828336 | 27412888 |
| Gorm_schema | 9421675 | 9741224 | 8943912 | 9051624 | 8675752 | 6279744 |
| IXGo | 47404128 | 46402656 | 45550272 | 45278520 | 44777328 | 44644264 |
| K8s_workqueue | 10681827 | 15858888 | 14059976 | 15146952 | 14878840 | 11214264 |
| Toml | 7324966 | 8559440 | 7082696 | 7896880 | 6225072 | 6123928 |
| Uber_zap | 10025000 | 16262176 | 12968672 | 15445888 | 13080320 | 12343160 |
| XGo | 18662581 | 24269888 | 20372232 | 23514600 | 19342376 | 18962856 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12569608 | 9496576 | 11458392 | 9222592 | 8998048 |
| Dustin_humanize | 3711728 | 4563352 | 2917248 | 4102064 | 2765304 | 2709032 |
| Etcdctl | 20251432 | 21349328 | 18858144 | 20023320 | 19348424 | 18944992 |
| Gorm_schema | 7186360 | 6831928 | 6061056 | 6299416 | 6041744 | 4431976 |
| IXGo | 37601624 | 31092208 | 30281152 | 28814616 | 28539864 | 28418840 |
| K8s_workqueue | 8105040 | 11084984 | 9332352 | 10223968 | 10077952 | 7533800 |
| Toml | 5573864 | 5990176 | 4567880 | 5420128 | 4343480 | 4259216 |
| Uber_zap | 7635104 | 11324856 | 8120584 | 10429624 | 8844720 | 8300880 |
| XGo | 14015312 | 17113856 | 13351880 | 15931080 | 13016176 | 12716688 |
