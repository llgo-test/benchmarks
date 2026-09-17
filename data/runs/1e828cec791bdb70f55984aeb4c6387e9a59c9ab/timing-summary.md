## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 571224.5 ms | 559178.6 ms | 12045.9 ms | 294489.7 ms |
| IXGo | LLGoFullLTOGlobalDCE | 568396.5 ms | 555543.9 ms | 12852.6 ms | 298317.3 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 531957.8 ms | 520754.5 ms | 11203.3 ms | 278744.6 ms |
| IXGo | LLGoDeadcodeDrop | 445142.9 ms | 434909.5 ms | 10233.5 ms | 131528.5 ms |
| IXGo | LLGoNoLTO | 422779.4 ms | 411839.2 ms | 10940.2 ms | 125700.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 301498.3 ms | 296401.8 ms | 5096.5 ms | 174386.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 291568.0 ms | 286666.4 ms | 4901.5 ms | 167769.5 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 290273.9 ms | 285389.2 ms | 4884.7 ms | 168253.2 ms |
| Etcdctl | LLGoDeadcodeDrop | 230184.9 ms | 225515.2 ms | 4669.7 ms | 74405.3 ms |
| Etcdctl | LLGoNoLTO | 223907.6 ms | 219787.9 ms | 4119.8 ms | 71555.2 ms |
| XGo | LLGoFullLTOGlobalDCE | 185625.6 ms | 182257.5 ms | 3368.1 ms | 128122.5 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 185296.1 ms | 181894.7 ms | 3401.4 ms | 126659.7 ms |
| XGo | LLGoFullLTONoGlobalDCE | 183619.4 ms | 180336.2 ms | 3283.3 ms | 126397.5 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 176215.6 ms | 173702.0 ms | 2513.6 ms | 138640.1 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 157445.0 ms | 155223.0 ms | 2222.0 ms | 119496.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 156555.0 ms | 154274.8 ms | 2280.2 ms | 118101.6 ms |
| Aws_restjson | LLGoDeadcodeDrop | 115286.1 ms | 113113.8 ms | 2172.2 ms | 70847.7 ms |
| Aws_restjson | LLGoNoLTO | 114797.4 ms | 112776.4 ms | 2021.0 ms | 70938.9 ms |
| XGo | LLGoDeadcodeDrop | 114166.8 ms | 111239.1 ms | 2927.7 ms | 42810.9 ms |
| XGo | LLGoNoLTO | 111934.2 ms | 109143.4 ms | 2790.8 ms | 42088.6 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 111307.7 ms | 109516.5 ms | 1791.2 ms | 84593.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 104773.9 ms | 102985.7 ms | 1788.2 ms | 80945.6 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 104690.3 ms | 102914.2 ms | 1776.1 ms | 81272.9 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 102285.6 ms | 100397.9 ms | 1887.7 ms | 74021.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 100973.5 ms | 99179.1 ms | 1794.4 ms | 73591.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 91440.0 ms | 89622.4 ms | 1817.6 ms | 67382.3 ms |
| IXGo | Go | 84264.7 ms | 79157.3 ms | 5107.4 ms | 23757.5 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 63801.1 ms | 62398.6 ms | 1402.5 ms | 43815.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 62558.8 ms | 61172.6 ms | 1386.3 ms | 42302.7 ms |
| Uber_zap | LLGoDeadcodeDrop | 59350.3 ms | 57884.8 ms | 1465.6 ms | 25996.1 ms |
| Uber_zap | LLGoNoLTO | 58336.6 ms | 56892.1 ms | 1444.5 ms | 25546.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 53240.5 ms | 51894.4 ms | 1346.1 ms | 32414.8 ms |
| K8s_workqueue | LLGoNoLTO | 53005.1 ms | 51332.7 ms | 1672.4 ms | 25041.4 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 51593.1 ms | 50099.4 ms | 1493.6 ms | 23654.2 ms |
| Toml | LLGoFullLTONoGlobalDCE | 49412.0 ms | 48361.0 ms | 1051.0 ms | 36982.8 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 42906.1 ms | 41836.5 ms | 1069.7 ms | 29467.5 ms |
| Toml | LLGoFullLTOGlobalDCE | 42685.8 ms | 41519.2 ms | 1166.6 ms | 29980.2 ms |
| Gorm_schema | LLGoDeadcodeDrop | 41192.1 ms | 39945.3 ms | 1246.9 ms | 13771.0 ms |
| Gorm_schema | LLGoNoLTO | 40457.9 ms | 39263.1 ms | 1194.7 ms | 13385.2 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 35198.0 ms | 34286.6 ms | 911.4 ms | 27263.9 ms |
| Etcdctl | Go | 34312.4 ms | 31909.8 ms | 2402.7 ms | 10698.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 26572.8 ms | 25729.5 ms | 843.3 ms | 18398.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 25930.6 ms | 25111.3 ms | 819.3 ms | 18415.0 ms |
| Toml | LLGoDeadcodeDrop | 25535.4 ms | 24463.1 ms | 1072.3 ms | 9459.8 ms |
| Toml | LLGoNoLTO | 25017.7 ms | 24013.7 ms | 1004.0 ms | 9414.2 ms |
| XGo | Go | 19427.4 ms | 18239.7 ms | 1187.7 ms | 5808.4 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 13809.4 ms | 13084.8 ms | 724.6 ms | 5961.0 ms |
| Dustin_humanize | LLGoNoLTO | 13802.9 ms | 13038.8 ms | 764.1 ms | 5923.6 ms |
| Aws_restjson | Go | 7961.8 ms | 7277.7 ms | 684.0 ms | 3249.5 ms |
| Gorm_schema | Go | 6005.7 ms | 5433.0 ms | 572.7 ms | 2653.5 ms |
| Uber_zap | Go | 5341.3 ms | 4905.9 ms | 435.4 ms | 2099.6 ms |
| K8s_workqueue | Go | 4891.3 ms | 4301.6 ms | 589.8 ms | 2156.7 ms |
| Toml | Go | 2073.6 ms | 1830.9 ms | 242.7 ms | 940.8 ms |
| Dustin_humanize | Go | 837.2 ms | 681.7 ms | 155.5 ms | 402.6 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1546475.7 ms | 985963.9 ms | 9 |
| LLGoFullLTOGlobalDCE | 1539957.7 ms | 958940.2 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1531018.9 ms | 935322.4 ms | 9 |
| LLGoDeadcodeDrop | 1096261.0 ms | 398434.6 ms | 9 |
| LLGoNoLTO | 1064038.9 ms | 389594.4 ms | 9 |
| Go | 165115.5 ms | 51766.6 ms | 9 |

Dependency download details are in `download-timings.log`.
