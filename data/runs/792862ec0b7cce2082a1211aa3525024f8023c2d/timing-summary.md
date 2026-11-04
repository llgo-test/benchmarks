## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 1055977.5 ms | 1029476.5 ms | 26501.0 ms | 624644.0 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 835176.8 ms | 809133.1 ms | 26043.7 ms | 527277.8 ms |
| IXGo | LLGoFullLTOGlobalDCE | 830300.3 ms | 804674.3 ms | 25626.0 ms | 522410.8 ms |
| IXGo | LLGoNoLTO | 509485.8 ms | 486924.1 ms | 22561.7 ms | 153135.6 ms |
| IXGo | LLGoDeadcodeDrop | 504376.9 ms | 478372.2 ms | 26004.7 ms | 155462.7 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 420559.1 ms | 408595.3 ms | 11963.9 ms | 307046.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 420073.0 ms | 408037.2 ms | 12035.8 ms | 303679.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 417574.3 ms | 405480.6 ms | 12093.7 ms | 301904.9 ms |
| XGo | LLGoFullLTONoGlobalDCE | 329003.9 ms | 320652.6 ms | 8351.3 ms | 262861.3 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 313960.4 ms | 307269.8 ms | 6690.6 ms | 215890.2 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 270239.5 ms | 262487.5 ms | 7752.0 ms | 205306.4 ms |
| XGo | LLGoFullLTOGlobalDCE | 268085.9 ms | 260372.2 ms | 7713.7 ms | 203738.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 259008.4 ms | 252860.0 ms | 6148.4 ms | 165470.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 258831.3 ms | 252667.0 ms | 6164.4 ms | 165564.9 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 246637.0 ms | 240999.0 ms | 5638.0 ms | 173783.9 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 243788.0 ms | 238406.1 ms | 5381.9 ms | 170710.8 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 233013.1 ms | 227627.7 ms | 5385.3 ms | 163439.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 231081.2 ms | 225808.4 ms | 5272.8 ms | 154236.0 ms |
| Etcdctl | LLGoDeadcodeDrop | 224515.5 ms | 213730.3 ms | 10785.3 ms | 76225.1 ms |
| Etcdctl | LLGoNoLTO | 221581.7 ms | 212396.8 ms | 9184.9 ms | 74544.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 216131.1 ms | 210923.4 ms | 5207.7 ms | 143252.0 ms |
| Aws_restjson | LLGoNoLTO | 211088.1 ms | 205941.4 ms | 5146.8 ms | 66264.9 ms |
| Aws_restjson | LLGoDeadcodeDrop | 207969.0 ms | 202305.4 ms | 5663.6 ms | 65417.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 199950.6 ms | 194943.6 ms | 5007.0 ms | 130452.7 ms |
| Uber_zap | LLGoNoLTO | 179611.1 ms | 175277.8 ms | 4333.3 ms | 57750.3 ms |
| Uber_zap | LLGoDeadcodeDrop | 171004.1 ms | 166460.9 ms | 4543.1 ms | 54894.4 ms |
| K8s_workqueue | LLGoNoLTO | 162833.2 ms | 158814.1 ms | 4019.2 ms | 52269.8 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 162361.5 ms | 157641.2 ms | 4720.2 ms | 52570.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 145748.3 ms | 141964.1 ms | 3784.1 ms | 100699.1 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 143115.2 ms | 139293.0 ms | 3822.2 ms | 99734.6 ms |
| Toml | LLGoFullLTONoGlobalDCE | 130975.5 ms | 127619.1 ms | 3356.4 ms | 90392.7 ms |
| XGo | LLGoNoLTO | 124818.3 ms | 118861.2 ms | 5957.0 ms | 44818.2 ms |
| XGo | LLGoDeadcodeDrop | 124669.8 ms | 117431.0 ms | 7238.8 ms | 43886.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 119155.4 ms | 115576.6 ms | 3578.7 ms | 74809.8 ms |
| Toml | LLGoFullLTOGlobalDCE | 114349.9 ms | 111042.9 ms | 3307.0 ms | 72645.5 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 114143.2 ms | 110846.9 ms | 3296.2 ms | 72847.9 ms |
| Gorm_schema | LLGoDeadcodeDrop | 105857.2 ms | 102450.6 ms | 3406.6 ms | 36478.7 ms |
| Gorm_schema | LLGoNoLTO | 104643.9 ms | 101595.2 ms | 3048.7 ms | 35459.9 ms |
| Toml | LLGoDeadcodeDrop | 98880.0 ms | 95925.0 ms | 2955.0 ms | 33518.1 ms |
| IXGo | Go | 98652.1 ms | 83556.1 ms | 15096.0 ms | 26862.9 ms |
| Toml | LLGoNoLTO | 98622.6 ms | 95988.8 ms | 2633.7 ms | 33062.4 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 94647.9 ms | 92237.8 ms | 2410.1 ms | 67631.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 76160.4 ms | 73961.0 ms | 2199.5 ms | 48781.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 73905.0 ms | 71705.8 ms | 2199.2 ms | 47321.1 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 68182.6 ms | 66063.8 ms | 2118.8 ms | 25117.6 ms |
| Dustin_humanize | LLGoNoLTO | 67182.6 ms | 65307.1 ms | 1875.5 ms | 24613.0 ms |
| Etcdctl | Go | 37970.3 ms | 32708.7 ms | 5261.7 ms | 11428.5 ms |
| XGo | Go | 21955.0 ms | 18945.2 ms | 3009.9 ms | 6430.1 ms |
| Aws_restjson | Go | 9253.1 ms | 7706.4 ms | 1546.7 ms | 3784.6 ms |
| Gorm_schema | Go | 6711.5 ms | 5645.7 ms | 1065.8 ms | 2840.0 ms |
| Uber_zap | Go | 6002.3 ms | 5116.1 ms | 886.2 ms | 2428.2 ms |
| K8s_workqueue | Go | 5325.5 ms | 4475.4 ms | 850.1 ms | 2019.0 ms |
| Toml | Go | 2354.0 ms | 1949.6 ms | 404.4 ms | 1134.6 ms |
| Dustin_humanize | Go | 896.3 ms | 697.2 ms | 199.2 ms | 445.6 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2757863.8 ms | 1915329.5 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2745612.1 ms | 1780321.8 ms | 9 |
| LLGoFullLTOGlobalDCE | 2558116.3 ms | 1720882.6 ms | 9 |
| LLGoNoLTO | 1679867.3 ms | 541918.8 ms | 9 |
| LLGoDeadcodeDrop | 1667816.6 ms | 543570.8 ms | 9 |
| Go | 189120.1 ms | 57373.5 ms | 9 |

Dependency download details are in `download-timings.log`.
