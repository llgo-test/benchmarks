## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 617683.8 ms | 598435.5 ms | 19248.3 ms | 327008.1 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 592114.5 ms | 580041.6 ms | 12072.9 ms | 306059.6 ms |
| IXGo | LLGoFullLTOGlobalDCE | 574070.9 ms | 561390.0 ms | 12680.9 ms | 295625.2 ms |
| IXGo | LLGoDeadcodeDrop | 478191.8 ms | 466343.5 ms | 11848.3 ms | 141259.3 ms |
| IXGo | LLGoNoLTO | 457469.9 ms | 446747.5 ms | 10722.4 ms | 136167.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 260094.0 ms | 254165.9 ms | 5928.0 ms | 162287.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 253714.5 ms | 248543.4 ms | 5171.1 ms | 158558.3 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 250840.4 ms | 245716.7 ms | 5123.8 ms | 159182.6 ms |
| Etcdctl | LLGoDeadcodeDrop | 187308.0 ms | 182763.2 ms | 4544.8 ms | 62745.5 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 183081.0 ms | 179495.1 ms | 3585.9 ms | 129775.2 ms |
| Etcdctl | LLGoNoLTO | 181053.2 ms | 176633.2 ms | 4420.0 ms | 60624.3 ms |
| XGo | LLGoFullLTOGlobalDCE | 178601.8 ms | 174567.5 ms | 4034.3 ms | 125406.2 ms |
| XGo | LLGoFullLTONoGlobalDCE | 176916.0 ms | 173382.0 ms | 3534.0 ms | 124830.7 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 137360.9 ms | 134739.8 ms | 2621.1 ms | 102213.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 126082.8 ms | 123357.6 ms | 2725.2 ms | 89684.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 124541.7 ms | 121986.2 ms | 2555.5 ms | 88260.8 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 107615.9 ms | 105646.8 ms | 1969.1 ms | 83048.9 ms |
| XGo | LLGoDeadcodeDrop | 106547.1 ms | 103333.0 ms | 3214.1 ms | 40560.6 ms |
| XGo | LLGoNoLTO | 104366.0 ms | 101331.4 ms | 3034.5 ms | 39820.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 103491.7 ms | 101408.3 ms | 2083.4 ms | 81333.2 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 102020.1 ms | 100149.6 ms | 1870.5 ms | 80286.9 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 97653.6 ms | 95715.5 ms | 1938.1 ms | 72157.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 97568.0 ms | 95667.6 ms | 1900.4 ms | 71902.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 88207.2 ms | 86311.5 ms | 1895.7 ms | 66137.8 ms |
| Aws_restjson | LLGoNoLTO | 83872.6 ms | 81526.4 ms | 2346.1 ms | 41764.6 ms |
| Aws_restjson | LLGoDeadcodeDrop | 82257.0 ms | 79955.8 ms | 2301.2 ms | 39740.2 ms |
| IXGo | Go | 81232.2 ms | 75744.8 ms | 5487.4 ms | 23072.1 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 60928.6 ms | 59448.6 ms | 1480.1 ms | 41978.2 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 60566.2 ms | 59081.5 ms | 1484.7 ms | 42435.3 ms |
| Uber_zap | LLGoDeadcodeDrop | 56291.7 ms | 54608.4 ms | 1683.4 ms | 24890.8 ms |
| Uber_zap | LLGoNoLTO | 55306.6 ms | 53776.9 ms | 1529.7 ms | 24483.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 50680.7 ms | 49297.1 ms | 1383.7 ms | 31454.5 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 48221.4 ms | 46677.1 ms | 1544.3 ms | 22741.6 ms |
| Toml | LLGoFullLTONoGlobalDCE | 48183.6 ms | 47025.9 ms | 1157.7 ms | 36855.8 ms |
| K8s_workqueue | LLGoNoLTO | 47868.2 ms | 46176.8 ms | 1691.4 ms | 22517.6 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 41246.5 ms | 40036.1 ms | 1210.4 ms | 29141.7 ms |
| Toml | LLGoFullLTOGlobalDCE | 40811.7 ms | 39728.6 ms | 1083.1 ms | 29177.8 ms |
| Gorm_schema | LLGoDeadcodeDrop | 38100.3 ms | 36852.0 ms | 1248.3 ms | 12906.3 ms |
| Gorm_schema | LLGoNoLTO | 37578.0 ms | 36297.1 ms | 1280.9 ms | 12759.0 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 34157.8 ms | 33198.3 ms | 959.4 ms | 26975.7 ms |
| Etcdctl | Go | 32768.5 ms | 30575.4 ms | 2193.1 ms | 9950.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 25377.8 ms | 24500.4 ms | 877.4 ms | 18249.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 24850.4 ms | 24008.1 ms | 842.4 ms | 17903.4 ms |
| Toml | LLGoDeadcodeDrop | 23863.7 ms | 22807.5 ms | 1056.2 ms | 8987.5 ms |
| Toml | LLGoNoLTO | 22709.5 ms | 21690.0 ms | 1019.5 ms | 8629.7 ms |
| XGo | Go | 18895.3 ms | 17450.6 ms | 1444.6 ms | 5866.2 ms |
| Dustin_humanize | LLGoNoLTO | 13154.4 ms | 12384.1 ms | 770.3 ms | 5717.8 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 13006.0 ms | 12195.1 ms | 810.8 ms | 5712.8 ms |
| Aws_restjson | Go | 8060.9 ms | 7112.5 ms | 948.5 ms | 3965.0 ms |
| Gorm_schema | Go | 5656.3 ms | 5176.7 ms | 479.6 ms | 2236.6 ms |
| Uber_zap | Go | 5234.5 ms | 4774.4 ms | 460.0 ms | 2055.1 ms |
| K8s_workqueue | Go | 4585.6 ms | 4107.3 ms | 478.3 ms | 1630.8 ms |
| Toml | Go | 1990.3 ms | 1711.7 ms | 278.6 ms | 925.8 ms |
| Dustin_humanize | Go | 804.6 ms | 660.1 ms | 144.5 ms | 388.2 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1509775.4 ms | 961889.3 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1488039.0 ms | 924127.0 ms | 9 |
| LLGoFullLTOGlobalDCE | 1460647.8 ms | 911916.2 ms | 9 |
| LLGoDeadcodeDrop | 1033787.0 ms | 359544.6 ms | 9 |
| LLGoNoLTO | 1003378.3 ms | 352483.9 ms | 9 |
| Go | 159228.2 ms | 50090.4 ms | 9 |

Dependency download details are in `download-timings.log`.
