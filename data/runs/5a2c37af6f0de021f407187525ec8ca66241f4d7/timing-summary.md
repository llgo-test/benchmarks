## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 807697.0 ms | 800297.2 ms | 7399.7 ms | 616696.3 ms |
| IXGo | LLGoFullLTOGlobalDCE | 796985.5 ms | 790104.1 ms | 6881.4 ms | 595432.6 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 779504.6 ms | 772971.0 ms | 6533.6 ms | 595233.9 ms |
| IXGo | LLGoNoLTO | 378125.0 ms | 371982.1 ms | 6143.0 ms | 137003.0 ms |
| IXGo | LLGoDeadcodeDrop | 375176.3 ms | 368882.5 ms | 6293.9 ms | 134781.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 274058.6 ms | 268879.6 ms | 5178.9 ms | 169717.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 270438.8 ms | 265345.5 ms | 5093.3 ms | 168369.6 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 267276.9 ms | 262281.9 ms | 4995.0 ms | 166060.5 ms |
| Etcdctl | LLGoDeadcodeDrop | 194392.0 ms | 189928.1 ms | 4463.9 ms | 63319.0 ms |
| Etcdctl | LLGoNoLTO | 192461.2 ms | 187974.1 ms | 4487.2 ms | 62592.2 ms |
| XGo | LLGoFullLTOGlobalDCE | 183134.0 ms | 179918.6 ms | 3215.5 ms | 129309.3 ms |
| XGo | LLGoFullLTONoGlobalDCE | 182174.7 ms | 179042.6 ms | 3132.2 ms | 129971.6 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 180599.1 ms | 177311.1 ms | 3287.9 ms | 126992.1 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 144978.5 ms | 142425.7 ms | 2552.8 ms | 109102.1 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 129995.1 ms | 127686.9 ms | 2308.2 ms | 93314.1 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 127556.7 ms | 125281.9 ms | 2274.8 ms | 92515.4 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 110689.3 ms | 108889.3 ms | 1800.0 ms | 85291.1 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 107245.8 ms | 105459.4 ms | 1786.4 ms | 84328.5 ms |
| XGo | LLGoDeadcodeDrop | 105162.2 ms | 102418.3 ms | 2743.9 ms | 38385.8 ms |
| XGo | LLGoNoLTO | 103211.5 ms | 100393.9 ms | 2817.6 ms | 37427.0 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 103177.4 ms | 101470.9 ms | 1706.6 ms | 81469.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 100606.9 ms | 98836.5 ms | 1770.4 ms | 74309.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 99626.9 ms | 97836.7 ms | 1790.2 ms | 74506.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 91750.3 ms | 89961.9 ms | 1788.4 ms | 69056.9 ms |
| Aws_restjson | LLGoDeadcodeDrop | 82255.9 ms | 80205.0 ms | 2050.8 ms | 39205.7 ms |
| Aws_restjson | LLGoNoLTO | 81599.2 ms | 79582.9 ms | 2016.3 ms | 39105.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 65933.5 ms | 64538.6 ms | 1394.9 ms | 46121.1 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 63153.1 ms | 61853.1 ms | 1300.0 ms | 45013.8 ms |
| Uber_zap | LLGoDeadcodeDrop | 54148.9 ms | 52696.8 ms | 1452.0 ms | 22977.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 53806.4 ms | 52455.8 ms | 1350.6 ms | 34504.3 ms |
| Uber_zap | LLGoNoLTO | 53749.1 ms | 52284.6 ms | 1464.5 ms | 22927.3 ms |
| Toml | LLGoFullLTONoGlobalDCE | 52542.2 ms | 51472.7 ms | 1069.5 ms | 41069.6 ms |
| K8s_workqueue | LLGoNoLTO | 46572.8 ms | 45047.0 ms | 1525.8 ms | 20610.5 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 45485.1 ms | 44053.0 ms | 1432.1 ms | 20248.0 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 45292.6 ms | 44265.1 ms | 1027.4 ms | 33222.4 ms |
| Toml | LLGoFullLTOGlobalDCE | 44750.9 ms | 43734.0 ms | 1017.0 ms | 33028.0 ms |
| IXGo | Go | 42970.9 ms | 39703.8 ms | 3267.1 ms | 12540.4 ms |
| Gorm_schema | LLGoNoLTO | 36851.5 ms | 35658.1 ms | 1193.4 ms | 11896.3 ms |
| Gorm_schema | LLGoDeadcodeDrop | 36746.5 ms | 35551.1 ms | 1195.4 ms | 12091.4 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 33725.7 ms | 32924.6 ms | 801.1 ms | 26836.7 ms |
| Etcdctl | Go | 33075.2 ms | 30774.5 ms | 2300.7 ms | 9902.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 25038.7 ms | 24305.7 ms | 733.1 ms | 17943.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 24845.0 ms | 24101.0 ms | 744.0 ms | 17852.7 ms |
| Toml | LLGoDeadcodeDrop | 23518.8 ms | 22621.2 ms | 897.6 ms | 8829.3 ms |
| Toml | LLGoNoLTO | 22041.7 ms | 21132.1 ms | 909.6 ms | 8283.9 ms |
| XGo | Go | 18697.6 ms | 17408.3 ms | 1289.3 ms | 5447.4 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 12875.4 ms | 12143.3 ms | 732.1 ms | 5543.2 ms |
| Dustin_humanize | LLGoNoLTO | 12649.1 ms | 12001.5 ms | 647.6 ms | 5471.0 ms |
| Aws_restjson | Go | 7739.2 ms | 7090.2 ms | 648.9 ms | 3106.2 ms |
| Gorm_schema | Go | 5792.9 ms | 5352.5 ms | 440.4 ms | 2184.4 ms |
| Uber_zap | Go | 5398.0 ms | 4976.3 ms | 421.7 ms | 2087.6 ms |
| K8s_workqueue | Go | 4758.4 ms | 4307.8 ms | 450.5 ms | 1657.9 ms |
| Toml | Go | 2041.3 ms | 1809.4 ms | 231.9 ms | 920.6 ms |
| Dustin_humanize | Go | 751.3 ms | 629.4 ms | 121.9 ms | 368.4 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1737222.4 ms | 1280048.9 ms | 9 |
| LLGoFullLTOGlobalDCE | 1720711.0 ms | 1241555.1 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1708650.7 ms | 1235665.6 ms | 9 |
| LLGoDeadcodeDrop | 929761.0 ms | 345381.3 ms | 9 |
| LLGoNoLTO | 927261.3 ms | 345316.9 ms | 9 |
| Go | 121224.8 ms | 38215.5 ms | 9 |

Dependency download details are in `download-timings.log`.
