## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTONoGlobalDCE | 652708.2 ms | 632804.3 ms | 19903.9 ms | 424683.7 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 603366.9 ms | 584313.1 ms | 19053.7 ms | 399718.9 ms |
| IXGo | LLGoFullLTOGlobalDCE | 566831.7 ms | 546994.5 ms | 19837.2 ms | 378242.5 ms |
| IXGo | LLGoDeadcodeDrop | 392874.4 ms | 372951.1 ms | 19923.3 ms | 128790.4 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 349147.8 ms | 339514.5 ms | 9633.4 ms | 264353.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 318186.0 ms | 308860.1 ms | 9325.9 ms | 235554.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 304137.7 ms | 295295.4 ms | 8842.3 ms | 228498.6 ms |
| IXGo | LLGoNoLTO | 299380.3 ms | 283653.2 ms | 15727.1 ms | 95404.7 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 280469.8 ms | 274449.5 ms | 6020.3 ms | 196932.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 231276.5 ms | 225776.3 ms | 5500.2 ms | 152743.3 ms |
| XGo | LLGoFullLTONoGlobalDCE | 229532.5 ms | 223342.9 ms | 6189.6 ms | 186734.5 ms |
| XGo | LLGoFullLTOGlobalDCE | 224637.4 ms | 218224.5 ms | 6412.9 ms | 177542.9 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 215397.9 ms | 209004.0 ms | 6394.0 ms | 169425.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 215087.9 ms | 209612.9 ms | 5475.0 ms | 138911.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 194661.7 ms | 189734.9 ms | 4926.7 ms | 139923.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 191689.5 ms | 186924.0 ms | 4765.5 ms | 132752.7 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 186051.9 ms | 181307.9 ms | 4743.9 ms | 133155.8 ms |
| Aws_restjson | LLGoNoLTO | 183080.5 ms | 178723.9 ms | 4356.6 ms | 57807.9 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 181981.5 ms | 177234.3 ms | 4747.2 ms | 132061.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 177929.5 ms | 173155.2 ms | 4774.3 ms | 121900.9 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 174928.7 ms | 170318.7 ms | 4609.9 ms | 119095.5 ms |
| Etcdctl | LLGoDeadcodeDrop | 164566.0 ms | 156564.9 ms | 8001.1 ms | 58373.8 ms |
| Aws_restjson | LLGoDeadcodeDrop | 159343.6 ms | 154834.4 ms | 4509.2 ms | 51892.5 ms |
| Etcdctl | LLGoNoLTO | 159287.0 ms | 152025.7 ms | 7261.3 ms | 55407.9 ms |
| Uber_zap | LLGoNoLTO | 140246.3 ms | 136718.7 ms | 3527.6 ms | 45559.1 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 140218.9 ms | 135967.8 ms | 4251.1 ms | 47564.1 ms |
| K8s_workqueue | LLGoNoLTO | 137855.1 ms | 134166.1 ms | 3689.0 ms | 44416.1 ms |
| Uber_zap | LLGoDeadcodeDrop | 124722.5 ms | 120941.5 ms | 3781.0 ms | 41733.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 102388.1 ms | 99502.2 ms | 2885.9 ms | 70747.2 ms |
| Toml | LLGoFullLTONoGlobalDCE | 97909.6 ms | 95092.2 ms | 2817.4 ms | 69184.4 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 95747.3 ms | 93001.1 ms | 2746.2 ms | 67960.5 ms |
| XGo | LLGoNoLTO | 93977.2 ms | 89053.1 ms | 4924.1 ms | 35437.9 ms |
| XGo | LLGoDeadcodeDrop | 92636.6 ms | 87352.3 ms | 5284.3 ms | 35089.1 ms |
| Toml | LLGoFullLTOGlobalDCE | 89628.6 ms | 86817.9 ms | 2810.7 ms | 56431.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 82633.0 ms | 79807.5 ms | 2825.5 ms | 52375.7 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 80110.1 ms | 77425.7 ms | 2684.4 ms | 51971.2 ms |
| Toml | LLGoNoLTO | 79114.3 ms | 76720.0 ms | 2394.3 ms | 27596.8 ms |
| Gorm_schema | LLGoDeadcodeDrop | 76823.1 ms | 74097.9 ms | 2725.2 ms | 27446.5 ms |
| Gorm_schema | LLGoNoLTO | 74072.2 ms | 71546.0 ms | 2526.2 ms | 26423.0 ms |
| Toml | LLGoDeadcodeDrop | 73317.6 ms | 70874.7 ms | 2442.9 ms | 26328.6 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 70071.9 ms | 68081.6 ms | 1990.3 ms | 52074.0 ms |
| IXGo | Go | 58381.2 ms | 48237.4 ms | 10143.8 ms | 16084.9 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 56079.0 ms | 54278.6 ms | 1800.4 ms | 36790.5 ms |
| Dustin_humanize | LLGoNoLTO | 50218.9 ms | 48710.0 ms | 1508.9 ms | 19053.5 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 49847.9 ms | 48202.8 ms | 1645.1 ms | 32867.2 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 44519.3 ms | 42955.6 ms | 1563.7 ms | 16886.1 ms |
| Etcdctl | Go | 25748.6 ms | 21921.0 ms | 3827.6 ms | 8127.5 ms |
| XGo | Go | 14014.8 ms | 11811.5 ms | 2203.3 ms | 4188.3 ms |
| Aws_restjson | Go | 5560.6 ms | 4473.9 ms | 1086.8 ms | 2373.4 ms |
| Gorm_schema | Go | 4245.8 ms | 3520.4 ms | 725.4 ms | 1759.6 ms |
| Uber_zap | Go | 3990.2 ms | 3278.9 ms | 711.3 ms | 1674.0 ms |
| K8s_workqueue | Go | 3854.2 ms | 3142.8 ms | 711.4 ms | 1759.1 ms |
| Toml | Go | 1518.4 ms | 1238.1 ms | 280.3 ms | 744.6 ms |
| Dustin_humanize | Go | 613.1 ms | 462.2 ms | 150.9 ms | 311.4 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2143620.5 ms | 1527139.8 ms | 9 |
| LLGoFullLTOGlobalDCE | 1955099.2 ms | 1369749.7 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1923719.1 ms | 1325744.4 ms | 9 |
| LLGoDeadcodeDrop | 1269022.0 ms | 434105.0 ms | 9 |
| LLGoNoLTO | 1217231.8 ms | 407107.0 ms | 9 |
| Go | 117927.0 ms | 37022.9 ms | 9 |

Dependency download details are in `download-timings.log`.
