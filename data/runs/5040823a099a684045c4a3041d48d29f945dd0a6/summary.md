# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18308632 | 15099224 | 17079416 | 13690168 | 13395808 |
| Dustin_humanize | 4999050 | 6934912 | 5197304 | 6244448 | 4184072 | 4112184 |
| Etcdctl | 25896967 | 30194208 | 27607848 | 28800376 | 27773704 | 27363200 |
| Gorm_schema | 9421675 | 9982136 | 9179416 | 9200736 | 8820704 | 6414136 |
| IXGo | 47404128 | 46718360 | 45852024 | 45304840 | 44805392 | 44665488 |
| K8s_workqueue | 10681827 | 16152096 | 14343424 | 15131440 | 14856008 | 11190664 |
| Toml | 7324966 | 8786352 | 7285360 | 8061544 | 6382720 | 6283392 |
| Uber_zap | 10025000 | 16553736 | 13217328 | 15459648 | 13059008 | 12326864 |
| XGo | 18662581 | 24614672 | 20648168 | 23465600 | 19291296 | 18913448 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12701784 | 9593384 | 11641672 | 9361328 | 9140432 |
| Dustin_humanize | 3711728 | 4715520 | 3043560 | 4246840 | 2898928 | 2842336 |
| Etcdctl | 20251432 | 21526984 | 19015432 | 20141952 | 19464440 | 19067896 |
| Gorm_schema | 7186360 | 6981384 | 6206624 | 6443144 | 6183224 | 4565472 |
| IXGo | 37601624 | 31001256 | 30182936 | 28932344 | 28654936 | 28538840 |
| K8s_workqueue | 8105040 | 11253896 | 9493544 | 10362776 | 10212128 | 7662008 |
| Toml | 5573864 | 6139320 | 4696552 | 5567528 | 4487792 | 4404704 |
| Uber_zap | 7635104 | 11492208 | 8250696 | 10593936 | 8967752 | 8427504 |
| XGo | 14015312 | 17285192 | 13468256 | 16075080 | 13152832 | 12854384 |
