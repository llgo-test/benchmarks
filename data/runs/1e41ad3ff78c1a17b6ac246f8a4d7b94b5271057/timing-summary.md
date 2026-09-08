## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 420615.3 ms | 416101.2 ms | 4514.2 ms | 277944.2 ms |
| IXGo | LLGoFullLTOGlobalDCE | 404199.5 ms | 399595.6 ms | 4603.9 ms | 263234.4 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 371599.3 ms | 367248.0 ms | 4351.3 ms | 240946.8 ms |
| IXGo | LLGoNoLTO | 260252.2 ms | 256446.6 ms | 3805.6 ms | 85390.0 ms |
| IXGo | LLGoDeadcodeDrop | 255137.9 ms | 251208.0 ms | 3929.9 ms | 86290.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 164634.6 ms | 161245.5 ms | 3389.1 ms | 101527.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 162384.6 ms | 159155.7 ms | 3228.8 ms | 100046.8 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 162078.4 ms | 158739.0 ms | 3339.4 ms | 100615.6 ms |
| Etcdctl | LLGoDeadcodeDrop | 119020.5 ms | 116271.6 ms | 2748.9 ms | 40214.8 ms |
| Etcdctl | LLGoNoLTO | 115187.6 ms | 112401.4 ms | 2786.2 ms | 38413.7 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 109483.0 ms | 107375.2 ms | 2107.8 ms | 77126.0 ms |
| XGo | LLGoFullLTOGlobalDCE | 109293.0 ms | 107243.6 ms | 2049.4 ms | 77250.5 ms |
| XGo | LLGoFullLTONoGlobalDCE | 109052.6 ms | 106973.8 ms | 2078.8 ms | 77220.3 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 84311.3 ms | 82729.0 ms | 1582.3 ms | 63301.1 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 78161.3 ms | 76585.8 ms | 1575.5 ms | 57088.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 77733.4 ms | 76244.2 ms | 1489.2 ms | 55842.0 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 67691.1 ms | 66599.9 ms | 1091.2 ms | 52895.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 63954.7 ms | 62819.9 ms | 1134.8 ms | 50556.7 ms |
| XGo | LLGoDeadcodeDrop | 63797.1 ms | 61980.7 ms | 1816.4 ms | 24339.7 ms |
| XGo | LLGoNoLTO | 63097.5 ms | 61313.9 ms | 1783.5 ms | 24042.1 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 63083.9 ms | 61863.9 ms | 1220.0 ms | 49939.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 61864.3 ms | 60623.1 ms | 1241.1 ms | 46022.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 61331.9 ms | 60205.9 ms | 1126.0 ms | 46112.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 56245.2 ms | 55034.0 ms | 1211.2 ms | 42761.0 ms |
| Aws_restjson | LLGoNoLTO | 49935.1 ms | 48667.2 ms | 1267.9 ms | 24125.6 ms |
| Aws_restjson | LLGoDeadcodeDrop | 49296.0 ms | 47937.3 ms | 1358.7 ms | 23511.3 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 38450.0 ms | 37600.8 ms | 849.2 ms | 27314.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 37871.6 ms | 36965.9 ms | 905.7 ms | 26652.1 ms |
| Uber_zap | LLGoNoLTO | 34554.4 ms | 33597.5 ms | 956.9 ms | 15884.3 ms |
| Uber_zap | LLGoDeadcodeDrop | 34281.9 ms | 33353.7 ms | 928.2 ms | 15975.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 32266.1 ms | 31369.4 ms | 896.7 ms | 20807.9 ms |
| Toml | LLGoFullLTONoGlobalDCE | 30672.2 ms | 29998.8 ms | 673.4 ms | 23793.4 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 29928.7 ms | 28967.7 ms | 961.1 ms | 14692.2 ms |
| K8s_workqueue | LLGoNoLTO | 29360.4 ms | 28412.5 ms | 947.9 ms | 13890.2 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 26488.4 ms | 25778.5 ms | 709.8 ms | 19310.7 ms |
| IXGo | Go | 26042.2 ms | 23966.9 ms | 2075.3 ms | 7557.4 ms |
| Toml | LLGoFullLTOGlobalDCE | 25836.1 ms | 25158.9 ms | 677.2 ms | 19003.8 ms |
| Gorm_schema | LLGoDeadcodeDrop | 22034.9 ms | 21255.2 ms | 779.7 ms | 7286.4 ms |
| Gorm_schema | LLGoNoLTO | 21083.2 ms | 20282.2 ms | 801.0 ms | 7039.5 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 19950.1 ms | 19390.5 ms | 559.6 ms | 15895.0 ms |
| Etcdctl | Go | 19669.0 ms | 18290.9 ms | 1378.1 ms | 5921.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 15284.0 ms | 14760.2 ms | 523.9 ms | 10780.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 14614.5 ms | 14101.6 ms | 512.9 ms | 10510.0 ms |
| Toml | LLGoDeadcodeDrop | 13823.7 ms | 13194.6 ms | 629.1 ms | 5188.1 ms |
| Toml | LLGoNoLTO | 13336.2 ms | 12730.7 ms | 605.5 ms | 5013.2 ms |
| XGo | Go | 11262.4 ms | 10441.8 ms | 820.6 ms | 3331.0 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 7699.2 ms | 7237.2 ms | 462.0 ms | 3753.1 ms |
| Dustin_humanize | LLGoNoLTO | 7661.5 ms | 7214.5 ms | 447.0 ms | 3315.0 ms |
| Aws_restjson | Go | 4604.1 ms | 4138.6 ms | 465.5 ms | 1876.1 ms |
| Gorm_schema | Go | 3337.1 ms | 3062.5 ms | 274.6 ms | 1265.0 ms |
| Uber_zap | Go | 3084.3 ms | 2818.4 ms | 265.9 ms | 1200.5 ms |
| K8s_workqueue | Go | 2737.3 ms | 2445.7 ms | 291.6 ms | 983.9 ms |
| Toml | Go | 1188.3 ms | 1038.4 ms | 149.9 ms | 544.9 ms |
| Dustin_humanize | Go | 466.1 ms | 375.1 ms | 91.1 ms | 226.8 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTOGlobalDCEPlugin | 965042.2 ms | 653368.3 ms | 9 |
| LLGoFullLTOGlobalDCE | 957219.2 ms | 649208.9 ms | 9 |
| LLGoFullLTONoGlobalDCE | 946888.9 ms | 651922.1 ms | 9 |
| LLGoDeadcodeDrop | 595020.0 ms | 221250.9 ms | 9 |
| LLGoNoLTO | 594468.0 ms | 217113.4 ms | 9 |
| Go | 72390.8 ms | 22907.2 ms | 9 |

Dependency download details are in `download-timings.log`.
