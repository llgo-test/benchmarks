## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 944514.2 ms | 916826.0 ms | 27688.2 ms | 617071.2 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 928299.3 ms | 900552.1 ms | 27747.1 ms | 585044.4 ms |
| IXGo | LLGoFullLTOGlobalDCE | 907918.7 ms | 880995.1 ms | 26923.6 ms | 603013.2 ms |
| IXGo | LLGoDeadcodeDrop | 587005.9 ms | 558995.7 ms | 28010.1 ms | 186889.0 ms |
| IXGo | LLGoNoLTO | 545808.3 ms | 522345.2 ms | 23463.1 ms | 169028.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 530007.8 ms | 516491.5 ms | 13516.3 ms | 389717.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 512442.5 ms | 498921.9 ms | 13520.6 ms | 372508.9 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 469322.9 ms | 456719.6 ms | 12603.3 ms | 343481.6 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 352091.7 ms | 344653.9 ms | 7437.8 ms | 235244.4 ms |
| XGo | LLGoFullLTONoGlobalDCE | 345270.8 ms | 336443.8 ms | 8827.0 ms | 274705.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 330563.6 ms | 323205.8 ms | 7357.9 ms | 208291.9 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 320095.8 ms | 313055.4 ms | 7040.4 ms | 227416.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 317187.6 ms | 309785.2 ms | 7402.4 ms | 203113.3 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 315077.5 ms | 306449.7 ms | 8627.8 ms | 241629.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 307743.7 ms | 301072.1 ms | 6671.5 ms | 214405.8 ms |
| XGo | LLGoFullLTOGlobalDCE | 307109.7 ms | 298632.0 ms | 8477.6 ms | 235890.0 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 298227.0 ms | 291528.5 ms | 6698.4 ms | 206264.5 ms |
| Aws_restjson | LLGoNoLTO | 285923.9 ms | 279854.3 ms | 6069.6 ms | 88859.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 283262.7 ms | 277006.5 ms | 6256.3 ms | 188786.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 275805.9 ms | 269562.1 ms | 6243.7 ms | 183539.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 272061.6 ms | 265638.8 ms | 6422.7 ms | 178653.7 ms |
| Etcdctl | LLGoDeadcodeDrop | 260589.7 ms | 249484.2 ms | 11105.5 ms | 90544.8 ms |
| Aws_restjson | LLGoDeadcodeDrop | 255497.0 ms | 249177.2 ms | 6319.7 ms | 81579.5 ms |
| Etcdctl | LLGoNoLTO | 245305.9 ms | 235395.4 ms | 9910.4 ms | 84479.4 ms |
| Uber_zap | LLGoNoLTO | 226522.2 ms | 221454.4 ms | 5067.8 ms | 72081.5 ms |
| Uber_zap | LLGoDeadcodeDrop | 216628.8 ms | 211095.8 ms | 5533.0 ms | 71290.6 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 214186.8 ms | 208764.3 ms | 5422.5 ms | 70319.2 ms |
| K8s_workqueue | LLGoNoLTO | 206566.5 ms | 201668.8 ms | 4897.7 ms | 65903.7 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 159656.4 ms | 155551.5 ms | 4105.0 ms | 109133.1 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 152603.7 ms | 148766.8 ms | 3836.9 ms | 102447.5 ms |
| XGo | LLGoDeadcodeDrop | 148794.4 ms | 140818.3 ms | 7976.2 ms | 54386.7 ms |
| Toml | LLGoFullLTONoGlobalDCE | 143888.7 ms | 140076.2 ms | 3812.5 ms | 96782.5 ms |
| XGo | LLGoNoLTO | 138829.9 ms | 132432.8 ms | 6397.2 ms | 51503.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 137845.8 ms | 133909.8 ms | 3936.0 ms | 83822.4 ms |
| Toml | LLGoFullLTOGlobalDCE | 137192.6 ms | 133479.0 ms | 3713.6 ms | 86718.9 ms |
| Gorm_schema | LLGoNoLTO | 130557.4 ms | 126984.8 ms | 3572.6 ms | 45386.7 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 127928.7 ms | 124269.7 ms | 3659.1 ms | 80039.0 ms |
| Gorm_schema | LLGoDeadcodeDrop | 123381.2 ms | 119523.5 ms | 3857.7 ms | 43321.5 ms |
| Toml | LLGoDeadcodeDrop | 115803.4 ms | 112520.4 ms | 3283.0 ms | 40342.7 ms |
| Toml | LLGoNoLTO | 111461.2 ms | 108332.9 ms | 3128.3 ms | 38201.5 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 102769.6 ms | 100237.5 ms | 2532.1 ms | 72965.5 ms |
| IXGo | Go | 100515.0 ms | 85045.1 ms | 15469.9 ms | 27491.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 91135.5 ms | 88580.0 ms | 2555.5 ms | 57673.9 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 81431.5 ms | 79087.1 ms | 2344.4 ms | 51193.0 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 78630.5 ms | 76413.6 ms | 2216.9 ms | 29306.8 ms |
| Dustin_humanize | LLGoNoLTO | 78111.3 ms | 76006.5 ms | 2104.8 ms | 29056.6 ms |
| Etcdctl | Go | 38409.5 ms | 32970.5 ms | 5438.9 ms | 11595.1 ms |
| XGo | Go | 22987.6 ms | 19642.4 ms | 3345.2 ms | 6835.8 ms |
| Aws_restjson | Go | 9820.6 ms | 8227.9 ms | 1592.7 ms | 4190.8 ms |
| Gorm_schema | Go | 6642.9 ms | 5631.7 ms | 1011.1 ms | 2606.1 ms |
| Uber_zap | Go | 6344.3 ms | 5405.9 ms | 938.4 ms | 2586.0 ms |
| K8s_workqueue | Go | 5743.2 ms | 4750.6 ms | 992.6 ms | 2121.6 ms |
| Toml | Go | 2365.4 ms | 1934.9 ms | 430.5 ms | 1125.5 ms |
| Dustin_humanize | Go | 947.8 ms | 699.9 ms | 247.9 ms | 557.8 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 3119622.2 ms | 2151038.3 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 3022693.5 ms | 2039204.0 ms | 9 |
| LLGoFullLTOGlobalDCE | 3009139.7 ms | 2059311.0 ms | 9 |
| LLGoDeadcodeDrop | 2000517.7 ms | 667980.9 ms | 9 |
| LLGoNoLTO | 1969086.6 ms | 644500.9 ms | 9 |
| Go | 193776.3 ms | 59110.3 ms | 9 |

Dependency download details are in `download-timings.log`.
