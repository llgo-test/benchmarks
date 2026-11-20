## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 673796.7 ms | 656728.8 ms | 17068.0 ms | 448787.5 ms |
| IXGo | LLGoFullLTOGlobalDCE | 660474.9 ms | 643653.5 ms | 16821.3 ms | 441868.1 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 647560.6 ms | 631396.1 ms | 16164.5 ms | 433573.8 ms |
| IXGo | LLGoDeadcodeDrop | 378496.5 ms | 361461.9 ms | 17034.6 ms | 122392.8 ms |
| IXGo | LLGoNoLTO | 368555.0 ms | 354116.4 ms | 14438.6 ms | 115310.6 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 351092.4 ms | 343238.6 ms | 7853.8 ms | 260662.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 343119.4 ms | 335551.9 ms | 7567.4 ms | 256461.9 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 341557.1 ms | 334258.5 ms | 7298.6 ms | 256353.0 ms |
| XGo | LLGoFullLTONoGlobalDCE | 254546.4 ms | 249375.2 ms | 5171.3 ms | 206833.7 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 238098.7 ms | 233654.1 ms | 4444.6 ms | 163082.5 ms |
| XGo | LLGoFullLTOGlobalDCE | 223483.4 ms | 218510.5 ms | 4972.9 ms | 174250.3 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 219759.0 ms | 215448.2 ms | 4310.9 ms | 143816.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 218571.5 ms | 214320.7 ms | 4250.8 ms | 141957.9 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 217079.3 ms | 212389.5 ms | 4689.8 ms | 168604.1 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 196602.0 ms | 192946.6 ms | 3655.4 ms | 141769.8 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 190597.4 ms | 186809.7 ms | 3787.7 ms | 138689.7 ms |
| Aws_restjson | LLGoNoLTO | 187803.7 ms | 184046.2 ms | 3757.5 ms | 58625.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 187151.9 ms | 183561.0 ms | 3590.9 ms | 134232.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 185281.8 ms | 181505.8 ms | 3775.9 ms | 127068.8 ms |
| Aws_restjson | LLGoDeadcodeDrop | 183029.9 ms | 179122.0 ms | 3907.9 ms | 59113.9 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 179468.0 ms | 175835.2 ms | 3632.8 ms | 122268.9 ms |
| Etcdctl | LLGoDeadcodeDrop | 176020.6 ms | 169570.1 ms | 6450.6 ms | 61925.4 ms |
| Etcdctl | LLGoNoLTO | 174976.2 ms | 168925.2 ms | 6051.0 ms | 60383.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 162362.8 ms | 158890.0 ms | 3472.8 ms | 108508.0 ms |
| Uber_zap | LLGoNoLTO | 146634.8 ms | 143663.0 ms | 2971.8 ms | 47128.9 ms |
| Uber_zap | LLGoDeadcodeDrop | 144995.3 ms | 141830.4 ms | 3164.8 ms | 47790.0 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 142795.9 ms | 139513.3 ms | 3282.6 ms | 47779.0 ms |
| K8s_workqueue | LLGoNoLTO | 140740.7 ms | 137706.3 ms | 3034.5 ms | 45563.3 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 111754.7 ms | 109257.8 ms | 2496.9 ms | 79854.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 111405.0 ms | 108976.5 ms | 2428.5 ms | 78270.2 ms |
| Toml | LLGoFullLTONoGlobalDCE | 106315.3 ms | 103929.7 ms | 2385.6 ms | 74992.9 ms |
| XGo | LLGoDeadcodeDrop | 101467.0 ms | 96863.7 ms | 4603.3 ms | 37364.5 ms |
| XGo | LLGoNoLTO | 98217.3 ms | 94330.3 ms | 3887.0 ms | 36325.0 ms |
| Toml | LLGoFullLTOGlobalDCE | 90526.7 ms | 88282.8 ms | 2244.0 ms | 59504.7 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 90248.8 ms | 88005.7 ms | 2243.1 ms | 57832.9 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 89632.2 ms | 87481.6 ms | 2150.6 ms | 59093.6 ms |
| Gorm_schema | LLGoNoLTO | 82535.4 ms | 80490.2 ms | 2045.2 ms | 28655.4 ms |
| Gorm_schema | LLGoDeadcodeDrop | 80588.4 ms | 78422.3 ms | 2166.1 ms | 28481.5 ms |
| Toml | LLGoDeadcodeDrop | 76652.8 ms | 74623.6 ms | 2029.1 ms | 26950.0 ms |
| Toml | LLGoNoLTO | 74141.8 ms | 72311.9 ms | 1829.9 ms | 25777.0 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 73974.4 ms | 72369.0 ms | 1605.4 ms | 54337.8 ms |
| IXGo | Go | 62393.3 ms | 54440.8 ms | 7952.5 ms | 17554.5 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 57784.7 ms | 56346.8 ms | 1437.9 ms | 38094.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 57366.9 ms | 55886.9 ms | 1480.0 ms | 37839.9 ms |
| Dustin_humanize | LLGoNoLTO | 53164.9 ms | 51830.2 ms | 1334.7 ms | 20111.6 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 52230.0 ms | 50878.0 ms | 1352.0 ms | 19844.1 ms |
| Etcdctl | Go | 25064.3 ms | 22208.6 ms | 2855.7 ms | 7561.4 ms |
| XGo | Go | 14381.2 ms | 12831.6 ms | 1549.6 ms | 4240.6 ms |
| Aws_restjson | Go | 6075.2 ms | 5268.4 ms | 806.8 ms | 2478.4 ms |
| Gorm_schema | Go | 4560.6 ms | 3972.1 ms | 588.5 ms | 1842.2 ms |
| Uber_zap | Go | 4083.9 ms | 3574.4 ms | 509.5 ms | 1621.7 ms |
| K8s_workqueue | Go | 3617.7 ms | 3075.2 ms | 542.5 ms | 1551.8 ms |
| Toml | Go | 1603.3 ms | 1370.5 ms | 232.8 ms | 762.0 ms |
| Dustin_humanize | Go | 654.2 ms | 513.7 ms | 140.6 ms | 449.5 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2161006.6 ms | 1549487.5 ms | 9 |
| LLGoFullLTOGlobalDCE | 2085354.5 ms | 1455654.8 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2033250.9 ms | 1403467.2 ms | 9 |
| LLGoDeadcodeDrop | 1336276.3 ms | 451641.3 ms | 9 |
| LLGoNoLTO | 1326769.8 ms | 437880.2 ms | 9 |
| Go | 122433.7 ms | 38062.1 ms | 9 |

Dependency download details are in `download-timings.log`.
