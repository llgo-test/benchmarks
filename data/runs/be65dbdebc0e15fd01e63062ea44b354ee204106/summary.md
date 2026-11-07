# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18029912 | 14863000 | 17172560 | 13795184 | 13494224 |
| Dustin_humanize | 4999050 | 6708944 | 5002768 | 6113752 | 4058432 | 3987376 |
| Etcdctl | 25896967 | 29838528 | 27278480 | 29052600 | 28032776 | 27614624 |
| Gorm_schema | 9421675 | 9736528 | 8939456 | 9103904 | 8727512 | 6314056 |
| IXGo | 47404128 | 46595568 | 45740776 | 45739904 | 45230424 | 45050096 |
| K8s_workqueue | 10681827 | 15854624 | 14056072 | 15248672 | 14979928 | 11279544 |
| Toml | 7324966 | 8554088 | 7077288 | 7958472 | 6266064 | 6164400 |
| Uber_zap | 10025000 | 16258368 | 12965160 | 15562136 | 13175008 | 12428136 |
| XGo | 18662581 | 24265728 | 20368264 | 23717576 | 19508008 | 19130616 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12568816 | 9495688 | 11466992 | 9230664 | 9005600 |
| Dustin_humanize | 3711728 | 4559488 | 2913384 | 4099600 | 2762992 | 2706440 |
| Etcdctl | 20251432 | 21369016 | 18877832 | 20062624 | 19388024 | 18984672 |
| Gorm_schema | 7186360 | 6828912 | 6058056 | 6298176 | 6040192 | 4430688 |
| IXGo | 37601624 | 31283040 | 30467816 | 29037944 | 28763208 | 28606408 |
| K8s_workqueue | 8105040 | 11082512 | 9329880 | 10228128 | 10082640 | 7537784 |
| Toml | 5573864 | 5986744 | 4564464 | 5421744 | 4342392 | 4258088 |
| Uber_zap | 7635104 | 11322432 | 8118144 | 10436488 | 8850960 | 8307008 |
| XGo | 14015312 | 17111864 | 13349888 | 15952600 | 13031232 | 12731888 |
