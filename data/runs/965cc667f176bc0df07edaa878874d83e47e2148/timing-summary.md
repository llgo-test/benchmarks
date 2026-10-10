## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 555575.3 ms | 545065.4 ms | 10509.9 ms | 295207.5 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 547416.2 ms | 537050.5 ms | 10365.7 ms | 294848.9 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 546068.3 ms | 536268.4 ms | 9799.9 ms | 291859.4 ms |
| IXGo | LLGoDeadcodeDrop | 435239.2 ms | 422517.3 ms | 12721.9 ms | 128625.9 ms |
| IXGo | LLGoNoLTO | 408452.1 ms | 399337.9 ms | 9114.2 ms | 117788.5 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 260434.3 ms | 255774.8 ms | 4659.5 ms | 168027.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 255690.7 ms | 251176.7 ms | 4514.0 ms | 164744.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 255129.5 ms | 250493.7 ms | 4635.8 ms | 164411.9 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 203951.6 ms | 200715.8 ms | 3235.8 ms | 126020.4 ms |
| Aws_restjson | LLGoDeadcodeDrop | 200718.4 ms | 197915.6 ms | 2802.9 ms | 69624.2 ms |
| Aws_restjson | LLGoNoLTO | 198665.2 ms | 195869.4 ms | 2795.8 ms | 68969.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 191563.0 ms | 188560.3 ms | 3002.7 ms | 111349.1 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 189336.2 ms | 186211.4 ms | 3124.8 ms | 109681.1 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 186128.2 ms | 182964.6 ms | 3163.7 ms | 133908.7 ms |
| Etcdctl | LLGoDeadcodeDrop | 180146.4 ms | 175746.3 ms | 4400.1 ms | 60052.0 ms |
| Etcdctl | LLGoNoLTO | 180005.8 ms | 175913.7 ms | 4092.2 ms | 58291.9 ms |
| XGo | LLGoFullLTOGlobalDCE | 177831.1 ms | 174752.1 ms | 3079.0 ms | 126787.7 ms |
| XGo | LLGoFullLTONoGlobalDCE | 174005.0 ms | 170952.5 ms | 3052.6 ms | 126467.7 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 165130.5 ms | 162507.3 ms | 2623.2 ms | 107600.1 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 161086.5 ms | 158392.0 ms | 2694.4 ms | 103822.1 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 161083.7 ms | 158429.2 ms | 2654.5 ms | 105260.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 160625.5 ms | 157979.9 ms | 2645.7 ms | 98957.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 159986.7 ms | 157355.7 ms | 2631.0 ms | 98447.8 ms |
| Uber_zap | LLGoDeadcodeDrop | 157883.3 ms | 155662.1 ms | 2221.3 ms | 58659.0 ms |
| Uber_zap | LLGoNoLTO | 157400.4 ms | 155169.9 ms | 2230.5 ms | 58323.5 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 151883.2 ms | 149556.1 ms | 2327.1 ms | 56486.9 ms |
| K8s_workqueue | LLGoNoLTO | 149864.5 ms | 147577.3 ms | 2287.2 ms | 55926.1 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 148091.9 ms | 145352.0 ms | 2739.9 ms | 90103.2 ms |
| XGo | LLGoDeadcodeDrop | 104904.6 ms | 101924.1 ms | 2980.5 ms | 38688.7 ms |
| XGo | LLGoNoLTO | 102238.1 ms | 99782.3 ms | 2455.8 ms | 37067.5 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 87477.2 ms | 85781.6 ms | 1695.6 ms | 53989.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 86965.4 ms | 85253.6 ms | 1711.7 ms | 53047.5 ms |
| Gorm_schema | LLGoDeadcodeDrop | 84949.3 ms | 83449.4 ms | 1499.8 ms | 28186.4 ms |
| Gorm_schema | LLGoNoLTO | 83550.2 ms | 82079.7 ms | 1470.5 ms | 27933.7 ms |
| Toml | LLGoDeadcodeDrop | 78524.2 ms | 77077.8 ms | 1446.4 ms | 26129.2 ms |
| Toml | LLGoNoLTO | 77828.7 ms | 76380.4 ms | 1448.4 ms | 26135.1 ms |
| Toml | LLGoFullLTONoGlobalDCE | 77313.5 ms | 75683.9 ms | 1629.6 ms | 47416.7 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 74068.7 ms | 72415.7 ms | 1653.1 ms | 40403.7 ms |
| IXGo | Go | 73449.3 ms | 68127.0 ms | 5322.3 ms | 19993.8 ms |
| Toml | LLGoFullLTOGlobalDCE | 70823.3 ms | 69266.1 ms | 1557.2 ms | 39396.9 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 69769.9 ms | 68258.4 ms | 1511.5 ms | 38789.3 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 55423.4 ms | 54212.8 ms | 1210.6 ms | 35482.3 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 54038.9 ms | 53013.6 ms | 1025.3 ms | 19497.4 ms |
| Dustin_humanize | LLGoNoLTO | 53629.0 ms | 52633.9 ms | 995.1 ms | 19354.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 46559.3 ms | 45464.4 ms | 1094.9 ms | 26419.5 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 45747.9 ms | 44647.7 ms | 1100.2 ms | 25662.1 ms |
| Etcdctl | Go | 28814.8 ms | 26860.9 ms | 1953.9 ms | 8513.8 ms |
| XGo | Go | 16887.5 ms | 15734.3 ms | 1153.2 ms | 4943.6 ms |
| Aws_restjson | Go | 6890.9 ms | 6306.9 ms | 584.0 ms | 2736.9 ms |
| Gorm_schema | Go | 5173.2 ms | 4785.6 ms | 387.7 ms | 1945.0 ms |
| Uber_zap | Go | 4639.8 ms | 4303.8 ms | 336.0 ms | 1764.9 ms |
| K8s_workqueue | Go | 4110.3 ms | 3683.1 ms | 427.2 ms | 1835.5 ms |
| Toml | Go | 1800.4 ms | 1573.6 ms | 226.8 ms | 991.7 ms |
| Dustin_humanize | Go | 720.9 ms | 599.2 ms | 121.7 ms | 340.5 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1732235.4 ms | 1065113.1 ms | 9 |
| LLGoFullLTOGlobalDCE | 1703043.1 ms | 1016796.7 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1678004.4 ms | 996201.9 ms | 9 |
| LLGoDeadcodeDrop | 1448287.5 ms | 485949.7 ms | 9 |
| LLGoNoLTO | 1411634.0 ms | 469790.8 ms | 9 |
| Go | 142487.1 ms | 43065.8 ms | 9 |

Dependency download details are in `download-timings.log`.
