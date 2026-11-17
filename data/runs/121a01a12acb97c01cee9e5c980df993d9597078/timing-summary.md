## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 885922.5 ms | 859066.6 ms | 26855.9 ms | 558911.1 ms |
| IXGo | LLGoFullLTOGlobalDCE | 835225.6 ms | 809318.0 ms | 25907.6 ms | 537371.2 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 811910.8 ms | 786476.4 ms | 25434.3 ms | 527334.1 ms |
| IXGo | LLGoDeadcodeDrop | 530904.3 ms | 503674.0 ms | 27230.2 ms | 170546.7 ms |
| IXGo | LLGoNoLTO | 479919.5 ms | 457665.8 ms | 22253.7 ms | 150658.4 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 454645.8 ms | 442218.3 ms | 12427.5 ms | 328725.6 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 444213.6 ms | 432154.4 ms | 12059.3 ms | 317916.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 439103.6 ms | 426870.3 ms | 12233.3 ms | 316318.0 ms |
| XGo | LLGoFullLTONoGlobalDCE | 320250.1 ms | 311880.6 ms | 8369.4 ms | 251234.5 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 310936.0 ms | 304209.0 ms | 6727.1 ms | 208385.3 ms |
| XGo | LLGoFullLTOGlobalDCE | 287671.9 ms | 279667.5 ms | 8004.5 ms | 217343.4 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 285688.1 ms | 277395.2 ms | 8292.9 ms | 214389.3 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 281326.6 ms | 274886.8 ms | 6439.8 ms | 176437.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 277247.1 ms | 270730.5 ms | 6516.6 ms | 175290.0 ms |
| Aws_restjson | LLGoDeadcodeDrop | 264480.0 ms | 258173.5 ms | 6306.5 ms | 84098.9 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 262159.4 ms | 256274.0 ms | 5885.5 ms | 179180.6 ms |
| Aws_restjson | LLGoNoLTO | 259633.2 ms | 253681.4 ms | 5951.9 ms | 81138.9 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 251000.5 ms | 245415.7 ms | 5584.8 ms | 173744.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 248304.5 ms | 242780.3 ms | 5524.2 ms | 170582.0 ms |
| Etcdctl | LLGoNoLTO | 247714.6 ms | 238049.0 ms | 9665.6 ms | 84239.7 ms |
| Etcdctl | LLGoDeadcodeDrop | 245890.3 ms | 235072.7 ms | 10817.6 ms | 85057.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 244052.0 ms | 238440.2 ms | 5611.8 ms | 160208.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 238841.7 ms | 233396.1 ms | 5445.6 ms | 154858.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 214886.5 ms | 209669.3 ms | 5217.2 ms | 137434.0 ms |
| Uber_zap | LLGoNoLTO | 214680.8 ms | 209687.2 ms | 4993.6 ms | 68479.9 ms |
| Uber_zap | LLGoDeadcodeDrop | 213202.3 ms | 208032.1 ms | 5170.2 ms | 69274.2 ms |
| K8s_workqueue | LLGoNoLTO | 203140.4 ms | 198256.8 ms | 4883.6 ms | 64625.0 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 202351.4 ms | 197248.4 ms | 5103.0 ms | 65921.8 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 155801.6 ms | 151988.8 ms | 3812.8 ms | 107929.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 154797.6 ms | 150734.2 ms | 4063.4 ms | 104007.8 ms |
| XGo | LLGoNoLTO | 139732.7 ms | 133499.9 ms | 6232.8 ms | 51000.5 ms |
| Toml | LLGoFullLTONoGlobalDCE | 139240.4 ms | 135591.2 ms | 3649.2 ms | 93838.3 ms |
| XGo | LLGoDeadcodeDrop | 139074.1 ms | 131800.5 ms | 7273.6 ms | 50406.6 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 128747.9 ms | 125210.6 ms | 3537.3 ms | 80688.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 126978.1 ms | 123311.6 ms | 3666.5 ms | 77816.0 ms |
| Toml | LLGoFullLTOGlobalDCE | 126422.7 ms | 122999.8 ms | 3422.9 ms | 79076.6 ms |
| Gorm_schema | LLGoDeadcodeDrop | 120116.5 ms | 116452.3 ms | 3664.3 ms | 41895.8 ms |
| Gorm_schema | LLGoNoLTO | 118477.2 ms | 115334.7 ms | 3142.5 ms | 40602.4 ms |
| Toml | LLGoDeadcodeDrop | 111812.9 ms | 108642.0 ms | 3170.9 ms | 38481.7 ms |
| Toml | LLGoNoLTO | 109038.9 ms | 106086.2 ms | 2952.7 ms | 37107.6 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 99536.0 ms | 97056.3 ms | 2479.7 ms | 70390.4 ms |
| IXGo | Go | 96721.6 ms | 81721.5 ms | 15000.1 ms | 27095.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 79918.9 ms | 77662.0 ms | 2256.9 ms | 50180.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 79857.1 ms | 77511.7 ms | 2345.4 ms | 50334.1 ms |
| Dustin_humanize | LLGoNoLTO | 76375.1 ms | 74353.9 ms | 2021.2 ms | 28340.2 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 75343.8 ms | 73283.6 ms | 2060.2 ms | 28090.6 ms |
| Etcdctl | Go | 38632.1 ms | 33347.0 ms | 5285.2 ms | 11575.4 ms |
| XGo | Go | 21552.1 ms | 18564.7 ms | 2987.3 ms | 6320.3 ms |
| Aws_restjson | Go | 8989.9 ms | 7474.6 ms | 1515.3 ms | 3625.5 ms |
| Gorm_schema | Go | 6517.2 ms | 5631.0 ms | 886.2 ms | 2565.4 ms |
| Uber_zap | Go | 5894.7 ms | 5028.0 ms | 866.7 ms | 2353.4 ms |
| K8s_workqueue | Go | 5293.9 ms | 4419.7 ms | 874.2 ms | 1888.9 ms |
| Toml | Go | 2228.8 ms | 1826.9 ms | 401.8 ms | 1041.1 ms |
| Dustin_humanize | Go | 920.6 ms | 697.8 ms | 222.7 ms | 441.7 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2805480.6 ms | 1940762.7 ms | 9 |
| LLGoFullLTOGlobalDCE | 2692682.2 ms | 1810531.9 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2686523.9 ms | 1768631.0 ms | 9 |
| LLGoDeadcodeDrop | 1903175.7 ms | 633773.2 ms | 9 |
| LLGoNoLTO | 1848712.5 ms | 606192.7 ms | 9 |
| Go | 186750.8 ms | 56907.0 ms | 9 |

Dependency download details are in `download-timings.log`.
