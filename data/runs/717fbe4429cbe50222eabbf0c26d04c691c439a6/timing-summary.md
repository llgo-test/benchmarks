## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 823368.6 ms | 793527.3 ms | 29841.3 ms | 540147.9 ms |
| IXGo | LLGoFullLTOGlobalDCE | 808659.4 ms | 778735.4 ms | 29924.0 ms | 526643.7 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 788195.6 ms | 758792.8 ms | 29402.8 ms | 519667.1 ms |
| IXGo | LLGoDeadcodeDrop | 462579.2 ms | 433427.2 ms | 29152.0 ms | 146948.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 443958.2 ms | 430290.8 ms | 13667.4 ms | 325889.7 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 443015.0 ms | 428858.7 ms | 14156.3 ms | 327701.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 442738.8 ms | 429017.2 ms | 13721.6 ms | 324990.3 ms |
| IXGo | LLGoNoLTO | 441419.5 ms | 416652.4 ms | 24767.1 ms | 136537.7 ms |
| XGo | LLGoFullLTONoGlobalDCE | 327535.9 ms | 318019.1 ms | 9516.8 ms | 263353.3 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 325855.2 ms | 317527.0 ms | 8328.2 ms | 222122.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 302279.1 ms | 294017.2 ms | 8261.9 ms | 193531.1 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 300343.9 ms | 292182.2 ms | 8161.7 ms | 192229.3 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 291369.9 ms | 282099.5 ms | 9270.4 ms | 225608.2 ms |
| XGo | LLGoFullLTOGlobalDCE | 290864.0 ms | 281473.1 ms | 9390.9 ms | 225797.9 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 278897.7 ms | 271553.4 ms | 7344.3 ms | 195715.3 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 270252.1 ms | 262966.8 ms | 7285.3 ms | 190863.1 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 269992.2 ms | 262736.7 ms | 7255.6 ms | 189962.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 257436.9 ms | 250604.3 ms | 6832.6 ms | 174325.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 253173.2 ms | 246226.3 ms | 6947.0 ms | 169460.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 235350.4 ms | 228507.9 ms | 6842.4 ms | 156260.8 ms |
| Aws_restjson | LLGoNoLTO | 234178.6 ms | 227703.2 ms | 6475.3 ms | 72750.6 ms |
| Aws_restjson | LLGoDeadcodeDrop | 227089.9 ms | 220242.9 ms | 6846.9 ms | 72589.2 ms |
| Etcdctl | LLGoDeadcodeDrop | 225573.5 ms | 213746.5 ms | 11827.0 ms | 78176.0 ms |
| Etcdctl | LLGoNoLTO | 224151.2 ms | 213565.4 ms | 10585.8 ms | 76717.8 ms |
| Uber_zap | LLGoNoLTO | 190833.2 ms | 185423.8 ms | 5409.4 ms | 60708.8 ms |
| Uber_zap | LLGoDeadcodeDrop | 190520.8 ms | 184823.8 ms | 5697.0 ms | 61997.5 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 182900.8 ms | 177088.4 ms | 5812.4 ms | 59792.0 ms |
| K8s_workqueue | LLGoNoLTO | 182748.4 ms | 177698.6 ms | 5049.9 ms | 58051.3 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 142178.4 ms | 137883.3 ms | 4295.1 ms | 98574.1 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 141701.8 ms | 137400.2 ms | 4301.5 ms | 96924.4 ms |
| Toml | LLGoFullLTONoGlobalDCE | 134988.5 ms | 130665.7 ms | 4322.8 ms | 92001.9 ms |
| XGo | LLGoNoLTO | 126757.4 ms | 119900.0 ms | 6857.5 ms | 46601.7 ms |
| XGo | LLGoDeadcodeDrop | 125745.8 ms | 117709.2 ms | 8036.6 ms | 45868.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 119621.4 ms | 115631.7 ms | 3989.8 ms | 74515.9 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 118244.6 ms | 114218.2 ms | 4026.4 ms | 75054.9 ms |
| Toml | LLGoFullLTOGlobalDCE | 117915.3 ms | 113747.1 ms | 4168.2 ms | 75193.1 ms |
| Gorm_schema | LLGoDeadcodeDrop | 105687.1 ms | 101726.3 ms | 3960.7 ms | 37087.7 ms |
| Gorm_schema | LLGoNoLTO | 103281.2 ms | 99658.4 ms | 3622.8 ms | 35963.2 ms |
| Toml | LLGoNoLTO | 99064.0 ms | 95708.1 ms | 3355.9 ms | 33957.3 ms |
| Toml | LLGoDeadcodeDrop | 98604.9 ms | 95192.7 ms | 3412.2 ms | 34201.8 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 93012.5 ms | 90234.4 ms | 2778.1 ms | 66562.5 ms |
| IXGo | Go | 91413.7 ms | 75525.7 ms | 15888.0 ms | 25281.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 75408.2 ms | 72861.9 ms | 2546.3 ms | 48120.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 74788.2 ms | 72237.0 ms | 2551.2 ms | 48074.1 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 68083.4 ms | 65628.4 ms | 2455.1 ms | 25640.7 ms |
| Dustin_humanize | LLGoNoLTO | 66654.0 ms | 64336.6 ms | 2317.3 ms | 25018.3 ms |
| Etcdctl | Go | 36103.7 ms | 30464.6 ms | 5639.1 ms | 10879.8 ms |
| XGo | Go | 20655.9 ms | 17356.6 ms | 3299.3 ms | 6059.4 ms |
| Aws_restjson | Go | 8627.0 ms | 6947.9 ms | 1679.1 ms | 3612.8 ms |
| Gorm_schema | Go | 6290.5 ms | 5201.5 ms | 1089.0 ms | 2475.8 ms |
| Uber_zap | Go | 5733.8 ms | 4764.9 ms | 968.9 ms | 2313.5 ms |
| K8s_workqueue | Go | 5052.9 ms | 4089.4 ms | 963.6 ms | 1814.6 ms |
| Toml | Go | 2245.4 ms | 1772.2 ms | 473.2 ms | 1160.4 ms |
| Dustin_humanize | Go | 872.4 ms | 633.7 ms | 238.8 ms | 428.4 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2803930.8 ms | 1976561.5 ms | 9 |
| LLGoFullLTOGlobalDCE | 2706375.6 ms | 1855442.3 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2660838.3 ms | 1807287.0 ms | 9 |
| LLGoDeadcodeDrop | 1686785.4 ms | 562301.6 ms | 9 |
| LLGoNoLTO | 1669087.5 ms | 546306.6 ms | 9 |
| Go | 176995.4 ms | 54026.0 ms | 9 |

Dependency download details are in `download-timings.log`.
