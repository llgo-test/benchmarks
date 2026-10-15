## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 618926.0 ms | 607095.3 ms | 11830.7 ms | 324933.1 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 614698.8 ms | 602637.9 ms | 12061.0 ms | 327380.9 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 589829.1 ms | 578268.9 ms | 11560.2 ms | 318226.8 ms |
| IXGo | LLGoDeadcodeDrop | 456500.2 ms | 441314.7 ms | 15185.6 ms | 136494.7 ms |
| IXGo | LLGoNoLTO | 444190.2 ms | 434017.8 ms | 10172.4 ms | 128854.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 285689.9 ms | 280101.6 ms | 5588.2 ms | 181976.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 282545.4 ms | 277252.4 ms | 5293.0 ms | 179683.5 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 282080.1 ms | 276007.5 ms | 6072.5 ms | 182422.2 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 225723.3 ms | 221930.7 ms | 3792.6 ms | 136911.0 ms |
| Aws_restjson | LLGoNoLTO | 217136.5 ms | 213910.4 ms | 3226.1 ms | 75652.9 ms |
| Aws_restjson | LLGoDeadcodeDrop | 216847.8 ms | 213198.0 ms | 3649.9 ms | 76681.1 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 211854.0 ms | 208266.2 ms | 3587.7 ms | 121699.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 211351.1 ms | 207813.2 ms | 3537.9 ms | 121611.5 ms |
| Etcdctl | LLGoDeadcodeDrop | 201508.3 ms | 195857.9 ms | 5650.4 ms | 68030.7 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 200156.8 ms | 196305.2 ms | 3851.6 ms | 144013.5 ms |
| XGo | LLGoFullLTONoGlobalDCE | 199760.5 ms | 196107.3 ms | 3653.2 ms | 145070.1 ms |
| XGo | LLGoFullLTOGlobalDCE | 199182.6 ms | 195417.1 ms | 3765.5 ms | 142870.7 ms |
| Etcdctl | LLGoNoLTO | 198218.9 ms | 193638.2 ms | 4580.7 ms | 65534.6 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 188599.5 ms | 185450.6 ms | 3148.9 ms | 120696.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 183082.3 ms | 179732.3 ms | 3350.1 ms | 117135.1 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 181975.6 ms | 178763.3 ms | 3212.3 ms | 117246.6 ms |
| Uber_zap | LLGoDeadcodeDrop | 180783.6 ms | 177760.2 ms | 3023.4 ms | 68412.1 ms |
| Uber_zap | LLGoNoLTO | 180060.2 ms | 177287.5 ms | 2772.7 ms | 67361.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 177836.6 ms | 174731.7 ms | 3104.9 ms | 108511.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 176967.4 ms | 173981.7 ms | 2985.8 ms | 108005.1 ms |
| K8s_workqueue | LLGoNoLTO | 173538.2 ms | 170735.8 ms | 2802.3 ms | 64956.8 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 173346.5 ms | 170142.6 ms | 3203.9 ms | 65855.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 166964.3 ms | 163853.4 ms | 3110.9 ms | 101136.5 ms |
| XGo | LLGoDeadcodeDrop | 114901.7 ms | 111188.7 ms | 3713.0 ms | 43782.5 ms |
| XGo | LLGoNoLTO | 113640.3 ms | 110650.0 ms | 2990.3 ms | 42369.1 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 95701.0 ms | 93688.0 ms | 2013.0 ms | 58015.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 95485.6 ms | 93476.9 ms | 2008.7 ms | 57281.9 ms |
| Gorm_schema | LLGoDeadcodeDrop | 95345.0 ms | 93264.5 ms | 2080.5 ms | 31711.9 ms |
| Gorm_schema | LLGoNoLTO | 93942.7 ms | 92193.4 ms | 1749.3 ms | 30919.2 ms |
| Toml | LLGoDeadcodeDrop | 88776.2 ms | 86659.5 ms | 2116.7 ms | 29502.0 ms |
| Toml | LLGoNoLTO | 88733.1 ms | 86834.3 ms | 1898.8 ms | 28990.8 ms |
| Toml | LLGoFullLTONoGlobalDCE | 88051.6 ms | 85953.4 ms | 2098.2 ms | 52758.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 83309.1 ms | 81447.4 ms | 1861.7 ms | 45045.2 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 79717.3 ms | 77674.6 ms | 2042.7 ms | 43639.5 ms |
| Toml | LLGoFullLTOGlobalDCE | 79566.4 ms | 77611.9 ms | 1954.5 ms | 43532.0 ms |
| IXGo | Go | 77768.0 ms | 72552.3 ms | 5215.7 ms | 21417.8 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 62058.4 ms | 60575.4 ms | 1483.0 ms | 39198.7 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 60965.4 ms | 59490.3 ms | 1475.1 ms | 22082.6 ms |
| Dustin_humanize | LLGoNoLTO | 60879.6 ms | 59567.8 ms | 1311.8 ms | 21667.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 52311.3 ms | 51009.9 ms | 1301.3 ms | 29333.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 52138.6 ms | 50758.0 ms | 1380.6 ms | 29132.9 ms |
| Etcdctl | Go | 31392.1 ms | 29371.8 ms | 2020.3 ms | 9425.2 ms |
| XGo | Go | 17940.7 ms | 16750.1 ms | 1190.5 ms | 5295.4 ms |
| Aws_restjson | Go | 7510.8 ms | 6808.6 ms | 702.2 ms | 3035.6 ms |
| Gorm_schema | Go | 5438.2 ms | 5042.8 ms | 395.3 ms | 2149.2 ms |
| Uber_zap | Go | 5062.4 ms | 4614.1 ms | 448.4 ms | 1969.9 ms |
| K8s_workqueue | Go | 4470.3 ms | 3965.4 ms | 504.9 ms | 1665.4 ms |
| Toml | Go | 1964.4 ms | 1699.0 ms | 265.4 ms | 897.1 ms |
| Dustin_humanize | Go | 862.7 ms | 633.1 ms | 229.6 ms | 557.5 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1913779.3 ms | 1170546.2 ms | 9 |
| LLGoFullLTOGlobalDCE | 1899245.5 ms | 1124185.7 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1872538.0 ms | 1102736.1 ms | 9 |
| LLGoDeadcodeDrop | 1588974.8 ms | 542552.4 ms | 9 |
| LLGoNoLTO | 1570339.6 ms | 526306.9 ms | 9 |
| Go | 152409.5 ms | 46413.2 ms | 9 |

Dependency download details are in `download-timings.log`.
