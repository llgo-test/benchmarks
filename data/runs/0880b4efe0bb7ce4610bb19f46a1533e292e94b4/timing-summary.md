## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 895394.0 ms | 884104.0 ms | 11290.0 ms | 551927.0 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 835487.1 ms | 823588.9 ms | 11898.2 ms | 513402.0 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 816834.1 ms | 805081.6 ms | 11752.5 ms | 504391.7 ms |
| IXGo | LLGoNoLTO | 505258.0 ms | 496727.1 ms | 8530.9 ms | 160617.6 ms |
| IXGo | LLGoDeadcodeDrop | 374796.1 ms | 361759.7 ms | 13036.4 ms | 120524.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 373395.0 ms | 367597.3 ms | 5797.7 ms | 280458.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 355618.0 ms | 350099.3 ms | 5518.7 ms | 268192.7 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 341746.5 ms | 336229.0 ms | 5517.5 ms | 261886.2 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 275169.5 ms | 271550.0 ms | 3619.5 ms | 190048.9 ms |
| XGo | LLGoFullLTONoGlobalDCE | 252226.0 ms | 248405.2 ms | 3820.8 ms | 207581.0 ms |
| XGo | LLGoFullLTOGlobalDCE | 248171.7 ms | 244356.5 ms | 3815.2 ms | 202027.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 243308.1 ms | 239810.2 ms | 3497.9 ms | 168410.6 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 230022.4 ms | 226623.9 ms | 3398.5 ms | 171243.7 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 225618.0 ms | 222121.3 ms | 3496.7 ms | 169644.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 223843.2 ms | 220501.6 ms | 3341.6 ms | 152907.3 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 223478.6 ms | 219871.6 ms | 3607.0 ms | 177371.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 222189.1 ms | 218730.8 ms | 3458.3 ms | 166123.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 211590.0 ms | 208394.2 ms | 3195.8 ms | 152557.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 195108.6 ms | 192006.9 ms | 3101.7 ms | 138820.2 ms |
| Aws_restjson | LLGoDeadcodeDrop | 193218.2 ms | 190029.0 ms | 3189.2 ms | 67723.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 187623.2 ms | 184548.5 ms | 3074.7 ms | 132228.6 ms |
| Aws_restjson | LLGoNoLTO | 187025.8 ms | 184110.6 ms | 2915.2 ms | 65770.8 ms |
| Etcdctl | LLGoDeadcodeDrop | 172886.7 ms | 167941.9 ms | 4944.8 ms | 63022.1 ms |
| Etcdctl | LLGoNoLTO | 171929.6 ms | 167640.2 ms | 4289.4 ms | 61562.7 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 154799.6 ms | 151842.2 ms | 2957.4 ms | 60111.0 ms |
| Uber_zap | LLGoNoLTO | 151081.1 ms | 148609.5 ms | 2471.5 ms | 58085.0 ms |
| Uber_zap | LLGoDeadcodeDrop | 150345.2 ms | 147609.4 ms | 2735.8 ms | 57986.8 ms |
| K8s_workqueue | LLGoNoLTO | 139981.9 ms | 137418.8 ms | 2563.0 ms | 54225.7 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 122711.5 ms | 120473.3 ms | 2238.2 ms | 90470.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 113710.7 ms | 111645.5 ms | 2065.2 ms | 81937.7 ms |
| Toml | LLGoFullLTONoGlobalDCE | 107122.2 ms | 105010.5 ms | 2111.7 ms | 77213.1 ms |
| XGo | LLGoNoLTO | 102151.8 ms | 99374.8 ms | 2777.0 ms | 41302.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 101788.6 ms | 99742.3 ms | 2046.4 ms | 67561.3 ms |
| XGo | LLGoDeadcodeDrop | 98336.9 ms | 95073.3 ms | 3263.6 ms | 39316.7 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 90232.0 ms | 88193.3 ms | 2038.7 ms | 60364.3 ms |
| Toml | LLGoFullLTOGlobalDCE | 84304.3 ms | 82398.3 ms | 1906.1 ms | 55740.4 ms |
| Gorm_schema | LLGoNoLTO | 79803.3 ms | 78174.7 ms | 1628.6 ms | 27194.2 ms |
| Gorm_schema | LLGoDeadcodeDrop | 76259.9 ms | 74495.3 ms | 1764.6 ms | 26331.9 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 75455.3 ms | 73881.6 ms | 1573.7 ms | 56706.4 ms |
| Toml | LLGoDeadcodeDrop | 71366.9 ms | 69561.3 ms | 1805.6 ms | 24382.9 ms |
| Toml | LLGoNoLTO | 71041.3 ms | 69426.3 ms | 1615.0 ms | 24224.0 ms |
| IXGo | Go | 61572.7 ms | 57445.3 ms | 4127.5 ms | 17794.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 58561.6 ms | 57118.2 ms | 1443.4 ms | 39551.5 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 54848.8 ms | 53536.3 ms | 1312.6 ms | 36633.5 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 50890.9 ms | 49497.6 ms | 1393.3 ms | 19062.9 ms |
| Dustin_humanize | LLGoNoLTO | 48805.1 ms | 47624.1 ms | 1181.0 ms | 17939.9 ms |
| Etcdctl | Go | 25697.4 ms | 23994.4 ms | 1702.9 ms | 7885.9 ms |
| XGo | Go | 14171.1 ms | 13214.9 ms | 956.2 ms | 4204.1 ms |
| Aws_restjson | Go | 5901.0 ms | 5360.9 ms | 540.1 ms | 2416.9 ms |
| Gorm_schema | Go | 4485.3 ms | 4111.3 ms | 373.9 ms | 1708.5 ms |
| Uber_zap | Go | 4072.8 ms | 3693.7 ms | 379.1 ms | 1618.6 ms |
| K8s_workqueue | Go | 3557.5 ms | 3180.0 ms | 377.5 ms | 1261.9 ms |
| Toml | Go | 1589.5 ms | 1381.7 ms | 207.8 ms | 850.7 ms |
| Dustin_humanize | Go | 604.4 ms | 472.8 ms | 131.6 ms | 289.6 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2446905.5 ms | 1729185.7 ms | 9 |
| LLGoFullLTOGlobalDCE | 2409670.0 ms | 1668047.9 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2308982.8 ms | 1578168.7 ms | 9 |
| LLGoNoLTO | 1457077.9 ms | 510922.7 ms | 9 |
| LLGoDeadcodeDrop | 1342900.3 ms | 478461.7 ms | 9 |
| Go | 121651.7 ms | 38030.7 ms | 9 |

Dependency download details are in `download-timings.log`.
