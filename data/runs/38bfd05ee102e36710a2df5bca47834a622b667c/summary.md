# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 27486312 | 25090936 | 30254512 | 24348968 | 24185776 |
| Dustin_humanize | 4999050 | 10698192 | 9350776 | 10365880 | 6971760 | 6904296 |
| Etcdctl | 25896967 | 46774080 | 45468672 | 51072632 | 49097376 | 48877944 |
| Gorm_schema | 9421675 | 15167504 | 14540008 | 15162368 | 14500216 | 10665224 |
| IXGo | 47404128 | 76572144 | 75849032 | 85104192 | 83526136 | 83440856 |
| K8s_workqueue | 10681827 | 23636112 | 22906608 | 26226888 | 25523976 | 19852480 |
| Toml | 7324966 | 13353896 | 12201176 | 13412256 | 10470304 | 10383792 |
| Uber_zap | 10025000 | 24408856 | 22005840 | 26825144 | 21980864 | 21790640 |
| XGo | 18662581 | 37240008 | 35007832 | 41746064 | 40262280 | 40177560 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 13017616 | 10622392 | 12240800 | 10338904 | 10225328 |
| Dustin_humanize | 3711728 | 4766832 | 3419672 | 4424888 | 3314472 | 3270272 |
| Etcdctl | 20251432 | 21887624 | 20590096 | 20933144 | 20530336 | 20234536 |
| Gorm_schema | 7186360 | 7126936 | 6499456 | 6730184 | 6546400 | 5190512 |
| IXGo | 37601624 | 31634680 | 30918648 | 30245648 | 29928416 | 29793024 |
| K8s_workqueue | 8105040 | 11478808 | 10749368 | 10904352 | 10800544 | 8694456 |
| Toml | 5573864 | 6221976 | 5069464 | 5818400 | 4930536 | 4874152 |
| Uber_zap | 7635104 | 11724328 | 9321384 | 11123152 | 9541960 | 9405336 |
| XGo | 14015312 | 17875288 | 15646472 | 17079032 | 16747272 | 16640880 |
