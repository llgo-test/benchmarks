# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18029864 | 14865608 | 17091784 | 13746736 | 13445864 |
| Dustin_humanize | 4999050 | 6725312 | 5017048 | 6096128 | 4050752 | 3978304 |
| Etcdctl | 25896967 | 29820448 | 27265800 | 28847664 | 27819336 | 27405712 |
| Gorm_schema | 9421675 | 9743080 | 8946728 | 9051056 | 8672696 | 6279968 |
| IXGo | 47404128 | 46375240 | 45521512 | 45284776 | 44798360 | 44641152 |
| K8s_workqueue | 10681827 | 15859896 | 14066664 | 15152440 | 14883120 | 11225864 |
| Toml | 7324966 | 8568736 | 7094840 | 7913504 | 6243232 | 6142048 |
| Uber_zap | 10025000 | 16266264 | 12981584 | 15447208 | 13092312 | 12355280 |
| XGo | 18662581 | 24257384 | 20367768 | 23516256 | 19344240 | 18964376 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12568592 | 9499144 | 11521056 | 9284064 | 9062328 |
| Dustin_humanize | 3711728 | 4567680 | 2920696 | 4113232 | 2773736 | 2717400 |
| Etcdctl | 20251432 | 21359920 | 18874272 | 20055664 | 19373712 | 18977032 |
| Gorm_schema | 7186360 | 6832272 | 6062912 | 6306872 | 6048792 | 4440152 |
| IXGo | 37601624 | 31076296 | 30263832 | 28842048 | 28565520 | 28451640 |
| K8s_workqueue | 8105040 | 11086256 | 9338464 | 10242944 | 10096096 | 7557336 |
| Toml | 5573864 | 5995384 | 4575408 | 5435008 | 4358432 | 4275328 |
| Uber_zap | 7635104 | 11328280 | 8133104 | 10449600 | 8866704 | 8325936 |
| XGo | 14015312 | 17110280 | 13353720 | 15969656 | 13049816 | 12752024 |
