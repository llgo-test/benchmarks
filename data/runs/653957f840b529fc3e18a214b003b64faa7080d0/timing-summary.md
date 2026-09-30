## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 482853.1 ms | 473227.6 ms | 9625.5 ms | 259245.7 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 447886.9 ms | 437920.8 ms | 9966.1 ms | 240275.3 ms |
| IXGo | LLGoDeadcodeDrop | 437262.6 ms | 428709.9 ms | 8552.6 ms | 146851.4 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 416149.2 ms | 407103.9 ms | 9045.3 ms | 234578.8 ms |
| IXGo | LLGoNoLTO | 408656.4 ms | 400447.6 ms | 8208.9 ms | 140790.7 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 198297.2 ms | 194277.6 ms | 4019.5 ms | 132236.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 192437.3 ms | 188250.7 ms | 4186.6 ms | 128054.6 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 191420.6 ms | 187346.7 ms | 4073.9 ms | 126467.4 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 180627.5 ms | 177700.6 ms | 2926.9 ms | 107584.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 160087.3 ms | 157440.4 ms | 2646.9 ms | 91691.7 ms |
| Aws_restjson | LLGoDeadcodeDrop | 153485.5 ms | 151034.6 ms | 2450.9 ms | 55826.6 ms |
| Aws_restjson | LLGoNoLTO | 149485.4 ms | 147077.2 ms | 2408.2 ms | 55272.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 146513.6 ms | 143765.8 ms | 2747.8 ms | 85739.3 ms |
| XGo | LLGoFullLTONoGlobalDCE | 143067.2 ms | 140356.0 ms | 2711.1 ms | 107034.9 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 134007.4 ms | 131311.4 ms | 2696.0 ms | 98029.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 133754.1 ms | 131217.7 ms | 2536.4 ms | 89268.2 ms |
| Etcdctl | LLGoDeadcodeDrop | 133702.8 ms | 130218.4 ms | 3484.4 ms | 47677.2 ms |
| Uber_zap | LLGoNoLTO | 131932.6 ms | 129767.5 ms | 2165.2 ms | 52886.8 ms |
| Etcdctl | LLGoNoLTO | 131362.2 ms | 127927.1 ms | 3435.1 ms | 47635.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 130992.3 ms | 128649.2 ms | 2343.1 ms | 82513.8 ms |
| XGo | LLGoFullLTOGlobalDCE | 130500.7 ms | 127949.9 ms | 2550.8 ms | 95821.3 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 129832.1 ms | 127551.8 ms | 2280.3 ms | 85750.5 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 129246.2 ms | 126854.7 ms | 2391.4 ms | 85302.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 129073.5 ms | 126705.7 ms | 2367.8 ms | 81899.4 ms |
| Uber_zap | LLGoDeadcodeDrop | 125770.1 ms | 123630.8 ms | 2139.3 ms | 50313.2 ms |
| K8s_workqueue | LLGoNoLTO | 123120.6 ms | 120876.0 ms | 2244.6 ms | 50302.6 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 119772.0 ms | 117722.1 ms | 2049.9 ms | 47893.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 113511.7 ms | 111148.3 ms | 2363.4 ms | 70742.2 ms |
| XGo | LLGoDeadcodeDrop | 79876.7 ms | 77356.7 ms | 2520.0 ms | 33526.7 ms |
| XGo | LLGoNoLTO | 76601.7 ms | 74164.6 ms | 2437.0 ms | 31235.0 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 70365.5 ms | 68743.0 ms | 1622.5 ms | 44292.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 68700.7 ms | 67093.6 ms | 1607.1 ms | 42289.0 ms |
| IXGo | Go | 67130.6 ms | 62516.1 ms | 4614.5 ms | 27144.7 ms |
| Gorm_schema | LLGoDeadcodeDrop | 64733.7 ms | 63304.3 ms | 1429.4 ms | 22127.8 ms |
| Gorm_schema | LLGoNoLTO | 64428.5 ms | 62987.1 ms | 1441.4 ms | 21984.4 ms |
| Toml | LLGoDeadcodeDrop | 60707.9 ms | 59228.3 ms | 1479.6 ms | 20413.3 ms |
| Toml | LLGoNoLTO | 60396.1 ms | 58966.8 ms | 1429.3 ms | 20211.2 ms |
| Toml | LLGoFullLTONoGlobalDCE | 59238.7 ms | 57804.4 ms | 1434.4 ms | 35898.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 56234.9 ms | 54778.8 ms | 1456.1 ms | 31359.1 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 55520.6 ms | 54050.1 ms | 1470.5 ms | 30936.5 ms |
| Toml | LLGoFullLTOGlobalDCE | 53157.0 ms | 51670.1 ms | 1486.9 ms | 29478.4 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 41118.0 ms | 40151.6 ms | 966.4 ms | 26575.0 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 40376.3 ms | 39431.4 ms | 944.9 ms | 14889.8 ms |
| Dustin_humanize | LLGoNoLTO | 39490.9 ms | 38527.4 ms | 963.5 ms | 14533.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 35155.9 ms | 34150.8 ms | 1005.1 ms | 19897.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 35080.3 ms | 34079.7 ms | 1000.6 ms | 20412.1 ms |
| Etcdctl | Go | 25751.9 ms | 23957.1 ms | 1794.8 ms | 9835.5 ms |
| XGo | Go | 14573.6 ms | 13594.8 ms | 978.8 ms | 4379.6 ms |
| Aws_restjson | Go | 6385.1 ms | 5824.8 ms | 560.4 ms | 2896.6 ms |
| Gorm_schema | Go | 4284.7 ms | 3966.3 ms | 318.4 ms | 2025.8 ms |
| Uber_zap | Go | 3964.1 ms | 3653.8 ms | 310.3 ms | 1556.7 ms |
| K8s_workqueue | Go | 3637.4 ms | 3276.3 ms | 361.1 ms | 1339.8 ms |
| Toml | Go | 1589.9 ms | 1374.7 ms | 215.2 ms | 1720.8 ms |
| Dustin_humanize | Go | 603.6 ms | 490.1 ms | 113.5 ms | 600.8 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTOGlobalDCE | 1385643.9 ms | 838160.3 ms | 9 |
| LLGoFullLTONoGlobalDCE | 1367941.6 ms | 859252.6 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1311244.0 ms | 785960.6 ms | 9 |
| LLGoDeadcodeDrop | 1215687.6 ms | 439519.0 ms | 9 |
| LLGoNoLTO | 1185474.4 ms | 434851.9 ms | 9 |
| Go | 127920.9 ms | 51500.4 ms | 9 |

Dependency download details are in `download-timings.log`.
