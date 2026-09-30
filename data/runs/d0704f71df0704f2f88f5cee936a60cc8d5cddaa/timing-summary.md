## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTONoGlobalDCE | 539855.7 ms | 529426.0 ms | 10429.7 ms | 285857.1 ms |
| IXGo | LLGoFullLTOGlobalDCE | 523853.4 ms | 512577.0 ms | 11276.3 ms | 282897.0 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 508549.6 ms | 496736.5 ms | 11813.1 ms | 277836.6 ms |
| IXGo | LLGoNoLTO | 465769.6 ms | 455750.6 ms | 10019.0 ms | 139639.8 ms |
| IXGo | LLGoDeadcodeDrop | 417643.1 ms | 406321.8 ms | 11321.4 ms | 127464.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 246123.0 ms | 241487.9 ms | 4635.1 ms | 158235.6 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 244909.3 ms | 240328.3 ms | 4581.0 ms | 159208.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 244208.6 ms | 239382.6 ms | 4826.0 ms | 157294.2 ms |
| Aws_restjson | LLGoDeadcodeDrop | 206040.3 ms | 203057.4 ms | 2982.9 ms | 74433.5 ms |
| Aws_restjson | LLGoNoLTO | 205884.8 ms | 202922.8 ms | 2962.0 ms | 74898.4 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 202422.7 ms | 199247.6 ms | 3175.2 ms | 122981.1 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 196030.4 ms | 192850.6 ms | 3179.8 ms | 112488.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 191748.2 ms | 188610.1 ms | 3138.1 ms | 110712.0 ms |
| Etcdctl | LLGoDeadcodeDrop | 184532.7 ms | 180333.5 ms | 4199.2 ms | 64253.8 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 178593.6 ms | 175212.6 ms | 3381.0 ms | 127164.3 ms |
| Etcdctl | LLGoNoLTO | 177991.3 ms | 173672.4 ms | 4318.8 ms | 61401.8 ms |
| XGo | LLGoFullLTONoGlobalDCE | 177034.9 ms | 173733.7 ms | 3301.2 ms | 128753.3 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 175434.8 ms | 172635.7 ms | 2799.1 ms | 111157.5 ms |
| XGo | LLGoFullLTOGlobalDCE | 174760.8 ms | 171438.7 ms | 3322.1 ms | 125191.0 ms |
| Uber_zap | LLGoDeadcodeDrop | 168870.3 ms | 166387.6 ms | 2482.7 ms | 65382.6 ms |
| Uber_zap | LLGoNoLTO | 168110.2 ms | 165751.9 ms | 2358.3 ms | 65488.3 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 167076.5 ms | 164309.5 ms | 2767.1 ms | 107182.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 165972.8 ms | 163126.3 ms | 2846.5 ms | 105204.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 163132.5 ms | 160364.0 ms | 2768.5 ms | 99921.0 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 162817.1 ms | 160335.9 ms | 2481.3 ms | 63510.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 161353.5 ms | 158717.2 ms | 2636.3 ms | 98082.4 ms |
| K8s_workqueue | LLGoNoLTO | 160722.0 ms | 158199.3 ms | 2522.7 ms | 62810.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 152375.5 ms | 149727.1 ms | 2648.4 ms | 91031.2 ms |
| XGo | LLGoDeadcodeDrop | 104081.2 ms | 101105.2 ms | 2976.0 ms | 40981.2 ms |
| XGo | LLGoNoLTO | 99994.4 ms | 97271.6 ms | 2722.8 ms | 39705.9 ms |
| Gorm_schema | LLGoDeadcodeDrop | 87744.8 ms | 86188.3 ms | 1556.5 ms | 29439.7 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 87509.4 ms | 85732.9 ms | 1776.4 ms | 52523.0 ms |
| Gorm_schema | LLGoNoLTO | 86895.6 ms | 85319.4 ms | 1576.2 ms | 29069.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 86065.4 ms | 84358.3 ms | 1707.2 ms | 50965.4 ms |
| IXGo | Go | 85906.8 ms | 80509.0 ms | 5397.9 ms | 23974.4 ms |
| Toml | LLGoNoLTO | 82481.7 ms | 80842.8 ms | 1638.9 ms | 27156.6 ms |
| Toml | LLGoDeadcodeDrop | 81655.7 ms | 80041.0 ms | 1614.7 ms | 27089.8 ms |
| Toml | LLGoFullLTONoGlobalDCE | 80120.8 ms | 78380.2 ms | 1740.6 ms | 47145.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 75337.4 ms | 73735.9 ms | 1601.4 ms | 40289.8 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 73307.0 ms | 71591.6 ms | 1715.4 ms | 39532.1 ms |
| Toml | LLGoFullLTOGlobalDCE | 72754.4 ms | 71043.1 ms | 1711.3 ms | 39423.1 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 56487.7 ms | 55320.1 ms | 1167.5 ms | 35460.8 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 55844.7 ms | 54780.4 ms | 1064.3 ms | 20070.8 ms |
| Dustin_humanize | LLGoNoLTO | 55524.0 ms | 54438.0 ms | 1086.1 ms | 19968.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 47517.0 ms | 46384.9 ms | 1132.1 ms | 26131.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 46771.3 ms | 45626.6 ms | 1144.7 ms | 25824.3 ms |
| Etcdctl | Go | 35208.8 ms | 32902.8 ms | 2306.0 ms | 10714.5 ms |
| XGo | Go | 19633.8 ms | 18318.6 ms | 1315.2 ms | 5667.1 ms |
| Aws_restjson | Go | 8176.8 ms | 7433.5 ms | 743.3 ms | 3309.4 ms |
| Gorm_schema | Go | 5865.7 ms | 5457.2 ms | 408.6 ms | 2248.0 ms |
| Uber_zap | Go | 5376.6 ms | 4909.0 ms | 467.6 ms | 2167.9 ms |
| K8s_workqueue | Go | 4883.8 ms | 4404.6 ms | 479.2 ms | 1734.7 ms |
| Toml | Go | 2037.4 ms | 1789.6 ms | 247.8 ms | 960.4 ms |
| Dustin_humanize | Go | 906.7 ms | 656.3 ms | 250.4 ms | 698.8 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1730851.8 ms | 1050269.3 ms | 9 |
| LLGoFullLTOGlobalDCE | 1673549.6 ms | 999208.8 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1634904.7 ms | 969015.7 ms | 9 |
| LLGoNoLTO | 1503373.6 ms | 520140.0 ms | 9 |
| LLGoDeadcodeDrop | 1469229.9 ms | 512625.9 ms | 9 |
| Go | 167996.5 ms | 51475.1 ms | 9 |

Dependency download details are in `download-timings.log`.
