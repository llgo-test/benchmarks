## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 577005.1 ms | 563758.2 ms | 13246.9 ms | 300104.1 ms |
| IXGo | LLGoFullLTOGlobalDCE | 560156.2 ms | 546310.3 ms | 13845.9 ms | 293154.5 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 542109.0 ms | 526932.4 ms | 15176.6 ms | 283557.3 ms |
| IXGo | LLGoDeadcodeDrop | 423453.2 ms | 412267.5 ms | 11185.7 ms | 126448.6 ms |
| IXGo | LLGoNoLTO | 415904.7 ms | 404287.6 ms | 11617.0 ms | 128462.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 257381.2 ms | 251654.6 ms | 5726.5 ms | 161917.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 251195.1 ms | 246106.3 ms | 5088.8 ms | 157989.7 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 248277.3 ms | 243434.5 ms | 4842.8 ms | 156919.8 ms |
| Etcdctl | LLGoDeadcodeDrop | 186248.7 ms | 181553.5 ms | 4695.2 ms | 62913.7 ms |
| Etcdctl | LLGoNoLTO | 179876.9 ms | 175502.4 ms | 4374.5 ms | 61077.6 ms |
| XGo | LLGoFullLTONoGlobalDCE | 177678.7 ms | 174170.2 ms | 3508.5 ms | 125529.4 ms |
| XGo | LLGoFullLTOGlobalDCE | 177647.9 ms | 173507.1 ms | 4140.8 ms | 124570.8 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 176797.6 ms | 173177.1 ms | 3620.5 ms | 124027.0 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 138346.6 ms | 135550.7 ms | 2796.0 ms | 102659.3 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 126309.0 ms | 123559.9 ms | 2749.1 ms | 90575.3 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 124412.7 ms | 121704.3 ms | 2708.4 ms | 87770.6 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 109477.9 ms | 107413.3 ms | 2064.6 ms | 83886.6 ms |
| XGo | LLGoDeadcodeDrop | 108367.1 ms | 105237.1 ms | 3130.0 ms | 42427.8 ms |
| XGo | LLGoNoLTO | 105091.4 ms | 102023.5 ms | 3067.9 ms | 40326.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 102375.6 ms | 100201.4 ms | 2174.2 ms | 80176.1 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 100986.9 ms | 98968.9 ms | 2018.0 ms | 79512.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 98788.4 ms | 96935.5 ms | 1852.9 ms | 72899.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 98121.2 ms | 96161.0 ms | 1960.2 ms | 71951.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 89606.4 ms | 87538.7 ms | 2067.7 ms | 67333.5 ms |
| Aws_restjson | LLGoDeadcodeDrop | 82563.9 ms | 80213.4 ms | 2350.4 ms | 40147.2 ms |
| Aws_restjson | LLGoNoLTO | 81034.6 ms | 78792.5 ms | 2242.1 ms | 39040.8 ms |
| IXGo | Go | 79305.1 ms | 73859.3 ms | 5445.8 ms | 22528.0 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 61957.7 ms | 60366.9 ms | 1590.8 ms | 43229.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 60968.8 ms | 59376.3 ms | 1592.4 ms | 41924.7 ms |
| Uber_zap | LLGoDeadcodeDrop | 56793.0 ms | 55245.0 ms | 1548.0 ms | 26133.3 ms |
| Uber_zap | LLGoNoLTO | 55664.9 ms | 54079.4 ms | 1585.5 ms | 25737.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 51545.2 ms | 50036.8 ms | 1508.3 ms | 32015.1 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 48475.9 ms | 46765.7 ms | 1710.2 ms | 22824.1 ms |
| Toml | LLGoFullLTONoGlobalDCE | 48212.6 ms | 46988.9 ms | 1223.7 ms | 36908.6 ms |
| K8s_workqueue | LLGoNoLTO | 48138.1 ms | 46346.8 ms | 1791.3 ms | 23043.6 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 40209.1 ms | 39050.1 ms | 1159.0 ms | 28635.2 ms |
| Toml | LLGoFullLTOGlobalDCE | 40183.2 ms | 39005.6 ms | 1177.5 ms | 28680.6 ms |
| Gorm_schema | LLGoDeadcodeDrop | 37890.1 ms | 36499.4 ms | 1390.7 ms | 13001.3 ms |
| Gorm_schema | LLGoNoLTO | 36621.4 ms | 35342.6 ms | 1278.8 ms | 12506.1 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 33934.1 ms | 33011.7 ms | 922.4 ms | 26718.1 ms |
| Etcdctl | Go | 31930.1 ms | 29751.2 ms | 2178.9 ms | 9928.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 25543.1 ms | 24557.3 ms | 985.9 ms | 18155.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 25414.1 ms | 24500.6 ms | 913.5 ms | 18203.2 ms |
| Toml | LLGoDeadcodeDrop | 23619.9 ms | 22474.2 ms | 1145.7 ms | 9178.4 ms |
| Toml | LLGoNoLTO | 22642.8 ms | 21528.8 ms | 1114.0 ms | 8736.5 ms |
| XGo | Go | 18568.6 ms | 17195.4 ms | 1373.2 ms | 5677.6 ms |
| Dustin_humanize | LLGoNoLTO | 13333.5 ms | 12469.3 ms | 864.2 ms | 5771.3 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 12866.7 ms | 12035.1 ms | 831.5 ms | 5717.8 ms |
| Aws_restjson | Go | 7955.9 ms | 6983.4 ms | 972.6 ms | 3712.1 ms |
| Gorm_schema | Go | 5536.1 ms | 5109.9 ms | 426.2 ms | 2131.3 ms |
| Uber_zap | Go | 5368.6 ms | 4814.2 ms | 554.5 ms | 2328.6 ms |
| K8s_workqueue | Go | 4588.5 ms | 4066.8 ms | 521.7 ms | 1627.3 ms |
| Toml | Go | 1995.7 ms | 1746.3 ms | 249.3 ms | 916.8 ms |
| Dustin_humanize | Go | 815.5 ms | 655.4 ms | 160.1 ms | 400.5 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1460980.8 ms | 938920.9 ms | 9 |
| LLGoFullLTOGlobalDCE | 1443038.2 ms | 908174.5 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1440621.6 ms | 891910.4 ms | 9 |
| LLGoDeadcodeDrop | 980278.4 ms | 348792.2 ms | 9 |
| LLGoNoLTO | 958308.2 ms | 344703.5 ms | 9 |
| Go | 156064.1 ms | 49251.1 ms | 9 |

Dependency download details are in `download-timings.log`.
