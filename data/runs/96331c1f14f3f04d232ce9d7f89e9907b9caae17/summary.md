# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18029136 | 14861408 | 17158408 | 13780608 | 13479256 |
| Dustin_humanize | 4999050 | 6741856 | 5030328 | 6118160 | 4067504 | 3994488 |
| Etcdctl | 25896967 | 29847536 | 27290352 | 28896800 | 27865696 | 27450880 |
| Gorm_schema | 9421675 | 9761840 | 8962136 | 9076128 | 8695984 | 6299544 |
| IXGo | 47404128 | 46456280 | 45600776 | 45428432 | 44938760 | 44787696 |
| K8s_workqueue | 10681827 | 15877704 | 14081104 | 15193592 | 14922328 | 11262112 |
| Toml | 7324966 | 8585592 | 7108344 | 7937376 | 6263952 | 6162624 |
| Uber_zap | 10025000 | 16284632 | 12997216 | 15487800 | 13129824 | 12393136 |
| XGo | 18662581 | 24282520 | 20387592 | 23555592 | 19392720 | 19010184 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12552496 | 9479472 | 11520624 | 9248592 | 9026720 |
| Dustin_humanize | 3711728 | 4578064 | 2927944 | 4115792 | 2774784 | 2718344 |
| Etcdctl | 20251432 | 21369568 | 18880208 | 20042600 | 19358400 | 18961008 |
| Gorm_schema | 7186360 | 6841832 | 6069288 | 6307816 | 6047648 | 4439536 |
| IXGo | 37601624 | 31082464 | 30267288 | 28818760 | 28541808 | 28427320 |
| K8s_workqueue | 8105040 | 11094480 | 9343136 | 10234248 | 10083816 | 7545752 |
| Toml | 5573864 | 6004520 | 4581584 | 5438168 | 4361392 | 4278400 |
| Uber_zap | 7635104 | 11336360 | 8138576 | 10438912 | 8854080 | 8314600 |
| XGo | 14015312 | 17117048 | 13357240 | 15953384 | 13038760 | 12740728 |
