# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18027168 | 14859984 | 17101984 | 13755696 | 13455736 |
| Dustin_humanize | 4999050 | 6740936 | 5029288 | 6110344 | 4062224 | 3989504 |
| Etcdctl | 25896967 | 29844192 | 27286872 | 28872584 | 27840440 | 27425432 |
| Gorm_schema | 9421675 | 9760592 | 8961160 | 9068144 | 8687160 | 6293384 |
| IXGo | 47404128 | 46455752 | 45600680 | 45404248 | 44906944 | 44758384 |
| K8s_workqueue | 10681827 | 15876440 | 14079360 | 15170280 | 14899576 | 11239568 |
| Toml | 7324966 | 8584944 | 7107808 | 7928656 | 6255832 | 6154520 |
| Uber_zap | 10025000 | 16283168 | 12996112 | 15462120 | 13106408 | 12368200 |
| XGo | 18662581 | 24281440 | 20387128 | 23535472 | 19362728 | 18982176 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12552080 | 9479280 | 11506896 | 9266872 | 9045040 |
| Dustin_humanize | 3711728 | 4578128 | 2928088 | 4123536 | 2781336 | 2724960 |
| Etcdctl | 20251432 | 21367584 | 18878592 | 20067912 | 19383712 | 18987088 |
| Gorm_schema | 7186360 | 6841640 | 6069176 | 6317560 | 6057168 | 4447920 |
| IXGo | 37601624 | 31082544 | 30267368 | 28855168 | 28576432 | 28462488 |
| K8s_workqueue | 8105040 | 11094144 | 9342912 | 10253808 | 10104952 | 7563992 |
| Toml | 5573864 | 6004584 | 4581680 | 5445024 | 4365832 | 4282936 |
| Uber_zap | 7635104 | 11335832 | 8138272 | 10458992 | 8873592 | 8333208 |
| XGo | 14015312 | 17117240 | 13357640 | 15980176 | 13057568 | 12759600 |
