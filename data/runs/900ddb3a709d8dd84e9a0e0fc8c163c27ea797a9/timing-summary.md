## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 757911.1 ms | 747040.5 ms | 10870.6 ms | 378796.8 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 719576.0 ms | 708307.0 ms | 11269.0 ms | 358600.0 ms |
| IXGo | LLGoFullLTOGlobalDCE | 665970.8 ms | 655510.6 ms | 10460.1 ms | 341634.9 ms |
| IXGo | LLGoNoLTO | 561178.3 ms | 551447.0 ms | 9731.3 ms | 162445.6 ms |
| IXGo | LLGoDeadcodeDrop | 517114.0 ms | 503204.4 ms | 13909.6 ms | 155166.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 347025.8 ms | 341625.8 ms | 5400.0 ms | 202461.6 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 346494.8 ms | 341392.3 ms | 5102.5 ms | 202345.9 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 339452.3 ms | 334218.6 ms | 5233.8 ms | 199579.4 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 300392.4 ms | 296359.3 ms | 4033.1 ms | 161962.2 ms |
| Aws_restjson | LLGoNoLTO | 284708.4 ms | 281279.2 ms | 3429.2 ms | 93760.0 ms |
| Aws_restjson | LLGoDeadcodeDrop | 275054.6 ms | 271615.8 ms | 3438.8 ms | 91574.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 265579.2 ms | 261624.9 ms | 3954.3 ms | 140151.7 ms |
| Etcdctl | LLGoDeadcodeDrop | 264155.7 ms | 258531.8 ms | 5624.0 ms | 87939.4 ms |
| Etcdctl | LLGoNoLTO | 263104.4 ms | 258760.1 ms | 4344.3 ms | 86069.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 254522.8 ms | 250561.0 ms | 3961.8 ms | 134045.3 ms |
| XGo | LLGoFullLTONoGlobalDCE | 244510.8 ms | 241186.3 ms | 3324.6 ms | 161953.6 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 243820.1 ms | 240467.9 ms | 3352.2 ms | 159872.0 ms |
| XGo | LLGoFullLTOGlobalDCE | 243371.6 ms | 240028.7 ms | 3342.9 ms | 158563.9 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 233334.5 ms | 229710.2 ms | 3624.3 ms | 134455.0 ms |
| Uber_zap | LLGoDeadcodeDrop | 231166.6 ms | 228032.6 ms | 3134.0 ms | 81256.4 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 229304.8 ms | 226061.0 ms | 3243.8 ms | 131414.5 ms |
| Uber_zap | LLGoNoLTO | 227656.2 ms | 224831.0 ms | 2825.1 ms | 80109.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 227490.2 ms | 224054.3 ms | 3435.9 ms | 124784.2 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 226857.7 ms | 223784.4 ms | 3073.4 ms | 79711.1 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 225980.2 ms | 222667.1 ms | 3313.1 ms | 128944.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 225926.3 ms | 222303.5 ms | 3622.8 ms | 123171.4 ms |
| K8s_workqueue | LLGoNoLTO | 224626.3 ms | 221529.1 ms | 3097.2 ms | 78837.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 215703.4 ms | 212156.6 ms | 3546.8 ms | 116222.5 ms |
| XGo | LLGoNoLTO | 164814.3 ms | 161895.5 ms | 2918.8 ms | 59138.0 ms |
| XGo | LLGoDeadcodeDrop | 162178.7 ms | 158435.5 ms | 3743.3 ms | 59298.5 ms |
| Gorm_schema | LLGoNoLTO | 112021.6 ms | 110183.1 ms | 1838.5 ms | 37192.1 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 110734.3 ms | 108647.4 ms | 2087.0 ms | 65020.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 109505.8 ms | 107375.3 ms | 2130.5 ms | 63611.6 ms |
| Gorm_schema | LLGoDeadcodeDrop | 109400.0 ms | 107705.5 ms | 1694.5 ms | 36147.7 ms |
| Toml | LLGoDeadcodeDrop | 105692.9 ms | 103857.7 ms | 1835.2 ms | 34966.4 ms |
| Toml | LLGoNoLTO | 104445.4 ms | 102611.5 ms | 1834.0 ms | 34466.4 ms |
| Toml | LLGoFullLTONoGlobalDCE | 99910.8 ms | 97865.8 ms | 2045.0 ms | 57239.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 98647.8 ms | 96640.6 ms | 2007.2 ms | 51385.2 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 94024.4 ms | 91905.9 ms | 2118.5 ms | 49621.0 ms |
| Toml | LLGoFullLTOGlobalDCE | 90888.1 ms | 88912.4 ms | 1975.7 ms | 48109.5 ms |
| IXGo | Go | 85394.3 ms | 80060.0 ms | 5334.2 ms | 23950.7 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 73704.1 ms | 72204.8 ms | 1499.3 ms | 45193.2 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 72353.2 ms | 71082.5 ms | 1270.7 ms | 25788.6 ms |
| Dustin_humanize | LLGoNoLTO | 70119.8 ms | 68859.7 ms | 1260.1 ms | 25047.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 60880.2 ms | 59506.8 ms | 1373.5 ms | 32504.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 60577.9 ms | 59239.2 ms | 1338.8 ms | 32396.0 ms |
| Etcdctl | Go | 33615.2 ms | 31580.6 ms | 2034.7 ms | 10317.9 ms |
| XGo | Go | 19789.2 ms | 18516.7 ms | 1272.5 ms | 5834.4 ms |
| Aws_restjson | Go | 7876.3 ms | 7201.5 ms | 674.9 ms | 3199.4 ms |
| Gorm_schema | Go | 5872.0 ms | 5464.6 ms | 407.4 ms | 2273.1 ms |
| Uber_zap | Go | 5495.2 ms | 5075.2 ms | 420.0 ms | 2169.6 ms |
| K8s_workqueue | Go | 4867.8 ms | 4394.3 ms | 473.5 ms | 1743.0 ms |
| Toml | Go | 2056.4 ms | 1818.3 ms | 238.1 ms | 932.7 ms |
| Dustin_humanize | Go | 811.4 ms | 667.4 ms | 143.9 ms | 389.3 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2350920.1 ms | 1315418.4 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2310551.3 ms | 1255684.0 ms | 9 |
| LLGoFullLTOGlobalDCE | 2223769.2 ms | 1232938.6 ms | 9 |
| LLGoNoLTO | 2012674.6 ms | 657065.4 ms | 9 |
| LLGoDeadcodeDrop | 1963973.6 ms | 651849.6 ms | 9 |
| Go | 165777.8 ms | 50810.0 ms | 9 |

Dependency download details are in `download-timings.log`.
