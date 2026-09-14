## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 266982.8 ms | 262017.4 ms | 4965.4 ms | 165006.8 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 265334.7 ms | 260517.2 ms | 4817.5 ms | 165898.6 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 264426.0 ms | 259603.9 ms | 4822.0 ms | 163081.1 ms |
| Etcdctl | LLGoDeadcodeDrop | 191517.0 ms | 186729.1 ms | 4787.9 ms | 62674.6 ms |
| Etcdctl | LLGoNoLTO | 189594.5 ms | 185234.7 ms | 4359.8 ms | 61607.2 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 182115.0 ms | 178714.2 ms | 3400.8 ms | 128189.5 ms |
| XGo | LLGoFullLTONoGlobalDCE | 179081.1 ms | 175986.1 ms | 3095.0 ms | 127160.5 ms |
| XGo | LLGoFullLTOGlobalDCE | 178940.8 ms | 175740.1 ms | 3200.8 ms | 126470.7 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 139867.7 ms | 137661.7 ms | 2206.0 ms | 104773.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 129378.0 ms | 127190.6 ms | 2187.4 ms | 93197.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 127754.7 ms | 125453.6 ms | 2301.1 ms | 91961.8 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 108971.6 ms | 107235.0 ms | 1736.6 ms | 84681.1 ms |
| XGo | LLGoDeadcodeDrop | 105044.0 ms | 102412.3 ms | 2631.7 ms | 38531.9 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 104320.8 ms | 102411.5 ms | 1909.3 ms | 82567.8 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 104118.6 ms | 102374.8 ms | 1743.8 ms | 82139.0 ms |
| XGo | LLGoNoLTO | 102801.6 ms | 100040.4 ms | 2761.2 ms | 38119.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 100148.1 ms | 98365.5 ms | 1782.5 ms | 74379.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 99496.0 ms | 97730.4 ms | 1765.6 ms | 74422.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 89568.5 ms | 87848.9 ms | 1719.6 ms | 67219.8 ms |
| Aws_restjson | LLGoNoLTO | 82113.6 ms | 80086.5 ms | 2027.1 ms | 39417.8 ms |
| Aws_restjson | LLGoDeadcodeDrop | 80228.6 ms | 78288.5 ms | 1940.1 ms | 37736.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 64169.0 ms | 62845.0 ms | 1324.1 ms | 45367.6 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 62833.3 ms | 61506.2 ms | 1327.1 ms | 44656.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 54460.7 ms | 53128.5 ms | 1332.2 ms | 34955.8 ms |
| Uber_zap | LLGoDeadcodeDrop | 53055.1 ms | 51600.2 ms | 1454.9 ms | 22463.1 ms |
| Uber_zap | LLGoNoLTO | 52632.1 ms | 51102.1 ms | 1530.0 ms | 22319.2 ms |
| Toml | LLGoFullLTONoGlobalDCE | 51712.3 ms | 50725.2 ms | 987.1 ms | 40440.2 ms |
| K8s_workqueue | LLGoNoLTO | 46242.3 ms | 44806.7 ms | 1435.6 ms | 20353.0 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 46086.9 ms | 44684.2 ms | 1402.7 ms | 20593.2 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 43879.3 ms | 42946.4 ms | 932.9 ms | 32150.1 ms |
| Toml | LLGoFullLTOGlobalDCE | 43561.6 ms | 42552.5 ms | 1009.0 ms | 31926.3 ms |
| Gorm_schema | LLGoDeadcodeDrop | 37061.0 ms | 35831.1 ms | 1229.8 ms | 12057.2 ms |
| Gorm_schema | LLGoNoLTO | 35465.1 ms | 34341.1 ms | 1124.1 ms | 11593.0 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 34152.3 ms | 33309.5 ms | 842.8 ms | 27182.3 ms |
| Etcdctl | Go | 31782.8 ms | 29622.0 ms | 2160.8 ms | 9585.9 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 25124.9 ms | 24327.7 ms | 797.3 ms | 18087.5 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 24633.3 ms | 23896.7 ms | 736.7 ms | 17744.1 ms |
| Toml | LLGoDeadcodeDrop | 23164.5 ms | 22238.0 ms | 926.6 ms | 8568.7 ms |
| Toml | LLGoNoLTO | 22269.6 ms | 21353.1 ms | 916.5 ms | 8500.3 ms |
| XGo | Go | 18541.0 ms | 17217.8 ms | 1323.2 ms | 5359.1 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 12766.9 ms | 12100.9 ms | 666.0 ms | 5612.7 ms |
| Dustin_humanize | LLGoNoLTO | 12763.5 ms | 12051.2 ms | 712.3 ms | 5529.8 ms |
| Aws_restjson | Go | 7507.9 ms | 6870.4 ms | 637.5 ms | 2993.5 ms |
| Gorm_schema | Go | 5498.2 ms | 5111.2 ms | 387.1 ms | 2080.4 ms |
| Uber_zap | Go | 5212.8 ms | 4779.9 ms | 433.0 ms | 1999.6 ms |
| K8s_workqueue | Go | 4465.6 ms | 4064.2 ms | 401.3 ms | 1560.6 ms |
| Toml | Go | 1916.9 ms | 1731.9 ms | 185.0 ms | 867.3 ms |
| Dustin_humanize | Go | 763.7 ms | 635.9 ms | 127.8 ms | 359.1 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 946273.9 ms | 677360.6 ms | 8 |
| LLGoFullLTOGlobalDCE | 907100.1 ms | 633112.6 ms | 8 |
| LLGoFullLTOGlobalDCEPlugin | 891657.3 ms | 613186.5 ms | 8 |
| LLGoDeadcodeDrop | 548924.0 ms | 208237.6 ms | 8 |
| LLGoNoLTO | 543882.2 ms | 207439.4 ms | 8 |
| Go | 75688.8 ms | 24805.4 ms | 8 |

Dependency download details are in `download-timings.log`.
