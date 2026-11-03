## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 874464.6 ms | 848812.7 ms | 25651.9 ms | 541842.9 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 863786.8 ms | 837799.3 ms | 25987.5 ms | 540575.5 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 848364.1 ms | 822635.8 ms | 25728.4 ms | 535933.8 ms |
| IXGo | LLGoNoLTO | 533994.4 ms | 511669.8 ms | 22324.6 ms | 159506.6 ms |
| IXGo | LLGoDeadcodeDrop | 509604.8 ms | 482604.4 ms | 27000.5 ms | 157192.2 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 431057.4 ms | 418737.0 ms | 12320.4 ms | 315197.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 422825.1 ms | 410803.6 ms | 12021.6 ms | 305896.6 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 420458.5 ms | 408487.0 ms | 11971.5 ms | 305227.3 ms |
| XGo | LLGoFullLTONoGlobalDCE | 311252.0 ms | 303087.2 ms | 8164.8 ms | 247967.1 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 306294.9 ms | 299762.0 ms | 6532.9 ms | 209398.5 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 271981.2 ms | 264106.5 ms | 7874.7 ms | 207235.6 ms |
| XGo | LLGoFullLTOGlobalDCE | 269607.9 ms | 261900.3 ms | 7707.6 ms | 205274.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 263643.8 ms | 257446.8 ms | 6197.0 ms | 169762.3 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 260104.8 ms | 253654.2 ms | 6450.6 ms | 166960.1 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 247307.4 ms | 241784.3 ms | 5523.0 ms | 174039.4 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 242157.0 ms | 236572.8 ms | 5584.2 ms | 170641.1 ms |
| Etcdctl | LLGoDeadcodeDrop | 236066.7 ms | 224813.3 ms | 11253.5 ms | 80261.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 235730.7 ms | 230314.6 ms | 5416.1 ms | 157793.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 235544.3 ms | 230272.1 ms | 5272.2 ms | 165714.2 ms |
| Aws_restjson | LLGoNoLTO | 227955.2 ms | 222675.9 ms | 5279.3 ms | 70911.7 ms |
| Etcdctl | LLGoNoLTO | 222673.4 ms | 213100.6 ms | 9572.8 ms | 75139.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 220789.5 ms | 215405.2 ms | 5384.4 ms | 147128.8 ms |
| Aws_restjson | LLGoDeadcodeDrop | 214527.5 ms | 208914.9 ms | 5612.6 ms | 67130.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 200432.4 ms | 195398.7 ms | 5033.7 ms | 130661.7 ms |
| Uber_zap | LLGoDeadcodeDrop | 172767.8 ms | 168151.1 ms | 4616.7 ms | 55475.2 ms |
| Uber_zap | LLGoNoLTO | 170868.1 ms | 166877.4 ms | 3990.6 ms | 54688.5 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 164391.0 ms | 159774.8 ms | 4616.2 ms | 53278.0 ms |
| K8s_workqueue | LLGoNoLTO | 163328.2 ms | 159071.5 ms | 4256.7 ms | 52207.7 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 148296.1 ms | 144333.2 ms | 3963.0 ms | 103919.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 142176.8 ms | 138308.4 ms | 3868.4 ms | 97861.3 ms |
| Toml | LLGoFullLTONoGlobalDCE | 130969.4 ms | 127544.8 ms | 3424.6 ms | 90387.4 ms |
| XGo | LLGoDeadcodeDrop | 126432.8 ms | 119215.1 ms | 7217.6 ms | 44802.6 ms |
| XGo | LLGoNoLTO | 124773.4 ms | 118664.3 ms | 6109.2 ms | 44905.7 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 119156.6 ms | 115450.8 ms | 3705.8 ms | 74810.1 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 115944.9 ms | 112572.3 ms | 3372.6 ms | 74507.5 ms |
| Toml | LLGoFullLTOGlobalDCE | 114918.5 ms | 111621.2 ms | 3297.2 ms | 73345.3 ms |
| Gorm_schema | LLGoDeadcodeDrop | 105944.1 ms | 102423.4 ms | 3520.7 ms | 36403.3 ms |
| Gorm_schema | LLGoNoLTO | 105120.5 ms | 101930.0 ms | 3190.4 ms | 35578.7 ms |
| Toml | LLGoNoLTO | 100155.9 ms | 97252.2 ms | 2903.7 ms | 33711.1 ms |
| Toml | LLGoDeadcodeDrop | 99261.0 ms | 96267.9 ms | 2993.1 ms | 33453.8 ms |
| IXGo | Go | 96784.2 ms | 82042.2 ms | 14742.0 ms | 26509.2 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 93344.4 ms | 90950.4 ms | 2394.0 ms | 67127.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 76022.3 ms | 73731.6 ms | 2290.7 ms | 49245.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 74158.6 ms | 71975.0 ms | 2183.7 ms | 47630.0 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 72418.9 ms | 70173.0 ms | 2245.9 ms | 26742.2 ms |
| Dustin_humanize | LLGoNoLTO | 68335.0 ms | 66378.4 ms | 1956.6 ms | 24970.9 ms |
| Etcdctl | Go | 38095.7 ms | 32900.6 ms | 5195.1 ms | 11802.4 ms |
| XGo | Go | 21752.8 ms | 18683.3 ms | 3069.5 ms | 6344.3 ms |
| Aws_restjson | Go | 9634.8 ms | 8094.7 ms | 1540.0 ms | 4107.1 ms |
| Gorm_schema | Go | 6633.6 ms | 5704.7 ms | 928.9 ms | 2637.8 ms |
| Uber_zap | Go | 6004.4 ms | 5073.4 ms | 931.1 ms | 2473.5 ms |
| K8s_workqueue | Go | 5221.2 ms | 4381.3 ms | 839.8 ms | 1852.8 ms |
| Toml | Go | 2245.5 ms | 1833.5 ms | 412.1 ms | 1064.4 ms |
| Dustin_humanize | Go | 988.2 ms | 734.9 ms | 253.3 ms | 556.5 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2759042.7 ms | 1914612.0 ms | 9 |
| LLGoFullLTOGlobalDCE | 2612223.5 ms | 1750984.7 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2569523.9 ms | 1710488.7 ms | 9 |
| LLGoNoLTO | 1717204.1 ms | 551620.6 ms | 9 |
| LLGoDeadcodeDrop | 1701414.6 ms | 554738.9 ms | 9 |
| Go | 187360.5 ms | 57347.9 ms | 9 |

Dependency download details are in `download-timings.log`.
