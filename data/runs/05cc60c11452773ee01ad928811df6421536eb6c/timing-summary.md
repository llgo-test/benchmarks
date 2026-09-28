## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 627634.2 ms | 605061.0 ms | 22573.2 ms | 345888.0 ms |
| IXGo | LLGoFullLTOGlobalDCE | 590056.4 ms | 573027.0 ms | 17029.3 ms | 312773.8 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 532291.2 ms | 519738.0 ms | 12553.3 ms | 279161.0 ms |
| IXGo | LLGoNoLTO | 449596.5 ms | 437901.9 ms | 11694.6 ms | 138370.0 ms |
| IXGo | LLGoDeadcodeDrop | 404673.2 ms | 393431.4 ms | 11241.8 ms | 121614.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 257793.8 ms | 252813.9 ms | 4979.9 ms | 161460.6 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 251304.7 ms | 245940.7 ms | 5364.0 ms | 158795.6 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 249256.9 ms | 244341.8 ms | 4915.1 ms | 157654.9 ms |
| Etcdctl | LLGoDeadcodeDrop | 184555.8 ms | 179989.7 ms | 4566.1 ms | 62245.5 ms |
| Etcdctl | LLGoNoLTO | 180493.2 ms | 176180.6 ms | 4312.5 ms | 60411.5 ms |
| XGo | LLGoFullLTONoGlobalDCE | 177073.8 ms | 173147.3 ms | 3926.5 ms | 124645.0 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 175306.6 ms | 171787.8 ms | 3518.7 ms | 122755.1 ms |
| XGo | LLGoFullLTOGlobalDCE | 174727.8 ms | 170955.3 ms | 3772.5 ms | 121934.9 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 138521.7 ms | 135550.4 ms | 2971.2 ms | 103026.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 126963.9 ms | 124254.6 ms | 2709.3 ms | 90333.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 122754.8 ms | 120225.6 ms | 2529.2 ms | 87147.5 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 109039.8 ms | 106987.8 ms | 2052.0 ms | 83445.4 ms |
| XGo | LLGoDeadcodeDrop | 106607.6 ms | 103361.1 ms | 3246.6 ms | 41025.3 ms |
| XGo | LLGoNoLTO | 103433.0 ms | 100437.7 ms | 2995.3 ms | 39577.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 100856.4 ms | 98814.6 ms | 2041.8 ms | 79213.3 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 100157.3 ms | 98334.2 ms | 1823.1 ms | 79029.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 99373.3 ms | 97390.9 ms | 1982.4 ms | 73313.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 98090.0 ms | 96155.6 ms | 1934.4 ms | 72304.8 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 90994.7 ms | 89083.9 ms | 1910.8 ms | 68757.7 ms |
| Aws_restjson | LLGoNoLTO | 84493.7 ms | 82150.0 ms | 2343.7 ms | 41253.0 ms |
| Aws_restjson | LLGoDeadcodeDrop | 83211.5 ms | 80933.2 ms | 2278.3 ms | 40123.5 ms |
| IXGo | Go | 79467.7 ms | 74178.4 ms | 5289.4 ms | 22378.1 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 60839.6 ms | 59340.5 ms | 1499.1 ms | 42683.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 60532.5 ms | 59000.7 ms | 1531.8 ms | 41687.3 ms |
| Uber_zap | LLGoDeadcodeDrop | 56607.9 ms | 54916.4 ms | 1691.5 ms | 25434.8 ms |
| Uber_zap | LLGoNoLTO | 54574.1 ms | 52986.4 ms | 1587.6 ms | 24425.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 51171.3 ms | 49686.6 ms | 1484.7 ms | 31853.1 ms |
| K8s_workqueue | LLGoNoLTO | 49529.9 ms | 47875.5 ms | 1654.4 ms | 24080.7 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 48266.4 ms | 46624.2 ms | 1642.2 ms | 22725.7 ms |
| Toml | LLGoFullLTONoGlobalDCE | 47902.2 ms | 46736.4 ms | 1165.8 ms | 36653.9 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 40819.5 ms | 39675.7 ms | 1143.8 ms | 28784.9 ms |
| Toml | LLGoFullLTOGlobalDCE | 40276.4 ms | 39096.4 ms | 1180.0 ms | 28734.2 ms |
| Gorm_schema | LLGoDeadcodeDrop | 37901.5 ms | 36580.2 ms | 1321.3 ms | 12966.5 ms |
| Gorm_schema | LLGoNoLTO | 36382.0 ms | 35076.9 ms | 1305.0 ms | 12555.0 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 34785.6 ms | 33842.8 ms | 942.8 ms | 27532.7 ms |
| Etcdctl | Go | 32410.9 ms | 30257.6 ms | 2153.4 ms | 10075.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 25517.9 ms | 24580.5 ms | 937.5 ms | 18254.9 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 25431.2 ms | 24492.9 ms | 938.3 ms | 18047.5 ms |
| Toml | LLGoDeadcodeDrop | 22858.1 ms | 21779.1 ms | 1079.0 ms | 8885.1 ms |
| Toml | LLGoNoLTO | 22665.6 ms | 21601.4 ms | 1064.3 ms | 8728.1 ms |
| XGo | Go | 18664.2 ms | 17438.9 ms | 1225.3 ms | 5541.3 ms |
| Dustin_humanize | LLGoNoLTO | 13637.9 ms | 12772.3 ms | 865.6 ms | 5868.1 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 13512.5 ms | 12681.1 ms | 831.4 ms | 5922.1 ms |
| Aws_restjson | Go | 7862.1 ms | 7052.1 ms | 810.0 ms | 3400.8 ms |
| Gorm_schema | Go | 5576.2 ms | 5138.4 ms | 437.8 ms | 2210.2 ms |
| Uber_zap | Go | 5200.3 ms | 4718.9 ms | 481.4 ms | 2152.4 ms |
| K8s_workqueue | Go | 4568.7 ms | 4116.6 ms | 452.2 ms | 1654.4 ms |
| Toml | Go | 2036.7 ms | 1776.6 ms | 260.1 ms | 946.1 ms |
| Dustin_humanize | Go | 794.7 ms | 645.8 ms | 148.9 ms | 381.3 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTOGlobalDCEPlugin | 1495488.5 ms | 941193.9 ms | 9 |
| LLGoFullLTOGlobalDCE | 1464116.9 ms | 920846.3 ms | 9 |
| LLGoFullLTONoGlobalDCE | 1449868.1 ms | 933832.5 ms | 9 |
| LLGoNoLTO | 994805.9 ms | 355269.3 ms | 9 |
| LLGoDeadcodeDrop | 958194.6 ms | 340942.5 ms | 9 |
| Go | 156581.7 ms | 48740.4 ms | 9 |

Dependency download details are in `download-timings.log`.
