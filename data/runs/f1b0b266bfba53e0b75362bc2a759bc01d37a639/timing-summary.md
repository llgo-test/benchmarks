## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 930110.5 ms | 903755.9 ms | 26354.5 ms | 580070.4 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 844783.8 ms | 818752.2 ms | 26031.7 ms | 531665.4 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 832083.6 ms | 805981.0 ms | 26102.7 ms | 533382.4 ms |
| IXGo | LLGoNoLTO | 557095.1 ms | 533886.0 ms | 23209.1 ms | 171772.9 ms |
| IXGo | LLGoDeadcodeDrop | 502406.6 ms | 475621.3 ms | 26785.3 ms | 161087.6 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 473665.8 ms | 461034.9 ms | 12630.9 ms | 343863.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 457435.0 ms | 445129.6 ms | 12305.4 ms | 334667.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 438536.4 ms | 426426.3 ms | 12110.2 ms | 314660.7 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 334987.4 ms | 328110.5 ms | 6876.9 ms | 222229.1 ms |
| XGo | LLGoFullLTONoGlobalDCE | 320809.2 ms | 312226.9 ms | 8582.3 ms | 251686.6 ms |
| XGo | LLGoFullLTOGlobalDCE | 311752.4 ms | 303165.7 ms | 8586.6 ms | 237638.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 307579.6 ms | 300839.6 ms | 6740.0 ms | 186171.3 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 303343.5 ms | 296896.0 ms | 6447.6 ms | 189362.2 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 301068.0 ms | 292970.8 ms | 8097.2 ms | 227055.1 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 276133.9 ms | 269904.9 ms | 6228.9 ms | 188039.7 ms |
| Aws_restjson | LLGoDeadcodeDrop | 263947.6 ms | 257049.3 ms | 6898.3 ms | 84157.3 ms |
| Aws_restjson | LLGoNoLTO | 262411.8 ms | 256226.5 ms | 6185.3 ms | 82146.6 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 261965.2 ms | 255989.3 ms | 5975.9 ms | 183706.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 258745.2 ms | 252926.1 ms | 5819.1 ms | 175519.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 248869.6 ms | 242987.1 ms | 5882.5 ms | 171317.7 ms |
| Etcdctl | LLGoNoLTO | 248291.9 ms | 238323.9 ms | 9968.0 ms | 84847.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 246882.4 ms | 241065.9 ms | 5816.5 ms | 161952.6 ms |
| Etcdctl | LLGoDeadcodeDrop | 244025.0 ms | 233242.6 ms | 10782.5 ms | 84214.5 ms |
| Uber_zap | LLGoNoLTO | 223461.3 ms | 218608.7 ms | 4852.6 ms | 71052.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 211378.1 ms | 205922.6 ms | 5455.6 ms | 135297.1 ms |
| Uber_zap | LLGoDeadcodeDrop | 210746.6 ms | 205401.7 ms | 5344.9 ms | 68288.1 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 205037.1 ms | 199474.0 ms | 5563.1 ms | 67141.1 ms |
| K8s_workqueue | LLGoNoLTO | 201887.3 ms | 196726.3 ms | 5161.0 ms | 64364.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 168093.8 ms | 163809.2 ms | 4284.6 ms | 114672.2 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 156683.9 ms | 152640.9 ms | 4043.0 ms | 106671.3 ms |
| XGo | LLGoNoLTO | 153476.0 ms | 146835.0 ms | 6641.0 ms | 55598.9 ms |
| Toml | LLGoFullLTONoGlobalDCE | 147968.2 ms | 144017.6 ms | 3950.5 ms | 98878.3 ms |
| XGo | LLGoDeadcodeDrop | 147089.4 ms | 139558.8 ms | 7530.6 ms | 53318.2 ms |
| Toml | LLGoFullLTOGlobalDCE | 125253.1 ms | 121633.9 ms | 3619.3 ms | 78567.2 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 124632.4 ms | 121151.3 ms | 3481.0 ms | 77864.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 123756.9 ms | 120136.9 ms | 3619.9 ms | 75506.6 ms |
| Toml | LLGoDeadcodeDrop | 119227.9 ms | 115708.2 ms | 3519.7 ms | 41102.6 ms |
| Gorm_schema | LLGoNoLTO | 118651.2 ms | 115299.8 ms | 3351.4 ms | 40808.3 ms |
| Gorm_schema | LLGoDeadcodeDrop | 116708.9 ms | 113122.6 ms | 3586.3 ms | 40535.1 ms |
| Toml | LLGoNoLTO | 110235.1 ms | 107410.8 ms | 2824.3 ms | 37413.2 ms |
| IXGo | Go | 97151.8 ms | 82375.1 ms | 14776.7 ms | 26526.5 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 96994.9 ms | 94475.6 ms | 2519.3 ms | 67922.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 82712.8 ms | 80267.7 ms | 2445.1 ms | 53104.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 78892.7 ms | 76600.6 ms | 2292.1 ms | 49273.5 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 77653.1 ms | 75276.5 ms | 2376.6 ms | 28941.7 ms |
| Dustin_humanize | LLGoNoLTO | 77334.1 ms | 75101.4 ms | 2232.7 ms | 28791.4 ms |
| Etcdctl | Go | 39626.5 ms | 34134.2 ms | 5492.3 ms | 12023.3 ms |
| XGo | Go | 21554.4 ms | 18468.0 ms | 3086.3 ms | 6365.7 ms |
| Aws_restjson | Go | 9119.4 ms | 7515.0 ms | 1604.4 ms | 4095.1 ms |
| Gorm_schema | Go | 6474.8 ms | 5519.0 ms | 955.8 ms | 2523.9 ms |
| Uber_zap | Go | 6114.3 ms | 5238.9 ms | 875.4 ms | 2474.0 ms |
| K8s_workqueue | Go | 5565.5 ms | 4631.6 ms | 933.9 ms | 2008.3 ms |
| Toml | Go | 2389.1 ms | 1982.4 ms | 406.7 ms | 1161.3 ms |
| Dustin_humanize | Go | 888.9 ms | 665.4 ms | 223.5 ms | 429.0 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2913992.3 ms | 1994662.6 ms | 9 |
| LLGoFullLTOGlobalDCE | 2886315.9 ms | 1934919.6 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2664810.2 ms | 1761163.3 ms | 9 |
| LLGoNoLTO | 1952843.9 ms | 636795.1 ms | 9 |
| LLGoDeadcodeDrop | 1886842.4 ms | 628786.2 ms | 9 |
| Go | 188884.6 ms | 57607.2 ms | 9 |

Dependency download details are in `download-timings.log`.
