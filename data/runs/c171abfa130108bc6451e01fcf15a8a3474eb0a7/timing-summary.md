## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 896662.9 ms | 883998.0 ms | 12665.0 ms | 560822.2 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 881436.6 ms | 868239.5 ms | 13197.1 ms | 566698.4 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 869407.3 ms | 856725.5 ms | 12681.8 ms | 561491.1 ms |
| IXGo | LLGoNoLTO | 632992.7 ms | 622898.8 ms | 10093.9 ms | 187838.6 ms |
| IXGo | LLGoDeadcodeDrop | 522165.0 ms | 507519.7 ms | 14645.3 ms | 164867.7 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 451892.0 ms | 445579.7 ms | 6312.3 ms | 334799.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 449267.1 ms | 441796.6 ms | 7470.4 ms | 329746.5 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 436131.0 ms | 430085.3 ms | 6045.7 ms | 319815.9 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 346315.2 ms | 341974.8 ms | 4340.4 ms | 239533.9 ms |
| XGo | LLGoFullLTONoGlobalDCE | 340421.7 ms | 335887.3 ms | 4534.4 ms | 275288.3 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 300212.9 ms | 296306.6 ms | 3906.3 ms | 200118.5 ms |
| XGo | LLGoFullLTOGlobalDCE | 293425.2 ms | 289273.1 ms | 4152.1 ms | 228578.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 292316.9 ms | 288489.9 ms | 3827.0 ms | 193454.6 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 290860.2 ms | 286655.9 ms | 4204.4 ms | 225824.4 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 276552.6 ms | 272708.6 ms | 3844.0 ms | 202586.5 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 274223.3 ms | 270632.3 ms | 3591.0 ms | 198065.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 265650.0 ms | 262005.4 ms | 3644.5 ms | 192105.8 ms |
| Aws_restjson | LLGoDeadcodeDrop | 254194.1 ms | 250578.0 ms | 3616.1 ms | 88764.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 253456.6 ms | 249915.3 ms | 3541.3 ms | 174836.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 251115.1 ms | 247710.2 ms | 3404.9 ms | 173638.3 ms |
| Aws_restjson | LLGoNoLTO | 239748.0 ms | 236603.5 ms | 3144.6 ms | 83641.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 235138.6 ms | 231667.7 ms | 3470.9 ms | 160391.7 ms |
| Etcdctl | LLGoNoLTO | 230000.8 ms | 225121.3 ms | 4879.4 ms | 80963.0 ms |
| Etcdctl | LLGoDeadcodeDrop | 228785.6 ms | 222994.1 ms | 5791.5 ms | 82126.4 ms |
| Uber_zap | LLGoDeadcodeDrop | 202259.1 ms | 199238.0 ms | 3021.1 ms | 75772.1 ms |
| Uber_zap | LLGoNoLTO | 200668.5 ms | 197952.4 ms | 2716.1 ms | 75106.5 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 200383.3 ms | 197113.1 ms | 3270.2 ms | 75830.6 ms |
| K8s_workqueue | LLGoNoLTO | 195026.9 ms | 192249.0 ms | 2777.9 ms | 72700.0 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 143675.5 ms | 141369.6 ms | 2305.9 ms | 101496.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 141787.9 ms | 139513.8 ms | 2274.1 ms | 99186.0 ms |
| Toml | LLGoFullLTONoGlobalDCE | 135172.4 ms | 132745.7 ms | 2426.7 ms | 94643.2 ms |
| XGo | LLGoNoLTO | 130268.3 ms | 127335.9 ms | 2932.4 ms | 50607.8 ms |
| XGo | LLGoDeadcodeDrop | 129571.9 ms | 125860.9 ms | 3711.0 ms | 49559.9 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 118154.8 ms | 115810.8 ms | 2344.0 ms | 76642.1 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 117772.7 ms | 115767.9 ms | 2004.8 ms | 74334.4 ms |
| Toml | LLGoFullLTOGlobalDCE | 112034.0 ms | 109806.9 ms | 2227.1 ms | 71986.4 ms |
| Gorm_schema | LLGoDeadcodeDrop | 107860.1 ms | 105795.3 ms | 2064.9 ms | 36609.3 ms |
| Toml | LLGoDeadcodeDrop | 104425.9 ms | 102187.3 ms | 2238.6 ms | 35181.2 ms |
| Gorm_schema | LLGoNoLTO | 103701.7 ms | 101928.3 ms | 1773.4 ms | 34724.3 ms |
| Toml | LLGoNoLTO | 99685.6 ms | 97810.0 ms | 1875.6 ms | 32856.7 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 94281.1 ms | 92593.1 ms | 1688.0 ms | 68828.7 ms |
| IXGo | Go | 85746.5 ms | 80438.3 ms | 5308.1 ms | 23573.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 75672.7 ms | 74086.5 ms | 1586.3 ms | 49045.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 73664.4 ms | 72078.9 ms | 1585.4 ms | 47535.7 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 67779.2 ms | 66296.9 ms | 1482.3 ms | 24581.4 ms |
| Dustin_humanize | LLGoNoLTO | 67711.0 ms | 66393.2 ms | 1317.8 ms | 24639.0 ms |
| Etcdctl | Go | 34651.2 ms | 32576.8 ms | 2074.5 ms | 10409.1 ms |
| XGo | Go | 19258.0 ms | 18053.2 ms | 1204.8 ms | 5772.4 ms |
| Aws_restjson | Go | 8300.3 ms | 7498.2 ms | 802.1 ms | 3709.6 ms |
| Gorm_schema | Go | 5810.1 ms | 5395.6 ms | 414.5 ms | 2221.4 ms |
| Uber_zap | Go | 5340.5 ms | 4913.5 ms | 426.9 ms | 2069.0 ms |
| K8s_workqueue | Go | 4689.2 ms | 4236.6 ms | 452.6 ms | 1663.9 ms |
| Toml | Go | 2134.2 ms | 1857.0 ms | 277.2 ms | 1109.4 ms |
| Dustin_humanize | Go | 827.2 ms | 667.3 ms | 159.8 ms | 387.9 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2943970.5 ms | 2081940.7 ms | 9 |
| LLGoFullLTOGlobalDCE | 2764795.8 ms | 1888633.0 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2707934.5 ms | 1850921.0 ms | 9 |
| LLGoNoLTO | 1899803.5 ms | 643077.6 ms | 9 |
| LLGoDeadcodeDrop | 1817424.3 ms | 633292.7 ms | 9 |
| Go | 166757.1 ms | 50916.1 ms | 9 |

Dependency download details are in `download-timings.log`.
