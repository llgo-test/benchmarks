# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18517704 | 15249032 | 17293432 | 13842904 | 13549528 |
| Dustin_humanize | 4999050 | 7042392 | 5274304 | 6347944 | 4251592 | 4177720 |
| Etcdctl | 25896967 | 30500488 | 27885904 | 29096184 | 28064888 | 27655008 |
| Gorm_schema | 9421675 | 10123616 | 9309784 | 9343576 | 8959256 | 6500216 |
| IXGo | 47404128 | 47311280 | 46462136 | 45958312 | 45450528 | 45312008 |
| K8s_workqueue | 10681827 | 16347168 | 14503400 | 15314440 | 15035144 | 11306096 |
| Toml | 7324966 | 8883952 | 7374792 | 8157704 | 6464176 | 6362824 |
| Uber_zap | 10025000 | 16759280 | 13353336 | 15647392 | 13195600 | 12453200 |
| XGo | 18662581 | 25001240 | 20969872 | 23823680 | 19583376 | 19208416 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12844968 | 9680336 | 11781288 | 9456648 | 9236296 |
| Dustin_humanize | 3711728 | 4789272 | 3088824 | 4318840 | 2944616 | 2887032 |
| Etcdctl | 20251432 | 21724616 | 19185424 | 20333560 | 19657424 | 19261072 |
| Gorm_schema | 7186360 | 7079176 | 6292984 | 6538064 | 6276288 | 4622024 |
| IXGo | 37601624 | 31259464 | 30449152 | 29249504 | 28973000 | 28866056 |
| K8s_workqueue | 8105040 | 11389712 | 9593856 | 10489656 | 10337832 | 7740968 |
| Toml | 5573864 | 6201040 | 4751720 | 5626584 | 4542936 | 4459136 |
| Uber_zap | 7635104 | 11628688 | 8319864 | 10721256 | 9059288 | 8513976 |
| XGo | 14015312 | 17567632 | 13689496 | 16344520 | 13374328 | 13077648 |
