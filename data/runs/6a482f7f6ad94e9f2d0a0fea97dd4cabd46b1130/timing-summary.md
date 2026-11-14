## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 715106.4 ms | 691396.0 ms | 23710.4 ms | 470046.6 ms |
| IXGo | LLGoFullLTOGlobalDCE | 693062.3 ms | 669128.1 ms | 23934.2 ms | 457804.1 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 671954.0 ms | 648044.3 ms | 23909.7 ms | 450024.2 ms |
| IXGo | LLGoDeadcodeDrop | 400484.8 ms | 377072.9 ms | 23411.9 ms | 130423.9 ms |
| IXGo | LLGoNoLTO | 380721.2 ms | 360718.6 ms | 20002.7 ms | 119913.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 372766.6 ms | 361491.7 ms | 11274.9 ms | 277704.8 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 368914.4 ms | 357780.3 ms | 11134.1 ms | 276366.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 368770.8 ms | 357329.2 ms | 11441.7 ms | 274203.9 ms |
| XGo | LLGoFullLTONoGlobalDCE | 275404.2 ms | 267481.4 ms | 7922.8 ms | 223348.1 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 274046.9 ms | 267084.9 ms | 6962.0 ms | 188158.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 262279.2 ms | 255560.7 ms | 6718.5 ms | 169852.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 257887.2 ms | 251126.9 ms | 6760.3 ms | 165154.5 ms |
| XGo | LLGoFullLTOGlobalDCE | 245288.7 ms | 237623.2 ms | 7665.5 ms | 192677.9 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 244908.6 ms | 237303.1 ms | 7605.5 ms | 192294.3 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 231636.8 ms | 225765.3 ms | 5871.5 ms | 164784.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 226514.3 ms | 220697.3 ms | 5817.0 ms | 161517.3 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 224602.3 ms | 218676.8 ms | 5925.5 ms | 160526.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 216443.7 ms | 210680.0 ms | 5763.7 ms | 148044.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 211231.0 ms | 205370.5 ms | 5860.5 ms | 143388.0 ms |
| Aws_restjson | LLGoNoLTO | 199281.0 ms | 193978.8 ms | 5302.1 ms | 62619.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 197053.4 ms | 191394.4 ms | 5659.0 ms | 132870.9 ms |
| Aws_restjson | LLGoDeadcodeDrop | 188865.9 ms | 183327.8 ms | 5538.1 ms | 61756.9 ms |
| Etcdctl | LLGoDeadcodeDrop | 184614.5 ms | 175166.3 ms | 9448.2 ms | 65530.5 ms |
| Etcdctl | LLGoNoLTO | 183543.5 ms | 174923.2 ms | 8620.3 ms | 64310.6 ms |
| Uber_zap | LLGoNoLTO | 156304.9 ms | 151828.6 ms | 4476.3 ms | 51097.8 ms |
| Uber_zap | LLGoDeadcodeDrop | 155500.0 ms | 150955.3 ms | 4544.8 ms | 51725.6 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 149870.2 ms | 145005.2 ms | 4865.1 ms | 50634.9 ms |
| K8s_workqueue | LLGoNoLTO | 148052.9 ms | 143704.6 ms | 4348.3 ms | 48271.4 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 119002.3 ms | 115441.4 ms | 3561.0 ms | 83526.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 118392.2 ms | 114857.1 ms | 3535.1 ms | 81737.8 ms |
| Toml | LLGoFullLTONoGlobalDCE | 110852.7 ms | 107437.8 ms | 3414.9 ms | 76448.4 ms |
| XGo | LLGoNoLTO | 103292.1 ms | 97669.0 ms | 5623.1 ms | 38990.5 ms |
| XGo | LLGoDeadcodeDrop | 103169.9 ms | 96783.3 ms | 6386.6 ms | 38698.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 99064.7 ms | 95628.0 ms | 3436.7 ms | 62790.5 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 97762.8 ms | 94634.4 ms | 3128.4 ms | 63029.1 ms |
| Toml | LLGoFullLTOGlobalDCE | 97470.9 ms | 94347.2 ms | 3123.7 ms | 62815.4 ms |
| Gorm_schema | LLGoDeadcodeDrop | 86212.5 ms | 82895.8 ms | 3316.7 ms | 30796.9 ms |
| Gorm_schema | LLGoNoLTO | 84084.3 ms | 81121.0 ms | 2963.3 ms | 29648.0 ms |
| Toml | LLGoDeadcodeDrop | 80484.5 ms | 77632.4 ms | 2852.2 ms | 28335.5 ms |
| Toml | LLGoNoLTO | 79705.4 ms | 77018.3 ms | 2687.1 ms | 28178.1 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 78355.9 ms | 76097.0 ms | 2258.9 ms | 56546.8 ms |
| IXGo | Go | 73936.5 ms | 61041.9 ms | 12894.6 ms | 20389.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 62541.1 ms | 60486.5 ms | 2054.6 ms | 40554.9 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 62421.7 ms | 60320.8 ms | 2100.9 ms | 40604.2 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 54831.2 ms | 52890.0 ms | 1941.2 ms | 21056.3 ms |
| Dustin_humanize | LLGoNoLTO | 54609.6 ms | 52694.7 ms | 1914.9 ms | 20856.4 ms |
| Etcdctl | Go | 29351.4 ms | 24682.8 ms | 4668.6 ms | 8935.3 ms |
| XGo | Go | 16960.3 ms | 14242.3 ms | 2718.0 ms | 5407.4 ms |
| Aws_restjson | Go | 7372.1 ms | 5973.3 ms | 1398.8 ms | 4015.8 ms |
| Gorm_schema | Go | 5077.7 ms | 4228.8 ms | 848.9 ms | 2114.0 ms |
| Uber_zap | Go | 4620.1 ms | 3849.3 ms | 770.8 ms | 1895.9 ms |
| K8s_workqueue | Go | 4099.1 ms | 3359.8 ms | 739.3 ms | 1494.9 ms |
| Toml | Go | 1766.2 ms | 1414.3 ms | 352.0 ms | 856.2 ms |
| Dustin_humanize | Go | 727.8 ms | 532.1 ms | 195.7 ms | 365.1 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2354769.7 ms | 1679728.8 ms | 9 |
| LLGoFullLTOGlobalDCE | 2290763.0 ms | 1589208.4 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2258202.4 ms | 1547882.9 ms | 9 |
| LLGoDeadcodeDrop | 1404033.6 ms | 478958.9 ms | 9 |
| LLGoNoLTO | 1389594.9 ms | 463886.5 ms | 9 |
| Go | 143911.1 ms | 45474.0 ms | 9 |

Dependency download details are in `download-timings.log`.
