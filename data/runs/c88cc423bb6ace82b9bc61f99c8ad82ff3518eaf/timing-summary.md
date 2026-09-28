## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 602995.9 ms | 581416.8 ms | 21579.1 ms | 317941.9 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 553711.9 ms | 539633.9 ms | 14078.0 ms | 288184.6 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 532447.3 ms | 519144.0 ms | 13303.2 ms | 286776.0 ms |
| IXGo | LLGoNoLTO | 455720.2 ms | 444759.7 ms | 10960.5 ms | 135988.0 ms |
| IXGo | LLGoDeadcodeDrop | 441664.8 ms | 430110.7 ms | 11554.1 ms | 130131.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 264373.1 ms | 258844.3 ms | 5528.8 ms | 165863.2 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 253539.5 ms | 248289.5 ms | 5250.1 ms | 160259.5 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 250107.7 ms | 244535.8 ms | 5571.9 ms | 156938.1 ms |
| Etcdctl | LLGoDeadcodeDrop | 190755.9 ms | 185771.0 ms | 4984.9 ms | 64384.9 ms |
| Etcdctl | LLGoNoLTO | 185548.2 ms | 180696.1 ms | 4852.1 ms | 62167.6 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 180735.4 ms | 176902.4 ms | 3833.1 ms | 126263.5 ms |
| XGo | LLGoFullLTOGlobalDCE | 177971.1 ms | 174247.7 ms | 3723.4 ms | 124034.0 ms |
| XGo | LLGoFullLTONoGlobalDCE | 177041.8 ms | 173514.7 ms | 3527.0 ms | 125496.5 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 138721.8 ms | 136097.8 ms | 2624.0 ms | 103618.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 133213.9 ms | 130467.6 ms | 2746.3 ms | 96572.1 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 123160.7 ms | 120706.1 ms | 2454.6 ms | 87723.9 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 109248.4 ms | 107277.9 ms | 1970.5 ms | 83637.6 ms |
| XGo | LLGoDeadcodeDrop | 108482.5 ms | 105162.1 ms | 3320.4 ms | 41831.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 107396.2 ms | 105147.7 ms | 2248.5 ms | 84564.5 ms |
| XGo | LLGoNoLTO | 106294.3 ms | 102987.0 ms | 3307.2 ms | 41467.6 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 103165.3 ms | 101020.2 ms | 2145.1 ms | 81739.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 101740.3 ms | 99664.4 ms | 2075.9 ms | 75591.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 98617.4 ms | 96533.4 ms | 2084.0 ms | 73175.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 90058.0 ms | 87912.8 ms | 2145.1 ms | 67907.0 ms |
| Aws_restjson | LLGoDeadcodeDrop | 86047.0 ms | 83600.2 ms | 2446.7 ms | 42309.2 ms |
| Aws_restjson | LLGoNoLTO | 82799.0 ms | 80520.1 ms | 2278.9 ms | 41003.1 ms |
| IXGo | Go | 81427.0 ms | 75825.4 ms | 5601.6 ms | 22492.0 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 62355.7 ms | 60798.4 ms | 1557.3 ms | 43733.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 61557.4 ms | 59971.7 ms | 1585.7 ms | 42144.2 ms |
| Uber_zap | LLGoNoLTO | 56823.5 ms | 55116.9 ms | 1706.6 ms | 25731.0 ms |
| Uber_zap | LLGoDeadcodeDrop | 55766.0 ms | 54124.2 ms | 1641.8 ms | 25141.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 50565.6 ms | 49088.7 ms | 1476.9 ms | 31407.2 ms |
| Toml | LLGoFullLTONoGlobalDCE | 49093.8 ms | 47827.3 ms | 1266.5 ms | 37614.5 ms |
| K8s_workqueue | LLGoNoLTO | 48345.7 ms | 46704.0 ms | 1641.6 ms | 22938.1 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 47928.9 ms | 46368.4 ms | 1560.6 ms | 22581.8 ms |
| Toml | LLGoFullLTOGlobalDCE | 41939.9 ms | 40724.8 ms | 1215.0 ms | 30193.8 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 41332.1 ms | 40120.5 ms | 1211.6 ms | 29078.8 ms |
| Gorm_schema | LLGoDeadcodeDrop | 38274.0 ms | 36862.4 ms | 1411.7 ms | 13068.3 ms |
| Gorm_schema | LLGoNoLTO | 37696.7 ms | 36400.9 ms | 1295.8 ms | 12658.6 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 35247.7 ms | 34297.8 ms | 949.9 ms | 27985.2 ms |
| Etcdctl | Go | 32884.2 ms | 30550.0 ms | 2334.3 ms | 9922.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 26847.6 ms | 25821.6 ms | 1026.0 ms | 19367.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 26572.2 ms | 25583.7 ms | 988.5 ms | 19106.2 ms |
| Toml | LLGoDeadcodeDrop | 23747.3 ms | 22687.2 ms | 1060.1 ms | 9143.9 ms |
| Toml | LLGoNoLTO | 22781.5 ms | 21657.6 ms | 1124.0 ms | 8832.4 ms |
| XGo | Go | 18306.0 ms | 17029.5 ms | 1276.5 ms | 5416.9 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 13960.0 ms | 13066.2 ms | 893.8 ms | 6126.5 ms |
| Dustin_humanize | LLGoNoLTO | 13607.3 ms | 12736.7 ms | 870.6 ms | 5868.4 ms |
| Aws_restjson | Go | 7952.7 ms | 7155.7 ms | 797.0 ms | 3347.3 ms |
| Gorm_schema | Go | 5660.2 ms | 5128.1 ms | 532.1 ms | 2393.1 ms |
| Uber_zap | Go | 5276.5 ms | 4831.5 ms | 445.1 ms | 2074.5 ms |
| K8s_workqueue | Go | 4754.5 ms | 4200.3 ms | 554.1 ms | 1785.2 ms |
| Toml | Go | 1986.5 ms | 1749.6 ms | 236.9 ms | 906.1 ms |
| Dustin_humanize | Go | 817.0 ms | 646.9 ms | 170.1 ms | 398.1 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTOGlobalDCE | 1490318.5 ms | 935822.0 ms | 9 |
| LLGoFullLTONoGlobalDCE | 1460861.3 ms | 950860.8 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1442577.9 ms | 900235.1 ms | 9 |
| LLGoNoLTO | 1009616.3 ms | 356654.8 ms | 9 |
| LLGoDeadcodeDrop | 1006626.4 ms | 354718.9 ms | 9 |
| Go | 159064.6 ms | 48735.6 ms | 9 |

Dependency download details are in `download-timings.log`.
