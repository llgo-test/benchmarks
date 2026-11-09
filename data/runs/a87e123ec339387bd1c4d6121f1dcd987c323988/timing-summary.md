## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 839232.9 ms | 813140.6 ms | 26092.3 ms | 537856.8 ms |
| IXGo | LLGoFullLTOGlobalDCE | 822134.6 ms | 796307.2 ms | 25827.4 ms | 526304.8 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 820755.2 ms | 794550.3 ms | 26205.0 ms | 532392.9 ms |
| IXGo | LLGoDeadcodeDrop | 494954.5 ms | 467867.5 ms | 27087.0 ms | 156577.9 ms |
| IXGo | LLGoNoLTO | 464807.4 ms | 443069.6 ms | 21737.9 ms | 143895.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 453653.4 ms | 441510.6 ms | 12142.8 ms | 326209.0 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 452329.9 ms | 440017.8 ms | 12312.1 ms | 328675.6 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 451018.0 ms | 438897.0 ms | 12121.0 ms | 325482.4 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 377785.8 ms | 369841.8 ms | 7944.0 ms | 249811.8 ms |
| XGo | LLGoFullLTONoGlobalDCE | 333572.3 ms | 324944.0 ms | 8628.3 ms | 264474.9 ms |
| XGo | LLGoFullLTOGlobalDCE | 313170.6 ms | 304526.6 ms | 8644.0 ms | 240156.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 308797.6 ms | 301710.3 ms | 7087.3 ms | 195006.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 307233.9 ms | 299953.0 ms | 7281.0 ms | 194552.5 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 302293.4 ms | 295219.2 ms | 7074.1 ms | 208116.4 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 295655.4 ms | 287640.7 ms | 8014.7 ms | 225345.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 279119.5 ms | 272567.6 ms | 6551.9 ms | 191694.2 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 277482.8 ms | 270864.1 ms | 6618.7 ms | 192087.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 267190.0 ms | 260863.0 ms | 6327.0 ms | 175986.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 261986.4 ms | 255889.0 ms | 6097.4 ms | 171332.4 ms |
| Aws_restjson | LLGoNoLTO | 245375.2 ms | 239534.7 ms | 5840.5 ms | 76209.7 ms |
| Aws_restjson | LLGoDeadcodeDrop | 244793.9 ms | 238565.5 ms | 6228.4 ms | 76604.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 244445.3 ms | 238293.7 ms | 6151.6 ms | 157780.9 ms |
| Etcdctl | LLGoDeadcodeDrop | 241015.7 ms | 230176.6 ms | 10839.1 ms | 82352.9 ms |
| Etcdctl | LLGoNoLTO | 237646.6 ms | 228363.6 ms | 9283.0 ms | 80328.9 ms |
| Uber_zap | LLGoNoLTO | 205586.8 ms | 200718.2 ms | 4868.6 ms | 64606.8 ms |
| Uber_zap | LLGoDeadcodeDrop | 204400.0 ms | 199194.1 ms | 5205.9 ms | 65417.9 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 197488.2 ms | 192129.8 ms | 5358.4 ms | 63655.8 ms |
| K8s_workqueue | LLGoNoLTO | 195408.9 ms | 190532.4 ms | 4876.4 ms | 61801.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 155729.5 ms | 151638.1 ms | 4091.3 ms | 104477.4 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 147695.7 ms | 143856.7 ms | 3839.0 ms | 99826.3 ms |
| Toml | LLGoFullLTONoGlobalDCE | 139784.8 ms | 136005.3 ms | 3779.5 ms | 93559.3 ms |
| XGo | LLGoNoLTO | 134492.0 ms | 128319.3 ms | 6172.7 ms | 49022.2 ms |
| XGo | LLGoDeadcodeDrop | 134109.7 ms | 126756.2 ms | 7353.4 ms | 48233.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 125495.3 ms | 121874.9 ms | 3620.4 ms | 76175.2 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 123817.8 ms | 120432.2 ms | 3385.6 ms | 76709.8 ms |
| Toml | LLGoFullLTOGlobalDCE | 123393.4 ms | 119895.0 ms | 3498.4 ms | 76565.6 ms |
| Gorm_schema | LLGoDeadcodeDrop | 113894.9 ms | 110394.2 ms | 3500.7 ms | 39235.2 ms |
| Gorm_schema | LLGoNoLTO | 112343.6 ms | 109228.4 ms | 3115.2 ms | 38186.0 ms |
| Toml | LLGoDeadcodeDrop | 106792.3 ms | 103642.0 ms | 3150.3 ms | 36253.1 ms |
| Toml | LLGoNoLTO | 106490.8 ms | 103522.2 ms | 2968.6 ms | 35974.7 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 98018.2 ms | 95506.9 ms | 2511.3 ms | 68431.7 ms |
| IXGo | Go | 96477.0 ms | 82046.2 ms | 14430.8 ms | 26242.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 78675.3 ms | 76447.1 ms | 2228.2 ms | 49287.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 78568.0 ms | 76188.2 ms | 2379.8 ms | 49084.9 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 76191.1 ms | 73904.7 ms | 2286.4 ms | 27944.0 ms |
| Dustin_humanize | LLGoNoLTO | 72020.0 ms | 69970.0 ms | 2049.9 ms | 26478.8 ms |
| Etcdctl | Go | 39266.3 ms | 33750.0 ms | 5516.3 ms | 12128.2 ms |
| XGo | Go | 21704.2 ms | 18587.9 ms | 3116.3 ms | 6413.2 ms |
| Aws_restjson | Go | 9072.0 ms | 7547.1 ms | 1525.0 ms | 3688.6 ms |
| Gorm_schema | Go | 6527.2 ms | 5606.5 ms | 920.6 ms | 2570.1 ms |
| Uber_zap | Go | 5934.5 ms | 5050.4 ms | 884.1 ms | 2372.6 ms |
| K8s_workqueue | Go | 5560.0 ms | 4552.5 ms | 1007.5 ms | 2470.4 ms |
| Toml | Go | 2281.3 ms | 1869.9 ms | 411.4 ms | 1073.1 ms |
| Dustin_humanize | Go | 943.3 ms | 729.0 ms | 214.3 ms | 468.0 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2949718.1 ms | 2037376.5 ms | 9 |
| LLGoFullLTOGlobalDCE | 2799228.6 ms | 1884961.8 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2730088.4 ms | 1815047.0 ms | 9 |
| LLGoDeadcodeDrop | 1813640.3 ms | 596274.2 ms | 9 |
| LLGoNoLTO | 1774171.2 ms | 576504.7 ms | 9 |
| Go | 187765.8 ms | 57426.5 ms | 9 |

Dependency download details are in `download-timings.log`.
