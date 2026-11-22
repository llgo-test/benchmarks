## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 838044.0 ms | 812116.2 ms | 25927.7 ms | 537460.5 ms |
| IXGo | LLGoFullLTOGlobalDCE | 820375.9 ms | 794259.3 ms | 26116.5 ms | 523152.1 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 808857.7 ms | 783200.5 ms | 25657.2 ms | 518355.9 ms |
| IXGo | LLGoDeadcodeDrop | 508682.3 ms | 481850.6 ms | 26831.7 ms | 163758.9 ms |
| IXGo | LLGoNoLTO | 485370.5 ms | 463369.0 ms | 22001.5 ms | 152130.6 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 441951.0 ms | 429607.3 ms | 12343.6 ms | 315590.0 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 438637.9 ms | 426390.2 ms | 12247.7 ms | 315470.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 435935.1 ms | 423967.0 ms | 11968.1 ms | 311970.4 ms |
| XGo | LLGoFullLTONoGlobalDCE | 322127.4 ms | 313678.9 ms | 8448.5 ms | 252074.5 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 306751.7 ms | 299824.4 ms | 6927.3 ms | 205774.9 ms |
| XGo | LLGoFullLTOGlobalDCE | 283944.5 ms | 275867.3 ms | 8077.2 ms | 213058.0 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 282190.8 ms | 274310.3 ms | 7880.4 ms | 211626.1 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 278723.2 ms | 272352.6 ms | 6370.6 ms | 174386.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 275239.6 ms | 268726.1 ms | 6513.6 ms | 173776.4 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 259962.6 ms | 254266.4 ms | 5696.2 ms | 178974.9 ms |
| Aws_restjson | LLGoNoLTO | 257119.6 ms | 251181.1 ms | 5938.6 ms | 80275.9 ms |
| Aws_restjson | LLGoDeadcodeDrop | 252093.6 ms | 245691.4 ms | 6402.3 ms | 80630.7 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 251429.5 ms | 245529.9 ms | 5899.6 ms | 173670.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 251093.3 ms | 245455.5 ms | 5637.8 ms | 172179.3 ms |
| Etcdctl | LLGoNoLTO | 248687.0 ms | 238607.1 ms | 10079.9 ms | 84951.7 ms |
| Etcdctl | LLGoDeadcodeDrop | 248020.3 ms | 237101.5 ms | 10918.7 ms | 85703.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 239238.3 ms | 233707.9 ms | 5530.4 ms | 156673.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 235316.2 ms | 229655.3 ms | 5660.9 ms | 152806.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 216989.8 ms | 211554.7 ms | 5435.1 ms | 138693.4 ms |
| Uber_zap | LLGoNoLTO | 213381.0 ms | 208412.8 ms | 4968.3 ms | 67967.0 ms |
| Uber_zap | LLGoDeadcodeDrop | 213280.5 ms | 207944.3 ms | 5336.2 ms | 68884.1 ms |
| K8s_workqueue | LLGoNoLTO | 203486.4 ms | 198473.1 ms | 5013.2 ms | 64917.0 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 203396.6 ms | 197890.7 ms | 5505.9 ms | 66425.8 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 151691.2 ms | 147797.8 ms | 3893.5 ms | 103087.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 150264.2 ms | 146474.3 ms | 3789.9 ms | 101233.3 ms |
| XGo | LLGoDeadcodeDrop | 141567.3 ms | 134025.0 ms | 7542.3 ms | 51053.7 ms |
| XGo | LLGoNoLTO | 141164.8 ms | 134875.9 ms | 6288.9 ms | 51503.0 ms |
| Toml | LLGoFullLTONoGlobalDCE | 141138.5 ms | 137579.0 ms | 3559.5 ms | 94953.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 127262.5 ms | 123615.5 ms | 3647.0 ms | 78134.9 ms |
| Toml | LLGoFullLTOGlobalDCE | 125176.2 ms | 121574.1 ms | 3602.2 ms | 78465.5 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 125075.8 ms | 121533.1 ms | 3542.7 ms | 78013.4 ms |
| Gorm_schema | LLGoDeadcodeDrop | 118728.6 ms | 115189.2 ms | 3539.4 ms | 41241.1 ms |
| Gorm_schema | LLGoNoLTO | 117922.5 ms | 114713.1 ms | 3209.4 ms | 40361.1 ms |
| Toml | LLGoDeadcodeDrop | 111028.1 ms | 107874.6 ms | 3153.5 ms | 38087.6 ms |
| Toml | LLGoNoLTO | 110335.3 ms | 107398.5 ms | 2936.8 ms | 37518.9 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 99594.4 ms | 97165.9 ms | 2428.5 ms | 70089.2 ms |
| IXGo | Go | 98088.1 ms | 82984.3 ms | 15103.8 ms | 27144.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 80872.0 ms | 78499.8 ms | 2372.2 ms | 50836.5 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 79962.7 ms | 77568.1 ms | 2394.6 ms | 50187.0 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 75886.7 ms | 73766.6 ms | 2120.1 ms | 28139.0 ms |
| Dustin_humanize | LLGoNoLTO | 75126.4 ms | 73106.7 ms | 2019.7 ms | 27694.6 ms |
| Etcdctl | Go | 38011.3 ms | 32723.4 ms | 5287.9 ms | 11420.5 ms |
| XGo | Go | 21776.5 ms | 18663.0 ms | 3113.5 ms | 6400.4 ms |
| Aws_restjson | Go | 9058.8 ms | 7532.4 ms | 1526.3 ms | 3674.3 ms |
| Gorm_schema | Go | 6525.3 ms | 5595.7 ms | 929.6 ms | 2567.6 ms |
| Uber_zap | Go | 6052.8 ms | 5167.5 ms | 885.2 ms | 2621.2 ms |
| K8s_workqueue | Go | 5296.9 ms | 4363.6 ms | 933.3 ms | 2091.6 ms |
| Toml | Go | 2276.4 ms | 1856.6 ms | 419.8 ms | 1063.1 ms |
| Dustin_humanize | Go | 895.7 ms | 669.4 ms | 226.3 ms | 438.2 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2780190.9 ms | 1912451.6 ms | 9 |
| LLGoFullLTOGlobalDCE | 2661229.8 ms | 1780695.4 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2626425.1 ms | 1737548.0 ms | 9 |
| LLGoDeadcodeDrop | 1872684.1 ms | 623924.6 ms | 9 |
| LLGoNoLTO | 1852593.6 ms | 607319.9 ms | 9 |
| Go | 187981.8 ms | 57421.6 ms | 9 |

Dependency download details are in `download-timings.log`.
