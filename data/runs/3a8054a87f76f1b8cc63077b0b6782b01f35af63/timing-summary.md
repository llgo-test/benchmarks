## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 818605.7 ms | 806626.0 ms | 11979.7 ms | 392983.7 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 701746.9 ms | 689791.6 ms | 11955.4 ms | 357887.5 ms |
| IXGo | LLGoFullLTOGlobalDCE | 683942.9 ms | 671771.0 ms | 12171.9 ms | 350474.4 ms |
| IXGo | LLGoNoLTO | 570327.1 ms | 559577.7 ms | 10749.3 ms | 164118.4 ms |
| IXGo | LLGoDeadcodeDrop | 558180.9 ms | 542658.3 ms | 15522.7 ms | 166335.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 350560.5 ms | 344050.7 ms | 6509.8 ms | 212958.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 350444.9 ms | 344056.5 ms | 6388.4 ms | 210513.8 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 337215.8 ms | 331320.2 ms | 5895.7 ms | 205274.5 ms |
| XGo | LLGoFullLTONoGlobalDCE | 263255.1 ms | 258832.9 ms | 4422.2 ms | 178915.2 ms |
| Aws_restjson | LLGoDeadcodeDrop | 261398.6 ms | 257513.5 ms | 3885.1 ms | 89290.7 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 259956.1 ms | 255707.8 ms | 4248.3 ms | 148856.8 ms |
| Aws_restjson | LLGoNoLTO | 256684.4 ms | 252918.3 ms | 3766.1 ms | 88071.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 254307.8 ms | 249813.4 ms | 4494.3 ms | 138067.5 ms |
| Etcdctl | LLGoDeadcodeDrop | 248602.0 ms | 242510.4 ms | 6091.6 ms | 84142.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 248529.4 ms | 244369.0 ms | 4160.4 ms | 135617.9 ms |
| XGo | LLGoFullLTOGlobalDCE | 245007.8 ms | 240996.3 ms | 4011.5 ms | 164814.1 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 244540.2 ms | 240492.3 ms | 4048.0 ms | 163766.6 ms |
| Etcdctl | LLGoNoLTO | 243662.6 ms | 238462.6 ms | 5200.0 ms | 80950.4 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 225548.5 ms | 221696.0 ms | 3852.5 ms | 134395.0 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 224884.0 ms | 220942.3 ms | 3941.7 ms | 134559.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 220666.8 ms | 216801.5 ms | 3865.3 ms | 130726.0 ms |
| Uber_zap | LLGoDeadcodeDrop | 218516.3 ms | 214924.7 ms | 3591.6 ms | 78898.1 ms |
| Uber_zap | LLGoNoLTO | 216190.5 ms | 212642.8 ms | 3547.7 ms | 77992.9 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 214668.8 ms | 210956.6 ms | 3712.2 ms | 121654.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 214409.8 ms | 210669.0 ms | 3740.8 ms | 121107.3 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 209964.1 ms | 206561.3 ms | 3402.8 ms | 76088.0 ms |
| K8s_workqueue | LLGoNoLTO | 208998.2 ms | 205694.0 ms | 3304.3 ms | 75858.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 203253.3 ms | 199414.3 ms | 3839.0 ms | 113728.4 ms |
| XGo | LLGoNoLTO | 160700.2 ms | 157147.5 ms | 3552.7 ms | 58445.6 ms |
| XGo | LLGoDeadcodeDrop | 153415.9 ms | 149317.7 ms | 4098.2 ms | 57199.2 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 107221.5 ms | 104849.0 ms | 2372.6 ms | 64621.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 104819.8 ms | 102478.9 ms | 2340.9 ms | 62564.1 ms |
| Gorm_schema | LLGoDeadcodeDrop | 103512.7 ms | 101377.7 ms | 2135.0 ms | 34594.5 ms |
| Toml | LLGoFullLTONoGlobalDCE | 102583.6 ms | 100151.8 ms | 2431.8 ms | 61252.0 ms |
| Gorm_schema | LLGoNoLTO | 101910.9 ms | 99863.3 ms | 2047.6 ms | 34334.1 ms |
| Toml | LLGoDeadcodeDrop | 97981.8 ms | 95852.9 ms | 2128.9 ms | 32880.0 ms |
| Toml | LLGoNoLTO | 95352.5 ms | 93233.8 ms | 2118.7 ms | 31922.7 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 92121.2 ms | 89874.7 ms | 2246.5 ms | 49478.4 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 88121.5 ms | 85788.9 ms | 2332.6 ms | 47352.9 ms |
| Toml | LLGoFullLTOGlobalDCE | 87395.5 ms | 85141.9 ms | 2253.7 ms | 47350.9 ms |
| IXGo | Go | 84121.2 ms | 78291.1 ms | 5830.1 ms | 23933.0 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 68333.2 ms | 66717.5 ms | 1615.7 ms | 42672.6 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 67669.2 ms | 66304.2 ms | 1365.0 ms | 24694.4 ms |
| Dustin_humanize | LLGoNoLTO | 66222.3 ms | 64884.7 ms | 1337.5 ms | 23993.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 58672.1 ms | 57116.5 ms | 1555.6 ms | 32446.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 58233.5 ms | 56709.7 ms | 1523.8 ms | 32152.0 ms |
| Etcdctl | Go | 32299.0 ms | 29877.4 ms | 2421.7 ms | 10226.2 ms |
| XGo | Go | 18486.1 ms | 17147.4 ms | 1338.8 ms | 5509.8 ms |
| Aws_restjson | Go | 7840.0 ms | 7059.4 ms | 780.6 ms | 3249.1 ms |
| Gorm_schema | Go | 5562.7 ms | 5155.6 ms | 407.1 ms | 2136.9 ms |
| Uber_zap | Go | 5164.5 ms | 4716.0 ms | 448.5 ms | 2050.4 ms |
| K8s_workqueue | Go | 4724.3 ms | 4173.9 ms | 550.4 ms | 1733.2 ms |
| Toml | Go | 2068.8 ms | 1767.8 ms | 301.0 ms | 1052.1 ms |
| Dustin_humanize | Go | 814.3 ms | 669.0 ms | 145.3 ms | 395.4 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTOGlobalDCEPlugin | 2324851.2 ms | 1272437.2 ms | 9 |
| LLGoFullLTONoGlobalDCE | 2290744.7 ms | 1328434.2 ms | 9 |
| LLGoFullLTOGlobalDCE | 2213450.3 ms | 1255320.4 ms | 9 |
| LLGoNoLTO | 1920048.6 ms | 635686.9 ms | 9 |
| LLGoDeadcodeDrop | 1919241.6 ms | 644123.0 ms | 9 |
| Go | 161081.0 ms | 50286.2 ms | 9 |

Dependency download details are in `download-timings.log`.
