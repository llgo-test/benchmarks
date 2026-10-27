# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 27478792 | 25085048 | 30249480 | 24347240 | 24184528 |
| Dustin_humanize | 4999050 | 10695600 | 9349080 | 10364480 | 6970320 | 6902808 |
| Etcdctl | 25896967 | 46758048 | 45453720 | 51071312 | 49088840 | 48870480 |
| Gorm_schema | 9421675 | 15163568 | 14536272 | 15157568 | 14494912 | 10660880 |
| IXGo | 47404128 | 76551736 | 75829056 | 85081376 | 83511272 | 83426728 |
| K8s_workqueue | 10681827 | 23629008 | 22900240 | 26221400 | 25521152 | 19850640 |
| Toml | 7324966 | 13349232 | 12198368 | 13410048 | 10468136 | 10381632 |
| Uber_zap | 10025000 | 24400768 | 21999624 | 26819384 | 21979520 | 21789760 |
| XGo | 18662581 | 37227312 | 34999296 | 41737920 | 40254488 | 40170456 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 13011048 | 10617456 | 12238656 | 10337656 | 10224144 |
| Dustin_humanize | 3711728 | 4765120 | 3418856 | 4424136 | 3313944 | 3269696 |
| Etcdctl | 20251432 | 21871216 | 20574768 | 20922496 | 20518704 | 20222968 |
| Gorm_schema | 7186360 | 7124040 | 6496752 | 6727928 | 6544128 | 5188744 |
| IXGo | 37601624 | 31619368 | 30903768 | 30234904 | 29919048 | 29783784 |
| K8s_workqueue | 8105040 | 11473328 | 10744624 | 10901776 | 10798448 | 8692984 |
| Toml | 5573864 | 6217960 | 5067304 | 5817104 | 4929672 | 4873304 |
| Uber_zap | 7635104 | 11718360 | 9317288 | 11120720 | 9540392 | 9403832 |
| XGo | 14015312 | 17860848 | 15636200 | 17070432 | 16738744 | 16632488 |
