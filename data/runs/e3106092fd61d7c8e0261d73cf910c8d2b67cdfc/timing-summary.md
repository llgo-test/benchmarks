## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 468806.3 ms | 460208.1 ms | 8598.2 ms | 245485.0 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 467240.6 ms | 459092.0 ms | 8148.5 ms | 245171.9 ms |
| IXGo | LLGoFullLTOGlobalDCE | 449937.5 ms | 441320.4 ms | 8617.1 ms | 234952.0 ms |
| IXGo | LLGoDeadcodeDrop | 406112.0 ms | 396572.9 ms | 9539.1 ms | 119901.0 ms |
| IXGo | LLGoNoLTO | 337658.3 ms | 330703.2 ms | 6955.0 ms | 98669.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 237132.2 ms | 232872.5 ms | 4259.7 ms | 141333.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 230018.6 ms | 226083.3 ms | 3935.3 ms | 137875.9 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 226696.0 ms | 222859.2 ms | 3836.8 ms | 138606.9 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 183351.3 ms | 180239.5 ms | 3111.8 ms | 104655.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 182321.0 ms | 179398.3 ms | 2922.7 ms | 94040.4 ms |
| Aws_restjson | LLGoNoLTO | 179376.3 ms | 176902.3 ms | 2474.0 ms | 58316.7 ms |
| Etcdctl | LLGoNoLTO | 178658.3 ms | 174727.1 ms | 3931.2 ms | 58603.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 175266.4 ms | 172339.6 ms | 2926.8 ms | 97125.2 ms |
| Aws_restjson | LLGoDeadcodeDrop | 170310.6 ms | 167728.1 ms | 2582.5 ms | 57108.4 ms |
| XGo | LLGoFullLTOGlobalDCE | 165736.3 ms | 163062.9 ms | 2673.4 ms | 110171.8 ms |
| Etcdctl | LLGoDeadcodeDrop | 164003.0 ms | 159994.8 ms | 4008.2 ms | 55505.1 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 162794.4 ms | 160138.1 ms | 2656.2 ms | 108656.8 ms |
| XGo | LLGoFullLTONoGlobalDCE | 158009.4 ms | 155468.1 ms | 2541.3 ms | 106435.4 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 149612.5 ms | 147132.0 ms | 2480.5 ms | 89789.9 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 148787.3 ms | 146236.6 ms | 2550.7 ms | 84445.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 147632.6 ms | 144988.4 ms | 2644.2 ms | 88342.9 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 143829.7 ms | 141463.0 ms | 2366.7 ms | 51449.2 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 143421.5 ms | 140846.4 ms | 2575.1 ms | 85824.4 ms |
| Uber_zap | LLGoNoLTO | 142863.0 ms | 140671.4 ms | 2191.6 ms | 50970.6 ms |
| Uber_zap | LLGoDeadcodeDrop | 140355.8 ms | 138249.3 ms | 2106.5 ms | 49365.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 137787.1 ms | 135431.0 ms | 2356.1 ms | 78068.1 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 130052.9 ms | 127621.1 ms | 2431.8 ms | 72842.5 ms |
| K8s_workqueue | LLGoNoLTO | 129766.6 ms | 127684.0 ms | 2082.6 ms | 46348.9 ms |
| XGo | LLGoDeadcodeDrop | 101821.8 ms | 99214.9 ms | 2606.9 ms | 38115.9 ms |
| XGo | LLGoNoLTO | 97525.2 ms | 95479.2 ms | 2046.0 ms | 35496.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 71598.2 ms | 70142.3 ms | 1456.0 ms | 43627.2 ms |
| Gorm_schema | LLGoNoLTO | 66978.2 ms | 65615.3 ms | 1362.9 ms | 22526.3 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 65855.4 ms | 64445.9 ms | 1409.5 ms | 39904.6 ms |
| Gorm_schema | LLGoDeadcodeDrop | 64463.1 ms | 63188.0 ms | 1275.1 ms | 21870.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 63729.4 ms | 62272.1 ms | 1457.3 ms | 35218.6 ms |
| Toml | LLGoDeadcodeDrop | 63113.9 ms | 61719.7 ms | 1394.1 ms | 21365.6 ms |
| Toml | LLGoNoLTO | 60749.7 ms | 59421.9 ms | 1327.8 ms | 20513.5 ms |
| Toml | LLGoFullLTONoGlobalDCE | 60030.9 ms | 58611.2 ms | 1419.8 ms | 35727.6 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 59170.2 ms | 57643.5 ms | 1526.7 ms | 32540.1 ms |
| Toml | LLGoFullLTOGlobalDCE | 56717.0 ms | 55231.2 ms | 1485.8 ms | 31080.5 ms |
| IXGo | Go | 52122.2 ms | 48334.5 ms | 3787.7 ms | 14439.2 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 50030.3 ms | 48855.4 ms | 1174.9 ms | 31435.1 ms |
| Dustin_humanize | LLGoNoLTO | 48966.6 ms | 48003.4 ms | 963.2 ms | 17847.8 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 43410.3 ms | 42446.4 ms | 963.9 ms | 15801.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 41243.0 ms | 40184.7 ms | 1058.3 ms | 23416.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 36972.4 ms | 36017.8 ms | 954.6 ms | 20698.3 ms |
| Etcdctl | Go | 20779.8 ms | 19350.4 ms | 1429.4 ms | 6481.0 ms |
| XGo | Go | 12421.7 ms | 11520.5 ms | 901.2 ms | 3676.5 ms |
| Aws_restjson | Go | 5091.3 ms | 4619.6 ms | 471.7 ms | 2123.8 ms |
| Gorm_schema | Go | 3902.4 ms | 3600.9 ms | 301.5 ms | 1565.1 ms |
| Uber_zap | Go | 3240.2 ms | 2956.3 ms | 283.9 ms | 1295.6 ms |
| K8s_workqueue | Go | 2879.4 ms | 2579.7 ms | 299.7 ms | 1035.3 ms |
| Toml | Go | 1285.6 ms | 1121.3 ms | 164.4 ms | 600.1 ms |
| Dustin_humanize | Go | 526.0 ms | 431.4 ms | 94.6 ms | 256.2 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1504247.7 ms | 877551.7 ms | 9 |
| LLGoFullLTOGlobalDCE | 1485834.3 ms | 842314.8 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1479868.3 ms | 837606.5 ms | 9 |
| LLGoDeadcodeDrop | 1297420.2 ms | 430482.9 ms | 9 |
| LLGoNoLTO | 1242542.2 ms | 409292.7 ms | 9 |
| Go | 102248.7 ms | 31472.8 ms | 9 |

Dependency download details are in `download-timings.log`.
