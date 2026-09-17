# LLGo binary-size CI
All values are ELF file sizes in bytes, collected by Bent `benchsize`.

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635492 | 12905600 | 10533416 | 12252944 | 10357296 | 10244624 |
| Dustin_humanize | 4999034 | 4730704 | 3396648 | 4401712 | 3290696 | 3246912 |
| Etcdctl | 25896983 | 21827864 | 20542640 | 20994464 | 20625784 | 20330056 |
| Gorm_schema | 9421683 | 7091920 | 6474648 | 6714888 | 6542864 | 5182184 |
| IXGo | 47404136 | 31493312 | 30788200 | 30173776 | 29875256 | 29739888 |
| K8s_workqueue | 10681819 | 11407008 | 10691176 | 10893272 | 10800456 | 8696248 |
| Toml | 7324958 | 6193232 | 5053232 | 5809016 | 4926136 | 4870112 |
| Uber_zap | 10024992 | 11678944 | 9298552 | 11142440 | 9575160 | 9439296 |
| XGo | 18662581 | 17855200 | 15659448 | 17103432 | 16796416 | 16690352 |
