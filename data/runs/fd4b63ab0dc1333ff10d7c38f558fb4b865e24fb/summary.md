# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18308656 | 15099184 | 17079224 | 13689704 | 13395744 |
| Dustin_humanize | 4999050 | 6934712 | 5197320 | 6244440 | 4184072 | 4112184 |
| Etcdctl | 25896967 | 30193992 | 27607672 | 28800000 | 27773968 | 27363024 |
| Gorm_schema | 9421675 | 9982184 | 9179264 | 9200736 | 8820704 | 6414160 |
| IXGo | 47404128 | 46717120 | 45854392 | 45304440 | 44804088 | 44667928 |
| K8s_workqueue | 10681827 | 16151968 | 14343448 | 15131376 | 14856184 | 11190464 |
| Toml | 7324966 | 8785920 | 7285048 | 8061784 | 6382704 | 6283216 |
| Uber_zap | 10025000 | 16553560 | 13217136 | 15459616 | 13058920 | 12326936 |
| XGo | 18662581 | 24613968 | 20647336 | 23465408 | 19291144 | 18913360 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12701784 | 9593368 | 11641672 | 9361328 | 9140432 |
| Dustin_humanize | 3711728 | 4715504 | 3043560 | 4246840 | 2898928 | 2842336 |
| Etcdctl | 20251432 | 21526968 | 19015432 | 20141952 | 19464440 | 19067896 |
| Gorm_schema | 7186360 | 6981384 | 6206624 | 6443144 | 6183224 | 4565472 |
| IXGo | 37601624 | 31001256 | 30182936 | 28932344 | 28654936 | 28538840 |
| K8s_workqueue | 8105040 | 11253896 | 9493544 | 10362760 | 10212128 | 7662008 |
| Toml | 5573864 | 6139304 | 4696552 | 5567528 | 4487728 | 4404704 |
| Uber_zap | 7635104 | 11492208 | 8250696 | 10593936 | 8967752 | 8427504 |
| XGo | 14015312 | 17285192 | 13468256 | 16075080 | 13152832 | 12854384 |
