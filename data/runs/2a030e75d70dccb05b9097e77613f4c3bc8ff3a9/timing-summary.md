## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 693462.6 ms | 669876.2 ms | 23586.4 ms | 459026.4 ms |
| IXGo | LLGoFullLTOGlobalDCE | 690576.6 ms | 666905.1 ms | 23671.5 ms | 462901.0 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 657023.5 ms | 633731.9 ms | 23291.6 ms | 438387.7 ms |
| IXGo | LLGoNoLTO | 419151.8 ms | 398911.4 ms | 20240.3 ms | 129649.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 383819.9 ms | 372354.3 ms | 11465.6 ms | 285312.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 372818.9 ms | 361572.4 ms | 11246.5 ms | 275101.4 ms |
| IXGo | LLGoDeadcodeDrop | 371637.0 ms | 348797.3 ms | 22839.7 ms | 123727.5 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 364782.1 ms | 353822.5 ms | 10959.5 ms | 273520.7 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 279892.7 ms | 273079.9 ms | 6812.8 ms | 189487.3 ms |
| XGo | LLGoFullLTONoGlobalDCE | 273702.6 ms | 265879.8 ms | 7822.8 ms | 222107.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 251348.1 ms | 244993.8 ms | 6354.3 ms | 162485.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 241727.9 ms | 235374.7 ms | 6353.2 ms | 158633.4 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 238219.5 ms | 230711.1 ms | 7508.5 ms | 186186.3 ms |
| XGo | LLGoFullLTOGlobalDCE | 238139.2 ms | 230745.0 ms | 7394.1 ms | 186526.4 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 228622.4 ms | 222828.1 ms | 5794.4 ms | 162034.7 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 224641.2 ms | 218753.3 ms | 5887.8 ms | 160084.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 222995.7 ms | 217198.7 ms | 5797.0 ms | 159220.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 216499.8 ms | 210595.7 ms | 5904.1 ms | 147670.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 210395.5 ms | 204965.5 ms | 5430.0 ms | 144372.5 ms |
| Aws_restjson | LLGoNoLTO | 198018.2 ms | 192663.5 ms | 5354.7 ms | 62414.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 197483.7 ms | 191848.1 ms | 5635.6 ms | 132650.7 ms |
| Aws_restjson | LLGoDeadcodeDrop | 183367.1 ms | 177970.8 ms | 5396.3 ms | 59601.0 ms |
| Etcdctl | LLGoDeadcodeDrop | 180389.2 ms | 171360.9 ms | 9028.3 ms | 64632.6 ms |
| Etcdctl | LLGoNoLTO | 179366.7 ms | 170822.1 ms | 8544.6 ms | 62643.3 ms |
| Uber_zap | LLGoNoLTO | 159698.2 ms | 155455.9 ms | 4242.3 ms | 51537.4 ms |
| Uber_zap | LLGoDeadcodeDrop | 156116.7 ms | 151510.2 ms | 4606.5 ms | 51948.9 ms |
| K8s_workqueue | LLGoNoLTO | 149142.9 ms | 144798.7 ms | 4344.1 ms | 48161.3 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 149111.4 ms | 144482.4 ms | 4629.0 ms | 50062.8 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 122085.0 ms | 118538.7 ms | 3546.3 ms | 85488.7 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 117696.7 ms | 114080.0 ms | 3616.7 ms | 81320.0 ms |
| Toml | LLGoFullLTONoGlobalDCE | 113532.5 ms | 110125.5 ms | 3406.9 ms | 78864.9 ms |
| XGo | LLGoNoLTO | 103685.4 ms | 98139.2 ms | 5546.2 ms | 39193.2 ms |
| XGo | LLGoDeadcodeDrop | 101311.7 ms | 94801.3 ms | 6510.4 ms | 37992.8 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 99207.1 ms | 96056.6 ms | 3150.4 ms | 63669.3 ms |
| Toml | LLGoFullLTOGlobalDCE | 98355.3 ms | 95099.4 ms | 3255.9 ms | 63415.7 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 97883.5 ms | 94583.3 ms | 3300.2 ms | 62033.2 ms |
| Gorm_schema | LLGoDeadcodeDrop | 85144.2 ms | 82001.2 ms | 3143.0 ms | 30467.5 ms |
| Gorm_schema | LLGoNoLTO | 82708.6 ms | 79918.6 ms | 2790.0 ms | 29047.1 ms |
| Toml | LLGoDeadcodeDrop | 82562.4 ms | 79732.1 ms | 2830.3 ms | 29146.6 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 79049.9 ms | 76722.4 ms | 2327.5 ms | 57100.2 ms |
| Toml | LLGoNoLTO | 78791.4 ms | 76226.1 ms | 2565.3 ms | 27430.4 ms |
| IXGo | Go | 73001.7 ms | 60273.0 ms | 12728.7 ms | 20258.9 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 64948.4 ms | 62756.0 ms | 2192.3 ms | 42060.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 62347.0 ms | 60176.3 ms | 2170.7 ms | 40400.8 ms |
| Dustin_humanize | LLGoNoLTO | 54654.5 ms | 52847.6 ms | 1807.0 ms | 20762.2 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 54003.3 ms | 52108.4 ms | 1894.9 ms | 20609.8 ms |
| Etcdctl | Go | 28809.1 ms | 24241.2 ms | 4567.9 ms | 8797.3 ms |
| XGo | Go | 16404.6 ms | 13804.9 ms | 2599.7 ms | 4829.7 ms |
| Aws_restjson | Go | 7009.1 ms | 5603.5 ms | 1405.6 ms | 3100.8 ms |
| Gorm_schema | Go | 5143.4 ms | 4245.8 ms | 897.5 ms | 2055.1 ms |
| Uber_zap | Go | 4605.8 ms | 3812.9 ms | 792.9 ms | 1914.1 ms |
| K8s_workqueue | Go | 4161.7 ms | 3353.1 ms | 808.6 ms | 1514.6 ms |
| Toml | Go | 1737.9 ms | 1380.2 ms | 357.7 ms | 838.6 ms |
| Dustin_humanize | Go | 690.4 ms | 510.6 ms | 179.8 ms | 346.2 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2343331.9 ms | 1667076.7 ms | 9 |
| LLGoFullLTOGlobalDCE | 2266053.7 ms | 1582102.6 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2231871.5 ms | 1530883.2 ms | 9 |
| LLGoNoLTO | 1425217.8 ms | 470838.3 ms | 9 |
| LLGoDeadcodeDrop | 1363643.0 ms | 468189.4 ms | 9 |
| Go | 141563.5 ms | 43655.2 ms | 9 |

Dependency download details are in `download-timings.log`.
