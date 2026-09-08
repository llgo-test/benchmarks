# LLGo binary-size CI
All values are ELF file sizes in bytes, collected by Bent `benchsize`.

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635492 | 12885800 | 10566320 | 12173336 | 10339696 | 10227816 |
| Dustin_humanize | 4999034 | 4685248 | 3376504 | 4356328 | 3280824 | 3237792 |
| Etcdctl | 25896983 | 21728240 | 20477976 | 20825728 | 20475040 | 20172464 |
| Gorm_schema | 9421683 | 7042488 | 6440624 | 6662016 | 6492872 | 5175944 |
| IXGo | 41505755 | 29763336 | 29133152 | 28724040 | 28438976 | 28301752 |
| K8s_workqueue | 10681819 | 11321520 | 10626704 | 10782584 | 10690528 | 8652904 |
| Toml | 7324958 | 6154040 | 5036552 | 5777080 | 4918696 | 4863160 |
| Uber_zap | 10024992 | 11595440 | 9278504 | 11033048 | 9520048 | 9384840 |
| XGo | 18662581 | 17640904 | 15500840 | 16834696 | 16541352 | 16433432 |
