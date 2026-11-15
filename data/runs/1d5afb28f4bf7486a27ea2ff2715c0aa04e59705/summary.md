# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18176392 | 14995600 | 17336112 | 13940552 | 13639448 |
| Dustin_humanize | 4999050 | 6875896 | 5157048 | 6260296 | 4195104 | 4122320 |
| Etcdctl | 25896967 | 29974968 | 27405176 | 29073632 | 28048224 | 27630832 |
| Gorm_schema | 9421675 | 9898448 | 9097608 | 9224688 | 8844016 | 6430808 |
| IXGo | 47404128 | 46611432 | 45750696 | 45633360 | 45141720 | 44995296 |
| K8s_workqueue | 10681827 | 16028904 | 14224912 | 15370792 | 15103424 | 11420896 |
| Toml | 7324966 | 8720408 | 7237880 | 8083704 | 6402264 | 6300552 |
| Uber_zap | 10025000 | 16431200 | 13125360 | 15664216 | 13295680 | 12555112 |
| XGo | 18662581 | 24425752 | 20521000 | 23736864 | 19559416 | 19176224 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12694224 | 9608416 | 11656968 | 9375920 | 9153496 |
| Dustin_humanize | 3711728 | 4706768 | 3049488 | 4242080 | 2893864 | 2837304 |
| Etcdctl | 20251432 | 21492232 | 18992536 | 20159784 | 19482944 | 19085448 |
| Gorm_schema | 7186360 | 6973424 | 6199568 | 6437616 | 6177736 | 4560888 |
| IXGo | 37601624 | 31221544 | 30404872 | 28947520 | 28671976 | 28555312 |
| K8s_workqueue | 8105040 | 11240024 | 9482048 | 10375040 | 10226272 | 7674168 |
| Toml | 5573864 | 6133736 | 4705392 | 5564352 | 4483016 | 4399808 |
| Uber_zap | 7635104 | 11478680 | 8263192 | 10575240 | 8983360 | 8440856 |
| XGo | 14015312 | 17258320 | 13487544 | 16086808 | 13165736 | 12866208 |
