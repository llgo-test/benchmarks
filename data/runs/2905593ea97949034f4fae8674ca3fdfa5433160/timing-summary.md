## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTONoGlobalDCE | 1006105.9 ms | 979092.1 ms | 27013.8 ms | 607000.0 ms |
| IXGo | LLGoFullLTOGlobalDCE | 979586.7 ms | 953201.5 ms | 26385.2 ms | 597884.0 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 912698.8 ms | 885645.9 ms | 27052.8 ms | 579613.3 ms |
| IXGo | LLGoDeadcodeDrop | 658149.2 ms | 631148.3 ms | 27000.9 ms | 199390.3 ms |
| IXGo | LLGoNoLTO | 519378.7 ms | 496940.9 ms | 22437.8 ms | 159414.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 481059.5 ms | 468001.3 ms | 13058.2 ms | 353454.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 473432.8 ms | 460049.1 ms | 13383.7 ms | 351403.6 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 468500.5 ms | 455787.7 ms | 12712.8 ms | 343591.9 ms |
| XGo | LLGoFullLTONoGlobalDCE | 409071.2 ms | 399209.5 ms | 9861.7 ms | 333003.8 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 367158.3 ms | 359660.5 ms | 7497.8 ms | 255618.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 342967.7 ms | 335710.6 ms | 7257.1 ms | 217558.2 ms |
| XGo | LLGoFullLTOGlobalDCE | 320548.8 ms | 312111.8 ms | 8437.0 ms | 248906.6 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 319402.5 ms | 310882.3 ms | 8520.2 ms | 247163.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 293308.7 ms | 286214.9 ms | 7093.8 ms | 193728.8 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 288722.0 ms | 282553.6 ms | 6168.4 ms | 212529.1 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 285604.8 ms | 279319.5 ms | 6285.3 ms | 207184.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 268037.4 ms | 262047.1 ms | 5990.3 ms | 185896.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 266631.3 ms | 260491.3 ms | 6140.0 ms | 192459.7 ms |
| Aws_restjson | LLGoDeadcodeDrop | 262958.0 ms | 256692.9 ms | 6265.1 ms | 91099.1 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 252726.9 ms | 246576.0 ms | 6150.9 ms | 173150.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 251178.7 ms | 245370.5 ms | 5808.2 ms | 173088.5 ms |
| Etcdctl | LLGoNoLTO | 248758.2 ms | 238357.5 ms | 10400.6 ms | 86463.3 ms |
| Etcdctl | LLGoDeadcodeDrop | 246506.1 ms | 235639.5 ms | 10866.6 ms | 86833.8 ms |
| Aws_restjson | LLGoNoLTO | 239561.6 ms | 233748.3 ms | 5813.3 ms | 84705.5 ms |
| Uber_zap | LLGoNoLTO | 212825.0 ms | 207935.0 ms | 4890.0 ms | 79966.7 ms |
| Uber_zap | LLGoDeadcodeDrop | 209484.5 ms | 204015.7 ms | 5468.8 ms | 79418.0 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 197199.7 ms | 192116.3 ms | 5083.5 ms | 74910.8 ms |
| K8s_workqueue | LLGoNoLTO | 193343.5 ms | 188829.7 ms | 4513.8 ms | 72443.9 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 154852.4 ms | 150947.7 ms | 3904.7 ms | 110106.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 143593.3 ms | 139813.9 ms | 3779.4 ms | 99674.5 ms |
| XGo | LLGoNoLTO | 142326.1 ms | 135442.4 ms | 6883.7 ms | 54746.6 ms |
| XGo | LLGoDeadcodeDrop | 139729.2 ms | 132094.8 ms | 7634.4 ms | 53282.9 ms |
| Toml | LLGoFullLTONoGlobalDCE | 133066.1 ms | 129537.2 ms | 3528.9 ms | 91966.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 127895.4 ms | 124253.8 ms | 3641.6 ms | 81026.4 ms |
| Toml | LLGoFullLTOGlobalDCE | 125610.2 ms | 122335.0 ms | 3275.2 ms | 81697.5 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 122930.5 ms | 119601.2 ms | 3329.3 ms | 79258.0 ms |
| Gorm_schema | LLGoDeadcodeDrop | 113247.7 ms | 109876.6 ms | 3371.0 ms | 38496.8 ms |
| Gorm_schema | LLGoNoLTO | 112445.2 ms | 109325.4 ms | 3119.8 ms | 37737.6 ms |
| Toml | LLGoDeadcodeDrop | 102035.3 ms | 99044.6 ms | 2990.7 ms | 34260.2 ms |
| IXGo | Go | 101699.6 ms | 85776.0 ms | 15923.6 ms | 27850.3 ms |
| Toml | LLGoNoLTO | 98323.6 ms | 95591.3 ms | 2732.3 ms | 32746.7 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 93622.4 ms | 91229.5 ms | 2392.9 ms | 67964.5 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 79563.9 ms | 77240.0 ms | 2323.9 ms | 51246.9 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 73773.0 ms | 71641.6 ms | 2131.5 ms | 47424.7 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 70925.6 ms | 68736.9 ms | 2188.7 ms | 25872.1 ms |
| Dustin_humanize | LLGoNoLTO | 69602.7 ms | 67506.2 ms | 2096.6 ms | 25235.3 ms |
| Etcdctl | Go | 38284.9 ms | 32901.5 ms | 5383.4 ms | 11582.5 ms |
| XGo | Go | 22816.0 ms | 19651.9 ms | 3164.1 ms | 6758.4 ms |
| Aws_restjson | Go | 9645.1 ms | 7977.6 ms | 1667.5 ms | 4106.3 ms |
| Gorm_schema | Go | 6867.4 ms | 5845.9 ms | 1021.5 ms | 2706.5 ms |
| Uber_zap | Go | 6034.8 ms | 5015.7 ms | 1019.1 ms | 2746.6 ms |
| K8s_workqueue | Go | 5911.3 ms | 4913.6 ms | 997.7 ms | 2154.6 ms |
| Toml | Go | 2253.2 ms | 1843.0 ms | 410.2 ms | 1061.0 ms |
| Dustin_humanize | Go | 970.3 ms | 741.5 ms | 228.7 ms | 486.2 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 3206703.5 ms | 2228965.0 ms | 9 |
| LLGoFullLTOGlobalDCE | 2933454.4 ms | 1990090.1 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2901491.8 ms | 1964545.5 ms | 9 |
| LLGoDeadcodeDrop | 2000235.4 ms | 683564.0 ms | 9 |
| LLGoNoLTO | 1836564.6 ms | 633460.0 ms | 9 |
| Go | 194482.5 ms | 59452.3 ms | 9 |

Dependency download details are in `download-timings.log`.
