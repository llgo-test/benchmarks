## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 656838.8 ms | 650046.1 ms | 6792.7 ms | 397247.7 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 619840.3 ms | 613664.7 ms | 6175.6 ms | 405299.6 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 605844.6 ms | 599403.3 ms | 6441.2 ms | 377838.4 ms |
| IXGo | LLGoDeadcodeDrop | 402959.6 ms | 397287.6 ms | 5672.0 ms | 135582.1 ms |
| IXGo | LLGoNoLTO | 388362.9 ms | 383112.1 ms | 5250.9 ms | 129678.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 269444.1 ms | 264932.2 ms | 4511.9 ms | 163210.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 269087.1 ms | 263864.1 ms | 5222.9 ms | 162970.4 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 265580.5 ms | 261171.2 ms | 4409.2 ms | 163691.4 ms |
| Etcdctl | LLGoDeadcodeDrop | 197904.6 ms | 194111.0 ms | 3793.6 ms | 65341.5 ms |
| Etcdctl | LLGoNoLTO | 195400.4 ms | 191455.7 ms | 3944.6 ms | 64066.7 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 182390.7 ms | 179218.5 ms | 3172.1 ms | 126825.3 ms |
| XGo | LLGoFullLTONoGlobalDCE | 179342.3 ms | 176192.7 ms | 3149.6 ms | 125453.2 ms |
| XGo | LLGoFullLTOGlobalDCE | 177098.2 ms | 174134.5 ms | 2963.6 ms | 124105.8 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 140180.3 ms | 137937.6 ms | 2242.8 ms | 102959.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 129290.4 ms | 127041.3 ms | 2249.1 ms | 90894.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 127995.4 ms | 125800.4 ms | 2195.1 ms | 90832.0 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 111752.2 ms | 110045.2 ms | 1707.0 ms | 85996.5 ms |
| XGo | LLGoDeadcodeDrop | 108350.6 ms | 105674.9 ms | 2675.7 ms | 40867.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 107520.6 ms | 105756.3 ms | 1764.4 ms | 84256.7 ms |
| XGo | LLGoNoLTO | 107012.1 ms | 104299.7 ms | 2712.4 ms | 40058.3 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 106801.3 ms | 105070.8 ms | 1730.5 ms | 83839.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 103905.9 ms | 102268.6 ms | 1637.3 ms | 77171.2 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 103034.1 ms | 101247.9 ms | 1786.3 ms | 76857.1 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 93521.5 ms | 91764.2 ms | 1757.3 ms | 70201.0 ms |
| Aws_restjson | LLGoDeadcodeDrop | 88884.2 ms | 86788.4 ms | 2095.8 ms | 41700.7 ms |
| Aws_restjson | LLGoNoLTO | 81866.6 ms | 79855.5 ms | 2011.1 ms | 37744.1 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 65303.8 ms | 64012.1 ms | 1291.7 ms | 45788.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 65025.5 ms | 63777.0 ms | 1248.5 ms | 45265.6 ms |
| Uber_zap | LLGoDeadcodeDrop | 59679.8 ms | 58183.5 ms | 1496.3 ms | 26442.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 56599.7 ms | 55322.6 ms | 1277.1 ms | 36521.0 ms |
| Uber_zap | LLGoNoLTO | 56532.6 ms | 55087.0 ms | 1445.6 ms | 24996.6 ms |
| Toml | LLGoFullLTONoGlobalDCE | 52159.6 ms | 51132.9 ms | 1026.7 ms | 40455.6 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 50982.7 ms | 49503.1 ms | 1479.6 ms | 23779.4 ms |
| K8s_workqueue | LLGoNoLTO | 49717.0 ms | 48301.0 ms | 1416.0 ms | 22912.1 ms |
| IXGo | Go | 47291.0 ms | 44232.3 ms | 3058.7 ms | 13594.7 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 45759.8 ms | 44739.6 ms | 1020.2 ms | 33169.9 ms |
| Toml | LLGoFullLTOGlobalDCE | 44909.5 ms | 43893.3 ms | 1016.2 ms | 32932.2 ms |
| Gorm_schema | LLGoDeadcodeDrop | 38233.3 ms | 37082.9 ms | 1150.4 ms | 12498.9 ms |
| Gorm_schema | LLGoNoLTO | 37413.3 ms | 36322.3 ms | 1091.0 ms | 12044.0 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 33041.0 ms | 32215.1 ms | 825.9 ms | 25898.3 ms |
| Etcdctl | Go | 32595.9 ms | 30715.2 ms | 1880.8 ms | 9957.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 25814.8 ms | 24979.6 ms | 835.1 ms | 18254.5 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 25622.7 ms | 24805.3 ms | 817.3 ms | 18135.7 ms |
| Toml | LLGoDeadcodeDrop | 24052.3 ms | 23032.0 ms | 1020.4 ms | 8962.7 ms |
| Toml | LLGoNoLTO | 22834.9 ms | 21971.4 ms | 863.5 ms | 8676.2 ms |
| XGo | Go | 18753.4 ms | 17612.5 ms | 1140.9 ms | 5551.7 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 13779.8 ms | 13032.6 ms | 747.1 ms | 5810.7 ms |
| Dustin_humanize | LLGoNoLTO | 12997.5 ms | 12302.1 ms | 695.4 ms | 5447.9 ms |
| Aws_restjson | Go | 7893.1 ms | 7197.3 ms | 695.8 ms | 3215.8 ms |
| Gorm_schema | Go | 5671.5 ms | 5294.2 ms | 377.3 ms | 2152.1 ms |
| Uber_zap | Go | 5195.5 ms | 4780.9 ms | 414.6 ms | 2002.2 ms |
| K8s_workqueue | Go | 4699.7 ms | 4222.8 ms | 476.9 ms | 1927.6 ms |
| Toml | Go | 1996.4 ms | 1785.2 ms | 211.2 ms | 907.8 ms |
| Dustin_humanize | Go | 797.9 ms | 662.4 ms | 135.5 ms | 365.3 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTOGlobalDCE | 1577132.0 ms | 1032603.3 ms | 9 |
| LLGoFullLTONoGlobalDCE | 1574001.3 ms | 1079381.8 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1512571.4 ms | 994086.2 ms | 9 |
| LLGoDeadcodeDrop | 984826.9 ms | 360986.8 ms | 9 |
| LLGoNoLTO | 952137.4 ms | 345624.1 ms | 9 |
| Go | 124894.3 ms | 39674.3 ms | 9 |

Dependency download details are in `download-timings.log`.
