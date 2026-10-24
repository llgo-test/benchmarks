## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 559432.2 ms | 549623.0 ms | 9809.2 ms | 367935.9 ms |
| IXGo | LLGoFullLTOGlobalDCE | 546731.2 ms | 537818.3 ms | 8912.8 ms | 359413.7 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 537784.0 ms | 528445.8 ms | 9338.1 ms | 357191.0 ms |
| IXGo | LLGoNoLTO | 313835.3 ms | 306486.6 ms | 7348.6 ms | 97021.3 ms |
| IXGo | LLGoDeadcodeDrop | 301609.0 ms | 291922.6 ms | 9686.4 ms | 97890.3 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 282759.9 ms | 278413.4 ms | 4346.5 ms | 216161.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 276022.7 ms | 271723.8 ms | 4298.8 ms | 208900.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 273450.5 ms | 268682.4 ms | 4768.1 ms | 206967.7 ms |
| XGo | LLGoFullLTONoGlobalDCE | 208406.2 ms | 205273.4 ms | 3132.8 ms | 172359.2 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 205071.1 ms | 202088.6 ms | 2982.6 ms | 146181.5 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 182115.5 ms | 179199.2 ms | 2916.4 ms | 145515.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 181781.3 ms | 178947.0 ms | 2834.3 ms | 123018.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 180923.2 ms | 178154.8 ms | 2768.4 ms | 122425.0 ms |
| XGo | LLGoFullLTOGlobalDCE | 178843.1 ms | 176006.6 ms | 2836.5 ms | 142770.8 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 171524.0 ms | 168898.6 ms | 2625.4 ms | 127068.9 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 167884.2 ms | 165283.9 ms | 2600.3 ms | 125325.8 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 163165.7 ms | 160487.3 ms | 2678.4 ms | 122213.2 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 151900.1 ms | 149499.4 ms | 2400.7 ms | 108078.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 151714.7 ms | 149297.1 ms | 2417.5 ms | 107638.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 147135.9 ms | 144650.3 ms | 2485.6 ms | 103036.9 ms |
| Aws_restjson | LLGoDeadcodeDrop | 143255.4 ms | 140776.1 ms | 2479.3 ms | 51164.7 ms |
| Aws_restjson | LLGoNoLTO | 141464.1 ms | 139091.2 ms | 2372.8 ms | 50165.2 ms |
| Etcdctl | LLGoNoLTO | 139406.5 ms | 136014.3 ms | 3392.1 ms | 50220.3 ms |
| Etcdctl | LLGoDeadcodeDrop | 136853.5 ms | 133196.8 ms | 3656.7 ms | 49571.6 ms |
| Uber_zap | LLGoNoLTO | 120163.3 ms | 118185.8 ms | 1977.5 ms | 45688.4 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 114398.2 ms | 112202.3 ms | 2195.9 ms | 43972.8 ms |
| Uber_zap | LLGoDeadcodeDrop | 113964.9 ms | 111777.2 ms | 2187.7 ms | 43375.2 ms |
| K8s_workqueue | LLGoNoLTO | 109786.6 ms | 107834.1 ms | 1952.6 ms | 41265.4 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 87598.0 ms | 86009.5 ms | 1588.5 ms | 63801.7 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 86596.8 ms | 84991.7 ms | 1605.1 ms | 62585.4 ms |
| Toml | LLGoFullLTONoGlobalDCE | 79459.0 ms | 77826.7 ms | 1632.3 ms | 57365.2 ms |
| XGo | LLGoNoLTO | 76776.0 ms | 74730.9 ms | 2045.1 ms | 30903.1 ms |
| XGo | LLGoDeadcodeDrop | 76430.0 ms | 73952.7 ms | 2477.3 ms | 30754.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 73261.5 ms | 71756.1 ms | 1505.4 ms | 47968.9 ms |
| Toml | LLGoFullLTOGlobalDCE | 69695.6 ms | 68097.9 ms | 1597.7 ms | 45988.0 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 67791.6 ms | 66239.2 ms | 1552.5 ms | 45093.0 ms |
| Gorm_schema | LLGoDeadcodeDrop | 61387.8 ms | 59959.6 ms | 1428.2 ms | 21216.1 ms |
| Gorm_schema | LLGoNoLTO | 60792.2 ms | 59547.4 ms | 1244.8 ms | 20724.3 ms |
| Toml | LLGoNoLTO | 57321.8 ms | 55986.9 ms | 1334.9 ms | 19660.9 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 57232.7 ms | 56041.6 ms | 1191.1 ms | 42876.5 ms |
| Toml | LLGoDeadcodeDrop | 55923.6 ms | 54463.3 ms | 1460.3 ms | 19301.8 ms |
| IXGo | Go | 48510.4 ms | 45076.7 ms | 3433.7 ms | 13545.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 44828.1 ms | 43732.5 ms | 1095.5 ms | 30305.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 44333.1 ms | 43284.9 ms | 1048.2 ms | 29753.3 ms |
| Dustin_humanize | LLGoNoLTO | 39098.2 ms | 38182.8 ms | 915.4 ms | 14381.0 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 38998.7 ms | 37958.6 ms | 1040.2 ms | 14626.7 ms |
| Etcdctl | Go | 20135.4 ms | 18694.5 ms | 1440.9 ms | 6059.0 ms |
| XGo | Go | 11488.3 ms | 10606.6 ms | 881.7 ms | 3783.0 ms |
| Aws_restjson | Go | 4882.6 ms | 4405.0 ms | 477.6 ms | 1997.4 ms |
| Gorm_schema | Go | 3350.7 ms | 3053.6 ms | 297.1 ms | 1296.0 ms |
| Uber_zap | Go | 3282.5 ms | 3021.0 ms | 261.5 ms | 1292.0 ms |
| K8s_workqueue | Go | 2795.8 ms | 2478.6 ms | 317.2 ms | 1013.3 ms |
| Toml | Go | 1215.0 ms | 1056.9 ms | 158.2 ms | 591.0 ms |
| Dustin_humanize | Go | 520.5 ms | 399.3 ms | 121.2 ms | 338.0 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1797719.1 ms | 1308331.3 ms | 9 |
| LLGoFullLTOGlobalDCE | 1695453.9 ms | 1199755.3 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1684268.9 ms | 1179854.2 ms | 9 |
| LLGoNoLTO | 1058644.0 ms | 370029.9 ms | 9 |
| LLGoDeadcodeDrop | 1042821.1 ms | 371873.5 ms | 9 |
| Go | 96181.2 ms | 29915.3 ms | 9 |

Dependency download details are in `download-timings.log`.
