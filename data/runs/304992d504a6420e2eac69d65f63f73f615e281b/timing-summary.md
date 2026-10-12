## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 707287.1 ms | 696648.9 ms | 10638.1 ms | 354405.2 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 561289.6 ms | 551949.0 ms | 9340.6 ms | 288194.2 ms |
| IXGo | LLGoFullLTOGlobalDCE | 530219.2 ms | 520494.2 ms | 9725.0 ms | 281362.7 ms |
| IXGo | LLGoNoLTO | 505520.8 ms | 495939.9 ms | 9580.9 ms | 149600.1 ms |
| IXGo | LLGoDeadcodeDrop | 447647.4 ms | 435747.5 ms | 11899.8 ms | 132100.1 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 235777.4 ms | 231343.5 ms | 4433.9 ms | 154284.5 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 235606.3 ms | 231270.6 ms | 4335.8 ms | 151908.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 232992.6 ms | 228522.9 ms | 4469.7 ms | 151598.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 209987.6 ms | 206957.8 ms | 3029.8 ms | 115664.7 ms |
| Aws_restjson | LLGoNoLTO | 198077.6 ms | 195307.5 ms | 2770.1 ms | 66186.5 ms |
| Aws_restjson | LLGoDeadcodeDrop | 189992.0 ms | 186990.7 ms | 3001.2 ms | 65980.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 185319.3 ms | 182263.3 ms | 3055.9 ms | 107822.2 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 184635.8 ms | 181700.5 ms | 2935.3 ms | 112199.8 ms |
| XGo | LLGoFullLTONoGlobalDCE | 177463.5 ms | 174356.7 ms | 3106.8 ms | 129946.4 ms |
| XGo | LLGoFullLTOGlobalDCE | 173580.7 ms | 170427.7 ms | 3153.0 ms | 125848.1 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 170472.3 ms | 167371.9 ms | 3100.4 ms | 124205.9 ms |
| Etcdctl | LLGoNoLTO | 168807.5 ms | 164522.1 ms | 4285.4 ms | 55815.8 ms |
| Etcdctl | LLGoDeadcodeDrop | 165275.5 ms | 160692.3 ms | 4583.2 ms | 56430.4 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 163073.4 ms | 160449.3 ms | 2624.1 ms | 105914.7 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 156064.2 ms | 153385.1 ms | 2679.1 ms | 102096.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 152127.0 ms | 149432.6 ms | 2694.4 ms | 98285.9 ms |
| Uber_zap | LLGoNoLTO | 151997.4 ms | 149647.9 ms | 2349.6 ms | 57396.5 ms |
| Uber_zap | LLGoDeadcodeDrop | 149464.3 ms | 146879.1 ms | 2585.2 ms | 57278.0 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 148932.7 ms | 146188.2 ms | 2744.4 ms | 57559.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 145601.8 ms | 143044.9 ms | 2557.0 ms | 89183.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 144100.6 ms | 141568.5 ms | 2532.1 ms | 88336.5 ms |
| K8s_workqueue | LLGoNoLTO | 143888.8 ms | 141519.9 ms | 2368.9 ms | 54118.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 138805.4 ms | 136217.6 ms | 2587.8 ms | 85080.7 ms |
| XGo | LLGoNoLTO | 94905.6 ms | 92381.0 ms | 2524.6 ms | 35232.8 ms |
| XGo | LLGoDeadcodeDrop | 94188.9 ms | 91201.1 ms | 2987.8 ms | 36690.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 81449.1 ms | 79741.5 ms | 1707.6 ms | 49547.6 ms |
| Gorm_schema | LLGoNoLTO | 79747.1 ms | 78184.9 ms | 1562.2 ms | 26648.2 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 79245.4 ms | 77560.0 ms | 1685.4 ms | 48597.5 ms |
| Gorm_schema | LLGoDeadcodeDrop | 78966.8 ms | 77240.2 ms | 1726.7 ms | 26647.6 ms |
| Toml | LLGoDeadcodeDrop | 74761.8 ms | 72918.0 ms | 1843.8 ms | 25272.9 ms |
| Toml | LLGoFullLTONoGlobalDCE | 74760.3 ms | 73031.2 ms | 1729.2 ms | 45490.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 69886.9 ms | 68321.4 ms | 1565.5 ms | 38623.2 ms |
| Toml | LLGoNoLTO | 69168.3 ms | 67669.2 ms | 1499.0 ms | 22874.2 ms |
| Toml | LLGoFullLTOGlobalDCE | 68300.7 ms | 66538.3 ms | 1762.4 ms | 38010.0 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 64744.8 ms | 63104.3 ms | 1640.5 ms | 35757.7 ms |
| IXGo | Go | 63806.1 ms | 59419.5 ms | 4386.6 ms | 18078.4 ms |
| Dustin_humanize | LLGoNoLTO | 50667.9 ms | 49544.9 ms | 1123.0 ms | 18152.8 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 50657.7 ms | 49387.0 ms | 1270.7 ms | 18603.9 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 50588.0 ms | 49393.5 ms | 1194.5 ms | 32385.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 43527.4 ms | 42363.0 ms | 1164.4 ms | 24562.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 43486.2 ms | 42328.5 ms | 1157.7 ms | 25069.6 ms |
| Etcdctl | Go | 25770.0 ms | 24020.6 ms | 1749.4 ms | 8331.4 ms |
| XGo | Go | 14224.8 ms | 13277.7 ms | 947.0 ms | 4254.0 ms |
| Aws_restjson | Go | 6141.6 ms | 5579.2 ms | 562.4 ms | 2692.4 ms |
| Gorm_schema | Go | 4456.7 ms | 4116.7 ms | 340.0 ms | 2308.2 ms |
| Uber_zap | Go | 4000.2 ms | 3675.9 ms | 324.3 ms | 1621.4 ms |
| K8s_workqueue | Go | 3541.3 ms | 3173.2 ms | 368.1 ms | 1283.5 ms |
| Toml | Go | 1501.7 ms | 1304.6 ms | 197.1 ms | 700.4 ms |
| Dustin_humanize | Go | 606.3 ms | 487.4 ms | 118.9 ms | 303.4 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTOGlobalDCEPlugin | 1761210.2 ms | 1012056.8 ms | 9 |
| LLGoFullLTONoGlobalDCE | 1682897.6 ms | 1019109.6 ms | 9 |
| LLGoFullLTOGlobalDCE | 1636285.1 ms | 973216.2 ms | 9 |
| LLGoNoLTO | 1462781.0 ms | 486025.2 ms | 9 |
| LLGoDeadcodeDrop | 1399887.1 ms | 476562.5 ms | 9 |
| Go | 124048.7 ms | 39573.2 ms | 9 |

Dependency download details are in `download-timings.log`.
