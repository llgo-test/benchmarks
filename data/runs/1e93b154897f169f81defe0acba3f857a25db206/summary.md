# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 27486280 | 25090912 | 30254512 | 24348976 | 24185784 |
| Dustin_humanize | 4999050 | 10698152 | 9350752 | 10365880 | 6971768 | 6904304 |
| Etcdctl | 25896967 | 46774056 | 45468632 | 51072640 | 49097376 | 48877944 |
| Gorm_schema | 9421675 | 15167472 | 14539984 | 15162376 | 14500224 | 10665224 |
| IXGo | 47404128 | 76572128 | 75849008 | 85104200 | 83526152 | 83440864 |
| K8s_workqueue | 10681827 | 23636088 | 22906592 | 26226896 | 25523976 | 19852488 |
| Toml | 7324966 | 13353872 | 12201152 | 13412264 | 10470312 | 10383792 |
| Uber_zap | 10025000 | 24408824 | 22005824 | 26825152 | 21980864 | 21790648 |
| XGo | 18662581 | 37239976 | 35007792 | 41746072 | 40262288 | 40177568 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 13017616 | 10622392 | 12240800 | 10338904 | 10225328 |
| Dustin_humanize | 3711728 | 4766816 | 3419672 | 4424888 | 3314472 | 3270272 |
| Etcdctl | 20251432 | 21887624 | 20590096 | 20933144 | 20530336 | 20234536 |
| Gorm_schema | 7186360 | 7126936 | 6499456 | 6730184 | 6546400 | 5190512 |
| IXGo | 37601624 | 31634680 | 30918648 | 30245648 | 29928416 | 29793024 |
| K8s_workqueue | 8105040 | 11478808 | 10749368 | 10904352 | 10800544 | 8694456 |
| Toml | 5573864 | 6221976 | 5069464 | 5818400 | 4930536 | 4874152 |
| Uber_zap | 7635104 | 11724328 | 9321400 | 11123152 | 9541960 | 9405336 |
| XGo | 14015312 | 17875288 | 15646472 | 17079032 | 16747272 | 16640880 |
