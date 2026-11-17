# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18308328 | 15099184 | 17079416 | 13689952 | 13395816 |
| Dustin_humanize | 4999050 | 6934720 | 5197328 | 6244440 | 4184072 | 4112184 |
| Etcdctl | 25896967 | 30194024 | 27607768 | 28799968 | 27774024 | 27362960 |
| Gorm_schema | 9421675 | 9982184 | 9179264 | 9200736 | 8820704 | 6414160 |
| IXGo | 47404128 | 46718320 | 45852184 | 45301296 | 44803000 | 44664608 |
| K8s_workqueue | 10681827 | 16151544 | 14343360 | 15131160 | 14856128 | 11190536 |
| Toml | 7324966 | 8785920 | 7285152 | 8061632 | 6382816 | 6283392 |
| Uber_zap | 10025000 | 16553816 | 13217144 | 15459776 | 13059056 | 12326968 |
| XGo | 18662581 | 24614320 | 20647288 | 23465648 | 19291000 | 18913336 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12701784 | 9593368 | 11641672 | 9361328 | 9140432 |
| Dustin_humanize | 3711728 | 4715504 | 3043560 | 4246840 | 2898928 | 2842336 |
| Etcdctl | 20251432 | 21526968 | 19015432 | 20141952 | 19464440 | 19067896 |
| Gorm_schema | 7186360 | 6981384 | 6206624 | 6443144 | 6183224 | 4565472 |
| IXGo | 37601624 | 31001256 | 30182936 | 28932344 | 28654936 | 28538840 |
| K8s_workqueue | 8105040 | 11253896 | 9493544 | 10362776 | 10212128 | 7662008 |
| Toml | 5573864 | 6139304 | 4696552 | 5567528 | 4487792 | 4404704 |
| Uber_zap | 7635104 | 11492208 | 8250696 | 10593936 | 8967752 | 8427504 |
| XGo | 14015312 | 17285192 | 13468256 | 16075080 | 13152832 | 12854384 |
