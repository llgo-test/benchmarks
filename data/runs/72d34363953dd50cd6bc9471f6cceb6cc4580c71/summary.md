# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18464200 | 15211560 | 17240280 | 13811856 | 13517920 |
| Dustin_humanize | 4999050 | 6995720 | 5245800 | 6302416 | 4228512 | 4154800 |
| Etcdctl | 25896967 | 30438912 | 27829552 | 29038096 | 28012800 | 27600888 |
| Gorm_schema | 9421675 | 10075136 | 9266064 | 9286064 | 8907920 | 6471000 |
| IXGo | 47404128 | 47125024 | 46271096 | 45696888 | 45210312 | 45075984 |
| K8s_workqueue | 10681827 | 16296144 | 14456672 | 15261616 | 14987440 | 11276368 |
| Toml | 7324966 | 8837376 | 7344320 | 8111520 | 6439808 | 6338616 |
| Uber_zap | 10025000 | 16708064 | 13317032 | 15594936 | 13162672 | 12421584 |
| XGo | 18662581 | 24941552 | 20925592 | 23769960 | 19551888 | 19175648 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12809304 | 9658640 | 11748248 | 9437808 | 9217824 |
| Dustin_humanize | 3711728 | 4756576 | 3071496 | 4288488 | 2929152 | 2871592 |
| Etcdctl | 20251432 | 21688560 | 19154336 | 20301392 | 19628984 | 19232144 |
| Gorm_schema | 7186360 | 7045176 | 6264024 | 6504808 | 6246728 | 4605824 |
| IXGo | 37601624 | 31299528 | 30490056 | 29221376 | 28947664 | 28839832 |
| K8s_workqueue | 8105040 | 11353832 | 9563448 | 10456448 | 10307784 | 7722696 |
| Toml | 5573864 | 6168368 | 4733688 | 5596272 | 4527824 | 4444456 |
| Uber_zap | 7635104 | 11593264 | 8297824 | 10688768 | 9039936 | 8495200 |
| XGo | 14015312 | 17529440 | 13665584 | 16311104 | 13354680 | 13058104 |
