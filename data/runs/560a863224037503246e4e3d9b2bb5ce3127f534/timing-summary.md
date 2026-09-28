## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 366491.1 ms | 357021.3 ms | 9469.8 ms | 196217.9 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 362761.6 ms | 354153.9 ms | 8607.7 ms | 194391.2 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 356718.1 ms | 348503.8 ms | 8214.3 ms | 190737.6 ms |
| IXGo | LLGoNoLTO | 312595.8 ms | 305615.3 ms | 6980.6 ms | 96354.8 ms |
| IXGo | LLGoDeadcodeDrop | 278555.5 ms | 270467.1 ms | 8088.4 ms | 85763.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 176374.0 ms | 172905.8 ms | 3468.2 ms | 110369.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 173048.3 ms | 169465.5 ms | 3582.8 ms | 108604.7 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 164480.1 ms | 161288.3 ms | 3191.8 ms | 103729.3 ms |
| Etcdctl | LLGoDeadcodeDrop | 124357.6 ms | 121201.8 ms | 3155.8 ms | 42357.5 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 120098.4 ms | 117727.2 ms | 2371.2 ms | 83567.5 ms |
| XGo | LLGoFullLTOGlobalDCE | 118844.1 ms | 116400.7 ms | 2443.3 ms | 83622.5 ms |
| XGo | LLGoFullLTONoGlobalDCE | 117855.9 ms | 115574.3 ms | 2281.6 ms | 83276.9 ms |
| Etcdctl | LLGoNoLTO | 117402.3 ms | 114465.9 ms | 2936.4 ms | 39703.5 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 91401.7 ms | 89459.8 ms | 1941.9 ms | 68816.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 81591.1 ms | 79875.7 ms | 1715.4 ms | 58249.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 81347.9 ms | 79612.3 ms | 1735.6 ms | 57799.1 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 71597.4 ms | 70338.1 ms | 1259.3 ms | 55086.1 ms |
| XGo | LLGoDeadcodeDrop | 71403.8 ms | 69369.6 ms | 2034.2 ms | 27765.0 ms |
| XGo | LLGoNoLTO | 70209.9 ms | 68191.8 ms | 2018.1 ms | 27499.5 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 68268.9 ms | 67013.0 ms | 1255.8 ms | 53863.8 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 67783.5 ms | 66419.5 ms | 1364.0 ms | 53010.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 67309.2 ms | 65982.8 ms | 1326.4 ms | 49986.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 63657.5 ms | 62275.7 ms | 1381.9 ms | 46611.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 59835.6 ms | 58530.2 ms | 1305.3 ms | 44847.6 ms |
| Aws_restjson | LLGoDeadcodeDrop | 54831.4 ms | 53354.9 ms | 1476.5 ms | 27094.2 ms |
| Aws_restjson | LLGoNoLTO | 54748.8 ms | 53165.6 ms | 1583.1 ms | 27335.8 ms |
| IXGo | Go | 52056.5 ms | 47893.3 ms | 4163.2 ms | 14720.2 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 40511.3 ms | 39532.1 ms | 979.2 ms | 28116.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 40013.3 ms | 39031.4 ms | 981.9 ms | 27968.0 ms |
| Uber_zap | LLGoDeadcodeDrop | 38424.2 ms | 37246.0 ms | 1178.2 ms | 17356.6 ms |
| Uber_zap | LLGoNoLTO | 36752.5 ms | 35663.8 ms | 1088.7 ms | 16835.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 35246.6 ms | 34208.5 ms | 1038.1 ms | 22068.0 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 32571.9 ms | 31419.9 ms | 1152.0 ms | 15895.2 ms |
| K8s_workqueue | LLGoNoLTO | 32445.1 ms | 31286.6 ms | 1158.5 ms | 16139.0 ms |
| Toml | LLGoFullLTONoGlobalDCE | 30880.5 ms | 30046.7 ms | 833.9 ms | 23903.9 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 27688.7 ms | 26866.0 ms | 822.7 ms | 20146.6 ms |
| Toml | LLGoFullLTOGlobalDCE | 26161.8 ms | 25399.6 ms | 762.1 ms | 18740.9 ms |
| Gorm_schema | LLGoDeadcodeDrop | 25142.6 ms | 24183.2 ms | 959.4 ms | 8879.3 ms |
| Gorm_schema | LLGoNoLTO | 24631.2 ms | 23798.8 ms | 832.4 ms | 8481.3 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 22479.7 ms | 21866.7 ms | 613.0 ms | 17732.1 ms |
| Etcdctl | Go | 21879.0 ms | 20188.4 ms | 1690.6 ms | 6622.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 17486.6 ms | 16886.3 ms | 600.3 ms | 12620.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 16615.9 ms | 15982.2 ms | 633.7 ms | 11774.7 ms |
| Toml | LLGoDeadcodeDrop | 15113.7 ms | 14446.7 ms | 667.0 ms | 5609.5 ms |
| Toml | LLGoNoLTO | 15093.9 ms | 14405.2 ms | 688.7 ms | 5707.7 ms |
| XGo | Go | 12118.4 ms | 11248.3 ms | 870.1 ms | 3599.8 ms |
| Dustin_humanize | LLGoNoLTO | 8950.6 ms | 8381.9 ms | 568.7 ms | 3953.7 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 8532.1 ms | 7996.6 ms | 535.5 ms | 3996.8 ms |
| Aws_restjson | Go | 5009.6 ms | 4535.7 ms | 473.9 ms | 2113.8 ms |
| Gorm_schema | Go | 3570.9 ms | 3286.3 ms | 284.6 ms | 1360.1 ms |
| Uber_zap | Go | 3419.5 ms | 3086.6 ms | 332.9 ms | 1506.9 ms |
| K8s_workqueue | Go | 2897.3 ms | 2526.0 ms | 371.3 ms | 1435.0 ms |
| Toml | Go | 1374.8 ms | 1115.3 ms | 259.4 ms | 1053.6 ms |
| Dustin_humanize | Go | 506.0 ms | 395.4 ms | 110.7 ms | 245.0 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 964193.6 ms | 625262.5 ms | 9 |
| LLGoFullLTOGlobalDCE | 958403.1 ms | 607410.4 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 943952.1 ms | 593185.5 ms | 9 |
| LLGoNoLTO | 672830.1 ms | 242011.0 ms | 9 |
| LLGoDeadcodeDrop | 648932.8 ms | 234717.1 ms | 9 |
| Go | 102832.0 ms | 32656.8 ms | 9 |

Dependency download details are in `download-timings.log`.
