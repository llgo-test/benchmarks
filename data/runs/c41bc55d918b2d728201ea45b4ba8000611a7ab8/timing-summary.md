## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 751678.4 ms | 740288.8 ms | 11389.6 ms | 372514.3 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 624427.9 ms | 613765.9 ms | 10662.0 ms | 328532.2 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 614086.8 ms | 602227.9 ms | 11858.9 ms | 330558.5 ms |
| IXGo | LLGoNoLTO | 499831.5 ms | 491085.7 ms | 8745.8 ms | 142975.8 ms |
| IXGo | LLGoDeadcodeDrop | 471041.1 ms | 456464.7 ms | 14576.4 ms | 140953.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 298991.2 ms | 293980.5 ms | 5010.8 ms | 186746.6 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 294564.0 ms | 289869.9 ms | 4694.2 ms | 185587.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 289276.5 ms | 284642.1 ms | 4634.4 ms | 179058.7 ms |
| Aws_restjson | LLGoNoLTO | 234107.1 ms | 231070.4 ms | 3036.7 ms | 79784.4 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 232433.9 ms | 229178.5 ms | 3255.5 ms | 136966.6 ms |
| Aws_restjson | LLGoDeadcodeDrop | 232007.3 ms | 228669.7 ms | 3337.6 ms | 80172.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 221203.3 ms | 218042.5 ms | 3160.8 ms | 123157.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 219611.0 ms | 216489.6 ms | 3121.4 ms | 122596.3 ms |
| Etcdctl | LLGoNoLTO | 219324.8 ms | 214904.4 ms | 4420.4 ms | 71171.4 ms |
| Etcdctl | LLGoDeadcodeDrop | 217819.6 ms | 212398.4 ms | 5421.2 ms | 72040.2 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 209616.0 ms | 206174.5 ms | 3441.5 ms | 147076.4 ms |
| XGo | LLGoFullLTOGlobalDCE | 206393.8 ms | 203017.0 ms | 3376.8 ms | 145021.1 ms |
| XGo | LLGoFullLTONoGlobalDCE | 204227.4 ms | 200829.0 ms | 3398.4 ms | 144995.4 ms |
| Uber_zap | LLGoDeadcodeDrop | 200178.7 ms | 197372.8 ms | 2806.0 ms | 74130.4 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 198302.4 ms | 195553.7 ms | 2748.7 ms | 123050.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 193307.8 ms | 190352.6 ms | 2955.2 ms | 112580.3 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 193290.2 ms | 190328.8 ms | 2961.3 ms | 120427.1 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 192367.4 ms | 189388.2 ms | 2979.2 ms | 119286.7 ms |
| Uber_zap | LLGoNoLTO | 191493.1 ms | 189088.3 ms | 2404.8 ms | 69587.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 189580.6 ms | 186875.4 ms | 2705.3 ms | 113450.3 ms |
| K8s_workqueue | LLGoNoLTO | 188727.0 ms | 186087.2 ms | 2639.8 ms | 68883.1 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 183908.4 ms | 181119.3 ms | 2789.1 ms | 67875.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 176328.5 ms | 173480.3 ms | 2848.1 ms | 103115.7 ms |
| XGo | LLGoDeadcodeDrop | 124809.4 ms | 121231.7 ms | 3577.8 ms | 45569.7 ms |
| XGo | LLGoNoLTO | 122315.3 ms | 119792.2 ms | 2523.0 ms | 44006.8 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 109854.0 ms | 107972.0 ms | 1882.0 ms | 65367.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 109085.2 ms | 107141.8 ms | 1943.3 ms | 64721.2 ms |
| Gorm_schema | LLGoDeadcodeDrop | 102320.2 ms | 100456.4 ms | 1863.8 ms | 33419.3 ms |
| Toml | LLGoNoLTO | 101229.3 ms | 99473.1 ms | 1756.2 ms | 32622.0 ms |
| Gorm_schema | LLGoNoLTO | 100866.7 ms | 99266.5 ms | 1600.2 ms | 32665.8 ms |
| Toml | LLGoDeadcodeDrop | 95607.9 ms | 93685.9 ms | 1922.0 ms | 31285.2 ms |
| Toml | LLGoFullLTONoGlobalDCE | 91841.5 ms | 89989.4 ms | 1852.1 ms | 53640.8 ms |
| Toml | LLGoFullLTOGlobalDCE | 90008.1 ms | 88109.2 ms | 1898.9 ms | 48311.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 89112.3 ms | 87389.4 ms | 1723.0 ms | 46767.3 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 88782.2 ms | 86915.7 ms | 1866.5 ms | 47658.7 ms |
| IXGo | Go | 87428.4 ms | 82171.8 ms | 5256.6 ms | 24080.9 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 68191.5 ms | 66760.2 ms | 1431.3 ms | 24402.0 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 65045.9 ms | 63824.7 ms | 1221.2 ms | 39894.9 ms |
| Dustin_humanize | LLGoNoLTO | 64807.6 ms | 63704.4 ms | 1103.2 ms | 22720.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 56241.6 ms | 55034.1 ms | 1207.5 ms | 30337.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 56183.1 ms | 54883.7 ms | 1299.3 ms | 30377.1 ms |
| Etcdctl | Go | 33776.7 ms | 31597.2 ms | 2179.5 ms | 11036.2 ms |
| XGo | Go | 19202.6 ms | 17991.8 ms | 1210.8 ms | 6131.7 ms |
| Aws_restjson | Go | 7766.1 ms | 7091.4 ms | 674.7 ms | 3181.0 ms |
| Gorm_schema | Go | 5777.6 ms | 5379.4 ms | 398.2 ms | 2289.1 ms |
| Uber_zap | Go | 5244.3 ms | 4825.6 ms | 418.7 ms | 2038.4 ms |
| K8s_workqueue | Go | 4649.4 ms | 4209.7 ms | 439.6 ms | 1631.9 ms |
| Toml | Go | 2013.4 ms | 1765.4 ms | 248.0 ms | 911.4 ms |
| Dustin_humanize | Go | 807.2 ms | 642.9 ms | 164.3 ms | 375.3 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTOGlobalDCE | 2105776.3 ms | 1195898.7 ms | 9 |
| LLGoFullLTONoGlobalDCE | 2003646.1 ms | 1200488.4 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1956418.6 ms | 1125410.8 ms | 9 |
| LLGoNoLTO | 1722702.3 ms | 564417.6 ms | 9 |
| LLGoDeadcodeDrop | 1695884.2 ms | 569847.5 ms | 9 |
| Go | 166665.6 ms | 51675.8 ms | 9 |

Dependency download details are in `download-timings.log`.
