# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18463768 | 15210792 | 17240304 | 13811744 | 13517720 |
| Dustin_humanize | 4999050 | 6994960 | 5245232 | 6302352 | 4228432 | 4154760 |
| Etcdctl | 25896967 | 30438344 | 27829056 | 29037968 | 28012496 | 27601104 |
| Gorm_schema | 9421675 | 10074584 | 9265512 | 9286016 | 8908072 | 6470968 |
| IXGo | 47404128 | 47123856 | 46270552 | 45696616 | 45207768 | 45077048 |
| K8s_workqueue | 10681827 | 16295616 | 14456016 | 15261616 | 14987440 | 11276176 |
| Toml | 7324966 | 8836984 | 7344008 | 8111448 | 6439792 | 6338704 |
| Uber_zap | 10025000 | 16707272 | 13316312 | 15595248 | 13162704 | 12421616 |
| XGo | 18662581 | 24940792 | 20925136 | 23770128 | 19551288 | 19175536 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12809304 | 9658640 | 11748248 | 9437808 | 9217824 |
| Dustin_humanize | 3711728 | 4756576 | 3071512 | 4288488 | 2929152 | 2871592 |
| Etcdctl | 20251432 | 21688576 | 19154352 | 20301392 | 19628984 | 19232144 |
| Gorm_schema | 7186360 | 7045176 | 6264024 | 6504808 | 6246728 | 4605824 |
| IXGo | 37601624 | 31299528 | 30490072 | 29221392 | 28947664 | 28839832 |
| K8s_workqueue | 8105040 | 11353832 | 9563464 | 10456448 | 10307784 | 7722696 |
| Toml | 5573864 | 6168368 | 4733688 | 5596272 | 4527824 | 4444456 |
| Uber_zap | 7635104 | 11593280 | 8297824 | 10688768 | 9039936 | 8495200 |
| XGo | 14015312 | 17529456 | 13665600 | 16311104 | 13354680 | 13058104 |
