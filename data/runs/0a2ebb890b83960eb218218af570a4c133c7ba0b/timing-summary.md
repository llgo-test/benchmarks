## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 646172.0 ms | 635452.4 ms | 10719.6 ms | 333567.5 ms |
| IXGo | LLGoFullLTOGlobalDCE | 626606.1 ms | 616354.9 ms | 10251.1 ms | 328148.3 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 610058.4 ms | 599758.7 ms | 10299.7 ms | 322971.2 ms |
| IXGo | LLGoDeadcodeDrop | 482936.7 ms | 468707.4 ms | 14229.3 ms | 142602.0 ms |
| IXGo | LLGoNoLTO | 476502.9 ms | 467487.2 ms | 9015.7 ms | 137623.6 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 297108.5 ms | 292175.8 ms | 4932.7 ms | 184211.2 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 294670.4 ms | 289779.5 ms | 4890.9 ms | 185410.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 293567.9 ms | 288599.5 ms | 4968.5 ms | 182483.2 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 234227.2 ms | 230904.2 ms | 3323.0 ms | 139414.9 ms |
| Aws_restjson | LLGoNoLTO | 232620.5 ms | 229665.9 ms | 2954.6 ms | 79245.1 ms |
| Aws_restjson | LLGoDeadcodeDrop | 232332.2 ms | 228967.8 ms | 3364.4 ms | 80137.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 221042.7 ms | 217769.9 ms | 3272.8 ms | 123733.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 221027.4 ms | 217775.6 ms | 3251.8 ms | 124424.9 ms |
| Etcdctl | LLGoDeadcodeDrop | 217999.9 ms | 212678.0 ms | 5321.9 ms | 71878.4 ms |
| Etcdctl | LLGoNoLTO | 213808.5 ms | 209511.0 ms | 4297.6 ms | 69294.4 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 208224.5 ms | 204873.2 ms | 3351.4 ms | 145782.8 ms |
| XGo | LLGoFullLTONoGlobalDCE | 207320.4 ms | 204044.6 ms | 3275.8 ms | 146817.3 ms |
| XGo | LLGoFullLTOGlobalDCE | 206063.1 ms | 202788.2 ms | 3274.9 ms | 144916.8 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 197916.7 ms | 195150.9 ms | 2765.7 ms | 122967.3 ms |
| Uber_zap | LLGoDeadcodeDrop | 194511.8 ms | 191778.1 ms | 2733.8 ms | 71443.3 ms |
| Uber_zap | LLGoNoLTO | 193668.3 ms | 191190.6 ms | 2477.7 ms | 70300.7 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 191476.2 ms | 188545.4 ms | 2930.8 ms | 119900.1 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 191246.8 ms | 188364.3 ms | 2882.6 ms | 119038.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 187493.7 ms | 184905.8 ms | 2587.9 ms | 110818.9 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 187052.4 ms | 184295.7 ms | 2756.7 ms | 110334.1 ms |
| K8s_workqueue | LLGoNoLTO | 186469.4 ms | 183880.2 ms | 2589.2 ms | 67983.1 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 186169.1 ms | 183297.0 ms | 2872.1 ms | 68753.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 177147.1 ms | 174363.3 ms | 2783.8 ms | 103607.5 ms |
| XGo | LLGoDeadcodeDrop | 124500.2 ms | 120760.2 ms | 3740.0 ms | 45886.0 ms |
| XGo | LLGoNoLTO | 122287.7 ms | 119635.5 ms | 2652.2 ms | 44107.0 ms |
| Gorm_schema | LLGoDeadcodeDrop | 103636.0 ms | 101860.9 ms | 1775.0 ms | 34128.1 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 102665.5 ms | 100849.7 ms | 1815.8 ms | 59957.5 ms |
| Gorm_schema | LLGoNoLTO | 102578.3 ms | 101004.7 ms | 1573.6 ms | 33287.6 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 101582.0 ms | 99814.9 ms | 1767.1 ms | 59881.9 ms |
| Toml | LLGoNoLTO | 97426.1 ms | 95718.0 ms | 1708.0 ms | 31405.5 ms |
| Toml | LLGoDeadcodeDrop | 96835.9 ms | 94989.0 ms | 1846.9 ms | 31713.0 ms |
| Toml | LLGoFullLTONoGlobalDCE | 94330.4 ms | 92514.1 ms | 1816.3 ms | 54807.7 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 89576.8 ms | 87879.9 ms | 1696.9 ms | 47049.7 ms |
| Toml | LLGoFullLTOGlobalDCE | 85198.0 ms | 83422.0 ms | 1776.0 ms | 45338.7 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 85008.4 ms | 83202.1 ms | 1806.3 ms | 45524.0 ms |
| IXGo | Go | 84145.9 ms | 78897.2 ms | 5248.6 ms | 24011.5 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 66473.9 ms | 65160.8 ms | 1313.2 ms | 23677.1 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 66251.9 ms | 64956.7 ms | 1295.2 ms | 40813.2 ms |
| Dustin_humanize | LLGoNoLTO | 66043.9 ms | 64875.9 ms | 1168.0 ms | 23230.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 56510.4 ms | 55297.3 ms | 1213.1 ms | 30593.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 56141.1 ms | 55005.9 ms | 1135.2 ms | 30392.5 ms |
| Etcdctl | Go | 33248.1 ms | 31260.6 ms | 1987.4 ms | 10247.7 ms |
| XGo | Go | 19208.9 ms | 18016.3 ms | 1192.6 ms | 5690.0 ms |
| Aws_restjson | Go | 7944.5 ms | 7312.9 ms | 631.7 ms | 3211.4 ms |
| Gorm_schema | Go | 5741.4 ms | 5336.4 ms | 405.1 ms | 2179.9 ms |
| Uber_zap | Go | 5291.0 ms | 4906.1 ms | 384.9 ms | 2054.1 ms |
| K8s_workqueue | Go | 4863.4 ms | 4299.0 ms | 564.4 ms | 2192.2 ms |
| Toml | Go | 2159.8 ms | 1832.7 ms | 327.1 ms | 1223.5 ms |
| Dustin_humanize | Go | 811.0 ms | 669.4 ms | 141.6 ms | 381.6 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1997833.5 ms | 1192984.3 ms | 9 |
| LLGoFullLTOGlobalDCE | 1969583.7 ms | 1144343.2 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1968269.0 ms | 1125580.2 ms | 9 |
| LLGoDeadcodeDrop | 1705395.7 ms | 570218.2 ms | 9 |
| LLGoNoLTO | 1691405.6 ms | 556477.5 ms | 9 |
| Go | 163414.0 ms | 51191.8 ms | 9 |

Dependency download details are in `download-timings.log`.
