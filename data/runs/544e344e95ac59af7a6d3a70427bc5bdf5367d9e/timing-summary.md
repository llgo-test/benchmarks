## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 678832.9 ms | 669375.5 ms | 9457.4 ms | 342519.4 ms |
| IXGo | LLGoFullLTOGlobalDCE | 647280.5 ms | 637472.4 ms | 9808.1 ms | 334134.0 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 632585.4 ms | 623307.6 ms | 9277.8 ms | 329611.9 ms |
| IXGo | LLGoDeadcodeDrop | 505065.8 ms | 491119.6 ms | 13946.2 ms | 151338.6 ms |
| IXGo | LLGoNoLTO | 498462.5 ms | 488716.7 ms | 9745.8 ms | 146332.0 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 338514.5 ms | 333336.7 ms | 5177.7 ms | 200160.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 336526.2 ms | 331623.8 ms | 4902.4 ms | 197320.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 335504.9 ms | 330507.8 ms | 4997.2 ms | 196593.7 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 266258.3 ms | 262628.2 ms | 3630.1 ms | 147494.0 ms |
| Aws_restjson | LLGoDeadcodeDrop | 263887.0 ms | 260613.4 ms | 3273.6 ms | 88205.1 ms |
| Aws_restjson | LLGoNoLTO | 261182.5 ms | 258087.3 ms | 3095.2 ms | 87267.3 ms |
| Etcdctl | LLGoDeadcodeDrop | 259200.8 ms | 253874.7 ms | 5326.0 ms | 86132.3 ms |
| Etcdctl | LLGoNoLTO | 253189.2 ms | 248934.4 ms | 4254.8 ms | 83722.1 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 252178.2 ms | 248466.2 ms | 3712.0 ms | 131155.4 ms |
| XGo | LLGoFullLTOGlobalDCE | 251599.7 ms | 248130.4 ms | 3469.3 ms | 164663.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 249286.6 ms | 245577.1 ms | 3709.5 ms | 130175.8 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 241516.3 ms | 238224.1 ms | 3292.2 ms | 157665.5 ms |
| XGo | LLGoFullLTONoGlobalDCE | 240266.4 ms | 237018.1 ms | 3248.3 ms | 157859.2 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 231895.2 ms | 228459.5 ms | 3435.7 ms | 132867.8 ms |
| Uber_zap | LLGoDeadcodeDrop | 226347.9 ms | 223581.5 ms | 2766.4 ms | 79398.3 ms |
| Uber_zap | LLGoNoLTO | 223606.4 ms | 220806.8 ms | 2799.7 ms | 78380.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 221315.3 ms | 217649.4 ms | 3665.9 ms | 125508.8 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 221111.3 ms | 217713.4 ms | 3397.9 ms | 125947.8 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 220924.6 ms | 218004.6 ms | 2920.0 ms | 77230.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 217800.5 ms | 214600.3 ms | 3200.2 ms | 118329.0 ms |
| K8s_workqueue | LLGoNoLTO | 217002.2 ms | 213968.6 ms | 3033.6 ms | 76274.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 216601.4 ms | 213502.0 ms | 3099.4 ms | 117888.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 205277.1 ms | 202082.3 ms | 3194.8 ms | 109923.9 ms |
| XGo | LLGoDeadcodeDrop | 158105.1 ms | 154501.4 ms | 3603.7 ms | 58377.0 ms |
| XGo | LLGoNoLTO | 157093.2 ms | 154297.5 ms | 2795.7 ms | 57018.2 ms |
| Gorm_schema | LLGoDeadcodeDrop | 108102.6 ms | 106328.4 ms | 1774.2 ms | 35787.2 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 107265.4 ms | 105212.9 ms | 2052.5 ms | 62097.4 ms |
| Gorm_schema | LLGoNoLTO | 105647.1 ms | 103968.6 ms | 1678.5 ms | 34925.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 104993.8 ms | 102979.7 ms | 2014.1 ms | 60283.8 ms |
| Toml | LLGoDeadcodeDrop | 102272.9 ms | 100473.5 ms | 1799.4 ms | 33814.3 ms |
| Toml | LLGoNoLTO | 99217.9 ms | 97488.7 ms | 1729.1 ms | 32591.1 ms |
| Toml | LLGoFullLTONoGlobalDCE | 97747.5 ms | 95674.7 ms | 2072.8 ms | 55766.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 92827.3 ms | 90927.3 ms | 1900.0 ms | 48064.2 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 89731.3 ms | 87747.6 ms | 1983.8 ms | 47043.3 ms |
| Toml | LLGoFullLTOGlobalDCE | 89243.4 ms | 87257.7 ms | 1985.7 ms | 46389.1 ms |
| IXGo | Go | 82624.1 ms | 77599.1 ms | 5025.1 ms | 22838.5 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 70427.0 ms | 69295.0 ms | 1132.0 ms | 25180.3 ms |
| Dustin_humanize | LLGoNoLTO | 70244.5 ms | 69104.9 ms | 1139.6 ms | 25190.8 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 70043.5 ms | 68726.3 ms | 1317.2 ms | 42168.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 60095.6 ms | 58711.7 ms | 1383.9 ms | 31996.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 59056.9 ms | 57749.7 ms | 1307.2 ms | 31434.9 ms |
| Etcdctl | Go | 33157.1 ms | 31220.1 ms | 1937.0 ms | 9913.3 ms |
| XGo | Go | 19041.2 ms | 17877.3 ms | 1163.9 ms | 5812.2 ms |
| Aws_restjson | Go | 7836.7 ms | 7199.4 ms | 637.2 ms | 3123.2 ms |
| Gorm_schema | Go | 5689.5 ms | 5309.1 ms | 380.4 ms | 2164.9 ms |
| Uber_zap | Go | 5368.3 ms | 4857.1 ms | 511.2 ms | 2284.7 ms |
| K8s_workqueue | Go | 4681.6 ms | 4233.1 ms | 448.5 ms | 1633.7 ms |
| Toml | Go | 1970.7 ms | 1750.0 ms | 220.7 ms | 900.5 ms |
| Dustin_humanize | Go | 799.0 ms | 663.8 ms | 135.2 ms | 374.8 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2205687.5 ms | 1253973.4 ms | 9 |
| LLGoFullLTOGlobalDCE | 2174882.5 ms | 1207072.0 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2174785.4 ms | 1184017.7 ms | 9 |
| LLGoDeadcodeDrop | 1914333.7 ms | 635463.1 ms | 9 |
| LLGoNoLTO | 1885645.6 ms | 621702.8 ms | 9 |
| Go | 161168.2 ms | 49045.9 ms | 9 |

Dependency download details are in `download-timings.log`.
