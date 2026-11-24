# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18517576 | 15248920 | 17292336 | 13842792 | 13549776 |
| Dustin_humanize | 4999050 | 7042104 | 5274416 | 6347696 | 4251440 | 4177432 |
| Etcdctl | 25896967 | 30498944 | 27886672 | 29097208 | 28065304 | 27654912 |
| Gorm_schema | 9421675 | 10123400 | 9309616 | 9343616 | 8959376 | 6499968 |
| IXGo | 47404128 | 47311736 | 46461256 | 45959816 | 45450680 | 45317736 |
| K8s_workqueue | 10681827 | 16346120 | 14502344 | 15314232 | 15034664 | 11306400 |
| Toml | 7324966 | 8883912 | 7374448 | 8157760 | 6464272 | 6362656 |
| Uber_zap | 10025000 | 16758976 | 13353304 | 15647360 | 13195248 | 12453136 |
| XGo | 18662581 | 25000992 | 20969936 | 23823136 | 19583360 | 19207808 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12844728 | 9680088 | 11781288 | 9456648 | 9236296 |
| Dustin_humanize | 3711728 | 4789032 | 3088616 | 4318840 | 2944600 | 2886968 |
| Etcdctl | 20251432 | 21724392 | 19185208 | 20333560 | 19657424 | 19261072 |
| Gorm_schema | 7186360 | 7078952 | 6292744 | 6538064 | 6276288 | 4622024 |
| IXGo | 37601624 | 31259240 | 30448952 | 29249504 | 28973000 | 28866040 |
| K8s_workqueue | 8105040 | 11389456 | 9593656 | 10489656 | 10337816 | 7740968 |
| Toml | 5573864 | 6200824 | 4751488 | 5626584 | 4542936 | 4459136 |
| Uber_zap | 7635104 | 11628464 | 8319664 | 10721256 | 9059272 | 8513976 |
| XGo | 14015312 | 17567432 | 13689272 | 16344520 | 13374328 | 13077632 |
