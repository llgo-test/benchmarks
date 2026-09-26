## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTONoGlobalDCE | 604382.8 ms | 592506.3 ms | 11876.5 ms | 306880.2 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 573339.7 ms | 561443.4 ms | 11896.4 ms | 293704.9 ms |
| IXGo | LLGoFullLTOGlobalDCE | 565384.4 ms | 552563.8 ms | 12820.6 ms | 292307.8 ms |
| IXGo | LLGoNoLTO | 479992.4 ms | 469119.3 ms | 10873.1 ms | 140072.1 ms |
| IXGo | LLGoDeadcodeDrop | 452951.6 ms | 442470.1 ms | 10481.5 ms | 133289.5 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 263690.9 ms | 258658.9 ms | 5032.0 ms | 162470.9 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 262971.8 ms | 258177.0 ms | 4794.8 ms | 162535.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 259634.0 ms | 254837.4 ms | 4796.6 ms | 158571.2 ms |
| Etcdctl | LLGoDeadcodeDrop | 199619.9 ms | 195225.8 ms | 4394.0 ms | 65439.5 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 189901.5 ms | 186231.8 ms | 3669.7 ms | 131204.0 ms |
| Etcdctl | LLGoNoLTO | 188635.4 ms | 184245.7 ms | 4389.7 ms | 62600.9 ms |
| XGo | LLGoFullLTONoGlobalDCE | 187239.4 ms | 183860.9 ms | 3378.5 ms | 129792.2 ms |
| XGo | LLGoFullLTOGlobalDCE | 179317.6 ms | 175816.1 ms | 3501.5 ms | 122707.5 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 137395.7 ms | 134647.8 ms | 2747.9 ms | 99906.3 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 131440.9 ms | 128715.4 ms | 2725.5 ms | 92057.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 127152.3 ms | 124544.6 ms | 2607.7 ms | 87695.7 ms |
| XGo | LLGoDeadcodeDrop | 113682.4 ms | 110551.2 ms | 3131.2 ms | 41692.1 ms |
| XGo | LLGoNoLTO | 111369.1 ms | 108425.2 ms | 2944.0 ms | 41211.6 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 110496.0 ms | 108654.6 ms | 1841.5 ms | 84214.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 106023.9 ms | 104073.6 ms | 1950.3 ms | 82057.2 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 105473.2 ms | 103641.3 ms | 1831.8 ms | 81755.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 104890.7 ms | 102879.0 ms | 2011.7 ms | 76093.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 99450.4 ms | 97653.8 ms | 1796.6 ms | 72616.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 90746.0 ms | 88777.1 ms | 1968.9 ms | 67058.4 ms |
| Aws_restjson | LLGoDeadcodeDrop | 88858.4 ms | 86609.5 ms | 2248.9 ms | 41392.5 ms |
| IXGo | Go | 87028.5 ms | 81734.5 ms | 5294.0 ms | 23947.8 ms |
| Aws_restjson | LLGoNoLTO | 85658.4 ms | 83508.1 ms | 2150.3 ms | 39696.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 65921.5 ms | 64381.3 ms | 1540.2 ms | 44794.9 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 64496.2 ms | 63058.8 ms | 1437.4 ms | 44346.0 ms |
| Uber_zap | LLGoDeadcodeDrop | 58825.2 ms | 57233.0 ms | 1592.2 ms | 25139.8 ms |
| Uber_zap | LLGoNoLTO | 57158.3 ms | 55641.0 ms | 1517.3 ms | 24442.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 54478.7 ms | 52973.3 ms | 1505.4 ms | 33324.0 ms |
| Toml | LLGoFullLTONoGlobalDCE | 51641.4 ms | 50482.0 ms | 1159.4 ms | 39177.1 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 50817.1 ms | 49310.0 ms | 1507.2 ms | 22736.0 ms |
| K8s_workqueue | LLGoNoLTO | 50271.0 ms | 48548.5 ms | 1722.5 ms | 22887.9 ms |
| Toml | LLGoFullLTOGlobalDCE | 43587.6 ms | 42488.7 ms | 1098.9 ms | 30546.0 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 42975.7 ms | 41910.0 ms | 1065.7 ms | 29994.3 ms |
| Gorm_schema | LLGoDeadcodeDrop | 41110.1 ms | 39795.0 ms | 1315.1 ms | 13915.8 ms |
| Gorm_schema | LLGoNoLTO | 39856.9 ms | 38663.8 ms | 1193.0 ms | 13366.6 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 36217.9 ms | 35321.9 ms | 896.0 ms | 28234.0 ms |
| Etcdctl | Go | 33956.7 ms | 31911.3 ms | 2045.4 ms | 10263.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 27471.6 ms | 26548.9 ms | 922.8 ms | 19253.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 27301.4 ms | 26434.6 ms | 866.7 ms | 19211.2 ms |
| Toml | LLGoDeadcodeDrop | 25776.2 ms | 24705.8 ms | 1070.4 ms | 9534.6 ms |
| Toml | LLGoNoLTO | 24703.0 ms | 23721.9 ms | 981.1 ms | 9181.9 ms |
| XGo | Go | 19552.0 ms | 18318.2 ms | 1233.8 ms | 5784.4 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 14434.3 ms | 13632.1 ms | 802.1 ms | 6117.6 ms |
| Dustin_humanize | LLGoNoLTO | 14371.4 ms | 13552.8 ms | 818.6 ms | 5913.6 ms |
| Aws_restjson | Go | 8754.0 ms | 7890.1 ms | 863.9 ms | 3997.6 ms |
| Gorm_schema | Go | 5940.3 ms | 5528.8 ms | 411.5 ms | 2335.9 ms |
| Uber_zap | Go | 5410.6 ms | 5000.7 ms | 409.9 ms | 2139.6 ms |
| K8s_workqueue | Go | 4924.1 ms | 4379.1 ms | 544.9 ms | 1810.0 ms |
| Toml | Go | 2077.0 ms | 1822.7 ms | 254.3 ms | 959.1 ms |
| Dustin_humanize | Go | 831.5 ms | 668.1 ms | 163.4 ms | 384.2 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1560314.3 ms | 976840.8 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1478935.7 ms | 905160.2 ms | 9 |
| LLGoFullLTOGlobalDCE | 1473773.1 ms | 910507.6 ms | 9 |
| LLGoNoLTO | 1052015.9 ms | 359373.6 ms | 9 |
| LLGoDeadcodeDrop | 1046075.1 ms | 359257.3 ms | 9 |
| Go | 168474.5 ms | 51622.1 ms | 9 |

Dependency download details are in `download-timings.log`.
