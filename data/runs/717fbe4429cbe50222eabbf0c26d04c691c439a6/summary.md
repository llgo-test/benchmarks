# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18027360 | 14860032 | 17102080 | 13755592 | 13455496 |
| Dustin_humanize | 4999050 | 6740920 | 5029280 | 6110344 | 4062224 | 3989504 |
| Etcdctl | 25896967 | 29844280 | 27287080 | 28872608 | 27840400 | 27425840 |
| Gorm_schema | 9421675 | 9760592 | 8961160 | 9068144 | 8687168 | 6293384 |
| IXGo | 47404128 | 46456344 | 45597520 | 45402240 | 44907440 | 44757400 |
| K8s_workqueue | 10681827 | 15876192 | 14079632 | 15170280 | 14899424 | 11239664 |
| Toml | 7324966 | 8584968 | 7107976 | 7928584 | 6255904 | 6154560 |
| Uber_zap | 10025000 | 16283368 | 12996368 | 15462224 | 13106240 | 12368048 |
| XGo | 18662581 | 24281264 | 20386960 | 23535544 | 19362728 | 18982312 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12552080 | 9479280 | 11506896 | 9266872 | 9045040 |
| Dustin_humanize | 3711728 | 4578128 | 2928088 | 4123536 | 2781336 | 2724960 |
| Etcdctl | 20251432 | 21367584 | 18878592 | 20067912 | 19383712 | 18987088 |
| Gorm_schema | 7186360 | 6841640 | 6069176 | 6317560 | 6057168 | 4447920 |
| IXGo | 37601624 | 31082544 | 30267352 | 28855168 | 28576432 | 28462488 |
| K8s_workqueue | 8105040 | 11094144 | 9342912 | 10253808 | 10104952 | 7563992 |
| Toml | 5573864 | 6004584 | 4581680 | 5445024 | 4365832 | 4282936 |
| Uber_zap | 7635104 | 11335832 | 8138272 | 10458992 | 8873592 | 8333144 |
| XGo | 14015312 | 17117240 | 13357640 | 15980176 | 13057568 | 12759600 |
