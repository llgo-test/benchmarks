## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTONoGlobalDCE | 586316.7 ms | 580565.0 ms | 5751.7 ms | 382929.2 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 537446.0 ms | 531465.3 ms | 5980.7 ms | 362871.2 ms |
| IXGo | LLGoFullLTOGlobalDCE | 533210.4 ms | 526974.1 ms | 6236.4 ms | 361127.7 ms |
| IXGo | LLGoNoLTO | 361753.0 ms | 356627.0 ms | 5126.0 ms | 121022.4 ms |
| IXGo | LLGoDeadcodeDrop | 337276.1 ms | 332081.0 ms | 5195.1 ms | 114525.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 214041.6 ms | 209879.7 ms | 4161.9 ms | 133243.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 213313.0 ms | 209288.8 ms | 4024.2 ms | 133151.4 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 206572.2 ms | 202613.6 ms | 3958.6 ms | 129700.0 ms |
| Etcdctl | LLGoDeadcodeDrop | 155183.1 ms | 151523.0 ms | 3660.1 ms | 52296.2 ms |
| Etcdctl | LLGoNoLTO | 153554.1 ms | 149864.6 ms | 3689.5 ms | 50918.6 ms |
| XGo | LLGoFullLTONoGlobalDCE | 146966.2 ms | 144248.3 ms | 2717.9 ms | 105623.2 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 143228.8 ms | 140381.9 ms | 2846.9 ms | 101794.9 ms |
| XGo | LLGoFullLTOGlobalDCE | 143005.4 ms | 140299.2 ms | 2706.2 ms | 101828.3 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 112102.5 ms | 110195.1 ms | 1907.4 ms | 84947.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 102907.6 ms | 101019.4 ms | 1888.1 ms | 74673.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 99753.9 ms | 97743.5 ms | 2010.4 ms | 71628.5 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 91619.3 ms | 90053.3 ms | 1566.0 ms | 71678.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 87378.3 ms | 85818.4 ms | 1559.8 ms | 69897.1 ms |
| XGo | LLGoDeadcodeDrop | 83246.3 ms | 80898.9 ms | 2347.4 ms | 32122.7 ms |
| XGo | LLGoNoLTO | 81772.9 ms | 79507.5 ms | 2265.4 ms | 31604.1 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 81645.8 ms | 80242.2 ms | 1403.6 ms | 65129.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 81052.4 ms | 79481.9 ms | 1570.5 ms | 61032.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 80211.8 ms | 78556.1 ms | 1655.7 ms | 60650.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 72863.2 ms | 71423.5 ms | 1439.8 ms | 55697.8 ms |
| Aws_restjson | LLGoDeadcodeDrop | 68610.6 ms | 66952.6 ms | 1658.0 ms | 34933.5 ms |
| Aws_restjson | LLGoNoLTO | 67755.1 ms | 66020.7 ms | 1734.3 ms | 33240.3 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 52851.4 ms | 51717.8 ms | 1133.6 ms | 37733.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 50176.2 ms | 49063.3 ms | 1113.0 ms | 35644.1 ms |
| Uber_zap | LLGoDeadcodeDrop | 45319.8 ms | 43975.8 ms | 1344.0 ms | 20135.7 ms |
| Uber_zap | LLGoNoLTO | 44030.8 ms | 42780.1 ms | 1250.7 ms | 19605.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 43964.6 ms | 42778.1 ms | 1186.5 ms | 28675.4 ms |
| Toml | LLGoFullLTONoGlobalDCE | 39965.0 ms | 39100.3 ms | 864.8 ms | 31336.4 ms |
| K8s_workqueue | LLGoNoLTO | 38447.0 ms | 37259.3 ms | 1187.7 ms | 18252.4 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 37801.0 ms | 36504.6 ms | 1296.4 ms | 18202.4 ms |
| Toml | LLGoFullLTOGlobalDCE | 35353.4 ms | 34457.2 ms | 896.2 ms | 25930.4 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 34483.8 ms | 33601.3 ms | 882.4 ms | 25594.2 ms |
| IXGo | Go | 33934.7 ms | 31466.6 ms | 2468.1 ms | 9917.1 ms |
| Gorm_schema | LLGoNoLTO | 29117.5 ms | 28066.3 ms | 1051.2 ms | 9734.4 ms |
| Gorm_schema | LLGoDeadcodeDrop | 28683.2 ms | 27687.4 ms | 995.8 ms | 9539.5 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 25949.2 ms | 25230.7 ms | 718.5 ms | 20771.5 ms |
| Etcdctl | Go | 24990.3 ms | 23346.4 ms | 1643.9 ms | 7488.5 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 20332.9 ms | 19672.3 ms | 660.6 ms | 14857.9 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 19595.9 ms | 18948.0 ms | 647.9 ms | 13934.1 ms |
| Toml | LLGoDeadcodeDrop | 18988.6 ms | 18160.4 ms | 828.2 ms | 7271.1 ms |
| Toml | LLGoNoLTO | 17582.8 ms | 16793.0 ms | 789.8 ms | 6693.8 ms |
| XGo | Go | 14392.2 ms | 13440.5 ms | 951.7 ms | 4265.2 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 10251.2 ms | 9651.5 ms | 599.7 ms | 4619.2 ms |
| Dustin_humanize | LLGoNoLTO | 9860.4 ms | 9264.2 ms | 596.2 ms | 4391.4 ms |
| Aws_restjson | Go | 5920.5 ms | 5370.5 ms | 550.1 ms | 2443.1 ms |
| Gorm_schema | Go | 4346.4 ms | 4010.1 ms | 336.4 ms | 1682.1 ms |
| Uber_zap | Go | 4024.8 ms | 3646.8 ms | 378.0 ms | 1604.3 ms |
| K8s_workqueue | Go | 3526.0 ms | 3137.5 ms | 388.6 ms | 1274.9 ms |
| Toml | Go | 1640.7 ms | 1442.5 ms | 198.1 ms | 779.9 ms |
| Dustin_humanize | Go | 605.7 ms | 480.6 ms | 125.1 ms | 292.0 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1343988.6 ms | 929849.5 ms | 9 |
| LLGoFullLTOGlobalDCE | 1266617.6 ms | 877853.4 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1245701.6 ms | 854379.6 ms | 9 |
| LLGoNoLTO | 803873.5 ms | 295462.6 ms | 9 |
| LLGoDeadcodeDrop | 785359.9 ms | 293645.7 ms | 9 |
| Go | 93381.3 ms | 29747.3 ms | 9 |

Dependency download details are in `download-timings.log`.
