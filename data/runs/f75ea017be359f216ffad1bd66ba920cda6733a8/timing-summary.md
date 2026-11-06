## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 847348.7 ms | 821289.1 ms | 26059.6 ms | 537299.6 ms |
| IXGo | LLGoFullLTOGlobalDCE | 834596.8 ms | 808400.3 ms | 26196.5 ms | 529984.2 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 831387.2 ms | 805598.4 ms | 25788.8 ms | 536797.6 ms |
| IXGo | LLGoDeadcodeDrop | 506375.7 ms | 479988.3 ms | 26387.4 ms | 156886.0 ms |
| IXGo | LLGoNoLTO | 479505.1 ms | 457604.8 ms | 21900.3 ms | 146076.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 427561.1 ms | 415511.0 ms | 12050.1 ms | 309611.0 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 424748.1 ms | 412893.5 ms | 11854.6 ms | 310006.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 420506.4 ms | 408910.0 ms | 11596.4 ms | 303754.8 ms |
| XGo | LLGoFullLTONoGlobalDCE | 312708.2 ms | 304594.6 ms | 8113.6 ms | 248644.2 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 291913.8 ms | 285291.0 ms | 6622.8 ms | 199346.3 ms |
| XGo | LLGoFullLTOGlobalDCE | 273417.8 ms | 265642.6 ms | 7775.2 ms | 208317.1 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 272296.7 ms | 264428.5 ms | 7868.2 ms | 207149.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 267601.1 ms | 261440.2 ms | 6160.9 ms | 170811.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 265860.6 ms | 259584.7 ms | 6275.9 ms | 170275.0 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 246067.7 ms | 240843.6 ms | 5224.1 ms | 172706.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 238025.3 ms | 232760.6 ms | 5264.7 ms | 167039.2 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 236672.9 ms | 231166.5 ms | 5506.4 ms | 166950.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 226065.9 ms | 220741.7 ms | 5324.2 ms | 151752.5 ms |
| Etcdctl | LLGoDeadcodeDrop | 225319.6 ms | 214670.1 ms | 10649.5 ms | 76488.1 ms |
| Etcdctl | LLGoNoLTO | 224494.0 ms | 214811.9 ms | 9682.1 ms | 75593.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 220292.0 ms | 215036.4 ms | 5255.6 ms | 146388.0 ms |
| Aws_restjson | LLGoDeadcodeDrop | 214305.4 ms | 208722.6 ms | 5582.8 ms | 67084.7 ms |
| Aws_restjson | LLGoNoLTO | 212088.8 ms | 206978.7 ms | 5110.0 ms | 66278.8 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 210448.1 ms | 205278.9 ms | 5169.3 ms | 137419.5 ms |
| Uber_zap | LLGoDeadcodeDrop | 172361.9 ms | 167658.5 ms | 4703.4 ms | 55330.7 ms |
| Uber_zap | LLGoNoLTO | 172192.9 ms | 168077.7 ms | 4115.1 ms | 55136.8 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 164664.8 ms | 160133.2 ms | 4531.6 ms | 53417.4 ms |
| K8s_workqueue | LLGoNoLTO | 164371.7 ms | 160162.4 ms | 4209.3 ms | 52548.8 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 145395.4 ms | 141531.5 ms | 3863.9 ms | 101405.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 144295.3 ms | 140431.4 ms | 3863.9 ms | 99453.9 ms |
| Toml | LLGoFullLTONoGlobalDCE | 135153.0 ms | 131518.8 ms | 3634.2 ms | 94024.0 ms |
| XGo | LLGoDeadcodeDrop | 125832.9 ms | 118577.9 ms | 7255.0 ms | 44282.6 ms |
| XGo | LLGoNoLTO | 125201.2 ms | 119029.2 ms | 6172.0 ms | 45023.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 121030.3 ms | 117351.6 ms | 3678.7 ms | 75932.0 ms |
| Toml | LLGoFullLTOGlobalDCE | 115857.2 ms | 112461.0 ms | 3396.2 ms | 74378.2 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 115652.1 ms | 112366.9 ms | 3285.2 ms | 74022.4 ms |
| Gorm_schema | LLGoDeadcodeDrop | 106643.6 ms | 103300.4 ms | 3343.1 ms | 36723.7 ms |
| Gorm_schema | LLGoNoLTO | 105884.7 ms | 102732.4 ms | 3152.3 ms | 35881.7 ms |
| Toml | LLGoDeadcodeDrop | 99519.7 ms | 96525.4 ms | 2994.2 ms | 33852.6 ms |
| Toml | LLGoNoLTO | 99370.9 ms | 96610.2 ms | 2760.7 ms | 33459.4 ms |
| IXGo | Go | 97490.1 ms | 82917.2 ms | 14572.9 ms | 26796.3 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 94549.1 ms | 92107.8 ms | 2441.3 ms | 67951.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 75935.3 ms | 73701.0 ms | 2234.3 ms | 48841.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 75480.8 ms | 73265.3 ms | 2215.5 ms | 48743.0 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 68655.9 ms | 66482.7 ms | 2173.1 ms | 25271.2 ms |
| Dustin_humanize | LLGoNoLTO | 67748.4 ms | 65855.4 ms | 1893.0 ms | 24832.4 ms |
| Etcdctl | Go | 38433.2 ms | 32867.1 ms | 5566.0 ms | 12002.9 ms |
| XGo | Go | 22059.7 ms | 18952.1 ms | 3107.6 ms | 6546.9 ms |
| Aws_restjson | Go | 9145.9 ms | 7627.0 ms | 1518.9 ms | 3738.7 ms |
| Gorm_schema | Go | 6560.9 ms | 5589.3 ms | 971.6 ms | 2554.6 ms |
| Uber_zap | Go | 5951.7 ms | 5087.7 ms | 863.9 ms | 2439.8 ms |
| K8s_workqueue | Go | 5492.4 ms | 4437.8 ms | 1054.6 ms | 2487.3 ms |
| Toml | Go | 2266.0 ms | 1852.8 ms | 413.2 ms | 1080.2 ms |
| Dustin_humanize | Go | 939.5 ms | 693.4 ms | 246.2 ms | 455.1 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2718595.3 ms | 1897833.7 ms | 9 |
| LLGoFullLTOGlobalDCE | 2595846.8 ms | 1754233.8 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2556424.9 ms | 1706938.6 ms | 9 |
| LLGoDeadcodeDrop | 1683679.4 ms | 549337.0 ms | 9 |
| LLGoNoLTO | 1650857.8 ms | 534830.3 ms | 9 |
| Go | 188339.4 ms | 58101.7 ms | 9 |

Dependency download details are in `download-timings.log`.
