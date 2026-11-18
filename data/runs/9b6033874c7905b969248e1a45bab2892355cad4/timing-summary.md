## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 670479.9 ms | 653701.3 ms | 16778.6 ms | 445258.4 ms |
| IXGo | LLGoFullLTOGlobalDCE | 644529.9 ms | 628170.6 ms | 16359.3 ms | 427275.1 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 643186.8 ms | 626487.0 ms | 16699.8 ms | 430932.8 ms |
| IXGo | LLGoDeadcodeDrop | 380858.8 ms | 363809.9 ms | 17048.9 ms | 123805.9 ms |
| IXGo | LLGoNoLTO | 363351.8 ms | 349082.7 ms | 14269.1 ms | 113844.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 354205.5 ms | 346573.7 ms | 7631.7 ms | 263567.8 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 345489.5 ms | 338254.4 ms | 7235.1 ms | 259383.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 333700.4 ms | 326767.6 ms | 6932.8 ms | 249885.7 ms |
| XGo | LLGoFullLTONoGlobalDCE | 254522.9 ms | 249307.6 ms | 5215.3 ms | 204886.4 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 246050.3 ms | 241708.9 ms | 4341.4 ms | 169036.1 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 224928.0 ms | 220018.1 ms | 4910.0 ms | 175256.9 ms |
| XGo | LLGoFullLTOGlobalDCE | 220561.3 ms | 215564.1 ms | 4997.2 ms | 172372.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 211376.8 ms | 207233.8 ms | 4143.0 ms | 138136.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 207317.5 ms | 203387.9 ms | 3929.6 ms | 132301.1 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 197238.4 ms | 193527.2 ms | 3711.2 ms | 141833.0 ms |
| Aws_restjson | LLGoNoLTO | 188790.4 ms | 185105.5 ms | 3684.9 ms | 58765.1 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 185145.7 ms | 181734.4 ms | 3411.3 ms | 134541.5 ms |
| Aws_restjson | LLGoDeadcodeDrop | 184549.5 ms | 180781.2 ms | 3768.3 ms | 59315.8 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 182786.4 ms | 179186.1 ms | 3600.3 ms | 130837.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 179462.9 ms | 175795.6 ms | 3667.3 ms | 121901.1 ms |
| Etcdctl | LLGoDeadcodeDrop | 177968.6 ms | 171653.2 ms | 6315.4 ms | 62106.3 ms |
| Etcdctl | LLGoNoLTO | 176238.0 ms | 170178.8 ms | 6059.2 ms | 60582.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 175947.0 ms | 172556.9 ms | 3390.1 ms | 121656.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 160061.3 ms | 156822.9 ms | 3238.4 ms | 107801.8 ms |
| Uber_zap | LLGoNoLTO | 149489.7 ms | 146465.1 ms | 3024.6 ms | 48072.6 ms |
| Uber_zap | LLGoDeadcodeDrop | 149455.5 ms | 146201.0 ms | 3254.5 ms | 49395.1 ms |
| K8s_workqueue | LLGoNoLTO | 142756.5 ms | 139676.2 ms | 3080.3 ms | 45949.4 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 138174.5 ms | 135140.3 ms | 3034.2 ms | 46190.9 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 117202.7 ms | 114573.5 ms | 2629.2 ms | 82994.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 113809.4 ms | 111389.8 ms | 2419.6 ms | 79985.6 ms |
| Toml | LLGoFullLTONoGlobalDCE | 106019.6 ms | 103674.9 ms | 2344.7 ms | 74948.1 ms |
| XGo | LLGoNoLTO | 99408.3 ms | 95768.4 ms | 3639.9 ms | 36589.3 ms |
| XGo | LLGoDeadcodeDrop | 97741.4 ms | 93360.6 ms | 4380.8 ms | 36034.1 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 91766.2 ms | 89506.8 ms | 2259.3 ms | 58664.2 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 91385.9 ms | 89271.3 ms | 2114.6 ms | 60398.9 ms |
| Toml | LLGoFullLTOGlobalDCE | 89016.6 ms | 86913.4 ms | 2103.3 ms | 58731.2 ms |
| Gorm_schema | LLGoDeadcodeDrop | 84491.4 ms | 82291.4 ms | 2200.0 ms | 29856.6 ms |
| Gorm_schema | LLGoNoLTO | 81281.5 ms | 79288.6 ms | 1992.9 ms | 28191.8 ms |
| Toml | LLGoNoLTO | 74735.6 ms | 72976.3 ms | 1759.2 ms | 25973.9 ms |
| Toml | LLGoDeadcodeDrop | 74521.0 ms | 72716.1 ms | 1804.9 ms | 26119.8 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 70841.0 ms | 69250.2 ms | 1590.7 ms | 51655.2 ms |
| IXGo | Go | 63017.7 ms | 55106.1 ms | 7911.6 ms | 17169.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 58549.5 ms | 57059.4 ms | 1490.1 ms | 38751.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 57079.7 ms | 55612.2 ms | 1467.6 ms | 37378.7 ms |
| Dustin_humanize | LLGoNoLTO | 52495.1 ms | 51210.7 ms | 1284.3 ms | 19756.0 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 51343.0 ms | 50017.4 ms | 1325.7 ms | 19644.0 ms |
| Etcdctl | Go | 24740.9 ms | 22012.7 ms | 2728.2 ms | 7593.3 ms |
| XGo | Go | 14485.1 ms | 12795.8 ms | 1689.3 ms | 4297.0 ms |
| Aws_restjson | Go | 6108.1 ms | 5275.2 ms | 833.0 ms | 2513.6 ms |
| Gorm_schema | Go | 4402.0 ms | 3844.5 ms | 557.5 ms | 1733.4 ms |
| Uber_zap | Go | 4113.7 ms | 3625.2 ms | 488.5 ms | 1688.9 ms |
| K8s_workqueue | Go | 3552.0 ms | 3107.2 ms | 444.8 ms | 1271.0 ms |
| Toml | Go | 1547.7 ms | 1349.8 ms | 197.9 ms | 794.7 ms |
| Dustin_humanize | Go | 620.2 ms | 499.4 ms | 120.8 ms | 301.5 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2165696.8 ms | 1550211.0 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2036686.8 ms | 1402528.8 ms | 9 |
| LLGoFullLTOGlobalDCE | 2030277.3 ms | 1417631.9 ms | 9 |
| LLGoDeadcodeDrop | 1339103.9 ms | 452468.6 ms | 9 |
| LLGoNoLTO | 1328546.8 ms | 437725.0 ms | 9 |
| Go | 122587.4 ms | 37363.3 ms | 9 |

Dependency download details are in `download-timings.log`.
