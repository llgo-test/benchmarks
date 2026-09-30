## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 539149.1 ms | 525463.1 ms | 13686.0 ms | 284848.9 ms |
| IXGo | LLGoFullLTOGlobalDCE | 536466.5 ms | 520622.6 ms | 15843.9 ms | 281342.8 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 517345.0 ms | 504557.0 ms | 12788.0 ms | 276569.8 ms |
| IXGo | LLGoDeadcodeDrop | 410919.6 ms | 399013.7 ms | 11905.9 ms | 123465.3 ms |
| IXGo | LLGoNoLTO | 404485.5 ms | 393043.0 ms | 11442.5 ms | 120694.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 252347.7 ms | 246529.3 ms | 5818.4 ms | 158049.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 250704.6 ms | 245038.0 ms | 5666.6 ms | 157299.8 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 247675.3 ms | 242583.1 ms | 5092.2 ms | 156442.1 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 195924.1 ms | 192511.6 ms | 3412.5 ms | 118962.5 ms |
| Aws_restjson | LLGoDeadcodeDrop | 195004.1 ms | 191601.2 ms | 3402.9 ms | 70717.5 ms |
| Aws_restjson | LLGoNoLTO | 192218.0 ms | 188969.0 ms | 3249.0 ms | 70347.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 186282.3 ms | 182695.8 ms | 3586.5 ms | 107199.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 185707.9 ms | 182311.1 ms | 3396.8 ms | 106989.0 ms |
| Etcdctl | LLGoDeadcodeDrop | 182151.4 ms | 177367.9 ms | 4783.5 ms | 61258.9 ms |
| Etcdctl | LLGoNoLTO | 178771.5 ms | 174252.8 ms | 4518.8 ms | 61154.0 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 177347.1 ms | 173457.3 ms | 3889.8 ms | 124030.8 ms |
| XGo | LLGoFullLTONoGlobalDCE | 175101.0 ms | 171255.9 ms | 3845.1 ms | 123174.0 ms |
| XGo | LLGoFullLTOGlobalDCE | 174369.9 ms | 170768.0 ms | 3601.9 ms | 122103.7 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 165588.8 ms | 162796.6 ms | 2792.2 ms | 106618.8 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 161102.7 ms | 158088.7 ms | 3014.0 ms | 103109.1 ms |
| Uber_zap | LLGoDeadcodeDrop | 160614.5 ms | 157817.7 ms | 2796.7 ms | 62570.7 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 160404.5 ms | 157283.5 ms | 3121.0 ms | 103546.7 ms |
| Uber_zap | LLGoNoLTO | 158618.4 ms | 155937.3 ms | 2681.1 ms | 62600.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 155885.3 ms | 152902.9 ms | 2982.3 ms | 95229.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 155270.9 ms | 152381.7 ms | 2889.2 ms | 94979.8 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 155066.3 ms | 152239.3 ms | 2827.0 ms | 61253.2 ms |
| K8s_workqueue | LLGoNoLTO | 153296.8 ms | 150586.4 ms | 2710.4 ms | 60804.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 148067.8 ms | 145116.5 ms | 2951.3 ms | 90071.1 ms |
| XGo | LLGoDeadcodeDrop | 106173.9 ms | 102868.3 ms | 3305.6 ms | 40606.0 ms |
| XGo | LLGoNoLTO | 103379.7 ms | 100474.3 ms | 2905.4 ms | 39420.7 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 82237.0 ms | 80332.5 ms | 1904.5 ms | 49513.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 82052.7 ms | 80235.2 ms | 1817.5 ms | 48896.4 ms |
| Gorm_schema | LLGoDeadcodeDrop | 81669.2 ms | 79930.0 ms | 1739.2 ms | 27609.4 ms |
| Gorm_schema | LLGoNoLTO | 80505.6 ms | 78723.6 ms | 1782.0 ms | 27069.6 ms |
| IXGo | Go | 79955.2 ms | 73714.1 ms | 6241.1 ms | 22834.7 ms |
| Toml | LLGoDeadcodeDrop | 77304.2 ms | 75572.0 ms | 1732.2 ms | 25649.1 ms |
| Toml | LLGoNoLTO | 76295.5 ms | 74551.3 ms | 1744.2 ms | 25439.5 ms |
| Toml | LLGoFullLTONoGlobalDCE | 75623.7 ms | 73738.4 ms | 1885.3 ms | 44937.1 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 71814.5 ms | 70025.1 ms | 1789.4 ms | 38638.0 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 68818.6 ms | 66852.2 ms | 1966.5 ms | 37713.3 ms |
| Toml | LLGoFullLTOGlobalDCE | 68386.8 ms | 66496.4 ms | 1890.4 ms | 37465.0 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 52483.5 ms | 51180.9 ms | 1302.6 ms | 33146.5 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 52182.5 ms | 50936.4 ms | 1246.1 ms | 18964.0 ms |
| Dustin_humanize | LLGoNoLTO | 51807.1 ms | 50584.3 ms | 1222.8 ms | 18760.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 44394.7 ms | 43137.1 ms | 1257.5 ms | 24614.9 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 44135.3 ms | 42879.8 ms | 1255.5 ms | 24528.8 ms |
| Etcdctl | Go | 32298.4 ms | 29831.4 ms | 2467.0 ms | 10150.1 ms |
| XGo | Go | 18477.9 ms | 16969.6 ms | 1508.3 ms | 5632.4 ms |
| Aws_restjson | Go | 7825.2 ms | 6968.1 ms | 857.1 ms | 3448.9 ms |
| Gorm_schema | Go | 5570.9 ms | 5153.0 ms | 417.9 ms | 2183.1 ms |
| Uber_zap | Go | 5161.7 ms | 4684.0 ms | 477.7 ms | 2028.4 ms |
| K8s_workqueue | Go | 4531.2 ms | 4023.7 ms | 507.5 ms | 1600.6 ms |
| Toml | Go | 1995.2 ms | 1729.0 ms | 266.2 ms | 925.5 ms |
| Dustin_humanize | Go | 818.1 ms | 656.3 ms | 161.8 ms | 389.3 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1672383.0 ms | 1012910.8 ms | 9 |
| LLGoFullLTOGlobalDCE | 1658197.3 ms | 976714.4 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1644107.1 ms | 960395.5 ms | 9 |
| LLGoDeadcodeDrop | 1421085.6 ms | 492094.0 ms | 9 |
| LLGoNoLTO | 1399378.2 ms | 486292.1 ms | 9 |
| Go | 156633.7 ms | 49193.0 ms | 9 |

Dependency download details are in `download-timings.log`.
