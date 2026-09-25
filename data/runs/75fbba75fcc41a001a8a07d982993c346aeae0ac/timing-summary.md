## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 438602.9 ms | 427886.4 ms | 10716.5 ms | 235090.6 ms |
| IXGo | LLGoFullLTOGlobalDCE | 426361.2 ms | 416480.6 ms | 9880.6 ms | 234549.2 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 406439.2 ms | 396111.7 ms | 10327.5 ms | 226347.3 ms |
| IXGo | LLGoNoLTO | 350780.9 ms | 342065.4 ms | 8715.4 ms | 107752.9 ms |
| IXGo | LLGoDeadcodeDrop | 337456.5 ms | 328917.1 ms | 8539.5 ms | 105123.5 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 198453.2 ms | 194517.5 ms | 3935.7 ms | 127438.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 198365.6 ms | 194500.2 ms | 3865.4 ms | 124296.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 195744.5 ms | 191817.3 ms | 3927.2 ms | 125143.4 ms |
| Etcdctl | LLGoDeadcodeDrop | 148785.5 ms | 145121.3 ms | 3664.2 ms | 50707.3 ms |
| Etcdctl | LLGoNoLTO | 148295.0 ms | 144503.8 ms | 3791.1 ms | 52540.0 ms |
| XGo | LLGoFullLTONoGlobalDCE | 140810.6 ms | 138066.5 ms | 2744.1 ms | 100084.2 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 138672.1 ms | 135930.7 ms | 2741.4 ms | 97072.9 ms |
| XGo | LLGoFullLTOGlobalDCE | 137437.7 ms | 134783.0 ms | 2654.6 ms | 97118.3 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 104929.6 ms | 102993.3 ms | 1936.3 ms | 79258.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 100081.3 ms | 98086.8 ms | 1994.5 ms | 73487.1 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 95881.9 ms | 93943.7 ms | 1938.3 ms | 68036.4 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 89055.7 ms | 87512.4 ms | 1543.4 ms | 70401.1 ms |
| XGo | LLGoDeadcodeDrop | 82965.6 ms | 80613.8 ms | 2351.8 ms | 33178.6 ms |
| XGo | LLGoNoLTO | 81154.4 ms | 78785.1 ms | 2369.3 ms | 31224.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 77096.1 ms | 75589.8 ms | 1506.3 ms | 58247.2 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 75961.4 ms | 74454.1 ms | 1507.3 ms | 56289.6 ms |
| Aws_restjson | LLGoNoLTO | 62847.7 ms | 61169.4 ms | 1678.3 ms | 31049.6 ms |
| Aws_restjson | LLGoDeadcodeDrop | 62841.2 ms | 61263.3 ms | 1577.9 ms | 29751.4 ms |
| IXGo | Go | 61667.4 ms | 57491.0 ms | 4176.3 ms | 17212.1 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 48392.5 ms | 47169.4 ms | 1223.1 ms | 33739.1 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 47666.7 ms | 46512.2 ms | 1154.5 ms | 33182.4 ms |
| Uber_zap | LLGoNoLTO | 44330.6 ms | 43053.5 ms | 1277.1 ms | 20168.0 ms |
| Uber_zap | LLGoDeadcodeDrop | 44301.6 ms | 42942.2 ms | 1359.4 ms | 21929.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 39278.8 ms | 38185.0 ms | 1093.8 ms | 24518.0 ms |
| Toml | LLGoFullLTONoGlobalDCE | 36901.7 ms | 36039.2 ms | 862.5 ms | 28363.5 ms |
| Toml | LLGoFullLTOGlobalDCE | 33284.8 ms | 32307.7 ms | 977.2 ms | 24570.5 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 31337.0 ms | 30401.2 ms | 935.7 ms | 23054.3 ms |
| Gorm_schema | LLGoDeadcodeDrop | 30772.1 ms | 29701.9 ms | 1070.3 ms | 11745.6 ms |
| Gorm_schema | LLGoNoLTO | 28892.5 ms | 27919.0 ms | 973.4 ms | 9945.9 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 27670.8 ms | 26919.5 ms | 751.3 ms | 23009.4 ms |
| Etcdctl | Go | 25129.2 ms | 23429.0 ms | 1700.3 ms | 7562.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 19889.4 ms | 19160.0 ms | 729.4 ms | 14688.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 19548.7 ms | 18830.6 ms | 718.1 ms | 14122.7 ms |
| Toml | LLGoDeadcodeDrop | 18546.1 ms | 17711.1 ms | 835.0 ms | 7016.9 ms |
| Toml | LLGoNoLTO | 18252.3 ms | 17437.1 ms | 815.2 ms | 7719.6 ms |
| XGo | Go | 14170.9 ms | 13167.6 ms | 1003.2 ms | 5686.5 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 10323.3 ms | 9714.7 ms | 608.6 ms | 4659.2 ms |
| Dustin_humanize | LLGoNoLTO | 10270.5 ms | 9611.4 ms | 659.1 ms | 5257.5 ms |
| Aws_restjson | Go | 5920.7 ms | 5313.8 ms | 606.9 ms | 3480.2 ms |
| Gorm_schema | Go | 4368.4 ms | 4009.3 ms | 359.2 ms | 2549.7 ms |
| Uber_zap | Go | 3947.0 ms | 3636.5 ms | 310.5 ms | 1579.7 ms |
| K8s_workqueue | Go | 3568.9 ms | 3164.7 ms | 404.2 ms | 2055.3 ms |
| Toml | Go | 1449.0 ms | 1286.8 ms | 162.1 ms | 690.0 ms |
| Dustin_humanize | Go | 551.0 ms | 457.9 ms | 93.1 ms | 283.9 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1051927.5 ms | 688085.1 ms | 8 |
| LLGoFullLTOGlobalDCEPlugin | 1042188.5 ms | 648497.4 ms | 8 |
| LLGoFullLTOGlobalDCE | 1033747.5 ms | 655526.9 ms | 8 |
| LLGoNoLTO | 744823.8 ms | 265658.4 ms | 8 |
| LLGoDeadcodeDrop | 735992.0 ms | 264112.4 ms | 8 |
| Go | 120772.5 ms | 41099.5 ms | 9 |

Dependency download details are in `download-timings.log`.
