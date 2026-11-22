## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 921604.4 ms | 894397.7 ms | 27206.7 ms | 578801.8 ms |
| IXGo | LLGoFullLTOGlobalDCE | 913099.3 ms | 885852.2 ms | 27247.1 ms | 565546.2 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 833218.6 ms | 806889.1 ms | 26329.5 ms | 538006.3 ms |
| IXGo | LLGoNoLTO | 570044.9 ms | 546154.1 ms | 23890.7 ms | 176050.1 ms |
| IXGo | LLGoDeadcodeDrop | 549214.6 ms | 521365.0 ms | 27849.6 ms | 176449.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 492974.6 ms | 480033.9 ms | 12940.7 ms | 355960.7 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 458869.5 ms | 446499.6 ms | 12370.0 ms | 330474.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 451588.1 ms | 439103.9 ms | 12484.2 ms | 322132.1 ms |
| XGo | LLGoFullLTONoGlobalDCE | 348734.4 ms | 340150.8 ms | 8583.6 ms | 274401.8 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 335594.8 ms | 328466.9 ms | 7127.8 ms | 221856.4 ms |
| Aws_restjson | LLGoNoLTO | 302752.8 ms | 296355.0 ms | 6397.8 ms | 95443.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 299480.7 ms | 292634.2 ms | 6846.5 ms | 186852.0 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 292545.5 ms | 284198.6 ms | 8346.9 ms | 219994.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 287934.1 ms | 281166.0 ms | 6768.0 ms | 180060.8 ms |
| XGo | LLGoFullLTOGlobalDCE | 285314.4 ms | 277140.8 ms | 8173.6 ms | 214338.8 ms |
| Aws_restjson | LLGoDeadcodeDrop | 279291.0 ms | 272702.3 ms | 6588.7 ms | 89070.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 272465.0 ms | 266387.2 ms | 6077.8 ms | 187884.3 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 269330.2 ms | 263527.0 ms | 5803.1 ms | 185223.0 ms |
| Etcdctl | LLGoNoLTO | 263775.9 ms | 253747.1 ms | 10028.7 ms | 90016.0 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 262341.5 ms | 256395.7 ms | 5945.8 ms | 181661.8 ms |
| Etcdctl | LLGoDeadcodeDrop | 258652.1 ms | 247394.6 ms | 11257.5 ms | 89085.9 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 250845.1 ms | 244961.9 ms | 5883.1 ms | 164913.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 244421.5 ms | 238605.2 ms | 5816.3 ms | 159600.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 231962.2 ms | 226353.2 ms | 5609.0 ms | 148575.0 ms |
| Uber_zap | LLGoNoLTO | 226008.0 ms | 220857.3 ms | 5150.7 ms | 72006.5 ms |
| K8s_workqueue | LLGoNoLTO | 219015.4 ms | 214020.8 ms | 4994.6 ms | 69700.6 ms |
| Uber_zap | LLGoDeadcodeDrop | 218227.6 ms | 212488.8 ms | 5738.8 ms | 71606.8 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 207640.6 ms | 202328.8 ms | 5311.8 ms | 67877.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 158041.6 ms | 153816.6 ms | 4225.0 ms | 106628.8 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 153224.0 ms | 149227.4 ms | 3996.6 ms | 104354.2 ms |
| XGo | LLGoNoLTO | 151574.0 ms | 145213.9 ms | 6360.1 ms | 54968.6 ms |
| Toml | LLGoFullLTONoGlobalDCE | 150081.2 ms | 146083.6 ms | 3997.6 ms | 100856.9 ms |
| XGo | LLGoDeadcodeDrop | 149274.6 ms | 141595.7 ms | 7678.9 ms | 54021.0 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 136943.3 ms | 133044.3 ms | 3899.0 ms | 86832.3 ms |
| Toml | LLGoFullLTOGlobalDCE | 132580.2 ms | 128787.2 ms | 3793.0 ms | 83369.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 130469.6 ms | 126635.1 ms | 3834.5 ms | 79917.3 ms |
| Gorm_schema | LLGoDeadcodeDrop | 121446.7 ms | 117675.9 ms | 3770.8 ms | 42342.9 ms |
| Gorm_schema | LLGoNoLTO | 119630.9 ms | 116502.7 ms | 3128.2 ms | 41041.3 ms |
| Toml | LLGoNoLTO | 114639.0 ms | 111488.0 ms | 3151.0 ms | 39426.1 ms |
| Toml | LLGoDeadcodeDrop | 113060.8 ms | 109965.7 ms | 3095.2 ms | 38833.7 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 107979.2 ms | 105375.2 ms | 2604.1 ms | 76923.2 ms |
| IXGo | Go | 101336.6 ms | 86169.2 ms | 15167.4 ms | 27681.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 85749.9 ms | 83197.0 ms | 2552.9 ms | 54716.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 82415.8 ms | 79936.2 ms | 2479.6 ms | 52254.1 ms |
| Dustin_humanize | LLGoNoLTO | 81748.4 ms | 79689.6 ms | 2058.8 ms | 30499.2 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 76495.6 ms | 74247.9 ms | 2247.8 ms | 28686.0 ms |
| Etcdctl | Go | 39120.3 ms | 33726.8 ms | 5393.4 ms | 12153.5 ms |
| XGo | Go | 22879.8 ms | 19784.4 ms | 3095.4 ms | 6908.5 ms |
| Aws_restjson | Go | 9568.0 ms | 7895.2 ms | 1672.8 ms | 4238.1 ms |
| Gorm_schema | Go | 6765.8 ms | 5758.1 ms | 1007.6 ms | 2653.0 ms |
| Uber_zap | Go | 6046.1 ms | 5136.1 ms | 910.0 ms | 2444.3 ms |
| K8s_workqueue | Go | 5524.1 ms | 4593.4 ms | 930.8 ms | 2002.5 ms |
| Toml | Go | 2428.6 ms | 2006.3 ms | 422.3 ms | 1173.2 ms |
| Dustin_humanize | Go | 958.5 ms | 757.9 ms | 200.6 ms | 474.8 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2919373.4 ms | 2013758.0 ms | 9 |
| LLGoFullLTOGlobalDCE | 2845830.1 ms | 1883919.6 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2824605.0 ms | 1864459.2 ms | 9 |
| LLGoNoLTO | 2049189.3 ms | 669151.4 ms | 9 |
| LLGoDeadcodeDrop | 1973303.6 ms | 657973.3 ms | 9 |
| Go | 194627.7 ms | 59729.1 ms | 9 |

Dependency download details are in `download-timings.log`.
