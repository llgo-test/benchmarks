## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 991293.0 ms | 978220.3 ms | 13072.7 ms | 595630.5 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 952610.8 ms | 940252.6 ms | 12358.2 ms | 589137.0 ms |
| IXGo | LLGoFullLTOGlobalDCE | 898353.9 ms | 884652.3 ms | 13701.6 ms | 561164.7 ms |
| IXGo | LLGoDeadcodeDrop | 622442.7 ms | 608636.9 ms | 13805.9 ms | 189949.7 ms |
| IXGo | LLGoNoLTO | 616585.1 ms | 607404.2 ms | 9180.8 ms | 183093.9 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 450826.8 ms | 444899.8 ms | 5927.0 ms | 333653.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 448416.8 ms | 442332.4 ms | 6084.3 ms | 330337.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 441567.0 ms | 435432.2 ms | 6134.9 ms | 325374.8 ms |
| XGo | LLGoFullLTONoGlobalDCE | 347524.8 ms | 342990.5 ms | 4534.4 ms | 281929.8 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 339141.3 ms | 334964.6 ms | 4176.8 ms | 239860.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 319808.6 ms | 315748.9 ms | 4059.7 ms | 209421.1 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 300932.1 ms | 296767.8 ms | 4164.3 ms | 234657.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 293014.1 ms | 289261.1 ms | 3753.0 ms | 193872.9 ms |
| XGo | LLGoFullLTOGlobalDCE | 291794.7 ms | 287657.6 ms | 4137.1 ms | 226327.2 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 285036.2 ms | 281236.1 ms | 3800.1 ms | 207536.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 280742.2 ms | 276932.0 ms | 3810.2 ms | 202067.6 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 280650.2 ms | 277055.2 ms | 3595.0 ms | 203463.8 ms |
| Aws_restjson | LLGoNoLTO | 269858.3 ms | 266668.7 ms | 3189.5 ms | 90992.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 264498.4 ms | 260999.7 ms | 3498.8 ms | 183532.8 ms |
| Aws_restjson | LLGoDeadcodeDrop | 263429.1 ms | 259908.2 ms | 3520.9 ms | 90054.2 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 252857.3 ms | 249531.7 ms | 3325.6 ms | 175302.6 ms |
| Etcdctl | LLGoNoLTO | 236168.9 ms | 231397.8 ms | 4771.0 ms | 82536.2 ms |
| Etcdctl | LLGoDeadcodeDrop | 236096.0 ms | 229753.4 ms | 6342.5 ms | 83688.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 232167.3 ms | 228791.0 ms | 3376.3 ms | 158806.3 ms |
| Uber_zap | LLGoNoLTO | 205111.2 ms | 202303.6 ms | 2807.6 ms | 76254.0 ms |
| Uber_zap | LLGoDeadcodeDrop | 203132.1 ms | 200081.7 ms | 3050.4 ms | 76276.1 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 200391.2 ms | 197162.1 ms | 3229.1 ms | 75684.9 ms |
| K8s_workqueue | LLGoNoLTO | 195881.0 ms | 193139.5 ms | 2741.5 ms | 72872.3 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 153274.9 ms | 151104.1 ms | 2170.8 ms | 109605.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 148149.8 ms | 145826.1 ms | 2323.7 ms | 103689.6 ms |
| XGo | LLGoNoLTO | 135526.7 ms | 132594.3 ms | 2932.5 ms | 52413.6 ms |
| Toml | LLGoFullLTONoGlobalDCE | 134075.3 ms | 131687.8 ms | 2387.5 ms | 93116.8 ms |
| XGo | LLGoDeadcodeDrop | 131584.1 ms | 127821.8 ms | 3762.3 ms | 50154.2 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 120733.9 ms | 118520.1 ms | 2213.8 ms | 78472.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 116759.0 ms | 114768.0 ms | 1991.0 ms | 73331.1 ms |
| Toml | LLGoFullLTOGlobalDCE | 114178.0 ms | 112027.4 ms | 2150.6 ms | 73473.3 ms |
| Gorm_schema | LLGoDeadcodeDrop | 111226.8 ms | 109228.4 ms | 1998.4 ms | 37688.9 ms |
| Gorm_schema | LLGoNoLTO | 107013.3 ms | 105337.1 ms | 1676.1 ms | 35681.0 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 100276.5 ms | 98583.7 ms | 1692.8 ms | 73324.6 ms |
| Toml | LLGoDeadcodeDrop | 99414.5 ms | 97291.9 ms | 2122.6 ms | 33128.7 ms |
| Toml | LLGoNoLTO | 99269.2 ms | 97397.7 ms | 1871.5 ms | 33111.9 ms |
| IXGo | Go | 85820.6 ms | 80742.1 ms | 5078.5 ms | 23538.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 75086.4 ms | 73603.5 ms | 1482.9 ms | 48693.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 72629.1 ms | 71197.5 ms | 1431.6 ms | 46983.5 ms |
| Dustin_humanize | LLGoNoLTO | 69571.9 ms | 68287.0 ms | 1284.9 ms | 25039.6 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 66549.9 ms | 65205.5 ms | 1344.4 ms | 24031.8 ms |
| Etcdctl | Go | 33442.2 ms | 31474.0 ms | 1968.2 ms | 10027.3 ms |
| XGo | Go | 19797.1 ms | 18566.9 ms | 1230.2 ms | 5787.8 ms |
| Aws_restjson | Go | 8516.7 ms | 7742.7 ms | 774.0 ms | 3981.0 ms |
| Gorm_schema | Go | 5899.6 ms | 5514.9 ms | 384.7 ms | 2300.0 ms |
| Uber_zap | Go | 5524.4 ms | 5096.9 ms | 427.5 ms | 2168.3 ms |
| K8s_workqueue | Go | 4827.4 ms | 4272.5 ms | 554.9 ms | 2151.7 ms |
| Toml | Go | 2103.9 ms | 1865.4 ms | 238.5 ms | 972.2 ms |
| Dustin_humanize | Go | 806.7 ms | 663.8 ms | 142.9 ms | 389.8 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 3043416.7 ms | 2131627.9 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2855597.1 ms | 1902942.3 ms | 9 |
| LLGoFullLTOGlobalDCE | 2807384.6 ms | 1918196.1 ms | 9 |
| LLGoNoLTO | 1934985.4 ms | 651994.8 ms | 9 |
| LLGoDeadcodeDrop | 1934266.4 ms | 660657.1 ms | 9 |
| Go | 166738.5 ms | 51316.0 ms | 9 |

Dependency download details are in `download-timings.log`.
