## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 960004.4 ms | 947525.6 ms | 12478.8 ms | 577197.9 ms |
| IXGo | LLGoFullLTOGlobalDCE | 845270.5 ms | 832938.2 ms | 12332.3 ms | 552535.9 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 840371.6 ms | 827298.9 ms | 13072.7 ms | 544624.8 ms |
| IXGo | LLGoDeadcodeDrop | 604802.3 ms | 590334.7 ms | 14467.5 ms | 184105.2 ms |
| IXGo | LLGoNoLTO | 509070.0 ms | 499598.1 ms | 9471.9 ms | 156753.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 454555.0 ms | 448528.9 ms | 6026.1 ms | 335625.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 446132.7 ms | 440135.1 ms | 5997.6 ms | 327201.5 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 441481.7 ms | 435371.7 ms | 6110.0 ms | 330570.6 ms |
| XGo | LLGoFullLTONoGlobalDCE | 330927.7 ms | 326533.2 ms | 4394.5 ms | 267898.6 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 328048.6 ms | 323924.5 ms | 4124.1 ms | 227805.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 304918.9 ms | 301046.4 ms | 3872.5 ms | 197051.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 304185.6 ms | 300410.5 ms | 3775.0 ms | 202714.3 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 289466.9 ms | 285262.5 ms | 4204.4 ms | 224470.6 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 287302.2 ms | 283731.5 ms | 3570.7 ms | 208195.5 ms |
| XGo | LLGoFullLTOGlobalDCE | 286956.6 ms | 282934.4 ms | 4022.1 ms | 224122.9 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 266074.8 ms | 262566.4 ms | 3508.4 ms | 193537.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 265822.0 ms | 262394.5 ms | 3427.5 ms | 191671.2 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 258051.9 ms | 254598.7 ms | 3453.2 ms | 178275.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 250016.7 ms | 246746.1 ms | 3270.6 ms | 172271.1 ms |
| Aws_restjson | LLGoNoLTO | 241078.0 ms | 237958.7 ms | 3119.3 ms | 84494.3 ms |
| Aws_restjson | LLGoDeadcodeDrop | 237602.2 ms | 234129.6 ms | 3472.6 ms | 83001.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 234746.3 ms | 231345.0 ms | 3401.3 ms | 160309.2 ms |
| Etcdctl | LLGoDeadcodeDrop | 233405.7 ms | 228032.8 ms | 5372.9 ms | 82578.8 ms |
| Etcdctl | LLGoNoLTO | 226184.1 ms | 221477.1 ms | 4707.0 ms | 79423.5 ms |
| Uber_zap | LLGoNoLTO | 203804.0 ms | 201021.7 ms | 2782.3 ms | 75933.4 ms |
| Uber_zap | LLGoDeadcodeDrop | 200809.3 ms | 197768.5 ms | 3040.8 ms | 75167.9 ms |
| K8s_workqueue | LLGoNoLTO | 192134.0 ms | 189296.5 ms | 2837.5 ms | 71802.3 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 190850.3 ms | 187728.7 ms | 3121.5 ms | 72064.5 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 151143.2 ms | 148808.4 ms | 2334.8 ms | 106997.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 142853.4 ms | 140689.8 ms | 2163.6 ms | 99891.3 ms |
| Toml | LLGoFullLTONoGlobalDCE | 138406.3 ms | 135900.4 ms | 2505.9 ms | 97097.9 ms |
| XGo | LLGoNoLTO | 129281.2 ms | 126526.7 ms | 2754.5 ms | 50194.8 ms |
| XGo | LLGoDeadcodeDrop | 128920.0 ms | 125134.5 ms | 3785.5 ms | 49431.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 120817.3 ms | 118847.4 ms | 1969.9 ms | 76340.8 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 114771.4 ms | 112440.3 ms | 2331.1 ms | 73716.4 ms |
| Toml | LLGoFullLTOGlobalDCE | 113497.1 ms | 111373.5 ms | 2123.6 ms | 73569.8 ms |
| Gorm_schema | LLGoDeadcodeDrop | 109406.5 ms | 107335.7 ms | 2070.8 ms | 37144.1 ms |
| Gorm_schema | LLGoNoLTO | 104967.3 ms | 103230.8 ms | 1736.5 ms | 35135.0 ms |
| Toml | LLGoDeadcodeDrop | 101594.3 ms | 99400.2 ms | 2194.0 ms | 34130.7 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 99138.4 ms | 97362.2 ms | 1776.2 ms | 72270.0 ms |
| Toml | LLGoNoLTO | 97598.4 ms | 95739.8 ms | 1858.6 ms | 32403.5 ms |
| IXGo | Go | 86513.9 ms | 81347.4 ms | 5166.5 ms | 23933.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 77643.3 ms | 76123.6 ms | 1519.7 ms | 50645.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 76899.9 ms | 75390.6 ms | 1509.3 ms | 50161.9 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 69914.3 ms | 68350.7 ms | 1563.6 ms | 25529.4 ms |
| Dustin_humanize | LLGoNoLTO | 69102.7 ms | 67840.8 ms | 1261.9 ms | 24673.8 ms |
| Etcdctl | Go | 35111.6 ms | 32727.8 ms | 2383.8 ms | 11140.7 ms |
| XGo | Go | 19156.1 ms | 17990.6 ms | 1165.5 ms | 5638.0 ms |
| Aws_restjson | Go | 8309.7 ms | 7598.8 ms | 710.9 ms | 3426.4 ms |
| Gorm_schema | Go | 5789.1 ms | 5404.6 ms | 384.5 ms | 2183.3 ms |
| Uber_zap | Go | 5431.2 ms | 5026.4 ms | 404.8 ms | 2141.7 ms |
| K8s_workqueue | Go | 4845.6 ms | 4410.2 ms | 435.4 ms | 1729.0 ms |
| Toml | Go | 2073.7 ms | 1869.2 ms | 204.6 ms | 951.1 ms |
| Dustin_humanize | Go | 845.7 ms | 686.7 ms | 159.0 ms | 426.3 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2882894.4 ms | 2048997.7 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2814975.5 ms | 1873631.9 ms | 9 |
| LLGoFullLTOGlobalDCE | 2731634.4 ms | 1894139.9 ms | 9 |
| LLGoDeadcodeDrop | 1877304.7 ms | 643153.1 ms | 9 |
| LLGoNoLTO | 1773219.7 ms | 610814.2 ms | 9 |
| Go | 168076.7 ms | 51569.6 ms | 9 |

Dependency download details are in `download-timings.log`.
