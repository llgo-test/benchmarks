## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 702753.6 ms | 685426.6 ms | 17327.0 ms | 473102.0 ms |
| IXGo | LLGoFullLTOGlobalDCE | 690690.4 ms | 673444.9 ms | 17245.6 ms | 462932.4 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 678654.4 ms | 660926.9 ms | 17727.5 ms | 457300.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 374019.3 ms | 366070.2 ms | 7949.1 ms | 281897.2 ms |
| IXGo | LLGoDeadcodeDrop | 373930.6 ms | 356617.3 ms | 17313.4 ms | 121193.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 372896.7 ms | 364903.4 ms | 7993.3 ms | 280604.9 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 369120.0 ms | 361251.1 ms | 7868.9 ms | 278704.5 ms |
| IXGo | LLGoNoLTO | 362058.6 ms | 347265.9 ms | 14792.7 ms | 113111.2 ms |
| XGo | LLGoFullLTONoGlobalDCE | 278575.9 ms | 273021.4 ms | 5554.5 ms | 227540.7 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 275873.4 ms | 271113.9 ms | 4759.5 ms | 189762.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 255463.8 ms | 250757.0 ms | 4706.8 ms | 166923.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 252259.3 ms | 247479.6 ms | 4779.7 ms | 163832.9 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 245889.4 ms | 240733.3 ms | 5156.1 ms | 195149.1 ms |
| XGo | LLGoFullLTOGlobalDCE | 245224.6 ms | 239844.9 ms | 5379.7 ms | 194013.5 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 230056.3 ms | 225818.8 ms | 4237.5 ms | 165869.0 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 224455.6 ms | 220273.3 ms | 4182.3 ms | 162806.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 220972.9 ms | 216838.1 ms | 4134.8 ms | 159958.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 213240.2 ms | 209108.8 ms | 4131.3 ms | 148537.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 205768.1 ms | 201745.6 ms | 4022.6 ms | 141515.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 190454.1 ms | 186587.0 ms | 3867.1 ms | 129983.8 ms |
| Aws_restjson | LLGoNoLTO | 186222.8 ms | 182504.5 ms | 3718.2 ms | 58101.2 ms |
| Aws_restjson | LLGoDeadcodeDrop | 181005.6 ms | 177221.3 ms | 3784.4 ms | 58323.5 ms |
| Etcdctl | LLGoDeadcodeDrop | 178559.5 ms | 171849.0 ms | 6710.6 ms | 62746.8 ms |
| Etcdctl | LLGoNoLTO | 175827.5 ms | 169634.2 ms | 6193.3 ms | 60747.7 ms |
| Uber_zap | LLGoNoLTO | 147149.0 ms | 144015.6 ms | 3133.5 ms | 47477.4 ms |
| Uber_zap | LLGoDeadcodeDrop | 146302.8 ms | 143077.6 ms | 3225.2 ms | 48611.0 ms |
| K8s_workqueue | LLGoNoLTO | 142402.6 ms | 139071.6 ms | 3331.0 ms | 45776.9 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 140684.0 ms | 137353.8 ms | 3330.2 ms | 47174.7 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 113956.9 ms | 111548.8 ms | 2408.0 ms | 79998.7 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 113631.0 ms | 111138.0 ms | 2493.0 ms | 80337.3 ms |
| Toml | LLGoFullLTONoGlobalDCE | 107192.1 ms | 104803.7 ms | 2388.4 ms | 75324.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 99067.4 ms | 96620.6 ms | 2446.8 ms | 63456.7 ms |
| XGo | LLGoNoLTO | 97476.6 ms | 93473.4 ms | 4003.2 ms | 36396.3 ms |
| XGo | LLGoDeadcodeDrop | 97385.0 ms | 93169.6 ms | 4215.4 ms | 36033.8 ms |
| Toml | LLGoFullLTOGlobalDCE | 96296.3 ms | 93985.7 ms | 2310.6 ms | 63261.5 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 92908.1 ms | 90622.4 ms | 2285.7 ms | 61327.4 ms |
| Gorm_schema | LLGoDeadcodeDrop | 80845.5 ms | 78561.0 ms | 2284.5 ms | 28800.1 ms |
| Gorm_schema | LLGoNoLTO | 80180.3 ms | 78067.9 ms | 2112.4 ms | 28053.5 ms |
| Toml | LLGoDeadcodeDrop | 76329.2 ms | 74294.0 ms | 2035.2 ms | 26897.5 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 75621.6 ms | 73902.2 ms | 1719.4 ms | 55207.4 ms |
| Toml | LLGoNoLTO | 75399.9 ms | 73555.5 ms | 1844.4 ms | 26137.4 ms |
| IXGo | Go | 63773.7 ms | 55649.7 ms | 8124.0 ms | 17714.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 61161.7 ms | 59668.4 ms | 1493.3 ms | 40022.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 60796.8 ms | 59261.1 ms | 1535.7 ms | 39969.8 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 52193.8 ms | 50788.9 ms | 1405.0 ms | 19755.9 ms |
| Dustin_humanize | LLGoNoLTO | 51987.2 ms | 50656.7 ms | 1330.5 ms | 19712.2 ms |
| Etcdctl | Go | 25903.4 ms | 22950.9 ms | 2952.5 ms | 7832.5 ms |
| XGo | Go | 14368.4 ms | 12735.6 ms | 1632.9 ms | 4378.7 ms |
| Aws_restjson | Go | 6343.7 ms | 5448.9 ms | 894.8 ms | 2637.6 ms |
| Gorm_schema | Go | 4524.4 ms | 3955.4 ms | 569.0 ms | 1767.0 ms |
| Uber_zap | Go | 4192.4 ms | 3695.1 ms | 497.3 ms | 1689.6 ms |
| K8s_workqueue | Go | 3522.1 ms | 3065.9 ms | 456.2 ms | 1262.6 ms |
| Toml | Go | 1602.9 ms | 1392.1 ms | 210.8 ms | 760.9 ms |
| Dustin_humanize | Go | 635.4 ms | 501.0 ms | 134.4 ms | 348.6 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2353180.4 ms | 1692853.2 ms | 9 |
| LLGoFullLTOGlobalDCE | 2267456.7 ms | 1594401.7 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2226362.8 ms | 1552086.2 ms | 9 |
| LLGoDeadcodeDrop | 1327236.1 ms | 449536.6 ms | 9 |
| LLGoNoLTO | 1318704.5 ms | 435513.7 ms | 9 |
| Go | 124866.5 ms | 38391.9 ms | 9 |

Dependency download details are in `download-timings.log`.
