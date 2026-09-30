## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 619885.6 ms | 608672.5 ms | 11213.1 ms | 316666.1 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 613614.6 ms | 602627.5 ms | 10987.0 ms | 322447.9 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 583934.2 ms | 572690.6 ms | 11243.7 ms | 307600.9 ms |
| IXGo | LLGoDeadcodeDrop | 482553.6 ms | 472753.0 ms | 9800.6 ms | 146653.5 ms |
| IXGo | LLGoNoLTO | 482272.3 ms | 472713.1 ms | 9559.2 ms | 143311.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 260822.5 ms | 256085.2 ms | 4737.3 ms | 172190.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 252403.8 ms | 247568.8 ms | 4835.1 ms | 162084.3 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 240402.7 ms | 235865.4 ms | 4537.3 ms | 156712.6 ms |
| Aws_restjson | LLGoNoLTO | 213042.5 ms | 210046.4 ms | 2996.1 ms | 76555.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 209727.7 ms | 206388.3 ms | 3339.5 ms | 117043.5 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 206902.2 ms | 203767.6 ms | 3134.6 ms | 124457.6 ms |
| Aws_restjson | LLGoDeadcodeDrop | 204111.3 ms | 201284.7 ms | 2826.6 ms | 73968.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 194663.9 ms | 191642.4 ms | 3021.5 ms | 112177.6 ms |
| Etcdctl | LLGoDeadcodeDrop | 185341.3 ms | 181000.9 ms | 4340.4 ms | 63983.9 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 181203.8 ms | 177843.6 ms | 3360.2 ms | 131287.6 ms |
| Etcdctl | LLGoNoLTO | 180386.2 ms | 176269.6 ms | 4116.6 ms | 62212.9 ms |
| XGo | LLGoFullLTOGlobalDCE | 178689.0 ms | 175481.4 ms | 3207.7 ms | 128329.4 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 176993.2 ms | 174275.8 ms | 2717.3 ms | 68872.0 ms |
| XGo | LLGoFullLTONoGlobalDCE | 176414.4 ms | 173079.2 ms | 3335.2 ms | 127960.4 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 175646.3 ms | 172963.5 ms | 2682.9 ms | 112139.7 ms |
| Uber_zap | LLGoDeadcodeDrop | 172290.1 ms | 169833.4 ms | 2456.8 ms | 66853.8 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 171482.6 ms | 168711.5 ms | 2771.2 ms | 109821.5 ms |
| Uber_zap | LLGoNoLTO | 168971.4 ms | 166526.6 ms | 2444.8 ms | 65642.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 168792.0 ms | 166063.2 ms | 2728.8 ms | 103552.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 168725.6 ms | 166101.2 ms | 2624.4 ms | 105621.2 ms |
| K8s_workqueue | LLGoNoLTO | 164090.7 ms | 161555.8 ms | 2534.9 ms | 64622.2 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 162281.7 ms | 159584.3 ms | 2697.4 ms | 104028.1 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 154902.3 ms | 152285.0 ms | 2617.3 ms | 93453.3 ms |
| XGo | LLGoNoLTO | 109368.8 ms | 106250.9 ms | 3117.9 ms | 42611.8 ms |
| XGo | LLGoDeadcodeDrop | 105979.7 ms | 103044.9 ms | 2934.9 ms | 41670.7 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 90456.6 ms | 88678.1 ms | 1778.4 ms | 54350.0 ms |
| Gorm_schema | LLGoNoLTO | 90198.1 ms | 88619.8 ms | 1578.3 ms | 30079.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 88866.3 ms | 87197.2 ms | 1669.0 ms | 52920.0 ms |
| Gorm_schema | LLGoDeadcodeDrop | 87645.5 ms | 86066.4 ms | 1579.0 ms | 29471.7 ms |
| IXGo | Go | 87486.7 ms | 81981.6 ms | 5505.1 ms | 24831.6 ms |
| Toml | LLGoDeadcodeDrop | 84480.2 ms | 82785.6 ms | 1694.6 ms | 27965.7 ms |
| Toml | LLGoFullLTONoGlobalDCE | 84176.7 ms | 82366.6 ms | 1810.1 ms | 50216.7 ms |
| Toml | LLGoNoLTO | 84161.4 ms | 82489.3 ms | 1672.0 ms | 27798.2 ms |
| Toml | LLGoFullLTOGlobalDCE | 75515.6 ms | 73818.2 ms | 1697.4 ms | 40646.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 74483.2 ms | 72964.8 ms | 1518.4 ms | 39623.4 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 73387.5 ms | 71705.6 ms | 1681.9 ms | 39831.1 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 61760.1 ms | 60493.7 ms | 1266.4 ms | 39740.4 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 57076.9 ms | 55969.4 ms | 1107.5 ms | 20524.2 ms |
| Dustin_humanize | LLGoNoLTO | 54998.6 ms | 53982.1 ms | 1016.5 ms | 19665.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 49828.3 ms | 48614.5 ms | 1213.8 ms | 28046.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 49531.2 ms | 48360.5 ms | 1170.7 ms | 27330.6 ms |
| Etcdctl | Go | 35495.9 ms | 33081.3 ms | 2414.6 ms | 11362.8 ms |
| XGo | Go | 20083.5 ms | 18788.2 ms | 1295.3 ms | 5969.8 ms |
| Aws_restjson | Go | 8506.7 ms | 7771.5 ms | 735.3 ms | 3520.9 ms |
| Gorm_schema | Go | 5949.9 ms | 5514.9 ms | 435.0 ms | 2303.8 ms |
| Uber_zap | Go | 5769.6 ms | 5161.2 ms | 608.4 ms | 2521.3 ms |
| K8s_workqueue | Go | 5136.8 ms | 4510.4 ms | 626.4 ms | 2316.7 ms |
| Toml | Go | 2176.1 ms | 1926.2 ms | 249.9 ms | 1131.4 ms |
| Dustin_humanize | Go | 846.6 ms | 693.8 ms | 152.8 ms | 407.5 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1811655.2 ms | 1092053.4 ms | 9 |
| LLGoFullLTOGlobalDCE | 1808479.4 ms | 1066419.0 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1748365.8 ms | 1021807.3 ms | 9 |
| LLGoDeadcodeDrop | 1556471.8 ms | 539964.5 ms | 9 |
| LLGoNoLTO | 1547489.9 ms | 532500.0 ms | 9 |
| Go | 171451.8 ms | 54366.0 ms | 9 |

Dependency download details are in `download-timings.log`.
