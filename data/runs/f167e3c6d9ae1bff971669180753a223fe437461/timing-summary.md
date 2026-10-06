## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTONoGlobalDCE | 725182.1 ms | 714169.8 ms | 11012.4 ms | 362460.6 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 702563.3 ms | 692043.3 ms | 10520.0 ms | 355460.4 ms |
| IXGo | LLGoFullLTOGlobalDCE | 691554.8 ms | 680957.8 ms | 10597.0 ms | 349624.0 ms |
| IXGo | LLGoNoLTO | 546656.5 ms | 537415.6 ms | 9240.9 ms | 158320.2 ms |
| IXGo | LLGoDeadcodeDrop | 544569.6 ms | 530286.2 ms | 14283.4 ms | 162116.5 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 346572.7 ms | 341288.4 ms | 5284.3 ms | 202788.4 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 342035.3 ms | 336855.5 ms | 5179.7 ms | 202081.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 341564.8 ms | 336377.3 ms | 5187.6 ms | 200078.0 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 273154.3 ms | 269239.6 ms | 3914.7 ms | 151930.6 ms |
| Aws_restjson | LLGoDeadcodeDrop | 271506.3 ms | 268030.1 ms | 3476.2 ms | 90951.7 ms |
| Aws_restjson | LLGoNoLTO | 268114.8 ms | 264689.2 ms | 3425.6 ms | 89923.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 262762.9 ms | 259007.2 ms | 3755.7 ms | 138100.0 ms |
| Etcdctl | LLGoDeadcodeDrop | 260886.8 ms | 255151.6 ms | 5735.2 ms | 86928.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 258436.2 ms | 254504.5 ms | 3931.7 ms | 135983.8 ms |
| Etcdctl | LLGoNoLTO | 258036.3 ms | 253833.6 ms | 4202.7 ms | 84615.8 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 251093.4 ms | 247597.1 ms | 3496.3 ms | 165220.0 ms |
| XGo | LLGoFullLTONoGlobalDCE | 247445.2 ms | 244011.0 ms | 3434.2 ms | 163252.0 ms |
| XGo | LLGoFullLTOGlobalDCE | 246896.9 ms | 243448.9 ms | 3448.1 ms | 160831.3 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 234434.3 ms | 231018.0 ms | 3416.3 ms | 135144.2 ms |
| Uber_zap | LLGoDeadcodeDrop | 231134.3 ms | 228193.1 ms | 2941.2 ms | 81301.5 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 230398.7 ms | 226678.1 ms | 3720.6 ms | 132005.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 228281.2 ms | 224872.4 ms | 3408.9 ms | 125606.9 ms |
| Uber_zap | LLGoNoLTO | 227714.6 ms | 225006.2 ms | 2708.4 ms | 80149.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 227460.4 ms | 223948.6 ms | 3511.8 ms | 130498.4 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 222453.1 ms | 219501.5 ms | 2951.6 ms | 78389.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 221670.8 ms | 218322.3 ms | 3348.5 ms | 121040.8 ms |
| K8s_workqueue | LLGoNoLTO | 220214.9 ms | 217090.7 ms | 3124.2 ms | 77627.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 212445.2 ms | 208957.4 ms | 3487.8 ms | 114174.3 ms |
| XGo | LLGoDeadcodeDrop | 162113.7 ms | 158449.4 ms | 3664.3 ms | 59084.4 ms |
| XGo | LLGoNoLTO | 160392.7 ms | 157701.9 ms | 2690.7 ms | 57485.7 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 110019.3 ms | 107889.6 ms | 2129.6 ms | 63947.9 ms |
| Gorm_schema | LLGoNoLTO | 109134.1 ms | 107242.7 ms | 1891.4 ms | 36158.3 ms |
| Gorm_schema | LLGoDeadcodeDrop | 109056.1 ms | 107201.2 ms | 1854.8 ms | 36186.0 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 107990.5 ms | 105969.3 ms | 2021.3 ms | 63044.7 ms |
| Toml | LLGoDeadcodeDrop | 102470.4 ms | 100593.0 ms | 1877.5 ms | 33872.5 ms |
| Toml | LLGoNoLTO | 101202.3 ms | 99279.7 ms | 1922.5 ms | 33479.2 ms |
| Toml | LLGoFullLTONoGlobalDCE | 100565.8 ms | 98464.4 ms | 2101.4 ms | 57734.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 97539.5 ms | 95590.6 ms | 1949.0 ms | 51185.7 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 91650.2 ms | 89578.1 ms | 2072.0 ms | 48596.9 ms |
| Toml | LLGoFullLTOGlobalDCE | 90937.8 ms | 88965.3 ms | 1972.5 ms | 47893.0 ms |
| IXGo | Go | 84302.8 ms | 79111.1 ms | 5191.6 ms | 23163.0 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 71266.3 ms | 69980.2 ms | 1286.1 ms | 25588.9 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 71076.2 ms | 69697.7 ms | 1378.6 ms | 43221.1 ms |
| Dustin_humanize | LLGoNoLTO | 71067.1 ms | 69823.8 ms | 1243.2 ms | 25439.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 61694.2 ms | 60337.8 ms | 1356.4 ms | 33255.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 61392.4 ms | 60011.1 ms | 1381.3 ms | 32950.8 ms |
| Etcdctl | Go | 33781.8 ms | 31665.4 ms | 2116.4 ms | 10184.5 ms |
| XGo | Go | 19220.3 ms | 18021.7 ms | 1198.6 ms | 5635.3 ms |
| Aws_restjson | Go | 8106.4 ms | 7401.8 ms | 704.6 ms | 3313.3 ms |
| Gorm_schema | Go | 5867.9 ms | 5456.6 ms | 411.4 ms | 2270.0 ms |
| Uber_zap | Go | 5402.7 ms | 4970.7 ms | 432.1 ms | 2098.6 ms |
| K8s_workqueue | Go | 4766.7 ms | 4246.4 ms | 520.3 ms | 1715.2 ms |
| Toml | Go | 2095.5 ms | 1845.8 ms | 249.6 ms | 965.6 ms |
| Dustin_humanize | Go | 832.9 ms | 694.0 ms | 138.9 ms | 386.2 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2332282.4 ms | 1310874.7 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2254300.8 ms | 1234083.4 ms | 9 |
| LLGoFullLTOGlobalDCE | 2250235.3 ms | 1243152.5 ms | 9 |
| LLGoDeadcodeDrop | 1975456.7 ms | 654418.8 ms | 9 |
| LLGoNoLTO | 1962533.2 ms | 643197.7 ms | 9 |
| Go | 164376.9 ms | 49731.7 ms | 9 |

Dependency download details are in `download-timings.log`.
