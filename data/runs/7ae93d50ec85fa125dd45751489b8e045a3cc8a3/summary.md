# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18517616 | 15248992 | 17292712 | 13842632 | 13549712 |
| Dustin_humanize | 4999050 | 7042112 | 5274408 | 6347696 | 4251448 | 4177520 |
| Etcdctl | 25896967 | 30498912 | 27886808 | 29097072 | 28065528 | 27655000 |
| Gorm_schema | 9421675 | 10123408 | 9309616 | 9343616 | 8959376 | 6499968 |
| IXGo | 47404128 | 47310976 | 46461088 | 45954432 | 45453072 | 45313160 |
| K8s_workqueue | 10681827 | 16346280 | 14502512 | 15314464 | 15034672 | 11306144 |
| Toml | 7324966 | 8884048 | 7374704 | 8157760 | 6464256 | 6362744 |
| Uber_zap | 10025000 | 16758720 | 13353400 | 15647496 | 13195336 | 12452928 |
| XGo | 18662581 | 25001008 | 20969760 | 23823504 | 19583400 | 19208224 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12844728 | 9680088 | 11781288 | 9456648 | 9236296 |
| Dustin_humanize | 3711728 | 4789032 | 3088616 | 4318840 | 2944600 | 2887032 |
| Etcdctl | 20251432 | 21724392 | 19185208 | 20333560 | 19657424 | 19261072 |
| Gorm_schema | 7186360 | 7078952 | 6292744 | 6538064 | 6276288 | 4622024 |
| IXGo | 37601624 | 31259240 | 30448952 | 29249504 | 28973000 | 28866040 |
| K8s_workqueue | 8105040 | 11389456 | 9593656 | 10489656 | 10337816 | 7740968 |
| Toml | 5573864 | 6200824 | 4751488 | 5626584 | 4542936 | 4459136 |
| Uber_zap | 7635104 | 11628464 | 8319664 | 10721256 | 9059272 | 8513976 |
| XGo | 14015312 | 17567432 | 13689272 | 16344520 | 13374328 | 13077632 |
