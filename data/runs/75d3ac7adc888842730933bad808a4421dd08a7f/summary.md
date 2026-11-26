# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18475104 | 15194088 | 17264528 | 13798976 | 13508328 |
| Dustin_humanize | 4999050 | 6975104 | 5199024 | 6284256 | 4179480 | 4104952 |
| Etcdctl | 25896967 | 30503704 | 27888360 | 29132512 | 28080672 | 27674416 |
| Gorm_schema | 9421675 | 10071744 | 9257088 | 9304744 | 8920320 | 6446168 |
| IXGo | 47404128 | 47337568 | 46484760 | 46020616 | 45513288 | 45377904 |
| K8s_workqueue | 10681827 | 16299096 | 14452296 | 15276224 | 15001032 | 11263624 |
| Toml | 7324966 | 8821176 | 7306464 | 8099936 | 6408848 | 6306416 |
| Uber_zap | 10025000 | 16707216 | 13296136 | 15611504 | 13154568 | 12415056 |
| XGo | 18662581 | 24991128 | 20949728 | 23842096 | 19592568 | 19219152 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12797008 | 9620456 | 11737664 | 9398632 | 9178832 |
| Dustin_humanize | 3711728 | 4710064 | 3001496 | 4240640 | 2855936 | 2797704 |
| Etcdctl | 20251432 | 21721744 | 19180432 | 20322408 | 19638728 | 19243928 |
| Gorm_schema | 7186360 | 7014440 | 6226824 | 6479928 | 6217952 | 4549120 |
| IXGo | 37601624 | 31273464 | 30460848 | 29271560 | 28994128 | 28888072 |
| K8s_workqueue | 8105040 | 11334544 | 9536784 | 10438080 | 10287056 | 7678792 |
| Toml | 5573864 | 6128464 | 4674352 | 5555008 | 4470304 | 4386040 |
| Uber_zap | 7635104 | 11571984 | 8257712 | 10670320 | 9001456 | 8457088 |
| XGo | 14015312 | 17549592 | 13662256 | 16329592 | 13350848 | 13054432 |
