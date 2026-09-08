## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTONoGlobalDCE | 786217.5 ms | 779897.0 ms | 6320.6 ms | 563219.5 ms |
| IXGo | LLGoFullLTOGlobalDCE | 765148.3 ms | 758623.0 ms | 6525.3 ms | 548980.2 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 741217.1 ms | 734634.8 ms | 6582.3 ms | 511861.4 ms |
| IXGo | LLGoNoLTO | 428523.1 ms | 422960.6 ms | 5562.4 ms | 150215.8 ms |
| IXGo | LLGoDeadcodeDrop | 417452.8 ms | 411452.1 ms | 6000.7 ms | 144235.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 269293.2 ms | 264742.5 ms | 4550.7 ms | 162183.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 265368.9 ms | 260864.5 ms | 4504.5 ms | 159825.5 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 263400.6 ms | 259197.6 ms | 4203.0 ms | 159701.8 ms |
| Etcdctl | LLGoDeadcodeDrop | 198163.4 ms | 194142.6 ms | 4020.8 ms | 64940.9 ms |
| Etcdctl | LLGoNoLTO | 197627.2 ms | 193557.1 ms | 4070.2 ms | 64223.2 ms |
| XGo | LLGoFullLTOGlobalDCE | 182324.3 ms | 179228.0 ms | 3096.3 ms | 125745.8 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 178199.8 ms | 175224.4 ms | 2975.3 ms | 122492.4 ms |
| XGo | LLGoFullLTONoGlobalDCE | 175359.0 ms | 172472.0 ms | 2886.9 ms | 122468.9 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 141379.1 ms | 139223.5 ms | 2155.6 ms | 103399.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 129180.0 ms | 127068.1 ms | 2111.9 ms | 89659.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 127559.7 ms | 125354.4 ms | 2205.3 ms | 89826.8 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 109283.8 ms | 107533.4 ms | 1750.5 ms | 82902.9 ms |
| XGo | LLGoDeadcodeDrop | 106460.6 ms | 103868.6 ms | 2592.1 ms | 39033.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 104571.7 ms | 102893.0 ms | 1678.7 ms | 80643.1 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 104073.6 ms | 102421.0 ms | 1652.5 ms | 80869.8 ms |
| XGo | LLGoNoLTO | 103986.6 ms | 101438.8 ms | 2547.8 ms | 38543.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 101742.5 ms | 100089.6 ms | 1652.9 ms | 74508.2 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 100333.9 ms | 98623.0 ms | 1710.9 ms | 73456.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 92508.4 ms | 90814.7 ms | 1693.8 ms | 68413.4 ms |
| Aws_restjson | LLGoDeadcodeDrop | 84575.1 ms | 82710.0 ms | 1865.1 ms | 39213.4 ms |
| Aws_restjson | LLGoNoLTO | 82787.0 ms | 80911.3 ms | 1875.7 ms | 38296.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 63516.1 ms | 62208.2 ms | 1307.9 ms | 43469.2 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 62708.8 ms | 61460.6 ms | 1248.2 ms | 43643.9 ms |
| Uber_zap | LLGoDeadcodeDrop | 57192.3 ms | 55761.6 ms | 1430.7 ms | 24236.0 ms |
| Uber_zap | LLGoNoLTO | 55514.4 ms | 54032.6 ms | 1481.9 ms | 23477.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 54131.7 ms | 52879.1 ms | 1252.6 ms | 33834.3 ms |
| Toml | LLGoFullLTONoGlobalDCE | 50341.2 ms | 49415.0 ms | 926.2 ms | 38606.1 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 48946.2 ms | 47571.4 ms | 1374.9 ms | 21657.5 ms |
| K8s_workqueue | LLGoNoLTO | 48058.3 ms | 46742.2 ms | 1316.1 ms | 21215.5 ms |
| IXGo | Go | 44186.5 ms | 41216.4 ms | 2970.1 ms | 12756.6 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 43732.1 ms | 42775.1 ms | 957.0 ms | 31465.0 ms |
| Toml | LLGoFullLTOGlobalDCE | 42498.1 ms | 41543.0 ms | 955.1 ms | 30553.8 ms |
| Gorm_schema | LLGoDeadcodeDrop | 38059.5 ms | 36917.8 ms | 1141.7 ms | 12344.1 ms |
| Gorm_schema | LLGoNoLTO | 37302.5 ms | 36148.3 ms | 1154.3 ms | 12078.2 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 33325.2 ms | 32606.4 ms | 718.8 ms | 25902.8 ms |
| Etcdctl | Go | 32759.1 ms | 30842.5 ms | 1916.7 ms | 9789.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 24916.3 ms | 24141.6 ms | 774.6 ms | 17468.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 24447.2 ms | 23750.6 ms | 696.6 ms | 17011.3 ms |
| Toml | LLGoDeadcodeDrop | 24334.1 ms | 23423.9 ms | 910.2 ms | 9057.4 ms |
| Toml | LLGoNoLTO | 22871.9 ms | 22072.1 ms | 799.8 ms | 8681.8 ms |
| XGo | Go | 19062.4 ms | 17890.2 ms | 1172.2 ms | 5566.6 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 13137.1 ms | 12502.5 ms | 634.7 ms | 5619.4 ms |
| Dustin_humanize | LLGoNoLTO | 13026.0 ms | 12369.9 ms | 656.1 ms | 5382.8 ms |
| Aws_restjson | Go | 7771.8 ms | 7149.8 ms | 622.0 ms | 3133.9 ms |
| Gorm_schema | Go | 5614.2 ms | 5246.3 ms | 367.9 ms | 2100.8 ms |
| Uber_zap | Go | 5266.6 ms | 4867.8 ms | 398.7 ms | 2068.0 ms |
| K8s_workqueue | Go | 4518.1 ms | 4166.5 ms | 351.6 ms | 1578.7 ms |
| Toml | Go | 1947.0 ms | 1753.7 ms | 193.3 ms | 884.7 ms |
| Dustin_humanize | Go | 756.8 ms | 656.0 ms | 100.8 ms | 358.9 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1726088.9 ms | 1220715.5 ms | 9 |
| LLGoFullLTOGlobalDCE | 1675768.2 ms | 1169512.3 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1634921.1 ms | 1111885.9 ms | 9 |
| LLGoNoLTO | 989697.1 ms | 362114.0 ms | 9 |
| LLGoDeadcodeDrop | 988321.1 ms | 360337.5 ms | 9 |
| Go | 121882.4 ms | 38237.5 ms | 9 |

Dependency download details are in `download-timings.log`.
