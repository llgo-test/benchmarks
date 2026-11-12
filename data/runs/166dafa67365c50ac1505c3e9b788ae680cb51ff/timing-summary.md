## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 735434.6 ms | 716877.3 ms | 18557.3 ms | 494259.2 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 697427.8 ms | 680000.7 ms | 17427.1 ms | 468399.8 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 654092.2 ms | 636741.7 ms | 17350.5 ms | 447455.1 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 387292.2 ms | 377960.7 ms | 9331.5 ms | 288431.5 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 367024.5 ms | 358760.3 ms | 8264.3 ms | 275346.2 ms |
| IXGo | LLGoDeadcodeDrop | 360776.3 ms | 343154.7 ms | 17621.6 ms | 119084.3 ms |
| IXGo | LLGoNoLTO | 354848.1 ms | 340346.0 ms | 14502.0 ms | 111478.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 349664.0 ms | 341654.3 ms | 8009.8 ms | 263555.6 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 276496.6 ms | 271227.9 ms | 5268.7 ms | 191383.0 ms |
| XGo | LLGoFullLTONoGlobalDCE | 263853.5 ms | 258313.2 ms | 5540.4 ms | 215459.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 245612.5 ms | 240758.8 ms | 4853.7 ms | 160147.0 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 236474.3 ms | 230850.1 ms | 5624.2 ms | 186063.0 ms |
| XGo | LLGoFullLTOGlobalDCE | 233391.6 ms | 227693.6 ms | 5698.0 ms | 183557.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 228519.0 ms | 223913.4 ms | 4605.6 ms | 150230.8 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 220495.7 ms | 216174.5 ms | 4321.2 ms | 155922.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 219954.5 ms | 215650.2 ms | 4304.4 ms | 159958.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 210211.5 ms | 205935.2 ms | 4276.3 ms | 146255.9 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 206717.6 ms | 202667.6 ms | 4050.0 ms | 144139.8 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 206473.8 ms | 202354.8 ms | 4118.9 ms | 150214.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 189632.3 ms | 185329.5 ms | 4302.8 ms | 128894.1 ms |
| Aws_restjson | LLGoNoLTO | 189204.1 ms | 185348.2 ms | 3855.8 ms | 59401.6 ms |
| Etcdctl | LLGoNoLTO | 177049.8 ms | 170678.9 ms | 6370.9 ms | 61669.8 ms |
| Etcdctl | LLGoDeadcodeDrop | 175442.4 ms | 168250.7 ms | 7191.7 ms | 62308.5 ms |
| Aws_restjson | LLGoDeadcodeDrop | 170276.4 ms | 166548.2 ms | 3728.2 ms | 55379.3 ms |
| Uber_zap | LLGoNoLTO | 150472.2 ms | 147370.8 ms | 3101.4 ms | 48624.2 ms |
| Uber_zap | LLGoDeadcodeDrop | 143644.4 ms | 140367.3 ms | 3277.1 ms | 47762.9 ms |
| K8s_workqueue | LLGoNoLTO | 137587.3 ms | 134339.5 ms | 3247.9 ms | 44704.6 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 135114.1 ms | 131775.7 ms | 3338.5 ms | 45950.6 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 118235.0 ms | 115515.3 ms | 2719.7 ms | 83923.4 ms |
| Toml | LLGoFullLTONoGlobalDCE | 117117.3 ms | 114534.1 ms | 2583.2 ms | 82475.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 108653.0 ms | 106091.0 ms | 2562.0 ms | 76085.1 ms |
| XGo | LLGoNoLTO | 106885.6 ms | 102269.8 ms | 4615.8 ms | 39946.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 98956.0 ms | 96538.1 ms | 2417.9 ms | 64628.4 ms |
| XGo | LLGoDeadcodeDrop | 96875.6 ms | 92154.7 ms | 4720.9 ms | 36279.6 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 92084.7 ms | 89746.7 ms | 2338.0 ms | 59916.9 ms |
| Toml | LLGoFullLTOGlobalDCE | 89193.7 ms | 86915.4 ms | 2278.3 ms | 58394.0 ms |
| Gorm_schema | LLGoNoLTO | 79668.2 ms | 77512.7 ms | 2155.5 ms | 28002.2 ms |
| Gorm_schema | LLGoDeadcodeDrop | 78781.7 ms | 76423.2 ms | 2358.5 ms | 27992.4 ms |
| Toml | LLGoDeadcodeDrop | 77412.0 ms | 75345.5 ms | 2066.4 ms | 27351.3 ms |
| Toml | LLGoNoLTO | 75523.3 ms | 73635.3 ms | 1887.9 ms | 26379.4 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 69091.2 ms | 67484.2 ms | 1607.0 ms | 50354.8 ms |
| IXGo | Go | 63439.1 ms | 54536.6 ms | 8902.5 ms | 17398.5 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 57938.5 ms | 56359.0 ms | 1579.5 ms | 37957.9 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 55147.9 ms | 53704.9 ms | 1443.0 ms | 36279.7 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 50691.5 ms | 49312.9 ms | 1378.6 ms | 19244.7 ms |
| Dustin_humanize | LLGoNoLTO | 48798.2 ms | 47478.8 ms | 1319.4 ms | 18601.2 ms |
| Etcdctl | Go | 25991.2 ms | 22741.0 ms | 3250.2 ms | 7851.0 ms |
| XGo | Go | 15117.0 ms | 13178.5 ms | 1938.6 ms | 4474.1 ms |
| Aws_restjson | Go | 6336.0 ms | 5389.6 ms | 946.4 ms | 2594.3 ms |
| Gorm_schema | Go | 4413.7 ms | 3831.0 ms | 582.7 ms | 1724.7 ms |
| Uber_zap | Go | 4063.2 ms | 3544.7 ms | 518.5 ms | 1642.2 ms |
| K8s_workqueue | Go | 3533.9 ms | 3009.1 ms | 524.8 ms | 1274.7 ms |
| Toml | Go | 1619.5 ms | 1370.5 ms | 248.9 ms | 846.7 ms |
| Dustin_humanize | Go | 620.3 ms | 489.6 ms | 130.7 ms | 309.1 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2313147.4 ms | 1665620.1 ms | 9 |
| LLGoFullLTOGlobalDCE | 2247263.3 ms | 1578491.9 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2174774.9 ms | 1515576.9 ms | 9 |
| LLGoNoLTO | 1320036.8 ms | 438807.4 ms | 9 |
| LLGoDeadcodeDrop | 1289014.4 ms | 441353.7 ms | 9 |
| Go | 125133.8 ms | 38115.4 ms | 9 |

Dependency download details are in `download-timings.log`.
