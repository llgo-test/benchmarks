## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTONoGlobalDCE | 577101.0 ms | 572175.7 ms | 4925.3 ms | 385363.1 ms |
| IXGo | LLGoFullLTOGlobalDCE | 540708.3 ms | 535830.5 ms | 4877.9 ms | 358829.6 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 485411.3 ms | 480470.1 ms | 4941.2 ms | 322061.5 ms |
| IXGo | LLGoDeadcodeDrop | 347134.8 ms | 342571.4 ms | 4563.4 ms | 117803.9 ms |
| IXGo | LLGoNoLTO | 309336.6 ms | 304998.7 ms | 4337.9 ms | 105169.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 191767.9 ms | 188031.4 ms | 3736.6 ms | 117867.5 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 181235.7 ms | 177860.8 ms | 3374.9 ms | 112300.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 179740.7 ms | 176281.4 ms | 3459.3 ms | 110148.7 ms |
| Etcdctl | LLGoDeadcodeDrop | 134678.8 ms | 131311.4 ms | 3367.4 ms | 45442.1 ms |
| Etcdctl | LLGoNoLTO | 133173.5 ms | 130032.1 ms | 3141.3 ms | 44548.7 ms |
| XGo | LLGoFullLTOGlobalDCE | 126872.9 ms | 124501.1 ms | 2371.8 ms | 90112.3 ms |
| XGo | LLGoFullLTONoGlobalDCE | 125955.7 ms | 123672.3 ms | 2283.5 ms | 90019.2 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 123768.6 ms | 121412.4 ms | 2356.2 ms | 87985.8 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 99940.7 ms | 98252.2 ms | 1688.6 ms | 75363.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 90290.9 ms | 88555.1 ms | 1735.7 ms | 65979.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 89759.0 ms | 88158.6 ms | 1600.4 ms | 64974.3 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 74623.8 ms | 73378.7 ms | 1245.1 ms | 57689.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 71637.9 ms | 70355.3 ms | 1282.7 ms | 56684.1 ms |
| XGo | LLGoDeadcodeDrop | 70775.3 ms | 68800.6 ms | 1974.7 ms | 26764.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 70398.5 ms | 68952.6 ms | 1445.9 ms | 53518.8 ms |
| XGo | LLGoNoLTO | 70308.2 ms | 68334.1 ms | 1974.0 ms | 26403.6 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 68849.0 ms | 67663.0 ms | 1186.1 ms | 54740.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 68154.3 ms | 66970.4 ms | 1183.9 ms | 51779.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 59757.4 ms | 58514.8 ms | 1242.6 ms | 45481.3 ms |
| Aws_restjson | LLGoNoLTO | 56823.5 ms | 55364.0 ms | 1459.5 ms | 28273.5 ms |
| Aws_restjson | LLGoDeadcodeDrop | 56045.7 ms | 54503.0 ms | 1542.7 ms | 26819.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 43924.3 ms | 42920.8 ms | 1003.5 ms | 31115.0 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 43080.0 ms | 42098.2 ms | 981.8 ms | 30475.9 ms |
| Uber_zap | LLGoDeadcodeDrop | 39824.3 ms | 38751.0 ms | 1073.2 ms | 17726.9 ms |
| Uber_zap | LLGoNoLTO | 37939.1 ms | 36829.8 ms | 1109.3 ms | 17573.1 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 35725.6 ms | 34744.6 ms | 981.0 ms | 23017.3 ms |
| Toml | LLGoFullLTONoGlobalDCE | 34813.2 ms | 34000.3 ms | 812.9 ms | 27006.6 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 34811.8 ms | 33719.4 ms | 1092.5 ms | 16721.8 ms |
| K8s_workqueue | LLGoNoLTO | 34405.2 ms | 33334.3 ms | 1070.9 ms | 16080.1 ms |
| Toml | LLGoFullLTOGlobalDCE | 29818.0 ms | 29063.1 ms | 754.9 ms | 21946.6 ms |
| IXGo | Go | 29181.9 ms | 26913.6 ms | 2268.3 ms | 8547.8 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 28723.2 ms | 27987.0 ms | 736.2 ms | 21104.3 ms |
| Gorm_schema | LLGoNoLTO | 25477.2 ms | 24601.8 ms | 875.4 ms | 8560.7 ms |
| Gorm_schema | LLGoDeadcodeDrop | 25458.4 ms | 24516.4 ms | 942.0 ms | 8583.3 ms |
| Etcdctl | Go | 21821.8 ms | 20304.8 ms | 1517.1 ms | 6609.9 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 21488.7 ms | 20940.1 ms | 548.6 ms | 16786.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 18024.1 ms | 17423.0 ms | 601.1 ms | 13068.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 17253.3 ms | 16651.7 ms | 601.6 ms | 12378.2 ms |
| Toml | LLGoDeadcodeDrop | 15803.4 ms | 15107.5 ms | 695.9 ms | 5957.9 ms |
| Toml | LLGoNoLTO | 14529.7 ms | 13876.1 ms | 653.6 ms | 5585.3 ms |
| XGo | Go | 12797.7 ms | 11931.4 ms | 866.3 ms | 3747.6 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 9167.5 ms | 8656.7 ms | 510.8 ms | 4055.2 ms |
| Dustin_humanize | LLGoNoLTO | 8559.3 ms | 8060.6 ms | 498.6 ms | 3789.3 ms |
| Aws_restjson | Go | 5439.4 ms | 4936.5 ms | 502.9 ms | 2295.7 ms |
| Gorm_schema | Go | 3807.8 ms | 3525.9 ms | 281.9 ms | 1494.4 ms |
| Uber_zap | Go | 3650.6 ms | 3303.4 ms | 347.2 ms | 1467.8 ms |
| K8s_workqueue | Go | 2924.8 ms | 2593.9 ms | 330.8 ms | 1061.9 ms |
| Toml | Go | 1405.2 ms | 1235.7 ms | 169.5 ms | 682.0 ms |
| Dustin_humanize | Go | 532.1 ms | 432.2 ms | 99.9 ms | 270.2 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1227088.0 ms | 849744.3 ms | 9 |
| LLGoFullLTOGlobalDCE | 1180666.9 ms | 806377.5 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1091069.6 ms | 741675.7 ms | 9 |
| LLGoDeadcodeDrop | 733700.0 ms | 269874.8 ms | 9 |
| LLGoNoLTO | 690552.1 ms | 255983.4 ms | 9 |
| Go | 81561.3 ms | 26177.2 ms | 9 |

Dependency download details are in `download-timings.log`.
