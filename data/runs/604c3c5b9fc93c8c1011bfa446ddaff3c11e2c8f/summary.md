# LLGo binary-size CI
All values are ELF file sizes in bytes, collected by Bent `benchsize`.

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635492 | 12952000 | 10590288 | 12288696 | 10395312 | 10282736 |
| Dustin_humanize | 4999034 | 4718672 | 3391512 | 4398376 | 3293648 | 3249928 |
| Etcdctl | 25896983 | 21777056 | 20496584 | 20986208 | 20611024 | 20315272 |
| Gorm_schema | 9421683 | 7077296 | 6464072 | 6717128 | 6544752 | 5186504 |
| IXGo | 47404136 | 31423952 | 30721544 | 30167856 | 29868624 | 29733000 |
| K8s_workqueue | 10681819 | — | — | — | — | — |
| Toml | 7324958 | 6177576 | 5043016 | 5805704 | 4927848 | 4871896 |
| Uber_zap | 10024992 | 11651192 | 9278896 | 11139504 | 9568664 | 9432744 |
| XGo | 18662581 | 17808544 | 15621400 | 17098160 | 16790128 | 16684160 |

5 results are missing; see the CI build log. Missing values are excluded from comparisons.
