## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 667541.4 ms | 650871.3 ms | 16670.1 ms | 450441.1 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 660833.6 ms | 643994.8 ms | 16838.7 ms | 441360.1 ms |
| IXGo | LLGoFullLTOGlobalDCE | 641352.5 ms | 624890.0 ms | 16462.5 ms | 427094.7 ms |
| IXGo | LLGoDeadcodeDrop | 379986.5 ms | 363023.1 ms | 16963.4 ms | 122732.6 ms |
| IXGo | LLGoNoLTO | 358862.4 ms | 345026.8 ms | 13835.6 ms | 112489.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 350786.9 ms | 342849.6 ms | 7937.4 ms | 260987.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 349452.3 ms | 341854.5 ms | 7597.8 ms | 260953.8 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 336132.7 ms | 328830.9 ms | 7301.8 ms | 252853.3 ms |
| XGo | LLGoFullLTONoGlobalDCE | 266261.2 ms | 260751.4 ms | 5509.8 ms | 215883.1 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 247325.1 ms | 242787.2 ms | 4538.0 ms | 169593.3 ms |
| XGo | LLGoFullLTOGlobalDCE | 228558.9 ms | 223379.3 ms | 5179.5 ms | 178131.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 219192.9 ms | 214852.6 ms | 4340.3 ms | 142217.6 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 218068.1 ms | 213197.5 ms | 4870.6 ms | 170778.1 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 212798.1 ms | 208647.9 ms | 4150.1 ms | 138159.1 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 202311.6 ms | 198478.7 ms | 3832.9 ms | 145719.8 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 193934.0 ms | 190066.9 ms | 3867.1 ms | 139847.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 191999.4 ms | 188334.1 ms | 3665.3 ms | 138720.4 ms |
| Aws_restjson | LLGoNoLTO | 187040.6 ms | 183253.4 ms | 3787.2 ms | 58608.1 ms |
| Aws_restjson | LLGoDeadcodeDrop | 185335.0 ms | 181254.7 ms | 4080.4 ms | 59621.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 181403.6 ms | 177951.8 ms | 3451.7 ms | 125355.2 ms |
| Etcdctl | LLGoDeadcodeDrop | 179205.6 ms | 172624.7 ms | 6580.9 ms | 62903.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 178906.4 ms | 175281.9 ms | 3624.5 ms | 122142.8 ms |
| Etcdctl | LLGoNoLTO | 174614.4 ms | 168519.7 ms | 6094.7 ms | 60369.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 159174.1 ms | 155806.5 ms | 3367.6 ms | 106915.3 ms |
| Uber_zap | LLGoDeadcodeDrop | 157711.1 ms | 154047.1 ms | 3664.0 ms | 52414.3 ms |
| Uber_zap | LLGoNoLTO | 148374.8 ms | 145184.7 ms | 3190.1 ms | 47966.3 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 142189.9 ms | 138937.7 ms | 3252.2 ms | 47559.0 ms |
| K8s_workqueue | LLGoNoLTO | 141021.5 ms | 137967.6 ms | 3053.9 ms | 45493.8 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 114892.4 ms | 112272.4 ms | 2620.0 ms | 81627.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 114674.8 ms | 112009.5 ms | 2665.3 ms | 80681.6 ms |
| Toml | LLGoFullLTONoGlobalDCE | 106026.9 ms | 103835.4 ms | 2191.5 ms | 74806.1 ms |
| XGo | LLGoDeadcodeDrop | 100487.1 ms | 96164.2 ms | 4322.9 ms | 36902.5 ms |
| XGo | LLGoNoLTO | 99689.0 ms | 95770.5 ms | 3918.5 ms | 36888.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 94808.5 ms | 92344.2 ms | 2464.3 ms | 60819.3 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 93621.0 ms | 91216.8 ms | 2404.2 ms | 61369.1 ms |
| Toml | LLGoFullLTOGlobalDCE | 93299.0 ms | 91066.9 ms | 2232.2 ms | 62031.4 ms |
| Gorm_schema | LLGoDeadcodeDrop | 84323.3 ms | 81879.7 ms | 2443.6 ms | 30055.5 ms |
| Gorm_schema | LLGoNoLTO | 82171.4 ms | 80169.5 ms | 2001.9 ms | 28545.9 ms |
| Toml | LLGoDeadcodeDrop | 77263.7 ms | 75223.9 ms | 2039.8 ms | 27275.5 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 76578.5 ms | 74908.2 ms | 1670.2 ms | 55947.5 ms |
| Toml | LLGoNoLTO | 76370.5 ms | 74397.5 ms | 1973.0 ms | 26688.5 ms |
| IXGo | Go | 65362.1 ms | 56745.5 ms | 8616.6 ms | 17995.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 59948.0 ms | 58375.1 ms | 1572.9 ms | 39465.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 57519.6 ms | 56034.5 ms | 1485.1 ms | 37835.2 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 53932.8 ms | 52474.7 ms | 1458.1 ms | 20714.6 ms |
| Dustin_humanize | LLGoNoLTO | 52676.7 ms | 51298.9 ms | 1377.8 ms | 20050.9 ms |
| Etcdctl | Go | 24789.1 ms | 22115.1 ms | 2674.0 ms | 7505.7 ms |
| XGo | Go | 14585.9 ms | 12801.6 ms | 1784.3 ms | 4442.3 ms |
| Aws_restjson | Go | 6252.4 ms | 5409.8 ms | 842.6 ms | 2587.6 ms |
| Gorm_schema | Go | 4510.0 ms | 3936.8 ms | 573.2 ms | 1756.5 ms |
| Uber_zap | Go | 4194.9 ms | 3625.9 ms | 569.0 ms | 1680.4 ms |
| K8s_workqueue | Go | 3589.6 ms | 3131.0 ms | 458.7 ms | 1286.0 ms |
| Toml | Go | 1570.6 ms | 1388.3 ms | 182.3 ms | 739.0 ms |
| Dustin_humanize | Go | 661.2 ms | 508.3 ms | 152.9 ms | 396.3 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2204296.0 ms | 1577638.2 ms | 9 |
| LLGoFullLTOGlobalDCE | 2072392.6 ms | 1448995.8 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2040712.8 ms | 1415102.4 ms | 9 |
| LLGoDeadcodeDrop | 1360435.2 ms | 460179.4 ms | 9 |
| LLGoNoLTO | 1320821.3 ms | 437100.5 ms | 9 |
| Go | 125515.9 ms | 38389.6 ms | 9 |

Dependency download details are in `download-timings.log`.
