## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTONoGlobalDCE | 552014.1 ms | 540349.2 ms | 11665.0 ms | 285837.8 ms |
| IXGo | LLGoFullLTOGlobalDCE | 544912.1 ms | 532706.4 ms | 12205.8 ms | 291596.7 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 533717.3 ms | 520252.0 ms | 13465.3 ms | 285668.4 ms |
| IXGo | LLGoDeadcodeDrop | 418015.7 ms | 407139.8 ms | 10875.9 ms | 127452.8 ms |
| IXGo | LLGoNoLTO | 409978.6 ms | 400065.6 ms | 9912.9 ms | 123373.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 260650.8 ms | 256010.0 ms | 4640.8 ms | 159702.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 258785.8 ms | 253684.6 ms | 5101.2 ms | 159445.7 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 256708.2 ms | 252015.4 ms | 4692.8 ms | 159283.5 ms |
| Aws_restjson | LLGoDeadcodeDrop | 205246.1 ms | 202234.9 ms | 3011.2 ms | 74138.4 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 204289.4 ms | 201159.8 ms | 3129.6 ms | 121365.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 204180.0 ms | 201042.1 ms | 3137.9 ms | 115692.1 ms |
| Aws_restjson | LLGoNoLTO | 202550.4 ms | 199701.9 ms | 2848.5 ms | 73136.5 ms |
| Etcdctl | LLGoDeadcodeDrop | 194470.0 ms | 190307.5 ms | 4162.5 ms | 64961.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 192894.4 ms | 189815.6 ms | 3078.9 ms | 108826.5 ms |
| Etcdctl | LLGoNoLTO | 191039.3 ms | 186831.4 ms | 4207.9 ms | 64435.0 ms |
| XGo | LLGoFullLTONoGlobalDCE | 180965.0 ms | 177637.9 ms | 3327.1 ms | 125046.2 ms |
| XGo | LLGoFullLTOGlobalDCE | 180895.0 ms | 177427.3 ms | 3467.7 ms | 124126.9 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 180385.6 ms | 177011.9 ms | 3373.7 ms | 123967.3 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 176676.2 ms | 173880.1 ms | 2796.2 ms | 111462.4 ms |
| Uber_zap | LLGoDeadcodeDrop | 171660.7 ms | 169265.7 ms | 2395.0 ms | 65521.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 168965.1 ms | 166032.2 ms | 2932.9 ms | 106279.4 ms |
| Uber_zap | LLGoNoLTO | 168657.9 ms | 166211.7 ms | 2446.2 ms | 64877.8 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 166187.5 ms | 163559.6 ms | 2627.9 ms | 104415.7 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 163965.7 ms | 161420.8 ms | 2544.9 ms | 62943.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 163096.5 ms | 160449.2 ms | 2647.3 ms | 97601.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 162951.8 ms | 160271.9 ms | 2679.8 ms | 97899.1 ms |
| K8s_workqueue | LLGoNoLTO | 161388.2 ms | 158944.2 ms | 2443.9 ms | 62144.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 153649.3 ms | 150965.5 ms | 2683.8 ms | 90676.8 ms |
| XGo | LLGoDeadcodeDrop | 111862.8 ms | 109026.4 ms | 2836.4 ms | 42226.9 ms |
| XGo | LLGoNoLTO | 111368.2 ms | 108449.4 ms | 2918.9 ms | 42822.9 ms |
| Gorm_schema | LLGoDeadcodeDrop | 87523.6 ms | 86013.4 ms | 1510.2 ms | 29206.4 ms |
| Gorm_schema | LLGoNoLTO | 86894.8 ms | 85377.5 ms | 1517.2 ms | 28672.4 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 86668.8 ms | 84933.4 ms | 1735.4 ms | 51377.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 86350.4 ms | 84654.8 ms | 1695.5 ms | 50317.3 ms |
| IXGo | Go | 83701.3 ms | 78752.0 ms | 4949.3 ms | 22880.0 ms |
| Toml | LLGoDeadcodeDrop | 83556.2 ms | 81989.5 ms | 1566.7 ms | 27701.2 ms |
| Toml | LLGoNoLTO | 81787.9 ms | 80101.0 ms | 1686.9 ms | 27133.1 ms |
| Toml | LLGoFullLTONoGlobalDCE | 79563.6 ms | 77839.0 ms | 1724.7 ms | 46285.1 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 75922.0 ms | 74297.4 ms | 1624.6 ms | 39745.1 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 72777.1 ms | 71078.2 ms | 1698.9 ms | 38623.7 ms |
| Toml | LLGoFullLTOGlobalDCE | 71812.5 ms | 70182.6 ms | 1630.0 ms | 38216.3 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 55578.8 ms | 54540.3 ms | 1038.4 ms | 19867.5 ms |
| Dustin_humanize | LLGoNoLTO | 55471.9 ms | 54335.1 ms | 1136.7 ms | 19813.6 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 54725.9 ms | 53637.4 ms | 1088.5 ms | 33697.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 48315.8 ms | 47194.1 ms | 1121.7 ms | 26274.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 46641.6 ms | 45524.8 ms | 1116.8 ms | 25279.2 ms |
| Etcdctl | Go | 33385.1 ms | 31345.5 ms | 2039.6 ms | 10044.4 ms |
| XGo | Go | 19483.6 ms | 18003.0 ms | 1480.6 ms | 6235.8 ms |
| Aws_restjson | Go | 8370.8 ms | 7539.6 ms | 831.2 ms | 3840.1 ms |
| Gorm_schema | Go | 5989.9 ms | 5534.6 ms | 455.3 ms | 2333.1 ms |
| Uber_zap | Go | 5387.6 ms | 4966.0 ms | 421.6 ms | 2135.8 ms |
| K8s_workqueue | Go | 4876.2 ms | 4316.6 ms | 559.6 ms | 2261.5 ms |
| Toml | Go | 2185.4 ms | 1874.1 ms | 311.3 ms | 1336.4 ms |
| Dustin_humanize | Go | 813.8 ms | 680.0 ms | 133.8 ms | 378.7 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1757798.7 ms | 1038771.0 ms | 9 |
| LLGoFullLTOGlobalDCE | 1714208.8 ms | 1001987.0 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1692694.2 ms | 977951.3 ms | 9 |
| LLGoDeadcodeDrop | 1491879.6 ms | 514019.4 ms | 9 |
| LLGoNoLTO | 1469137.1 ms | 506409.6 ms | 9 |
| Go | 164193.7 ms | 51445.8 ms | 9 |

Dependency download details are in `download-timings.log`.
