# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18053992 | 14887024 | 17121544 | 13772944 | 13473664 |
| Dustin_humanize | 4999050 | 6740608 | 5029296 | 6111744 | 4062856 | 3990128 |
| Etcdctl | 25896967 | 29846520 | 27289752 | 28875336 | 27842864 | 27428256 |
| Gorm_schema | 9421675 | 9761440 | 8962128 | 9068736 | 8687472 | 6294344 |
| IXGo | 47404128 | 46461672 | 45599296 | 45407040 | 44912488 | 44760936 |
| K8s_workqueue | 10681827 | 15879000 | 14082392 | 15172240 | 14899552 | 11242016 |
| Toml | 7324966 | 8586032 | 7108568 | 7930584 | 6257328 | 6156304 |
| Uber_zap | 10025000 | 16285920 | 12998536 | 15466584 | 13108392 | 12370552 |
| XGo | 18662581 | 24283752 | 20389416 | 23539008 | 19365984 | 18985496 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12579248 | 9506584 | 11531904 | 9292320 | 9070608 |
| Dustin_humanize | 3711728 | 4578360 | 2928168 | 4124144 | 2781528 | 2725168 |
| Etcdctl | 20251432 | 21370576 | 18881776 | 20066560 | 19381984 | 18985328 |
| Gorm_schema | 7186360 | 6842992 | 6070416 | 6317744 | 6057104 | 4448416 |
| IXGo | 37601624 | 31086912 | 30271352 | 28852936 | 28573896 | 28459888 |
| K8s_workqueue | 8105040 | 11096928 | 9345936 | 10253904 | 10104384 | 7565608 |
| Toml | 5573864 | 6005992 | 4582848 | 5445840 | 4366184 | 4283176 |
| Uber_zap | 7635104 | 11338936 | 8140640 | 10460496 | 8874872 | 8334216 |
| XGo | 14015312 | 17120952 | 13361208 | 15980544 | 13058048 | 12760272 |
