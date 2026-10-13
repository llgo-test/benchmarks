## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 583374.0 ms | 574005.9 ms | 9368.0 ms | 294606.5 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 545260.7 ms | 534707.8 ms | 10552.9 ms | 283719.6 ms |
| IXGo | LLGoNoLTO | 534635.1 ms | 526378.5 ms | 8256.7 ms | 174233.0 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 496473.6 ms | 486290.3 ms | 10183.3 ms | 266915.6 ms |
| IXGo | LLGoDeadcodeDrop | 467040.8 ms | 456205.0 ms | 10835.8 ms | 136344.1 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 273981.2 ms | 268601.3 ms | 5379.9 ms | 174414.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 240049.2 ms | 235493.9 ms | 4555.3 ms | 155910.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 232364.4 ms | 227912.9 ms | 4451.5 ms | 149364.5 ms |
| Aws_restjson | LLGoNoLTO | 203570.4 ms | 200814.9 ms | 2755.5 ms | 66189.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 187792.0 ms | 184851.8 ms | 2940.2 ms | 103994.0 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 186337.8 ms | 183312.8 ms | 3025.1 ms | 113264.5 ms |
| Aws_restjson | LLGoDeadcodeDrop | 186172.5 ms | 183065.0 ms | 3107.5 ms | 65064.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 175935.5 ms | 172991.5 ms | 2944.0 ms | 100634.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 173061.2 ms | 169993.5 ms | 3067.7 ms | 105564.8 ms |
| XGo | LLGoFullLTONoGlobalDCE | 170685.8 ms | 167611.8 ms | 3074.0 ms | 125569.2 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 170673.7 ms | 167560.1 ms | 3113.6 ms | 123859.5 ms |
| Etcdctl | LLGoNoLTO | 170152.3 ms | 166217.2 ms | 3935.1 ms | 56290.6 ms |
| XGo | LLGoFullLTOGlobalDCE | 169835.1 ms | 166721.6 ms | 3113.5 ms | 123332.7 ms |
| Etcdctl | LLGoDeadcodeDrop | 164180.3 ms | 159616.5 ms | 4563.8 ms | 55911.2 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 161886.8 ms | 159216.4 ms | 2670.3 ms | 104758.7 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 157089.8 ms | 154283.9 ms | 2805.9 ms | 102412.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 154084.2 ms | 151331.7 ms | 2752.5 ms | 98480.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 152106.8 ms | 149449.9 ms | 2656.8 ms | 93625.2 ms |
| Uber_zap | LLGoDeadcodeDrop | 149494.2 ms | 146840.7 ms | 2653.5 ms | 56877.2 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 146324.7 ms | 143627.9 ms | 2696.8 ms | 55378.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 146308.8 ms | 143513.1 ms | 2795.7 ms | 88610.7 ms |
| Uber_zap | LLGoNoLTO | 144480.5 ms | 142224.8 ms | 2255.7 ms | 54168.6 ms |
| K8s_workqueue | LLGoNoLTO | 139893.9 ms | 137423.2 ms | 2470.6 ms | 53251.5 ms |
| XGo | LLGoDeadcodeDrop | 96070.8 ms | 92784.6 ms | 3286.2 ms | 36522.6 ms |
| XGo | LLGoNoLTO | 93774.8 ms | 91232.8 ms | 2542.0 ms | 35499.0 ms |
| Gorm_schema | LLGoNoLTO | 90001.0 ms | 88258.8 ms | 1742.2 ms | 29567.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 83111.6 ms | 81340.0 ms | 1771.7 ms | 50541.5 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 77944.6 ms | 76187.7 ms | 1757.0 ms | 47880.7 ms |
| Toml | LLGoFullLTONoGlobalDCE | 77013.5 ms | 75223.2 ms | 1790.3 ms | 46992.3 ms |
| Gorm_schema | LLGoDeadcodeDrop | 76153.1 ms | 74451.3 ms | 1701.9 ms | 25533.7 ms |
| Toml | LLGoDeadcodeDrop | 74184.1 ms | 72364.8 ms | 1819.2 ms | 24889.4 ms |
| Toml | LLGoNoLTO | 71741.0 ms | 70125.5 ms | 1615.5 ms | 23623.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 69114.5 ms | 67579.2 ms | 1535.4 ms | 37424.6 ms |
| Toml | LLGoFullLTOGlobalDCE | 67869.5 ms | 66176.2 ms | 1693.3 ms | 37872.3 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 66410.1 ms | 64669.5 ms | 1740.5 ms | 36907.4 ms |
| IXGo | Go | 62848.0 ms | 58638.8 ms | 4209.2 ms | 18301.6 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 53131.9 ms | 51920.2 ms | 1211.7 ms | 34238.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 52986.7 ms | 51561.8 ms | 1424.9 ms | 29690.7 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 49628.9 ms | 48437.9 ms | 1191.0 ms | 18247.3 ms |
| Dustin_humanize | LLGoNoLTO | 48941.5 ms | 47844.7 ms | 1096.9 ms | 17753.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 42828.8 ms | 41694.5 ms | 1134.2 ms | 24363.2 ms |
| Etcdctl | Go | 25815.7 ms | 24017.5 ms | 1798.3 ms | 8009.9 ms |
| XGo | Go | 14637.2 ms | 13595.9 ms | 1041.3 ms | 5334.3 ms |
| Aws_restjson | Go | 6006.7 ms | 5419.6 ms | 587.1 ms | 2931.3 ms |
| Gorm_schema | Go | 4340.1 ms | 4017.5 ms | 322.7 ms | 1671.9 ms |
| Uber_zap | Go | 4120.8 ms | 3765.7 ms | 355.2 ms | 1651.3 ms |
| K8s_workqueue | Go | 3822.0 ms | 3386.0 ms | 436.0 ms | 1408.7 ms |
| Toml | Go | 1559.2 ms | 1369.2 ms | 190.0 ms | 726.5 ms |
| Dustin_humanize | Go | 635.1 ms | 520.2 ms | 114.9 ms | 305.4 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTOGlobalDCE | 1683524.3 ms | 981507.9 ms | 9 |
| LLGoFullLTONoGlobalDCE | 1654545.0 ms | 1016446.5 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1629642.4 ms | 956995.2 ms | 9 |
| LLGoNoLTO | 1497190.6 ms | 510576.1 ms | 9 |
| LLGoDeadcodeDrop | 1409249.4 ms | 474768.1 ms | 9 |
| Go | 123784.8 ms | 40340.9 ms | 9 |

Dependency download details are in `download-timings.log`.
