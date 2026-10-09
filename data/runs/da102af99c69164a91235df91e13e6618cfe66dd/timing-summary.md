## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTONoGlobalDCE | 674284.3 ms | 663627.7 ms | 10656.6 ms | 344943.4 ms |
| IXGo | LLGoFullLTOGlobalDCE | 640540.9 ms | 628380.3 ms | 12160.7 ms | 327618.2 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 618765.6 ms | 608320.9 ms | 10444.7 ms | 327019.2 ms |
| IXGo | LLGoDeadcodeDrop | 527309.5 ms | 514113.0 ms | 13196.5 ms | 153581.6 ms |
| IXGo | LLGoNoLTO | 498207.7 ms | 490035.8 ms | 8171.8 ms | 142323.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 289449.0 ms | 284821.0 ms | 4628.0 ms | 179763.7 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 289362.6 ms | 284649.4 ms | 4713.2 ms | 181902.6 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 287393.7 ms | 283008.7 ms | 4384.9 ms | 178352.4 ms |
| Aws_restjson | LLGoNoLTO | 243201.8 ms | 239977.7 ms | 3224.1 ms | 83009.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 231089.6 ms | 227585.9 ms | 3503.7 ms | 131332.1 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 229064.2 ms | 225494.7 ms | 3569.5 ms | 137588.7 ms |
| Aws_restjson | LLGoDeadcodeDrop | 225614.7 ms | 222634.2 ms | 2980.6 ms | 78175.9 ms |
| Etcdctl | LLGoDeadcodeDrop | 225384.9 ms | 219581.4 ms | 5803.4 ms | 74164.3 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 218310.2 ms | 214850.0 ms | 3460.2 ms | 124925.1 ms |
| Etcdctl | LLGoNoLTO | 216718.5 ms | 212351.7 ms | 4366.8 ms | 70288.6 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 210689.3 ms | 207512.5 ms | 3176.8 ms | 147803.8 ms |
| XGo | LLGoFullLTONoGlobalDCE | 203643.9 ms | 200527.6 ms | 3116.3 ms | 144076.8 ms |
| XGo | LLGoFullLTOGlobalDCE | 202934.3 ms | 199711.1 ms | 3223.2 ms | 142268.9 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 198438.4 ms | 195235.5 ms | 3202.9 ms | 126694.1 ms |
| Uber_zap | LLGoDeadcodeDrop | 196872.4 ms | 194324.9 ms | 2547.4 ms | 72654.1 ms |
| Uber_zap | LLGoNoLTO | 195230.8 ms | 192413.3 ms | 2817.5 ms | 72087.3 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 191477.8 ms | 188533.7 ms | 2944.1 ms | 120618.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 189251.6 ms | 186139.8 ms | 3111.8 ms | 114340.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 186356.3 ms | 183150.1 ms | 3206.2 ms | 117515.8 ms |
| K8s_workqueue | LLGoNoLTO | 185657.5 ms | 182852.1 ms | 2805.4 ms | 68843.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 182293.3 ms | 179077.9 ms | 3215.4 ms | 108800.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 181708.3 ms | 178721.3 ms | 2987.0 ms | 109110.4 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 181191.7 ms | 178503.0 ms | 2688.7 ms | 67277.9 ms |
| XGo | LLGoDeadcodeDrop | 130449.7 ms | 127045.3 ms | 3404.4 ms | 47235.0 ms |
| XGo | LLGoNoLTO | 118617.2 ms | 116094.0 ms | 2523.2 ms | 42898.8 ms |
| Gorm_schema | LLGoDeadcodeDrop | 104618.0 ms | 102835.4 ms | 1782.6 ms | 34372.4 ms |
| Gorm_schema | LLGoNoLTO | 98405.0 ms | 96777.7 ms | 1627.4 ms | 32415.0 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 98023.9 ms | 96049.2 ms | 1974.7 ms | 58327.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 97900.5 ms | 95970.2 ms | 1930.3 ms | 57560.3 ms |
| Toml | LLGoDeadcodeDrop | 93877.2 ms | 92105.0 ms | 1772.2 ms | 30706.5 ms |
| Toml | LLGoNoLTO | 92060.5 ms | 90410.4 ms | 1650.1 ms | 30205.1 ms |
| Toml | LLGoFullLTONoGlobalDCE | 90117.4 ms | 88222.6 ms | 1894.9 ms | 53141.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 87016.1 ms | 85146.0 ms | 1870.1 ms | 45913.5 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 83266.8 ms | 81300.0 ms | 1966.7 ms | 45645.2 ms |
| IXGo | Go | 82906.8 ms | 77891.4 ms | 5015.4 ms | 23226.7 ms |
| Toml | LLGoFullLTOGlobalDCE | 82285.3 ms | 80418.1 ms | 1867.2 ms | 44727.8 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 68699.4 ms | 67218.0 ms | 1481.4 ms | 43086.7 ms |
| Dustin_humanize | LLGoNoLTO | 65290.1 ms | 64110.3 ms | 1179.8 ms | 23081.2 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 64366.7 ms | 63144.7 ms | 1222.0 ms | 22920.5 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 57130.0 ms | 55865.6 ms | 1264.5 ms | 31693.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 54665.7 ms | 53328.2 ms | 1337.5 ms | 29929.1 ms |
| Etcdctl | Go | 32765.9 ms | 30812.1 ms | 1953.8 ms | 9797.4 ms |
| XGo | Go | 18540.3 ms | 17501.9 ms | 1038.4 ms | 5407.6 ms |
| Aws_restjson | Go | 8352.2 ms | 7615.2 ms | 737.0 ms | 3551.4 ms |
| Gorm_schema | Go | 5660.1 ms | 5275.6 ms | 384.6 ms | 2136.3 ms |
| Uber_zap | Go | 5250.2 ms | 4871.2 ms | 379.0 ms | 2046.9 ms |
| K8s_workqueue | Go | 4763.1 ms | 4309.7 ms | 453.4 ms | 1687.8 ms |
| Toml | Go | 1985.9 ms | 1762.5 ms | 223.4 ms | 917.7 ms |
| Dustin_humanize | Go | 820.4 ms | 664.7 ms | 155.7 ms | 381.4 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2043111.9 ms | 1210379.2 ms | 9 |
| LLGoFullLTOGlobalDCE | 1954559.6 ms | 1133772.2 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1946487.0 ms | 1130548.0 ms | 9 |
| LLGoDeadcodeDrop | 1749684.8 ms | 581088.2 ms | 9 |
| LLGoNoLTO | 1713389.1 ms | 565153.1 ms | 9 |
| Go | 161045.0 ms | 49153.2 ms | 9 |

Dependency download details are in `download-timings.log`.
