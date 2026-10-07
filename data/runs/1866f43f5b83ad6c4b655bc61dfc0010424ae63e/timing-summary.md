## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 627164.6 ms | 616288.3 ms | 10876.3 ms | 326540.7 ms |
| IXGo | LLGoFullLTOGlobalDCE | 624574.3 ms | 614620.9 ms | 9953.5 ms | 324646.1 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 610907.4 ms | 601355.3 ms | 9552.0 ms | 321358.8 ms |
| IXGo | LLGoDeadcodeDrop | 504374.6 ms | 490291.0 ms | 14083.5 ms | 151014.3 ms |
| IXGo | LLGoNoLTO | 487790.2 ms | 479141.8 ms | 8648.4 ms | 143421.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 333110.7 ms | 328176.1 ms | 4934.6 ms | 193920.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 330701.5 ms | 325722.5 ms | 4979.0 ms | 192258.2 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 329596.2 ms | 324687.6 ms | 4908.6 ms | 193755.7 ms |
| K8s_workqueue | LLGoNoLTO | 273035.1 ms | 270098.3 ms | 2936.8 ms | 133128.0 ms |
| Aws_restjson | LLGoDeadcodeDrop | 260481.4 ms | 257260.6 ms | 3220.8 ms | 87220.0 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 260022.3 ms | 256229.0 ms | 3793.3 ms | 143909.2 ms |
| Aws_restjson | LLGoNoLTO | 258432.0 ms | 255314.1 ms | 3117.9 ms | 86259.8 ms |
| Etcdctl | LLGoDeadcodeDrop | 256781.4 ms | 251414.5 ms | 5366.8 ms | 85151.0 ms |
| Etcdctl | LLGoNoLTO | 254128.0 ms | 249809.2 ms | 4318.8 ms | 83189.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 246586.0 ms | 242831.8 ms | 3754.2 ms | 129358.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 246141.8 ms | 242358.3 ms | 3783.5 ms | 129155.2 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 237604.0 ms | 234274.0 ms | 3330.0 ms | 154614.0 ms |
| XGo | LLGoFullLTONoGlobalDCE | 236587.1 ms | 233332.8 ms | 3254.3 ms | 155018.4 ms |
| XGo | LLGoFullLTOGlobalDCE | 235997.5 ms | 232754.1 ms | 3243.5 ms | 153407.9 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 226419.7 ms | 223231.1 ms | 3188.6 ms | 129236.0 ms |
| Uber_zap | LLGoDeadcodeDrop | 225311.2 ms | 222364.9 ms | 2946.2 ms | 79227.9 ms |
| Uber_zap | LLGoNoLTO | 223538.2 ms | 220586.2 ms | 2952.0 ms | 78464.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 220008.2 ms | 216501.5 ms | 3506.7 ms | 125506.1 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 219576.7 ms | 216375.4 ms | 3201.3 ms | 125216.9 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 217851.3 ms | 214828.9 ms | 3022.5 ms | 76429.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 216264.3 ms | 212957.7 ms | 3306.6 ms | 116889.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 215383.4 ms | 212001.2 ms | 3382.2 ms | 116819.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 204643.4 ms | 201392.6 ms | 3250.8 ms | 109407.8 ms |
| XGo | LLGoDeadcodeDrop | 157995.9 ms | 154532.6 ms | 3463.2 ms | 57917.1 ms |
| XGo | LLGoNoLTO | 155630.4 ms | 152989.6 ms | 2640.8 ms | 56627.1 ms |
| Gorm_schema | LLGoDeadcodeDrop | 106873.3 ms | 105143.7 ms | 1729.7 ms | 35283.1 ms |
| Gorm_schema | LLGoNoLTO | 104686.2 ms | 102995.3 ms | 1690.9 ms | 34664.8 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 104641.0 ms | 102697.3 ms | 1943.7 ms | 60715.1 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 104459.7 ms | 102434.3 ms | 2025.4 ms | 59848.4 ms |
| Toml | LLGoDeadcodeDrop | 100064.5 ms | 98320.1 ms | 1744.4 ms | 32958.6 ms |
| Toml | LLGoNoLTO | 98964.0 ms | 97176.5 ms | 1787.5 ms | 32448.9 ms |
| Toml | LLGoFullLTONoGlobalDCE | 96671.8 ms | 94717.6 ms | 1954.3 ms | 55006.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 92594.0 ms | 90761.1 ms | 1832.9 ms | 47860.0 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 88328.2 ms | 86394.4 ms | 1933.7 ms | 45985.4 ms |
| Toml | LLGoFullLTOGlobalDCE | 88044.8 ms | 86082.7 ms | 1962.1 ms | 46176.1 ms |
| IXGo | Go | 82187.0 ms | 77334.3 ms | 4852.8 ms | 22597.8 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 70167.4 ms | 68985.1 ms | 1182.4 ms | 24927.2 ms |
| Dustin_humanize | LLGoNoLTO | 68881.0 ms | 67704.2 ms | 1176.8 ms | 24474.3 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 68856.8 ms | 67493.9 ms | 1363.0 ms | 41462.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 59338.3 ms | 58017.0 ms | 1321.3 ms | 31542.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 59336.2 ms | 58109.4 ms | 1226.8 ms | 31628.9 ms |
| Etcdctl | Go | 32969.6 ms | 31085.0 ms | 1884.6 ms | 9798.4 ms |
| XGo | Go | 18913.8 ms | 17654.8 ms | 1259.0 ms | 5891.4 ms |
| Aws_restjson | Go | 7791.0 ms | 7106.4 ms | 684.6 ms | 3134.9 ms |
| Gorm_schema | Go | 5696.9 ms | 5326.1 ms | 370.8 ms | 2210.5 ms |
| Uber_zap | Go | 5194.3 ms | 4781.9 ms | 412.3 ms | 2031.4 ms |
| K8s_workqueue | Go | 4624.8 ms | 4173.7 ms | 451.1 ms | 1627.1 ms |
| Toml | Go | 1989.6 ms | 1748.8 ms | 240.8 ms | 900.3 ms |
| Dustin_humanize | Go | 800.9 ms | 649.3 ms | 151.6 ms | 370.9 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2153279.1 ms | 1225678.7 ms | 9 |
| LLGoFullLTOGlobalDCE | 2124649.5 ms | 1179359.4 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2105631.4 ms | 1156205.0 ms | 9 |
| LLGoNoLTO | 1925085.0 ms | 672678.4 ms | 9 |
| LLGoDeadcodeDrop | 1899901.0 ms | 630128.4 ms | 9 |
| Go | 160167.9 ms | 48562.8 ms | 9 |

Dependency download details are in `download-timings.log`.
