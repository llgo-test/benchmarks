## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 649903.4 ms | 633881.8 ms | 16021.6 ms | 343126.2 ms |
| IXGo | LLGoFullLTOGlobalDCE | 641233.8 ms | 627496.8 ms | 13737.1 ms | 337886.5 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 623510.1 ms | 611067.8 ms | 12442.3 ms | 332995.6 ms |
| IXGo | LLGoDeadcodeDrop | 514310.3 ms | 503119.1 ms | 11191.3 ms | 155906.0 ms |
| IXGo | LLGoNoLTO | 495158.7 ms | 484361.5 ms | 10797.3 ms | 149706.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 340023.9 ms | 334047.0 ms | 5976.9 ms | 201419.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 336236.4 ms | 330370.2 ms | 5866.2 ms | 199120.1 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 335900.7 ms | 329931.7 ms | 5969.0 ms | 201234.3 ms |
| Aws_restjson | LLGoDeadcodeDrop | 268884.4 ms | 265775.3 ms | 3109.1 ms | 90637.6 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 268656.8 ms | 264828.1 ms | 3828.7 ms | 149970.8 ms |
| Aws_restjson | LLGoNoLTO | 264437.0 ms | 261290.9 ms | 3146.1 ms | 89548.6 ms |
| Etcdctl | LLGoDeadcodeDrop | 260522.4 ms | 255488.2 ms | 5034.2 ms | 88158.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 256975.0 ms | 253051.1 ms | 3923.9 ms | 135941.2 ms |
| Etcdctl | LLGoNoLTO | 255805.3 ms | 250943.9 ms | 4861.4 ms | 86470.3 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 255065.0 ms | 251333.7 ms | 3731.3 ms | 134961.5 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 247404.4 ms | 242825.4 ms | 4579.0 ms | 163059.4 ms |
| XGo | LLGoFullLTOGlobalDCE | 244465.6 ms | 240054.1 ms | 4411.5 ms | 160747.1 ms |
| XGo | LLGoFullLTONoGlobalDCE | 243747.2 ms | 239533.4 ms | 4213.8 ms | 161335.2 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 233410.2 ms | 229961.0 ms | 3449.2 ms | 134077.6 ms |
| Uber_zap | LLGoDeadcodeDrop | 230077.4 ms | 227300.1 ms | 2777.3 ms | 81497.1 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 227972.4 ms | 224554.5 ms | 3417.9 ms | 131064.6 ms |
| Uber_zap | LLGoNoLTO | 227966.5 ms | 225113.8 ms | 2852.7 ms | 80979.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 227053.2 ms | 223620.8 ms | 3432.4 ms | 129562.2 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 223698.4 ms | 220369.1 ms | 3329.3 ms | 79234.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 222443.2 ms | 219127.0 ms | 3316.2 ms | 121438.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 221602.0 ms | 218225.8 ms | 3376.3 ms | 120963.2 ms |
| K8s_workqueue | LLGoNoLTO | 220333.4 ms | 217275.8 ms | 3057.5 ms | 78832.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 210873.5 ms | 207560.3 ms | 3313.2 ms | 113350.8 ms |
| XGo | LLGoDeadcodeDrop | 162089.5 ms | 158762.6 ms | 3326.9 ms | 60855.0 ms |
| XGo | LLGoNoLTO | 160253.4 ms | 156584.1 ms | 3669.3 ms | 59415.7 ms |
| Gorm_schema | LLGoDeadcodeDrop | 108784.9 ms | 107063.3 ms | 1721.6 ms | 35894.7 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 108046.5 ms | 106006.4 ms | 2040.1 ms | 62399.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 106930.7 ms | 104870.1 ms | 2060.6 ms | 61447.8 ms |
| Gorm_schema | LLGoNoLTO | 106876.3 ms | 105237.0 ms | 1639.4 ms | 35236.4 ms |
| Toml | LLGoDeadcodeDrop | 101936.6 ms | 99975.8 ms | 1960.7 ms | 33891.3 ms |
| Toml | LLGoNoLTO | 100291.5 ms | 98494.5 ms | 1796.9 ms | 33320.7 ms |
| Toml | LLGoFullLTONoGlobalDCE | 98411.4 ms | 96280.4 ms | 2131.0 ms | 55973.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 94824.9 ms | 92753.9 ms | 2071.0 ms | 49268.1 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 90484.8 ms | 88530.0 ms | 1954.8 ms | 47442.0 ms |
| Toml | LLGoFullLTOGlobalDCE | 89882.3 ms | 87995.9 ms | 1886.4 ms | 47190.9 ms |
| IXGo | Go | 84422.3 ms | 79331.3 ms | 5091.0 ms | 23846.1 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 70833.2 ms | 69594.1 ms | 1239.2 ms | 25333.4 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 69857.8 ms | 68452.7 ms | 1405.1 ms | 42271.0 ms |
| Dustin_humanize | LLGoNoLTO | 69845.3 ms | 68648.8 ms | 1196.4 ms | 25333.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 60600.8 ms | 59249.4 ms | 1351.5 ms | 32498.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 60543.0 ms | 59204.2 ms | 1338.8 ms | 32440.4 ms |
| Etcdctl | Go | 33523.7 ms | 31410.6 ms | 2113.1 ms | 10490.3 ms |
| XGo | Go | 19192.8 ms | 18008.6 ms | 1184.1 ms | 5632.4 ms |
| Aws_restjson | Go | 7951.2 ms | 7275.4 ms | 675.8 ms | 3166.8 ms |
| Gorm_schema | Go | 5818.3 ms | 5398.0 ms | 420.2 ms | 2295.6 ms |
| Uber_zap | Go | 5286.6 ms | 4835.1 ms | 451.6 ms | 2067.1 ms |
| K8s_workqueue | Go | 4927.9 ms | 4269.5 ms | 658.4 ms | 2408.6 ms |
| Toml | Go | 2059.9 ms | 1775.5 ms | 284.5 ms | 1027.3 ms |
| Dustin_humanize | Go | 810.4 ms | 685.4 ms | 125.0 ms | 382.5 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2209513.0 ms | 1271321.4 ms | 9 |
| LLGoFullLTOGlobalDCE | 2183853.3 ms | 1224795.3 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2172692.8 ms | 1207068.5 ms | 9 |
| LLGoDeadcodeDrop | 1941137.2 ms | 651408.0 ms | 9 |
| LLGoNoLTO | 1900967.4 ms | 638844.0 ms | 9 |
| Go | 163993.2 ms | 51316.7 ms | 9 |

Dependency download details are in `download-timings.log`.
