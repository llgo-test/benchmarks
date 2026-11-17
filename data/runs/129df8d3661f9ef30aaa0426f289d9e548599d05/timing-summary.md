## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 649384.0 ms | 633518.4 ms | 15865.6 ms | 433795.2 ms |
| IXGo | LLGoFullLTOGlobalDCE | 642801.1 ms | 626606.3 ms | 16194.8 ms | 428189.3 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 635014.5 ms | 618953.1 ms | 16061.4 ms | 424128.9 ms |
| IXGo | LLGoNoLTO | 359020.7 ms | 345100.7 ms | 13920.1 ms | 112423.8 ms |
| IXGo | LLGoDeadcodeDrop | 355738.5 ms | 339199.6 ms | 16538.9 ms | 116283.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 339498.9 ms | 331957.5 ms | 7541.3 ms | 253064.1 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 332371.8 ms | 325029.4 ms | 7342.4 ms | 249833.5 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 326436.4 ms | 319297.0 ms | 7139.3 ms | 243358.2 ms |
| XGo | LLGoFullLTONoGlobalDCE | 249406.1 ms | 244311.0 ms | 5095.1 ms | 202161.4 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 235759.5 ms | 231522.9 ms | 4236.6 ms | 162555.9 ms |
| XGo | LLGoFullLTOGlobalDCE | 223657.2 ms | 218640.1 ms | 5017.1 ms | 173858.4 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 218917.5 ms | 214116.0 ms | 4801.5 ms | 170184.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 217489.1 ms | 213390.2 ms | 4098.9 ms | 140128.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 209424.6 ms | 205368.9 ms | 4055.7 ms | 134802.3 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 193679.7 ms | 189951.4 ms | 3728.3 ms | 140409.1 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 191034.8 ms | 187225.6 ms | 3809.2 ms | 138101.5 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 187572.8 ms | 183957.9 ms | 3614.9 ms | 136130.1 ms |
| Aws_restjson | LLGoDeadcodeDrop | 179684.4 ms | 175704.9 ms | 3979.4 ms | 57962.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 179158.2 ms | 175444.9 ms | 3713.4 ms | 123400.7 ms |
| Aws_restjson | LLGoNoLTO | 177733.7 ms | 174226.0 ms | 3507.7 ms | 55689.9 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 176480.1 ms | 172877.3 ms | 3602.8 ms | 120699.1 ms |
| Etcdctl | LLGoNoLTO | 175779.4 ms | 169631.4 ms | 6148.0 ms | 60736.0 ms |
| Etcdctl | LLGoDeadcodeDrop | 169245.3 ms | 163228.3 ms | 6017.1 ms | 59637.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 163116.4 ms | 159618.6 ms | 3497.8 ms | 109587.0 ms |
| Uber_zap | LLGoNoLTO | 146562.2 ms | 143593.1 ms | 2969.1 ms | 47260.3 ms |
| Uber_zap | LLGoDeadcodeDrop | 142243.8 ms | 139134.9 ms | 3108.8 ms | 47070.5 ms |
| K8s_workqueue | LLGoNoLTO | 141116.2 ms | 137970.1 ms | 3146.1 ms | 45571.6 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 140288.1 ms | 137061.6 ms | 3226.5 ms | 46912.5 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 112728.8 ms | 110139.2 ms | 2589.6 ms | 80087.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 110710.2 ms | 108212.2 ms | 2498.0 ms | 77701.0 ms |
| Toml | LLGoFullLTONoGlobalDCE | 103212.1 ms | 100869.3 ms | 2342.8 ms | 73039.6 ms |
| XGo | LLGoDeadcodeDrop | 97065.3 ms | 92795.3 ms | 4270.1 ms | 36393.3 ms |
| XGo | LLGoNoLTO | 96398.3 ms | 92579.7 ms | 3818.6 ms | 36019.7 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 92643.8 ms | 90122.2 ms | 2521.6 ms | 59320.5 ms |
| Toml | LLGoFullLTOGlobalDCE | 88082.5 ms | 85963.9 ms | 2118.6 ms | 57921.3 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 87804.9 ms | 85578.6 ms | 2226.3 ms | 57670.3 ms |
| Gorm_schema | LLGoDeadcodeDrop | 78865.8 ms | 76670.7 ms | 2195.1 ms | 27957.0 ms |
| Gorm_schema | LLGoNoLTO | 78461.8 ms | 76496.8 ms | 1965.0 ms | 27385.0 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 74353.8 ms | 72666.5 ms | 1687.3 ms | 54253.8 ms |
| Toml | LLGoNoLTO | 73708.8 ms | 71887.3 ms | 1821.5 ms | 25778.1 ms |
| Toml | LLGoDeadcodeDrop | 73564.4 ms | 71657.7 ms | 1906.6 ms | 25864.6 ms |
| IXGo | Go | 62380.3 ms | 54661.8 ms | 7718.5 ms | 17067.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 60486.3 ms | 58889.4 ms | 1596.9 ms | 39818.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 54794.9 ms | 53386.6 ms | 1408.3 ms | 36018.4 ms |
| Dustin_humanize | LLGoNoLTO | 52412.2 ms | 51142.6 ms | 1269.6 ms | 19711.0 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 51551.2 ms | 50185.7 ms | 1365.5 ms | 19599.4 ms |
| Etcdctl | Go | 25177.3 ms | 22272.8 ms | 2904.5 ms | 7590.6 ms |
| XGo | Go | 14120.7 ms | 12503.7 ms | 1617.0 ms | 4182.5 ms |
| Aws_restjson | Go | 6307.7 ms | 5393.2 ms | 914.5 ms | 2914.7 ms |
| Gorm_schema | Go | 4433.0 ms | 3910.8 ms | 522.2 ms | 1696.5 ms |
| Uber_zap | Go | 4149.1 ms | 3649.2 ms | 499.8 ms | 1663.8 ms |
| K8s_workqueue | Go | 3561.1 ms | 3092.0 ms | 469.2 ms | 1268.0 ms |
| Toml | Go | 1583.1 ms | 1383.0 ms | 200.1 ms | 740.1 ms |
| Dustin_humanize | Go | 597.3 ms | 499.0 ms | 98.2 ms | 292.9 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2124099.1 ms | 1522599.8 ms | 9 |
| LLGoFullLTOGlobalDCE | 2039162.3 ms | 1423056.9 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1992758.6 ms | 1374560.9 ms | 9 |
| LLGoNoLTO | 1301193.4 ms | 430575.4 ms | 9 |
| LLGoDeadcodeDrop | 1288246.7 ms | 437680.1 ms | 9 |
| Go | 122309.7 ms | 37416.1 ms | 9 |

Dependency download details are in `download-timings.log`.
