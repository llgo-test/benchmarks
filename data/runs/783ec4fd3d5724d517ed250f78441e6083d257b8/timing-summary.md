## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 447309.1 ms | 438292.1 ms | 9016.9 ms | 239089.7 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 430860.9 ms | 423304.6 ms | 7556.3 ms | 228454.7 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 425441.9 ms | 417756.0 ms | 7685.9 ms | 228132.5 ms |
| IXGo | LLGoDeadcodeDrop | 396900.3 ms | 386603.5 ms | 10296.8 ms | 118366.1 ms |
| IXGo | LLGoNoLTO | 350977.8 ms | 343918.8 ms | 7059.0 ms | 101751.9 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 222534.2 ms | 218635.8 ms | 3898.4 ms | 137680.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 218577.6 ms | 215049.1 ms | 3528.5 ms | 131795.6 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 215739.1 ms | 211555.4 ms | 4183.7 ms | 130370.2 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 181256.9 ms | 178348.1 ms | 2908.8 ms | 106659.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 169620.9 ms | 166735.7 ms | 2885.2 ms | 92997.9 ms |
| XGo | LLGoFullLTONoGlobalDCE | 161666.7 ms | 159161.2 ms | 2505.5 ms | 108963.0 ms |
| Etcdctl | LLGoDeadcodeDrop | 159907.6 ms | 156206.3 ms | 3701.3 ms | 53242.5 ms |
| Etcdctl | LLGoNoLTO | 159816.9 ms | 156562.0 ms | 3254.9 ms | 53062.0 ms |
| Aws_restjson | LLGoNoLTO | 159395.6 ms | 157068.2 ms | 2327.4 ms | 53767.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 157752.5 ms | 155108.0 ms | 2644.5 ms | 86545.8 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 157716.6 ms | 155196.8 ms | 2519.8 ms | 105856.1 ms |
| Aws_restjson | LLGoDeadcodeDrop | 157011.2 ms | 154611.1 ms | 2400.2 ms | 53243.7 ms |
| XGo | LLGoFullLTOGlobalDCE | 155039.6 ms | 152543.8 ms | 2495.8 ms | 104987.4 ms |
| Uber_zap | LLGoDeadcodeDrop | 145226.4 ms | 142967.9 ms | 2258.4 ms | 52465.2 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 142995.5 ms | 140616.8 ms | 2378.7 ms | 85138.7 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 139538.6 ms | 137275.3 ms | 2263.2 ms | 49818.6 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 138833.9 ms | 136347.8 ms | 2486.2 ms | 82501.1 ms |
| Uber_zap | LLGoNoLTO | 138738.7 ms | 136582.2 ms | 2156.5 ms | 49660.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 138623.6 ms | 136216.8 ms | 2406.8 ms | 78190.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 138566.4 ms | 136195.0 ms | 2371.4 ms | 81689.6 ms |
| K8s_workqueue | LLGoNoLTO | 136796.7 ms | 134562.7 ms | 2234.0 ms | 48921.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 136503.6 ms | 134100.6 ms | 2403.0 ms | 76645.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 133049.7 ms | 130448.8 ms | 2600.8 ms | 73905.4 ms |
| XGo | LLGoDeadcodeDrop | 105439.8 ms | 102777.8 ms | 2662.0 ms | 38701.2 ms |
| XGo | LLGoNoLTO | 100434.3 ms | 98376.0 ms | 2058.2 ms | 36695.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 67856.1 ms | 66351.0 ms | 1505.1 ms | 41097.7 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 67568.4 ms | 66047.1 ms | 1521.3 ms | 40634.5 ms |
| Gorm_schema | LLGoDeadcodeDrop | 67258.5 ms | 65933.8 ms | 1324.8 ms | 22687.5 ms |
| Toml | LLGoDeadcodeDrop | 66054.6 ms | 64643.3 ms | 1411.2 ms | 22217.8 ms |
| Gorm_schema | LLGoNoLTO | 64099.8 ms | 62862.3 ms | 1237.4 ms | 21566.1 ms |
| Toml | LLGoFullLTONoGlobalDCE | 60894.6 ms | 59468.6 ms | 1426.0 ms | 36375.5 ms |
| Toml | LLGoNoLTO | 60700.3 ms | 59423.7 ms | 1276.6 ms | 20411.1 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 60454.6 ms | 58973.8 ms | 1480.8 ms | 32601.2 ms |
| Toml | LLGoFullLTOGlobalDCE | 58094.8 ms | 56623.0 ms | 1471.8 ms | 32192.8 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 56199.7 ms | 54798.8 ms | 1400.9 ms | 30713.2 ms |
| IXGo | Go | 53163.2 ms | 49329.2 ms | 3834.0 ms | 15077.1 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 44697.8 ms | 43741.6 ms | 956.2 ms | 16148.2 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 43107.2 ms | 42066.4 ms | 1040.8 ms | 26958.4 ms |
| Dustin_humanize | LLGoNoLTO | 42704.3 ms | 41744.6 ms | 959.7 ms | 15648.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 38521.2 ms | 37486.2 ms | 1035.0 ms | 21344.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 36781.1 ms | 35800.9 ms | 980.2 ms | 20246.4 ms |
| Etcdctl | Go | 23917.5 ms | 22185.0 ms | 1732.5 ms | 7304.1 ms |
| XGo | Go | 12376.4 ms | 11456.8 ms | 919.7 ms | 3775.3 ms |
| Aws_restjson | Go | 5180.1 ms | 4702.6 ms | 477.5 ms | 2110.6 ms |
| Gorm_schema | Go | 3501.2 ms | 3221.5 ms | 279.7 ms | 1340.0 ms |
| Uber_zap | Go | 3276.9 ms | 2977.7 ms | 299.2 ms | 1294.3 ms |
| K8s_workqueue | Go | 3015.6 ms | 2680.3 ms | 335.3 ms | 1082.9 ms |
| Toml | Go | 1364.0 ms | 1148.9 ms | 215.2 ms | 636.4 ms |
| Dustin_humanize | Go | 505.4 ms | 414.0 ms | 91.4 ms | 241.1 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1449718.3 ms | 853366.0 ms | 9 |
| LLGoFullLTOGlobalDCE | 1416480.8 ms | 814290.6 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1395367.3 ms | 794111.3 ms | 9 |
| LLGoDeadcodeDrop | 1282034.9 ms | 426890.8 ms | 9 |
| LLGoNoLTO | 1213664.4 ms | 401484.9 ms | 9 |
| Go | 106300.3 ms | 32861.9 ms | 9 |

Dependency download details are in `download-timings.log`.
