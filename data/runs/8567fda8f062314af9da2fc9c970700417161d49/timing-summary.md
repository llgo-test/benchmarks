## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 575526.6 ms | 563393.3 ms | 12133.3 ms | 295291.0 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 555706.7 ms | 543373.2 ms | 12333.5 ms | 285091.7 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 542842.1 ms | 530710.5 ms | 12131.7 ms | 283030.1 ms |
| IXGo | LLGoNoLTO | 443387.7 ms | 433253.4 ms | 10134.3 ms | 129965.3 ms |
| IXGo | LLGoDeadcodeDrop | 423302.1 ms | 412477.6 ms | 10824.5 ms | 132467.6 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 265550.0 ms | 260529.4 ms | 5020.6 ms | 163832.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 254723.6 ms | 250020.1 ms | 4703.5 ms | 155133.1 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 252955.9 ms | 248462.0 ms | 4493.9 ms | 155431.6 ms |
| Etcdctl | LLGoDeadcodeDrop | 199610.2 ms | 195354.6 ms | 4255.6 ms | 65535.1 ms |
| Etcdctl | LLGoNoLTO | 187305.8 ms | 183309.5 ms | 3996.4 ms | 61913.9 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 186134.8 ms | 182716.7 ms | 3418.1 ms | 128319.7 ms |
| XGo | LLGoFullLTONoGlobalDCE | 180211.7 ms | 176872.3 ms | 3339.4 ms | 125383.6 ms |
| XGo | LLGoFullLTOGlobalDCE | 178501.0 ms | 175253.1 ms | 3247.9 ms | 121773.8 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 138822.5 ms | 136224.2 ms | 2598.3 ms | 101297.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 128173.5 ms | 125587.4 ms | 2586.1 ms | 88729.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 127390.1 ms | 124769.7 ms | 2620.4 ms | 87973.4 ms |
| XGo | LLGoDeadcodeDrop | 113101.9 ms | 109964.0 ms | 3137.8 ms | 42083.0 ms |
| XGo | LLGoNoLTO | 110684.9 ms | 107763.9 ms | 2921.0 ms | 41070.1 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 106513.1 ms | 104817.2 ms | 1695.8 ms | 80764.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 103622.1 ms | 101494.1 ms | 2128.0 ms | 80136.2 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 100897.7 ms | 99056.6 ms | 1841.1 ms | 78016.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 100431.9 ms | 98585.7 ms | 1846.3 ms | 72670.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 98728.9 ms | 96912.0 ms | 1816.9 ms | 71055.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 88221.4 ms | 86435.2 ms | 1786.2 ms | 64729.2 ms |
| Aws_restjson | LLGoDeadcodeDrop | 87247.1 ms | 85035.0 ms | 2212.1 ms | 39935.9 ms |
| IXGo | Go | 85307.5 ms | 79947.0 ms | 5360.6 ms | 24857.9 ms |
| Aws_restjson | LLGoNoLTO | 81676.7 ms | 79625.4 ms | 2051.3 ms | 36624.4 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 65810.4 ms | 64342.7 ms | 1467.7 ms | 45411.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 61736.8 ms | 60278.6 ms | 1458.2 ms | 41879.4 ms |
| Uber_zap | LLGoDeadcodeDrop | 58460.1 ms | 56844.5 ms | 1615.6 ms | 25050.0 ms |
| Uber_zap | LLGoNoLTO | 57366.3 ms | 55705.9 ms | 1660.4 ms | 24687.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 52075.6 ms | 50661.5 ms | 1414.1 ms | 31775.0 ms |
| K8s_workqueue | LLGoNoLTO | 50106.1 ms | 48443.8 ms | 1662.3 ms | 23034.7 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 50010.1 ms | 48416.1 ms | 1594.0 ms | 22522.9 ms |
| Toml | LLGoFullLTONoGlobalDCE | 48833.4 ms | 47610.4 ms | 1223.0 ms | 36605.5 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 43301.3 ms | 42202.2 ms | 1099.1 ms | 30088.7 ms |
| Toml | LLGoFullLTOGlobalDCE | 42023.7 ms | 40840.1 ms | 1183.6 ms | 29663.5 ms |
| Gorm_schema | LLGoDeadcodeDrop | 41696.8 ms | 40386.5 ms | 1310.4 ms | 13917.1 ms |
| Gorm_schema | LLGoNoLTO | 39017.2 ms | 37772.3 ms | 1245.0 ms | 13054.4 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 35727.2 ms | 34784.6 ms | 942.6 ms | 27731.4 ms |
| Etcdctl | Go | 34204.5 ms | 32016.2 ms | 2188.3 ms | 10320.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 26302.2 ms | 25462.9 ms | 839.3 ms | 18245.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 26178.7 ms | 25263.4 ms | 915.4 ms | 18246.5 ms |
| Toml | LLGoDeadcodeDrop | 25147.3 ms | 24122.8 ms | 1024.5 ms | 9731.2 ms |
| Toml | LLGoNoLTO | 24448.1 ms | 23422.9 ms | 1025.3 ms | 9284.8 ms |
| XGo | Go | 19518.0 ms | 18202.5 ms | 1315.5 ms | 5823.1 ms |
| Dustin_humanize | LLGoNoLTO | 14476.7 ms | 13644.0 ms | 832.7 ms | 6117.6 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 14400.4 ms | 13624.0 ms | 776.4 ms | 6125.5 ms |
| Aws_restjson | Go | 8804.8 ms | 7776.4 ms | 1028.5 ms | 4825.4 ms |
| Gorm_schema | Go | 5858.0 ms | 5424.0 ms | 434.0 ms | 2347.0 ms |
| Uber_zap | Go | 5260.3 ms | 4844.1 ms | 416.3 ms | 2057.3 ms |
| K8s_workqueue | Go | 4714.9 ms | 4221.5 ms | 493.4 ms | 1801.1 ms |
| Toml | Go | 2026.6 ms | 1811.9 ms | 214.7 ms | 931.5 ms |
| Dustin_humanize | Go | 796.7 ms | 645.0 ms | 151.7 ms | 389.7 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1485478.6 ms | 935732.8 ms | 9 |
| LLGoFullLTOGlobalDCE | 1470918.0 ms | 903523.3 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1430546.5 ms | 879049.3 ms | 9 |
| LLGoDeadcodeDrop | 1012976.2 ms | 357368.3 ms | 9 |
| LLGoNoLTO | 1008469.6 ms | 345753.1 ms | 9 |
| Go | 166491.4 ms | 53353.2 ms | 9 |

Dependency download details are in `download-timings.log`.
