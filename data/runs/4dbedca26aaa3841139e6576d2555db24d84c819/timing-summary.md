## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 618600.8 ms | 605763.8 ms | 12837.0 ms | 314439.0 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 611109.4 ms | 598398.2 ms | 12711.1 ms | 308094.7 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 568143.4 ms | 557113.4 ms | 11030.0 ms | 290571.5 ms |
| IXGo | LLGoNoLTO | 481436.5 ms | 471321.1 ms | 10115.5 ms | 142633.4 ms |
| IXGo | LLGoDeadcodeDrop | 454547.3 ms | 444363.1 ms | 10184.3 ms | 133376.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 266544.2 ms | 261841.8 ms | 4702.4 ms | 164747.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 264253.8 ms | 259274.4 ms | 4979.4 ms | 161481.0 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 262197.6 ms | 257464.4 ms | 4733.2 ms | 163562.3 ms |
| Etcdctl | LLGoDeadcodeDrop | 195448.6 ms | 191308.7 ms | 4140.0 ms | 64796.7 ms |
| Etcdctl | LLGoNoLTO | 191445.4 ms | 187423.9 ms | 4021.4 ms | 62832.9 ms |
| XGo | LLGoFullLTONoGlobalDCE | 187040.5 ms | 183610.4 ms | 3430.1 ms | 130605.7 ms |
| XGo | LLGoFullLTOGlobalDCE | 184138.4 ms | 180922.9 ms | 3215.6 ms | 127005.5 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 183762.5 ms | 180389.7 ms | 3372.9 ms | 126147.7 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 142180.0 ms | 139648.0 ms | 2532.0 ms | 104074.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 131855.2 ms | 129428.6 ms | 2426.6 ms | 92445.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 128655.5 ms | 126166.7 ms | 2488.8 ms | 89478.4 ms |
| XGo | LLGoDeadcodeDrop | 113691.8 ms | 110692.8 ms | 2999.0 ms | 41697.8 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 111767.6 ms | 109857.6 ms | 1910.1 ms | 85155.7 ms |
| XGo | LLGoNoLTO | 110159.5 ms | 107305.9 ms | 2853.6 ms | 40556.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 100425.1 ms | 98481.2 ms | 1943.9 ms | 72516.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 99592.9 ms | 97752.5 ms | 1840.4 ms | 72167.5 ms |
| IXGo | Go | 85280.1 ms | 80106.3 ms | 5173.9 ms | 23385.7 ms |
| Aws_restjson | LLGoNoLTO | 85040.1 ms | 82954.5 ms | 2085.6 ms | 39150.0 ms |
| Aws_restjson | LLGoDeadcodeDrop | 84564.1 ms | 82408.2 ms | 2155.9 ms | 38839.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 64759.7 ms | 63382.8 ms | 1376.9 ms | 43893.9 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 63963.4 ms | 62525.7 ms | 1437.7 ms | 43338.3 ms |
| Uber_zap | LLGoDeadcodeDrop | 58768.2 ms | 57213.2 ms | 1555.0 ms | 25037.8 ms |
| Uber_zap | LLGoNoLTO | 57233.5 ms | 55739.8 ms | 1493.7 ms | 24445.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 54164.3 ms | 52800.4 ms | 1363.9 ms | 33153.1 ms |
| Toml | LLGoFullLTONoGlobalDCE | 49677.0 ms | 48507.7 ms | 1169.3 ms | 37266.5 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 43314.5 ms | 42291.2 ms | 1023.2 ms | 30149.0 ms |
| Toml | LLGoFullLTOGlobalDCE | 42142.3 ms | 41084.9 ms | 1057.3 ms | 29182.8 ms |
| Gorm_schema | LLGoDeadcodeDrop | 40521.1 ms | 39270.1 ms | 1251.0 ms | 13459.7 ms |
| Gorm_schema | LLGoNoLTO | 40196.3 ms | 38918.8 ms | 1277.4 ms | 13459.9 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 35586.0 ms | 34709.9 ms | 876.1 ms | 27629.8 ms |
| Etcdctl | Go | 33989.2 ms | 31903.7 ms | 2085.4 ms | 10263.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 26679.3 ms | 25859.6 ms | 819.7 ms | 18554.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 26164.3 ms | 25317.5 ms | 846.7 ms | 18303.7 ms |
| Toml | LLGoDeadcodeDrop | 25058.2 ms | 24054.0 ms | 1004.2 ms | 9434.7 ms |
| Toml | LLGoNoLTO | 24565.8 ms | 23553.9 ms | 1011.9 ms | 9235.4 ms |
| XGo | Go | 19503.3 ms | 18249.3 ms | 1254.0 ms | 5916.8 ms |
| Dustin_humanize | LLGoNoLTO | 14293.5 ms | 13534.0 ms | 759.5 ms | 6117.2 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 14051.3 ms | 13285.1 ms | 766.2 ms | 6067.7 ms |
| Aws_restjson | Go | 8040.6 ms | 7381.5 ms | 659.1 ms | 3287.9 ms |
| Gorm_schema | Go | 6160.9 ms | 5693.6 ms | 467.3 ms | 2661.8 ms |
| Uber_zap | Go | 5309.0 ms | 4869.0 ms | 440.0 ms | 2072.0 ms |
| K8s_workqueue | Go | 4883.4 ms | 4386.8 ms | 496.6 ms | 1889.9 ms |
| Toml | Go | 2127.2 ms | 1892.6 ms | 234.6 ms | 978.9 ms |
| Dustin_humanize | Go | 841.3 ms | 677.2 ms | 164.1 ms | 399.8 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTOGlobalDCE | 1433797.7 ms | 862186.1 ms | 8 |
| LLGoFullLTONoGlobalDCE | 1420555.5 ms | 882204.3 ms | 8 |
| LLGoFullLTOGlobalDCEPlugin | 1412364.3 ms | 839574.3 ms | 8 |
| LLGoNoLTO | 1004370.5 ms | 338430.5 ms | 8 |
| LLGoDeadcodeDrop | 986650.6 ms | 332710.6 ms | 8 |
| Go | 166135.0 ms | 50856.5 ms | 9 |

Dependency download details are in `download-timings.log`.
