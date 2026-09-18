## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 595870.4 ms | 583572.0 ms | 12298.4 ms | 303614.5 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 546744.7 ms | 536071.9 ms | 10672.8 ms | 286285.4 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 545419.3 ms | 533597.2 ms | 11822.1 ms | 282595.0 ms |
| IXGo | LLGoDeadcodeDrop | 519171.6 ms | 509303.6 ms | 9868.0 ms | 152246.4 ms |
| IXGo | LLGoNoLTO | 444229.8 ms | 434949.7 ms | 9280.1 ms | 129828.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 300718.5 ms | 295625.4 ms | 5093.1 ms | 176040.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 292987.8 ms | 287777.1 ms | 5210.6 ms | 169224.7 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 292885.3 ms | 288168.4 ms | 4716.9 ms | 170065.1 ms |
| Etcdctl | LLGoDeadcodeDrop | 226198.9 ms | 221561.7 ms | 4637.1 ms | 73587.3 ms |
| Etcdctl | LLGoNoLTO | 225112.9 ms | 220779.1 ms | 4333.9 ms | 72625.0 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 188878.3 ms | 185431.5 ms | 3446.8 ms | 129907.7 ms |
| XGo | LLGoFullLTONoGlobalDCE | 185510.3 ms | 182281.9 ms | 3228.4 ms | 129055.5 ms |
| XGo | LLGoFullLTOGlobalDCE | 181208.8 ms | 177807.7 ms | 3401.1 ms | 124536.9 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 141428.6 ms | 139071.7 ms | 2356.9 ms | 102764.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 130893.8 ms | 128501.4 ms | 2392.5 ms | 90800.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 130538.9 ms | 128249.7 ms | 2289.2 ms | 90569.3 ms |
| XGo | LLGoDeadcodeDrop | 114317.6 ms | 111530.3 ms | 2787.2 ms | 42611.8 ms |
| XGo | LLGoNoLTO | 112011.6 ms | 109290.2 ms | 2721.4 ms | 41787.8 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 111348.8 ms | 109613.6 ms | 1735.2 ms | 84750.5 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 105839.9 ms | 103943.0 ms | 1896.9 ms | 82413.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 105489.0 ms | 103703.0 ms | 1786.1 ms | 81412.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 102498.9 ms | 100682.1 ms | 1816.7 ms | 74313.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 101113.2 ms | 99300.2 ms | 1813.0 ms | 74123.1 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 90252.4 ms | 88390.8 ms | 1861.6 ms | 66319.5 ms |
| Aws_restjson | LLGoDeadcodeDrop | 88829.5 ms | 86612.2 ms | 2217.4 ms | 41946.0 ms |
| Aws_restjson | LLGoNoLTO | 85663.1 ms | 83578.6 ms | 2084.5 ms | 39846.4 ms |
| IXGo | Go | 85408.0 ms | 80187.1 ms | 5221.0 ms | 23393.7 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 64989.0 ms | 63603.4 ms | 1385.5 ms | 44535.5 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 64717.7 ms | 63345.8 ms | 1371.9 ms | 44350.8 ms |
| Uber_zap | LLGoDeadcodeDrop | 59885.3 ms | 58398.8 ms | 1486.6 ms | 26935.9 ms |
| Uber_zap | LLGoNoLTO | 58316.4 ms | 56814.7 ms | 1501.6 ms | 25584.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 54547.5 ms | 53177.7 ms | 1369.8 ms | 32910.7 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 51957.4 ms | 50336.4 ms | 1621.1 ms | 24320.8 ms |
| K8s_workqueue | LLGoNoLTO | 51446.9 ms | 49876.1 ms | 1570.9 ms | 23924.6 ms |
| Toml | LLGoFullLTONoGlobalDCE | 50036.8 ms | 48913.9 ms | 1122.9 ms | 37735.8 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 42969.1 ms | 41843.4 ms | 1125.7 ms | 29791.9 ms |
| Toml | LLGoFullLTOGlobalDCE | 42137.9 ms | 41087.9 ms | 1050.0 ms | 29503.2 ms |
| Gorm_schema | LLGoDeadcodeDrop | 41113.8 ms | 39903.3 ms | 1210.5 ms | 13540.7 ms |
| Gorm_schema | LLGoNoLTO | 40248.2 ms | 39112.5 ms | 1135.7 ms | 13487.4 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 34980.9 ms | 34164.1 ms | 816.8 ms | 27575.0 ms |
| Etcdctl | Go | 34334.6 ms | 32064.0 ms | 2270.6 ms | 10717.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 26697.7 ms | 25863.6 ms | 834.2 ms | 19036.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 26430.0 ms | 25572.7 ms | 857.3 ms | 18838.1 ms |
| Toml | LLGoDeadcodeDrop | 25758.7 ms | 24695.7 ms | 1063.0 ms | 9459.8 ms |
| Toml | LLGoNoLTO | 24205.7 ms | 23252.6 ms | 953.1 ms | 9093.9 ms |
| XGo | Go | 19634.8 ms | 18228.2 ms | 1406.6 ms | 6028.4 ms |
| Dustin_humanize | LLGoNoLTO | 14261.3 ms | 13552.1 ms | 709.2 ms | 5951.6 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 13866.1 ms | 13117.7 ms | 748.4 ms | 6031.2 ms |
| Aws_restjson | Go | 8130.1 ms | 7443.6 ms | 686.5 ms | 3331.2 ms |
| Gorm_schema | Go | 5792.4 ms | 5389.4 ms | 403.0 ms | 2203.1 ms |
| Uber_zap | Go | 5343.4 ms | 4937.3 ms | 406.0 ms | 2116.5 ms |
| K8s_workqueue | Go | 4781.7 ms | 4344.1 ms | 437.6 ms | 1691.8 ms |
| Toml | Go | 2080.8 ms | 1838.9 ms | 241.9 ms | 960.2 ms |
| Dustin_humanize | Go | 822.7 ms | 669.5 ms | 153.1 ms | 397.2 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTOGlobalDCE | 1548850.7 ms | 943404.2 ms | 9 |
| LLGoFullLTONoGlobalDCE | 1533493.0 ms | 964995.9 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1474789.8 ms | 894668.0 ms | 9 |
| LLGoDeadcodeDrop | 1141099.0 ms | 390679.7 ms | 9 |
| LLGoNoLTO | 1055495.9 ms | 362129.9 ms | 9 |
| Go | 166328.4 ms | 50839.9 ms | 9 |

Dependency download details are in `download-timings.log`.
