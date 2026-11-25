# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18512496 | 15243864 | 17293144 | 13842680 | 13549432 |
| Dustin_humanize | 4999050 | 7037208 | 5270032 | 6347368 | 4251032 | 4177288 |
| Etcdctl | 25896967 | 30495264 | 27881880 | 29096088 | 28064912 | 27654712 |
| Gorm_schema | 9421675 | 10119320 | 9305336 | 9343296 | 8958984 | 6499640 |
| IXGo | 47404128 | 47308072 | 46456384 | 45957048 | 45451496 | 45312824 |
| K8s_workqueue | 10681827 | 16341992 | 14497712 | 15314048 | 15034616 | 11305696 |
| Toml | 7324966 | 8879264 | 7369560 | 8157432 | 6463712 | 6362392 |
| Uber_zap | 10025000 | 16754912 | 13349352 | 15646832 | 13195112 | 12452808 |
| XGo | 18662581 | 24996560 | 20964952 | 23823160 | 19582376 | 19206736 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12844216 | 9679576 | 11781072 | 9456432 | 9236088 |
| Dustin_humanize | 3711728 | 4788520 | 3088104 | 4318640 | 2944416 | 2886816 |
| Etcdctl | 20251432 | 21723832 | 19184680 | 20333368 | 19657176 | 19260864 |
| Gorm_schema | 7186360 | 7078424 | 6292200 | 6537864 | 6276088 | 4621808 |
| IXGo | 37601624 | 31258712 | 30448408 | 29249288 | 28972792 | 28865840 |
| K8s_workqueue | 8105040 | 11388960 | 9593112 | 10489440 | 10337624 | 7740736 |
| Toml | 5573864 | 6200296 | 4750976 | 5626384 | 4542720 | 4458944 |
| Uber_zap | 7635104 | 11627936 | 8319128 | 10721048 | 9059088 | 8513760 |
| XGo | 14015312 | 17566888 | 13688744 | 16344328 | 13374128 | 13077416 |
