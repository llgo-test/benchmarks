## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 657986.8 ms | 641588.6 ms | 16398.2 ms | 435788.2 ms |
| IXGo | LLGoFullLTOGlobalDCE | 627888.9 ms | 612051.2 ms | 15837.7 ms | 417463.3 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 626398.7 ms | 610345.0 ms | 16053.7 ms | 415174.7 ms |
| IXGo | LLGoDeadcodeDrop | 373169.5 ms | 356247.9 ms | 16921.6 ms | 121287.3 ms |
| IXGo | LLGoNoLTO | 360157.9 ms | 345873.4 ms | 14284.6 ms | 112683.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 346021.2 ms | 338357.5 ms | 7663.8 ms | 259140.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 336545.9 ms | 328928.7 ms | 7617.1 ms | 249953.1 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 327226.5 ms | 319964.3 ms | 7262.1 ms | 245111.8 ms |
| XGo | LLGoFullLTONoGlobalDCE | 244307.1 ms | 239277.4 ms | 5029.7 ms | 198671.8 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 229605.2 ms | 225458.7 ms | 4146.5 ms | 158183.2 ms |
| XGo | LLGoFullLTOGlobalDCE | 219249.3 ms | 214198.5 ms | 5050.8 ms | 171184.7 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 217439.4 ms | 212559.6 ms | 4879.8 ms | 169124.1 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 217287.6 ms | 213098.0 ms | 4189.7 ms | 141323.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 212790.8 ms | 208588.2 ms | 4202.5 ms | 137900.5 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 194421.8 ms | 190957.0 ms | 3464.8 ms | 140988.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 191712.4 ms | 188036.3 ms | 3676.1 ms | 138405.5 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 190966.0 ms | 187256.6 ms | 3709.4 ms | 138353.1 ms |
| Aws_restjson | LLGoDeadcodeDrop | 178024.6 ms | 174252.9 ms | 3771.7 ms | 57218.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 177449.5 ms | 173881.0 ms | 3568.5 ms | 122694.9 ms |
| Aws_restjson | LLGoNoLTO | 177354.4 ms | 173834.3 ms | 3520.1 ms | 55571.5 ms |
| Etcdctl | LLGoNoLTO | 175055.8 ms | 168911.8 ms | 6143.9 ms | 60453.7 ms |
| Etcdctl | LLGoDeadcodeDrop | 174673.6 ms | 168138.1 ms | 6535.5 ms | 61401.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 168755.2 ms | 165243.3 ms | 3511.9 ms | 114839.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 155978.0 ms | 152657.9 ms | 3320.1 ms | 105211.3 ms |
| Uber_zap | LLGoDeadcodeDrop | 149310.1 ms | 145985.8 ms | 3324.3 ms | 49475.4 ms |
| Uber_zap | LLGoNoLTO | 142235.3 ms | 139288.3 ms | 2947.0 ms | 45974.4 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 137705.4 ms | 134544.5 ms | 3161.0 ms | 46194.1 ms |
| K8s_workqueue | LLGoNoLTO | 135916.4 ms | 132978.5 ms | 2937.8 ms | 43918.5 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 110872.7 ms | 108306.2 ms | 2566.5 ms | 78520.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 108229.8 ms | 105738.7 ms | 2491.1 ms | 75746.6 ms |
| Toml | LLGoFullLTONoGlobalDCE | 103715.8 ms | 101403.3 ms | 2312.5 ms | 73200.9 ms |
| XGo | LLGoNoLTO | 97430.8 ms | 93533.2 ms | 3897.6 ms | 36398.2 ms |
| XGo | LLGoDeadcodeDrop | 95281.0 ms | 91005.5 ms | 4275.5 ms | 35585.7 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 94171.0 ms | 91866.6 ms | 2304.4 ms | 61880.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 93012.2 ms | 90656.7 ms | 2355.5 ms | 59832.0 ms |
| Toml | LLGoFullLTOGlobalDCE | 91601.2 ms | 89394.6 ms | 2206.6 ms | 60715.0 ms |
| Gorm_schema | LLGoDeadcodeDrop | 80169.2 ms | 77891.5 ms | 2277.7 ms | 28506.9 ms |
| Gorm_schema | LLGoNoLTO | 79120.2 ms | 77037.3 ms | 2082.8 ms | 27652.5 ms |
| Toml | LLGoNoLTO | 73431.5 ms | 71654.4 ms | 1777.1 ms | 25628.8 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 72602.9 ms | 71063.1 ms | 1539.8 ms | 53442.7 ms |
| Toml | LLGoDeadcodeDrop | 72502.4 ms | 70669.8 ms | 1832.6 ms | 25517.1 ms |
| IXGo | Go | 63607.3 ms | 55427.4 ms | 8180.0 ms | 17376.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 58214.3 ms | 56703.3 ms | 1511.0 ms | 38599.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 57669.4 ms | 56208.1 ms | 1461.3 ms | 37954.0 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 53521.0 ms | 51995.1 ms | 1525.9 ms | 20417.0 ms |
| Dustin_humanize | LLGoNoLTO | 51794.5 ms | 50475.2 ms | 1319.3 ms | 19702.7 ms |
| Etcdctl | Go | 25335.1 ms | 22402.7 ms | 2932.3 ms | 7645.9 ms |
| XGo | Go | 14225.9 ms | 12623.0 ms | 1603.0 ms | 4264.8 ms |
| Aws_restjson | Go | 6119.5 ms | 5204.5 ms | 915.0 ms | 2516.7 ms |
| Gorm_schema | Go | 4476.4 ms | 3948.9 ms | 527.5 ms | 1747.7 ms |
| Uber_zap | Go | 4131.1 ms | 3634.3 ms | 496.8 ms | 1622.9 ms |
| K8s_workqueue | Go | 3596.9 ms | 3108.0 ms | 488.8 ms | 1306.1 ms |
| Toml | Go | 1578.6 ms | 1356.2 ms | 222.4 ms | 740.8 ms |
| Dustin_humanize | Go | 619.4 ms | 467.9 ms | 151.5 ms | 368.4 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2100116.6 ms | 1501646.9 ms | 9 |
| LLGoFullLTOGlobalDCE | 2023682.1 ms | 1412663.4 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2008320.9 ms | 1385093.5 ms | 9 |
| LLGoDeadcodeDrop | 1314356.9 ms | 445603.1 ms | 9 |
| LLGoNoLTO | 1292496.8 ms | 427983.6 ms | 9 |
| Go | 123690.3 ms | 37590.0 ms | 9 |

Dependency download details are in `download-timings.log`.
