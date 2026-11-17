# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18308584 | 15099032 | 17079672 | 13689672 | 13395696 |
| Dustin_humanize | 4999050 | 6934912 | 5197296 | 6244448 | 4184072 | 4112184 |
| Etcdctl | 25896967 | 30194208 | 27608112 | 28799968 | 27773776 | 27362896 |
| Gorm_schema | 9421675 | 9982136 | 9179408 | 9200736 | 8820704 | 6414160 |
| IXGo | 47404128 | 46717784 | 45853176 | 45302728 | 44803320 | 44665536 |
| K8s_workqueue | 10681827 | 16151720 | 14343848 | 15131400 | 14856280 | 11190584 |
| Toml | 7324966 | 8786416 | 7285312 | 8061608 | 6382704 | 6283336 |
| Uber_zap | 10025000 | 16553632 | 13217376 | 15459568 | 13058904 | 12326920 |
| XGo | 18662581 | 24614608 | 20648168 | 23465648 | 19291144 | 18913416 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12701784 | 9593384 | 11641672 | 9361328 | 9140432 |
| Dustin_humanize | 3711728 | 4715520 | 3043560 | 4246840 | 2898928 | 2842336 |
| Etcdctl | 20251432 | 21526984 | 19015432 | 20141952 | 19464440 | 19067896 |
| Gorm_schema | 7186360 | 6981384 | 6206624 | 6443144 | 6183224 | 4565472 |
| IXGo | 37601624 | 31001256 | 30182936 | 28932344 | 28654936 | 28538840 |
| K8s_workqueue | 8105040 | 11253896 | 9493560 | 10362776 | 10212128 | 7662008 |
| Toml | 5573864 | 6139320 | 4696552 | 5567528 | 4487792 | 4404704 |
| Uber_zap | 7635104 | 11492208 | 8250696 | 10593936 | 8967752 | 8427504 |
| XGo | 14015312 | 17285192 | 13468256 | 16075080 | 13152832 | 12854384 |
