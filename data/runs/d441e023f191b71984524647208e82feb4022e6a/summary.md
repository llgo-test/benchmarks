# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18511496 | 15230480 | 17135456 | 13700744 | 13411312 |
| Dustin_humanize | 4999050 | 7001656 | 5225376 | 6247368 | 4160840 | 4085752 |
| Etcdctl | 25896967 | 30532472 | 27918600 | 28916736 | 27873464 | 27464992 |
| Gorm_schema | 9421675 | 10100448 | 9284712 | 9256616 | 8873056 | 6415496 |
| IXGo | 47404128 | 47420848 | 46571352 | 45774872 | 45264000 | 45136928 |
| K8s_workqueue | 10681827 | 16324048 | 14478160 | 15166992 | 14893152 | 11186456 |
| Toml | 7324966 | 8848352 | 7333360 | 8023776 | 6344624 | 6243400 |
| Uber_zap | 10025000 | 16732824 | 13320848 | 15500152 | 13059280 | 12325216 |
| XGo | 18662581 | 25020616 | 20978936 | 23636720 | 19414232 | 19042368 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12807064 | 9630824 | 11701688 | 9372632 | 9153024 |
| Dustin_humanize | 3711728 | 4723336 | 3014456 | 4233656 | 2854520 | 2796168 |
| Etcdctl | 20251432 | 21728952 | 19187584 | 20259240 | 19580000 | 19184696 |
| Gorm_schema | 7186360 | 7027504 | 6239584 | 6468568 | 6207248 | 4543608 |
| IXGo | 37601624 | 31282408 | 30469520 | 29183912 | 28906096 | 28800352 |
| K8s_workqueue | 8105040 | 11344488 | 9546376 | 10407920 | 10256904 | 7658032 |
| Toml | 5573864 | 6141176 | 4687136 | 5535528 | 4454584 | 4370288 |
| Uber_zap | 7635104 | 11581432 | 8267936 | 10641760 | 8978744 | 8435816 |
| XGo | 14015312 | 17558912 | 13671584 | 16273488 | 13302056 | 13005416 |
