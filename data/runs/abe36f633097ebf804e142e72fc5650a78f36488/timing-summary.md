## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 403874.8 ms | 394828.3 ms | 9046.5 ms | 217466.1 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 400317.0 ms | 390571.3 ms | 9745.8 ms | 218828.0 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 381519.3 ms | 372586.8 ms | 8932.5 ms | 211302.3 ms |
| IXGo | LLGoDeadcodeDrop | 299355.9 ms | 291459.0 ms | 7896.9 ms | 92183.2 ms |
| IXGo | LLGoNoLTO | 284937.7 ms | 277405.8 ms | 7531.9 ms | 86920.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 183009.9 ms | 179237.0 ms | 3772.9 ms | 120253.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 182489.3 ms | 178653.6 ms | 3835.7 ms | 119790.2 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 180315.4 ms | 176688.3 ms | 3627.1 ms | 119869.2 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 149768.3 ms | 147196.1 ms | 2572.2 ms | 92375.1 ms |
| Aws_restjson | LLGoDeadcodeDrop | 146678.3 ms | 144209.8 ms | 2468.5 ms | 54632.6 ms |
| Aws_restjson | LLGoNoLTO | 143732.0 ms | 141332.6 ms | 2399.5 ms | 53413.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 142040.3 ms | 139515.7 ms | 2524.6 ms | 83932.1 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 140195.3 ms | 137571.1 ms | 2624.2 ms | 83059.6 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 130892.1 ms | 128223.5 ms | 2668.6 ms | 95706.3 ms |
| Etcdctl | LLGoDeadcodeDrop | 130219.4 ms | 126767.5 ms | 3451.9 ms | 46400.2 ms |
| XGo | LLGoFullLTONoGlobalDCE | 128518.1 ms | 125843.3 ms | 2674.8 ms | 95253.0 ms |
| XGo | LLGoFullLTOGlobalDCE | 128396.4 ms | 125605.4 ms | 2791.0 ms | 94236.7 ms |
| Etcdctl | LLGoNoLTO | 125770.5 ms | 122463.2 ms | 3307.3 ms | 44452.1 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 125079.2 ms | 122915.2 ms | 2164.0 ms | 82255.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 123445.3 ms | 121090.3 ms | 2355.0 ms | 81703.0 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 122722.2 ms | 120413.2 ms | 2309.0 ms | 81348.3 ms |
| Uber_zap | LLGoDeadcodeDrop | 121506.7 ms | 119422.6 ms | 2084.1 ms | 48684.2 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 118409.3 ms | 116259.0 ms | 2150.3 ms | 74395.1 ms |
| Uber_zap | LLGoNoLTO | 118093.6 ms | 116196.6 ms | 1897.1 ms | 47129.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 116827.2 ms | 114651.7 ms | 2175.5 ms | 73228.0 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 116232.3 ms | 114149.0 ms | 2083.3 ms | 46085.8 ms |
| K8s_workqueue | LLGoNoLTO | 114251.6 ms | 112162.9 ms | 2088.7 ms | 45522.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 111420.9 ms | 109199.2 ms | 2221.8 ms | 69031.0 ms |
| XGo | LLGoDeadcodeDrop | 74136.8 ms | 71777.9 ms | 2358.9 ms | 29802.8 ms |
| XGo | LLGoNoLTO | 72715.3 ms | 70474.1 ms | 2241.3 ms | 29404.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 62334.7 ms | 60868.4 ms | 1466.3 ms | 37993.6 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 62182.4 ms | 60798.3 ms | 1384.1 ms | 38248.4 ms |
| Gorm_schema | LLGoDeadcodeDrop | 61694.6 ms | 60331.3 ms | 1363.2 ms | 21061.0 ms |
| IXGo | Go | 61641.3 ms | 57419.5 ms | 4221.8 ms | 17512.8 ms |
| Gorm_schema | LLGoNoLTO | 60633.4 ms | 59367.7 ms | 1265.7 ms | 20613.2 ms |
| Toml | LLGoDeadcodeDrop | 58456.7 ms | 57067.6 ms | 1389.1 ms | 19660.3 ms |
| Toml | LLGoNoLTO | 57895.4 ms | 56503.8 ms | 1391.6 ms | 19399.4 ms |
| Toml | LLGoFullLTONoGlobalDCE | 57351.8 ms | 55919.5 ms | 1432.3 ms | 34735.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 54214.6 ms | 52887.4 ms | 1327.2 ms | 29840.7 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 51966.9 ms | 50503.7 ms | 1463.3 ms | 29064.3 ms |
| Toml | LLGoFullLTOGlobalDCE | 51780.0 ms | 50382.6 ms | 1397.4 ms | 28870.8 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 39859.0 ms | 38867.8 ms | 991.3 ms | 25560.5 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 39625.2 ms | 38680.0 ms | 945.2 ms | 14543.8 ms |
| Dustin_humanize | LLGoNoLTO | 39017.1 ms | 38112.9 ms | 904.1 ms | 14235.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 33616.6 ms | 32626.6 ms | 990.0 ms | 18984.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 33341.7 ms | 32400.5 ms | 941.2 ms | 18897.0 ms |
| Etcdctl | Go | 24800.5 ms | 23066.6 ms | 1733.9 ms | 7829.0 ms |
| XGo | Go | 14204.1 ms | 13228.7 ms | 975.4 ms | 4269.0 ms |
| Aws_restjson | Go | 5971.6 ms | 5391.6 ms | 580.1 ms | 2424.1 ms |
| Gorm_schema | Go | 4283.0 ms | 3932.2 ms | 350.8 ms | 1638.9 ms |
| Uber_zap | Go | 3951.3 ms | 3636.4 ms | 314.9 ms | 1541.5 ms |
| K8s_workqueue | Go | 3613.6 ms | 3132.5 ms | 481.2 ms | 1777.9 ms |
| Toml | Go | 1541.4 ms | 1350.9 ms | 190.5 ms | 701.8 ms |
| Dustin_humanize | Go | 612.8 ms | 486.6 ms | 126.2 ms | 293.3 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1247315.8 ms | 780947.6 ms | 9 |
| LLGoFullLTOGlobalDCE | 1244529.7 ms | 756117.5 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1224042.7 ms | 739163.3 ms | 9 |
| LLGoDeadcodeDrop | 1047905.8 ms | 373053.9 ms | 9 |
| LLGoNoLTO | 1017046.6 ms | 361090.3 ms | 9 |
| Go | 120619.5 ms | 37988.3 ms | 9 |

Dependency download details are in `download-timings.log`.
