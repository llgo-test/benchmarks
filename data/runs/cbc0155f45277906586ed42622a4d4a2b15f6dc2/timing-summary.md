## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 574856.1 ms | 568482.6 ms | 6373.5 ms | 360980.2 ms |
| IXGo | LLGoFullLTOGlobalDCE | 573428.5 ms | 566675.2 ms | 6753.2 ms | 358225.1 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 563034.3 ms | 556979.7 ms | 6054.6 ms | 354922.9 ms |
| IXGo | LLGoDeadcodeDrop | 381170.2 ms | 375346.1 ms | 5824.2 ms | 126358.2 ms |
| IXGo | LLGoNoLTO | 378558.2 ms | 372991.0 ms | 5567.2 ms | 126116.5 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 265986.2 ms | 261445.3 ms | 4540.9 ms | 161337.6 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 263915.2 ms | 259427.3 ms | 4487.9 ms | 159504.7 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 261447.2 ms | 256895.0 ms | 4552.2 ms | 159484.1 ms |
| Etcdctl | LLGoDeadcodeDrop | 197748.9 ms | 193764.5 ms | 3984.4 ms | 65360.1 ms |
| Etcdctl | LLGoNoLTO | 194638.0 ms | 190741.1 ms | 3896.9 ms | 64010.2 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 177407.6 ms | 174340.1 ms | 3067.5 ms | 122987.0 ms |
| XGo | LLGoFullLTOGlobalDCE | 176554.4 ms | 173510.7 ms | 3043.7 ms | 122493.0 ms |
| XGo | LLGoFullLTONoGlobalDCE | 175366.9 ms | 172380.6 ms | 2986.4 ms | 123316.5 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 137425.2 ms | 135245.6 ms | 2179.6 ms | 100469.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 128013.0 ms | 125757.2 ms | 2255.9 ms | 89877.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 127340.5 ms | 125000.1 ms | 2340.4 ms | 88996.2 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 111622.3 ms | 109958.5 ms | 1663.9 ms | 85393.6 ms |
| XGo | LLGoDeadcodeDrop | 107784.7 ms | 105043.1 ms | 2741.6 ms | 40309.1 ms |
| XGo | LLGoNoLTO | 106329.8 ms | 103748.0 ms | 2581.8 ms | 40745.2 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 105251.1 ms | 103567.0 ms | 1684.0 ms | 82475.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 105036.9 ms | 103336.1 ms | 1700.8 ms | 81925.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 101877.9 ms | 100141.6 ms | 1736.2 ms | 75610.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 101334.4 ms | 99689.6 ms | 1644.9 ms | 75346.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 92572.3 ms | 90868.3 ms | 1704.0 ms | 69310.9 ms |
| Aws_restjson | LLGoDeadcodeDrop | 82123.4 ms | 80221.5 ms | 1901.9 ms | 37488.1 ms |
| Aws_restjson | LLGoNoLTO | 81494.0 ms | 79564.8 ms | 1929.3 ms | 37070.1 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 64580.7 ms | 63230.9 ms | 1349.8 ms | 44680.5 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 64129.7 ms | 62867.6 ms | 1262.1 ms | 45253.9 ms |
| Uber_zap | LLGoDeadcodeDrop | 57376.5 ms | 55956.2 ms | 1420.3 ms | 25013.8 ms |
| Uber_zap | LLGoNoLTO | 55964.9 ms | 54546.1 ms | 1418.8 ms | 24732.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 54889.2 ms | 53613.3 ms | 1275.9 ms | 34877.6 ms |
| Toml | LLGoFullLTONoGlobalDCE | 51974.3 ms | 50950.2 ms | 1024.1 ms | 40240.3 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 49904.8 ms | 48434.3 ms | 1470.5 ms | 23014.9 ms |
| K8s_workqueue | LLGoNoLTO | 49231.0 ms | 47805.1 ms | 1425.9 ms | 22677.7 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 45872.5 ms | 44762.8 ms | 1109.7 ms | 33082.1 ms |
| IXGo | Go | 44709.6 ms | 41950.9 ms | 2758.6 ms | 12768.5 ms |
| Toml | LLGoFullLTOGlobalDCE | 44549.9 ms | 43538.9 ms | 1010.9 ms | 32565.1 ms |
| Gorm_schema | LLGoDeadcodeDrop | 37788.0 ms | 36690.1 ms | 1097.9 ms | 12301.3 ms |
| Gorm_schema | LLGoNoLTO | 37319.1 ms | 36201.5 ms | 1117.6 ms | 12064.4 ms |
| Etcdctl | Go | 32810.5 ms | 30874.7 ms | 1935.9 ms | 9838.2 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 32613.2 ms | 31747.5 ms | 865.8 ms | 25403.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 24907.3 ms | 24113.8 ms | 793.6 ms | 17078.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 24266.2 ms | 23495.1 ms | 771.1 ms | 16940.8 ms |
| Toml | LLGoDeadcodeDrop | 23869.0 ms | 22923.5 ms | 945.5 ms | 8889.4 ms |
| Toml | LLGoNoLTO | 22873.8 ms | 21950.8 ms | 923.0 ms | 8669.1 ms |
| XGo | Go | 18935.5 ms | 17832.2 ms | 1103.2 ms | 5457.4 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 13058.9 ms | 12354.0 ms | 704.9 ms | 5501.7 ms |
| Dustin_humanize | LLGoNoLTO | 13056.6 ms | 12322.5 ms | 734.0 ms | 5625.7 ms |
| Aws_restjson | Go | 7776.1 ms | 7150.9 ms | 625.1 ms | 3092.3 ms |
| Gorm_schema | Go | 5675.7 ms | 5260.3 ms | 415.5 ms | 2152.6 ms |
| Uber_zap | Go | 5233.5 ms | 4830.9 ms | 402.6 ms | 2015.3 ms |
| K8s_workqueue | Go | 4608.2 ms | 4164.8 ms | 443.5 ms | 1618.3 ms |
| Toml | Go | 1985.9 ms | 1753.1 ms | 232.9 ms | 898.9 ms |
| Dustin_humanize | Go | 806.1 ms | 640.8 ms | 165.3 ms | 380.5 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1502864.2 ms | 1016960.4 ms | 9 |
| LLGoFullLTOGlobalDCE | 1481679.2 ms | 981557.6 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1465709.6 ms | 964260.8 ms | 9 |
| LLGoDeadcodeDrop | 950824.5 ms | 344236.6 ms | 9 |
| LLGoNoLTO | 939465.3 ms | 341711.1 ms | 9 |
| Go | 122541.2 ms | 38222.0 ms | 9 |

Dependency download details are in `download-timings.log`.
