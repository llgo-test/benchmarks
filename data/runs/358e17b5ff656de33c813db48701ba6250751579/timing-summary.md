## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTONoGlobalDCE | 563739.9 ms | 553607.5 ms | 10132.4 ms | 286848.2 ms |
| IXGo | LLGoFullLTOGlobalDCE | 534171.8 ms | 524718.4 ms | 9453.4 ms | 281590.3 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 534018.2 ms | 523977.1 ms | 10041.1 ms | 281199.9 ms |
| IXGo | LLGoNoLTO | 451154.9 ms | 442020.9 ms | 9134.1 ms | 130154.1 ms |
| IXGo | LLGoDeadcodeDrop | 406680.3 ms | 394508.4 ms | 12171.9 ms | 124078.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 266044.2 ms | 261351.3 ms | 4692.9 ms | 161443.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 263237.3 ms | 258769.4 ms | 4467.8 ms | 159615.3 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 261116.7 ms | 256474.8 ms | 4641.9 ms | 159977.7 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 205446.2 ms | 202054.2 ms | 3392.0 ms | 118229.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 200236.2 ms | 196838.9 ms | 3397.3 ms | 107427.1 ms |
| Aws_restjson | LLGoDeadcodeDrop | 199289.9 ms | 196403.3 ms | 2886.6 ms | 68487.0 ms |
| Aws_restjson | LLGoNoLTO | 197702.0 ms | 194749.5 ms | 2952.5 ms | 67926.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 194698.0 ms | 191360.4 ms | 3337.7 ms | 105757.9 ms |
| Etcdctl | LLGoDeadcodeDrop | 194611.9 ms | 189636.4 ms | 4975.5 ms | 66750.1 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 192608.7 ms | 189463.7 ms | 3145.0 ms | 130529.0 ms |
| Etcdctl | LLGoNoLTO | 192524.9 ms | 188567.3 ms | 3957.6 ms | 64555.1 ms |
| XGo | LLGoFullLTOGlobalDCE | 189987.7 ms | 186802.7 ms | 3185.0 ms | 128012.1 ms |
| XGo | LLGoFullLTONoGlobalDCE | 189170.6 ms | 186027.6 ms | 3142.9 ms | 127980.7 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 176219.2 ms | 173306.8 ms | 2912.3 ms | 105545.4 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 176003.9 ms | 172586.0 ms | 3417.9 ms | 105540.8 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 175500.3 ms | 172494.6 ms | 3005.7 ms | 105167.9 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 171736.9 ms | 168570.3 ms | 3166.5 ms | 97389.0 ms |
| Uber_zap | LLGoDeadcodeDrop | 170557.9 ms | 167827.5 ms | 2730.4 ms | 61767.5 ms |
| Uber_zap | LLGoNoLTO | 169384.0 ms | 166795.2 ms | 2588.9 ms | 61518.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 166852.4 ms | 163844.3 ms | 3008.0 ms | 94875.4 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 163622.8 ms | 160870.8 ms | 2752.0 ms | 59497.6 ms |
| K8s_workqueue | LLGoNoLTO | 162612.6 ms | 159886.2 ms | 2726.4 ms | 59266.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 160018.9 ms | 157078.9 ms | 2940.0 ms | 89847.5 ms |
| XGo | LLGoDeadcodeDrop | 120656.8 ms | 117479.9 ms | 3176.9 ms | 45205.2 ms |
| XGo | LLGoNoLTO | 118071.5 ms | 115567.7 ms | 2503.8 ms | 43414.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 81731.7 ms | 79781.3 ms | 1950.5 ms | 49182.7 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 80898.7 ms | 79079.2 ms | 1819.4 ms | 48782.6 ms |
| Gorm_schema | LLGoDeadcodeDrop | 79934.4 ms | 78293.4 ms | 1641.1 ms | 27201.2 ms |
| Gorm_schema | LLGoNoLTO | 79073.9 ms | 77506.1 ms | 1567.8 ms | 26737.5 ms |
| Toml | LLGoFullLTONoGlobalDCE | 75560.9 ms | 73695.6 ms | 1865.2 ms | 45125.8 ms |
| Toml | LLGoDeadcodeDrop | 74637.4 ms | 72992.8 ms | 1644.7 ms | 25239.4 ms |
| Toml | LLGoNoLTO | 73432.1 ms | 71786.2 ms | 1645.9 ms | 24677.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 71265.2 ms | 69397.1 ms | 1868.1 ms | 38569.2 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 68204.7 ms | 66403.3 ms | 1801.3 ms | 37256.0 ms |
| Toml | LLGoFullLTOGlobalDCE | 67821.2 ms | 66041.6 ms | 1779.6 ms | 36859.8 ms |
| IXGo | Go | 62575.6 ms | 58202.5 ms | 4373.1 ms | 17977.5 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 52935.5 ms | 51636.6 ms | 1299.0 ms | 33137.8 ms |
| Dustin_humanize | LLGoNoLTO | 52063.3 ms | 50896.0 ms | 1167.3 ms | 19118.3 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 51583.4 ms | 50418.8 ms | 1164.6 ms | 18958.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 46700.2 ms | 45490.4 ms | 1209.8 ms | 26218.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 45702.4 ms | 44444.2 ms | 1258.2 ms | 25314.4 ms |
| Etcdctl | Go | 25258.6 ms | 23499.4 ms | 1759.1 ms | 7644.2 ms |
| XGo | Go | 14365.2 ms | 13344.9 ms | 1020.3 ms | 4343.9 ms |
| Aws_restjson | Go | 6068.7 ms | 5460.7 ms | 608.0 ms | 2663.5 ms |
| Gorm_schema | Go | 4385.0 ms | 4037.5 ms | 347.5 ms | 1679.8 ms |
| Uber_zap | Go | 4067.5 ms | 3654.9 ms | 412.6 ms | 1969.1 ms |
| K8s_workqueue | Go | 3614.6 ms | 3155.1 ms | 459.6 ms | 1731.1 ms |
| Toml | Go | 1559.3 ms | 1360.1 ms | 199.2 ms | 723.4 ms |
| Dustin_humanize | Go | 621.8 ms | 503.0 ms | 118.8 ms | 304.2 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1781091.6 ms | 1031168.6 ms | 9 |
| LLGoFullLTOGlobalDCE | 1720700.5 ms | 987280.0 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1709835.4 ms | 968975.8 ms | 9 |
| LLGoNoLTO | 1496019.2 ms | 497369.0 ms | 9 |
| LLGoDeadcodeDrop | 1461574.9 ms | 497185.2 ms | 9 |
| Go | 122516.3 ms | 39036.5 ms | 9 |

Dependency download details are in `download-timings.log`.
