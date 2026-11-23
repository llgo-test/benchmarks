## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 698281.2 ms | 681508.4 ms | 16772.8 ms | 462723.2 ms |
| IXGo | LLGoFullLTOGlobalDCE | 679233.7 ms | 662021.1 ms | 17212.6 ms | 453033.2 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 658326.1 ms | 641630.8 ms | 16695.3 ms | 442162.1 ms |
| IXGo | LLGoDeadcodeDrop | 384191.3 ms | 367234.5 ms | 16956.8 ms | 124067.4 ms |
| IXGo | LLGoNoLTO | 362348.2 ms | 347881.5 ms | 14466.7 ms | 113561.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 343844.8 ms | 336517.6 ms | 7327.2 ms | 256227.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 341107.0 ms | 333722.6 ms | 7384.4 ms | 255004.3 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 334436.3 ms | 327180.8 ms | 7255.5 ms | 250860.9 ms |
| XGo | LLGoFullLTONoGlobalDCE | 260395.7 ms | 255137.4 ms | 5258.3 ms | 210832.8 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 237658.3 ms | 233517.4 ms | 4140.9 ms | 162462.2 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 227161.0 ms | 222098.6 ms | 5062.4 ms | 176621.0 ms |
| XGo | LLGoFullLTOGlobalDCE | 224920.4 ms | 219894.6 ms | 5025.8 ms | 175521.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 222116.6 ms | 217997.3 ms | 4119.3 ms | 144677.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 218678.6 ms | 214281.7 ms | 4396.9 ms | 141619.2 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 197471.9 ms | 193661.0 ms | 3810.9 ms | 142201.4 ms |
| Aws_restjson | LLGoNoLTO | 194691.5 ms | 190878.9 ms | 3812.6 ms | 60613.8 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 193389.0 ms | 189644.2 ms | 3744.8 ms | 139195.3 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 185810.2 ms | 181973.7 ms | 3836.5 ms | 134963.6 ms |
| Aws_restjson | LLGoDeadcodeDrop | 184207.3 ms | 180198.0 ms | 4009.3 ms | 59373.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 181377.2 ms | 177834.5 ms | 3542.7 ms | 125904.8 ms |
| Etcdctl | LLGoDeadcodeDrop | 180987.6 ms | 174309.2 ms | 6678.3 ms | 63711.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 179779.6 ms | 176132.2 ms | 3647.4 ms | 121867.3 ms |
| Etcdctl | LLGoNoLTO | 176669.9 ms | 170759.5 ms | 5910.4 ms | 60871.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 163458.7 ms | 160092.7 ms | 3365.9 ms | 109798.4 ms |
| Uber_zap | LLGoDeadcodeDrop | 149994.9 ms | 146805.8 ms | 3189.1 ms | 49567.2 ms |
| Uber_zap | LLGoNoLTO | 148862.2 ms | 145770.8 ms | 3091.4 ms | 47913.4 ms |
| K8s_workqueue | LLGoNoLTO | 143803.2 ms | 140763.9 ms | 3039.3 ms | 46410.8 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 142897.7 ms | 139454.9 ms | 3442.8 ms | 48103.1 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 115536.9 ms | 112973.7 ms | 2563.2 ms | 81927.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 114360.0 ms | 111800.5 ms | 2559.5 ms | 80626.5 ms |
| Toml | LLGoFullLTONoGlobalDCE | 110128.6 ms | 107746.9 ms | 2381.6 ms | 78070.6 ms |
| XGo | LLGoNoLTO | 102049.0 ms | 98096.0 ms | 3952.9 ms | 37540.9 ms |
| XGo | LLGoDeadcodeDrop | 98680.1 ms | 94199.3 ms | 4480.8 ms | 36760.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 96823.8 ms | 94409.2 ms | 2414.6 ms | 62357.2 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 94932.5 ms | 92462.6 ms | 2469.9 ms | 62587.1 ms |
| Toml | LLGoFullLTOGlobalDCE | 93098.2 ms | 90833.6 ms | 2264.6 ms | 61779.5 ms |
| Gorm_schema | LLGoDeadcodeDrop | 82502.8 ms | 80217.5 ms | 2285.3 ms | 29154.0 ms |
| Gorm_schema | LLGoNoLTO | 82096.1 ms | 79945.8 ms | 2150.3 ms | 28650.1 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 77161.2 ms | 75443.0 ms | 1718.3 ms | 56309.4 ms |
| Toml | LLGoNoLTO | 76481.4 ms | 74600.0 ms | 1881.5 ms | 26623.8 ms |
| Toml | LLGoDeadcodeDrop | 75217.0 ms | 73348.7 ms | 1868.3 ms | 26416.9 ms |
| IXGo | Go | 62438.3 ms | 54634.3 ms | 7804.0 ms | 17200.5 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 59746.0 ms | 58242.9 ms | 1503.1 ms | 39200.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 59613.6 ms | 58128.7 ms | 1484.9 ms | 39612.5 ms |
| Dustin_humanize | LLGoNoLTO | 52543.2 ms | 51234.1 ms | 1309.1 ms | 19799.9 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 52482.4 ms | 51068.7 ms | 1413.7 ms | 20203.1 ms |
| Etcdctl | Go | 25942.0 ms | 22848.0 ms | 3094.0 ms | 7877.8 ms |
| XGo | Go | 14849.9 ms | 13101.0 ms | 1748.9 ms | 4640.9 ms |
| Aws_restjson | Go | 6034.6 ms | 5258.8 ms | 775.8 ms | 2438.1 ms |
| Gorm_schema | Go | 4352.2 ms | 3847.6 ms | 504.6 ms | 1673.7 ms |
| Uber_zap | Go | 4234.1 ms | 3756.5 ms | 477.6 ms | 1721.0 ms |
| K8s_workqueue | Go | 3541.6 ms | 3083.4 ms | 458.1 ms | 1259.7 ms |
| Toml | Go | 1658.4 ms | 1436.8 ms | 221.6 ms | 984.2 ms |
| Dustin_humanize | Go | 640.4 ms | 519.4 ms | 121.0 ms | 318.8 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2176925.3 ms | 1559791.1 ms | 9 |
| LLGoFullLTOGlobalDCE | 2111953.6 ms | 1476579.1 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2079968.4 ms | 1431778.2 ms | 9 |
| LLGoDeadcodeDrop | 1351161.0 ms | 457357.7 ms | 9 |
| LLGoNoLTO | 1339544.7 ms | 441985.4 ms | 9 |
| Go | 123691.5 ms | 38114.8 ms | 9 |

Dependency download details are in `download-timings.log`.
