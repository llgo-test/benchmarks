# LLGo binary-size CI
All values are ELF file sizes in bytes, collected by Bent `benchsize`.

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635492 | 12908608 | 10536512 | 12255864 | 10359992 | 10247320 |
| Dustin_humanize | 4999034 | 4733752 | 3399760 | 4404096 | 3292776 | 3249056 |
| Etcdctl | 25896983 | 21830976 | 20545736 | 20998616 | 20629904 | 20334184 |
| Gorm_schema | 9421683 | 7094992 | 6477640 | 6717312 | 6545368 | 5184448 |
| IXGo | 47404136 | 31496392 | 30791296 | 30177304 | 29878888 | 29743488 |
| K8s_workqueue | 10681819 | 11410104 | 10694272 | 10896576 | 10803648 | 8699008 |
| Toml | 7324958 | 6196280 | 5056296 | 5811424 | 4928432 | 4872336 |
| Uber_zap | 10024992 | 11682072 | 9301600 | 11145504 | 9577824 | 9441856 |
| XGo | 18662581 | 17858288 | 15662504 | 17106336 | 16799384 | 16693272 |
