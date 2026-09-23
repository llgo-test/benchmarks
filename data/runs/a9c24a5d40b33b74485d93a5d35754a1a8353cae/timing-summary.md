## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 514080.5 ms | 502509.3 ms | 11571.2 ms | 271785.3 ms |
| IXGo | LLGoFullLTOGlobalDCE | 507216.4 ms | 495231.6 ms | 11984.9 ms | 268899.6 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 506605.5 ms | 495759.0 ms | 10846.6 ms | 266340.1 ms |
| IXGo | LLGoDeadcodeDrop | 413169.9 ms | 403175.5 ms | 9994.4 ms | 123850.0 ms |
| IXGo | LLGoNoLTO | 400319.0 ms | 390678.7 ms | 9640.3 ms | 120045.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 255594.7 ms | 251020.7 ms | 4574.0 ms | 156647.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 252270.8 ms | 247828.4 ms | 4442.4 ms | 155421.5 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 251662.6 ms | 247253.6 ms | 4409.0 ms | 156002.9 ms |
| Etcdctl | LLGoDeadcodeDrop | 192241.7 ms | 188108.2 ms | 4133.4 ms | 64297.6 ms |
| Etcdctl | LLGoNoLTO | 188393.5 ms | 184607.5 ms | 3786.0 ms | 62867.0 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 179744.9 ms | 176407.3 ms | 3337.6 ms | 123688.0 ms |
| XGo | LLGoFullLTOGlobalDCE | 178563.2 ms | 175392.9 ms | 3170.3 ms | 122663.6 ms |
| XGo | LLGoFullLTONoGlobalDCE | 175833.9 ms | 172740.6 ms | 3093.3 ms | 121487.3 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 135592.4 ms | 133111.1 ms | 2481.3 ms | 97840.3 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 125101.8 ms | 122639.2 ms | 2462.6 ms | 86508.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 125049.5 ms | 122765.8 ms | 2283.6 ms | 86499.4 ms |
| XGo | LLGoDeadcodeDrop | 111675.1 ms | 108879.5 ms | 2795.6 ms | 41866.7 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 109994.7 ms | 108196.5 ms | 1798.3 ms | 83277.6 ms |
| XGo | LLGoNoLTO | 109917.8 ms | 107120.0 ms | 2797.8 ms | 41844.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 100704.1 ms | 98794.1 ms | 1910.0 ms | 73014.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 97931.3 ms | 96131.6 ms | 1799.7 ms | 70648.8 ms |
| Aws_restjson | LLGoNoLTO | 84901.8 ms | 82757.8 ms | 2144.0 ms | 38797.7 ms |
| Aws_restjson | LLGoDeadcodeDrop | 84836.7 ms | 82757.2 ms | 2079.5 ms | 39129.3 ms |
| IXGo | Go | 83462.6 ms | 78405.0 ms | 5057.5 ms | 23245.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 64660.7 ms | 63216.9 ms | 1443.8 ms | 43701.6 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 61931.8 ms | 60592.8 ms | 1338.9 ms | 42019.7 ms |
| Uber_zap | LLGoDeadcodeDrop | 58381.5 ms | 56915.2 ms | 1466.3 ms | 25599.9 ms |
| Uber_zap | LLGoNoLTO | 57125.7 ms | 55633.4 ms | 1492.4 ms | 25379.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 51673.7 ms | 50312.8 ms | 1360.9 ms | 31385.2 ms |
| Toml | LLGoFullLTONoGlobalDCE | 48003.1 ms | 46889.4 ms | 1113.6 ms | 36042.7 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 41433.0 ms | 40369.0 ms | 1063.9 ms | 28370.5 ms |
| Toml | LLGoFullLTOGlobalDCE | 40461.3 ms | 39424.5 ms | 1036.9 ms | 28222.5 ms |
| Gorm_schema | LLGoDeadcodeDrop | 40042.8 ms | 38833.6 ms | 1209.2 ms | 13396.4 ms |
| Gorm_schema | LLGoNoLTO | 39116.5 ms | 37898.4 ms | 1218.1 ms | 13056.9 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 34310.6 ms | 33450.5 ms | 860.1 ms | 26568.6 ms |
| Etcdctl | Go | 33295.7 ms | 31069.8 ms | 2225.9 ms | 10483.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 26195.4 ms | 25312.6 ms | 882.7 ms | 18153.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 26058.3 ms | 25231.6 ms | 826.7 ms | 18048.6 ms |
| Toml | LLGoDeadcodeDrop | 24441.0 ms | 23459.6 ms | 981.4 ms | 9234.0 ms |
| Toml | LLGoNoLTO | 23969.9 ms | 22982.5 ms | 987.5 ms | 8936.0 ms |
| XGo | Go | 18992.1 ms | 17821.1 ms | 1170.9 ms | 5600.9 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 14069.9 ms | 13346.7 ms | 723.2 ms | 5864.5 ms |
| Dustin_humanize | LLGoNoLTO | 14014.8 ms | 13212.9 ms | 801.9 ms | 5869.2 ms |
| Aws_restjson | Go | 7890.0 ms | 7222.1 ms | 668.0 ms | 3139.7 ms |
| Gorm_schema | Go | 5675.0 ms | 5331.5 ms | 343.5 ms | 2161.3 ms |
| Uber_zap | Go | 5297.3 ms | 4835.5 ms | 461.8 ms | 2084.2 ms |
| K8s_workqueue | Go | 4664.7 ms | 4206.0 ms | 458.7 ms | 1642.8 ms |
| Toml | Go | 2060.0 ms | 1804.8 ms | 255.2 ms | 936.8 ms |
| Dustin_humanize | Go | 928.5 ms | 699.6 ms | 228.8 ms | 634.7 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1323934.6 ms | 829579.2 ms | 8 |
| LLGoFullLTOGlobalDCEPlugin | 1294338.5 ms | 789438.4 ms | 8 |
| LLGoFullLTOGlobalDCE | 1292400.9 ms | 794219.4 ms | 8 |
| LLGoDeadcodeDrop | 938858.6 ms | 323238.4 ms | 8 |
| LLGoNoLTO | 917759.1 ms | 316795.9 ms | 8 |
| Go | 162265.8 ms | 49929.4 ms | 9 |

Dependency download details are in `download-timings.log`.
