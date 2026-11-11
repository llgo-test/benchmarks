# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18028296 | 14861064 | 17130824 | 13782592 | 13482520 |
| Dustin_humanize | 4999050 | 6741624 | 5030168 | 6117944 | 4066992 | 3993824 |
| Etcdctl | 25896967 | 29845272 | 27287592 | 28904320 | 27872656 | 27457880 |
| Gorm_schema | 9421675 | 9761352 | 8961992 | 9077544 | 8697120 | 6300232 |
| IXGo | 47404128 | 46458248 | 45600320 | 45438680 | 44948712 | 44796560 |
| K8s_workqueue | 10681827 | 15877536 | 14080376 | 15197544 | 14928432 | 11264984 |
| Toml | 7324966 | 8585320 | 7108208 | 7937368 | 6262696 | 6161488 |
| Uber_zap | 10025000 | 16283784 | 12996736 | 15489752 | 13131904 | 12393808 |
| XGo | 18662581 | 24282384 | 20387600 | 23567304 | 19393728 | 19010752 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12551936 | 9479120 | 11486168 | 9246704 | 9024960 |
| Dustin_humanize | 3711728 | 4577968 | 2927928 | 4115000 | 2773864 | 2717424 |
| Etcdctl | 20251432 | 21367408 | 18878416 | 20042216 | 19357984 | 18961616 |
| Gorm_schema | 7186360 | 6841496 | 6069016 | 6307664 | 6047584 | 4439072 |
| IXGo | 37601624 | 31082384 | 30267208 | 28821896 | 28544512 | 28430080 |
| K8s_workqueue | 8105040 | 11093984 | 9342768 | 10232752 | 10084016 | 7544584 |
| Toml | 5573864 | 6004424 | 4581536 | 5436288 | 4359504 | 4276912 |
| Uber_zap | 7635104 | 11335688 | 8138128 | 10437040 | 8852896 | 8312424 |
| XGo | 14015312 | 17117080 | 13357496 | 15958208 | 13036736 | 12738544 |
