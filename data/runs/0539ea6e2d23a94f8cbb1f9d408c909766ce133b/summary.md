# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18176648 | 14995704 | 17336568 | 13940576 | 13639744 |
| Dustin_humanize | 4999050 | 6875896 | 5157048 | 6260296 | 4195104 | 4122320 |
| Etcdctl | 25896967 | 29975480 | 27405448 | 29073384 | 28048152 | 27630504 |
| Gorm_schema | 9421675 | 9898456 | 9097600 | 9224688 | 8844016 | 6430808 |
| IXGo | 47404128 | 46608616 | 45751760 | 45633904 | 45141872 | 44992560 |
| K8s_workqueue | 10681827 | 16028784 | 14224744 | 15370744 | 15103256 | 11420720 |
| Toml | 7324966 | 8720472 | 7237936 | 8083704 | 6402224 | 6300536 |
| Uber_zap | 10025000 | 16431136 | 13125592 | 15664200 | 13295392 | 12555000 |
| XGo | 18662581 | 24425680 | 20521008 | 23736776 | 19559400 | 19176328 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12694224 | 9608416 | 11656968 | 9375920 | 9153496 |
| Dustin_humanize | 3711728 | 4706768 | 3049488 | 4242080 | 2893864 | 2837304 |
| Etcdctl | 20251432 | 21492232 | 18992536 | 20159784 | 19482944 | 19085448 |
| Gorm_schema | 7186360 | 6973424 | 6199568 | 6437616 | 6177736 | 4560888 |
| IXGo | 37601624 | 31221544 | 30404872 | 28947520 | 28671976 | 28555312 |
| K8s_workqueue | 8105040 | 11240024 | 9482048 | 10375040 | 10226288 | 7674168 |
| Toml | 5573864 | 6133736 | 4705392 | 5564352 | 4483016 | 4399808 |
| Uber_zap | 7635104 | 11478680 | 8263192 | 10575240 | 8983360 | 8440856 |
| XGo | 14015312 | 17258320 | 13487544 | 16086808 | 13165736 | 12866208 |
