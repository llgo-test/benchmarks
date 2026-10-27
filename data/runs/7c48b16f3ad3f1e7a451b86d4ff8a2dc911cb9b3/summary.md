# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 17467616 | 14318944 | 17232160 | 13622160 | 13481976 |
| Dustin_humanize | 4999050 | 6664368 | 4969456 | 6180680 | 4081056 | 4025640 |
| Etcdctl | 25896967 | 29180632 | 26656256 | 29173648 | 28061576 | 27783848 |
| Gorm_schema | 9421675 | 9664944 | 8874368 | 9228648 | 8827424 | 6396224 |
| IXGo | 47404128 | 45672648 | 44716016 | 46424800 | 45661104 | 45541000 |
| K8s_workqueue | 10681827 | 15332888 | 13561536 | 15226008 | 14897408 | 11223136 |
| Toml | 7324966 | 8507176 | 7025920 | 8093824 | 6345240 | 6274592 |
| Uber_zap | 10025000 | 15712496 | 12446960 | 15535672 | 12545728 | 12383992 |
| XGo | 18662581 | 23660376 | 19793688 | 23841768 | 19404640 | 19222864 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12616760 | 9562352 | 11681304 | 9304840 | 9179936 |
| Dustin_humanize | 3711728 | 4575104 | 2939760 | 4137568 | 2787672 | 2738960 |
| Etcdctl | 20251432 | 21380712 | 18924096 | 20258008 | 19531176 | 19230288 |
| Gorm_schema | 7186360 | 6844960 | 6082312 | 6362024 | 6089128 | 4483408 |
| IXGo | 37601624 | 31134144 | 30215984 | 29487056 | 29038160 | 28899184 |
| K8s_workqueue | 8105040 | 11129192 | 9402216 | 10388568 | 10209600 | 7694136 |
| Toml | 5573864 | 6003176 | 4577752 | 5506624 | 4393144 | 4330904 |
| Uber_zap | 7635104 | 11347440 | 8169048 | 10574800 | 8596056 | 8448168 |
| XGo | 14015312 | 17138680 | 13403704 | 16158264 | 13100656 | 12938880 |
