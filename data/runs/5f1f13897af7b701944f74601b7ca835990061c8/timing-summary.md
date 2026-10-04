## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 790654.9 ms | 780075.5 ms | 10579.4 ms | 380071.6 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 722300.1 ms | 711065.5 ms | 11234.6 ms | 355940.7 ms |
| IXGo | LLGoFullLTOGlobalDCE | 660960.5 ms | 649884.9 ms | 11075.7 ms | 341287.6 ms |
| IXGo | LLGoDeadcodeDrop | 634359.6 ms | 620757.3 ms | 13602.3 ms | 185328.3 ms |
| IXGo | LLGoNoLTO | 518212.5 ms | 509256.7 ms | 8955.8 ms | 151068.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 350242.9 ms | 344342.8 ms | 5900.1 ms | 205973.5 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 345242.8 ms | 340155.0 ms | 5087.8 ms | 201505.7 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 344788.1 ms | 339617.2 ms | 5170.9 ms | 204140.4 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 279443.7 ms | 275331.4 ms | 4112.2 ms | 156274.6 ms |
| Aws_restjson | LLGoDeadcodeDrop | 274403.0 ms | 270844.7 ms | 3558.3 ms | 91555.2 ms |
| Aws_restjson | LLGoNoLTO | 271185.5 ms | 267855.6 ms | 3330.0 ms | 90477.8 ms |
| Etcdctl | LLGoDeadcodeDrop | 261333.9 ms | 255911.2 ms | 5422.7 ms | 86684.4 ms |
| Etcdctl | LLGoNoLTO | 261230.0 ms | 256795.6 ms | 4434.5 ms | 85437.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 260012.1 ms | 256213.1 ms | 3799.0 ms | 137615.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 258320.4 ms | 254300.4 ms | 4020.0 ms | 136309.2 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 248852.8 ms | 245403.1 ms | 3449.7 ms | 162781.8 ms |
| XGo | LLGoFullLTONoGlobalDCE | 246256.4 ms | 242980.3 ms | 3276.1 ms | 162908.8 ms |
| XGo | LLGoFullLTOGlobalDCE | 245511.2 ms | 242147.6 ms | 3363.6 ms | 160706.0 ms |
| Uber_zap | LLGoDeadcodeDrop | 234199.7 ms | 231238.4 ms | 2961.3 ms | 82213.5 ms |
| Uber_zap | LLGoNoLTO | 232886.2 ms | 230037.4 ms | 2848.8 ms | 81744.9 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 232166.9 ms | 228762.2 ms | 3404.7 ms | 133556.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 229017.3 ms | 225572.4 ms | 3444.9 ms | 130797.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 227044.8 ms | 223655.7 ms | 3389.0 ms | 124279.9 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 226972.1 ms | 223627.1 ms | 3345.0 ms | 130628.8 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 225462.3 ms | 222588.9 ms | 2873.4 ms | 79602.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 225342.7 ms | 221826.7 ms | 3516.0 ms | 122604.1 ms |
| K8s_workqueue | LLGoNoLTO | 222506.5 ms | 219331.3 ms | 3175.2 ms | 78653.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 216957.0 ms | 213557.0 ms | 3400.0 ms | 117298.0 ms |
| XGo | LLGoDeadcodeDrop | 162275.2 ms | 158673.8 ms | 3601.4 ms | 59503.3 ms |
| XGo | LLGoNoLTO | 161471.7 ms | 158713.5 ms | 2758.2 ms | 58022.3 ms |
| Gorm_schema | LLGoDeadcodeDrop | 110276.8 ms | 108470.8 ms | 1806.0 ms | 36550.7 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 109901.3 ms | 107869.2 ms | 2032.1 ms | 64263.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 108738.8 ms | 106669.7 ms | 2069.1 ms | 62806.8 ms |
| Gorm_schema | LLGoNoLTO | 108223.5 ms | 106542.7 ms | 1680.8 ms | 35684.1 ms |
| Toml | LLGoDeadcodeDrop | 103488.9 ms | 101688.8 ms | 1800.0 ms | 34013.2 ms |
| Toml | LLGoNoLTO | 101753.6 ms | 99960.6 ms | 1793.0 ms | 33570.4 ms |
| Toml | LLGoFullLTONoGlobalDCE | 99274.4 ms | 97274.4 ms | 2000.1 ms | 57182.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 96765.2 ms | 94661.0 ms | 2104.2 ms | 50475.4 ms |
| Toml | LLGoFullLTOGlobalDCE | 93519.2 ms | 91501.9 ms | 2017.4 ms | 49210.4 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 90970.3 ms | 88933.6 ms | 2036.8 ms | 47952.5 ms |
| IXGo | Go | 86984.1 ms | 81731.6 ms | 5252.5 ms | 23846.6 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 72828.7 ms | 71566.6 ms | 1262.0 ms | 25938.8 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 71360.8 ms | 69902.3 ms | 1458.5 ms | 43076.6 ms |
| Dustin_humanize | LLGoNoLTO | 70969.8 ms | 69738.2 ms | 1231.6 ms | 25324.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 62083.2 ms | 60629.1 ms | 1454.1 ms | 33362.9 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 61669.4 ms | 60304.5 ms | 1364.9 ms | 33009.7 ms |
| Etcdctl | Go | 33905.4 ms | 31879.1 ms | 2026.3 ms | 10314.6 ms |
| XGo | Go | 19677.9 ms | 18468.5 ms | 1209.3 ms | 5772.7 ms |
| Aws_restjson | Go | 7949.0 ms | 7252.4 ms | 696.6 ms | 3203.7 ms |
| Gorm_schema | Go | 5809.9 ms | 5449.0 ms | 360.9 ms | 2207.6 ms |
| Uber_zap | Go | 5366.7 ms | 4955.5 ms | 411.2 ms | 2108.0 ms |
| K8s_workqueue | Go | 4903.9 ms | 4387.2 ms | 516.7 ms | 1976.7 ms |
| Toml | Go | 2064.2 ms | 1822.3 ms | 241.9 ms | 948.9 ms |
| Dustin_humanize | Go | 825.4 ms | 670.5 ms | 154.9 ms | 384.9 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTOGlobalDCEPlugin | 2340189.3 ms | 1256828.9 ms | 9 |
| LLGoFullLTONoGlobalDCE | 2332463.9 ms | 1307973.2 ms | 9 |
| LLGoFullLTOGlobalDCE | 2231716.1 ms | 1241218.4 ms | 9 |
| LLGoDeadcodeDrop | 2078628.0 ms | 681390.1 ms | 9 |
| LLGoNoLTO | 1948439.4 ms | 639984.3 ms | 9 |
| Go | 167486.5 ms | 50763.8 ms | 9 |

Dependency download details are in `download-timings.log`.
