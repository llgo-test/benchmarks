# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18157320 | 14984768 | 17322776 | 13932488 | 13629984 |
| Dustin_humanize | 4999050 | 6868768 | 5152504 | 6255536 | 4192664 | 4120096 |
| Etcdctl | 25896967 | 29971480 | 27412368 | 29075272 | 28045856 | 27630712 |
| Gorm_schema | 9421675 | 9888480 | 9087720 | 9217416 | 8837240 | 6427040 |
| IXGo | 47404128 | 46591192 | 45735784 | 45629608 | 45139600 | 44985608 |
| K8s_workqueue | 10681827 | 16006592 | 14208200 | 15353592 | 15083136 | 11411032 |
| Toml | 7324966 | 8713112 | 7230432 | 8079104 | 6397848 | 6296608 |
| Uber_zap | 10025000 | 16413168 | 13120088 | 15651352 | 13285448 | 12546680 |
| XGo | 18662581 | 24415056 | 20516104 | 23730752 | 19556864 | 19172040 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12675488 | 9597464 | 11640512 | 9365232 | 9142624 |
| Dustin_humanize | 3711728 | 4700592 | 3045864 | 4237136 | 2891416 | 2834864 |
| Etcdctl | 20251432 | 21485616 | 18995280 | 20152656 | 19474888 | 19077528 |
| Gorm_schema | 7186360 | 6963960 | 6190640 | 6429240 | 6169568 | 4556400 |
| IXGo | 37601624 | 31207056 | 30391472 | 28935712 | 28659552 | 28544584 |
| K8s_workqueue | 8105040 | 11217560 | 9464928 | 10354456 | 10205136 | 7662312 |
| Toml | 5573864 | 6127240 | 4699392 | 5559344 | 4478352 | 4395024 |
| Uber_zap | 7635104 | 11459656 | 8256992 | 10557424 | 8970256 | 8430024 |
| XGo | 14015312 | 17240840 | 13476496 | 16071440 | 13153824 | 12854608 |
