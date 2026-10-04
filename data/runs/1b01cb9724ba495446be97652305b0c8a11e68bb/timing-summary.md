## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 680611.0 ms | 671182.2 ms | 9428.8 ms | 346815.0 ms |
| IXGo | LLGoFullLTOGlobalDCE | 668759.4 ms | 659110.1 ms | 9649.3 ms | 340969.7 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 652570.8 ms | 642402.7 ms | 10168.1 ms | 336774.1 ms |
| IXGo | LLGoNoLTO | 645249.2 ms | 635290.3 ms | 9959.0 ms | 183138.5 ms |
| IXGo | LLGoDeadcodeDrop | 578839.0 ms | 563644.3 ms | 15194.8 ms | 171690.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 353823.7 ms | 348300.3 ms | 5523.4 ms | 206247.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 343743.3 ms | 338474.7 ms | 5268.5 ms | 201062.0 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 334410.9 ms | 329307.2 ms | 5103.7 ms | 197312.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 286981.6 ms | 282934.0 ms | 4047.6 ms | 147283.5 ms |
| Aws_restjson | LLGoDeadcodeDrop | 280338.4 ms | 276915.7 ms | 3422.7 ms | 93656.0 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 277235.2 ms | 273517.6 ms | 3717.6 ms | 157329.7 ms |
| Aws_restjson | LLGoNoLTO | 271345.2 ms | 267999.4 ms | 3345.8 ms | 90415.9 ms |
| Etcdctl | LLGoDeadcodeDrop | 259482.9 ms | 253724.7 ms | 5758.2 ms | 86127.6 ms |
| Etcdctl | LLGoNoLTO | 259028.5 ms | 254690.6 ms | 4337.9 ms | 84951.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 255395.8 ms | 251513.0 ms | 3882.8 ms | 134138.6 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 253883.1 ms | 250242.0 ms | 3641.0 ms | 163644.4 ms |
| XGo | LLGoFullLTONoGlobalDCE | 249796.7 ms | 246445.5 ms | 3351.2 ms | 164892.3 ms |
| XGo | LLGoFullLTOGlobalDCE | 239380.3 ms | 236108.8 ms | 3271.4 ms | 155630.6 ms |
| Uber_zap | LLGoDeadcodeDrop | 233643.6 ms | 230765.3 ms | 2878.3 ms | 81603.5 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 233263.9 ms | 229974.8 ms | 3289.1 ms | 133779.1 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 231541.4 ms | 228111.0 ms | 3430.5 ms | 134450.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 230825.9 ms | 227375.4 ms | 3450.6 ms | 132340.8 ms |
| Uber_zap | LLGoNoLTO | 226996.1 ms | 224079.6 ms | 2916.5 ms | 79891.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 222611.2 ms | 219298.1 ms | 3313.1 ms | 121651.6 ms |
| K8s_workqueue | LLGoNoLTO | 220391.2 ms | 217581.5 ms | 2809.7 ms | 77702.0 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 220334.9 ms | 217464.6 ms | 2870.3 ms | 77427.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 220108.2 ms | 216893.6 ms | 3214.6 ms | 120076.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 210026.3 ms | 206712.9 ms | 3313.4 ms | 112475.1 ms |
| XGo | LLGoDeadcodeDrop | 168003.8 ms | 164197.4 ms | 3806.4 ms | 61141.9 ms |
| XGo | LLGoNoLTO | 159058.9 ms | 156331.2 ms | 2727.7 ms | 57439.7 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 107833.3 ms | 105793.4 ms | 2039.9 ms | 62096.1 ms |
| Gorm_schema | LLGoNoLTO | 107795.8 ms | 106016.9 ms | 1778.9 ms | 35742.7 ms |
| Toml | LLGoDeadcodeDrop | 107689.0 ms | 105751.0 ms | 1938.0 ms | 35637.1 ms |
| Gorm_schema | LLGoDeadcodeDrop | 107683.0 ms | 106003.9 ms | 1679.1 ms | 35691.1 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 106913.7 ms | 104976.0 ms | 1937.7 ms | 61685.7 ms |
| Toml | LLGoFullLTONoGlobalDCE | 104463.6 ms | 102426.8 ms | 2036.8 ms | 60242.0 ms |
| Toml | LLGoNoLTO | 102345.7 ms | 100608.8 ms | 1736.9 ms | 33723.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 96204.1 ms | 94221.6 ms | 1982.6 ms | 49720.5 ms |
| Toml | LLGoFullLTOGlobalDCE | 95322.6 ms | 93332.8 ms | 1989.8 ms | 50915.4 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 89332.7 ms | 87455.3 ms | 1877.4 ms | 46632.9 ms |
| IXGo | Go | 86684.9 ms | 81532.2 ms | 5152.7 ms | 24038.1 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 71534.9 ms | 70157.0 ms | 1377.9 ms | 43333.2 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 70161.0 ms | 68946.8 ms | 1214.2 ms | 25087.0 ms |
| Dustin_humanize | LLGoNoLTO | 69995.2 ms | 68783.8 ms | 1211.4 ms | 24978.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 62615.8 ms | 61236.7 ms | 1379.2 ms | 33550.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 62019.0 ms | 60664.0 ms | 1355.0 ms | 33151.8 ms |
| Etcdctl | Go | 35332.4 ms | 33141.0 ms | 2191.4 ms | 10677.6 ms |
| XGo | Go | 20185.2 ms | 18947.0 ms | 1238.2 ms | 5941.4 ms |
| Aws_restjson | Go | 7843.0 ms | 7170.3 ms | 672.7 ms | 3135.2 ms |
| Gorm_schema | Go | 6079.1 ms | 5684.7 ms | 394.3 ms | 2367.7 ms |
| Uber_zap | Go | 5284.1 ms | 4864.7 ms | 419.4 ms | 2075.6 ms |
| K8s_workqueue | Go | 5039.1 ms | 4578.5 ms | 460.7 ms | 1788.8 ms |
| Toml | Go | 2077.6 ms | 1839.9 ms | 237.7 ms | 958.9 ms |
| Dustin_humanize | Go | 867.8 ms | 702.2 ms | 165.6 ms | 413.1 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2261731.2 ms | 1289799.0 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2242909.4 ms | 1220862.0 ms | 9 |
| LLGoFullLTOGlobalDCE | 2236568.0 ms | 1237540.3 ms | 9 |
| LLGoNoLTO | 2062205.9 ms | 667984.1 ms | 9 |
| LLGoDeadcodeDrop | 2026175.5 ms | 668062.7 ms | 9 |
| Go | 169393.2 ms | 51396.4 ms | 9 |

Dependency download details are in `download-timings.log`.
