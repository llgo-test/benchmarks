## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTONoGlobalDCE | 890585.2 ms | 878026.0 ms | 12559.3 ms | 562020.3 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 887565.1 ms | 874789.8 ms | 12775.3 ms | 564744.8 ms |
| IXGo | LLGoFullLTOGlobalDCE | 880694.3 ms | 867635.8 ms | 13058.5 ms | 557058.9 ms |
| IXGo | LLGoDeadcodeDrop | 527298.2 ms | 513252.4 ms | 14045.8 ms | 166132.9 ms |
| IXGo | LLGoNoLTO | 521319.1 ms | 511781.4 ms | 9537.7 ms | 161204.6 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 442363.9 ms | 436415.1 ms | 5948.8 ms | 325776.1 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 438750.4 ms | 432748.4 ms | 6002.0 ms | 325796.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 436136.4 ms | 430171.8 ms | 5964.6 ms | 322592.5 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 331119.5 ms | 327068.6 ms | 4051.0 ms | 229639.2 ms |
| XGo | LLGoFullLTONoGlobalDCE | 330742.1 ms | 326454.6 ms | 4287.5 ms | 267425.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 301812.0 ms | 297861.8 ms | 3950.2 ms | 198546.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 300584.9 ms | 296621.2 ms | 3963.7 ms | 197167.9 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 290231.1 ms | 286106.3 ms | 4124.9 ms | 226075.6 ms |
| XGo | LLGoFullLTOGlobalDCE | 289150.8 ms | 285244.4 ms | 3906.3 ms | 225349.3 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 280279.2 ms | 276713.9 ms | 3565.2 ms | 202775.4 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 271608.8 ms | 267911.8 ms | 3697.0 ms | 197571.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 271474.5 ms | 267795.5 ms | 3679.0 ms | 197012.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 255299.9 ms | 251922.9 ms | 3377.0 ms | 176561.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 253701.1 ms | 250339.9 ms | 3361.2 ms | 175750.8 ms |
| Aws_restjson | LLGoNoLTO | 241852.5 ms | 238581.0 ms | 3271.5 ms | 85695.2 ms |
| Aws_restjson | LLGoDeadcodeDrop | 239202.5 ms | 235616.3 ms | 3586.2 ms | 84513.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 237862.4 ms | 234329.3 ms | 3533.1 ms | 162980.0 ms |
| Etcdctl | LLGoDeadcodeDrop | 228340.8 ms | 223065.0 ms | 5275.8 ms | 81626.9 ms |
| Etcdctl | LLGoNoLTO | 227809.1 ms | 223185.8 ms | 4623.3 ms | 80812.9 ms |
| Uber_zap | LLGoNoLTO | 200877.4 ms | 198077.3 ms | 2800.1 ms | 75600.2 ms |
| Uber_zap | LLGoDeadcodeDrop | 198954.7 ms | 195952.7 ms | 3002.0 ms | 75015.0 ms |
| K8s_workqueue | LLGoNoLTO | 192214.2 ms | 189565.3 ms | 2648.9 ms | 72554.9 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 191619.5 ms | 188546.9 ms | 3072.6 ms | 72808.7 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 145754.1 ms | 143530.6 ms | 2223.5 ms | 103153.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 144386.2 ms | 142134.8 ms | 2251.4 ms | 101571.8 ms |
| Toml | LLGoFullLTONoGlobalDCE | 133419.6 ms | 131141.2 ms | 2278.3 ms | 93308.5 ms |
| XGo | LLGoNoLTO | 131404.9 ms | 128604.1 ms | 2800.8 ms | 51380.5 ms |
| XGo | LLGoDeadcodeDrop | 130453.5 ms | 126805.4 ms | 3648.1 ms | 50990.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 119654.3 ms | 117604.3 ms | 2050.0 ms | 75792.2 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 114656.2 ms | 112436.7 ms | 2219.5 ms | 73969.4 ms |
| Toml | LLGoFullLTOGlobalDCE | 114632.7 ms | 112433.8 ms | 2199.0 ms | 74308.9 ms |
| Gorm_schema | LLGoDeadcodeDrop | 106708.3 ms | 104806.7 ms | 1901.6 ms | 36537.6 ms |
| Gorm_schema | LLGoNoLTO | 105709.3 ms | 104006.4 ms | 1702.9 ms | 35881.9 ms |
| Toml | LLGoNoLTO | 99909.9 ms | 97958.9 ms | 1951.1 ms | 33412.0 ms |
| Toml | LLGoDeadcodeDrop | 99495.1 ms | 97493.8 ms | 2001.3 ms | 33737.0 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 96076.3 ms | 94472.1 ms | 1604.2 ms | 70196.1 ms |
| IXGo | Go | 84732.0 ms | 79558.3 ms | 5173.7 ms | 23243.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 75108.5 ms | 73559.3 ms | 1549.2 ms | 48935.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 75097.6 ms | 73717.3 ms | 1380.3 ms | 48941.1 ms |
| Dustin_humanize | LLGoNoLTO | 68674.4 ms | 67396.1 ms | 1278.3 ms | 24937.0 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 68479.5 ms | 67053.8 ms | 1425.7 ms | 25132.9 ms |
| Etcdctl | Go | 33609.3 ms | 31559.4 ms | 2049.9 ms | 10305.6 ms |
| XGo | Go | 19417.9 ms | 18245.3 ms | 1172.6 ms | 5744.9 ms |
| Aws_restjson | Go | 8298.5 ms | 7373.6 ms | 925.0 ms | 4284.4 ms |
| Gorm_schema | Go | 5772.7 ms | 5366.6 ms | 406.0 ms | 2270.5 ms |
| Uber_zap | Go | 5304.3 ms | 4893.6 ms | 410.7 ms | 2084.6 ms |
| K8s_workqueue | Go | 4728.9 ms | 4279.2 ms | 449.7 ms | 1689.5 ms |
| Toml | Go | 2045.9 ms | 1822.7 ms | 223.2 ms | 933.2 ms |
| Dustin_humanize | Go | 805.3 ms | 661.4 ms | 143.9 ms | 388.9 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2918335.2 ms | 2051886.1 ms | 9 |
| LLGoFullLTOGlobalDCE | 2767085.6 ms | 1901132.5 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2723326.3 ms | 1852002.8 ms | 9 |
| LLGoDeadcodeDrop | 1790552.2 ms | 626494.2 ms | 9 |
| LLGoNoLTO | 1789770.8 ms | 621479.2 ms | 9 |
| Go | 164714.9 ms | 50945.1 ms | 9 |

Dependency download details are in `download-timings.log`.
