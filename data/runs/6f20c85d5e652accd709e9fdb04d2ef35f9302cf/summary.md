# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18037048 | 14870752 | 17107616 | 13754720 | 13454720 |
| Dustin_humanize | 4999050 | 6725192 | 5016824 | 6097616 | 4049552 | 3977056 |
| Etcdctl | 25896967 | 29839416 | 27284912 | 28883080 | 27857720 | 27444184 |
| Gorm_schema | 9421675 | 9747152 | 8952128 | 9057936 | 8679608 | 6281888 |
| IXGo | 47404128 | 46428016 | 45575840 | 45373184 | 44879904 | 44726152 |
| K8s_workqueue | 10681827 | 15864864 | 14070952 | 15163408 | 14895904 | 11230728 |
| Toml | 7324966 | 8570832 | 7096328 | 7919672 | 6246504 | 6144808 |
| Uber_zap | 10025000 | 16272264 | 12984208 | 15460800 | 13097976 | 12360080 |
| XGo | 18662581 | 24279768 | 20388968 | 23545920 | 19374952 | 18994768 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12565880 | 9493744 | 11519336 | 9281160 | 9059240 |
| Dustin_humanize | 3711728 | 4564440 | 2917072 | 4110944 | 2771744 | 2715136 |
| Etcdctl | 20251432 | 21363744 | 18875664 | 20059928 | 19380032 | 18982168 |
| Gorm_schema | 7186360 | 6829928 | 6060672 | 6306056 | 6047352 | 4438296 |
| IXGo | 37601624 | 31104648 | 30293680 | 28872936 | 28598224 | 28482080 |
| K8s_workqueue | 8105040 | 11083056 | 9334208 | 10240432 | 10094048 | 7552320 |
| Toml | 5573864 | 5992440 | 4571808 | 5432984 | 4356160 | 4272792 |
| Uber_zap | 7635104 | 11325816 | 8127152 | 10447984 | 8863008 | 8321368 |
| XGo | 14015312 | 17111568 | 13353968 | 15972472 | 13053792 | 12756960 |
