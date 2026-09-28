## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 609151.5 ms | 597399.9 ms | 11751.6 ms | 302206.3 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 585992.6 ms | 574505.3 ms | 11487.3 ms | 295528.0 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 530634.1 ms | 517847.8 ms | 12786.3 ms | 279069.8 ms |
| IXGo | LLGoNoLTO | 431265.2 ms | 421458.4 ms | 9806.8 ms | 127131.9 ms |
| IXGo | LLGoDeadcodeDrop | 429062.1 ms | 417753.1 ms | 11309.0 ms | 127461.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 256515.5 ms | 251923.5 ms | 4592.0 ms | 157255.3 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 255490.8 ms | 251034.6 ms | 4456.1 ms | 157036.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 250865.0 ms | 246325.3 ms | 4539.7 ms | 153501.8 ms |
| Etcdctl | LLGoDeadcodeDrop | 189865.9 ms | 185866.3 ms | 3999.6 ms | 62746.5 ms |
| Etcdctl | LLGoNoLTO | 185565.1 ms | 181628.3 ms | 3936.8 ms | 61346.1 ms |
| XGo | LLGoFullLTOGlobalDCE | 179940.6 ms | 176536.7 ms | 3403.9 ms | 123361.0 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 176902.4 ms | 173845.9 ms | 3056.4 ms | 121158.2 ms |
| XGo | LLGoFullLTONoGlobalDCE | 176147.9 ms | 172938.0 ms | 3209.9 ms | 120662.4 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 138314.9 ms | 135898.5 ms | 2416.3 ms | 100452.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 128148.4 ms | 125809.9 ms | 2338.5 ms | 88657.3 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 125806.0 ms | 123471.9 ms | 2334.1 ms | 86638.6 ms |
| XGo | LLGoDeadcodeDrop | 110409.6 ms | 107681.8 ms | 2727.8 ms | 40470.7 ms |
| XGo | LLGoNoLTO | 107395.7 ms | 104620.8 ms | 2774.9 ms | 39561.2 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 106748.0 ms | 104953.8 ms | 1794.2 ms | 80214.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 101703.1 ms | 99960.0 ms | 1743.0 ms | 77956.4 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 99883.0 ms | 98107.7 ms | 1775.3 ms | 77052.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 99010.3 ms | 97246.9 ms | 1763.4 ms | 70996.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 98166.9 ms | 96403.9 ms | 1763.0 ms | 70446.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 88213.1 ms | 86456.8 ms | 1756.3 ms | 64425.7 ms |
| Aws_restjson | LLGoDeadcodeDrop | 85638.9 ms | 83656.2 ms | 1982.7 ms | 39545.2 ms |
| Aws_restjson | LLGoNoLTO | 85043.2 ms | 82980.1 ms | 2063.1 ms | 39832.3 ms |
| IXGo | Go | 81977.4 ms | 76364.3 ms | 5613.0 ms | 22999.7 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 62129.1 ms | 60768.0 ms | 1361.1 ms | 42321.3 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 62050.6 ms | 60707.8 ms | 1342.8 ms | 42482.4 ms |
| Uber_zap | LLGoDeadcodeDrop | 57369.7 ms | 55957.2 ms | 1412.5 ms | 24272.6 ms |
| Uber_zap | LLGoNoLTO | 57012.5 ms | 55519.3 ms | 1493.2 ms | 24189.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 51692.6 ms | 50383.1 ms | 1309.6 ms | 31395.2 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 50370.7 ms | 48814.5 ms | 1556.2 ms | 22573.5 ms |
| K8s_workqueue | LLGoNoLTO | 48708.5 ms | 47331.6 ms | 1376.8 ms | 21669.8 ms |
| Toml | LLGoFullLTONoGlobalDCE | 47821.1 ms | 46806.1 ms | 1015.0 ms | 35842.6 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 40842.5 ms | 39833.3 ms | 1009.2 ms | 28625.5 ms |
| Toml | LLGoFullLTOGlobalDCE | 40515.7 ms | 39503.0 ms | 1012.7 ms | 28282.0 ms |
| Gorm_schema | LLGoDeadcodeDrop | 39654.0 ms | 38394.2 ms | 1259.8 ms | 13409.7 ms |
| Gorm_schema | LLGoNoLTO | 39102.9 ms | 37874.2 ms | 1228.6 ms | 12905.0 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 34412.7 ms | 33640.2 ms | 772.5 ms | 26507.5 ms |
| Etcdctl | Go | 33229.6 ms | 30908.7 ms | 2320.9 ms | 10597.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 26130.4 ms | 25325.6 ms | 804.8 ms | 17993.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 25916.8 ms | 25129.1 ms | 787.6 ms | 17746.0 ms |
| Toml | LLGoDeadcodeDrop | 23779.4 ms | 22887.0 ms | 892.4 ms | 9081.0 ms |
| Toml | LLGoNoLTO | 23577.7 ms | 22658.0 ms | 919.7 ms | 9028.8 ms |
| XGo | Go | 18963.1 ms | 17676.2 ms | 1286.9 ms | 5772.1 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 14237.0 ms | 13553.7 ms | 683.2 ms | 5912.5 ms |
| Dustin_humanize | LLGoNoLTO | 13838.6 ms | 13163.7 ms | 674.9 ms | 5820.7 ms |
| Aws_restjson | Go | 7986.4 ms | 7268.9 ms | 717.5 ms | 3471.9 ms |
| Gorm_schema | Go | 5588.9 ms | 5193.2 ms | 395.6 ms | 2111.2 ms |
| Uber_zap | Go | 5259.0 ms | 4873.8 ms | 385.2 ms | 2064.3 ms |
| K8s_workqueue | Go | 4523.2 ms | 4100.3 ms | 422.9 ms | 1588.1 ms |
| Toml | Go | 1984.6 ms | 1768.0 ms | 216.7 ms | 959.0 ms |
| Dustin_humanize | Go | 869.7 ms | 676.9 ms | 192.9 ms | 740.4 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTOGlobalDCE | 1494194.7 ms | 902459.6 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1453447.7 ms | 876035.2 ms | 9 |
| LLGoFullLTONoGlobalDCE | 1451503.0 ms | 919319.6 ms | 9 |
| LLGoDeadcodeDrop | 1000387.3 ms | 345473.3 ms | 9 |
| LLGoNoLTO | 991509.3 ms | 341485.4 ms | 9 |
| Go | 160382.0 ms | 50304.7 ms | 9 |

Dependency download details are in `download-timings.log`.
