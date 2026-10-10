## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 649972.5 ms | 637822.4 ms | 12150.1 ms | 338472.1 ms |
| IXGo | LLGoFullLTOGlobalDCE | 640230.9 ms | 630075.2 ms | 10155.8 ms | 338737.6 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 624051.7 ms | 613960.8 ms | 10090.9 ms | 332935.1 ms |
| IXGo | LLGoDeadcodeDrop | 559236.9 ms | 545769.3 ms | 13467.6 ms | 163387.0 ms |
| IXGo | LLGoNoLTO | 503001.3 ms | 493799.4 ms | 9201.9 ms | 145855.4 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 303758.5 ms | 298790.2 ms | 4968.3 ms | 191901.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 303426.3 ms | 298544.9 ms | 4881.4 ms | 188104.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 300550.0 ms | 295874.1 ms | 4675.9 ms | 187463.0 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 236823.7 ms | 233194.8 ms | 3628.9 ms | 142733.0 ms |
| Aws_restjson | LLGoNoLTO | 235858.5 ms | 232738.7 ms | 3119.8 ms | 82807.9 ms |
| Aws_restjson | LLGoDeadcodeDrop | 234645.9 ms | 231500.8 ms | 3145.1 ms | 81772.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 228607.2 ms | 224883.3 ms | 3723.9 ms | 130469.5 ms |
| Etcdctl | LLGoDeadcodeDrop | 226984.2 ms | 221757.2 ms | 5227.0 ms | 75729.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 222148.4 ms | 218539.4 ms | 3609.0 ms | 127006.1 ms |
| Etcdctl | LLGoNoLTO | 218225.8 ms | 213911.0 ms | 4314.9 ms | 71652.3 ms |
| XGo | LLGoFullLTONoGlobalDCE | 217643.0 ms | 214247.1 ms | 3395.9 ms | 154588.6 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 217172.3 ms | 213883.3 ms | 3289.0 ms | 152267.1 ms |
| XGo | LLGoFullLTOGlobalDCE | 211307.1 ms | 208009.9 ms | 3297.2 ms | 149619.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 199247.6 ms | 195976.4 ms | 3271.2 ms | 120232.2 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 198150.6 ms | 194918.4 ms | 3232.1 ms | 125423.0 ms |
| Uber_zap | LLGoDeadcodeDrop | 194600.8 ms | 191909.7 ms | 2691.2 ms | 72524.1 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 193835.6 ms | 190564.0 ms | 3271.6 ms | 122782.7 ms |
| Uber_zap | LLGoNoLTO | 193364.5 ms | 190824.9 ms | 2539.6 ms | 72131.2 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 191678.7 ms | 188452.1 ms | 3226.6 ms | 115227.2 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 191479.3 ms | 188281.8 ms | 3197.5 ms | 121510.7 ms |
| K8s_workqueue | LLGoNoLTO | 187950.2 ms | 185283.2 ms | 2667.0 ms | 70204.3 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 186587.2 ms | 183850.1 ms | 2737.0 ms | 70250.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 177101.6 ms | 173930.9 ms | 3170.8 ms | 105458.9 ms |
| XGo | LLGoDeadcodeDrop | 126608.9 ms | 122954.1 ms | 3654.8 ms | 47578.7 ms |
| XGo | LLGoNoLTO | 124491.1 ms | 121884.6 ms | 2606.5 ms | 45623.3 ms |
| Gorm_schema | LLGoDeadcodeDrop | 104686.5 ms | 102914.3 ms | 1772.3 ms | 34585.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 102378.3 ms | 100313.3 ms | 2065.0 ms | 59940.5 ms |
| Gorm_schema | LLGoNoLTO | 102004.0 ms | 100343.5 ms | 1660.5 ms | 33618.3 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 101984.3 ms | 99919.3 ms | 2065.0 ms | 60740.8 ms |
| Toml | LLGoDeadcodeDrop | 100752.0 ms | 98921.7 ms | 1830.3 ms | 33478.1 ms |
| Toml | LLGoNoLTO | 94778.2 ms | 93010.2 ms | 1768.0 ms | 31055.1 ms |
| Toml | LLGoFullLTONoGlobalDCE | 92641.2 ms | 90710.4 ms | 1930.8 ms | 54808.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 90383.4 ms | 88368.1 ms | 2015.3 ms | 48074.4 ms |
| IXGo | Go | 85363.7 ms | 80230.7 ms | 5133.0 ms | 23507.5 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 85361.8 ms | 83383.0 ms | 1978.8 ms | 46798.2 ms |
| Toml | LLGoFullLTOGlobalDCE | 84629.9 ms | 82716.0 ms | 1913.9 ms | 46295.0 ms |
| Dustin_humanize | LLGoNoLTO | 69563.6 ms | 68235.9 ms | 1327.7 ms | 24843.5 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 66281.6 ms | 65079.6 ms | 1202.0 ms | 23524.8 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 65944.5 ms | 64519.6 ms | 1425.0 ms | 41124.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 56533.1 ms | 55166.3 ms | 1366.8 ms | 31096.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 56111.4 ms | 54772.5 ms | 1338.9 ms | 30934.7 ms |
| Etcdctl | Go | 33947.9 ms | 31968.0 ms | 1979.9 ms | 10200.7 ms |
| XGo | Go | 19534.0 ms | 18323.1 ms | 1210.9 ms | 5807.6 ms |
| Aws_restjson | Go | 8017.7 ms | 7338.5 ms | 679.2 ms | 3213.2 ms |
| Gorm_schema | Go | 5820.7 ms | 5423.9 ms | 396.8 ms | 2219.2 ms |
| Uber_zap | Go | 5612.6 ms | 5164.0 ms | 448.6 ms | 2492.9 ms |
| K8s_workqueue | Go | 4725.7 ms | 4252.8 ms | 472.9 ms | 1660.6 ms |
| Toml | Go | 2057.1 ms | 1818.8 ms | 238.4 ms | 942.1 ms |
| Dustin_humanize | Go | 813.6 ms | 669.7 ms | 143.9 ms | 383.7 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2032476.8 ms | 1225765.7 ms | 9 |
| LLGoFullLTOGlobalDCE | 2010439.3 ms | 1183011.3 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2000236.9 ms | 1155968.4 ms | 9 |
| LLGoDeadcodeDrop | 1800384.0 ms | 602830.0 ms | 9 |
| LLGoNoLTO | 1729237.3 ms | 577791.2 ms | 9 |
| Go | 165893.0 ms | 50427.4 ms | 9 |

Dependency download details are in `download-timings.log`.
