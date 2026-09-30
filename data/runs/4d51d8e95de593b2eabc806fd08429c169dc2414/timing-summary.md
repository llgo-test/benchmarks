## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 555913.5 ms | 544616.1 ms | 11297.4 ms | 287770.1 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 522291.2 ms | 511502.1 ms | 10789.1 ms | 279424.7 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 494549.2 ms | 484431.2 ms | 10118.1 ms | 271593.0 ms |
| IXGo | LLGoNoLTO | 442551.4 ms | 433920.6 ms | 8630.8 ms | 133962.3 ms |
| IXGo | LLGoDeadcodeDrop | 415121.3 ms | 405782.8 ms | 9338.5 ms | 125988.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 254630.0 ms | 250034.7 ms | 4595.3 ms | 164263.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 241591.5 ms | 237090.2 ms | 4501.3 ms | 155096.9 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 238884.5 ms | 234509.4 ms | 4375.1 ms | 155565.5 ms |
| Aws_restjson | LLGoDeadcodeDrop | 203851.8 ms | 201043.9 ms | 2807.8 ms | 73606.8 ms |
| Aws_restjson | LLGoNoLTO | 200591.8 ms | 197948.9 ms | 2642.8 ms | 73148.1 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 197761.4 ms | 194806.8 ms | 2954.6 ms | 120694.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 187528.0 ms | 184607.3 ms | 2920.7 ms | 107966.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 186149.5 ms | 183268.6 ms | 2880.9 ms | 107393.5 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 178264.1 ms | 174938.9 ms | 3325.2 ms | 127685.0 ms |
| Etcdctl | LLGoDeadcodeDrop | 176996.1 ms | 173165.4 ms | 3830.7 ms | 61163.0 ms |
| Etcdctl | LLGoNoLTO | 174274.7 ms | 170295.9 ms | 3978.8 ms | 61131.2 ms |
| XGo | LLGoFullLTONoGlobalDCE | 171476.5 ms | 168405.6 ms | 3070.8 ms | 124265.9 ms |
| XGo | LLGoFullLTOGlobalDCE | 170610.8 ms | 167506.6 ms | 3104.2 ms | 121860.0 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 167829.4 ms | 165333.2 ms | 2496.2 ms | 107014.4 ms |
| Uber_zap | LLGoDeadcodeDrop | 165357.4 ms | 163150.2 ms | 2207.2 ms | 64618.0 ms |
| Uber_zap | LLGoNoLTO | 163779.8 ms | 161626.7 ms | 2153.1 ms | 63765.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 163598.1 ms | 160987.6 ms | 2610.5 ms | 103796.1 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 163002.9 ms | 160612.7 ms | 2390.3 ms | 63611.0 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 162865.6 ms | 160257.5 ms | 2608.1 ms | 104347.9 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 159525.3 ms | 157023.7 ms | 2501.7 ms | 97187.9 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 159387.4 ms | 156916.3 ms | 2471.1 ms | 97328.9 ms |
| K8s_workqueue | LLGoNoLTO | 158272.7 ms | 155914.0 ms | 2358.6 ms | 62708.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 151383.2 ms | 148807.3 ms | 2576.0 ms | 91273.3 ms |
| XGo | LLGoDeadcodeDrop | 102701.3 ms | 99906.5 ms | 2794.8 ms | 40198.9 ms |
| XGo | LLGoNoLTO | 102124.4 ms | 99428.8 ms | 2695.6 ms | 40453.1 ms |
| Gorm_schema | LLGoDeadcodeDrop | 88802.7 ms | 87224.3 ms | 1578.4 ms | 29668.3 ms |
| Gorm_schema | LLGoNoLTO | 86661.0 ms | 85160.6 ms | 1500.4 ms | 28914.3 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 85161.8 ms | 83623.0 ms | 1538.9 ms | 51217.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 84433.2 ms | 82795.7 ms | 1637.5 ms | 49947.7 ms |
| IXGo | Go | 84204.6 ms | 79076.7 ms | 5127.9 ms | 23871.6 ms |
| Toml | LLGoNoLTO | 82320.3 ms | 80753.8 ms | 1566.4 ms | 27151.5 ms |
| Toml | LLGoDeadcodeDrop | 80569.1 ms | 78970.3 ms | 1598.8 ms | 26546.5 ms |
| Toml | LLGoFullLTONoGlobalDCE | 77330.0 ms | 75729.3 ms | 1600.7 ms | 45687.7 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 73959.0 ms | 72432.2 ms | 1526.8 ms | 39478.6 ms |
| Toml | LLGoFullLTOGlobalDCE | 72065.9 ms | 70468.9 ms | 1597.0 ms | 38867.3 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 70980.2 ms | 69360.3 ms | 1619.9 ms | 38662.0 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 55018.3 ms | 53996.2 ms | 1022.1 ms | 19714.4 ms |
| Dustin_humanize | LLGoNoLTO | 54676.0 ms | 53641.4 ms | 1034.5 ms | 19460.8 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 54244.6 ms | 53141.9 ms | 1102.6 ms | 33853.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 45814.6 ms | 44742.6 ms | 1072.0 ms | 25068.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 45543.8 ms | 44466.9 ms | 1077.0 ms | 25021.1 ms |
| Etcdctl | Go | 33127.4 ms | 31189.6 ms | 1937.8 ms | 9919.4 ms |
| XGo | Go | 19175.6 ms | 18060.0 ms | 1115.6 ms | 5909.0 ms |
| Aws_restjson | Go | 7958.2 ms | 7292.2 ms | 666.0 ms | 3265.6 ms |
| Gorm_schema | Go | 5809.8 ms | 5440.9 ms | 368.9 ms | 2217.8 ms |
| Uber_zap | Go | 5308.6 ms | 4861.2 ms | 447.4 ms | 2317.0 ms |
| K8s_workqueue | Go | 4695.0 ms | 4239.1 ms | 455.9 ms | 1668.3 ms |
| Toml | Go | 2170.9 ms | 1919.6 ms | 251.3 ms | 1178.9 ms |
| Dustin_humanize | Go | 804.8 ms | 646.9 ms | 157.9 ms | 373.4 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTOGlobalDCE | 1679431.6 ms | 986940.6 ms | 9 |
| LLGoFullLTONoGlobalDCE | 1650102.9 ms | 1014239.2 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1644237.8 ms | 971151.0 ms | 9 |
| LLGoNoLTO | 1465251.9 ms | 510695.7 ms | 9 |
| LLGoDeadcodeDrop | 1451420.9 ms | 505115.0 ms | 9 |
| Go | 163255.0 ms | 50720.9 ms | 9 |

Dependency download details are in `download-timings.log`.
