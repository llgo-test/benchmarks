# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18308528 | 15099184 | 17079128 | 13689832 | 13395672 |
| Dustin_humanize | 4999050 | 6934920 | 5197304 | 6244448 | 4184072 | 4112184 |
| Etcdctl | 25896967 | 30194120 | 27607848 | 28800224 | 27773792 | 27363168 |
| Gorm_schema | 9421675 | 9982144 | 9179416 | 9200736 | 8820704 | 6414160 |
| IXGo | 47404128 | 46718176 | 45850488 | 45302024 | 44805080 | 44666328 |
| K8s_workqueue | 10681827 | 16151600 | 14343832 | 15131304 | 14855936 | 11190872 |
| Toml | 7324966 | 8786328 | 7285272 | 8061608 | 6382672 | 6283344 |
| Uber_zap | 10025000 | 16553752 | 13217088 | 15459616 | 13059056 | 12327024 |
| XGo | 18662581 | 24614536 | 20647696 | 23465696 | 19291112 | 18913584 |

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
