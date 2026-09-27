## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 516173.9 ms | 502023.8 ms | 14150.1 ms | 285988.4 ms |
| IXGo | LLGoFullLTOGlobalDCE | 497197.4 ms | 485915.8 ms | 11281.6 ms | 259698.6 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 456677.3 ms | 446680.5 ms | 9996.8 ms | 238776.2 ms |
| IXGo | LLGoDeadcodeDrop | 397228.6 ms | 387895.6 ms | 9333.0 ms | 125732.9 ms |
| IXGo | LLGoNoLTO | 394249.4 ms | 385744.8 ms | 8504.6 ms | 121218.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 206679.7 ms | 202445.1 ms | 4234.5 ms | 130139.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 201915.1 ms | 197839.9 ms | 4075.2 ms | 128355.1 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 201610.8 ms | 197478.5 ms | 4132.3 ms | 128841.4 ms |
| Etcdctl | LLGoDeadcodeDrop | 150179.7 ms | 146150.4 ms | 4029.4 ms | 50741.4 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 148000.8 ms | 144909.5 ms | 3091.3 ms | 105084.0 ms |
| XGo | LLGoFullLTOGlobalDCE | 147009.8 ms | 143926.9 ms | 3082.9 ms | 103617.9 ms |
| Etcdctl | LLGoNoLTO | 143639.0 ms | 139751.8 ms | 3887.2 ms | 48836.3 ms |
| XGo | LLGoFullLTONoGlobalDCE | 140080.7 ms | 137303.0 ms | 2777.6 ms | 99789.8 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 110825.5 ms | 108658.1 ms | 2167.4 ms | 84395.3 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 103918.9 ms | 101552.4 ms | 2366.5 ms | 74568.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 102371.6 ms | 100103.6 ms | 2268.0 ms | 73813.1 ms |
| XGo | LLGoDeadcodeDrop | 86521.4 ms | 83955.9 ms | 2565.5 ms | 32839.8 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 85140.4 ms | 83514.7 ms | 1625.7 ms | 65810.9 ms |
| XGo | LLGoNoLTO | 83925.6 ms | 81449.0 ms | 2476.6 ms | 32081.4 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 81690.7 ms | 80059.0 ms | 1631.8 ms | 64999.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 81442.8 ms | 79884.2 ms | 1558.5 ms | 64081.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 79411.7 ms | 77658.4 ms | 1753.3 ms | 58458.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 78064.3 ms | 76501.0 ms | 1563.4 ms | 58095.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 71315.8 ms | 69639.5 ms | 1676.3 ms | 54808.4 ms |
| Aws_restjson | LLGoNoLTO | 67662.0 ms | 65731.6 ms | 1930.4 ms | 33601.4 ms |
| Aws_restjson | LLGoDeadcodeDrop | 66808.0 ms | 65100.5 ms | 1707.5 ms | 32854.2 ms |
| IXGo | Go | 64863.6 ms | 60596.1 ms | 4267.5 ms | 18112.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 49060.9 ms | 47775.2 ms | 1285.6 ms | 34053.0 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 48827.6 ms | 47584.5 ms | 1243.1 ms | 34357.3 ms |
| Uber_zap | LLGoNoLTO | 44160.3 ms | 42881.8 ms | 1278.5 ms | 19661.6 ms |
| Uber_zap | LLGoDeadcodeDrop | 43662.6 ms | 42364.9 ms | 1297.7 ms | 19650.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 40839.5 ms | 39675.3 ms | 1164.2 ms | 25781.8 ms |
| Toml | LLGoFullLTONoGlobalDCE | 39894.5 ms | 38898.3 ms | 996.2 ms | 30884.9 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 39120.2 ms | 37759.8 ms | 1360.4 ms | 18353.0 ms |
| K8s_workqueue | LLGoNoLTO | 38896.4 ms | 37479.9 ms | 1416.5 ms | 18711.3 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 33655.9 ms | 32629.8 ms | 1026.2 ms | 24371.4 ms |
| Toml | LLGoFullLTOGlobalDCE | 32800.5 ms | 31835.0 ms | 965.5 ms | 23513.3 ms |
| Gorm_schema | LLGoDeadcodeDrop | 30191.9 ms | 29092.5 ms | 1099.3 ms | 10950.4 ms |
| Gorm_schema | LLGoNoLTO | 30110.8 ms | 29038.9 ms | 1072.0 ms | 10342.7 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 28160.5 ms | 27350.9 ms | 809.6 ms | 22757.5 ms |
| Etcdctl | Go | 25892.3 ms | 24118.7 ms | 1773.6 ms | 8244.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 21620.0 ms | 20860.5 ms | 759.5 ms | 15739.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 21508.8 ms | 20676.5 ms | 832.3 ms | 15693.7 ms |
| Toml | LLGoNoLTO | 18923.7 ms | 18054.4 ms | 869.3 ms | 7277.5 ms |
| Toml | LLGoDeadcodeDrop | 18110.6 ms | 17214.6 ms | 896.0 ms | 7076.2 ms |
| XGo | Go | 14919.6 ms | 13810.2 ms | 1109.4 ms | 4967.9 ms |
| Dustin_humanize | LLGoNoLTO | 10840.3 ms | 10161.9 ms | 678.3 ms | 4806.1 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 10824.7 ms | 10155.8 ms | 668.9 ms | 4808.8 ms |
| Aws_restjson | Go | 6116.3 ms | 5535.2 ms | 581.2 ms | 2569.4 ms |
| Gorm_schema | Go | 4377.2 ms | 4085.0 ms | 292.2 ms | 1677.8 ms |
| Uber_zap | Go | 4015.7 ms | 3668.7 ms | 347.0 ms | 1589.4 ms |
| K8s_workqueue | Go | 3708.5 ms | 3327.8 ms | 380.8 ms | 1345.8 ms |
| Toml | Go | 1572.4 ms | 1377.5 ms | 194.9 ms | 731.4 ms |
| Dustin_humanize | Go | 650.4 ms | 533.3 ms | 117.2 ms | 327.4 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTOGlobalDCEPlugin | 1220069.0 ms | 774185.1 ms | 9 |
| LLGoFullLTOGlobalDCE | 1212918.4 ms | 761677.1 ms | 9 |
| LLGoFullLTONoGlobalDCE | 1192908.0 ms | 770613.1 ms | 9 |
| LLGoDeadcodeDrop | 842647.8 ms | 303006.6 ms | 9 |
| LLGoNoLTO | 832407.4 ms | 296536.3 ms | 9 |
| Go | 126116.2 ms | 39565.6 ms | 9 |

Dependency download details are in `download-timings.log`.
