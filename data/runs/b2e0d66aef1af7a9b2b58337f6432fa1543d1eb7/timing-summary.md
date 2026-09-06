## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 497193.6 ms | 491423.7 ms | 5769.9 ms | 316445.1 ms |
| IXGo | LLGoFullLTOGlobalDCE | 482556.3 ms | 476836.5 ms | 5719.8 ms | 310064.7 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 469704.3 ms | 464220.3 ms | 5484.0 ms | 308976.9 ms |
| IXGo | LLGoNoLTO | 321054.9 ms | 316321.9 ms | 4733.0 ms | 108156.1 ms |
| IXGo | LLGoDeadcodeDrop | 316823.6 ms | 311716.2 ms | 5107.3 ms | 106895.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 204764.2 ms | 200703.9 ms | 4060.3 ms | 127261.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 202737.8 ms | 198888.1 ms | 3849.7 ms | 126321.7 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 200018.8 ms | 196320.8 ms | 3698.0 ms | 125088.4 ms |
| Etcdctl | LLGoDeadcodeDrop | 145695.2 ms | 142313.5 ms | 3381.7 ms | 49410.0 ms |
| Etcdctl | LLGoNoLTO | 145091.8 ms | 141705.7 ms | 3386.1 ms | 48367.5 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 137306.8 ms | 134760.5 ms | 2546.3 ms | 97489.0 ms |
| XGo | LLGoFullLTONoGlobalDCE | 136631.2 ms | 134051.4 ms | 2579.8 ms | 97123.4 ms |
| XGo | LLGoFullLTOGlobalDCE | 136526.0 ms | 133982.7 ms | 2543.3 ms | 96654.0 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 106646.2 ms | 104877.6 ms | 1768.6 ms | 79859.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 98902.6 ms | 96957.2 ms | 1945.4 ms | 70946.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 97873.8 ms | 96039.9 ms | 1833.9 ms | 70650.6 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 85152.8 ms | 83711.4 ms | 1441.4 ms | 65857.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 81233.3 ms | 79764.6 ms | 1468.7 ms | 64465.8 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 80948.5 ms | 79495.5 ms | 1453.0 ms | 64556.4 ms |
| XGo | LLGoDeadcodeDrop | 80574.6 ms | 78348.8 ms | 2225.8 ms | 31292.7 ms |
| XGo | LLGoNoLTO | 79352.6 ms | 77031.6 ms | 2321.1 ms | 30578.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 78577.5 ms | 77135.6 ms | 1441.9 ms | 58863.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 77784.1 ms | 76353.5 ms | 1430.6 ms | 58226.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 70450.3 ms | 69090.3 ms | 1360.0 ms | 53591.4 ms |
| Aws_restjson | LLGoDeadcodeDrop | 63907.9 ms | 62213.4 ms | 1694.5 ms | 31199.4 ms |
| Aws_restjson | LLGoNoLTO | 62256.0 ms | 60556.4 ms | 1699.6 ms | 30020.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 48720.0 ms | 47558.9 ms | 1161.1 ms | 34275.1 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 48206.0 ms | 47152.4 ms | 1053.7 ms | 34536.5 ms |
| Uber_zap | LLGoDeadcodeDrop | 41782.3 ms | 40568.1 ms | 1214.2 ms | 18933.2 ms |
| Uber_zap | LLGoNoLTO | 41701.7 ms | 40513.6 ms | 1188.1 ms | 18785.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 40875.1 ms | 39818.0 ms | 1057.1 ms | 26365.7 ms |
| Toml | LLGoFullLTONoGlobalDCE | 39242.6 ms | 38357.8 ms | 884.8 ms | 30663.3 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 36617.5 ms | 35390.5 ms | 1227.0 ms | 17320.8 ms |
| K8s_workqueue | LLGoNoLTO | 36446.0 ms | 35208.6 ms | 1237.3 ms | 17136.2 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 34104.2 ms | 33200.9 ms | 903.3 ms | 24892.2 ms |
| Toml | LLGoFullLTOGlobalDCE | 33362.8 ms | 32539.2 ms | 823.6 ms | 24592.9 ms |
| IXGo | Go | 33201.8 ms | 30715.1 ms | 2486.8 ms | 9614.4 ms |
| Gorm_schema | LLGoDeadcodeDrop | 27866.6 ms | 26886.1 ms | 980.5 ms | 9278.3 ms |
| Gorm_schema | LLGoNoLTO | 26717.0 ms | 25733.4 ms | 983.6 ms | 8945.5 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 25429.2 ms | 24649.7 ms | 779.5 ms | 20026.1 ms |
| Etcdctl | Go | 24808.0 ms | 23139.3 ms | 1668.7 ms | 7479.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 19167.4 ms | 18482.0 ms | 685.4 ms | 13439.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 18613.2 ms | 17966.0 ms | 647.2 ms | 13345.9 ms |
| Toml | LLGoDeadcodeDrop | 17426.7 ms | 16639.4 ms | 787.3 ms | 6664.4 ms |
| Toml | LLGoNoLTO | 16924.6 ms | 16173.6 ms | 751.0 ms | 6558.2 ms |
| XGo | Go | 14236.9 ms | 13255.6 ms | 981.4 ms | 4175.5 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 9695.9 ms | 9089.7 ms | 606.2 ms | 4229.5 ms |
| Dustin_humanize | LLGoNoLTO | 9524.5 ms | 8938.3 ms | 586.1 ms | 4118.9 ms |
| Aws_restjson | Go | 5826.9 ms | 5284.4 ms | 542.4 ms | 2395.0 ms |
| Gorm_schema | Go | 4273.5 ms | 3964.6 ms | 308.8 ms | 1628.9 ms |
| Uber_zap | Go | 3956.5 ms | 3622.1 ms | 334.4 ms | 1538.9 ms |
| K8s_workqueue | Go | 3550.2 ms | 3176.9 ms | 373.3 ms | 1276.8 ms |
| Toml | Go | 1535.2 ms | 1328.8 ms | 206.4 ms | 708.4 ms |
| Dustin_humanize | Go | 614.2 ms | 481.8 ms | 132.4 ms | 304.3 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1191979.7 ms | 826688.4 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1181341.7 ms | 789293.5 ms | 9 |
| LLGoFullLTOGlobalDCE | 1179407.4 ms | 798597.1 ms | 9 |
| LLGoDeadcodeDrop | 740390.3 ms | 275223.3 ms | 9 |
| LLGoNoLTO | 739069.3 ms | 272667.0 ms | 9 |
| Go | 92003.2 ms | 29121.9 ms | 9 |

Dependency download details are in `download-timings.log`.
