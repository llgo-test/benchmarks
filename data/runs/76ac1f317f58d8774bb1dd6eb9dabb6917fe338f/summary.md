# LLGo binary-size CI
All values are ELF file sizes in bytes, collected by Bent `benchsize`.

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635492 | 12884632 | 10565248 | 12172664 | 10339048 | 10227200 |
| Dustin_humanize | 4999034 | 4684320 | 3375592 | 4355720 | 3280192 | 3237160 |
| Etcdctl | 25896983 | 21726832 | 20476680 | 20825104 | 20474424 | 20171856 |
| Gorm_schema | 9421683 | 7041512 | 6439632 | 6661400 | 6492272 | 5175352 |
| IXGo | 41505755 | 29762120 | 29131984 | 28723440 | 28438408 | 28301104 |
| K8s_workqueue | 10681819 | 11320336 | 10625504 | 10781960 | 10689960 | 8652312 |
| Toml | 7324958 | 6153048 | 5035576 | 5776464 | 4918112 | 4862528 |
| Uber_zap | 10024992 | 11594240 | 9277488 | 11032432 | 9519448 | 9384216 |
| XGo | 18662581 | 17639768 | 15499776 | 16834112 | 16540752 | 16432832 |
