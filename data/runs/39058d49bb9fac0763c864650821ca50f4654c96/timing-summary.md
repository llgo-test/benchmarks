## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 691795.9 ms | 674465.6 ms | 17330.4 ms | 461715.8 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 672225.9 ms | 654938.8 ms | 17287.1 ms | 449813.5 ms |
| IXGo | LLGoFullLTOGlobalDCE | 649934.7 ms | 633080.8 ms | 16854.0 ms | 431757.5 ms |
| IXGo | LLGoDeadcodeDrop | 381462.2 ms | 363774.1 ms | 17688.0 ms | 124289.3 ms |
| IXGo | LLGoNoLTO | 362396.3 ms | 348327.5 ms | 14068.8 ms | 113035.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 344410.3 ms | 337141.5 ms | 7268.9 ms | 256510.5 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 341165.9 ms | 333911.8 ms | 7254.1 ms | 256043.3 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 340172.3 ms | 332600.8 ms | 7571.5 ms | 254765.7 ms |
| XGo | LLGoFullLTONoGlobalDCE | 247707.0 ms | 242847.8 ms | 4859.2 ms | 201457.1 ms |
| XGo | LLGoFullLTOGlobalDCE | 226735.5 ms | 221820.9 ms | 4914.5 ms | 177133.6 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 225715.5 ms | 221819.0 ms | 3896.5 ms | 154228.9 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 222028.3 ms | 217238.8 ms | 4789.5 ms | 172983.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 214267.4 ms | 210231.2 ms | 4036.2 ms | 138150.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 211937.8 ms | 207751.7 ms | 4186.1 ms | 137124.1 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 199619.1 ms | 195848.5 ms | 3770.7 ms | 143701.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 194799.6 ms | 191088.0 ms | 3711.7 ms | 140461.5 ms |
| Aws_restjson | LLGoNoLTO | 191670.4 ms | 188013.0 ms | 3657.4 ms | 59878.9 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 187373.7 ms | 183637.3 ms | 3736.4 ms | 127547.2 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 185807.7 ms | 182296.1 ms | 3511.6 ms | 134575.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 184157.9 ms | 180496.4 ms | 3661.5 ms | 127445.4 ms |
| Etcdctl | LLGoNoLTO | 183308.2 ms | 177087.2 ms | 6221.0 ms | 63025.0 ms |
| Aws_restjson | LLGoDeadcodeDrop | 182696.4 ms | 178771.4 ms | 3925.0 ms | 58997.0 ms |
| Etcdctl | LLGoDeadcodeDrop | 182393.5 ms | 175748.3 ms | 6645.2 ms | 63779.8 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 161631.2 ms | 158260.7 ms | 3370.4 ms | 109100.4 ms |
| Uber_zap | LLGoDeadcodeDrop | 148535.7 ms | 145298.0 ms | 3237.7 ms | 48836.0 ms |
| Uber_zap | LLGoNoLTO | 148230.1 ms | 145155.5 ms | 3074.6 ms | 47714.8 ms |
| K8s_workqueue | LLGoNoLTO | 143682.8 ms | 140495.6 ms | 3187.2 ms | 46572.8 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 141991.7 ms | 138736.3 ms | 3255.5 ms | 47421.8 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 113510.4 ms | 110917.2 ms | 2593.2 ms | 81429.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 111354.0 ms | 108963.8 ms | 2390.2 ms | 78202.4 ms |
| Toml | LLGoFullLTONoGlobalDCE | 105964.8 ms | 103530.7 ms | 2434.2 ms | 75250.7 ms |
| XGo | LLGoNoLTO | 104058.9 ms | 100036.4 ms | 4022.5 ms | 38560.8 ms |
| XGo | LLGoDeadcodeDrop | 96016.5 ms | 91671.8 ms | 4344.6 ms | 35635.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 95498.5 ms | 93131.3 ms | 2367.2 ms | 61423.2 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 90818.9 ms | 88723.7 ms | 2095.3 ms | 60166.4 ms |
| Toml | LLGoFullLTOGlobalDCE | 88874.0 ms | 86689.0 ms | 2185.0 ms | 58638.3 ms |
| Gorm_schema | LLGoDeadcodeDrop | 82650.0 ms | 80310.5 ms | 2339.6 ms | 29393.7 ms |
| Gorm_schema | LLGoNoLTO | 81932.0 ms | 79876.6 ms | 2055.4 ms | 28647.2 ms |
| Toml | LLGoNoLTO | 76480.3 ms | 74588.4 ms | 1891.9 ms | 26728.0 ms |
| Toml | LLGoDeadcodeDrop | 75888.5 ms | 73855.0 ms | 2033.5 ms | 26729.9 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 74301.5 ms | 72630.6 ms | 1670.9 ms | 54636.9 ms |
| IXGo | Go | 61281.6 ms | 53516.1 ms | 7765.4 ms | 17051.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 59863.2 ms | 58264.2 ms | 1599.0 ms | 39302.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 58898.7 ms | 57396.8 ms | 1501.9 ms | 38955.8 ms |
| Dustin_humanize | LLGoNoLTO | 52885.5 ms | 51518.4 ms | 1367.1 ms | 20304.0 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 52464.2 ms | 51138.1 ms | 1326.1 ms | 19955.8 ms |
| Etcdctl | Go | 25901.6 ms | 22851.1 ms | 3050.5 ms | 7826.2 ms |
| XGo | Go | 14522.6 ms | 12836.1 ms | 1686.6 ms | 4232.8 ms |
| Aws_restjson | Go | 6117.8 ms | 5275.8 ms | 842.0 ms | 2528.1 ms |
| Gorm_schema | Go | 4436.6 ms | 3882.1 ms | 554.5 ms | 1718.2 ms |
| Uber_zap | Go | 4126.9 ms | 3663.0 ms | 463.9 ms | 1629.0 ms |
| K8s_workqueue | Go | 3563.7 ms | 3063.6 ms | 500.1 ms | 1461.8 ms |
| Toml | Go | 1581.1 ms | 1352.9 ms | 228.2 ms | 796.4 ms |
| Dustin_humanize | Go | 623.5 ms | 494.2 ms | 129.3 ms | 307.8 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2165024.2 ms | 1549859.3 ms | 9 |
| LLGoFullLTOGlobalDCE | 2067858.2 ms | 1445762.0 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2067687.5 ms | 1426899.8 ms | 9 |
| LLGoNoLTO | 1344644.6 ms | 444466.7 ms | 9 |
| LLGoDeadcodeDrop | 1344098.6 ms | 455038.8 ms | 9 |
| Go | 122155.5 ms | 37551.5 ms | 9 |

Dependency download details are in `download-timings.log`.
