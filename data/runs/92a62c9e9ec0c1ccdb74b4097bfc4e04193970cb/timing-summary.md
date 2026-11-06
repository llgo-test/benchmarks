## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| Etcdctl | LLGoFullLTONoGlobalDCE | 369666.2 ms | 358301.1 ms | 11365.1 ms | 268377.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 365415.8 ms | 353930.0 ms | 11485.8 ms | 269894.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 350831.6 ms | 339407.5 ms | 11424.1 ms | 259457.3 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 264968.7 ms | 258238.1 ms | 6730.6 ms | 176851.1 ms |
| XGo | LLGoFullLTONoGlobalDCE | 261756.5 ms | 254057.6 ms | 7698.9 ms | 212358.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 253999.4 ms | 247238.1 ms | 6761.3 ms | 161416.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 244556.2 ms | 237972.7 ms | 6583.6 ms | 157907.1 ms |
| XGo | LLGoFullLTOGlobalDCE | 233139.2 ms | 225700.0 ms | 7439.1 ms | 181578.8 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 231885.3 ms | 224356.7 ms | 7528.6 ms | 180675.4 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 217557.9 ms | 211651.8 ms | 5906.1 ms | 152121.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 212038.2 ms | 206129.8 ms | 5908.5 ms | 150047.1 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 208654.6 ms | 202652.8 ms | 6001.8 ms | 147232.9 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 204873.8 ms | 199112.9 ms | 5760.9 ms | 137359.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 204245.7 ms | 198554.4 ms | 5691.3 ms | 137885.0 ms |
| Aws_restjson | LLGoNoLTO | 199427.6 ms | 193922.8 ms | 5504.8 ms | 61967.2 ms |
| Etcdctl | LLGoDeadcodeDrop | 192658.9 ms | 183208.4 ms | 9450.5 ms | 65552.8 ms |
| Etcdctl | LLGoNoLTO | 191548.1 ms | 182744.5 ms | 8803.6 ms | 64284.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 188286.8 ms | 182782.1 ms | 5504.7 ms | 125636.3 ms |
| Aws_restjson | LLGoDeadcodeDrop | 186195.5 ms | 180474.3 ms | 5721.2 ms | 59601.8 ms |
| Uber_zap | LLGoDeadcodeDrop | 154985.2 ms | 150172.2 ms | 4813.1 ms | 50901.5 ms |
| Uber_zap | LLGoNoLTO | 152027.8 ms | 147536.2 ms | 4491.5 ms | 48524.0 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 143539.4 ms | 138880.8 ms | 4658.6 ms | 47507.4 ms |
| K8s_workqueue | LLGoNoLTO | 142767.6 ms | 138261.3 ms | 4506.2 ms | 45745.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 120120.7 ms | 116466.8 ms | 3654.0 ms | 83507.3 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 119611.6 ms | 115860.6 ms | 3750.9 ms | 84087.2 ms |
| Toml | LLGoFullLTONoGlobalDCE | 107007.1 ms | 103641.8 ms | 3365.3 ms | 74737.1 ms |
| XGo | LLGoNoLTO | 97193.5 ms | 91773.8 ms | 5419.7 ms | 35531.1 ms |
| XGo | LLGoDeadcodeDrop | 96674.8 ms | 90344.7 ms | 6330.1 ms | 35206.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 95360.0 ms | 91923.6 ms | 3436.4 ms | 60819.3 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 94091.8 ms | 90746.3 ms | 3345.5 ms | 60898.4 ms |
| Toml | LLGoFullLTOGlobalDCE | 93693.3 ms | 90346.4 ms | 3346.9 ms | 60958.6 ms |
| Gorm_schema | LLGoNoLTO | 83812.9 ms | 80751.5 ms | 3061.4 ms | 29107.0 ms |
| Gorm_schema | LLGoDeadcodeDrop | 82260.4 ms | 79073.9 ms | 3186.5 ms | 29033.7 ms |
| Toml | LLGoDeadcodeDrop | 78435.6 ms | 75558.9 ms | 2876.7 ms | 27492.6 ms |
| Toml | LLGoNoLTO | 75478.3 ms | 72784.2 ms | 2694.0 ms | 26074.2 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 74797.8 ms | 72499.8 ms | 2298.0 ms | 53629.7 ms |
| IXGo | Go | 72977.4 ms | 60109.7 ms | 12867.7 ms | 20114.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 62498.1 ms | 60169.6 ms | 2328.5 ms | 40663.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 59673.1 ms | 57526.1 ms | 2147.0 ms | 38535.3 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 53362.3 ms | 51409.1 ms | 1953.2 ms | 20097.7 ms |
| Dustin_humanize | LLGoNoLTO | 52843.5 ms | 50939.7 ms | 1903.8 ms | 19746.2 ms |
| Etcdctl | Go | 29342.0 ms | 24658.4 ms | 4683.6 ms | 8907.7 ms |
| XGo | Go | 16457.0 ms | 13759.5 ms | 2697.5 ms | 4881.5 ms |
| Aws_restjson | Go | 6990.7 ms | 5651.3 ms | 1339.4 ms | 3014.7 ms |
| Gorm_schema | Go | 4941.8 ms | 4101.7 ms | 840.0 ms | 1957.1 ms |
| Uber_zap | Go | 4650.1 ms | 3837.6 ms | 812.5 ms | 1922.4 ms |
| K8s_workqueue | Go | 4056.7 ms | 3250.8 ms | 805.9 ms | 1477.3 ms |
| Toml | Go | 1759.9 ms | 1442.2 ms | 317.7 ms | 947.6 ms |
| Dustin_humanize | Go | 709.8 ms | 538.8 ms | 170.9 ms | 363.5 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1624020.5 ms | 1169396.1 ms | 8 |
| LLGoFullLTOGlobalDCE | 1521123.1 ms | 1072004.4 ms | 8 |
| LLGoFullLTOGlobalDCEPlugin | 1493585.9 ms | 1035233.8 ms | 8 |
| LLGoNoLTO | 995099.2 ms | 330979.6 ms | 8 |
| LLGoDeadcodeDrop | 988112.1 ms | 335393.5 ms | 8 |
| Go | 141885.4 ms | 43585.8 ms | 9 |

Dependency download details are in `download-timings.log`.
