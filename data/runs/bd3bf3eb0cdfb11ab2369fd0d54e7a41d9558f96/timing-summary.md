## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 668644.1 ms | 651720.5 ms | 16923.7 ms | 444994.7 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 645885.0 ms | 629563.8 ms | 16321.2 ms | 427634.7 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 618667.4 ms | 602838.3 ms | 15829.1 ms | 419666.1 ms |
| IXGo | LLGoDeadcodeDrop | 360477.5 ms | 344540.1 ms | 15937.4 ms | 116681.8 ms |
| IXGo | LLGoNoLTO | 347566.7 ms | 333633.4 ms | 13933.3 ms | 108983.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 346614.5 ms | 339141.9 ms | 7472.7 ms | 259218.3 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 337313.5 ms | 329814.2 ms | 7499.2 ms | 250515.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 327815.9 ms | 320578.5 ms | 7237.5 ms | 243296.6 ms |
| XGo | LLGoFullLTONoGlobalDCE | 240513.1 ms | 235719.6 ms | 4793.4 ms | 194356.3 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 227468.9 ms | 223375.1 ms | 4093.9 ms | 157884.4 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 216508.4 ms | 211887.5 ms | 4620.9 ms | 168530.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 211100.7 ms | 206925.7 ms | 4175.0 ms | 137057.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 210859.2 ms | 206917.3 ms | 3942.0 ms | 137534.0 ms |
| XGo | LLGoFullLTOGlobalDCE | 203682.6 ms | 199122.3 ms | 4560.4 ms | 157633.0 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 196482.0 ms | 192920.2 ms | 3561.8 ms | 141446.8 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 185780.3 ms | 182337.4 ms | 3442.9 ms | 136045.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 184025.4 ms | 180420.8 ms | 3604.5 ms | 132940.4 ms |
| Aws_restjson | LLGoNoLTO | 180256.2 ms | 176597.2 ms | 3659.0 ms | 56408.0 ms |
| Aws_restjson | LLGoDeadcodeDrop | 174736.1 ms | 170900.5 ms | 3835.6 ms | 56082.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 174403.9 ms | 171004.3 ms | 3399.7 ms | 120120.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 170770.7 ms | 167374.4 ms | 3396.2 ms | 115394.4 ms |
| Etcdctl | LLGoNoLTO | 169422.6 ms | 163739.5 ms | 5683.1 ms | 58655.6 ms |
| Etcdctl | LLGoDeadcodeDrop | 166636.4 ms | 160526.4 ms | 6109.9 ms | 58838.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 159351.1 ms | 156114.2 ms | 3236.9 ms | 107895.9 ms |
| Uber_zap | LLGoDeadcodeDrop | 144611.4 ms | 141344.2 ms | 3267.1 ms | 48055.2 ms |
| Uber_zap | LLGoNoLTO | 141202.4 ms | 138264.5 ms | 2937.9 ms | 45635.4 ms |
| K8s_workqueue | LLGoNoLTO | 140214.0 ms | 137119.2 ms | 3094.8 ms | 45156.3 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 136291.7 ms | 133198.6 ms | 3093.1 ms | 45433.7 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 108983.9 ms | 106655.1 ms | 2328.8 ms | 77904.8 ms |
| Toml | LLGoFullLTONoGlobalDCE | 106966.7 ms | 104685.8 ms | 2281.0 ms | 75626.7 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 102949.2 ms | 100716.0 ms | 2233.2 ms | 72566.6 ms |
| XGo | LLGoDeadcodeDrop | 96411.9 ms | 92250.0 ms | 4161.9 ms | 36146.3 ms |
| XGo | LLGoNoLTO | 94177.1 ms | 90508.7 ms | 3668.4 ms | 35372.3 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 92767.3 ms | 90505.7 ms | 2261.6 ms | 61260.6 ms |
| Toml | LLGoFullLTOGlobalDCE | 90662.9 ms | 88463.1 ms | 2199.9 ms | 59670.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 89517.4 ms | 87267.2 ms | 2250.2 ms | 57816.4 ms |
| Gorm_schema | LLGoDeadcodeDrop | 79865.5 ms | 77699.5 ms | 2166.0 ms | 28436.0 ms |
| Gorm_schema | LLGoNoLTO | 77541.1 ms | 75601.9 ms | 1939.2 ms | 27175.7 ms |
| Toml | LLGoNoLTO | 74122.3 ms | 72325.4 ms | 1796.9 ms | 25832.7 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 72994.0 ms | 71339.6 ms | 1654.4 ms | 53943.0 ms |
| Toml | LLGoDeadcodeDrop | 72916.6 ms | 71065.9 ms | 1850.7 ms | 25706.6 ms |
| IXGo | Go | 64344.8 ms | 56052.3 ms | 8292.5 ms | 17771.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 56029.0 ms | 54576.7 ms | 1452.3 ms | 36689.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 53041.7 ms | 51653.4 ms | 1388.2 ms | 34760.9 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 50640.6 ms | 49285.9 ms | 1354.8 ms | 19198.0 ms |
| Dustin_humanize | LLGoNoLTO | 49689.8 ms | 48455.2 ms | 1234.7 ms | 18741.7 ms |
| Etcdctl | Go | 25292.7 ms | 22305.9 ms | 2986.8 ms | 7620.4 ms |
| XGo | Go | 14522.3 ms | 12772.0 ms | 1750.3 ms | 4299.1 ms |
| Aws_restjson | Go | 6205.6 ms | 5303.6 ms | 902.0 ms | 2770.3 ms |
| Gorm_schema | Go | 4393.7 ms | 3876.8 ms | 516.9 ms | 1704.0 ms |
| Uber_zap | Go | 4047.3 ms | 3559.0 ms | 488.3 ms | 1662.3 ms |
| K8s_workqueue | Go | 3495.3 ms | 3036.1 ms | 459.2 ms | 1249.7 ms |
| Toml | Go | 1577.6 ms | 1358.2 ms | 219.5 ms | 737.7 ms |
| Dustin_humanize | Go | 612.8 ms | 510.0 ms | 102.7 ms | 302.5 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2095169.8 ms | 1507388.2 ms | 9 |
| LLGoFullLTOGlobalDCE | 2016085.1 ms | 1403516.5 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1988544.2 ms | 1371497.2 ms | 9 |
| LLGoDeadcodeDrop | 1282587.7 ms | 434578.8 ms | 9 |
| LLGoNoLTO | 1274192.2 ms | 421961.3 ms | 9 |
| Go | 124492.2 ms | 38117.4 ms | 9 |

Dependency download details are in `download-timings.log`.
