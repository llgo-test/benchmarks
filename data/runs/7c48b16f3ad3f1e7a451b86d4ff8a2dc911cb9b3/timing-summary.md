## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 836722.9 ms | 823853.3 ms | 12869.5 ms | 518716.2 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 818672.2 ms | 807400.3 ms | 11271.8 ms | 506008.7 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 767689.8 ms | 756690.3 ms | 10999.4 ms | 483397.9 ms |
| IXGo | LLGoDeadcodeDrop | 546238.7 ms | 533997.4 ms | 12241.3 ms | 182699.8 ms |
| IXGo | LLGoNoLTO | 521626.4 ms | 512560.6 ms | 9065.8 ms | 170476.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 377471.6 ms | 371728.2 ms | 5743.5 ms | 287059.5 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 365948.2 ms | 359881.8 ms | 6066.4 ms | 279152.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 338695.5 ms | 333368.5 ms | 5327.1 ms | 256826.7 ms |
| XGo | LLGoFullLTONoGlobalDCE | 272734.4 ms | 268697.7 ms | 4036.7 ms | 225281.1 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 267342.6 ms | 263557.5 ms | 3785.1 ms | 191133.3 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 253535.9 ms | 249837.1 ms | 3698.8 ms | 166374.1 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 252199.1 ms | 248347.5 ms | 3851.6 ms | 170910.8 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 248083.3 ms | 244258.9 ms | 3824.5 ms | 196614.1 ms |
| XGo | LLGoFullLTOGlobalDCE | 247025.7 ms | 243097.8 ms | 3927.9 ms | 201506.3 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 232680.6 ms | 229332.2 ms | 3348.3 ms | 174510.6 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 227696.0 ms | 224188.9 ms | 3507.2 ms | 171665.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 223185.9 ms | 219820.4 ms | 3365.5 ms | 167123.2 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 206399.4 ms | 203113.5 ms | 3285.9 ms | 148773.1 ms |
| Aws_restjson | LLGoNoLTO | 205984.9 ms | 203075.3 ms | 2909.6 ms | 70885.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 201165.3 ms | 198012.4 ms | 3152.9 ms | 143985.3 ms |
| Aws_restjson | LLGoDeadcodeDrop | 198697.5 ms | 195395.6 ms | 3301.9 ms | 71648.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 182649.6 ms | 179567.3 ms | 3082.3 ms | 129484.1 ms |
| Etcdctl | LLGoDeadcodeDrop | 176212.1 ms | 171447.8 ms | 4764.3 ms | 68556.7 ms |
| Etcdctl | LLGoNoLTO | 176041.0 ms | 171784.3 ms | 4256.6 ms | 63738.1 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 155710.8 ms | 152651.1 ms | 3059.7 ms | 62262.5 ms |
| Uber_zap | LLGoNoLTO | 154497.6 ms | 151858.2 ms | 2639.4 ms | 59902.5 ms |
| Uber_zap | LLGoDeadcodeDrop | 150896.6 ms | 148121.6 ms | 2775.0 ms | 58796.3 ms |
| K8s_workqueue | LLGoNoLTO | 148660.5 ms | 145960.1 ms | 2700.4 ms | 57583.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 116077.1 ms | 113946.6 ms | 2130.4 ms | 83848.0 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 115922.6 ms | 113868.3 ms | 2054.2 ms | 85590.9 ms |
| Toml | LLGoFullLTONoGlobalDCE | 109467.7 ms | 107209.0 ms | 2258.7 ms | 79684.2 ms |
| XGo | LLGoNoLTO | 102939.5 ms | 100197.1 ms | 2742.3 ms | 41821.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 101859.8 ms | 99832.5 ms | 2027.2 ms | 67765.3 ms |
| XGo | LLGoDeadcodeDrop | 98690.1 ms | 95402.8 ms | 3287.3 ms | 40402.0 ms |
| Toml | LLGoFullLTOGlobalDCE | 93899.2 ms | 91813.3 ms | 2085.8 ms | 63081.2 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 91672.7 ms | 89665.8 ms | 2006.8 ms | 61310.9 ms |
| Gorm_schema | LLGoDeadcodeDrop | 83380.6 ms | 81443.6 ms | 1936.9 ms | 29563.3 ms |
| Gorm_schema | LLGoNoLTO | 80430.8 ms | 78733.3 ms | 1697.5 ms | 27890.1 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 77151.7 ms | 75584.7 ms | 1567.1 ms | 58309.3 ms |
| Toml | LLGoNoLTO | 76119.2 ms | 74316.2 ms | 1803.0 ms | 26130.8 ms |
| Toml | LLGoDeadcodeDrop | 74588.2 ms | 72653.4 ms | 1934.9 ms | 25936.2 ms |
| IXGo | Go | 63684.3 ms | 59229.5 ms | 4454.8 ms | 20150.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 60784.3 ms | 59338.3 ms | 1446.0 ms | 41460.9 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 58682.9 ms | 57338.8 ms | 1344.1 ms | 39960.7 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 52046.8 ms | 50665.7 ms | 1381.0 ms | 19970.0 ms |
| Dustin_humanize | LLGoNoLTO | 51747.9 ms | 50489.2 ms | 1258.6 ms | 19361.5 ms |
| Etcdctl | Go | 25834.7 ms | 24016.1 ms | 1818.6 ms | 11336.9 ms |
| XGo | Go | 14643.8 ms | 13639.2 ms | 1004.6 ms | 4401.3 ms |
| Aws_restjson | Go | 6224.3 ms | 5650.1 ms | 574.1 ms | 4946.4 ms |
| Gorm_schema | Go | 4507.2 ms | 4167.8 ms | 339.4 ms | 2113.3 ms |
| Uber_zap | Go | 4086.7 ms | 3770.0 ms | 316.7 ms | 1626.6 ms |
| K8s_workqueue | Go | 3626.8 ms | 3266.7 ms | 360.1 ms | 1353.0 ms |
| Toml | Go | 1518.8 ms | 1314.7 ms | 204.1 ms | 750.6 ms |
| Dustin_humanize | Go | 603.6 ms | 489.0 ms | 114.6 ms | 532.2 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2436633.7 ms | 1748724.6 ms | 9 |
| LLGoFullLTOGlobalDCE | 2368990.3 ms | 1641421.8 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2339792.0 ms | 1609387.2 ms | 9 |
| LLGoDeadcodeDrop | 1536461.4 ms | 559835.5 ms | 9 |
| LLGoNoLTO | 1518047.7 ms | 537790.5 ms | 9 |
| Go | 124730.3 ms | 47210.8 ms | 9 |

Dependency download details are in `download-timings.log`.
