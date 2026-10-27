# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 17391088 | 14243152 | 17170384 | 13575104 | 13436256 |
| Dustin_humanize | 4999050 | 6634160 | 4939040 | 6157904 | 4071184 | 4015616 |
| Etcdctl | 25896967 | 29037184 | 26512808 | 29054816 | 27941296 | 27664336 |
| Gorm_schema | 9421675 | 9613216 | 8822528 | 9187416 | 8786368 | 6375464 |
| IXGo | 47404128 | 45458840 | 44500224 | 46202216 | 45451936 | 45328392 |
| K8s_workqueue | 10681827 | 15252856 | 13481632 | 15157808 | 14830608 | 11182496 |
| Toml | 7324966 | 8465816 | 6984640 | 8060040 | 6320664 | 6250320 |
| Uber_zap | 10025000 | 15628600 | 12363264 | 15464640 | 12495504 | 12334128 |
| XGo | 18662581 | 23545632 | 19680312 | 23741552 | 19322512 | 19140264 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12616760 | 9562352 | 11681304 | 9304840 | 9179936 |
| Dustin_humanize | 3711728 | 4575104 | 2939760 | 4137568 | 2787672 | 2738960 |
| Etcdctl | 20251432 | 21380712 | 18924096 | 20258008 | 19531176 | 19230288 |
| Gorm_schema | 7186360 | 6844960 | 6082312 | 6362024 | 6089128 | 4483408 |
| IXGo | 37601624 | 31134144 | 30215984 | 29487056 | 29038160 | 28899192 |
| K8s_workqueue | 8105040 | 11129192 | 9402216 | 10388568 | 10209600 | 7694136 |
| Toml | 5573864 | 6003176 | 4577752 | 5506624 | 4393144 | 4330904 |
| Uber_zap | 7635104 | 11347440 | 8169048 | 10574800 | 8596056 | 8448168 |
| XGo | 14015312 | 17138680 | 13403704 | 16158264 | 13100656 | 12938880 |
