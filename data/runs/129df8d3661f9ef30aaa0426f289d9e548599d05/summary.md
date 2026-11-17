# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18308440 | 15099056 | 17079512 | 13689896 | 13395784 |
| Dustin_humanize | 4999050 | 6934904 | 5197304 | 6244448 | 4184064 | 4112184 |
| Etcdctl | 25896967 | 30194096 | 27608120 | 28800112 | 27773768 | 27363112 |
| Gorm_schema | 9421675 | 9982136 | 9179416 | 9200736 | 8820704 | 6414160 |
| IXGo | 47404128 | 46717800 | 45854280 | 45304608 | 44804872 | 44663752 |
| K8s_workqueue | 10681827 | 16152008 | 14343648 | 15131344 | 14855936 | 11190552 |
| Toml | 7324966 | 8786344 | 7285232 | 8061616 | 6382600 | 6283304 |
| Uber_zap | 10025000 | 16553728 | 13217264 | 15459680 | 13058976 | 12326832 |
| XGo | 18662581 | 24614792 | 20648176 | 23465152 | 19290976 | 18913328 |

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
| Uber_zap | 7635104 | 11492192 | 8250696 | 10593936 | 8967752 | 8427504 |
| XGo | 14015312 | 17285192 | 13468256 | 16075080 | 13152832 | 12854384 |
