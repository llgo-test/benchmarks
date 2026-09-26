# LLGo binary-size CI
All values are ELF file sizes in bytes, collected by Bent `benchsize`.

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635492 | 12954600 | 10592768 | 12286856 | 10394200 | 10281616 |
| Dustin_humanize | 4999034 | 4719376 | 3391856 | 4398312 | 3293960 | 3250224 |
| Etcdctl | 25896983 | 21779096 | 20498856 | 20985336 | 20610072 | 20314296 |
| Gorm_schema | 9421683 | 7078992 | 6465936 | 6716992 | 6544328 | 5186272 |
| IXGo | 47404136 | 31427440 | 30725200 | 30166312 | 29867168 | 29731784 |
| K8s_workqueue | 10681819 | — | — | — | — | — |
| Toml | 7324958 | 6178288 | 5043992 | 5805656 | 4927872 | 4871856 |
| Uber_zap | 10024992 | 11653088 | 9281016 | 11138408 | 9567648 | 9431704 |
| XGo | 18662581 | 17810808 | 15623632 | 17097128 | 16789176 | 16683192 |

5 results are missing; see the CI build log. Missing values are excluded from comparisons.
