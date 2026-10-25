## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 834657.1 ms | 822702.8 ms | 11954.3 ms | 537502.4 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 833824.9 ms | 820592.7 ms | 13232.2 ms | 542120.6 ms |
| IXGo | LLGoFullLTOGlobalDCE | 822858.6 ms | 811119.1 ms | 11739.5 ms | 530874.9 ms |
| IXGo | LLGoNoLTO | 490463.1 ms | 481521.8 ms | 8941.3 ms | 153211.1 ms |
| IXGo | LLGoDeadcodeDrop | 488457.8 ms | 474109.1 ms | 14348.7 ms | 156452.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 437452.8 ms | 431486.9 ms | 5965.9 ms | 320947.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 429115.6 ms | 423096.4 ms | 6019.2 ms | 315312.9 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 427393.6 ms | 421475.8 ms | 5917.8 ms | 316520.6 ms |
| XGo | LLGoFullLTONoGlobalDCE | 380898.1 ms | 375382.2 ms | 5515.9 ms | 299144.3 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 317908.4 ms | 313951.6 ms | 3956.7 ms | 222077.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 292297.8 ms | 288345.3 ms | 3952.5 ms | 192838.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 289339.4 ms | 285419.6 ms | 3919.8 ms | 191058.6 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 282848.9 ms | 278756.9 ms | 4092.0 ms | 219450.9 ms |
| XGo | LLGoFullLTOGlobalDCE | 280027.6 ms | 276067.6 ms | 3960.0 ms | 217519.4 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 273481.3 ms | 269968.0 ms | 3513.4 ms | 197253.3 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 268021.4 ms | 264285.4 ms | 3736.0 ms | 194516.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 263845.4 ms | 260256.5 ms | 3588.9 ms | 189935.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 247849.7 ms | 244405.8 ms | 3443.9 ms | 171593.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 247575.7 ms | 244226.9 ms | 3348.8 ms | 171348.4 ms |
| Aws_restjson | LLGoDeadcodeDrop | 235374.9 ms | 231954.2 ms | 3420.7 ms | 83274.8 ms |
| Aws_restjson | LLGoNoLTO | 235223.2 ms | 232178.8 ms | 3044.4 ms | 82934.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 231324.0 ms | 227888.2 ms | 3435.8 ms | 157600.3 ms |
| Etcdctl | LLGoDeadcodeDrop | 227612.8 ms | 221940.6 ms | 5672.2 ms | 82439.6 ms |
| Etcdctl | LLGoNoLTO | 226545.9 ms | 222386.7 ms | 4159.2 ms | 80345.8 ms |
| Uber_zap | LLGoDeadcodeDrop | 198235.6 ms | 195334.8 ms | 2900.9 ms | 74890.5 ms |
| Uber_zap | LLGoNoLTO | 197640.2 ms | 195121.2 ms | 2519.0 ms | 74419.1 ms |
| K8s_workqueue | LLGoNoLTO | 190221.4 ms | 187426.8 ms | 2794.5 ms | 72383.0 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 189097.9 ms | 185960.0 ms | 3137.8 ms | 72635.9 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 141130.4 ms | 138920.6 ms | 2209.8 ms | 99176.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 140724.0 ms | 138525.1 ms | 2198.9 ms | 97515.4 ms |
| XGo | LLGoNoLTO | 129534.1 ms | 126662.3 ms | 2871.8 ms | 51218.6 ms |
| Toml | LLGoFullLTONoGlobalDCE | 128506.2 ms | 126257.8 ms | 2248.4 ms | 89625.0 ms |
| XGo | LLGoDeadcodeDrop | 128317.3 ms | 124678.8 ms | 3638.4 ms | 50145.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 123824.2 ms | 121771.1 ms | 2053.1 ms | 79336.4 ms |
| Toml | LLGoFullLTOGlobalDCE | 111165.1 ms | 108958.2 ms | 2206.9 ms | 70889.6 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 110783.7 ms | 108717.2 ms | 2066.5 ms | 70842.7 ms |
| Gorm_schema | LLGoDeadcodeDrop | 104784.9 ms | 102803.8 ms | 1981.1 ms | 35331.8 ms |
| Gorm_schema | LLGoNoLTO | 103887.5 ms | 102140.2 ms | 1747.3 ms | 34576.4 ms |
| Toml | LLGoDeadcodeDrop | 97969.0 ms | 95890.4 ms | 2078.6 ms | 32863.4 ms |
| Toml | LLGoNoLTO | 96767.6 ms | 94831.5 ms | 1936.1 ms | 32250.3 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 92910.1 ms | 91256.4 ms | 1653.7 ms | 67567.9 ms |
| IXGo | Go | 83663.7 ms | 78359.2 ms | 5304.5 ms | 23986.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 72587.3 ms | 71107.3 ms | 1480.0 ms | 46810.9 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 72532.3 ms | 71042.6 ms | 1489.6 ms | 46723.3 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 66806.5 ms | 65428.8 ms | 1377.7 ms | 24132.5 ms |
| Dustin_humanize | LLGoNoLTO | 66530.9 ms | 65295.4 ms | 1235.5 ms | 23922.2 ms |
| Etcdctl | Go | 33204.0 ms | 31136.5 ms | 2067.5 ms | 9967.0 ms |
| XGo | Go | 18874.7 ms | 17695.2 ms | 1179.5 ms | 5590.5 ms |
| Aws_restjson | Go | 7885.4 ms | 7171.1 ms | 714.3 ms | 3173.8 ms |
| Uber_zap | Go | 6568.4 ms | 5955.4 ms | 613.0 ms | 2802.6 ms |
| Gorm_schema | Go | 5837.6 ms | 5361.7 ms | 475.9 ms | 2488.3 ms |
| K8s_workqueue | Go | 4775.6 ms | 4202.2 ms | 573.5 ms | 2192.2 ms |
| Toml | Go | 1987.3 ms | 1764.3 ms | 223.0 ms | 906.5 ms |
| Dustin_humanize | Go | 795.4 ms | 644.7 ms | 150.6 ms | 386.1 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2864074.3 ms | 2028002.0 ms | 9 |
| LLGoFullLTOGlobalDCE | 2660142.0 ms | 1832958.1 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2630667.1 ms | 1795142.9 ms | 9 |
| LLGoNoLTO | 1736813.9 ms | 605260.3 ms | 9 |
| LLGoDeadcodeDrop | 1736656.7 ms | 612165.8 ms | 9 |
| Go | 163592.1 ms | 51493.3 ms | 9 |

Dependency download details are in `download-timings.log`.
