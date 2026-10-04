## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 709519.9 ms | 698427.5 ms | 11092.3 ms | 356375.2 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 706328.0 ms | 694729.8 ms | 11598.2 ms | 354683.8 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 700660.3 ms | 689481.7 ms | 11178.6 ms | 354779.0 ms |
| IXGo | LLGoDeadcodeDrop | 557807.9 ms | 543967.2 ms | 13840.6 ms | 164478.9 ms |
| IXGo | LLGoNoLTO | 553831.7 ms | 544407.9 ms | 9423.8 ms | 159913.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 347695.1 ms | 342399.6 ms | 5295.6 ms | 202819.2 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 342565.4 ms | 337229.0 ms | 5336.4 ms | 201695.5 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 342250.8 ms | 336808.6 ms | 5442.2 ms | 198880.0 ms |
| Aws_restjson | LLGoDeadcodeDrop | 281536.7 ms | 278172.5 ms | 3364.2 ms | 93081.8 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 270806.9 ms | 267079.5 ms | 3727.4 ms | 150951.5 ms |
| Aws_restjson | LLGoNoLTO | 265058.1 ms | 261796.5 ms | 3261.6 ms | 89485.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 261552.3 ms | 257727.4 ms | 3824.9 ms | 136610.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 258995.0 ms | 255391.7 ms | 3603.3 ms | 136156.8 ms |
| Etcdctl | LLGoNoLTO | 258467.1 ms | 254030.4 ms | 4436.7 ms | 84111.4 ms |
| Etcdctl | LLGoDeadcodeDrop | 257916.8 ms | 252568.5 ms | 5348.3 ms | 85723.5 ms |
| XGo | LLGoFullLTONoGlobalDCE | 245791.2 ms | 242266.7 ms | 3524.6 ms | 161170.1 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 244699.3 ms | 241242.5 ms | 3456.8 ms | 159198.1 ms |
| XGo | LLGoFullLTOGlobalDCE | 243720.5 ms | 240247.2 ms | 3473.3 ms | 158750.9 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 231084.5 ms | 227793.2 ms | 3291.3 ms | 133707.1 ms |
| Uber_zap | LLGoDeadcodeDrop | 227590.8 ms | 224893.4 ms | 2697.4 ms | 80488.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 224827.6 ms | 221714.4 ms | 3113.2 ms | 129904.6 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 222818.9 ms | 219722.7 ms | 3096.2 ms | 129045.3 ms |
| Uber_zap | LLGoNoLTO | 221612.9 ms | 218994.3 ms | 2618.6 ms | 78660.9 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 221279.5 ms | 218111.4 ms | 3168.0 ms | 121752.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 219554.0 ms | 216246.1 ms | 3307.8 ms | 120885.9 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 219405.0 ms | 216532.4 ms | 2872.6 ms | 77886.7 ms |
| K8s_workqueue | LLGoNoLTO | 214594.6 ms | 211812.5 ms | 2782.1 ms | 76478.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 209448.8 ms | 206326.9 ms | 3121.9 ms | 113533.5 ms |
| XGo | LLGoNoLTO | 159789.8 ms | 156837.0 ms | 2952.8 ms | 57437.6 ms |
| XGo | LLGoDeadcodeDrop | 158119.4 ms | 154714.2 ms | 3405.2 ms | 57865.3 ms |
| Gorm_schema | LLGoDeadcodeDrop | 106184.9 ms | 104560.3 ms | 1624.6 ms | 35177.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 105858.5 ms | 103991.4 ms | 1867.1 ms | 61559.1 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 105620.0 ms | 103767.6 ms | 1852.5 ms | 62007.1 ms |
| Gorm_schema | LLGoNoLTO | 104287.0 ms | 102615.6 ms | 1671.4 ms | 34676.6 ms |
| Toml | LLGoNoLTO | 99194.3 ms | 97588.0 ms | 1606.3 ms | 32721.1 ms |
| Toml | LLGoDeadcodeDrop | 99179.4 ms | 97613.2 ms | 1566.2 ms | 32662.3 ms |
| Toml | LLGoFullLTONoGlobalDCE | 97354.9 ms | 95572.6 ms | 1782.3 ms | 56068.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 92910.9 ms | 91083.8 ms | 1827.1 ms | 48661.1 ms |
| Toml | LLGoFullLTOGlobalDCE | 89777.6 ms | 87980.0 ms | 1797.5 ms | 47643.0 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 88414.3 ms | 86673.8 ms | 1740.4 ms | 46684.0 ms |
| IXGo | Go | 82059.3 ms | 76839.3 ms | 5220.0 ms | 22604.9 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 69638.4 ms | 68457.6 ms | 1180.8 ms | 24941.8 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 69354.4 ms | 68069.6 ms | 1284.8 ms | 42170.9 ms |
| Dustin_humanize | LLGoNoLTO | 68643.4 ms | 67516.2 ms | 1127.2 ms | 24474.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 59682.6 ms | 58467.4 ms | 1215.1 ms | 32241.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 59363.7 ms | 58169.7 ms | 1194.0 ms | 31951.5 ms |
| Etcdctl | Go | 33223.7 ms | 31164.8 ms | 2058.8 ms | 10064.0 ms |
| XGo | Go | 18895.9 ms | 17748.8 ms | 1147.1 ms | 5538.8 ms |
| Aws_restjson | Go | 8073.5 ms | 7409.6 ms | 664.0 ms | 3551.7 ms |
| Gorm_schema | Go | 5693.0 ms | 5271.9 ms | 421.1 ms | 2239.1 ms |
| Uber_zap | Go | 5293.0 ms | 4907.3 ms | 385.6 ms | 2066.8 ms |
| K8s_workqueue | Go | 4572.5 ms | 4178.5 ms | 393.9 ms | 1610.9 ms |
| Toml | Go | 1982.9 ms | 1771.3 ms | 211.6 ms | 909.4 ms |
| Dustin_humanize | Go | 774.9 ms | 660.1 ms | 114.8 ms | 380.4 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2291724.4 ms | 1291499.9 ms | 9 |
| LLGoFullLTOGlobalDCE | 2254186.4 ms | 1242397.2 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2226024.2 ms | 1215988.5 ms | 9 |
| LLGoDeadcodeDrop | 1977379.3 ms | 652306.2 ms | 9 |
| LLGoNoLTO | 1945479.0 ms | 637960.0 ms | 9 |
| Go | 160568.5 ms | 48966.0 ms | 9 |

Dependency download details are in `download-timings.log`.
