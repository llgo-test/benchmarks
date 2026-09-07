# LLGo binary-size CI
All values are ELF file sizes in bytes, collected by Bent `benchsize`.

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635492 | 12885752 | 10566312 | 12173320 | 10339696 | 10227800 |
| Dustin_humanize | 4999034 | 4685216 | 3376480 | 4356312 | 3280776 | 3237744 |
| Etcdctl | 25896983 | 21728208 | 20477936 | 20825712 | 20475024 | 20172464 |
| Gorm_schema | 9421683 | 7042456 | 6440576 | 6662000 | 6492856 | 5175944 |
| IXGo | 41505755 | 29763288 | 29133128 | 28724024 | 28438976 | 28301736 |
| K8s_workqueue | 10681819 | 11321488 | 10626664 | 10782568 | 10690528 | 8652888 |
| Toml | 7324958 | 6154008 | 5036504 | 5777064 | 4918680 | 4863144 |
| Uber_zap | 10024992 | 11595360 | 9278488 | 11033032 | 9520032 | 9384840 |
| XGo | 18662581 | 17640872 | 15500808 | 16834696 | 16541352 | 16433416 |
