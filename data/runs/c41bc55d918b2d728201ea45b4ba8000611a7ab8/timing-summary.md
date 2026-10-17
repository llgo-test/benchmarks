## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 689769.3 ms | 678491.5 ms | 11277.7 ms | 345539.7 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 670470.2 ms | 660082.4 ms | 10387.8 ms | 342619.7 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 633984.9 ms | 623182.4 ms | 10802.4 ms | 331448.4 ms |
| IXGo | LLGoNoLTO | 543759.2 ms | 534673.2 ms | 9086.0 ms | 154906.9 ms |
| IXGo | LLGoDeadcodeDrop | 540868.5 ms | 526233.2 ms | 14635.3 ms | 158047.5 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 302490.3 ms | 297500.1 ms | 4990.3 ms | 188372.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 298736.8 ms | 293759.1 ms | 4977.6 ms | 185663.2 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 295546.4 ms | 290816.0 ms | 4730.4 ms | 186085.6 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 240734.9 ms | 237441.0 ms | 3293.8 ms | 141904.9 ms |
| Aws_restjson | LLGoDeadcodeDrop | 238447.8 ms | 235172.4 ms | 3275.3 ms | 82112.2 ms |
| Aws_restjson | LLGoNoLTO | 237968.6 ms | 235122.8 ms | 2845.7 ms | 80679.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 227394.8 ms | 224163.6 ms | 3231.2 ms | 126052.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 225203.6 ms | 222022.2 ms | 3181.4 ms | 125393.7 ms |
| Etcdctl | LLGoDeadcodeDrop | 219077.6 ms | 213880.7 ms | 5196.9 ms | 72137.2 ms |
| Etcdctl | LLGoNoLTO | 215207.1 ms | 211059.7 ms | 4147.4 ms | 69735.5 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 210804.1 ms | 207498.5 ms | 3305.6 ms | 147928.5 ms |
| XGo | LLGoFullLTOGlobalDCE | 209643.5 ms | 206292.7 ms | 3350.9 ms | 147162.1 ms |
| XGo | LLGoFullLTONoGlobalDCE | 208834.5 ms | 205557.3 ms | 3277.2 ms | 147760.8 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 202074.3 ms | 199306.2 ms | 2768.1 ms | 125346.9 ms |
| Uber_zap | LLGoNoLTO | 197615.2 ms | 195284.3 ms | 2330.9 ms | 71757.3 ms |
| Uber_zap | LLGoDeadcodeDrop | 195712.8 ms | 192823.5 ms | 2889.3 ms | 71899.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 195077.6 ms | 192257.1 ms | 2820.5 ms | 121395.2 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 193111.9 ms | 190124.0 ms | 2987.9 ms | 121174.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 189195.2 ms | 186416.8 ms | 2778.4 ms | 111785.4 ms |
| K8s_workqueue | LLGoNoLTO | 188635.4 ms | 186021.4 ms | 2614.0 ms | 68679.3 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 188620.5 ms | 185795.5 ms | 2825.0 ms | 69746.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 188431.9 ms | 185750.0 ms | 2681.9 ms | 111792.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 179417.2 ms | 176508.8 ms | 2908.5 ms | 105282.5 ms |
| XGo | LLGoDeadcodeDrop | 125478.2 ms | 122016.9 ms | 3461.3 ms | 45690.0 ms |
| XGo | LLGoNoLTO | 122901.3 ms | 120268.9 ms | 2632.5 ms | 44475.8 ms |
| Gorm_schema | LLGoDeadcodeDrop | 104450.0 ms | 102544.0 ms | 1906.0 ms | 34291.0 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 103199.4 ms | 101511.6 ms | 1687.9 ms | 60885.6 ms |
| Gorm_schema | LLGoNoLTO | 103149.9 ms | 101615.6 ms | 1534.2 ms | 33526.1 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 101905.3 ms | 100200.7 ms | 1704.7 ms | 59346.3 ms |
| Toml | LLGoDeadcodeDrop | 97636.1 ms | 95719.2 ms | 1916.9 ms | 32025.0 ms |
| Toml | LLGoNoLTO | 97601.0 ms | 95875.3 ms | 1725.7 ms | 31370.1 ms |
| Toml | LLGoFullLTONoGlobalDCE | 95430.6 ms | 93575.7 ms | 1854.9 ms | 55531.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 90203.1 ms | 88525.4 ms | 1677.7 ms | 47509.9 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 86814.2 ms | 85042.4 ms | 1771.8 ms | 46245.2 ms |
| Toml | LLGoFullLTOGlobalDCE | 86804.9 ms | 84993.5 ms | 1811.4 ms | 46441.2 ms |
| IXGo | Go | 85328.1 ms | 80388.6 ms | 4939.6 ms | 23299.8 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 67103.1 ms | 65796.7 ms | 1306.4 ms | 23885.8 ms |
| Dustin_humanize | LLGoNoLTO | 66964.1 ms | 65809.6 ms | 1154.6 ms | 23332.1 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 66807.5 ms | 65527.6 ms | 1279.9 ms | 41380.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 57202.9 ms | 55952.3 ms | 1250.6 ms | 31197.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 56863.9 ms | 55635.5 ms | 1228.4 ms | 31100.3 ms |
| Etcdctl | Go | 33751.1 ms | 31669.4 ms | 2081.7 ms | 10139.6 ms |
| XGo | Go | 19502.1 ms | 18205.7 ms | 1296.4 ms | 6022.3 ms |
| Aws_restjson | Go | 8029.8 ms | 7371.1 ms | 658.8 ms | 3258.4 ms |
| Gorm_schema | Go | 5764.2 ms | 5373.4 ms | 390.8 ms | 2227.8 ms |
| Uber_zap | Go | 5347.7 ms | 4918.7 ms | 429.0 ms | 2198.7 ms |
| K8s_workqueue | Go | 4764.0 ms | 4324.4 ms | 439.6 ms | 1684.3 ms |
| Toml | Go | 2117.8 ms | 1884.6 ms | 233.3 ms | 1134.3 ms |
| Dustin_humanize | Go | 830.4 ms | 674.7 ms | 155.7 ms | 387.3 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTOGlobalDCE | 2052775.8 ms | 1173930.6 ms | 9 |
| LLGoFullLTONoGlobalDCE | 2039724.4 ms | 1211518.4 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2013653.0 ms | 1146896.3 ms | 9 |
| LLGoDeadcodeDrop | 1777394.6 ms | 589834.0 ms | 9 |
| LLGoNoLTO | 1773801.9 ms | 578463.0 ms | 9 |
| Go | 165435.3 ms | 50352.5 ms | 9 |

Dependency download details are in `download-timings.log`.
