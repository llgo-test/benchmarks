## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 538808.7 ms | 526720.9 ms | 12087.8 ms | 280236.8 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 530797.2 ms | 518481.5 ms | 12315.6 ms | 281544.4 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 520635.3 ms | 508599.6 ms | 12035.8 ms | 275527.0 ms |
| IXGo | LLGoDeadcodeDrop | 430319.4 ms | 419543.2 ms | 10776.2 ms | 128407.2 ms |
| IXGo | LLGoNoLTO | 406413.4 ms | 396434.2 ms | 9979.2 ms | 122028.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 259800.5 ms | 255131.7 ms | 4668.7 ms | 158301.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 256845.2 ms | 251932.3 ms | 4912.8 ms | 156585.9 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 254963.0 ms | 250319.3 ms | 4643.6 ms | 157520.0 ms |
| Etcdctl | LLGoDeadcodeDrop | 195162.1 ms | 190876.1 ms | 4286.0 ms | 65375.9 ms |
| Etcdctl | LLGoNoLTO | 190121.9 ms | 185672.1 ms | 4449.8 ms | 64449.8 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 180256.5 ms | 176899.4 ms | 3357.1 ms | 123710.4 ms |
| XGo | LLGoFullLTONoGlobalDCE | 180222.7 ms | 176999.4 ms | 3223.2 ms | 124425.6 ms |
| XGo | LLGoFullLTOGlobalDCE | 179929.8 ms | 176519.7 ms | 3410.1 ms | 123216.2 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 137686.4 ms | 135278.0 ms | 2408.4 ms | 99739.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 126357.5 ms | 123907.9 ms | 2449.6 ms | 86518.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 126047.9 ms | 123443.9 ms | 2604.0 ms | 87552.6 ms |
| XGo | LLGoDeadcodeDrop | 113526.9 ms | 110686.0 ms | 2840.9 ms | 42816.7 ms |
| XGo | LLGoNoLTO | 111020.6 ms | 108262.8 ms | 2757.8 ms | 41689.5 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 109890.3 ms | 108036.9 ms | 1853.4 ms | 82678.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 100731.3 ms | 98907.2 ms | 1824.2 ms | 72654.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 99908.5 ms | 98069.6 ms | 1839.0 ms | 72256.7 ms |
| IXGo | Go | 84287.5 ms | 79135.9 ms | 5151.6 ms | 23041.0 ms |
| Aws_restjson | LLGoDeadcodeDrop | 84218.1 ms | 81916.0 ms | 2302.1 ms | 39146.2 ms |
| Aws_restjson | LLGoNoLTO | 84185.5 ms | 82054.6 ms | 2130.9 ms | 38572.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 62713.9 ms | 61333.7 ms | 1380.2 ms | 42285.2 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 62628.9 ms | 61168.5 ms | 1460.4 ms | 42936.2 ms |
| Uber_zap | LLGoDeadcodeDrop | 59271.3 ms | 57765.5 ms | 1505.8 ms | 26049.5 ms |
| Uber_zap | LLGoNoLTO | 57646.8 ms | 56176.8 ms | 1469.9 ms | 25385.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 52429.9 ms | 51121.8 ms | 1308.1 ms | 31745.2 ms |
| Toml | LLGoFullLTONoGlobalDCE | 48609.9 ms | 47586.8 ms | 1023.2 ms | 36499.1 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 41809.7 ms | 40729.9 ms | 1079.8 ms | 28736.9 ms |
| Toml | LLGoFullLTOGlobalDCE | 40969.5 ms | 39939.2 ms | 1030.2 ms | 28531.1 ms |
| Gorm_schema | LLGoDeadcodeDrop | 40444.9 ms | 39181.8 ms | 1263.1 ms | 13598.7 ms |
| Gorm_schema | LLGoNoLTO | 39793.7 ms | 38528.9 ms | 1264.8 ms | 13405.1 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 34521.9 ms | 33620.1 ms | 901.8 ms | 26771.6 ms |
| Etcdctl | Go | 33747.7 ms | 31463.6 ms | 2284.0 ms | 10603.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 26201.0 ms | 25331.4 ms | 869.5 ms | 18095.9 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 26018.5 ms | 25186.7 ms | 831.8 ms | 18101.6 ms |
| Toml | LLGoDeadcodeDrop | 25260.4 ms | 24201.2 ms | 1059.2 ms | 9277.2 ms |
| Toml | LLGoNoLTO | 24331.8 ms | 23303.6 ms | 1028.2 ms | 9078.2 ms |
| XGo | Go | 19237.3 ms | 18004.3 ms | 1233.0 ms | 5899.6 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 14314.1 ms | 13541.3 ms | 772.8 ms | 6016.2 ms |
| Dustin_humanize | LLGoNoLTO | 14268.4 ms | 13494.8 ms | 773.5 ms | 5915.0 ms |
| Aws_restjson | Go | 7914.1 ms | 7192.7 ms | 721.4 ms | 3181.1 ms |
| Gorm_schema | Go | 5758.9 ms | 5353.5 ms | 405.4 ms | 2205.0 ms |
| Uber_zap | Go | 5314.8 ms | 4887.8 ms | 427.0 ms | 2156.5 ms |
| K8s_workqueue | Go | 4691.2 ms | 4230.7 ms | 460.4 ms | 1656.8 ms |
| Toml | Go | 2025.2 ms | 1756.1 ms | 269.1 ms | 915.4 ms |
| Dustin_humanize | Go | 989.3 ms | 715.6 ms | 273.7 ms | 732.3 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1349158.4 ms | 846097.4 ms | 8 |
| LLGoFullLTOGlobalDCE | 1331241.9 ms | 808766.2 ms | 8 |
| LLGoFullLTOGlobalDCEPlugin | 1318383.5 ms | 801308.1 ms | 8 |
| LLGoDeadcodeDrop | 962517.2 ms | 330687.7 ms | 8 |
| LLGoNoLTO | 927782.0 ms | 320524.3 ms | 8 |
| Go | 163965.8 ms | 50391.2 ms | 9 |

Dependency download details are in `download-timings.log`.
