## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTONoGlobalDCE | 689407.3 ms | 669611.7 ms | 19795.6 ms | 430922.0 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 599510.5 ms | 580149.4 ms | 19361.1 ms | 398532.1 ms |
| IXGo | LLGoFullLTOGlobalDCE | 584963.4 ms | 565939.5 ms | 19023.9 ms | 378892.0 ms |
| IXGo | LLGoDeadcodeDrop | 451677.8 ms | 431779.6 ms | 19898.3 ms | 137996.8 ms |
| IXGo | LLGoNoLTO | 387039.2 ms | 371519.9 ms | 15519.3 ms | 116821.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 328510.3 ms | 318972.9 ms | 9537.5 ms | 247027.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 313760.9 ms | 303873.3 ms | 9887.6 ms | 232676.0 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 299132.7 ms | 290010.9 ms | 9121.9 ms | 225217.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 227224.7 ms | 221832.6 ms | 5392.1 ms | 146954.8 ms |
| XGo | LLGoFullLTONoGlobalDCE | 226010.8 ms | 219598.3 ms | 6412.5 ms | 185832.2 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 221059.4 ms | 215272.0 ms | 5787.4 ms | 156002.6 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 207576.2 ms | 202493.6 ms | 5082.7 ms | 153875.0 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 204163.0 ms | 198142.6 ms | 6020.4 ms | 162067.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 193606.4 ms | 188292.4 ms | 5314.0 ms | 132254.0 ms |
| XGo | LLGoFullLTOGlobalDCE | 190130.0 ms | 184448.3 ms | 5681.6 ms | 150542.1 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 177781.7 ms | 173174.6 ms | 4607.1 ms | 132478.1 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 174939.1 ms | 170333.6 ms | 4605.5 ms | 129877.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 167784.5 ms | 163401.6 ms | 4382.9 ms | 116372.1 ms |
| Aws_restjson | LLGoDeadcodeDrop | 167470.6 ms | 162761.5 ms | 4709.1 ms | 57644.9 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 158762.4 ms | 154318.7 ms | 4443.8 ms | 112849.4 ms |
| Aws_restjson | LLGoNoLTO | 153250.1 ms | 149091.0 ms | 4159.1 ms | 54075.5 ms |
| Etcdctl | LLGoDeadcodeDrop | 149796.6 ms | 141892.5 ms | 7904.1 ms | 53720.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 147435.5 ms | 143212.9 ms | 4222.6 ms | 103618.9 ms |
| Etcdctl | LLGoNoLTO | 146707.8 ms | 140015.1 ms | 6692.6 ms | 52883.5 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 133635.5 ms | 129487.1 ms | 4148.4 ms | 51313.3 ms |
| Uber_zap | LLGoDeadcodeDrop | 129343.1 ms | 125615.7 ms | 3727.4 ms | 49797.7 ms |
| Uber_zap | LLGoNoLTO | 124212.6 ms | 120728.1 ms | 3484.4 ms | 47124.7 ms |
| K8s_workqueue | LLGoNoLTO | 123747.0 ms | 120134.4 ms | 3612.7 ms | 47244.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 98417.3 ms | 95464.9 ms | 2952.5 ms | 72542.0 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 90612.8 ms | 87735.2 ms | 2877.6 ms | 65937.0 ms |
| Toml | LLGoFullLTONoGlobalDCE | 88790.5 ms | 86215.4 ms | 2575.1 ms | 63539.4 ms |
| XGo | LLGoNoLTO | 86938.3 ms | 82209.0 ms | 4729.3 ms | 34375.4 ms |
| XGo | LLGoDeadcodeDrop | 84108.7 ms | 79036.0 ms | 5072.7 ms | 33401.6 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 76960.8 ms | 74441.0 ms | 2519.7 ms | 52082.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 75221.8 ms | 72674.1 ms | 2547.6 ms | 49214.8 ms |
| Toml | LLGoFullLTOGlobalDCE | 69919.1 ms | 67619.4 ms | 2299.7 ms | 46653.4 ms |
| Gorm_schema | LLGoDeadcodeDrop | 66679.8 ms | 64105.1 ms | 2574.6 ms | 23425.1 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 65163.2 ms | 63303.4 ms | 1859.8 ms | 49020.0 ms |
| Gorm_schema | LLGoNoLTO | 63827.5 ms | 61565.4 ms | 2262.1 ms | 21828.1 ms |
| Toml | LLGoDeadcodeDrop | 63729.3 ms | 61421.2 ms | 2308.1 ms | 22067.4 ms |
| Toml | LLGoNoLTO | 59748.5 ms | 57638.9 ms | 2109.6 ms | 20248.3 ms |
| IXGo | Go | 58203.9 ms | 47942.2 ms | 10261.7 ms | 16116.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 54517.3 ms | 52761.2 ms | 1756.2 ms | 36289.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 48053.7 ms | 46350.1 ms | 1703.6 ms | 32213.5 ms |
| Dustin_humanize | LLGoNoLTO | 45387.3 ms | 43832.4 ms | 1554.8 ms | 17049.7 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 44579.5 ms | 42956.3 ms | 1623.2 ms | 16545.5 ms |
| Etcdctl | Go | 22877.1 ms | 19304.4 ms | 3572.8 ms | 6916.6 ms |
| XGo | Go | 13766.3 ms | 11541.2 ms | 2225.1 ms | 4214.5 ms |
| Aws_restjson | Go | 5744.0 ms | 4684.2 ms | 1059.8 ms | 2564.3 ms |
| Gorm_schema | Go | 3859.2 ms | 3261.9 ms | 597.3 ms | 1564.7 ms |
| Uber_zap | Go | 3603.6 ms | 3006.2 ms | 597.4 ms | 1478.5 ms |
| K8s_workqueue | Go | 3460.7 ms | 2876.6 ms | 584.1 ms | 1280.5 ms |
| Toml | Go | 1405.7 ms | 1138.4 ms | 267.3 ms | 678.3 ms |
| Dustin_humanize | Go | 535.2 ms | 393.9 ms | 141.3 ms | 266.2 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2065534.7 ms | 1462824.2 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1874864.8 ms | 1308083.8 ms | 9 |
| LLGoFullLTOGlobalDCE | 1839016.0 ms | 1292576.0 ms | 9 |
| LLGoDeadcodeDrop | 1291020.8 ms | 445912.7 ms | 9 |
| LLGoNoLTO | 1190858.1 ms | 411651.9 ms | 9 |
| Go | 113455.7 ms | 35080.4 ms | 9 |

Dependency download details are in `download-timings.log`.
