# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18464360 | 15211264 | 17239264 | 13811744 | 13517568 |
| Dustin_humanize | 4999050 | 6996224 | 5245856 | 6302672 | 4228584 | 4154832 |
| Etcdctl | 25896967 | 30439208 | 27829840 | 29038504 | 28012560 | 27602832 |
| Gorm_schema | 9421675 | 10075056 | 9266224 | 9286048 | 8908304 | 6470984 |
| IXGo | 47404128 | 47124136 | 46267792 | 45701944 | 45209320 | 45075392 |
| K8s_workqueue | 10681827 | 16296408 | 14456944 | 15261800 | 14987440 | 11276432 |
| Toml | 7324966 | 8837584 | 7344784 | 8111360 | 6439872 | 6339088 |
| Uber_zap | 10025000 | 16708216 | 13316704 | 15595000 | 13162688 | 12421768 |
| XGo | 18662581 | 24941368 | 20925768 | 23769760 | 19551112 | 19175568 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12809704 | 9659056 | 11748360 | 9437904 | 9217920 |
| Dustin_humanize | 3711728 | 4756976 | 3071616 | 4288656 | 2929248 | 2871736 |
| Etcdctl | 20251432 | 21688976 | 19154736 | 20301544 | 19629072 | 19232304 |
| Gorm_schema | 7186360 | 7045576 | 6264480 | 6504904 | 6246888 | 4605920 |
| IXGo | 37601624 | 31299960 | 30490496 | 29221576 | 28947840 | 28839944 |
| K8s_workqueue | 8105040 | 11354248 | 9563888 | 10456520 | 10307880 | 7722784 |
| Toml | 5573864 | 6168808 | 4734104 | 5596360 | 4527992 | 4444616 |
| Uber_zap | 7635104 | 11593680 | 8298232 | 10688872 | 9040032 | 8495288 |
| XGo | 14015312 | 17529880 | 13666056 | 16311208 | 13354776 | 13058264 |
