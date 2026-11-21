# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18464280 | 15211688 | 17239328 | 13811448 | 13517760 |
| Dustin_humanize | 4999050 | 6995776 | 5245544 | 6302568 | 4228512 | 4154688 |
| Etcdctl | 25896967 | 30438896 | 27829240 | 29038888 | 28012304 | 27602216 |
| Gorm_schema | 9421675 | 10075096 | 9265944 | 9285976 | 8907968 | 6470912 |
| IXGo | 47404128 | 47120712 | 46270200 | 45698824 | 45205216 | 45076832 |
| K8s_workqueue | 10681827 | 16295840 | 14456848 | 15261840 | 14987528 | 11276856 |
| Toml | 7324966 | 8837488 | 7344400 | 8111456 | 6439736 | 6338648 |
| Uber_zap | 10025000 | 16707776 | 13316720 | 15594944 | 13162504 | 12421592 |
| XGo | 18662581 | 24940240 | 20925912 | 23770000 | 19550960 | 19175344 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12809600 | 9658952 | 11748280 | 9437824 | 9217840 |
| Dustin_humanize | 3711728 | 4756872 | 3071528 | 4288520 | 2929168 | 2871592 |
| Etcdctl | 20251432 | 21688888 | 19154648 | 20301408 | 19629000 | 19232160 |
| Gorm_schema | 7186360 | 7045472 | 6264392 | 6504824 | 6246744 | 4605840 |
| IXGo | 37601624 | 31299856 | 30490384 | 29221440 | 28947696 | 28839864 |
| K8s_workqueue | 8105040 | 11354144 | 9563792 | 10456464 | 10307800 | 7722712 |
| Toml | 5573864 | 6168688 | 4734000 | 5596288 | 4527856 | 4444472 |
| Uber_zap | 7635104 | 11593576 | 8298120 | 10688800 | 9039952 | 8495216 |
| XGo | 14015312 | 17529768 | 13665944 | 16311136 | 13354696 | 13058120 |
