# LLGo binary-size CI
All values are ELF file sizes in bytes, collected by Bent `benchsize`.

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635492 | 13001888 | 10627336 | 12332336 | 10436704 | 10324088 |
| Dustin_humanize | 4999034 | 4716200 | 3382656 | 4402976 | 3296232 | 3252448 |
| Etcdctl | 25896983 | 21876312 | 20598088 | 21052296 | 20685576 | 20389912 |
| Gorm_schema | 9421683 | 7091056 | 6481456 | 6731328 | 6559224 | 5197464 |
| IXGo | 41505755 | 30033928 | 29389512 | 29063680 | 28772560 | 28641464 |
| K8s_workqueue | 10681819 | 11424592 | 10716288 | 10930272 | 10837584 | 8732584 |
| Toml | 7324958 | 6199952 | 5054320 | 5836256 | 4949736 | 4893896 |
| Uber_zap | 10024992 | 11699256 | 9315312 | 11182840 | 9614840 | 9478864 |
| XGo | 18662581 | 17886168 | 15687288 | 17151208 | 16844520 | 16738536 |
