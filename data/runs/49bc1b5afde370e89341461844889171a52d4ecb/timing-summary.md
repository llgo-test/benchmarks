## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTONoGlobalDCE | 690660.5 ms | 684849.1 ms | 5811.4 ms | 485859.3 ms |
| IXGo | LLGoFullLTOGlobalDCE | 690488.6 ms | 684559.0 ms | 5929.6 ms | 498709.1 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 623617.4 ms | 617783.9 ms | 5833.5 ms | 434782.0 ms |
| IXGo | LLGoDeadcodeDrop | 352878.9 ms | 347636.6 ms | 5242.3 ms | 116747.3 ms |
| IXGo | LLGoNoLTO | 331989.9 ms | 326938.1 ms | 5051.8 ms | 114159.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 218602.7 ms | 214528.9 ms | 4073.8 ms | 136694.5 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 216915.1 ms | 212937.9 ms | 3977.2 ms | 136502.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 213760.4 ms | 209688.1 ms | 4072.3 ms | 132361.3 ms |
| Etcdctl | LLGoDeadcodeDrop | 155501.8 ms | 151826.0 ms | 3675.8 ms | 52997.1 ms |
| Etcdctl | LLGoNoLTO | 150836.6 ms | 147330.0 ms | 3506.6 ms | 51324.2 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 144579.6 ms | 141877.5 ms | 2702.1 ms | 103556.5 ms |
| XGo | LLGoFullLTONoGlobalDCE | 141663.6 ms | 139010.2 ms | 2653.4 ms | 101583.2 ms |
| XGo | LLGoFullLTOGlobalDCE | 141260.2 ms | 138591.5 ms | 2668.8 ms | 101122.0 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 110465.9 ms | 108557.9 ms | 1908.0 ms | 83881.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 105990.4 ms | 103957.1 ms | 2033.3 ms | 77255.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 103168.0 ms | 100956.0 ms | 2212.0 ms | 74387.0 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 89856.1 ms | 88384.6 ms | 1471.5 ms | 70479.1 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 86397.6 ms | 84905.2 ms | 1492.3 ms | 69146.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 85675.7 ms | 84185.8 ms | 1489.9 ms | 68634.3 ms |
| XGo | LLGoDeadcodeDrop | 83169.8 ms | 80880.3 ms | 2289.5 ms | 32030.7 ms |
| XGo | LLGoNoLTO | 81862.4 ms | 79571.8 ms | 2290.6 ms | 31375.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 80946.6 ms | 79481.6 ms | 1465.0 ms | 60961.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 80215.0 ms | 78756.5 ms | 1458.5 ms | 60549.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 74314.1 ms | 72823.9 ms | 1490.2 ms | 56739.8 ms |
| Aws_restjson | LLGoDeadcodeDrop | 66934.3 ms | 65176.2 ms | 1758.2 ms | 33261.5 ms |
| Aws_restjson | LLGoNoLTO | 65991.2 ms | 64344.1 ms | 1647.1 ms | 33286.7 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 51047.6 ms | 49812.2 ms | 1235.4 ms | 35986.6 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 50376.3 ms | 49241.3 ms | 1135.0 ms | 35992.1 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 43721.0 ms | 42587.0 ms | 1134.0 ms | 28381.7 ms |
| Uber_zap | LLGoDeadcodeDrop | 43551.0 ms | 42378.2 ms | 1172.7 ms | 19545.0 ms |
| Uber_zap | LLGoNoLTO | 42941.9 ms | 41836.9 ms | 1105.0 ms | 19463.2 ms |
| Toml | LLGoFullLTONoGlobalDCE | 40746.2 ms | 39838.0 ms | 908.2 ms | 32052.6 ms |
| K8s_workqueue | LLGoNoLTO | 39340.9 ms | 38118.1 ms | 1222.8 ms | 18853.0 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 38906.9 ms | 37692.2 ms | 1214.7 ms | 18985.9 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 35065.4 ms | 34169.2 ms | 896.2 ms | 25976.8 ms |
| Toml | LLGoFullLTOGlobalDCE | 34511.6 ms | 33604.2 ms | 907.4 ms | 25793.5 ms |
| IXGo | Go | 34194.2 ms | 31687.9 ms | 2506.2 ms | 9933.6 ms |
| Gorm_schema | LLGoNoLTO | 29098.7 ms | 28097.8 ms | 1000.9 ms | 9638.6 ms |
| Gorm_schema | LLGoDeadcodeDrop | 28710.1 ms | 27717.6 ms | 992.6 ms | 9824.5 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 26270.4 ms | 25529.2 ms | 741.3 ms | 20805.0 ms |
| Etcdctl | Go | 25514.2 ms | 23795.6 ms | 1718.6 ms | 7736.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 20587.2 ms | 19879.1 ms | 708.1 ms | 15038.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 20467.6 ms | 19750.7 ms | 716.9 ms | 14580.7 ms |
| Toml | LLGoDeadcodeDrop | 17887.5 ms | 17111.5 ms | 776.0 ms | 6911.3 ms |
| Toml | LLGoNoLTO | 17123.2 ms | 16341.0 ms | 782.2 ms | 6667.0 ms |
| XGo | Go | 14743.9 ms | 13685.5 ms | 1058.5 ms | 4451.1 ms |
| Dustin_humanize | LLGoNoLTO | 10503.0 ms | 9896.9 ms | 606.1 ms | 4502.2 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 10012.9 ms | 9410.4 ms | 602.6 ms | 4441.2 ms |
| Aws_restjson | Go | 6021.5 ms | 5456.3 ms | 565.2 ms | 2514.3 ms |
| Gorm_schema | Go | 4533.7 ms | 4202.8 ms | 330.9 ms | 1773.5 ms |
| Uber_zap | Go | 4038.5 ms | 3719.0 ms | 319.5 ms | 1615.8 ms |
| K8s_workqueue | Go | 3581.2 ms | 3170.8 ms | 410.4 ms | 1284.6 ms |
| Toml | Go | 1648.9 ms | 1430.5 ms | 218.4 ms | 782.5 ms |
| Dustin_humanize | Go | 639.8 ms | 509.9 ms | 130.0 ms | 307.4 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1453351.7 ms | 1036300.4 ms | 9 |
| LLGoFullLTOGlobalDCE | 1426168.6 ms | 1016869.3 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1341850.5 ms | 934641.0 ms | 9 |
| LLGoDeadcodeDrop | 797553.3 ms | 294744.4 ms | 9 |
| LLGoNoLTO | 769687.7 ms | 289269.4 ms | 9 |
| Go | 94915.9 ms | 30399.0 ms | 9 |

Dependency download details are in `download-timings.log`.
