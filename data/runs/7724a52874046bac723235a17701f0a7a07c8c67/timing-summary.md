## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 838369.1 ms | 817568.7 ms | 20800.4 ms | 548041.1 ms |
| IXGo | LLGoFullLTOGlobalDCE | 827477.5 ms | 806690.1 ms | 20787.5 ms | 538711.3 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 801964.7 ms | 781287.2 ms | 20677.5 ms | 528412.8 ms |
| IXGo | LLGoDeadcodeDrop | 486695.2 ms | 465184.1 ms | 21511.1 ms | 157722.0 ms |
| IXGo | LLGoNoLTO | 478476.4 ms | 460516.4 ms | 17960.0 ms | 148667.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 436773.9 ms | 427040.3 ms | 9733.6 ms | 318968.6 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 434010.7 ms | 424127.3 ms | 9883.4 ms | 319711.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 432222.6 ms | 422647.6 ms | 9575.1 ms | 315873.8 ms |
| XGo | LLGoFullLTONoGlobalDCE | 320700.1 ms | 313928.0 ms | 6772.2 ms | 256299.9 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 305237.2 ms | 299763.1 ms | 5474.0 ms | 206601.3 ms |
| XGo | LLGoFullLTOGlobalDCE | 280701.0 ms | 274150.3 ms | 6550.7 ms | 215411.9 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 280598.7 ms | 274177.5 ms | 6421.2 ms | 214781.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 275340.9 ms | 270092.9 ms | 5248.0 ms | 175399.3 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 272603.5 ms | 267443.8 ms | 5159.7 ms | 173700.5 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 256793.3 ms | 252174.0 ms | 4619.2 ms | 180646.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 248576.0 ms | 243830.4 ms | 4745.6 ms | 175038.3 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 245174.4 ms | 240603.6 ms | 4570.9 ms | 173756.7 ms |
| Aws_restjson | LLGoNoLTO | 240314.9 ms | 235732.4 ms | 4582.5 ms | 75346.4 ms |
| Aws_restjson | LLGoDeadcodeDrop | 239899.8 ms | 235014.6 ms | 4885.1 ms | 76700.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 233871.1 ms | 229352.7 ms | 4518.4 ms | 157263.2 ms |
| Etcdctl | LLGoDeadcodeDrop | 233157.5 ms | 224679.5 ms | 8478.0 ms | 81277.8 ms |
| Etcdctl | LLGoNoLTO | 232976.6 ms | 225442.7 ms | 7533.9 ms | 79580.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 228288.7 ms | 223756.8 ms | 4531.9 ms | 151547.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 209472.4 ms | 205171.1 ms | 4301.3 ms | 137327.9 ms |
| Uber_zap | LLGoNoLTO | 202869.4 ms | 198901.3 ms | 3968.0 ms | 65020.9 ms |
| Uber_zap | LLGoDeadcodeDrop | 199234.4 ms | 195087.0 ms | 4147.3 ms | 65197.2 ms |
| K8s_workqueue | LLGoNoLTO | 191847.9 ms | 188030.0 ms | 3817.9 ms | 61436.6 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 190984.4 ms | 186829.1 ms | 4155.3 ms | 63037.2 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 149910.2 ms | 146677.6 ms | 3232.5 ms | 104386.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 147107.0 ms | 144084.2 ms | 3022.8 ms | 101575.4 ms |
| Toml | LLGoFullLTONoGlobalDCE | 139388.3 ms | 136410.9 ms | 2977.4 ms | 96257.5 ms |
| XGo | LLGoNoLTO | 132017.5 ms | 126904.5 ms | 5113.0 ms | 48945.2 ms |
| XGo | LLGoDeadcodeDrop | 130820.4 ms | 125088.6 ms | 5731.8 ms | 47724.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 124509.8 ms | 121567.8 ms | 2942.0 ms | 78188.5 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 121045.4 ms | 118089.4 ms | 2956.0 ms | 77810.8 ms |
| Toml | LLGoFullLTOGlobalDCE | 120446.2 ms | 117512.5 ms | 2933.7 ms | 77264.8 ms |
| Gorm_schema | LLGoDeadcodeDrop | 112785.0 ms | 109711.4 ms | 3073.6 ms | 39619.9 ms |
| Gorm_schema | LLGoNoLTO | 111367.3 ms | 108728.4 ms | 2638.8 ms | 38464.4 ms |
| Toml | LLGoDeadcodeDrop | 104318.2 ms | 101811.1 ms | 2507.1 ms | 36153.8 ms |
| Toml | LLGoNoLTO | 103642.7 ms | 101289.1 ms | 2353.6 ms | 35814.9 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 97823.1 ms | 95692.0 ms | 2131.1 ms | 70398.5 ms |
| IXGo | Go | 85836.5 ms | 74722.6 ms | 11113.9 ms | 23378.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 78608.7 ms | 76725.5 ms | 1883.2 ms | 50488.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 77662.8 ms | 75803.7 ms | 1859.1 ms | 50034.5 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 71894.2 ms | 70024.0 ms | 1870.3 ms | 26971.3 ms |
| Dustin_humanize | LLGoNoLTO | 71688.1 ms | 70078.7 ms | 1609.4 ms | 26728.8 ms |
| Etcdctl | Go | 34377.5 ms | 30522.5 ms | 3855.1 ms | 10235.9 ms |
| XGo | Go | 19832.3 ms | 17525.1 ms | 2307.2 ms | 5934.3 ms |
| Aws_restjson | Go | 8258.0 ms | 7130.2 ms | 1127.8 ms | 3278.3 ms |
| Gorm_schema | Go | 5989.2 ms | 5275.7 ms | 713.5 ms | 2522.4 ms |
| Uber_zap | Go | 5451.5 ms | 4852.3 ms | 599.2 ms | 2136.6 ms |
| K8s_workqueue | Go | 4841.4 ms | 4151.0 ms | 690.4 ms | 1679.1 ms |
| Toml | Go | 2073.4 ms | 1798.1 ms | 275.3 ms | 941.2 ms |
| Dustin_humanize | Go | 802.1 ms | 650.2 ms | 151.9 ms | 391.5 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2751002.0 ms | 1936470.6 ms | 9 |
| LLGoFullLTOGlobalDCE | 2643405.0 ms | 1806572.6 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2590270.2 ms | 1750855.0 ms | 9 |
| LLGoDeadcodeDrop | 1769789.1 ms | 594404.2 ms | 9 |
| LLGoNoLTO | 1765200.7 ms | 580004.9 ms | 9 |
| Go | 167462.0 ms | 50497.5 ms | 9 |

Dependency download details are in `download-timings.log`.
