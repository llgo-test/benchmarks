## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTONoGlobalDCE | 616934.2 ms | 597797.3 ms | 19136.8 ms | 383399.2 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 586058.9 ms | 566602.2 ms | 19456.7 ms | 378496.0 ms |
| IXGo | LLGoFullLTOGlobalDCE | 546112.3 ms | 528266.9 ms | 17845.5 ms | 362526.5 ms |
| IXGo | LLGoDeadcodeDrop | 350041.6 ms | 331222.9 ms | 18818.7 ms | 113591.0 ms |
| IXGo | LLGoNoLTO | 309184.1 ms | 293611.7 ms | 15572.5 ms | 97590.5 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 296811.2 ms | 288370.2 ms | 8441.0 ms | 219622.1 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 287521.4 ms | 278847.4 ms | 8674.0 ms | 214962.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 284968.6 ms | 276662.4 ms | 8306.2 ms | 210923.4 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 217499.9 ms | 212388.6 ms | 5111.4 ms | 146371.9 ms |
| XGo | LLGoFullLTONoGlobalDCE | 216144.7 ms | 210124.5 ms | 6020.2 ms | 172866.9 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 202588.9 ms | 196859.6 ms | 5729.2 ms | 158228.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 200659.7 ms | 195869.2 ms | 4790.5 ms | 128155.6 ms |
| XGo | LLGoFullLTOGlobalDCE | 191126.1 ms | 185349.7 ms | 5776.4 ms | 147303.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 191050.1 ms | 186108.4 ms | 4941.8 ms | 121808.4 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 166430.6 ms | 162295.8 ms | 4134.8 ms | 119480.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 165534.4 ms | 161393.0 ms | 4141.4 ms | 113060.9 ms |
| Aws_restjson | LLGoDeadcodeDrop | 165517.6 ms | 160891.0 ms | 4626.6 ms | 54338.8 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 165501.5 ms | 161358.3 ms | 4143.2 ms | 119551.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 159581.5 ms | 155595.6 ms | 3986.0 ms | 115272.5 ms |
| Etcdctl | LLGoNoLTO | 158146.8 ms | 151067.1 ms | 7079.7 ms | 54901.2 ms |
| Etcdctl | LLGoDeadcodeDrop | 155689.5 ms | 148364.8 ms | 7324.8 ms | 55469.6 ms |
| Aws_restjson | LLGoNoLTO | 151015.5 ms | 146940.7 ms | 4074.7 ms | 48157.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 150026.1 ms | 146027.8 ms | 3998.3 ms | 101837.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 140762.9 ms | 136817.3 ms | 3945.6 ms | 93623.4 ms |
| Uber_zap | LLGoNoLTO | 133552.4 ms | 129976.2 ms | 3576.2 ms | 43295.8 ms |
| Uber_zap | LLGoDeadcodeDrop | 128058.5 ms | 124410.7 ms | 3647.8 ms | 42789.3 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 122297.7 ms | 118653.7 ms | 3644.0 ms | 41174.5 ms |
| K8s_workqueue | LLGoNoLTO | 121004.5 ms | 117623.9 ms | 3380.6 ms | 39358.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 97577.1 ms | 94715.5 ms | 2861.6 ms | 68019.7 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 96968.0 ms | 94201.6 ms | 2766.5 ms | 68612.2 ms |
| Toml | LLGoFullLTONoGlobalDCE | 88885.4 ms | 86260.3 ms | 2625.0 ms | 62494.3 ms |
| XGo | LLGoDeadcodeDrop | 87128.1 ms | 82207.9 ms | 4920.2 ms | 32669.2 ms |
| XGo | LLGoNoLTO | 86045.4 ms | 81758.8 ms | 4286.6 ms | 32174.4 ms |
| Toml | LLGoFullLTOGlobalDCE | 83896.0 ms | 81271.7 ms | 2624.3 ms | 55240.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 80773.8 ms | 78072.2 ms | 2701.6 ms | 51329.4 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 78534.1 ms | 76065.9 ms | 2468.2 ms | 51783.8 ms |
| Gorm_schema | LLGoDeadcodeDrop | 70828.8 ms | 68309.9 ms | 2519.0 ms | 25226.3 ms |
| Gorm_schema | LLGoNoLTO | 69881.0 ms | 67674.0 ms | 2206.9 ms | 24536.2 ms |
| Toml | LLGoDeadcodeDrop | 67369.0 ms | 65157.2 ms | 2211.8 ms | 23875.0 ms |
| Toml | LLGoNoLTO | 65859.2 ms | 63779.4 ms | 2079.8 ms | 23012.4 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 65304.8 ms | 63448.9 ms | 1855.9 ms | 47660.0 ms |
| IXGo | Go | 60715.6 ms | 50476.8 ms | 10238.8 ms | 16815.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 54782.9 ms | 53041.1 ms | 1741.9 ms | 36536.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 52343.1 ms | 50612.0 ms | 1731.2 ms | 34532.7 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 50283.7 ms | 48612.9 ms | 1670.8 ms | 19543.5 ms |
| Dustin_humanize | LLGoNoLTO | 46676.8 ms | 45226.4 ms | 1450.4 ms | 17591.6 ms |
| Etcdctl | Go | 24514.2 ms | 20793.6 ms | 3720.6 ms | 7462.8 ms |
| XGo | Go | 14222.5 ms | 12102.6 ms | 2119.9 ms | 4279.5 ms |
| Aws_restjson | Go | 5568.5 ms | 4528.4 ms | 1040.1 ms | 2352.4 ms |
| Gorm_schema | Go | 3953.4 ms | 3281.5 ms | 671.9 ms | 1566.0 ms |
| Uber_zap | Go | 3638.6 ms | 3037.2 ms | 601.4 ms | 1513.9 ms |
| K8s_workqueue | Go | 3450.9 ms | 2844.5 ms | 606.4 ms | 1259.8 ms |
| Toml | Go | 1409.4 ms | 1162.5 ms | 246.8 ms | 690.9 ms |
| Dustin_humanize | Go | 588.5 ms | 441.8 ms | 146.7 ms | 297.1 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1921190.5 ms | 1335399.1 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1788558.8 ms | 1217608.2 ms | 9 |
| LLGoFullLTOGlobalDCE | 1774629.2 ms | 1230691.0 ms | 9 |
| LLGoDeadcodeDrop | 1197214.6 ms | 408677.1 ms | 9 |
| LLGoNoLTO | 1141365.7 ms | 380618.4 ms | 9 |
| Go | 118061.6 ms | 36237.6 ms | 9 |

Dependency download details are in `download-timings.log`.
