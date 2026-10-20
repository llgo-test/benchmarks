## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 949129.6 ms | 935897.7 ms | 13231.9 ms | 581580.7 ms |
| IXGo | LLGoFullLTOGlobalDCE | 883378.1 ms | 871909.3 ms | 11468.8 ms | 552928.3 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 870762.8 ms | 858282.7 ms | 12480.1 ms | 553952.3 ms |
| IXGo | LLGoDeadcodeDrop | 514743.6 ms | 500618.2 ms | 14125.4 ms | 161546.0 ms |
| IXGo | LLGoNoLTO | 502637.7 ms | 493765.1 ms | 8872.6 ms | 154258.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 431310.8 ms | 425407.0 ms | 5903.7 ms | 317416.7 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 428341.9 ms | 422734.4 ms | 5607.5 ms | 318519.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 426737.9 ms | 421018.2 ms | 5719.7 ms | 313018.2 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 328965.3 ms | 325071.4 ms | 3893.9 ms | 228375.9 ms |
| XGo | LLGoFullLTONoGlobalDCE | 324331.1 ms | 320040.2 ms | 4290.9 ms | 261923.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 292086.7 ms | 288396.8 ms | 3689.9 ms | 192362.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 288528.3 ms | 284755.3 ms | 3773.0 ms | 190554.0 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 283288.5 ms | 279350.0 ms | 3938.5 ms | 220157.8 ms |
| XGo | LLGoFullLTOGlobalDCE | 281921.0 ms | 278011.8 ms | 3909.3 ms | 219068.1 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 274531.0 ms | 271072.5 ms | 3458.5 ms | 198217.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 266349.1 ms | 262864.0 ms | 3485.1 ms | 192334.7 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 265716.4 ms | 262289.3 ms | 3427.0 ms | 192897.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 255006.0 ms | 251639.7 ms | 3366.3 ms | 174915.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 248043.5 ms | 244820.7 ms | 3222.8 ms | 171081.5 ms |
| Aws_restjson | LLGoNoLTO | 243627.0 ms | 240542.0 ms | 3085.0 ms | 84682.5 ms |
| Aws_restjson | LLGoDeadcodeDrop | 234916.5 ms | 231571.6 ms | 3345.0 ms | 82182.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 232997.3 ms | 229628.9 ms | 3368.3 ms | 159213.5 ms |
| Etcdctl | LLGoNoLTO | 226308.8 ms | 221833.4 ms | 4475.4 ms | 79360.2 ms |
| Etcdctl | LLGoDeadcodeDrop | 226230.6 ms | 220797.3 ms | 5433.3 ms | 80157.4 ms |
| Uber_zap | LLGoNoLTO | 196427.5 ms | 193934.8 ms | 2492.7 ms | 73332.5 ms |
| Uber_zap | LLGoDeadcodeDrop | 196307.3 ms | 193410.2 ms | 2897.1 ms | 73340.9 ms |
| K8s_workqueue | LLGoNoLTO | 192319.7 ms | 189652.5 ms | 2667.2 ms | 72038.3 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 189859.8 ms | 187001.6 ms | 2858.2 ms | 71696.6 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 147459.2 ms | 145304.4 ms | 2154.7 ms | 104413.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 143761.6 ms | 141602.2 ms | 2159.5 ms | 100564.9 ms |
| XGo | LLGoDeadcodeDrop | 131050.2 ms | 127330.8 ms | 3719.4 ms | 49811.9 ms |
| XGo | LLGoNoLTO | 129909.0 ms | 126973.0 ms | 2935.9 ms | 50743.5 ms |
| Toml | LLGoFullLTONoGlobalDCE | 129504.5 ms | 127229.2 ms | 2275.3 ms | 90714.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 117094.9 ms | 115154.1 ms | 1940.8 ms | 73642.2 ms |
| Toml | LLGoFullLTOGlobalDCE | 114734.1 ms | 112688.6 ms | 2045.5 ms | 73963.8 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 111743.0 ms | 109584.8 ms | 2158.2 ms | 71605.5 ms |
| Gorm_schema | LLGoDeadcodeDrop | 106040.8 ms | 104166.3 ms | 1874.4 ms | 35790.1 ms |
| Gorm_schema | LLGoNoLTO | 105199.6 ms | 103600.5 ms | 1599.1 ms | 35081.6 ms |
| Toml | LLGoDeadcodeDrop | 99581.9 ms | 97638.9 ms | 1943.0 ms | 33174.3 ms |
| Toml | LLGoNoLTO | 97111.8 ms | 95316.6 ms | 1795.2 ms | 32207.9 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 95930.4 ms | 94324.7 ms | 1605.7 ms | 70098.0 ms |
| IXGo | Go | 83997.6 ms | 79050.2 ms | 4947.3 ms | 23047.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 74919.7 ms | 73482.9 ms | 1436.8 ms | 48446.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 74071.3 ms | 72677.2 ms | 1394.0 ms | 47990.8 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 67521.9 ms | 66148.2 ms | 1373.7 ms | 24423.9 ms |
| Dustin_humanize | LLGoNoLTO | 67436.3 ms | 66246.9 ms | 1189.4 ms | 24235.8 ms |
| Etcdctl | Go | 33414.5 ms | 31501.8 ms | 1912.7 ms | 10032.7 ms |
| XGo | Go | 18956.6 ms | 17812.6 ms | 1144.0 ms | 5632.1 ms |
| Aws_restjson | Go | 8155.8 ms | 7370.4 ms | 785.5 ms | 3763.4 ms |
| Gorm_schema | Go | 5725.0 ms | 5337.0 ms | 388.0 ms | 2188.0 ms |
| Uber_zap | Go | 5335.0 ms | 4916.3 ms | 418.7 ms | 2070.8 ms |
| K8s_workqueue | Go | 4655.4 ms | 4188.8 ms | 466.6 ms | 1677.8 ms |
| Toml | Go | 2041.6 ms | 1787.5 ms | 254.1 ms | 944.0 ms |
| Dustin_humanize | Go | 817.6 ms | 674.4 ms | 143.2 ms | 390.1 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2865542.6 ms | 2019111.7 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2746728.0 ms | 1838884.5 ms | 9 |
| LLGoFullLTOGlobalDCE | 2728373.3 ms | 1861960.2 ms | 9 |
| LLGoDeadcodeDrop | 1766252.6 ms | 612123.5 ms | 9 |
| LLGoNoLTO | 1760977.3 ms | 605940.7 ms | 9 |
| Go | 163099.1 ms | 49746.5 ms | 9 |

Dependency download details are in `download-timings.log`.
