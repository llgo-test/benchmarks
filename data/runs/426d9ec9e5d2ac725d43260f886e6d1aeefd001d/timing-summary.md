## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 465490.4 ms | 456082.2 ms | 9408.1 ms | 251662.1 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 449296.3 ms | 439718.6 ms | 9577.8 ms | 243266.4 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 417892.7 ms | 408489.4 ms | 9403.3 ms | 213951.8 ms |
| IXGo | LLGoNoLTO | 386783.3 ms | 379290.4 ms | 7492.9 ms | 126911.5 ms |
| IXGo | LLGoDeadcodeDrop | 281180.8 ms | 273860.2 ms | 7320.6 ms | 84988.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 181848.9 ms | 178363.4 ms | 3485.5 ms | 116750.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 179897.4 ms | 175737.4 ms | 4160.0 ms | 113691.3 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 170176.1 ms | 166562.5 ms | 3613.6 ms | 106643.3 ms |
| Etcdctl | LLGoDeadcodeDrop | 134463.8 ms | 130899.6 ms | 3564.2 ms | 44881.1 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 128249.1 ms | 125678.7 ms | 2570.4 ms | 90406.6 ms |
| Etcdctl | LLGoNoLTO | 125519.5 ms | 122425.3 ms | 3094.2 ms | 42317.4 ms |
| XGo | LLGoFullLTOGlobalDCE | 119248.2 ms | 116946.7 ms | 2301.5 ms | 84686.5 ms |
| XGo | LLGoFullLTONoGlobalDCE | 116846.6 ms | 114501.9 ms | 2344.7 ms | 82534.4 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 97898.7 ms | 96167.0 ms | 1731.7 ms | 73892.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 90317.6 ms | 88519.2 ms | 1798.4 ms | 63999.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 80866.2 ms | 79040.7 ms | 1825.5 ms | 57725.3 ms |
| XGo | LLGoDeadcodeDrop | 75023.5 ms | 72880.6 ms | 2142.9 ms | 28508.0 ms |
| XGo | LLGoNoLTO | 74178.5 ms | 71945.6 ms | 2232.9 ms | 28675.3 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 70714.5 ms | 69425.9 ms | 1288.6 ms | 54222.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 68689.7 ms | 67109.7 ms | 1580.0 ms | 54235.8 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 68536.6 ms | 67267.0 ms | 1269.6 ms | 54126.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 66114.7 ms | 64794.1 ms | 1320.7 ms | 48906.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 65431.7 ms | 64152.6 ms | 1279.1 ms | 48020.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 64197.2 ms | 62790.6 ms | 1406.6 ms | 47973.0 ms |
| Aws_restjson | LLGoNoLTO | 55123.8 ms | 53601.2 ms | 1522.7 ms | 27672.8 ms |
| Aws_restjson | LLGoDeadcodeDrop | 54408.1 ms | 52863.8 ms | 1544.4 ms | 26279.3 ms |
| IXGo | Go | 51616.3 ms | 47712.0 ms | 3904.2 ms | 15097.7 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 40276.3 ms | 39303.7 ms | 972.6 ms | 27922.5 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 40150.0 ms | 39164.2 ms | 985.8 ms | 28269.8 ms |
| Uber_zap | LLGoNoLTO | 40125.7 ms | 38927.7 ms | 1198.0 ms | 17903.9 ms |
| Uber_zap | LLGoDeadcodeDrop | 37100.9 ms | 36025.9 ms | 1075.0 ms | 16490.7 ms |
| K8s_workqueue | LLGoNoLTO | 33863.3 ms | 32712.3 ms | 1151.0 ms | 16346.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 33540.1 ms | 32532.5 ms | 1007.6 ms | 21192.7 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 32458.4 ms | 31260.0 ms | 1198.3 ms | 15990.6 ms |
| Toml | LLGoFullLTONoGlobalDCE | 32024.1 ms | 31208.5 ms | 815.7 ms | 24404.9 ms |
| Toml | LLGoFullLTOGlobalDCE | 29324.1 ms | 28417.9 ms | 906.2 ms | 21050.0 ms |
| Gorm_schema | LLGoDeadcodeDrop | 27201.6 ms | 26244.5 ms | 957.1 ms | 9386.8 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 26594.6 ms | 25778.4 ms | 816.2 ms | 18837.2 ms |
| Gorm_schema | LLGoNoLTO | 26184.7 ms | 25233.0 ms | 951.7 ms | 9141.3 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 22675.8 ms | 22023.5 ms | 652.3 ms | 17829.8 ms |
| Etcdctl | Go | 21883.1 ms | 20372.3 ms | 1510.8 ms | 6644.9 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 17611.7 ms | 17016.2 ms | 595.6 ms | 12722.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 16792.6 ms | 16194.7 ms | 597.9 ms | 11967.2 ms |
| Toml | LLGoDeadcodeDrop | 16316.3 ms | 15552.8 ms | 763.4 ms | 6415.8 ms |
| Toml | LLGoNoLTO | 15872.9 ms | 15182.1 ms | 690.8 ms | 6062.0 ms |
| XGo | Go | 12301.2 ms | 11341.2 ms | 960.0 ms | 3980.7 ms |
| Dustin_humanize | LLGoNoLTO | 9447.0 ms | 8846.5 ms | 600.5 ms | 4209.0 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 9415.2 ms | 8804.1 ms | 611.0 ms | 4361.8 ms |
| Aws_restjson | Go | 4791.2 ms | 4331.9 ms | 459.2 ms | 1956.8 ms |
| Gorm_schema | Go | 3904.0 ms | 3555.7 ms | 348.3 ms | 1806.6 ms |
| Uber_zap | Go | 3154.4 ms | 2849.6 ms | 304.8 ms | 1244.3 ms |
| K8s_workqueue | Go | 3121.6 ms | 2796.4 ms | 325.3 ms | 1141.0 ms |
| Toml | Go | 1468.2 ms | 1306.7 ms | 161.5 ms | 693.3 ms |
| Dustin_humanize | Go | 509.2 ms | 404.9 ms | 104.4 ms | 253.3 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1068318.8 ms | 685189.3 ms | 9 |
| LLGoFullLTOGlobalDCE | 1067968.1 ms | 674020.5 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1024415.2 ms | 631681.0 ms | 9 |
| LLGoNoLTO | 767098.8 ms | 279239.7 ms | 9 |
| LLGoDeadcodeDrop | 667568.6 ms | 237302.2 ms | 9 |
| Go | 102749.0 ms | 32818.5 ms | 9 |

Dependency download details are in `download-timings.log`.
