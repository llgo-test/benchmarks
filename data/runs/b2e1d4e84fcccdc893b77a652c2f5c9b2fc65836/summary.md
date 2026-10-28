# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 17463368 | 14314776 | 17227248 | 13619320 | 13478760 |
| Dustin_humanize | 4999050 | 6659864 | 4963640 | 6173744 | 4074376 | 4019096 |
| Etcdctl | 25896967 | 29171824 | 26648552 | 29156480 | 28044616 | 27768944 |
| Gorm_schema | 9421675 | 9660472 | 8869664 | 9222096 | 8822968 | 6390608 |
| IXGo | 47404128 | 45666456 | 44710000 | 46409048 | 45652264 | 45528120 |
| K8s_workqueue | 10681827 | 15328064 | 13556832 | 15219272 | 14892256 | 11218168 |
| Toml | 7324966 | 8503320 | 7022528 | 8088568 | 6341464 | 6270720 |
| Uber_zap | 10025000 | 15706944 | 12442912 | 15528784 | 12542016 | 12379736 |
| XGo | 18662581 | 23655792 | 19789672 | 23835176 | 19397312 | 19217696 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12614744 | 9559928 | 11677224 | 9301968 | 9177128 |
| Dustin_humanize | 3711728 | 4572872 | 2936624 | 4132824 | 2782080 | 2733336 |
| Etcdctl | 20251432 | 21377296 | 18921224 | 20249920 | 19523608 | 19222728 |
| Gorm_schema | 7186360 | 6842904 | 6079720 | 6357848 | 6085912 | 4478664 |
| IXGo | 37601624 | 31129128 | 30211552 | 29478048 | 29029648 | 28890728 |
| K8s_workqueue | 8105040 | 11126824 | 9400288 | 10384064 | 10205672 | 7690440 |
| Toml | 5573864 | 6001456 | 4576984 | 5502488 | 4390104 | 4327824 |
| Uber_zap | 7635104 | 11345040 | 8167640 | 10570360 | 8592640 | 8444760 |
| XGo | 14015312 | 17136408 | 13401904 | 16153280 | 13096240 | 12934472 |
