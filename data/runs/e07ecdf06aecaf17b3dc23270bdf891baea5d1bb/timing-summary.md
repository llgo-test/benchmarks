## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 640898.6 ms | 630679.8 ms | 10218.8 ms | 330609.5 ms |
| IXGo | LLGoFullLTOGlobalDCE | 634733.2 ms | 624294.1 ms | 10439.1 ms | 328322.0 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 628666.5 ms | 617766.2 ms | 10900.2 ms | 328074.3 ms |
| IXGo | LLGoDeadcodeDrop | 512802.9 ms | 498679.2 ms | 14123.7 ms | 154040.8 ms |
| IXGo | LLGoNoLTO | 494080.2 ms | 485613.0 ms | 8467.1 ms | 145186.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 337342.8 ms | 332422.7 ms | 4920.1 ms | 196373.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 333826.7 ms | 328922.4 ms | 4904.3 ms | 194427.7 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 330752.2 ms | 325819.0 ms | 4933.2 ms | 194918.3 ms |
| Aws_restjson | LLGoDeadcodeDrop | 264178.9 ms | 260907.7 ms | 3271.2 ms | 88469.7 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 263329.8 ms | 259624.2 ms | 3705.6 ms | 145840.8 ms |
| Aws_restjson | LLGoNoLTO | 260894.2 ms | 257529.9 ms | 3364.3 ms | 87778.5 ms |
| Etcdctl | LLGoDeadcodeDrop | 259068.6 ms | 253731.9 ms | 5336.7 ms | 85868.1 ms |
| Etcdctl | LLGoNoLTO | 254729.3 ms | 250537.1 ms | 4192.2 ms | 83635.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 250416.4 ms | 246587.2 ms | 3829.2 ms | 131393.1 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 249669.8 ms | 245887.0 ms | 3782.8 ms | 130703.7 ms |
| XGo | LLGoFullLTOGlobalDCE | 241536.4 ms | 238116.7 ms | 3419.7 ms | 157160.4 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 240741.9 ms | 237470.8 ms | 3271.1 ms | 156292.6 ms |
| XGo | LLGoFullLTONoGlobalDCE | 239670.5 ms | 236304.0 ms | 3366.5 ms | 157179.0 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 228751.7 ms | 225399.5 ms | 3352.2 ms | 130678.2 ms |
| Uber_zap | LLGoDeadcodeDrop | 227280.6 ms | 224402.3 ms | 2878.3 ms | 79622.3 ms |
| Uber_zap | LLGoNoLTO | 225060.1 ms | 222175.7 ms | 2884.3 ms | 79110.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 222527.3 ms | 219253.2 ms | 3274.1 ms | 126574.8 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 221153.8 ms | 217939.0 ms | 3214.7 ms | 126371.9 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 220530.3 ms | 217560.2 ms | 2970.1 ms | 77925.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 217550.4 ms | 214297.6 ms | 3252.8 ms | 118044.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 217105.3 ms | 213930.1 ms | 3175.2 ms | 117831.0 ms |
| K8s_workqueue | LLGoNoLTO | 216836.5 ms | 213780.3 ms | 3056.2 ms | 76491.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 206868.0 ms | 203511.8 ms | 3356.2 ms | 110729.3 ms |
| XGo | LLGoDeadcodeDrop | 158395.5 ms | 154935.1 ms | 3460.5 ms | 58023.8 ms |
| XGo | LLGoNoLTO | 157150.9 ms | 154542.1 ms | 2608.9 ms | 56826.0 ms |
| Gorm_schema | LLGoDeadcodeDrop | 107280.6 ms | 105627.1 ms | 1653.5 ms | 35425.0 ms |
| Gorm_schema | LLGoNoLTO | 106126.4 ms | 104463.1 ms | 1663.4 ms | 35043.4 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 105854.7 ms | 103896.9 ms | 1957.8 ms | 61469.1 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 105701.0 ms | 103702.1 ms | 1998.9 ms | 60583.2 ms |
| Toml | LLGoDeadcodeDrop | 100524.4 ms | 98653.7 ms | 1870.7 ms | 33163.0 ms |
| Toml | LLGoNoLTO | 99455.4 ms | 97686.8 ms | 1768.6 ms | 32710.4 ms |
| Toml | LLGoFullLTONoGlobalDCE | 97947.0 ms | 95923.9 ms | 2023.1 ms | 56056.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 93636.1 ms | 91721.8 ms | 1914.3 ms | 48356.7 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 89117.3 ms | 87141.5 ms | 1975.9 ms | 46626.1 ms |
| Toml | LLGoFullLTOGlobalDCE | 88344.6 ms | 86489.1 ms | 1855.5 ms | 45828.3 ms |
| IXGo | Go | 83298.9 ms | 78326.0 ms | 4972.9 ms | 23023.3 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 70233.1 ms | 68999.4 ms | 1233.7 ms | 25081.2 ms |
| Dustin_humanize | LLGoNoLTO | 69608.7 ms | 68443.4 ms | 1165.3 ms | 24827.6 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 69565.3 ms | 68187.9 ms | 1377.4 ms | 41849.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 60031.8 ms | 58647.4 ms | 1384.5 ms | 31881.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 59792.7 ms | 58481.5 ms | 1311.2 ms | 31779.2 ms |
| Etcdctl | Go | 33449.8 ms | 31339.6 ms | 2110.3 ms | 10519.8 ms |
| XGo | Go | 18996.1 ms | 17820.6 ms | 1175.4 ms | 5740.2 ms |
| Aws_restjson | Go | 7909.8 ms | 7237.7 ms | 672.1 ms | 3143.8 ms |
| Gorm_schema | Go | 5809.8 ms | 5370.9 ms | 439.0 ms | 2397.9 ms |
| Uber_zap | Go | 5299.1 ms | 4903.3 ms | 395.9 ms | 2113.4 ms |
| K8s_workqueue | Go | 4688.2 ms | 4246.3 ms | 441.9 ms | 1646.3 ms |
| Toml | Go | 2037.7 ms | 1803.2 ms | 234.5 ms | 945.4 ms |
| Dustin_humanize | Go | 819.6 ms | 667.2 ms | 152.4 ms | 391.6 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2185691.4 ms | 1242437.5 ms | 9 |
| LLGoFullLTOGlobalDCE | 2154428.7 ms | 1194113.0 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2135411.6 ms | 1169403.4 ms | 9 |
| LLGoDeadcodeDrop | 1920295.0 ms | 637619.3 ms | 9 |
| LLGoNoLTO | 1883941.8 ms | 621609.9 ms | 9 |
| Go | 162309.1 ms | 49921.7 ms | 9 |

Dependency download details are in `download-timings.log`.
