## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 728123.4 ms | 716353.2 ms | 11770.2 ms | 365850.0 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 715911.7 ms | 705324.8 ms | 10586.9 ms | 364174.7 ms |
| IXGo | LLGoDeadcodeDrop | 696612.5 ms | 682215.3 ms | 14397.2 ms | 201747.2 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 691596.2 ms | 680367.7 ms | 11228.5 ms | 358205.3 ms |
| IXGo | LLGoNoLTO | 517110.6 ms | 507844.3 ms | 9266.3 ms | 152311.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 386910.2 ms | 381232.7 ms | 5677.5 ms | 238542.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 359771.7 ms | 354475.6 ms | 5296.1 ms | 212028.4 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 352013.0 ms | 346622.4 ms | 5390.6 ms | 207070.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 314833.8 ms | 309934.3 ms | 4899.5 ms | 160648.2 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 287958.2 ms | 283717.8 ms | 4240.4 ms | 160496.5 ms |
| Aws_restjson | LLGoDeadcodeDrop | 278931.1 ms | 275604.5 ms | 3326.6 ms | 93030.9 ms |
| Etcdctl | LLGoNoLTO | 273104.6 ms | 268293.1 ms | 4811.5 ms | 89441.9 ms |
| XGo | LLGoFullLTOGlobalDCE | 271480.4 ms | 267511.6 ms | 3968.8 ms | 176083.0 ms |
| Etcdctl | LLGoDeadcodeDrop | 270477.4 ms | 264865.2 ms | 5612.2 ms | 89378.0 ms |
| Aws_restjson | LLGoNoLTO | 268773.4 ms | 265478.5 ms | 3294.9 ms | 90062.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 262383.7 ms | 258605.3 ms | 3778.4 ms | 138681.4 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 249928.4 ms | 246409.8 ms | 3518.6 ms | 162189.0 ms |
| XGo | LLGoFullLTONoGlobalDCE | 248739.5 ms | 245266.5 ms | 3473.0 ms | 163846.8 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 242564.3 ms | 238893.5 ms | 3670.8 ms | 139435.2 ms |
| Uber_zap | LLGoDeadcodeDrop | 242457.6 ms | 239408.6 ms | 3048.9 ms | 85594.5 ms |
| K8s_workqueue | LLGoNoLTO | 239087.4 ms | 235705.9 ms | 3381.5 ms | 84340.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 236873.3 ms | 233360.7 ms | 3512.7 ms | 131347.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 234056.4 ms | 230337.8 ms | 3718.6 ms | 133652.8 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 233910.8 ms | 230386.7 ms | 3524.1 ms | 134800.1 ms |
| Uber_zap | LLGoNoLTO | 232579.2 ms | 229775.8 ms | 2803.4 ms | 81956.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 230637.1 ms | 227126.0 ms | 3511.1 ms | 125797.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 229616.5 ms | 225851.9 ms | 3764.7 ms | 124912.4 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 227790.8 ms | 224712.1 ms | 3078.7 ms | 80125.2 ms |
| XGo | LLGoDeadcodeDrop | 164594.8 ms | 160845.8 ms | 3749.0 ms | 60351.0 ms |
| XGo | LLGoNoLTO | 164017.0 ms | 161307.2 ms | 2709.8 ms | 58904.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 114402.3 ms | 112172.1 ms | 2230.2 ms | 66386.0 ms |
| Toml | LLGoDeadcodeDrop | 112252.3 ms | 110190.8 ms | 2061.4 ms | 37347.4 ms |
| Gorm_schema | LLGoDeadcodeDrop | 112249.4 ms | 110426.2 ms | 1823.3 ms | 37155.1 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 112074.5 ms | 109840.6 ms | 2233.9 ms | 65630.9 ms |
| Gorm_schema | LLGoNoLTO | 110339.6 ms | 108444.6 ms | 1895.0 ms | 36734.3 ms |
| Toml | LLGoNoLTO | 103355.2 ms | 101483.7 ms | 1871.4 ms | 34190.2 ms |
| Toml | LLGoFullLTONoGlobalDCE | 102173.9 ms | 99978.6 ms | 2195.3 ms | 58813.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 99518.8 ms | 97423.2 ms | 2095.6 ms | 52176.1 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 95265.4 ms | 93097.5 ms | 2167.9 ms | 49716.3 ms |
| Toml | LLGoFullLTOGlobalDCE | 92613.7 ms | 90550.1 ms | 2063.6 ms | 48852.5 ms |
| IXGo | Go | 90799.1 ms | 84957.2 ms | 5841.9 ms | 25187.9 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 73691.1 ms | 72442.6 ms | 1248.5 ms | 26286.0 ms |
| Dustin_humanize | LLGoNoLTO | 73432.1 ms | 72122.0 ms | 1310.1 ms | 26385.5 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 73143.7 ms | 71643.5 ms | 1500.2 ms | 44232.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 63925.2 ms | 62492.8 ms | 1432.4 ms | 34621.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 61531.1 ms | 60228.6 ms | 1302.6 ms | 33001.0 ms |
| Etcdctl | Go | 37229.8 ms | 34931.0 ms | 2298.8 ms | 11244.1 ms |
| XGo | Go | 20646.2 ms | 19337.1 ms | 1309.1 ms | 6172.5 ms |
| Aws_restjson | Go | 9056.8 ms | 8133.5 ms | 923.3 ms | 4095.4 ms |
| Gorm_schema | Go | 5911.3 ms | 5494.4 ms | 416.8 ms | 2265.7 ms |
| Uber_zap | Go | 5639.2 ms | 5211.4 ms | 427.7 ms | 2198.6 ms |
| K8s_workqueue | Go | 4905.9 ms | 4405.2 ms | 500.7 ms | 1745.0 ms |
| Toml | Go | 2094.9 ms | 1868.2 ms | 226.7 ms | 951.8 ms |
| Dustin_humanize | Go | 828.0 ms | 678.5 ms | 149.5 ms | 394.0 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTOGlobalDCEPlugin | 2384153.1 ms | 1311157.8 ms | 9 |
| LLGoFullLTOGlobalDCE | 2363630.2 ms | 1307502.3 ms | 9 |
| LLGoFullLTONoGlobalDCE | 2344174.0 ms | 1332531.2 ms | 9 |
| LLGoDeadcodeDrop | 2179056.9 ms | 711015.4 ms | 9 |
| LLGoNoLTO | 1981799.2 ms | 654326.5 ms | 9 |
| Go | 177111.2 ms | 54254.9 ms | 9 |

Dependency download details are in `download-timings.log`.
