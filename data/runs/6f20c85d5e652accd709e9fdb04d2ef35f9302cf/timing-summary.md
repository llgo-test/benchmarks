## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 1012885.2 ms | 984998.7 ms | 27886.5 ms | 638225.1 ms |
| IXGo | LLGoFullLTOGlobalDCE | 982204.5 ms | 954232.4 ms | 27972.2 ms | 621517.6 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 957035.1 ms | 929865.4 ms | 27169.6 ms | 605286.1 ms |
| IXGo | LLGoDeadcodeDrop | 602259.1 ms | 574099.0 ms | 28160.1 ms | 185575.0 ms |
| IXGo | LLGoNoLTO | 554281.8 ms | 531368.1 ms | 22913.7 ms | 168504.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 524158.3 ms | 510998.6 ms | 13159.7 ms | 381930.8 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 517287.6 ms | 504185.2 ms | 13102.4 ms | 378626.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 510775.8 ms | 497699.4 ms | 13076.4 ms | 371493.1 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 396151.9 ms | 388172.1 ms | 7979.8 ms | 264332.5 ms |
| XGo | LLGoFullLTONoGlobalDCE | 377125.9 ms | 368011.5 ms | 9114.4 ms | 300681.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 373313.9 ms | 365848.0 ms | 7465.9 ms | 238896.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 371198.7 ms | 363766.1 ms | 7432.5 ms | 237022.5 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 339452.0 ms | 330700.5 ms | 8751.4 ms | 261882.1 ms |
| XGo | LLGoFullLTOGlobalDCE | 334640.4 ms | 325760.4 ms | 8880.1 ms | 256903.1 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 322644.9 ms | 315734.5 ms | 6910.4 ms | 224201.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 311981.0 ms | 304995.4 ms | 6985.6 ms | 217817.7 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 310994.2 ms | 304072.3 ms | 6921.8 ms | 217899.2 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 300567.8 ms | 293710.4 ms | 6857.4 ms | 202394.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 290436.3 ms | 283911.2 ms | 6525.1 ms | 190443.6 ms |
| Aws_restjson | LLGoNoLTO | 290301.6 ms | 284465.3 ms | 5836.3 ms | 88674.8 ms |
| Aws_restjson | LLGoDeadcodeDrop | 281394.0 ms | 275025.2 ms | 6368.8 ms | 87859.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 276385.9 ms | 269937.7 ms | 6448.2 ms | 181895.0 ms |
| Etcdctl | LLGoDeadcodeDrop | 264949.6 ms | 253761.7 ms | 11187.8 ms | 90614.8 ms |
| Etcdctl | LLGoNoLTO | 260444.8 ms | 250473.8 ms | 9971.0 ms | 87861.7 ms |
| Uber_zap | LLGoDeadcodeDrop | 223183.9 ms | 217444.3 ms | 5739.6 ms | 72153.5 ms |
| Uber_zap | LLGoNoLTO | 220996.1 ms | 215876.1 ms | 5120.0 ms | 69855.8 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 213570.8 ms | 208141.7 ms | 5429.1 ms | 69202.6 ms |
| K8s_workqueue | LLGoNoLTO | 213402.1 ms | 208068.4 ms | 5333.7 ms | 67781.6 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 169162.2 ms | 165055.5 ms | 4106.7 ms | 116338.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 164756.8 ms | 160553.4 ms | 4203.4 ms | 111990.4 ms |
| Toml | LLGoFullLTONoGlobalDCE | 152269.1 ms | 148466.0 ms | 3803.1 ms | 103507.3 ms |
| XGo | LLGoDeadcodeDrop | 147012.2 ms | 139281.6 ms | 7730.7 ms | 52747.4 ms |
| XGo | LLGoNoLTO | 143741.5 ms | 137176.5 ms | 6565.0 ms | 52361.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 139314.1 ms | 135434.4 ms | 3879.7 ms | 86330.4 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 139094.4 ms | 135322.2 ms | 3772.2 ms | 88768.9 ms |
| Toml | LLGoFullLTOGlobalDCE | 137245.8 ms | 133406.5 ms | 3839.3 ms | 86702.6 ms |
| Gorm_schema | LLGoNoLTO | 123939.8 ms | 120617.9 ms | 3321.8 ms | 42560.4 ms |
| Gorm_schema | LLGoDeadcodeDrop | 123308.5 ms | 119543.6 ms | 3764.9 ms | 42823.9 ms |
| Toml | LLGoDeadcodeDrop | 118169.1 ms | 114901.9 ms | 3267.2 ms | 40637.1 ms |
| Toml | LLGoNoLTO | 115268.4 ms | 112047.4 ms | 3221.0 ms | 39182.0 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 108459.6 ms | 105741.9 ms | 2717.7 ms | 76683.9 ms |
| IXGo | Go | 105499.4 ms | 89428.6 ms | 16070.8 ms | 29078.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 88735.0 ms | 86290.9 ms | 2444.1 ms | 56968.9 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 88468.9 ms | 86037.9 ms | 2430.9 ms | 55867.8 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 80919.2 ms | 78644.9 ms | 2274.3 ms | 29950.1 ms |
| Dustin_humanize | LLGoNoLTO | 77433.1 ms | 75312.9 ms | 2120.2 ms | 28653.1 ms |
| Etcdctl | Go | 41021.4 ms | 35373.6 ms | 5647.7 ms | 12438.5 ms |
| XGo | Go | 23054.3 ms | 19904.3 ms | 3150.0 ms | 6855.7 ms |
| Aws_restjson | Go | 10292.9 ms | 8634.3 ms | 1658.6 ms | 4477.7 ms |
| Gorm_schema | Go | 6792.2 ms | 5797.7 ms | 994.5 ms | 2695.7 ms |
| Uber_zap | Go | 6237.0 ms | 5310.8 ms | 926.2 ms | 2563.4 ms |
| K8s_workqueue | Go | 5737.5 ms | 4756.4 ms | 981.1 ms | 2541.1 ms |
| Toml | Go | 2416.0 ms | 2003.1 ms | 412.9 ms | 1167.4 ms |
| Dustin_humanize | Go | 961.5 ms | 738.0 ms | 223.5 ms | 472.7 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 3311130.4 ms | 2287555.8 ms | 9 |
| LLGoFullLTOGlobalDCE | 3204221.1 ms | 2164685.0 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 3181393.6 ms | 2122366.2 ms | 9 |
| LLGoDeadcodeDrop | 2054766.3 ms | 671563.8 ms | 9 |
| LLGoNoLTO | 1999809.1 ms | 645434.9 ms | 9 |
| Go | 202012.3 ms | 62290.8 ms | 9 |

Dependency download details are in `download-timings.log`.
