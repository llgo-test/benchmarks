## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 746833.5 ms | 736335.0 ms | 10498.5 ms | 365161.8 ms |
| IXGo | LLGoFullLTOGlobalDCE | 697537.6 ms | 686687.0 ms | 10850.6 ms | 354238.8 ms |
| IXGo | LLGoDeadcodeDrop | 680776.2 ms | 667009.0 ms | 13767.2 ms | 196660.8 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 650695.7 ms | 640723.6 ms | 9972.2 ms | 340629.3 ms |
| IXGo | LLGoNoLTO | 525871.9 ms | 516269.2 ms | 9602.7 ms | 153172.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 386254.5 ms | 381124.8 ms | 5129.7 ms | 242457.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 352409.7 ms | 346961.1 ms | 5448.6 ms | 205252.5 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 348835.9 ms | 343504.0 ms | 5331.9 ms | 205821.8 ms |
| Aws_restjson | LLGoDeadcodeDrop | 284367.8 ms | 281025.4 ms | 3342.5 ms | 94575.8 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 278556.9 ms | 274558.2 ms | 3998.7 ms | 154352.3 ms |
| Aws_restjson | LLGoNoLTO | 271848.1 ms | 268464.3 ms | 3383.8 ms | 91468.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 264442.6 ms | 260671.6 ms | 3771.0 ms | 139318.6 ms |
| Etcdctl | LLGoDeadcodeDrop | 261003.0 ms | 255216.7 ms | 5786.3 ms | 86412.3 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 258346.4 ms | 254222.9 ms | 4123.5 ms | 134526.4 ms |
| Etcdctl | LLGoNoLTO | 258262.5 ms | 254178.5 ms | 4083.9 ms | 84621.7 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 251130.7 ms | 247635.5 ms | 3495.2 ms | 164088.0 ms |
| XGo | LLGoFullLTONoGlobalDCE | 246884.7 ms | 243529.7 ms | 3355.1 ms | 163910.4 ms |
| XGo | LLGoFullLTOGlobalDCE | 244034.5 ms | 240693.4 ms | 3341.1 ms | 159755.6 ms |
| Uber_zap | LLGoDeadcodeDrop | 236673.3 ms | 233639.1 ms | 3034.2 ms | 83524.7 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 235748.2 ms | 232172.1 ms | 3576.1 ms | 135937.7 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 235064.1 ms | 231604.6 ms | 3459.5 ms | 136596.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 230254.9 ms | 226740.3 ms | 3514.5 ms | 132593.5 ms |
| Uber_zap | LLGoNoLTO | 227245.3 ms | 224251.7 ms | 2993.6 ms | 80043.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 226737.2 ms | 223336.4 ms | 3400.8 ms | 124722.2 ms |
| K8s_workqueue | LLGoNoLTO | 222866.6 ms | 219792.8 ms | 3073.8 ms | 78494.6 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 221739.3 ms | 218881.8 ms | 2857.5 ms | 78020.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 220020.0 ms | 216677.9 ms | 3342.1 ms | 120226.1 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 217174.6 ms | 213810.1 ms | 3364.5 ms | 118398.7 ms |
| XGo | LLGoDeadcodeDrop | 167297.4 ms | 163535.8 ms | 3761.6 ms | 61039.7 ms |
| XGo | LLGoNoLTO | 163248.4 ms | 160390.3 ms | 2858.1 ms | 58891.7 ms |
| Gorm_schema | LLGoDeadcodeDrop | 116025.4 ms | 114095.7 ms | 1929.7 ms | 38511.5 ms |
| Gorm_schema | LLGoNoLTO | 112084.4 ms | 110304.8 ms | 1779.6 ms | 37245.6 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 111203.6 ms | 109072.1 ms | 2131.4 ms | 65026.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 109092.8 ms | 107095.3 ms | 1997.5 ms | 62804.6 ms |
| Toml | LLGoDeadcodeDrop | 104252.4 ms | 102485.9 ms | 1766.4 ms | 34475.3 ms |
| Toml | LLGoNoLTO | 101288.9 ms | 99492.9 ms | 1795.9 ms | 33336.1 ms |
| Toml | LLGoFullLTONoGlobalDCE | 100790.0 ms | 98772.4 ms | 2017.5 ms | 57682.1 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 96617.4 ms | 94658.5 ms | 1958.9 ms | 50725.0 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 94422.8 ms | 92358.5 ms | 2064.2 ms | 49762.3 ms |
| Toml | LLGoFullLTOGlobalDCE | 91648.8 ms | 89642.3 ms | 2006.4 ms | 48102.8 ms |
| IXGo | Go | 83576.5 ms | 78727.4 ms | 4849.0 ms | 22841.6 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 73994.1 ms | 72528.0 ms | 1466.1 ms | 45193.5 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 71854.5 ms | 70618.1 ms | 1236.3 ms | 25634.9 ms |
| Dustin_humanize | LLGoNoLTO | 71743.6 ms | 70503.6 ms | 1240.0 ms | 25534.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 63693.9 ms | 62280.7 ms | 1413.2 ms | 34302.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 61348.8 ms | 59975.7 ms | 1373.2 ms | 32701.4 ms |
| Etcdctl | Go | 34539.1 ms | 32425.9 ms | 2113.2 ms | 10757.6 ms |
| XGo | Go | 19561.0 ms | 18367.7 ms | 1193.3 ms | 5761.4 ms |
| Aws_restjson | Go | 7993.4 ms | 7351.7 ms | 641.7 ms | 3234.4 ms |
| Gorm_schema | Go | 5912.6 ms | 5552.2 ms | 360.4 ms | 2287.1 ms |
| Uber_zap | Go | 5457.0 ms | 5043.6 ms | 413.5 ms | 2139.8 ms |
| K8s_workqueue | Go | 4892.8 ms | 4441.9 ms | 450.9 ms | 1745.3 ms |
| Toml | Go | 2088.7 ms | 1841.2 ms | 247.5 ms | 975.2 ms |
| Dustin_humanize | Go | 812.7 ms | 668.8 ms | 143.9 ms | 400.7 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTOGlobalDCEPlugin | 2338245.0 ms | 1282839.1 ms | 9 |
| LLGoFullLTONoGlobalDCE | 2281773.2 ms | 1305149.7 ms | 9 |
| LLGoFullLTOGlobalDCE | 2273755.7 ms | 1256298.9 ms | 9 |
| LLGoDeadcodeDrop | 2143989.3 ms | 698855.8 ms | 9 |
| LLGoNoLTO | 1954459.6 ms | 642807.9 ms | 9 |
| Go | 164833.7 ms | 50143.0 ms | 9 |

Dependency download details are in `download-timings.log`.
