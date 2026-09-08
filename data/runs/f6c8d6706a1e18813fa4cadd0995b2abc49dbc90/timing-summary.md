## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 535593.9 ms | 530016.7 ms | 5577.2 ms | 352580.1 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 514522.8 ms | 509031.9 ms | 5490.8 ms | 339584.3 ms |
| IXGo | LLGoFullLTOGlobalDCE | 510184.6 ms | 504342.5 ms | 5842.1 ms | 327706.0 ms |
| IXGo | LLGoDeadcodeDrop | 356763.4 ms | 351584.3 ms | 5179.1 ms | 118048.8 ms |
| IXGo | LLGoNoLTO | 335244.2 ms | 330152.2 ms | 5092.0 ms | 110991.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 216219.5 ms | 211857.3 ms | 4362.2 ms | 133974.0 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 213847.1 ms | 209749.8 ms | 4097.2 ms | 134166.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 213136.5 ms | 208941.3 ms | 4195.2 ms | 133379.7 ms |
| Etcdctl | LLGoNoLTO | 152218.4 ms | 148480.9 ms | 3737.5 ms | 51310.2 ms |
| Etcdctl | LLGoDeadcodeDrop | 147459.6 ms | 143958.4 ms | 3501.2 ms | 49495.8 ms |
| XGo | LLGoFullLTONoGlobalDCE | 142944.9 ms | 140271.0 ms | 2673.9 ms | 102080.0 ms |
| XGo | LLGoFullLTOGlobalDCE | 141910.2 ms | 139243.5 ms | 2666.7 ms | 101113.6 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 138420.4 ms | 135837.9 ms | 2582.5 ms | 98191.9 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 110329.8 ms | 108453.2 ms | 1876.6 ms | 83389.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 101228.7 ms | 99236.8 ms | 1991.8 ms | 72856.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 100652.3 ms | 98740.7 ms | 1911.6 ms | 73013.4 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 85352.7 ms | 83862.6 ms | 1490.1 ms | 66578.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 81618.3 ms | 80144.2 ms | 1474.1 ms | 64440.9 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 81150.8 ms | 79346.6 ms | 1804.2 ms | 61001.8 ms |
| XGo | LLGoDeadcodeDrop | 81104.2 ms | 78833.6 ms | 2270.5 ms | 30845.7 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 81001.0 ms | 79542.7 ms | 1458.3 ms | 64610.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 79405.4 ms | 77935.9 ms | 1469.5 ms | 60143.8 ms |
| XGo | LLGoNoLTO | 78881.5 ms | 76666.5 ms | 2215.0 ms | 29980.1 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 71269.3 ms | 69804.5 ms | 1464.8 ms | 54140.5 ms |
| Aws_restjson | LLGoDeadcodeDrop | 65112.9 ms | 63348.4 ms | 1764.4 ms | 32104.5 ms |
| Aws_restjson | LLGoNoLTO | 62056.9 ms | 60297.5 ms | 1759.4 ms | 29604.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 50126.7 ms | 48923.4 ms | 1203.3 ms | 35497.7 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 48570.2 ms | 47457.6 ms | 1112.6 ms | 34835.6 ms |
| Uber_zap | LLGoDeadcodeDrop | 43610.6 ms | 42363.6 ms | 1247.0 ms | 20145.1 ms |
| Uber_zap | LLGoNoLTO | 42243.6 ms | 41073.2 ms | 1170.4 ms | 19045.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 42118.1 ms | 40958.0 ms | 1160.1 ms | 27302.6 ms |
| Toml | LLGoFullLTONoGlobalDCE | 39563.1 ms | 38641.2 ms | 921.9 ms | 31007.8 ms |
| K8s_workqueue | LLGoNoLTO | 37643.9 ms | 36441.1 ms | 1202.8 ms | 18219.4 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 37308.7 ms | 36082.6 ms | 1226.1 ms | 17927.5 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 34104.0 ms | 33226.8 ms | 877.2 ms | 24887.3 ms |
| Toml | LLGoFullLTOGlobalDCE | 33500.2 ms | 32624.7 ms | 875.5 ms | 24840.0 ms |
| IXGo | Go | 33495.5 ms | 31047.6 ms | 2448.0 ms | 9699.1 ms |
| Gorm_schema | LLGoDeadcodeDrop | 27942.5 ms | 26950.6 ms | 991.9 ms | 9357.1 ms |
| Gorm_schema | LLGoNoLTO | 27056.2 ms | 26115.3 ms | 940.9 ms | 9042.0 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 25244.1 ms | 24484.5 ms | 759.6 ms | 20158.8 ms |
| Etcdctl | Go | 25209.1 ms | 23508.5 ms | 1700.6 ms | 7586.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 19067.8 ms | 18400.5 ms | 667.3 ms | 13732.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 18556.0 ms | 17872.2 ms | 683.8 ms | 13408.7 ms |
| Toml | LLGoNoLTO | 17716.9 ms | 16923.7 ms | 793.2 ms | 6732.9 ms |
| Toml | LLGoDeadcodeDrop | 16908.9 ms | 16180.2 ms | 728.7 ms | 6697.2 ms |
| XGo | Go | 14376.0 ms | 13430.1 ms | 945.8 ms | 4264.1 ms |
| Dustin_humanize | LLGoNoLTO | 10202.3 ms | 9614.3 ms | 588.0 ms | 4362.7 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 9747.0 ms | 9065.3 ms | 681.7 ms | 4259.2 ms |
| Aws_restjson | Go | 5921.2 ms | 5363.7 ms | 557.4 ms | 2413.7 ms |
| Gorm_schema | Go | 4273.0 ms | 3966.4 ms | 306.6 ms | 1654.1 ms |
| Uber_zap | Go | 4007.0 ms | 3634.4 ms | 372.6 ms | 1582.1 ms |
| K8s_workqueue | Go | 3580.3 ms | 3173.2 ms | 407.1 ms | 1310.1 ms |
| Toml | Go | 1540.7 ms | 1351.2 ms | 189.5 ms | 716.7 ms |
| Dustin_humanize | Go | 625.8 ms | 498.7 ms | 127.1 ms | 299.8 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1261375.6 ms | 876411.3 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1236089.4 ms | 838071.9 ms | 9 |
| LLGoFullLTOGlobalDCE | 1232173.1 ms | 834138.0 ms | 9 |
| LLGoDeadcodeDrop | 785957.7 ms | 288880.8 ms | 9 |
| LLGoNoLTO | 763263.9 ms | 279287.9 ms | 9 |
| Go | 93028.6 ms | 29525.6 ms | 9 |

Dependency download details are in `download-timings.log`.
