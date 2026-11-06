## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 919880.9 ms | 893702.7 ms | 26178.1 ms | 563196.7 ms |
| IXGo | LLGoFullLTOGlobalDCE | 892712.2 ms | 866628.4 ms | 26083.7 ms | 550507.2 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 818072.0 ms | 792391.4 ms | 25680.7 ms | 520200.2 ms |
| IXGo | LLGoDeadcodeDrop | 510975.5 ms | 484077.5 ms | 26898.0 ms | 157681.7 ms |
| IXGo | LLGoNoLTO | 496320.9 ms | 474261.1 ms | 22059.9 ms | 150244.5 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 432025.4 ms | 419895.1 ms | 12130.4 ms | 312351.5 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 430269.5 ms | 418022.0 ms | 12247.5 ms | 311296.2 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 428091.8 ms | 415817.9 ms | 12273.9 ms | 311570.7 ms |
| XGo | LLGoFullLTONoGlobalDCE | 312987.4 ms | 304747.1 ms | 8240.3 ms | 248685.0 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 294348.1 ms | 287865.1 ms | 6483.0 ms | 200133.6 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 276946.5 ms | 268810.7 ms | 8135.8 ms | 210536.4 ms |
| XGo | LLGoFullLTOGlobalDCE | 273274.8 ms | 265334.4 ms | 7940.4 ms | 207941.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 270041.1 ms | 263659.9 ms | 6381.1 ms | 172677.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 269865.3 ms | 263526.3 ms | 6339.1 ms | 171977.7 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 251844.6 ms | 246351.6 ms | 5493.0 ms | 176674.1 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 238900.6 ms | 233464.3 ms | 5436.2 ms | 168161.7 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 236346.7 ms | 230916.6 ms | 5430.1 ms | 166233.1 ms |
| Etcdctl | LLGoDeadcodeDrop | 231486.4 ms | 220566.2 ms | 10920.2 ms | 78602.7 ms |
| Etcdctl | LLGoNoLTO | 228263.5 ms | 218194.7 ms | 10068.8 ms | 76955.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 227426.6 ms | 221995.2 ms | 5431.4 ms | 153147.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 220990.3 ms | 215792.7 ms | 5197.6 ms | 146475.3 ms |
| Aws_restjson | LLGoDeadcodeDrop | 213031.6 ms | 207289.7 ms | 5741.8 ms | 67248.7 ms |
| Aws_restjson | LLGoNoLTO | 212841.8 ms | 207548.1 ms | 5293.7 ms | 66528.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 207827.6 ms | 202915.8 ms | 4911.9 ms | 136082.3 ms |
| Uber_zap | LLGoNoLTO | 171772.4 ms | 167459.5 ms | 4312.9 ms | 55044.7 ms |
| Uber_zap | LLGoDeadcodeDrop | 171122.1 ms | 166550.5 ms | 4571.6 ms | 55087.4 ms |
| K8s_workqueue | LLGoNoLTO | 165403.3 ms | 161212.3 ms | 4191.0 ms | 52740.5 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 164385.2 ms | 159824.2 ms | 4561.0 ms | 53380.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 145375.5 ms | 141419.6 ms | 3955.8 ms | 99898.6 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 144759.3 ms | 140858.4 ms | 3900.8 ms | 100764.5 ms |
| Toml | LLGoFullLTONoGlobalDCE | 134644.6 ms | 130933.9 ms | 3710.7 ms | 93313.7 ms |
| XGo | LLGoNoLTO | 127289.0 ms | 120976.5 ms | 6312.5 ms | 45476.3 ms |
| XGo | LLGoDeadcodeDrop | 125501.3 ms | 118173.0 ms | 7328.3 ms | 44415.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 124125.7 ms | 120445.5 ms | 3680.2 ms | 78193.1 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 120475.9 ms | 117043.5 ms | 3432.4 ms | 77241.6 ms |
| Toml | LLGoFullLTOGlobalDCE | 115400.9 ms | 112097.3 ms | 3303.6 ms | 73764.5 ms |
| Gorm_schema | LLGoNoLTO | 108090.0 ms | 104970.1 ms | 3119.9 ms | 36833.4 ms |
| Gorm_schema | LLGoDeadcodeDrop | 107715.1 ms | 104179.3 ms | 3535.8 ms | 37126.6 ms |
| Toml | LLGoDeadcodeDrop | 100014.4 ms | 96979.8 ms | 3034.6 ms | 33916.8 ms |
| Toml | LLGoNoLTO | 99977.8 ms | 97111.1 ms | 2866.7 ms | 33715.1 ms |
| IXGo | Go | 99335.0 ms | 84183.5 ms | 15151.4 ms | 26992.1 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 94627.4 ms | 92111.7 ms | 2515.7 ms | 67839.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 76261.7 ms | 74012.3 ms | 2249.4 ms | 49289.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 75520.9 ms | 73294.9 ms | 2226.1 ms | 48590.4 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 70235.2 ms | 68059.8 ms | 2175.4 ms | 25775.4 ms |
| Dustin_humanize | LLGoNoLTO | 69623.8 ms | 67632.7 ms | 1991.1 ms | 25388.8 ms |
| Etcdctl | Go | 38272.5 ms | 32927.9 ms | 5344.5 ms | 11500.6 ms |
| XGo | Go | 21943.5 ms | 18802.8 ms | 3140.7 ms | 6486.1 ms |
| Aws_restjson | Go | 9356.5 ms | 7776.0 ms | 1580.5 ms | 3872.3 ms |
| Gorm_schema | Go | 6616.3 ms | 5658.5 ms | 957.9 ms | 2567.3 ms |
| Uber_zap | Go | 6215.4 ms | 5236.3 ms | 979.1 ms | 2590.8 ms |
| K8s_workqueue | Go | 5573.9 ms | 4593.8 ms | 980.1 ms | 2256.8 ms |
| Toml | Go | 2287.7 ms | 1897.5 ms | 390.2 ms | 1140.0 ms |
| Dustin_humanize | Go | 906.0 ms | 678.0 ms | 228.0 ms | 456.8 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2715721.9 ms | 1885414.2 ms | 9 |
| LLGoFullLTOGlobalDCE | 2671418.8 ms | 1787739.6 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2645902.8 ms | 1743589.7 ms | 9 |
| LLGoDeadcodeDrop | 1694466.7 ms | 553235.0 ms | 9 |
| LLGoNoLTO | 1679582.5 ms | 542926.5 ms | 9 |
| Go | 190506.9 ms | 57862.9 ms | 9 |

Dependency download details are in `download-timings.log`.
