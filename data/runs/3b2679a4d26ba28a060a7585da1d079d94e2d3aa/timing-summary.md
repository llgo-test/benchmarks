## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 636119.3 ms | 624462.5 ms | 11656.8 ms | 336524.5 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 629243.6 ms | 617582.8 ms | 11660.7 ms | 336731.4 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 619217.0 ms | 607818.6 ms | 11398.4 ms | 331024.1 ms |
| IXGo | LLGoDeadcodeDrop | 470938.6 ms | 457029.3 ms | 13909.3 ms | 139166.6 ms |
| IXGo | LLGoNoLTO | 465981.6 ms | 455453.3 ms | 10528.4 ms | 135097.6 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 288329.5 ms | 282706.4 ms | 5623.1 ms | 183130.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 288086.0 ms | 283069.1 ms | 5016.9 ms | 183584.9 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 281702.1 ms | 276638.1 ms | 5064.0 ms | 182970.2 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 220581.2 ms | 217069.6 ms | 3511.7 ms | 136156.2 ms |
| Aws_restjson | LLGoDeadcodeDrop | 216676.0 ms | 213727.0 ms | 2949.0 ms | 74410.7 ms |
| Aws_restjson | LLGoNoLTO | 213214.5 ms | 210263.9 ms | 2950.6 ms | 73586.3 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 211164.1 ms | 207724.2 ms | 3439.9 ms | 122585.3 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 211016.9 ms | 207509.1 ms | 3507.9 ms | 121833.4 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 202006.3 ms | 198613.2 ms | 3393.1 ms | 146147.4 ms |
| XGo | LLGoFullLTOGlobalDCE | 200371.6 ms | 196895.1 ms | 3476.5 ms | 144034.1 ms |
| XGo | LLGoFullLTONoGlobalDCE | 200370.0 ms | 196941.1 ms | 3428.9 ms | 145342.0 ms |
| Etcdctl | LLGoDeadcodeDrop | 198725.2 ms | 193759.4 ms | 4965.9 ms | 66273.2 ms |
| Etcdctl | LLGoNoLTO | 198430.0 ms | 194090.7 ms | 4339.3 ms | 64543.1 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 185482.5 ms | 182542.6 ms | 2939.9 ms | 121160.1 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 179785.2 ms | 176798.0 ms | 2987.2 ms | 117054.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 178818.1 ms | 175865.9 ms | 2952.2 ms | 115797.5 ms |
| Uber_zap | LLGoDeadcodeDrop | 176989.6 ms | 174356.5 ms | 2633.1 ms | 65618.9 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 175570.3 ms | 172706.3 ms | 2864.0 ms | 108423.3 ms |
| Uber_zap | LLGoNoLTO | 174047.3 ms | 171607.5 ms | 2439.7 ms | 64429.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 173860.0 ms | 171003.7 ms | 2856.3 ms | 107285.1 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 167715.2 ms | 165246.6 ms | 2468.6 ms | 63115.4 ms |
| K8s_workqueue | LLGoNoLTO | 167422.0 ms | 164913.5 ms | 2508.5 ms | 61906.1 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 163538.1 ms | 160601.4 ms | 2936.8 ms | 99850.3 ms |
| XGo | LLGoDeadcodeDrop | 112360.8 ms | 109145.1 ms | 3215.7 ms | 41202.7 ms |
| XGo | LLGoNoLTO | 111875.2 ms | 109202.1 ms | 2673.1 ms | 40326.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 96145.2 ms | 94217.7 ms | 1927.5 ms | 58584.9 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 96097.3 ms | 93793.9 ms | 2303.5 ms | 59238.9 ms |
| Gorm_schema | LLGoDeadcodeDrop | 94580.8 ms | 92916.2 ms | 1664.6 ms | 31473.6 ms |
| Gorm_schema | LLGoNoLTO | 92478.2 ms | 90864.5 ms | 1613.7 ms | 30919.7 ms |
| Toml | LLGoFullLTONoGlobalDCE | 87029.6 ms | 85280.4 ms | 1749.2 ms | 53211.6 ms |
| Toml | LLGoDeadcodeDrop | 86852.8 ms | 85235.8 ms | 1617.0 ms | 29048.8 ms |
| Toml | LLGoNoLTO | 86458.5 ms | 84895.1 ms | 1563.3 ms | 28743.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 83540.7 ms | 81755.2 ms | 1785.5 ms | 45800.1 ms |
| IXGo | Go | 79826.3 ms | 74169.3 ms | 5657.0 ms | 21962.0 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 78798.6 ms | 77097.5 ms | 1701.0 ms | 44389.7 ms |
| Toml | LLGoFullLTOGlobalDCE | 77298.6 ms | 75650.8 ms | 1647.8 ms | 43387.4 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 61886.5 ms | 60624.2 ms | 1262.3 ms | 39867.5 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 59943.2 ms | 58859.7 ms | 1083.5 ms | 21770.9 ms |
| Dustin_humanize | LLGoNoLTO | 59638.4 ms | 58572.5 ms | 1065.9 ms | 21532.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 52540.9 ms | 51282.5 ms | 1258.4 ms | 30129.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 51784.3 ms | 50598.0 ms | 1186.3 ms | 29682.1 ms |
| Etcdctl | Go | 31965.9 ms | 29768.8 ms | 2197.1 ms | 9554.9 ms |
| XGo | Go | 18639.8 ms | 17190.1 ms | 1449.8 ms | 6809.3 ms |
| Aws_restjson | Go | 7697.5 ms | 6983.2 ms | 714.4 ms | 3222.2 ms |
| Gorm_schema | Go | 5547.2 ms | 5135.8 ms | 411.4 ms | 2170.1 ms |
| Uber_zap | Go | 5286.3 ms | 4841.8 ms | 444.6 ms | 2093.6 ms |
| K8s_workqueue | Go | 4480.9 ms | 4086.6 ms | 394.3 ms | 1596.2 ms |
| Toml | Go | 1976.7 ms | 1767.2 ms | 209.5 ms | 895.3 ms |
| Dustin_humanize | Go | 777.8 ms | 644.7 ms | 133.1 ms | 377.2 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1932151.6 ms | 1186025.2 ms | 9 |
| LLGoFullLTOGlobalDCE | 1913499.9 ms | 1140713.9 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1884732.1 ms | 1117187.1 ms | 9 |
| LLGoDeadcodeDrop | 1584782.2 ms | 532080.8 ms | 9 |
| LLGoNoLTO | 1569545.6 ms | 521084.4 ms | 9 |
| Go | 156198.5 ms | 48681.0 ms | 9 |

Dependency download details are in `download-timings.log`.
