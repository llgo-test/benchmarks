# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18464384 | 15211760 | 17239344 | 13811568 | 13517656 |
| Dustin_humanize | 4999050 | 6996216 | 5245856 | 6302672 | 4228584 | 4154832 |
| Etcdctl | 25896967 | 30439112 | 27829728 | 29038712 | 28012544 | 27603024 |
| Gorm_schema | 9421675 | 10075064 | 9266216 | 9286048 | 8908304 | 6470984 |
| IXGo | 47404128 | 47123096 | 46268272 | 45700360 | 45209360 | 45077408 |
| K8s_workqueue | 10681827 | 16296352 | 14457000 | 15261576 | 14987688 | 11276376 |
| Toml | 7324966 | 8837520 | 7344760 | 8111520 | 6439744 | 6339048 |
| Uber_zap | 10025000 | 16708256 | 13317016 | 15594824 | 13162496 | 12421960 |
| XGo | 18662581 | 24941440 | 20925600 | 23769608 | 19550960 | 19175680 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12809704 | 9659056 | 11748360 | 9437904 | 9217920 |
| Dustin_humanize | 3711728 | 4756976 | 3071616 | 4288656 | 2929248 | 2871736 |
| Etcdctl | 20251432 | 21688976 | 19154736 | 20301544 | 19629072 | 19232304 |
| Gorm_schema | 7186360 | 7045576 | 6264480 | 6504904 | 6246888 | 4605920 |
| IXGo | 37601624 | 31299960 | 30490496 | 29221576 | 28947840 | 28839944 |
| K8s_workqueue | 8105040 | 11354248 | 9563888 | 10456536 | 10307864 | 7722784 |
| Toml | 5573864 | 6168808 | 4734104 | 5596360 | 4527992 | 4444616 |
| Uber_zap | 7635104 | 11593680 | 8298232 | 10688872 | 9040032 | 8495288 |
| XGo | 14015312 | 17529880 | 13666056 | 16311208 | 13354776 | 13058264 |
