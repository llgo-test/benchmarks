## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 621436.5 ms | 612435.1 ms | 9001.4 ms | 312024.7 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 547446.7 ms | 539518.5 ms | 7928.2 ms | 274615.7 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 485717.7 ms | 478341.2 ms | 7376.5 ms | 240866.5 ms |
| IXGo | LLGoDeadcodeDrop | 401242.0 ms | 392342.9 ms | 8899.1 ms | 117062.2 ms |
| IXGo | LLGoNoLTO | 367616.1 ms | 360445.6 ms | 7170.5 ms | 103770.3 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 214384.5 ms | 210013.6 ms | 4370.9 ms | 141723.6 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 208006.9 ms | 204276.9 ms | 3730.0 ms | 133389.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 194833.2 ms | 191136.4 ms | 3696.8 ms | 126825.1 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 174059.9 ms | 171251.8 ms | 2808.0 ms | 104493.8 ms |
| Aws_restjson | LLGoNoLTO | 143092.2 ms | 140815.0 ms | 2277.3 ms | 49612.0 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 143005.2 ms | 140433.3 ms | 2571.9 ms | 103739.2 ms |
| Aws_restjson | LLGoDeadcodeDrop | 142038.3 ms | 139803.8 ms | 2234.6 ms | 50001.7 ms |
| Etcdctl | LLGoDeadcodeDrop | 141496.7 ms | 137784.8 ms | 3711.9 ms | 47566.0 ms |
| XGo | LLGoFullLTOGlobalDCE | 140401.6 ms | 137913.7 ms | 2487.9 ms | 100915.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 139672.5 ms | 137098.1 ms | 2574.3 ms | 83004.3 ms |
| XGo | LLGoFullLTONoGlobalDCE | 139168.3 ms | 136720.0 ms | 2448.3 ms | 101227.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 134578.5 ms | 132122.1 ms | 2456.4 ms | 78991.3 ms |
| Etcdctl | LLGoNoLTO | 134017.7 ms | 130915.8 ms | 3101.9 ms | 44023.1 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 124125.3 ms | 121653.4 ms | 2471.9 ms | 80501.6 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 123212.0 ms | 120917.7 ms | 2294.3 ms | 80737.6 ms |
| Uber_zap | LLGoNoLTO | 120393.4 ms | 118405.4 ms | 1988.0 ms | 45301.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 120084.7 ms | 117698.9 ms | 2385.9 ms | 75014.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 119741.9 ms | 117536.1 ms | 2205.8 ms | 74692.9 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 117551.5 ms | 115364.4 ms | 2187.0 ms | 44297.5 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 117211.0 ms | 114944.9 ms | 2266.1 ms | 77176.7 ms |
| Uber_zap | LLGoDeadcodeDrop | 116311.6 ms | 114344.2 ms | 1967.4 ms | 43302.3 ms |
| K8s_workqueue | LLGoNoLTO | 116085.3 ms | 114001.3 ms | 2083.9 ms | 43452.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 105618.0 ms | 103491.8 ms | 2126.2 ms | 65491.2 ms |
| XGo | LLGoDeadcodeDrop | 81041.8 ms | 78550.6 ms | 2491.2 ms | 30772.2 ms |
| XGo | LLGoNoLTO | 75983.9 ms | 73916.2 ms | 2067.7 ms | 28694.6 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 63951.7 ms | 62483.2 ms | 1468.5 ms | 40355.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 63769.6 ms | 62273.8 ms | 1495.9 ms | 39553.4 ms |
| Gorm_schema | LLGoNoLTO | 63434.0 ms | 62164.2 ms | 1269.7 ms | 21265.4 ms |
| Toml | LLGoDeadcodeDrop | 62634.2 ms | 61259.6 ms | 1374.7 ms | 21115.9 ms |
| Toml | LLGoNoLTO | 61947.9 ms | 60519.0 ms | 1428.9 ms | 20975.3 ms |
| Gorm_schema | LLGoDeadcodeDrop | 60804.1 ms | 59510.0 ms | 1294.0 ms | 20372.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 60470.4 ms | 59005.7 ms | 1464.7 ms | 33949.0 ms |
| Toml | LLGoFullLTONoGlobalDCE | 59101.8 ms | 57680.5 ms | 1421.3 ms | 37454.5 ms |
| IXGo | Go | 52470.4 ms | 48675.6 ms | 3794.8 ms | 14608.2 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 51907.8 ms | 50560.3 ms | 1347.4 ms | 29359.7 ms |
| Toml | LLGoFullLTOGlobalDCE | 51054.9 ms | 49690.9 ms | 1364.0 ms | 29022.2 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 44635.0 ms | 43559.1 ms | 1076.0 ms | 29268.7 ms |
| Dustin_humanize | LLGoNoLTO | 40043.3 ms | 39141.4 ms | 901.9 ms | 14584.5 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 39212.4 ms | 38396.1 ms | 816.3 ms | 14233.5 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 35737.7 ms | 34743.5 ms | 994.2 ms | 20645.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 35618.4 ms | 34682.1 ms | 936.3 ms | 20289.5 ms |
| Etcdctl | Go | 21728.7 ms | 20151.9 ms | 1576.8 ms | 6809.4 ms |
| XGo | Go | 12218.7 ms | 11352.9 ms | 865.8 ms | 3714.7 ms |
| Aws_restjson | Go | 5640.8 ms | 5116.3 ms | 524.5 ms | 2437.8 ms |
| Gorm_schema | Go | 3711.0 ms | 3415.8 ms | 295.2 ms | 1461.9 ms |
| Uber_zap | Go | 3275.7 ms | 2986.9 ms | 288.8 ms | 1313.9 ms |
| K8s_workqueue | Go | 2940.7 ms | 2600.2 ms | 340.6 ms | 1118.5 ms |
| Toml | Go | 1245.5 ms | 1069.3 ms | 176.2 ms | 632.3 ms |
| Dustin_humanize | Go | 552.8 ms | 410.4 ms | 142.4 ms | 538.5 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTOGlobalDCE | 1485902.8 ms | 863138.0 ms | 9 |
| LLGoFullLTONoGlobalDCE | 1421441.9 ms | 853303.7 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1411607.0 ms | 818886.6 ms | 9 |
| LLGoDeadcodeDrop | 1162332.6 ms | 388724.1 ms | 9 |
| LLGoNoLTO | 1122613.8 ms | 371679.2 ms | 9 |
| Go | 103784.4 ms | 32635.1 ms | 9 |

Dependency download details are in `download-timings.log`.
