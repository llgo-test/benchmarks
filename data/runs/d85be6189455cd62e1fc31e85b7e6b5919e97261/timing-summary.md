## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 434952.1 ms | 426848.6 ms | 8103.5 ms | 233790.1 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 420894.3 ms | 412615.6 ms | 8278.7 ms | 226825.9 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 384852.5 ms | 376505.8 ms | 8346.7 ms | 210028.5 ms |
| IXGo | LLGoNoLTO | 325229.5 ms | 318738.8 ms | 6490.7 ms | 93345.0 ms |
| IXGo | LLGoDeadcodeDrop | 294330.3 ms | 284537.4 ms | 9792.9 ms | 89410.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 206311.9 ms | 202212.5 ms | 4099.4 ms | 125698.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 185034.1 ms | 181477.8 ms | 3556.4 ms | 118785.6 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 183167.0 ms | 179692.9 ms | 3474.1 ms | 120519.3 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 144375.0 ms | 141874.3 ms | 2500.8 ms | 88389.8 ms |
| Aws_restjson | LLGoNoLTO | 141763.3 ms | 139601.0 ms | 2162.4 ms | 48785.4 ms |
| Aws_restjson | LLGoDeadcodeDrop | 138791.9 ms | 136489.8 ms | 2302.1 ms | 48352.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 136990.6 ms | 134657.5 ms | 2333.1 ms | 79130.4 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 136307.3 ms | 133757.2 ms | 2550.1 ms | 97943.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 136039.9 ms | 133777.2 ms | 2262.8 ms | 77133.6 ms |
| Etcdctl | LLGoDeadcodeDrop | 134486.2 ms | 130699.8 ms | 3786.4 ms | 45974.6 ms |
| XGo | LLGoFullLTOGlobalDCE | 131110.5 ms | 128768.6 ms | 2341.9 ms | 95481.6 ms |
| XGo | LLGoFullLTONoGlobalDCE | 130790.8 ms | 128338.7 ms | 2452.1 ms | 95361.7 ms |
| Uber_zap | LLGoDeadcodeDrop | 129006.3 ms | 126853.0 ms | 2153.2 ms | 49014.5 ms |
| Etcdctl | LLGoNoLTO | 128413.6 ms | 125313.0 ms | 3100.6 ms | 42669.4 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 120086.0 ms | 118038.5 ms | 2047.5 ms | 77133.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 117261.5 ms | 115224.1 ms | 2037.3 ms | 75225.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 115657.2 ms | 113672.1 ms | 1985.1 ms | 71173.2 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 115181.1 ms | 113171.7 ms | 2009.4 ms | 75280.9 ms |
| Uber_zap | LLGoNoLTO | 112417.8 ms | 110615.8 ms | 1802.0 ms | 41668.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 112088.9 ms | 110099.3 ms | 1989.6 ms | 67967.1 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 110071.2 ms | 107912.1 ms | 2159.1 ms | 41676.4 ms |
| K8s_workqueue | LLGoNoLTO | 107867.2 ms | 105947.2 ms | 1920.0 ms | 40017.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 106940.4 ms | 104837.7 ms | 2102.7 ms | 65048.4 ms |
| XGo | LLGoNoLTO | 79860.8 ms | 77836.7 ms | 2024.1 ms | 28963.3 ms |
| XGo | LLGoDeadcodeDrop | 74257.5 ms | 71907.1 ms | 2350.4 ms | 28744.2 ms |
| Gorm_schema | LLGoNoLTO | 60570.2 ms | 59375.5 ms | 1194.7 ms | 20160.5 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 60464.4 ms | 59155.9 ms | 1308.5 ms | 36928.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 60459.2 ms | 59230.3 ms | 1228.9 ms | 36731.2 ms |
| Gorm_schema | LLGoDeadcodeDrop | 60135.2 ms | 58780.8 ms | 1354.4 ms | 20113.3 ms |
| Toml | LLGoFullLTONoGlobalDCE | 56593.3 ms | 55226.2 ms | 1367.2 ms | 34023.7 ms |
| Toml | LLGoNoLTO | 56333.5 ms | 55014.1 ms | 1319.3 ms | 18553.9 ms |
| Toml | LLGoDeadcodeDrop | 55146.5 ms | 53771.2 ms | 1375.2 ms | 18660.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 54439.7 ms | 53226.9 ms | 1212.8 ms | 29927.7 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 52154.5 ms | 50811.3 ms | 1343.2 ms | 28914.4 ms |
| Toml | LLGoFullLTOGlobalDCE | 50402.4 ms | 49040.7 ms | 1361.7 ms | 27705.0 ms |
| IXGo | Go | 48465.8 ms | 44919.5 ms | 3546.4 ms | 13552.9 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 38599.7 ms | 37704.7 ms | 895.0 ms | 24702.3 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 38261.5 ms | 37351.0 ms | 910.5 ms | 13974.5 ms |
| Dustin_humanize | LLGoNoLTO | 38080.6 ms | 37275.5 ms | 805.1 ms | 13784.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 34634.0 ms | 33759.4 ms | 874.5 ms | 19533.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 33418.5 ms | 32512.2 ms | 906.3 ms | 19089.2 ms |
| Etcdctl | Go | 20338.2 ms | 18851.8 ms | 1486.4 ms | 6598.0 ms |
| XGo | Go | 11483.0 ms | 10655.4 ms | 827.6 ms | 3424.1 ms |
| Aws_restjson | Go | 4834.6 ms | 4356.0 ms | 478.6 ms | 1988.7 ms |
| Gorm_schema | Go | 3366.1 ms | 3097.9 ms | 268.2 ms | 1287.0 ms |
| Uber_zap | Go | 3098.1 ms | 2811.4 ms | 286.7 ms | 1225.5 ms |
| K8s_workqueue | Go | 2886.6 ms | 2567.8 ms | 318.8 ms | 1034.9 ms |
| Toml | Go | 1257.7 ms | 1091.1 ms | 166.6 ms | 585.2 ms |
| Dustin_humanize | Go | 488.2 ms | 393.5 ms | 94.6 ms | 242.0 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTOGlobalDCE | 1286828.6 ms | 762471.9 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1238268.4 ms | 733632.7 ms | 9 |
| LLGoFullLTONoGlobalDCE | 1234109.9 ms | 762368.3 ms | 9 |
| LLGoNoLTO | 1050536.6 ms | 347948.3 ms | 9 |
| LLGoDeadcodeDrop | 1034486.5 ms | 355921.3 ms | 9 |
| Go | 96218.2 ms | 29938.4 ms | 9 |

Dependency download details are in `download-timings.log`.
