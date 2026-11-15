## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 685623.4 ms | 668685.8 ms | 16937.6 ms | 462894.5 ms |
| IXGo | LLGoFullLTOGlobalDCE | 668300.7 ms | 651155.3 ms | 17145.4 ms | 449643.5 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 655231.5 ms | 638290.7 ms | 16940.8 ms | 440917.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 365918.3 ms | 358115.8 ms | 7802.6 ms | 275015.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 364961.1 ms | 357044.1 ms | 7917.0 ms | 272876.1 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 362389.6 ms | 354480.6 ms | 7909.0 ms | 273564.2 ms |
| IXGo | LLGoDeadcodeDrop | 359323.0 ms | 342947.0 ms | 16376.0 ms | 116442.5 ms |
| IXGo | LLGoNoLTO | 354037.4 ms | 340199.1 ms | 13838.4 ms | 110387.6 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 279061.2 ms | 274047.1 ms | 5014.2 ms | 192890.7 ms |
| XGo | LLGoFullLTONoGlobalDCE | 277702.6 ms | 272305.1 ms | 5397.5 ms | 227369.9 ms |
| XGo | LLGoFullLTOGlobalDCE | 241934.7 ms | 236640.4 ms | 5294.3 ms | 190713.1 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 240800.1 ms | 236291.2 ms | 4508.9 ms | 158200.8 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 235929.7 ms | 230755.1 ms | 5174.5 ms | 185955.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 235655.5 ms | 231108.3 ms | 4547.1 ms | 156134.8 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 224059.5 ms | 219840.9 ms | 4218.6 ms | 161848.6 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 221761.8 ms | 217584.5 ms | 4177.4 ms | 159485.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 217921.1 ms | 213732.9 ms | 4188.1 ms | 155567.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 202300.4 ms | 198393.4 ms | 3907.0 ms | 140003.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 201042.8 ms | 197119.8 ms | 3923.0 ms | 138484.8 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 187314.8 ms | 183470.1 ms | 3844.7 ms | 127461.8 ms |
| Aws_restjson | LLGoNoLTO | 183078.0 ms | 179350.1 ms | 3728.0 ms | 56946.3 ms |
| Aws_restjson | LLGoDeadcodeDrop | 178736.9 ms | 174931.3 ms | 3805.7 ms | 57471.9 ms |
| Etcdctl | LLGoDeadcodeDrop | 172603.4 ms | 166069.2 ms | 6534.2 ms | 60533.3 ms |
| Etcdctl | LLGoNoLTO | 171520.8 ms | 165711.5 ms | 5809.4 ms | 59362.7 ms |
| Uber_zap | LLGoNoLTO | 143419.5 ms | 140460.5 ms | 2959.0 ms | 46049.0 ms |
| Uber_zap | LLGoDeadcodeDrop | 142556.8 ms | 139333.4 ms | 3223.4 ms | 47257.1 ms |
| K8s_workqueue | LLGoNoLTO | 139437.8 ms | 136263.4 ms | 3174.4 ms | 44956.7 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 133916.0 ms | 130729.8 ms | 3186.2 ms | 44674.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 111081.5 ms | 108609.6 ms | 2471.9 ms | 78363.9 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 109944.1 ms | 107504.8 ms | 2439.3 ms | 78044.6 ms |
| Toml | LLGoFullLTONoGlobalDCE | 106159.4 ms | 103698.5 ms | 2460.9 ms | 74553.8 ms |
| Toml | LLGoFullLTOGlobalDCE | 99087.9 ms | 96622.0 ms | 2465.9 ms | 64908.9 ms |
| XGo | LLGoDeadcodeDrop | 95482.7 ms | 91234.0 ms | 4248.8 ms | 35443.5 ms |
| XGo | LLGoNoLTO | 94973.1 ms | 91290.7 ms | 3682.4 ms | 35432.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 92326.8 ms | 89991.2 ms | 2335.7 ms | 58759.9 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 92253.5 ms | 89992.5 ms | 2261.0 ms | 60511.5 ms |
| Gorm_schema | LLGoNoLTO | 80446.4 ms | 78250.3 ms | 2196.1 ms | 28207.7 ms |
| Gorm_schema | LLGoDeadcodeDrop | 78118.2 ms | 75892.2 ms | 2226.0 ms | 27673.8 ms |
| Toml | LLGoNoLTO | 75166.0 ms | 73221.5 ms | 1944.6 ms | 26185.2 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 74839.3 ms | 73140.6 ms | 1698.7 ms | 54795.6 ms |
| Toml | LLGoDeadcodeDrop | 73515.7 ms | 71578.1 ms | 1937.6 ms | 26040.4 ms |
| IXGo | Go | 63332.6 ms | 55369.3 ms | 7963.3 ms | 17469.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 60980.2 ms | 59435.4 ms | 1544.8 ms | 40209.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 59168.5 ms | 57675.8 ms | 1492.7 ms | 38558.9 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 52677.1 ms | 51239.8 ms | 1437.2 ms | 19911.2 ms |
| Dustin_humanize | LLGoNoLTO | 51134.2 ms | 49852.6 ms | 1281.6 ms | 19211.7 ms |
| Etcdctl | Go | 25262.0 ms | 22427.8 ms | 2834.2 ms | 7825.0 ms |
| XGo | Go | 14412.8 ms | 12723.3 ms | 1689.5 ms | 4333.7 ms |
| Aws_restjson | Go | 6367.4 ms | 5450.1 ms | 917.3 ms | 2875.4 ms |
| Gorm_schema | Go | 4553.2 ms | 3990.9 ms | 562.2 ms | 1774.3 ms |
| Uber_zap | Go | 4115.3 ms | 3625.9 ms | 489.5 ms | 1648.3 ms |
| K8s_workqueue | Go | 3521.7 ms | 2994.7 ms | 527.0 ms | 1301.4 ms |
| Toml | Go | 1572.5 ms | 1335.6 ms | 237.0 ms | 797.8 ms |
| Dustin_humanize | Go | 608.0 ms | 500.1 ms | 107.9 ms | 299.3 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2311149.2 ms | 1663469.7 ms | 9 |
| LLGoFullLTOGlobalDCE | 2208325.0 ms | 1552625.3 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2154276.1 ms | 1501637.8 ms | 9 |
| LLGoNoLTO | 1293213.4 ms | 426739.5 ms | 9 |
| LLGoDeadcodeDrop | 1286929.9 ms | 435448.1 ms | 9 |
| Go | 123745.4 ms | 38324.6 ms | 9 |

Dependency download details are in `download-timings.log`.
