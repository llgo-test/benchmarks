## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 926227.2 ms | 903601.7 ms | 22625.5 ms | 589486.8 ms |
| IXGo | LLGoFullLTOGlobalDCE | 894723.6 ms | 872630.0 ms | 22093.6 ms | 571968.3 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 890645.4 ms | 868153.2 ms | 22492.3 ms | 568251.3 ms |
| IXGo | LLGoDeadcodeDrop | 508848.4 ms | 486403.2 ms | 22445.3 ms | 161240.6 ms |
| IXGo | LLGoNoLTO | 493345.4 ms | 474860.4 ms | 18485.1 ms | 149352.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 450248.9 ms | 439547.0 ms | 10701.9 ms | 334135.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 443442.1 ms | 433079.1 ms | 10363.0 ms | 328309.5 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 442310.6 ms | 432065.6 ms | 10245.0 ms | 330429.8 ms |
| XGo | LLGoFullLTONoGlobalDCE | 325600.9 ms | 318832.9 ms | 6768.1 ms | 263491.3 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 305339.8 ms | 299819.9 ms | 5519.9 ms | 212387.7 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 283820.5 ms | 277164.9 ms | 6655.6 ms | 221503.7 ms |
| XGo | LLGoFullLTOGlobalDCE | 281912.2 ms | 275405.5 ms | 6506.7 ms | 218825.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 274842.7 ms | 269438.2 ms | 5404.4 ms | 179687.3 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 273242.8 ms | 267848.4 ms | 5394.4 ms | 178883.6 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 249975.9 ms | 245285.9 ms | 4690.0 ms | 180370.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 242574.4 ms | 237721.1 ms | 4853.3 ms | 174152.5 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 239312.7 ms | 234617.3 ms | 4695.4 ms | 173675.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 227919.6 ms | 223236.7 ms | 4682.9 ms | 156998.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 224447.0 ms | 219745.2 ms | 4701.9 ms | 153334.4 ms |
| Etcdctl | LLGoDeadcodeDrop | 220516.4 ms | 211614.5 ms | 8901.9 ms | 75894.0 ms |
| Etcdctl | LLGoNoLTO | 219995.8 ms | 211672.9 ms | 8323.0 ms | 74697.6 ms |
| Aws_restjson | LLGoDeadcodeDrop | 209441.1 ms | 204871.3 ms | 4569.9 ms | 66059.0 ms |
| Aws_restjson | LLGoNoLTO | 209104.5 ms | 204854.6 ms | 4249.9 ms | 65700.8 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 204080.4 ms | 199544.6 ms | 4535.8 ms | 137846.4 ms |
| Uber_zap | LLGoDeadcodeDrop | 167942.0 ms | 164104.9 ms | 3837.1 ms | 54584.7 ms |
| Uber_zap | LLGoNoLTO | 167266.1 ms | 163543.3 ms | 3722.8 ms | 53983.6 ms |
| K8s_workqueue | LLGoNoLTO | 159821.3 ms | 156298.1 ms | 3523.2 ms | 51567.8 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 159075.3 ms | 155211.7 ms | 3863.6 ms | 52150.3 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 148136.1 ms | 144734.1 ms | 3402.0 ms | 106227.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 144274.8 ms | 140921.1 ms | 3353.7 ms | 102650.7 ms |
| Toml | LLGoFullLTONoGlobalDCE | 135641.5 ms | 132440.6 ms | 3200.9 ms | 96223.6 ms |
| XGo | LLGoNoLTO | 123819.6 ms | 118510.0 ms | 5309.6 ms | 45386.7 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 121682.9 ms | 118623.3 ms | 3059.7 ms | 79153.3 ms |
| XGo | LLGoDeadcodeDrop | 121567.1 ms | 115740.7 ms | 5826.4 ms | 43677.8 ms |
| Toml | LLGoFullLTOGlobalDCE | 117565.3 ms | 114772.3 ms | 2793.0 ms | 77481.0 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 115690.3 ms | 112999.8 ms | 2690.5 ms | 76224.4 ms |
| Gorm_schema | LLGoDeadcodeDrop | 102925.9 ms | 99985.6 ms | 2940.3 ms | 35987.5 ms |
| Gorm_schema | LLGoNoLTO | 102739.1 ms | 99822.7 ms | 2916.5 ms | 35440.4 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 96845.1 ms | 94730.3 ms | 2114.8 ms | 71352.7 ms |
| Toml | LLGoNoLTO | 94775.6 ms | 92244.4 ms | 2531.3 ms | 32151.4 ms |
| Toml | LLGoDeadcodeDrop | 93664.1 ms | 91180.1 ms | 2484.0 ms | 32460.3 ms |
| IXGo | Go | 90236.0 ms | 78518.9 ms | 11717.1 ms | 24444.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 75721.9 ms | 73875.9 ms | 1846.0 ms | 50144.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 75003.5 ms | 73162.2 ms | 1841.3 ms | 49841.8 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 66136.9 ms | 64303.6 ms | 1833.4 ms | 24830.6 ms |
| Dustin_humanize | LLGoNoLTO | 64969.7 ms | 63308.7 ms | 1661.0 ms | 24120.5 ms |
| Etcdctl | Go | 35940.6 ms | 31793.8 ms | 4146.8 ms | 10706.2 ms |
| XGo | Go | 20691.5 ms | 18243.1 ms | 2448.4 ms | 6056.2 ms |
| Aws_restjson | Go | 8702.6 ms | 7514.9 ms | 1187.7 ms | 3544.9 ms |
| Gorm_schema | Go | 6263.0 ms | 5469.4 ms | 793.6 ms | 2411.4 ms |
| Uber_zap | Go | 5761.6 ms | 5076.0 ms | 685.7 ms | 2245.9 ms |
| K8s_workqueue | Go | 4978.5 ms | 4338.7 ms | 639.8 ms | 1756.3 ms |
| Toml | Go | 2166.0 ms | 1861.7 ms | 304.3 ms | 987.4 ms |
| Dustin_humanize | Go | 866.5 ms | 715.2 ms | 151.3 ms | 421.7 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2833808.1 ms | 2002409.5 ms | 9 |
| LLGoFullLTOGlobalDCE | 2702258.2 ms | 1859915.3 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2675162.1 ms | 1820712.6 ms | 9 |
| LLGoDeadcodeDrop | 1650117.3 ms | 546884.8 ms | 9 |
| LLGoNoLTO | 1635837.3 ms | 532400.9 ms | 9 |
| Go | 175606.3 ms | 52574.3 ms | 9 |

Dependency download details are in `download-timings.log`.
