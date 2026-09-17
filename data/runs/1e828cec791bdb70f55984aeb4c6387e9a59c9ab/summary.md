# LLGo binary-size CI
All values are ELF file sizes in bytes, collected by Bent `benchsize`.

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635492 | 12910520 | 10538112 | 12257664 | 10361520 | 10248808 |
| Dustin_humanize | 4999034 | 4735224 | 3401152 | 4405408 | 3294120 | 3250352 |
| Etcdctl | 25896983 | 21832808 | 20547568 | 21000440 | 20631672 | 20335968 |
| Gorm_schema | 9421683 | 7101112 | 6483808 | 6725912 | 6553928 | 5193024 |
| IXGo | 47404136 | 31505608 | 30800504 | 30189104 | 29890728 | 29755360 |
| K8s_workqueue | 10681819 | 11436344 | 10720568 | 10922928 | 10830216 | 8722144 |
| Toml | 7324958 | 6197752 | 5057760 | 5812824 | 4929744 | 4873712 |
| Uber_zap | 10024992 | 11684240 | 9303232 | 11147568 | 9579328 | 9443408 |
| XGo | 18662581 | 17863152 | 15666832 | 17111232 | 16804368 | 16698304 |
