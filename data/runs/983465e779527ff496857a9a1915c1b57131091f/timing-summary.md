## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 917757.4 ms | 896414.0 ms | 21343.4 ms | 569858.5 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 862754.1 ms | 841182.9 ms | 21571.2 ms | 553406.2 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 843012.1 ms | 822409.6 ms | 20602.5 ms | 548935.7 ms |
| IXGo | LLGoDeadcodeDrop | 507407.1 ms | 485753.6 ms | 21653.5 ms | 157426.8 ms |
| IXGo | LLGoNoLTO | 505464.0 ms | 487778.6 ms | 17685.4 ms | 151792.8 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 427667.0 ms | 417950.3 ms | 9716.7 ms | 319691.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 426039.7 ms | 416484.2 ms | 9555.6 ms | 316259.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 418551.5 ms | 408879.6 ms | 9671.9 ms | 310699.4 ms |
| XGo | LLGoFullLTONoGlobalDCE | 313684.9 ms | 306972.2 ms | 6712.7 ms | 254889.2 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 302179.6 ms | 296727.4 ms | 5452.2 ms | 209350.0 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 273264.2 ms | 266834.6 ms | 6429.6 ms | 212952.4 ms |
| XGo | LLGoFullLTOGlobalDCE | 270321.6 ms | 263912.2 ms | 6409.3 ms | 210768.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 262477.1 ms | 257389.5 ms | 5087.6 ms | 171995.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 259991.9 ms | 254894.8 ms | 5097.1 ms | 170445.3 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 247210.6 ms | 242581.2 ms | 4629.4 ms | 179634.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 237256.1 ms | 232712.6 ms | 4543.5 ms | 173036.7 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 233363.1 ms | 228918.7 ms | 4444.4 ms | 169588.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 221765.6 ms | 217251.7 ms | 4513.9 ms | 151412.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 213045.6 ms | 208810.8 ms | 4234.8 ms | 145929.8 ms |
| Etcdctl | LLGoDeadcodeDrop | 212449.2 ms | 203902.4 ms | 8546.8 ms | 73284.5 ms |
| Etcdctl | LLGoNoLTO | 210505.6 ms | 202441.3 ms | 8064.3 ms | 72126.1 ms |
| Aws_restjson | LLGoNoLTO | 203709.2 ms | 199324.0 ms | 4385.2 ms | 64032.4 ms |
| Aws_restjson | LLGoDeadcodeDrop | 200692.1 ms | 196194.4 ms | 4497.8 ms | 63318.1 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 197905.3 ms | 193794.9 ms | 4110.4 ms | 133655.0 ms |
| Uber_zap | LLGoNoLTO | 162085.1 ms | 158615.4 ms | 3469.7 ms | 52389.3 ms |
| Uber_zap | LLGoDeadcodeDrop | 161309.7 ms | 157626.9 ms | 3682.8 ms | 52647.0 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 153733.3 ms | 150022.8 ms | 3710.4 ms | 50586.6 ms |
| K8s_workqueue | LLGoNoLTO | 150947.5 ms | 147664.8 ms | 3282.7 ms | 48870.1 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 143113.7 ms | 139929.3 ms | 3184.4 ms | 103537.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 142337.7 ms | 139130.3 ms | 3207.4 ms | 101171.9 ms |
| Toml | LLGoFullLTONoGlobalDCE | 130184.7 ms | 127429.1 ms | 2755.6 ms | 92525.2 ms |
| XGo | LLGoNoLTO | 117042.3 ms | 111937.3 ms | 5105.0 ms | 42620.7 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 116135.1 ms | 113131.9 ms | 3003.2 ms | 75210.0 ms |
| XGo | LLGoDeadcodeDrop | 115644.3 ms | 110029.6 ms | 5614.7 ms | 41973.6 ms |
| Toml | LLGoFullLTOGlobalDCE | 110347.4 ms | 107708.6 ms | 2638.8 ms | 72863.7 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 110239.5 ms | 107608.9 ms | 2630.6 ms | 72706.6 ms |
| Gorm_schema | LLGoNoLTO | 98925.4 ms | 96318.1 ms | 2607.3 ms | 33879.3 ms |
| Gorm_schema | LLGoDeadcodeDrop | 98490.0 ms | 95648.9 ms | 2841.1 ms | 34528.8 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 92887.9 ms | 90824.1 ms | 2063.8 ms | 68760.9 ms |
| Toml | LLGoDeadcodeDrop | 92102.1 ms | 89689.6 ms | 2412.5 ms | 31705.2 ms |
| Toml | LLGoNoLTO | 91488.6 ms | 89199.1 ms | 2289.5 ms | 31104.4 ms |
| IXGo | Go | 87335.5 ms | 75969.1 ms | 11366.4 ms | 23659.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 73150.4 ms | 71257.3 ms | 1893.1 ms | 48543.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 72496.6 ms | 70692.7 ms | 1804.0 ms | 48087.0 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 63414.0 ms | 61687.3 ms | 1726.7 ms | 23629.9 ms |
| Dustin_humanize | LLGoNoLTO | 62645.5 ms | 61071.0 ms | 1574.5 ms | 23209.6 ms |
| Etcdctl | Go | 34864.6 ms | 30825.0 ms | 4039.6 ms | 10433.8 ms |
| XGo | Go | 20284.4 ms | 17879.9 ms | 2404.5 ms | 5984.9 ms |
| Aws_restjson | Go | 8391.5 ms | 7192.6 ms | 1198.9 ms | 3339.2 ms |
| Gorm_schema | Go | 6124.0 ms | 5396.0 ms | 727.9 ms | 2336.6 ms |
| Uber_zap | Go | 5630.2 ms | 5001.2 ms | 629.0 ms | 2217.7 ms |
| K8s_workqueue | Go | 4971.6 ms | 4237.3 ms | 734.2 ms | 2074.0 ms |
| Toml | Go | 2168.6 ms | 1842.1 ms | 326.6 ms | 1005.2 ms |
| Dustin_humanize | Go | 824.2 ms | 639.3 ms | 184.9 ms | 393.3 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2733303.7 ms | 1946912.5 ms | 9 |
| LLGoFullLTOGlobalDCE | 2645244.7 ms | 1804867.4 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2540592.2 ms | 1734134.2 ms | 9 |
| LLGoDeadcodeDrop | 1605241.8 ms | 529100.5 ms | 9 |
| LLGoNoLTO | 1602813.3 ms | 520024.7 ms | 9 |
| Go | 170594.6 ms | 51443.8 ms | 9 |

Dependency download details are in `download-timings.log`.
