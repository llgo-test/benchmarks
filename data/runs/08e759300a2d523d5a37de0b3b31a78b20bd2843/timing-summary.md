## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 665343.9 ms | 649026.8 ms | 16317.2 ms | 426563.6 ms |
| IXGo | LLGoFullLTOGlobalDCE | 659379.2 ms | 642813.6 ms | 16565.6 ms | 420929.3 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 657410.2 ms | 640983.0 ms | 16427.3 ms | 426061.8 ms |
| IXGo | LLGoNoLTO | 382781.2 ms | 368229.7 ms | 14551.6 ms | 115281.6 ms |
| IXGo | LLGoDeadcodeDrop | 370275.5 ms | 353356.9 ms | 16918.6 ms | 116289.4 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 319980.5 ms | 312265.1 ms | 7715.4 ms | 243947.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 317469.5 ms | 309466.4 ms | 8003.1 ms | 239871.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 313951.5 ms | 306126.0 ms | 7825.5 ms | 237429.6 ms |
| XGo | LLGoFullLTONoGlobalDCE | 237663.3 ms | 232068.1 ms | 5595.2 ms | 194632.4 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 224000.6 ms | 219687.0 ms | 4313.6 ms | 157845.0 ms |
| XGo | LLGoFullLTOGlobalDCE | 201837.7 ms | 196771.6 ms | 5066.2 ms | 158401.7 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 199961.0 ms | 194801.5 ms | 5159.5 ms | 156829.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 189218.0 ms | 185251.6 ms | 3966.4 ms | 124668.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 188274.3 ms | 184411.5 ms | 3862.8 ms | 122658.5 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 177281.9 ms | 173751.1 ms | 3530.8 ms | 130374.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 168162.8 ms | 164690.3 ms | 3472.5 ms | 124759.0 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 165624.5 ms | 162097.5 ms | 3527.1 ms | 122699.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 158793.3 ms | 155211.6 ms | 3581.7 ms | 109666.2 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 157592.0 ms | 154260.4 ms | 3331.6 ms | 109246.9 ms |
| Etcdctl | LLGoNoLTO | 153416.0 ms | 147259.3 ms | 6156.7 ms | 52549.3 ms |
| Etcdctl | LLGoDeadcodeDrop | 152828.7 ms | 146304.2 ms | 6524.5 ms | 53365.5 ms |
| Aws_restjson | LLGoNoLTO | 152428.0 ms | 149113.5 ms | 3314.5 ms | 47743.3 ms |
| Aws_restjson | LLGoDeadcodeDrop | 147301.9 ms | 143719.1 ms | 3582.8 ms | 47036.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 143146.5 ms | 139874.9 ms | 3271.6 ms | 97364.4 ms |
| Uber_zap | LLGoDeadcodeDrop | 114632.3 ms | 111496.3 ms | 3136.0 ms | 37944.2 ms |
| Uber_zap | LLGoNoLTO | 112007.1 ms | 109407.3 ms | 2599.8 ms | 36845.7 ms |
| K8s_workqueue | LLGoNoLTO | 107608.9 ms | 104876.5 ms | 2732.4 ms | 36085.9 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 107305.7 ms | 104460.4 ms | 2845.3 ms | 35731.6 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 105042.5 ms | 102436.7 ms | 2605.8 ms | 75504.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 98752.4 ms | 96247.6 ms | 2504.7 ms | 70811.4 ms |
| Toml | LLGoFullLTONoGlobalDCE | 90933.3 ms | 88767.0 ms | 2166.3 ms | 65374.5 ms |
| XGo | LLGoDeadcodeDrop | 85226.3 ms | 80881.4 ms | 4344.9 ms | 31045.0 ms |
| XGo | LLGoNoLTO | 83858.8 ms | 79978.3 ms | 3880.5 ms | 30961.8 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 80881.9 ms | 78695.5 ms | 2186.4 ms | 54334.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 80652.8 ms | 78395.1 ms | 2257.6 ms | 52964.2 ms |
| Toml | LLGoFullLTOGlobalDCE | 79500.7 ms | 77451.7 ms | 2048.9 ms | 52459.9 ms |
| Gorm_schema | LLGoNoLTO | 69412.3 ms | 67381.3 ms | 2031.0 ms | 24015.4 ms |
| Gorm_schema | LLGoDeadcodeDrop | 69151.7 ms | 66868.7 ms | 2283.0 ms | 24657.9 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 65095.4 ms | 63504.2 ms | 1591.2 ms | 49045.7 ms |
| Toml | LLGoNoLTO | 63558.0 ms | 61770.5 ms | 1787.5 ms | 21998.5 ms |
| Toml | LLGoDeadcodeDrop | 63490.7 ms | 61647.5 ms | 1843.3 ms | 22240.8 ms |
| IXGo | Go | 62921.4 ms | 53882.0 ms | 9039.4 ms | 17202.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 50169.0 ms | 48755.3 ms | 1413.7 ms | 33514.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 50154.7 ms | 48718.3 ms | 1436.4 ms | 33552.8 ms |
| Dustin_humanize | LLGoNoLTO | 44942.1 ms | 43611.7 ms | 1330.4 ms | 16931.5 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 43527.4 ms | 42174.7 ms | 1352.7 ms | 16640.0 ms |
| Etcdctl | Go | 25181.5 ms | 21913.6 ms | 3267.9 ms | 7728.3 ms |
| XGo | Go | 14055.8 ms | 12190.6 ms | 1865.2 ms | 4218.8 ms |
| Aws_restjson | Go | 5881.6 ms | 5023.3 ms | 858.3 ms | 2416.8 ms |
| Uber_zap | Go | 4372.6 ms | 3814.6 ms | 558.0 ms | 1727.0 ms |
| Gorm_schema | Go | 4270.6 ms | 3733.4 ms | 537.2 ms | 1659.5 ms |
| K8s_workqueue | Go | 3373.6 ms | 2869.6 ms | 504.0 ms | 1227.7 ms |
| Toml | Go | 1476.9 ms | 1276.0 ms | 200.9 ms | 697.0 ms |
| Dustin_humanize | Go | 597.4 ms | 468.1 ms | 129.4 ms | 475.4 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2043032.2 ms | 1465485.3 ms | 9 |
| LLGoFullLTOGlobalDCE | 1921137.6 ms | 1332653.4 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1882103.5 ms | 1293373.2 ms | 9 |
| LLGoNoLTO | 1170012.4 ms | 382413.0 ms | 9 |
| LLGoDeadcodeDrop | 1153740.3 ms | 384951.1 ms | 9 |
| Go | 122131.5 ms | 37352.5 ms | 9 |

Dependency download details are in `download-timings.log`.
