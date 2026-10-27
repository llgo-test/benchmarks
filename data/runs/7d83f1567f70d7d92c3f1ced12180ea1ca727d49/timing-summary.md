## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTONoGlobalDCE | 665731.7 ms | 654606.3 ms | 11125.3 ms | 337954.5 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 636948.1 ms | 626261.0 ms | 10687.0 ms | 332788.4 ms |
| IXGo | LLGoFullLTOGlobalDCE | 616165.8 ms | 605634.7 ms | 10531.1 ms | 324972.8 ms |
| IXGo | LLGoDeadcodeDrop | 484015.4 ms | 470723.5 ms | 13292.0 ms | 143362.6 ms |
| IXGo | LLGoNoLTO | 466187.9 ms | 457423.9 ms | 8764.0 ms | 134793.5 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 300792.9 ms | 295123.9 ms | 5669.0 ms | 186564.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 292684.0 ms | 287968.7 ms | 4715.3 ms | 182204.3 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 290915.6 ms | 286234.5 ms | 4681.1 ms | 182783.2 ms |
| Aws_restjson | LLGoNoLTO | 235757.1 ms | 232670.2 ms | 3086.9 ms | 80578.1 ms |
| Aws_restjson | LLGoDeadcodeDrop | 235562.0 ms | 232060.0 ms | 3502.0 ms | 81435.4 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 234142.0 ms | 230803.7 ms | 3338.3 ms | 138766.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 224132.0 ms | 220899.1 ms | 3233.0 ms | 126058.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 222835.8 ms | 219577.2 ms | 3258.7 ms | 124241.6 ms |
| Etcdctl | LLGoDeadcodeDrop | 216727.3 ms | 211300.4 ms | 5426.9 ms | 72397.1 ms |
| Etcdctl | LLGoNoLTO | 214821.9 ms | 210416.5 ms | 4405.5 ms | 69889.3 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 208663.1 ms | 205345.5 ms | 3317.6 ms | 146170.4 ms |
| XGo | LLGoFullLTONoGlobalDCE | 207367.2 ms | 203947.8 ms | 3419.4 ms | 146781.8 ms |
| XGo | LLGoFullLTOGlobalDCE | 206027.4 ms | 202714.3 ms | 3313.1 ms | 144408.8 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 200659.2 ms | 197673.0 ms | 2986.3 ms | 124559.6 ms |
| Uber_zap | LLGoNoLTO | 195018.8 ms | 192612.1 ms | 2406.7 ms | 70897.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 194229.9 ms | 191266.7 ms | 2963.3 ms | 120728.5 ms |
| Uber_zap | LLGoDeadcodeDrop | 193545.9 ms | 190766.0 ms | 2779.9 ms | 71296.8 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 192369.3 ms | 189411.1 ms | 2958.2 ms | 120757.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 188347.7 ms | 185686.6 ms | 2661.1 ms | 111695.3 ms |
| K8s_workqueue | LLGoNoLTO | 186455.3 ms | 183843.4 ms | 2611.9 ms | 68162.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 186401.0 ms | 183612.0 ms | 2789.0 ms | 110261.4 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 186296.0 ms | 183478.6 ms | 2817.4 ms | 68788.8 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 181060.7 ms | 178183.8 ms | 2876.9 ms | 105683.0 ms |
| XGo | LLGoDeadcodeDrop | 123514.6 ms | 119965.6 ms | 3549.0 ms | 45592.0 ms |
| XGo | LLGoNoLTO | 122157.1 ms | 119610.9 ms | 2546.2 ms | 43821.5 ms |
| Gorm_schema | LLGoDeadcodeDrop | 103533.5 ms | 101648.9 ms | 1884.7 ms | 33985.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 103159.2 ms | 101406.6 ms | 1752.6 ms | 59847.3 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 102929.4 ms | 101154.8 ms | 1774.6 ms | 60892.3 ms |
| Gorm_schema | LLGoNoLTO | 102585.6 ms | 101036.0 ms | 1549.6 ms | 33318.7 ms |
| Toml | LLGoDeadcodeDrop | 96520.7 ms | 94556.3 ms | 1964.5 ms | 31623.5 ms |
| Toml | LLGoNoLTO | 96196.7 ms | 94484.7 ms | 1712.0 ms | 30952.9 ms |
| Toml | LLGoFullLTONoGlobalDCE | 95192.1 ms | 93195.1 ms | 1997.0 ms | 55218.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 89711.1 ms | 87976.6 ms | 1734.5 ms | 47340.6 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 86568.4 ms | 84720.9 ms | 1847.5 ms | 46002.0 ms |
| Toml | LLGoFullLTOGlobalDCE | 85042.8 ms | 83256.9 ms | 1785.9 ms | 45286.4 ms |
| IXGo | Go | 84672.7 ms | 79546.3 ms | 5126.4 ms | 23837.0 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 66615.9 ms | 65330.4 ms | 1285.5 ms | 23737.8 ms |
| Dustin_humanize | LLGoNoLTO | 66292.9 ms | 65117.1 ms | 1175.8 ms | 23134.4 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 66032.7 ms | 64740.4 ms | 1292.3 ms | 40607.5 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 56312.5 ms | 55074.9 ms | 1237.6 ms | 30689.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 55858.4 ms | 54621.8 ms | 1236.6 ms | 30293.5 ms |
| Etcdctl | Go | 33298.0 ms | 31256.1 ms | 2041.9 ms | 10020.1 ms |
| XGo | Go | 19197.7 ms | 17998.3 ms | 1199.4 ms | 5821.7 ms |
| Aws_restjson | Go | 8155.5 ms | 7463.7 ms | 691.9 ms | 3274.8 ms |
| Gorm_schema | Go | 5741.2 ms | 5344.8 ms | 396.5 ms | 2198.3 ms |
| Uber_zap | Go | 5368.3 ms | 4937.3 ms | 431.0 ms | 2106.7 ms |
| K8s_workqueue | Go | 4651.2 ms | 4204.9 ms | 446.4 ms | 1647.0 ms |
| Toml | Go | 2082.5 ms | 1822.8 ms | 259.7 ms | 1045.7 ms |
| Dustin_humanize | Go | 820.1 ms | 690.4 ms | 129.7 ms | 381.8 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2055339.2 ms | 1208321.1 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1971240.3 ms | 1131175.2 ms | 9 |
| LLGoFullLTOGlobalDCE | 1963700.6 ms | 1144061.2 ms | 9 |
| LLGoDeadcodeDrop | 1706331.4 ms | 572220.0 ms | 9 |
| LLGoNoLTO | 1685473.3 ms | 555548.3 ms | 9 |
| Go | 163987.3 ms | 50333.1 ms | 9 |

Dependency download details are in `download-timings.log`.
