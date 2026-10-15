## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 724365.6 ms | 714061.1 ms | 10304.5 ms | 361639.2 ms |
| IXGo | LLGoFullLTOGlobalDCE | 690295.9 ms | 679424.0 ms | 10871.9 ms | 349732.2 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 656901.7 ms | 646563.7 ms | 10338.0 ms | 342211.6 ms |
| IXGo | LLGoNoLTO | 581413.9 ms | 572056.7 ms | 9357.2 ms | 163866.7 ms |
| IXGo | LLGoDeadcodeDrop | 531687.7 ms | 516935.5 ms | 14752.2 ms | 155670.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 318666.3 ms | 313411.4 ms | 5254.9 ms | 197664.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 311418.5 ms | 306313.8 ms | 5104.7 ms | 194309.7 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 305290.2 ms | 300253.5 ms | 5036.7 ms | 191372.0 ms |
| Aws_restjson | LLGoNoLTO | 248481.2 ms | 245499.5 ms | 2981.7 ms | 84404.7 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 243944.8 ms | 240601.5 ms | 3343.3 ms | 143400.6 ms |
| Aws_restjson | LLGoDeadcodeDrop | 238874.9 ms | 235539.1 ms | 3335.7 ms | 82349.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 238423.7 ms | 235102.6 ms | 3321.1 ms | 131800.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 230529.8 ms | 227279.6 ms | 3250.2 ms | 128453.2 ms |
| Etcdctl | LLGoDeadcodeDrop | 227684.5 ms | 222058.3 ms | 5626.2 ms | 75610.1 ms |
| Etcdctl | LLGoNoLTO | 226011.2 ms | 221291.8 ms | 4719.4 ms | 72909.1 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 220431.8 ms | 216958.5 ms | 3473.3 ms | 155117.4 ms |
| XGo | LLGoFullLTONoGlobalDCE | 210871.5 ms | 207573.0 ms | 3298.4 ms | 148970.2 ms |
| XGo | LLGoFullLTOGlobalDCE | 209336.3 ms | 206022.1 ms | 3314.2 ms | 147006.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 203368.1 ms | 200277.8 ms | 3090.3 ms | 126254.2 ms |
| Uber_zap | LLGoNoLTO | 202238.0 ms | 199634.7 ms | 2603.4 ms | 74127.0 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 200236.0 ms | 197320.6 ms | 2915.3 ms | 125437.8 ms |
| Uber_zap | LLGoDeadcodeDrop | 197708.7 ms | 194759.4 ms | 2949.3 ms | 72997.4 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 197359.2 ms | 194232.4 ms | 3126.8 ms | 123798.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 192984.5 ms | 190073.8 ms | 2910.7 ms | 115119.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 191938.8 ms | 189140.7 ms | 2798.2 ms | 113960.2 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 190184.9 ms | 187372.7 ms | 2812.2 ms | 70003.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 188504.7 ms | 185507.9 ms | 2996.7 ms | 110457.3 ms |
| K8s_workqueue | LLGoNoLTO | 187942.3 ms | 185345.1 ms | 2597.2 ms | 68598.4 ms |
| XGo | LLGoDeadcodeDrop | 126719.2 ms | 123163.0 ms | 3556.2 ms | 46193.2 ms |
| XGo | LLGoNoLTO | 126084.1 ms | 123351.1 ms | 2733.0 ms | 45457.5 ms |
| Gorm_schema | LLGoNoLTO | 105110.1 ms | 103460.8 ms | 1649.3 ms | 34326.3 ms |
| Gorm_schema | LLGoDeadcodeDrop | 104919.3 ms | 103136.4 ms | 1782.9 ms | 34440.8 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 104181.3 ms | 102457.9 ms | 1723.5 ms | 61209.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 104055.9 ms | 102278.6 ms | 1777.3 ms | 60657.5 ms |
| Toml | LLGoDeadcodeDrop | 100476.1 ms | 98455.9 ms | 2020.2 ms | 33120.7 ms |
| Toml | LLGoNoLTO | 99246.6 ms | 97449.5 ms | 1797.1 ms | 32016.7 ms |
| Toml | LLGoFullLTONoGlobalDCE | 95824.9 ms | 93944.3 ms | 1880.6 ms | 56013.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 90681.8 ms | 89087.4 ms | 1594.4 ms | 47617.9 ms |
| Toml | LLGoFullLTOGlobalDCE | 89274.5 ms | 87330.6 ms | 1943.9 ms | 47954.2 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 88058.7 ms | 86164.2 ms | 1894.5 ms | 47011.7 ms |
| IXGo | Go | 85468.4 ms | 80562.4 ms | 4906.0 ms | 23448.6 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 69473.5 ms | 68021.0 ms | 1452.5 ms | 24787.2 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 67828.2 ms | 66516.5 ms | 1311.7 ms | 41925.5 ms |
| Dustin_humanize | LLGoNoLTO | 66253.2 ms | 65058.6 ms | 1194.7 ms | 23584.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 59809.2 ms | 58528.1 ms | 1281.1 ms | 32857.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 57296.1 ms | 56029.5 ms | 1266.6 ms | 31094.9 ms |
| Etcdctl | Go | 33798.3 ms | 31693.4 ms | 2104.9 ms | 10135.7 ms |
| XGo | Go | 19563.0 ms | 18337.7 ms | 1225.3 ms | 5959.1 ms |
| Aws_restjson | Go | 8444.3 ms | 7761.5 ms | 682.8 ms | 3609.3 ms |
| Gorm_schema | Go | 5883.4 ms | 5463.3 ms | 420.1 ms | 2286.3 ms |
| Uber_zap | Go | 5312.1 ms | 4899.3 ms | 412.8 ms | 2054.9 ms |
| K8s_workqueue | Go | 4800.1 ms | 4332.8 ms | 467.4 ms | 1704.1 ms |
| Toml | Go | 2043.5 ms | 1807.8 ms | 235.7 ms | 929.4 ms |
| Dustin_humanize | Go | 842.3 ms | 703.0 ms | 139.4 ms | 403.8 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTOGlobalDCEPlugin | 2111519.3 ms | 1194175.4 ms | 9 |
| LLGoFullLTOGlobalDCE | 2097920.9 ms | 1204532.5 ms | 9 |
| LLGoFullLTONoGlobalDCE | 2082437.8 ms | 1234338.7 ms | 9 |
| LLGoNoLTO | 1842780.8 ms | 599291.0 ms | 9 |
| LLGoDeadcodeDrop | 1787728.7 ms | 595172.0 ms | 9 |
| Go | 166155.5 ms | 50531.2 ms | 9 |

Dependency download details are in `download-timings.log`.
