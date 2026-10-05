## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 717835.9 ms | 707501.1 ms | 10334.8 ms | 360484.4 ms |
| IXGo | LLGoFullLTOGlobalDCE | 710828.1 ms | 700329.1 ms | 10499.1 ms | 354808.2 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 687640.2 ms | 677500.0 ms | 10140.2 ms | 350192.8 ms |
| IXGo | LLGoDeadcodeDrop | 574436.9 ms | 560435.9 ms | 14001.1 ms | 170069.9 ms |
| IXGo | LLGoNoLTO | 549251.8 ms | 539901.1 ms | 9350.7 ms | 159337.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 347798.8 ms | 342614.6 ms | 5184.2 ms | 201480.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 344493.3 ms | 338947.5 ms | 5545.8 ms | 202416.2 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 343620.1 ms | 338688.2 ms | 4931.8 ms | 204222.3 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 282922.0 ms | 278936.3 ms | 3985.6 ms | 157422.0 ms |
| Aws_restjson | LLGoNoLTO | 277913.8 ms | 274427.5 ms | 3486.3 ms | 92826.5 ms |
| Aws_restjson | LLGoDeadcodeDrop | 272499.3 ms | 269191.0 ms | 3308.2 ms | 90966.3 ms |
| Etcdctl | LLGoDeadcodeDrop | 261648.0 ms | 256208.6 ms | 5439.4 ms | 86751.3 ms |
| Etcdctl | LLGoNoLTO | 259645.4 ms | 255386.7 ms | 4258.7 ms | 84904.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 258228.1 ms | 254318.4 ms | 3909.7 ms | 135908.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 256076.6 ms | 252318.7 ms | 3757.9 ms | 133784.5 ms |
| XGo | LLGoFullLTOGlobalDCE | 252414.4 ms | 248895.7 ms | 3518.7 ms | 164135.4 ms |
| XGo | LLGoFullLTONoGlobalDCE | 247416.4 ms | 243813.5 ms | 3602.8 ms | 162247.8 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 246381.0 ms | 242986.9 ms | 3394.1 ms | 160459.3 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 236027.1 ms | 232575.6 ms | 3451.5 ms | 134791.7 ms |
| Uber_zap | LLGoDeadcodeDrop | 229463.1 ms | 226610.7 ms | 2852.4 ms | 80531.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 228705.3 ms | 225371.2 ms | 3334.2 ms | 130504.4 ms |
| Uber_zap | LLGoNoLTO | 228634.7 ms | 225949.0 ms | 2685.7 ms | 80484.5 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 228279.7 ms | 225005.7 ms | 3274.0 ms | 131481.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 227749.7 ms | 224502.6 ms | 3247.1 ms | 125041.5 ms |
| K8s_workqueue | LLGoNoLTO | 224622.9 ms | 221507.0 ms | 3115.9 ms | 78803.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 222866.5 ms | 219531.1 ms | 3335.4 ms | 121653.5 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 219482.5 ms | 216503.6 ms | 2978.9 ms | 77404.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 214988.9 ms | 211578.4 ms | 3410.6 ms | 115219.9 ms |
| XGo | LLGoDeadcodeDrop | 163478.7 ms | 159829.9 ms | 3648.8 ms | 59394.6 ms |
| XGo | LLGoNoLTO | 160292.7 ms | 157582.0 ms | 2710.6 ms | 58134.3 ms |
| Gorm_schema | LLGoNoLTO | 110127.6 ms | 108343.8 ms | 1783.8 ms | 36489.2 ms |
| Gorm_schema | LLGoDeadcodeDrop | 109462.5 ms | 107727.1 ms | 1735.4 ms | 36339.1 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 109277.9 ms | 107206.1 ms | 2071.9 ms | 63611.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 107891.4 ms | 105857.5 ms | 2034.0 ms | 62001.6 ms |
| Toml | LLGoDeadcodeDrop | 105804.3 ms | 103860.7 ms | 1943.6 ms | 34985.4 ms |
| Toml | LLGoFullLTONoGlobalDCE | 102924.0 ms | 100840.0 ms | 2084.1 ms | 59037.8 ms |
| Toml | LLGoNoLTO | 101684.3 ms | 99852.7 ms | 1831.6 ms | 33436.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 96744.2 ms | 94757.7 ms | 1986.5 ms | 50816.7 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 93674.6 ms | 91675.0 ms | 1999.6 ms | 49053.7 ms |
| Toml | LLGoFullLTOGlobalDCE | 92944.5 ms | 90953.4 ms | 1991.1 ms | 49302.9 ms |
| IXGo | Go | 85203.3 ms | 80171.9 ms | 5031.4 ms | 23406.3 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 73115.3 ms | 71914.0 ms | 1201.3 ms | 26146.8 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 70850.7 ms | 69451.7 ms | 1399.0 ms | 42875.2 ms |
| Dustin_humanize | LLGoNoLTO | 70559.3 ms | 69314.8 ms | 1244.5 ms | 25188.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 62867.7 ms | 61488.7 ms | 1379.0 ms | 33809.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 61178.0 ms | 59826.7 ms | 1351.3 ms | 32801.2 ms |
| Etcdctl | Go | 34333.3 ms | 32218.3 ms | 2115.1 ms | 10369.9 ms |
| XGo | Go | 19532.6 ms | 18300.6 ms | 1232.0 ms | 5775.0 ms |
| Aws_restjson | Go | 8205.8 ms | 7499.4 ms | 706.4 ms | 3696.8 ms |
| Gorm_schema | Go | 5812.3 ms | 5401.5 ms | 410.8 ms | 2210.3 ms |
| Uber_zap | Go | 5407.9 ms | 4995.0 ms | 412.9 ms | 2106.5 ms |
| K8s_workqueue | Go | 4921.7 ms | 4390.6 ms | 531.0 ms | 1989.0 ms |
| Toml | Go | 2058.8 ms | 1829.5 ms | 229.3 ms | 937.9 ms |
| Dustin_humanize | Go | 819.1 ms | 665.0 ms | 154.1 ms | 387.4 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2308958.0 ms | 1305883.0 ms | 9 |
| LLGoFullLTOGlobalDCE | 2282393.5 ms | 1251481.2 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2261273.7 ms | 1232201.6 ms | 9 |
| LLGoDeadcodeDrop | 2009390.6 ms | 662589.5 ms | 9 |
| LLGoNoLTO | 1982732.4 ms | 649603.4 ms | 9 |
| Go | 166294.9 ms | 50879.1 ms | 9 |

Dependency download details are in `download-timings.log`.
