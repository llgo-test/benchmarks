## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 498491.5 ms | 488689.3 ms | 9802.3 ms | 266831.1 ms |
| IXGo | LLGoFullLTOGlobalDCE | 492678.1 ms | 482727.7 ms | 9950.4 ms | 262005.2 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 476471.4 ms | 467125.4 ms | 9346.0 ms | 259034.9 ms |
| IXGo | LLGoDeadcodeDrop | 369734.4 ms | 357817.3 ms | 11917.1 ms | 112095.5 ms |
| IXGo | LLGoNoLTO | 355857.2 ms | 346386.4 ms | 9470.8 ms | 103772.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 225882.8 ms | 221573.9 ms | 4308.9 ms | 146543.6 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 223809.1 ms | 219549.9 ms | 4259.3 ms | 146095.5 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 223441.0 ms | 219090.7 ms | 4350.2 ms | 145162.2 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 177999.7 ms | 175109.4 ms | 2890.3 ms | 110188.3 ms |
| Aws_restjson | LLGoDeadcodeDrop | 172892.4 ms | 169943.4 ms | 2949.0 ms | 61295.3 ms |
| Aws_restjson | LLGoNoLTO | 169737.6 ms | 167095.7 ms | 2641.9 ms | 59694.3 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 167044.6 ms | 164223.6 ms | 2820.9 ms | 96916.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 166792.9 ms | 163807.5 ms | 2985.4 ms | 97316.8 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 159794.7 ms | 156832.4 ms | 2962.3 ms | 116063.3 ms |
| XGo | LLGoFullLTONoGlobalDCE | 159529.6 ms | 156537.6 ms | 2992.0 ms | 117357.0 ms |
| Etcdctl | LLGoDeadcodeDrop | 159094.5 ms | 154569.7 ms | 4524.8 ms | 55492.0 ms |
| XGo | LLGoFullLTOGlobalDCE | 158687.0 ms | 155757.1 ms | 2930.0 ms | 114762.0 ms |
| Etcdctl | LLGoNoLTO | 156285.7 ms | 152689.6 ms | 3596.1 ms | 52542.3 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 148947.9 ms | 146428.3 ms | 2519.5 ms | 96911.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 145027.8 ms | 142468.4 ms | 2559.4 ms | 93285.0 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 143840.1 ms | 141235.0 ms | 2605.1 ms | 93838.7 ms |
| Uber_zap | LLGoNoLTO | 141351.5 ms | 139172.0 ms | 2179.5 ms | 53059.4 ms |
| Uber_zap | LLGoDeadcodeDrop | 141240.8 ms | 138822.0 ms | 2418.8 ms | 53749.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 141198.3 ms | 138767.0 ms | 2431.3 ms | 86294.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 139312.0 ms | 136909.7 ms | 2402.4 ms | 85921.9 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 136013.7 ms | 133571.4 ms | 2442.4 ms | 52194.1 ms |
| K8s_workqueue | LLGoNoLTO | 135890.2 ms | 133554.2 ms | 2336.0 ms | 54014.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 132793.0 ms | 130285.2 ms | 2507.9 ms | 80516.4 ms |
| XGo | LLGoDeadcodeDrop | 90987.9 ms | 87895.3 ms | 3092.6 ms | 35131.4 ms |
| XGo | LLGoNoLTO | 89709.3 ms | 87324.0 ms | 2385.3 ms | 33661.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 75485.6 ms | 73886.5 ms | 1599.1 ms | 45676.9 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 75356.9 ms | 73761.3 ms | 1595.6 ms | 46079.6 ms |
| Gorm_schema | LLGoDeadcodeDrop | 74522.8 ms | 72847.2 ms | 1675.5 ms | 25179.0 ms |
| Gorm_schema | LLGoNoLTO | 73666.3 ms | 72270.2 ms | 1396.1 ms | 24325.1 ms |
| Toml | LLGoFullLTONoGlobalDCE | 69973.3 ms | 68317.0 ms | 1656.3 ms | 42153.2 ms |
| Toml | LLGoDeadcodeDrop | 69784.2 ms | 68109.2 ms | 1675.0 ms | 23312.0 ms |
| Toml | LLGoNoLTO | 69593.2 ms | 68020.7 ms | 1572.5 ms | 22813.7 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 66613.0 ms | 65136.1 ms | 1476.9 ms | 35952.8 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 63226.7 ms | 61595.0 ms | 1631.7 ms | 34832.8 ms |
| Toml | LLGoFullLTOGlobalDCE | 63033.0 ms | 61416.0 ms | 1617.1 ms | 34751.5 ms |
| IXGo | Go | 61998.7 ms | 57837.5 ms | 4161.2 ms | 17095.1 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 48939.7 ms | 47776.6 ms | 1163.0 ms | 31267.0 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 47948.6 ms | 46778.7 ms | 1170.0 ms | 17443.7 ms |
| Dustin_humanize | LLGoNoLTO | 47445.5 ms | 46422.1 ms | 1023.4 ms | 17050.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 41458.7 ms | 40306.8 ms | 1151.9 ms | 23509.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 41274.4 ms | 40175.7 ms | 1098.7 ms | 23147.8 ms |
| Etcdctl | Go | 24854.5 ms | 23258.3 ms | 1596.1 ms | 7566.1 ms |
| XGo | Go | 14316.1 ms | 13318.1 ms | 998.0 ms | 4186.6 ms |
| Aws_restjson | Go | 5832.1 ms | 5260.9 ms | 571.2 ms | 3163.5 ms |
| Gorm_schema | Go | 4258.2 ms | 3933.2 ms | 325.0 ms | 1628.6 ms |
| Uber_zap | Go | 3937.7 ms | 3607.6 ms | 330.2 ms | 1562.0 ms |
| K8s_workqueue | Go | 3487.5 ms | 3133.8 ms | 353.7 ms | 1252.9 ms |
| Toml | Go | 1503.7 ms | 1323.9 ms | 179.8 ms | 688.9 ms |
| Dustin_humanize | Go | 623.7 ms | 494.0 ms | 129.8 ms | 307.0 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1524867.7 ms | 942925.1 ms | 9 |
| LLGoFullLTOGlobalDCE | 1505731.9 ms | 902029.2 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1496503.2 ms | 887459.9 ms | 9 |
| LLGoDeadcodeDrop | 1262219.3 ms | 435892.7 ms | 9 |
| LLGoNoLTO | 1239536.6 ms | 420933.7 ms | 9 |
| Go | 120812.4 ms | 37450.6 ms | 9 |

Dependency download details are in `download-timings.log`.
