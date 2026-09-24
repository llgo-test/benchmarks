# LLGo binary-size CI
All values are ELF file sizes in bytes, collected by Bent `benchsize`.

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635492 | 12954600 | 10592768 | 12286840 | 10394184 | 10281584 |
| Dustin_humanize | 4999034 | 4719360 | 3391856 | 4398296 | 3293944 | 3250192 |
| Etcdctl | 25896983 | 21779080 | 20498856 | 20985320 | 20610040 | 20314264 |
| Gorm_schema | 9421683 | 7078976 | 6465928 | 6716976 | 6544312 | 5186256 |
| IXGo | 47404136 | 31427136 | 30724896 | 30165976 | 29866848 | 29731448 |
| K8s_workqueue | 10681819 | — | — | — | — | — |
| Toml | 7324958 | 6178272 | 5043960 | 5805640 | 4927856 | 4871856 |
| Uber_zap | 10024992 | 11653088 | 9281016 | 11138392 | 9567632 | 9431688 |
| XGo | 18662581 | 17810808 | 15623648 | 17097112 | 16789144 | 16683176 |

5 results are missing; see the CI build log. Missing values are excluded from comparisons.
