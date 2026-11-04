## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 832016.6 ms | 811713.5 ms | 20303.1 ms | 528679.9 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 820369.4 ms | 799967.6 ms | 20401.7 ms | 532207.1 ms |
| IXGo | LLGoFullLTOGlobalDCE | 819101.7 ms | 798415.7 ms | 20686.1 ms | 524708.1 ms |
| IXGo | LLGoDeadcodeDrop | 476853.4 ms | 456487.8 ms | 20365.5 ms | 147742.5 ms |
| IXGo | LLGoNoLTO | 474323.8 ms | 457099.8 ms | 17224.0 ms | 146309.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 413597.7 ms | 403680.0 ms | 9917.7 ms | 306881.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 407563.4 ms | 398073.2 ms | 9490.2 ms | 300603.6 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 404397.4 ms | 395132.3 ms | 9265.1 ms | 301902.8 ms |
| XGo | LLGoFullLTONoGlobalDCE | 300623.9 ms | 294173.4 ms | 6450.4 ms | 243763.1 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 284026.4 ms | 278866.4 ms | 5160.0 ms | 198089.1 ms |
| XGo | LLGoFullLTOGlobalDCE | 261523.4 ms | 255297.6 ms | 6225.8 ms | 204242.7 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 261422.2 ms | 255199.3 ms | 6222.9 ms | 203096.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 255162.9 ms | 250191.3 ms | 4971.6 ms | 165948.1 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 248299.5 ms | 243324.8 ms | 4974.6 ms | 162373.5 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 230532.8 ms | 226274.5 ms | 4258.3 ms | 165822.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 227037.4 ms | 222647.7 ms | 4389.7 ms | 163659.4 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 220536.0 ms | 216145.0 ms | 4391.0 ms | 159821.9 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 210754.6 ms | 206608.4 ms | 4146.2 ms | 144527.3 ms |
| Etcdctl | LLGoDeadcodeDrop | 205039.4 ms | 196939.4 ms | 8100.0 ms | 70511.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 204638.5 ms | 200606.1 ms | 4032.4 ms | 140034.1 ms |
| Etcdctl | LLGoNoLTO | 204557.4 ms | 196681.9 ms | 7875.5 ms | 69793.4 ms |
| Aws_restjson | LLGoDeadcodeDrop | 194539.9 ms | 190024.7 ms | 4515.2 ms | 61655.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 194072.1 ms | 190022.7 ms | 4049.5 ms | 131295.0 ms |
| Aws_restjson | LLGoNoLTO | 193688.8 ms | 189601.7 ms | 4087.1 ms | 60754.7 ms |
| Uber_zap | LLGoNoLTO | 155653.5 ms | 152285.8 ms | 3367.7 ms | 50307.0 ms |
| Uber_zap | LLGoDeadcodeDrop | 154701.9 ms | 151159.7 ms | 3542.1 ms | 50314.2 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 148869.3 ms | 145248.6 ms | 3620.8 ms | 49008.7 ms |
| K8s_workqueue | LLGoNoLTO | 147253.6 ms | 143944.7 ms | 3308.9 ms | 47716.8 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 138218.2 ms | 135058.6 ms | 3159.6 ms | 99888.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 133852.7 ms | 130779.9 ms | 3072.9 ms | 95202.8 ms |
| Toml | LLGoFullLTONoGlobalDCE | 121644.3 ms | 118910.6 ms | 2733.7 ms | 86114.0 ms |
| XGo | LLGoNoLTO | 113227.3 ms | 108370.9 ms | 4856.4 ms | 41144.0 ms |
| XGo | LLGoDeadcodeDrop | 112602.8 ms | 107341.5 ms | 5261.2 ms | 40720.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 110714.3 ms | 107921.9 ms | 2792.4 ms | 71390.0 ms |
| Toml | LLGoFullLTOGlobalDCE | 106418.1 ms | 103822.1 ms | 2596.0 ms | 69683.8 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 106094.6 ms | 103523.0 ms | 2571.6 ms | 69524.4 ms |
| Gorm_schema | LLGoDeadcodeDrop | 96081.8 ms | 93359.9 ms | 2722.0 ms | 33523.1 ms |
| Gorm_schema | LLGoNoLTO | 95829.6 ms | 93274.3 ms | 2555.3 ms | 32816.7 ms |
| Toml | LLGoNoLTO | 91100.6 ms | 88885.2 ms | 2215.4 ms | 31051.4 ms |
| Toml | LLGoDeadcodeDrop | 89358.0 ms | 87062.5 ms | 2295.5 ms | 30749.7 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 87239.2 ms | 85305.8 ms | 1933.4 ms | 64153.7 ms |
| IXGo | Go | 86343.6 ms | 75059.1 ms | 11284.5 ms | 23627.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 70131.0 ms | 68307.9 ms | 1823.2 ms | 46225.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 69654.1 ms | 67770.2 ms | 1883.9 ms | 45920.6 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 62924.9 ms | 61133.1 ms | 1791.9 ms | 23477.8 ms |
| Dustin_humanize | LLGoNoLTO | 61440.0 ms | 59900.8 ms | 1539.3 ms | 22772.4 ms |
| Etcdctl | Go | 34363.2 ms | 30242.6 ms | 4120.6 ms | 11139.5 ms |
| XGo | Go | 19850.3 ms | 17503.6 ms | 2346.7 ms | 5754.8 ms |
| Aws_restjson | Go | 8480.2 ms | 7257.9 ms | 1222.3 ms | 4144.7 ms |
| Gorm_schema | Go | 5895.1 ms | 5170.0 ms | 725.1 ms | 2257.8 ms |
| Uber_zap | Go | 5594.1 ms | 4869.6 ms | 724.4 ms | 2682.1 ms |
| K8s_workqueue | Go | 4825.8 ms | 4159.4 ms | 666.4 ms | 1694.8 ms |
| Toml | Go | 2037.0 ms | 1747.9 ms | 289.1 ms | 925.5 ms |
| Dustin_humanize | Go | 800.1 ms | 639.6 ms | 160.5 ms | 382.4 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2607587.4 ms | 1851762.3 ms | 9 |
| LLGoFullLTOGlobalDCE | 2478565.8 ms | 1706732.9 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2453489.2 ms | 1667263.6 ms | 9 |
| LLGoDeadcodeDrop | 1540971.4 ms | 507703.7 ms | 9 |
| LLGoNoLTO | 1537074.8 ms | 502665.5 ms | 9 |
| Go | 168189.3 ms | 52609.4 ms | 9 |

Dependency download details are in `download-timings.log`.
