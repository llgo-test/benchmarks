## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 945816.9 ms | 933541.3 ms | 12275.6 ms | 580382.9 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 940432.6 ms | 927198.5 ms | 13234.1 ms | 584544.9 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 834071.0 ms | 820319.1 ms | 13751.9 ms | 542169.4 ms |
| IXGo | LLGoNoLTO | 557578.0 ms | 547843.1 ms | 9734.9 ms | 169807.1 ms |
| IXGo | LLGoDeadcodeDrop | 508732.8 ms | 494247.1 ms | 14485.7 ms | 161599.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 442831.4 ms | 436952.2 ms | 5879.2 ms | 325244.8 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 438844.7 ms | 432951.3 ms | 5893.4 ms | 325422.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 429381.3 ms | 423697.7 ms | 5683.6 ms | 316122.0 ms |
| XGo | LLGoFullLTONoGlobalDCE | 331314.5 ms | 326920.3 ms | 4394.2 ms | 267812.0 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 330900.8 ms | 326801.5 ms | 4099.4 ms | 232355.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 297580.6 ms | 293753.5 ms | 3827.1 ms | 197286.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 296940.9 ms | 293103.5 ms | 3837.4 ms | 196051.3 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 288437.1 ms | 284452.6 ms | 3984.5 ms | 223800.7 ms |
| XGo | LLGoFullLTOGlobalDCE | 284776.2 ms | 280799.3 ms | 3976.8 ms | 221572.5 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 278506.9 ms | 275027.1 ms | 3479.8 ms | 201805.2 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 266930.2 ms | 263373.3 ms | 3556.9 ms | 194159.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 265964.5 ms | 262458.4 ms | 3506.1 ms | 191929.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 262096.4 ms | 258664.2 ms | 3432.2 ms | 181855.9 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 254336.8 ms | 250951.7 ms | 3385.1 ms | 175858.9 ms |
| Aws_restjson | LLGoDeadcodeDrop | 243924.6 ms | 240450.0 ms | 3474.6 ms | 86049.2 ms |
| Aws_restjson | LLGoNoLTO | 236189.1 ms | 233167.1 ms | 3022.0 ms | 83692.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 235338.1 ms | 232054.1 ms | 3284.0 ms | 161197.2 ms |
| Etcdctl | LLGoDeadcodeDrop | 231278.1 ms | 225664.8 ms | 5613.2 ms | 82564.0 ms |
| Etcdctl | LLGoNoLTO | 225788.1 ms | 221620.4 ms | 4167.8 ms | 80817.0 ms |
| Uber_zap | LLGoNoLTO | 202016.9 ms | 199308.0 ms | 2708.9 ms | 76563.9 ms |
| Uber_zap | LLGoDeadcodeDrop | 198045.0 ms | 195131.9 ms | 2913.1 ms | 74646.2 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 193149.9 ms | 190085.3 ms | 3064.6 ms | 73562.5 ms |
| K8s_workqueue | LLGoNoLTO | 191173.4 ms | 188620.3 ms | 2553.0 ms | 72344.2 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 150239.4 ms | 147939.6 ms | 2299.8 ms | 106536.7 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 146760.9 ms | 144490.0 ms | 2270.9 ms | 102616.3 ms |
| XGo | LLGoDeadcodeDrop | 134300.5 ms | 130453.6 ms | 3846.9 ms | 52015.9 ms |
| Toml | LLGoFullLTONoGlobalDCE | 131705.8 ms | 129347.5 ms | 2358.3 ms | 92268.2 ms |
| XGo | LLGoNoLTO | 131051.6 ms | 128145.4 ms | 2906.2 ms | 52156.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 118082.1 ms | 116104.6 ms | 1977.5 ms | 74536.0 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 117608.6 ms | 115414.2 ms | 2194.4 ms | 75685.2 ms |
| Toml | LLGoFullLTOGlobalDCE | 117558.2 ms | 115325.9 ms | 2232.2 ms | 75513.1 ms |
| Gorm_schema | LLGoDeadcodeDrop | 106387.5 ms | 104378.3 ms | 2009.2 ms | 35991.4 ms |
| Gorm_schema | LLGoNoLTO | 104322.7 ms | 102550.1 ms | 1772.6 ms | 34984.7 ms |
| Toml | LLGoDeadcodeDrop | 99043.5 ms | 96940.8 ms | 2102.8 ms | 33311.1 ms |
| Toml | LLGoNoLTO | 98741.8 ms | 96870.2 ms | 1871.6 ms | 32901.2 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 95263.3 ms | 93581.9 ms | 1681.4 ms | 69392.0 ms |
| IXGo | Go | 84501.0 ms | 79497.6 ms | 5003.4 ms | 23129.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 73569.3 ms | 72057.6 ms | 1511.7 ms | 47788.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 72782.8 ms | 71292.7 ms | 1490.1 ms | 46928.8 ms |
| Dustin_humanize | LLGoNoLTO | 67697.9 ms | 66373.9 ms | 1324.0 ms | 24381.8 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 67204.8 ms | 65754.8 ms | 1450.0 ms | 24320.7 ms |
| Etcdctl | Go | 33554.2 ms | 31511.6 ms | 2042.6 ms | 10037.5 ms |
| XGo | Go | 19381.1 ms | 18170.2 ms | 1210.9 ms | 5725.5 ms |
| Aws_restjson | Go | 8143.1 ms | 7464.5 ms | 678.6 ms | 3352.2 ms |
| Gorm_schema | Go | 5762.7 ms | 5402.0 ms | 360.7 ms | 2207.7 ms |
| Uber_zap | Go | 5303.6 ms | 4911.4 ms | 392.2 ms | 2059.5 ms |
| K8s_workqueue | Go | 4784.0 ms | 4245.0 ms | 539.0 ms | 1953.3 ms |
| Toml | Go | 1994.4 ms | 1754.3 ms | 240.2 ms | 906.3 ms |
| Dustin_humanize | Go | 796.1 ms | 656.2 ms | 139.9 ms | 374.0 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2857776.4 ms | 2031920.0 ms | 9 |
| LLGoFullLTOGlobalDCE | 2836167.8 ms | 1923329.8 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2754126.9 ms | 1855584.2 ms | 9 |
| LLGoNoLTO | 1814559.5 ms | 627648.9 ms | 9 |
| LLGoDeadcodeDrop | 1782066.7 ms | 624060.0 ms | 9 |
| Go | 164220.3 ms | 49744.9 ms | 9 |

Dependency download details are in `download-timings.log`.
