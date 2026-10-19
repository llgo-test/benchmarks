# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 17692928 | 15206008 | 17627152 | 14511336 | 14382304 |
| Dustin_humanize | 4999050 | 6783312 | 5377176 | 6396848 | 4568728 | 4517824 |
| Etcdctl | 25896967 | 29448144 | 28095288 | 29613568 | 28822456 | 28549880 |
| Gorm_schema | 9421675 | 9848080 | 9192056 | 9502832 | 9189248 | 7036072 |
| IXGo | 47404128 | 45581880 | 44827656 | 46442424 | 45814608 | 45698296 |
| K8s_workqueue | 10681827 | 15540928 | 14782448 | 15600216 | 15346656 | 12113440 |
| Toml | 7324966 | 8635400 | 7427184 | 8310376 | 6806616 | 6741272 |
| Uber_zap | 10025000 | 15946120 | 13461104 | 15942000 | 13373336 | 13222632 |
| XGo | 18662581 | 24207784 | 21885848 | 24558448 | 23941040 | 23841712 |

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
| Uber_zap | 7635104 | 11724328 | 9321400 | 11123152 | 9541960 | 9405336 |
| XGo | 14015312 | 17875288 | 15646472 | 17079032 | 16747272 | 16640880 |
