# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18464144 | 15211376 | 17240664 | 13811760 | 13517976 |
| Dustin_humanize | 4999050 | 6995592 | 5245680 | 6302416 | 4228512 | 4154816 |
| Etcdctl | 25896967 | 30439160 | 27829816 | 29038080 | 28012336 | 27601016 |
| Gorm_schema | 9421675 | 10075064 | 9266008 | 9286064 | 8907920 | 6471000 |
| IXGo | 47404128 | 47125352 | 46271344 | 45695632 | 45205536 | 45075760 |
| K8s_workqueue | 10681827 | 16295776 | 14456336 | 15261704 | 14987840 | 11276272 |
| Toml | 7324966 | 8837232 | 7344464 | 8111472 | 6439832 | 6338464 |
| Uber_zap | 10025000 | 16707920 | 13316896 | 15594936 | 13162544 | 12421616 |
| XGo | 18662581 | 24941816 | 20925528 | 23769904 | 19551920 | 19175664 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12809288 | 9658640 | 11748248 | 9437808 | 9217824 |
| Dustin_humanize | 3711728 | 4756576 | 3071496 | 4288488 | 2929152 | 2871592 |
| Etcdctl | 20251432 | 21688560 | 19154336 | 20301392 | 19628984 | 19232144 |
| Gorm_schema | 7186360 | 7045176 | 6264024 | 6504808 | 6246728 | 4605824 |
| IXGo | 37601624 | 31299528 | 30490056 | 29221392 | 28947664 | 28839832 |
| K8s_workqueue | 8105040 | 11353832 | 9563464 | 10456448 | 10307784 | 7722696 |
| Toml | 5573864 | 6168368 | 4733688 | 5596272 | 4527824 | 4444456 |
| Uber_zap | 7635104 | 11593264 | 8297824 | 10688768 | 9039936 | 8495200 |
| XGo | 14015312 | 17529440 | 13665584 | 16311104 | 13354680 | 13058104 |
