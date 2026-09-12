## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 781341.7 ms | 773821.6 ms | 7520.1 ms | 545848.0 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 779806.1 ms | 772487.7 ms | 7318.5 ms | 550624.6 ms |
| IXGo | LLGoFullLTOGlobalDCE | 775563.9 ms | 768503.8 ms | 7060.1 ms | 540119.7 ms |
| IXGo | LLGoNoLTO | 444522.9 ms | 438306.0 ms | 6216.9 ms | 146943.1 ms |
| IXGo | LLGoDeadcodeDrop | 427290.8 ms | 420833.5 ms | 6457.3 ms | 141671.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 275337.0 ms | 270097.0 ms | 5240.0 ms | 171033.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 270907.9 ms | 265921.9 ms | 4986.0 ms | 167839.6 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 266231.9 ms | 261409.1 ms | 4822.8 ms | 166711.6 ms |
| Etcdctl | LLGoDeadcodeDrop | 195533.9 ms | 191011.6 ms | 4522.3 ms | 65709.9 ms |
| Etcdctl | LLGoNoLTO | 192205.9 ms | 187835.2 ms | 4370.7 ms | 63415.7 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 188219.9 ms | 184562.8 ms | 3657.1 ms | 133529.3 ms |
| XGo | LLGoFullLTOGlobalDCE | 187542.4 ms | 184057.9 ms | 3484.5 ms | 133356.3 ms |
| XGo | LLGoFullLTONoGlobalDCE | 185714.8 ms | 182327.1 ms | 3387.7 ms | 132879.6 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 141532.7 ms | 139119.5 ms | 2413.2 ms | 106531.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 131773.6 ms | 129291.9 ms | 2481.7 ms | 95326.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 130145.4 ms | 127626.7 ms | 2518.7 ms | 93266.5 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 113324.0 ms | 111500.8 ms | 1823.2 ms | 88566.1 ms |
| XGo | LLGoDeadcodeDrop | 109413.7 ms | 106367.2 ms | 3046.5 ms | 42783.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 108592.0 ms | 106735.1 ms | 1856.9 ms | 86124.4 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 107377.9 ms | 105549.9 ms | 1828.0 ms | 85442.7 ms |
| XGo | LLGoNoLTO | 107338.2 ms | 104410.7 ms | 2927.5 ms | 41949.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 104269.0 ms | 102390.1 ms | 1878.9 ms | 78375.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 103368.7 ms | 101536.4 ms | 1832.3 ms | 77653.1 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 95105.8 ms | 93259.7 ms | 1846.2 ms | 71888.5 ms |
| Aws_restjson | LLGoDeadcodeDrop | 83790.0 ms | 81691.8 ms | 2098.2 ms | 39802.7 ms |
| Aws_restjson | LLGoNoLTO | 80924.1 ms | 78945.8 ms | 1978.4 ms | 38746.1 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 64980.9 ms | 63519.6 ms | 1461.3 ms | 45820.3 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 64860.6 ms | 63459.1 ms | 1401.6 ms | 46480.4 ms |
| Uber_zap | LLGoDeadcodeDrop | 56610.6 ms | 55100.4 ms | 1510.2 ms | 25202.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 54957.9 ms | 53505.0 ms | 1452.9 ms | 35450.3 ms |
| Uber_zap | LLGoNoLTO | 54738.5 ms | 53238.6 ms | 1499.9 ms | 24394.9 ms |
| Toml | LLGoFullLTONoGlobalDCE | 52569.0 ms | 51455.1 ms | 1114.0 ms | 41078.7 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 51446.5 ms | 49915.7 ms | 1530.8 ms | 25363.3 ms |
| K8s_workqueue | LLGoNoLTO | 48621.9 ms | 47088.5 ms | 1533.4 ms | 23191.0 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 44976.3 ms | 43858.4 ms | 1117.9 ms | 32751.6 ms |
| Toml | LLGoFullLTOGlobalDCE | 44506.4 ms | 43409.2 ms | 1097.2 ms | 32810.9 ms |
| IXGo | Go | 43467.0 ms | 40261.8 ms | 3205.2 ms | 12601.8 ms |
| Gorm_schema | LLGoDeadcodeDrop | 37274.3 ms | 36000.3 ms | 1273.9 ms | 12360.8 ms |
| Gorm_schema | LLGoNoLTO | 36139.2 ms | 34896.1 ms | 1243.1 ms | 12007.6 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 33492.7 ms | 32636.8 ms | 855.9 ms | 26847.6 ms |
| Etcdctl | Go | 32270.4 ms | 30129.8 ms | 2140.6 ms | 9754.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 24806.1 ms | 23943.9 ms | 862.1 ms | 17959.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 24635.3 ms | 23791.1 ms | 844.2 ms | 17792.8 ms |
| Toml | LLGoDeadcodeDrop | 23274.5 ms | 22275.1 ms | 999.4 ms | 8695.4 ms |
| Toml | LLGoNoLTO | 23005.8 ms | 22054.0 ms | 951.8 ms | 8737.0 ms |
| XGo | Go | 18420.7 ms | 17160.7 ms | 1260.0 ms | 5445.9 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 12821.6 ms | 12049.4 ms | 772.3 ms | 5704.2 ms |
| Dustin_humanize | LLGoNoLTO | 12630.3 ms | 11909.9 ms | 720.4 ms | 5560.8 ms |
| Aws_restjson | Go | 7793.9 ms | 7068.2 ms | 725.7 ms | 3259.1 ms |
| Gorm_schema | Go | 5604.4 ms | 5220.3 ms | 384.1 ms | 2148.2 ms |
| Uber_zap | Go | 5160.1 ms | 4732.0 ms | 428.1 ms | 2033.8 ms |
| K8s_workqueue | Go | 4591.8 ms | 4122.3 ms | 469.5 ms | 1643.8 ms |
| Toml | Go | 1997.7 ms | 1755.6 ms | 242.2 ms | 922.7 ms |
| Dustin_humanize | Go | 809.6 ms | 664.8 ms | 144.8 ms | 390.7 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1744909.9 ms | 1245163.0 ms | 9 |
| LLGoFullLTOGlobalDCE | 1710242.9 ms | 1194783.6 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1700787.3 ms | 1182161.3 ms | 9 |
| LLGoNoLTO | 1000126.9 ms | 364945.6 ms | 9 |
| LLGoDeadcodeDrop | 997455.8 ms | 367292.9 ms | 9 |
| Go | 120115.7 ms | 38200.3 ms | 9 |

Dependency download details are in `download-timings.log`.
