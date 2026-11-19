# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18464128 | 15211640 | 17240528 | 13812248 | 13517856 |
| Dustin_humanize | 4999050 | 6995720 | 5245784 | 6302416 | 4228512 | 4154808 |
| Etcdctl | 25896967 | 30439040 | 27829808 | 29038232 | 28012512 | 27600872 |
| Gorm_schema | 9421675 | 10075152 | 9266056 | 9286064 | 8907920 | 6471000 |
| IXGo | 47404128 | 47122072 | 46270056 | 45697360 | 45209824 | 45076576 |
| K8s_workqueue | 10681827 | 16295912 | 14456424 | 15261744 | 14987528 | 11276280 |
| Toml | 7324966 | 8837312 | 7344544 | 8111456 | 6439768 | 6338704 |
| Uber_zap | 10025000 | 16708096 | 13316880 | 15595168 | 13162648 | 12421512 |
| XGo | 18662581 | 24941488 | 20925784 | 23770168 | 19551680 | 19175456 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12809304 | 9658640 | 11748248 | 9437808 | 9217824 |
| Dustin_humanize | 3711728 | 4756576 | 3071496 | 4288488 | 2929152 | 2871592 |
| Etcdctl | 20251432 | 21688560 | 19154336 | 20301392 | 19628984 | 19232144 |
| Gorm_schema | 7186360 | 7045176 | 6264024 | 6504808 | 6246728 | 4605824 |
| IXGo | 37601624 | 31299528 | 30490056 | 29221392 | 28947664 | 28839832 |
| K8s_workqueue | 8105040 | 11353832 | 9563464 | 10456448 | 10307768 | 7722696 |
| Toml | 5573864 | 6168368 | 4733688 | 5596272 | 4527824 | 4444456 |
| Uber_zap | 7635104 | 11593264 | 8297824 | 10688768 | 9039936 | 8495200 |
| XGo | 14015312 | 17529440 | 13665584 | 16311104 | 13354680 | 13058104 |
