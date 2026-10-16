## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 609868.9 ms | 598966.4 ms | 10902.5 ms | 319245.8 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 607386.9 ms | 595771.3 ms | 11615.7 ms | 320668.8 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 588591.9 ms | 577916.0 ms | 10675.9 ms | 314125.3 ms |
| IXGo | LLGoDeadcodeDrop | 477708.0 ms | 463403.1 ms | 14304.8 ms | 141409.5 ms |
| IXGo | LLGoNoLTO | 462937.3 ms | 453856.5 ms | 9080.8 ms | 134373.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 293114.5 ms | 288293.6 ms | 4820.9 ms | 181780.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 289123.8 ms | 284549.4 ms | 4574.4 ms | 178894.2 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 287344.0 ms | 282557.9 ms | 4786.1 ms | 181300.7 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 232303.9 ms | 229199.1 ms | 3104.8 ms | 137190.4 ms |
| Aws_restjson | LLGoDeadcodeDrop | 229770.6 ms | 226548.6 ms | 3222.0 ms | 79109.8 ms |
| Aws_restjson | LLGoNoLTO | 229080.4 ms | 226183.0 ms | 2897.4 ms | 78359.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 219873.1 ms | 216731.2 ms | 3141.9 ms | 122644.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 216465.6 ms | 213330.4 ms | 3135.1 ms | 121160.8 ms |
| Etcdctl | LLGoDeadcodeDrop | 214292.9 ms | 209200.0 ms | 5092.8 ms | 70719.6 ms |
| Etcdctl | LLGoNoLTO | 209761.6 ms | 205796.7 ms | 3964.9 ms | 68173.6 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 204008.7 ms | 200662.4 ms | 3346.4 ms | 143197.3 ms |
| XGo | LLGoFullLTONoGlobalDCE | 203803.1 ms | 200538.0 ms | 3265.2 ms | 143704.6 ms |
| XGo | LLGoFullLTOGlobalDCE | 202915.7 ms | 199703.8 ms | 3211.9 ms | 142054.0 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 196318.1 ms | 193610.7 ms | 2707.4 ms | 121534.4 ms |
| Uber_zap | LLGoNoLTO | 192143.6 ms | 189779.3 ms | 2364.4 ms | 69785.9 ms |
| Uber_zap | LLGoDeadcodeDrop | 191892.0 ms | 189205.1 ms | 2687.0 ms | 70683.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 189850.2 ms | 186925.2 ms | 2925.0 ms | 117823.9 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 188744.2 ms | 185924.5 ms | 2819.7 ms | 117785.9 ms |
| K8s_workqueue | LLGoNoLTO | 185271.0 ms | 182702.2 ms | 2568.8 ms | 67533.3 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 184711.0 ms | 181901.3 ms | 2809.6 ms | 68163.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 184166.6 ms | 181499.0 ms | 2667.6 ms | 108701.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 182874.2 ms | 180214.5 ms | 2659.7 ms | 108411.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 173646.2 ms | 170981.5 ms | 2664.7 ms | 101442.5 ms |
| XGo | LLGoDeadcodeDrop | 122712.6 ms | 119334.2 ms | 3378.4 ms | 44754.2 ms |
| XGo | LLGoNoLTO | 121275.4 ms | 118732.5 ms | 2542.8 ms | 43423.1 ms |
| Gorm_schema | LLGoDeadcodeDrop | 101941.6 ms | 100228.4 ms | 1713.2 ms | 33525.8 ms |
| Gorm_schema | LLGoNoLTO | 100909.5 ms | 99447.5 ms | 1462.0 ms | 32878.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 100348.6 ms | 98578.9 ms | 1769.8 ms | 58177.5 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 100004.7 ms | 98214.0 ms | 1790.7 ms | 58833.5 ms |
| Toml | LLGoDeadcodeDrop | 95451.1 ms | 93591.4 ms | 1859.7 ms | 31257.8 ms |
| Toml | LLGoNoLTO | 95073.2 ms | 93360.8 ms | 1712.5 ms | 30864.6 ms |
| Toml | LLGoFullLTONoGlobalDCE | 92646.3 ms | 90798.4 ms | 1847.8 ms | 53837.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 88141.2 ms | 86524.5 ms | 1616.6 ms | 46090.9 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 84165.2 ms | 82404.6 ms | 1760.7 ms | 44784.5 ms |
| Toml | LLGoFullLTOGlobalDCE | 83984.4 ms | 82206.6 ms | 1777.8 ms | 44680.0 ms |
| IXGo | Go | 83217.4 ms | 78392.0 ms | 4825.4 ms | 22724.7 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 65582.4 ms | 64257.3 ms | 1325.1 ms | 23274.8 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 65036.7 ms | 63754.0 ms | 1282.8 ms | 39858.0 ms |
| Dustin_humanize | LLGoNoLTO | 65026.7 ms | 63892.1 ms | 1134.6 ms | 22822.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 55548.1 ms | 54420.6 ms | 1127.5 ms | 29992.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 55314.2 ms | 54179.3 ms | 1134.9 ms | 29985.0 ms |
| Etcdctl | Go | 32869.4 ms | 30880.1 ms | 1989.3 ms | 9908.2 ms |
| XGo | Go | 18874.7 ms | 17719.4 ms | 1155.3 ms | 5579.9 ms |
| Aws_restjson | Go | 7798.7 ms | 7096.5 ms | 702.2 ms | 3147.2 ms |
| Gorm_schema | Go | 5772.6 ms | 5356.9 ms | 415.7 ms | 2376.1 ms |
| Uber_zap | Go | 5198.3 ms | 4807.6 ms | 390.8 ms | 2024.0 ms |
| K8s_workqueue | Go | 4649.6 ms | 4188.0 ms | 461.6 ms | 1641.7 ms |
| Toml | Go | 2013.5 ms | 1780.4 ms | 233.1 ms | 909.8 ms |
| Dustin_humanize | Go | 793.6 ms | 661.7 ms | 131.9 ms | 373.5 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1954792.9 ms | 1168170.2 ms | 9 |
| LLGoFullLTOGlobalDCE | 1930745.6 ms | 1120432.7 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1910050.5 ms | 1099302.2 ms | 9 |
| LLGoDeadcodeDrop | 1684062.1 ms | 562898.8 ms | 9 |
| LLGoNoLTO | 1661478.7 ms | 548214.4 ms | 9 |
| Go | 161188.0 ms | 48685.1 ms | 9 |

Dependency download details are in `download-timings.log`.
