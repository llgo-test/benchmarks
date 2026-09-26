## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 559975.7 ms | 549695.6 ms | 10280.1 ms | 298002.8 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 536121.0 ms | 525313.1 ms | 10807.9 ms | 277358.2 ms |
| IXGo | LLGoFullLTOGlobalDCE | 444471.0 ms | 434149.8 ms | 10321.2 ms | 240622.2 ms |
| IXGo | LLGoNoLTO | 345444.9 ms | 337359.8 ms | 8085.1 ms | 104743.5 ms |
| IXGo | LLGoDeadcodeDrop | 336713.2 ms | 328036.2 ms | 8677.0 ms | 100809.6 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 200304.8 ms | 196212.5 ms | 4092.3 ms | 126288.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 195135.2 ms | 190941.4 ms | 4193.9 ms | 122703.0 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 195102.0 ms | 191279.5 ms | 3822.5 ms | 123857.2 ms |
| XGo | LLGoFullLTONoGlobalDCE | 146879.0 ms | 143969.2 ms | 2909.9 ms | 104939.7 ms |
| Etcdctl | LLGoDeadcodeDrop | 144495.3 ms | 141017.1 ms | 3478.3 ms | 48813.3 ms |
| XGo | LLGoFullLTOGlobalDCE | 143509.1 ms | 140728.7 ms | 2780.4 ms | 101602.2 ms |
| Etcdctl | LLGoNoLTO | 141207.5 ms | 137670.2 ms | 3537.3 ms | 47611.7 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 138788.7 ms | 136044.0 ms | 2744.7 ms | 97732.0 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 111197.4 ms | 109051.0 ms | 2146.4 ms | 83653.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 98007.6 ms | 95965.2 ms | 2042.4 ms | 69338.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 96329.3 ms | 94316.8 ms | 2012.5 ms | 68372.4 ms |
| XGo | LLGoDeadcodeDrop | 84067.2 ms | 81676.2 ms | 2391.0 ms | 32167.1 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 83214.2 ms | 81765.4 ms | 1448.8 ms | 64256.9 ms |
| XGo | LLGoNoLTO | 82089.7 ms | 79654.4 ms | 2435.4 ms | 31312.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 82043.5 ms | 80441.7 ms | 1601.9 ms | 61385.9 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 76480.4 ms | 74887.9 ms | 1592.5 ms | 56290.2 ms |
| Aws_restjson | LLGoDeadcodeDrop | 63932.9 ms | 62184.9 ms | 1748.0 ms | 30396.1 ms |
| Aws_restjson | LLGoNoLTO | 62166.2 ms | 60460.7 ms | 1705.5 ms | 29548.8 ms |
| IXGo | Go | 62154.6 ms | 57999.4 ms | 4155.1 ms | 17053.1 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 48074.7 ms | 46945.6 ms | 1129.1 ms | 33503.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 47370.1 ms | 46114.6 ms | 1255.4 ms | 32530.9 ms |
| Uber_zap | LLGoDeadcodeDrop | 44891.1 ms | 43538.8 ms | 1352.3 ms | 20371.6 ms |
| Uber_zap | LLGoNoLTO | 42621.1 ms | 41425.6 ms | 1195.5 ms | 19065.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 39394.4 ms | 38209.0 ms | 1185.3 ms | 24612.7 ms |
| Toml | LLGoFullLTONoGlobalDCE | 36885.3 ms | 36027.3 ms | 857.9 ms | 28262.6 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 31818.1 ms | 30906.5 ms | 911.6 ms | 22303.0 ms |
| Toml | LLGoFullLTOGlobalDCE | 31051.3 ms | 30194.6 ms | 856.7 ms | 22200.5 ms |
| Gorm_schema | LLGoDeadcodeDrop | 29423.1 ms | 28424.6 ms | 998.5 ms | 10144.4 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 29312.8 ms | 28522.4 ms | 790.4 ms | 23410.9 ms |
| Gorm_schema | LLGoNoLTO | 28830.1 ms | 27812.4 ms | 1017.7 ms | 10884.9 ms |
| Etcdctl | Go | 26964.0 ms | 25126.2 ms | 1837.8 ms | 8319.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 19780.5 ms | 19098.1 ms | 682.3 ms | 14282.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 19695.6 ms | 19004.6 ms | 691.0 ms | 14027.7 ms |
| Toml | LLGoNoLTO | 18590.9 ms | 17742.0 ms | 848.9 ms | 7573.1 ms |
| Toml | LLGoDeadcodeDrop | 17985.9 ms | 17211.7 ms | 774.2 ms | 6874.7 ms |
| XGo | Go | 14338.4 ms | 13359.9 ms | 978.6 ms | 4259.3 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 10707.4 ms | 10005.9 ms | 701.5 ms | 4655.7 ms |
| Dustin_humanize | LLGoNoLTO | 10477.1 ms | 9877.7 ms | 599.4 ms | 4509.8 ms |
| Aws_restjson | Go | 6620.3 ms | 5893.5 ms | 726.9 ms | 3740.1 ms |
| Gorm_schema | Go | 4294.8 ms | 3991.1 ms | 303.7 ms | 1663.0 ms |
| Uber_zap | Go | 3993.8 ms | 3641.8 ms | 352.0 ms | 1570.7 ms |
| K8s_workqueue | Go | 3796.7 ms | 3389.3 ms | 407.4 ms | 1456.8 ms |
| Toml | Go | 1536.0 ms | 1336.6 ms | 199.4 ms | 705.9 ms |
| Dustin_humanize | Go | 621.5 ms | 491.3 ms | 130.3 ms | 296.3 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1186786.5 ms | 739243.1 ms | 8 |
| LLGoFullLTOGlobalDCEPlugin | 1170113.3 ms | 713945.5 ms | 8 |
| LLGoFullLTOGlobalDCE | 1054042.0 ms | 658349.2 ms | 8 |
| LLGoDeadcodeDrop | 732216.0 ms | 254232.4 ms | 8 |
| LLGoNoLTO | 731427.6 ms | 255249.6 ms | 8 |
| Go | 124320.2 ms | 39064.3 ms | 9 |

Dependency download details are in `download-timings.log`.
