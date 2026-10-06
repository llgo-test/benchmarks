## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 515815.0 ms | 507051.0 ms | 8764.0 ms | 260765.9 ms |
| IXGo | LLGoFullLTOGlobalDCE | 484102.4 ms | 475190.7 ms | 8911.6 ms | 249499.9 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 483290.5 ms | 475143.8 ms | 8146.7 ms | 252947.2 ms |
| IXGo | LLGoDeadcodeDrop | 425360.0 ms | 415315.2 ms | 10044.8 ms | 125258.9 ms |
| IXGo | LLGoNoLTO | 360659.4 ms | 352678.6 ms | 7980.8 ms | 104776.1 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 241123.7 ms | 236735.4 ms | 4388.4 ms | 150907.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 232032.4 ms | 227878.6 ms | 4153.9 ms | 142713.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 219150.2 ms | 215264.7 ms | 3885.5 ms | 132934.0 ms |
| Aws_restjson | LLGoDeadcodeDrop | 213844.4 ms | 211001.5 ms | 2842.9 ms | 67904.3 ms |
| XGo | LLGoFullLTOGlobalDCE | 182979.6 ms | 180118.5 ms | 2861.1 ms | 124328.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 182736.7 ms | 179694.2 ms | 3042.5 ms | 96086.6 ms |
| XGo | LLGoFullLTONoGlobalDCE | 176869.3 ms | 174147.9 ms | 2721.3 ms | 119096.8 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 176122.3 ms | 173142.0 ms | 2980.3 ms | 101334.4 ms |
| Etcdctl | LLGoDeadcodeDrop | 174087.5 ms | 169632.7 ms | 4454.8 ms | 58086.7 ms |
| Aws_restjson | LLGoNoLTO | 172070.8 ms | 169446.2 ms | 2624.6 ms | 58834.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 172012.2 ms | 169073.6 ms | 2938.6 ms | 92931.9 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 168139.1 ms | 165551.3 ms | 2587.8 ms | 113829.7 ms |
| Etcdctl | LLGoNoLTO | 165892.0 ms | 162510.2 ms | 3381.9 ms | 54319.8 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 156021.1 ms | 153280.0 ms | 2741.1 ms | 93322.0 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 155776.0 ms | 153003.1 ms | 2773.0 ms | 92802.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 155048.3 ms | 152289.9 ms | 2758.4 ms | 87569.7 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 148696.2 ms | 146147.8 ms | 2548.4 ms | 89776.6 ms |
| Uber_zap | LLGoDeadcodeDrop | 146721.8 ms | 144495.4 ms | 2226.4 ms | 52435.9 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 143107.6 ms | 140602.2 ms | 2505.4 ms | 81340.8 ms |
| Uber_zap | LLGoNoLTO | 141799.7 ms | 139648.4 ms | 2151.3 ms | 50777.5 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 137011.6 ms | 134805.1 ms | 2206.5 ms | 49172.6 ms |
| K8s_workqueue | LLGoNoLTO | 136414.6 ms | 134166.5 ms | 2248.1 ms | 48568.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 133231.6 ms | 130819.8 ms | 2411.7 ms | 74095.8 ms |
| XGo | LLGoDeadcodeDrop | 109179.3 ms | 106348.7 ms | 2830.6 ms | 39979.2 ms |
| XGo | LLGoNoLTO | 103674.9 ms | 101434.1 ms | 2240.8 ms | 37198.9 ms |
| Gorm_schema | LLGoDeadcodeDrop | 71991.4 ms | 70582.6 ms | 1408.8 ms | 24481.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 71560.5 ms | 70044.0 ms | 1516.4 ms | 43569.9 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 70364.2 ms | 68861.6 ms | 1502.6 ms | 42788.0 ms |
| Gorm_schema | LLGoNoLTO | 67363.3 ms | 66015.1 ms | 1348.2 ms | 22766.6 ms |
| Toml | LLGoNoLTO | 65264.9 ms | 63848.1 ms | 1416.8 ms | 22120.4 ms |
| Toml | LLGoFullLTONoGlobalDCE | 65084.9 ms | 63557.1 ms | 1527.8 ms | 39356.4 ms |
| Toml | LLGoDeadcodeDrop | 62499.2 ms | 61157.3 ms | 1342.0 ms | 21364.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 62271.9 ms | 60762.9 ms | 1509.0 ms | 34096.3 ms |
| Toml | LLGoFullLTOGlobalDCE | 59323.2 ms | 57879.1 ms | 1444.2 ms | 32488.9 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 58995.2 ms | 57536.1 ms | 1459.1 ms | 32476.7 ms |
| IXGo | Go | 51293.2 ms | 47559.4 ms | 3733.8 ms | 14425.6 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 49669.8 ms | 48589.8 ms | 1080.0 ms | 31634.8 ms |
| Dustin_humanize | LLGoNoLTO | 46989.1 ms | 46001.1 ms | 988.0 ms | 17142.1 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 46815.4 ms | 45846.5 ms | 968.9 ms | 17044.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 42355.6 ms | 41303.5 ms | 1052.1 ms | 23656.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 41251.7 ms | 40173.2 ms | 1078.5 ms | 23463.4 ms |
| Etcdctl | Go | 21207.1 ms | 19660.1 ms | 1547.0 ms | 6357.8 ms |
| XGo | Go | 12929.5 ms | 11996.6 ms | 932.9 ms | 3992.7 ms |
| Aws_restjson | Go | 5158.9 ms | 4646.7 ms | 512.3 ms | 2131.4 ms |
| Gorm_schema | Go | 3705.0 ms | 3401.7 ms | 303.3 ms | 1431.3 ms |
| Uber_zap | Go | 3399.7 ms | 3098.2 ms | 301.5 ms | 1498.7 ms |
| K8s_workqueue | Go | 3097.0 ms | 2787.7 ms | 309.3 ms | 1124.0 ms |
| Toml | Go | 1303.0 ms | 1127.2 ms | 175.8 ms | 612.6 ms |
| Dustin_humanize | Go | 515.9 ms | 402.5 ms | 113.4 ms | 255.0 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1566996.9 ms | 920643.6 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1549522.0 ms | 865097.1 ms | 9 |
| LLGoFullLTOGlobalDCE | 1530612.3 ms | 874072.1 ms | 9 |
| LLGoDeadcodeDrop | 1387510.5 ms | 455727.8 ms | 9 |
| LLGoNoLTO | 1260128.7 ms | 416504.5 ms | 9 |
| Go | 102609.4 ms | 31829.0 ms | 9 |

Dependency download details are in `download-timings.log`.
