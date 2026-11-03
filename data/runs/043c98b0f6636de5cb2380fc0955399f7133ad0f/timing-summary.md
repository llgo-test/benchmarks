## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 723475.9 ms | 704699.5 ms | 18776.5 ms | 423323.9 ms |
| IXGo | LLGoFullLTOGlobalDCE | 613754.6 ms | 594400.8 ms | 19353.8 ms | 378507.0 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 590330.0 ms | 571065.1 ms | 19264.9 ms | 388131.5 ms |
| IXGo | LLGoDeadcodeDrop | 484237.0 ms | 465238.9 ms | 18998.1 ms | 156742.8 ms |
| IXGo | LLGoNoLTO | 319770.8 ms | 303994.8 ms | 15776.0 ms | 96887.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 296351.0 ms | 287239.7 ms | 9111.3 ms | 219035.3 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 294570.7 ms | 285407.2 ms | 9163.5 ms | 221028.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 266920.9 ms | 258627.0 ms | 8293.9 ms | 199430.6 ms |
| XGo | LLGoFullLTONoGlobalDCE | 238339.8 ms | 231969.0 ms | 6370.7 ms | 197802.1 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 203615.8 ms | 198671.8 ms | 4944.0 ms | 141586.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 187472.3 ms | 182805.5 ms | 4666.8 ms | 124090.5 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 178741.3 ms | 172843.4 ms | 5897.9 ms | 140277.5 ms |
| XGo | LLGoFullLTOGlobalDCE | 178701.9 ms | 173135.5 ms | 5566.4 ms | 140224.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 167689.0 ms | 163205.4 ms | 4483.6 ms | 111556.3 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 158968.3 ms | 154901.2 ms | 4067.1 ms | 116457.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 158966.6 ms | 154699.5 ms | 4267.0 ms | 108911.4 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 157389.4 ms | 153352.3 ms | 4037.1 ms | 114715.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 156368.3 ms | 152253.6 ms | 4114.7 ms | 115790.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 153583.1 ms | 149480.7 ms | 4102.4 ms | 105091.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 150019.1 ms | 145924.4 ms | 4094.7 ms | 104409.1 ms |
| Etcdctl | LLGoDeadcodeDrop | 149780.7 ms | 141903.7 ms | 7877.0 ms | 51782.1 ms |
| Etcdctl | LLGoNoLTO | 145671.5 ms | 138415.4 ms | 7256.1 ms | 49850.1 ms |
| Aws_restjson | LLGoDeadcodeDrop | 139172.4 ms | 134825.0 ms | 4347.4 ms | 44895.0 ms |
| Aws_restjson | LLGoNoLTO | 125100.2 ms | 121165.5 ms | 3934.6 ms | 39871.9 ms |
| K8s_workqueue | LLGoNoLTO | 111892.4 ms | 108540.3 ms | 3352.1 ms | 36736.1 ms |
| Uber_zap | LLGoDeadcodeDrop | 107900.6 ms | 104388.1 ms | 3512.5 ms | 35516.2 ms |
| Uber_zap | LLGoNoLTO | 103213.5 ms | 100135.1 ms | 3078.4 ms | 33662.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 101767.3 ms | 98818.8 ms | 2948.5 ms | 73628.0 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 97511.5 ms | 94166.0 ms | 3345.5 ms | 32500.9 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 95239.7 ms | 92415.0 ms | 2824.7 ms | 69363.7 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 89344.4 ms | 86463.1 ms | 2881.4 ms | 59055.7 ms |
| Toml | LLGoFullLTONoGlobalDCE | 81031.0 ms | 78497.0 ms | 2534.0 ms | 57865.7 ms |
| Toml | LLGoFullLTOGlobalDCE | 80177.7 ms | 77673.8 ms | 2503.9 ms | 53995.4 ms |
| XGo | LLGoDeadcodeDrop | 77170.1 ms | 72020.3 ms | 5149.8 ms | 28398.2 ms |
| XGo | LLGoNoLTO | 74511.0 ms | 70218.3 ms | 4292.8 ms | 27335.6 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 72949.9 ms | 70577.7 ms | 2372.2 ms | 48203.0 ms |
| Gorm_schema | LLGoDeadcodeDrop | 71164.5 ms | 68280.3 ms | 2884.2 ms | 25155.1 ms |
| Toml | LLGoNoLTO | 68622.6 ms | 66352.0 ms | 2270.7 ms | 24131.7 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 63895.0 ms | 61923.6 ms | 1971.3 ms | 47348.2 ms |
| IXGo | Go | 62234.7 ms | 51324.4 ms | 10910.3 ms | 18158.7 ms |
| Gorm_schema | LLGoNoLTO | 61214.5 ms | 58936.8 ms | 2277.7 ms | 21420.6 ms |
| Toml | LLGoDeadcodeDrop | 58776.6 ms | 56607.7 ms | 2168.9 ms | 20596.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 54293.2 ms | 52472.8 ms | 1820.4 ms | 36651.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 48294.8 ms | 46612.3 ms | 1682.5 ms | 32819.4 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 40274.9 ms | 38730.4 ms | 1544.5 ms | 15388.9 ms |
| Dustin_humanize | LLGoNoLTO | 39926.3 ms | 38553.9 ms | 1372.4 ms | 14981.0 ms |
| Etcdctl | Go | 25092.8 ms | 21246.4 ms | 3846.4 ms | 7672.7 ms |
| XGo | Go | 13708.2 ms | 11624.9 ms | 2083.3 ms | 4193.6 ms |
| Aws_restjson | Go | 6041.0 ms | 4913.9 ms | 1127.0 ms | 2577.4 ms |
| Gorm_schema | Go | 4092.1 ms | 3444.9 ms | 647.3 ms | 1635.5 ms |
| Uber_zap | Go | 3459.2 ms | 2886.4 ms | 572.7 ms | 1408.5 ms |
| K8s_workqueue | Go | 3277.4 ms | 2629.0 ms | 648.4 ms | 1186.3 ms |
| Toml | Go | 1718.4 ms | 1418.4 ms | 300.0 ms | 863.6 ms |
| Dustin_humanize | Go | 551.5 ms | 403.8 ms | 147.7 ms | 280.5 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTOGlobalDCEPlugin | 1915177.7 ms | 1264640.3 ms | 9 |
| LLGoFullLTONoGlobalDCE | 1883379.6 ms | 1354299.6 ms | 9 |
| LLGoFullLTOGlobalDCE | 1763693.7 ms | 1210361.1 ms | 9 |
| LLGoDeadcodeDrop | 1225988.3 ms | 410975.6 ms | 9 |
| LLGoNoLTO | 1049922.9 ms | 344876.7 ms | 9 |
| Go | 120175.2 ms | 37976.9 ms | 9 |

Dependency download details are in `download-timings.log`.
