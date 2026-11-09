# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18037720 | 14870592 | 17107264 | 13755080 | 13454552 |
| Dustin_humanize | 4999050 | 6725352 | 5016920 | 6097960 | 4049800 | 3977272 |
| Etcdctl | 25896967 | 29839296 | 27284696 | 28883648 | 27857128 | 27443744 |
| Gorm_schema | 9421675 | 9747152 | 8952176 | 9058104 | 8679912 | 6282296 |
| IXGo | 47404128 | 46426208 | 45575984 | 45373296 | 44881328 | 44726176 |
| K8s_workqueue | 10681827 | 15864640 | 14070952 | 15164120 | 14896568 | 11231304 |
| Toml | 7324966 | 8571136 | 7096432 | 7919984 | 6246408 | 6145008 |
| Uber_zap | 10025000 | 16272424 | 12984424 | 15460984 | 13098496 | 12360360 |
| XGo | 18662581 | 24280072 | 20389032 | 23547000 | 19374256 | 18994648 |

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
| Uber_zap | 7635104 | 11325816 | 8127136 | 10447984 | 8863008 | 8321368 |
| XGo | 14015312 | 17111568 | 13353968 | 15972472 | 13053792 | 12756960 |
