## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 622368.5 ms | 611846.8 ms | 10521.7 ms | 325041.8 ms |
| IXGo | LLGoFullLTOGlobalDCE | 613555.0 ms | 602998.8 ms | 10556.2 ms | 323349.8 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 600451.9 ms | 590001.0 ms | 10450.8 ms | 320858.2 ms |
| IXGo | LLGoDeadcodeDrop | 475933.7 ms | 461986.8 ms | 13947.0 ms | 142047.2 ms |
| IXGo | LLGoNoLTO | 468767.1 ms | 459503.6 ms | 9263.5 ms | 136379.5 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 295426.6 ms | 290610.3 ms | 4816.3 ms | 184279.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 290951.9 ms | 286196.6 ms | 4755.3 ms | 180741.3 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 289302.5 ms | 284637.8 ms | 4664.7 ms | 182589.5 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 233101.5 ms | 229988.9 ms | 3112.6 ms | 138596.6 ms |
| Aws_restjson | LLGoDeadcodeDrop | 229758.3 ms | 226683.1 ms | 3075.2 ms | 80320.0 ms |
| Aws_restjson | LLGoNoLTO | 229383.6 ms | 226557.7 ms | 2825.9 ms | 79277.3 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 218951.1 ms | 215856.0 ms | 3095.1 ms | 123330.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 217209.3 ms | 214183.0 ms | 3026.3 ms | 122600.3 ms |
| Etcdctl | LLGoDeadcodeDrop | 214729.7 ms | 209503.2 ms | 5226.5 ms | 71776.4 ms |
| Etcdctl | LLGoNoLTO | 212153.1 ms | 207966.1 ms | 4187.0 ms | 70532.8 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 206021.4 ms | 202844.8 ms | 3176.6 ms | 145249.6 ms |
| XGo | LLGoFullLTONoGlobalDCE | 204470.7 ms | 201181.1 ms | 3289.5 ms | 144823.2 ms |
| XGo | LLGoFullLTOGlobalDCE | 203890.6 ms | 200702.0 ms | 3188.5 ms | 143099.0 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 195754.4 ms | 193072.9 ms | 2681.5 ms | 122031.1 ms |
| Uber_zap | LLGoDeadcodeDrop | 191181.9 ms | 188521.1 ms | 2660.9 ms | 71554.0 ms |
| Uber_zap | LLGoNoLTO | 191126.8 ms | 188718.2 ms | 2408.6 ms | 70659.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 190557.3 ms | 187767.9 ms | 2789.4 ms | 118781.8 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 190245.8 ms | 187442.4 ms | 2803.4 ms | 119226.9 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 185826.3 ms | 183101.6 ms | 2724.7 ms | 110411.8 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 184921.8 ms | 182092.5 ms | 2829.3 ms | 69167.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 184327.7 ms | 181669.9 ms | 2657.9 ms | 109951.6 ms |
| K8s_workqueue | LLGoNoLTO | 183618.8 ms | 181150.2 ms | 2468.5 ms | 68525.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 175006.0 ms | 172162.6 ms | 2843.3 ms | 103349.4 ms |
| XGo | LLGoDeadcodeDrop | 122974.1 ms | 119623.7 ms | 3350.3 ms | 46330.3 ms |
| XGo | LLGoNoLTO | 121368.4 ms | 118724.9 ms | 2643.5 ms | 45078.3 ms |
| Gorm_schema | LLGoDeadcodeDrop | 101382.2 ms | 99595.5 ms | 1786.7 ms | 33212.5 ms |
| Gorm_schema | LLGoNoLTO | 100389.0 ms | 98803.8 ms | 1585.2 ms | 32619.4 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 99808.2 ms | 98120.1 ms | 1688.1 ms | 58925.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 99108.9 ms | 97424.9 ms | 1683.9 ms | 57825.3 ms |
| Toml | LLGoNoLTO | 94721.1 ms | 93054.4 ms | 1666.7 ms | 30753.0 ms |
| Toml | LLGoDeadcodeDrop | 94622.0 ms | 92845.2 ms | 1776.7 ms | 31013.9 ms |
| Toml | LLGoFullLTONoGlobalDCE | 92053.4 ms | 90223.5 ms | 1829.9 ms | 53691.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 87740.2 ms | 86101.8 ms | 1638.4 ms | 45887.3 ms |
| Toml | LLGoFullLTOGlobalDCE | 83647.5 ms | 81898.6 ms | 1748.9 ms | 44678.0 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 83469.9 ms | 81714.6 ms | 1755.3 ms | 44683.7 ms |
| IXGo | Go | 82973.7 ms | 77840.0 ms | 5133.8 ms | 24038.5 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 65171.2 ms | 63886.8 ms | 1284.4 ms | 23185.7 ms |
| Dustin_humanize | LLGoNoLTO | 64934.8 ms | 63783.9 ms | 1150.9 ms | 22766.7 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 64908.6 ms | 63668.6 ms | 1240.0 ms | 39957.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 55031.3 ms | 53895.2 ms | 1136.1 ms | 29738.9 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 54906.3 ms | 53784.6 ms | 1121.7 ms | 29770.9 ms |
| Etcdctl | Go | 33178.6 ms | 30952.5 ms | 2226.1 ms | 10835.3 ms |
| XGo | Go | 18798.8 ms | 17535.7 ms | 1263.1 ms | 5792.6 ms |
| Aws_restjson | Go | 7837.9 ms | 7152.6 ms | 685.3 ms | 3118.4 ms |
| Gorm_schema | Go | 5648.0 ms | 5276.9 ms | 371.0 ms | 2133.7 ms |
| Uber_zap | Go | 5206.1 ms | 4832.9 ms | 373.1 ms | 2046.6 ms |
| K8s_workqueue | Go | 4675.8 ms | 4148.8 ms | 527.1 ms | 2156.5 ms |
| Toml | Go | 1990.4 ms | 1769.6 ms | 220.7 ms | 898.4 ms |
| Dustin_humanize | Go | 791.2 ms | 649.8 ms | 141.5 ms | 372.6 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1970096.7 ms | 1180700.5 ms | 9 |
| LLGoFullLTOGlobalDCE | 1938154.5 ms | 1130798.0 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1929841.2 ms | 1111972.2 ms | 9 |
| LLGoDeadcodeDrop | 1680674.8 ms | 568607.0 ms | 9 |
| LLGoNoLTO | 1666462.6 ms | 556592.0 ms | 9 |
| Go | 161100.5 ms | 51392.6 ms | 9 |

Dependency download details are in `download-timings.log`.
