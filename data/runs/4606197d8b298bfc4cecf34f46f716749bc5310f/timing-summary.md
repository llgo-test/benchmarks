## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 571480.5 ms | 564813.5 ms | 6667.0 ms | 397808.0 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 560818.1 ms | 554462.9 ms | 6355.2 ms | 392926.6 ms |
| IXGo | LLGoFullLTOGlobalDCE | 536676.9 ms | 530483.7 ms | 6193.2 ms | 373430.8 ms |
| IXGo | LLGoDeadcodeDrop | 335814.7 ms | 330120.2 ms | 5694.5 ms | 125757.6 ms |
| IXGo | LLGoNoLTO | 329233.9 ms | 323659.6 ms | 5574.3 ms | 122689.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 260573.9 ms | 255850.3 ms | 4723.6 ms | 160155.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 251015.4 ms | 246143.5 ms | 4871.9 ms | 153968.4 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 249205.9 ms | 244565.6 ms | 4640.3 ms | 154805.7 ms |
| Etcdctl | LLGoDeadcodeDrop | 184731.9 ms | 180635.6 ms | 4096.3 ms | 60634.4 ms |
| Etcdctl | LLGoNoLTO | 179227.2 ms | 175147.1 ms | 4080.1 ms | 58444.5 ms |
| XGo | LLGoFullLTOGlobalDCE | 173764.7 ms | 170654.9 ms | 3109.7 ms | 122896.4 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 173504.4 ms | 170363.8 ms | 3140.6 ms | 121693.6 ms |
| XGo | LLGoFullLTONoGlobalDCE | 170887.4 ms | 168003.1 ms | 2884.3 ms | 121852.2 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 131413.8 ms | 129266.1 ms | 2147.6 ms | 98383.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 124183.4 ms | 122133.3 ms | 2050.1 ms | 89922.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 123398.5 ms | 121213.7 ms | 2184.8 ms | 89514.3 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 102399.2 ms | 100785.4 ms | 1613.8 ms | 79398.7 ms |
| XGo | LLGoDeadcodeDrop | 100869.9 ms | 98147.3 ms | 2722.6 ms | 37303.1 ms |
| XGo | LLGoNoLTO | 100734.0 ms | 98029.4 ms | 2704.7 ms | 37487.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 98564.1 ms | 96817.6 ms | 1746.4 ms | 77377.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 96067.9 ms | 94332.3 ms | 1735.6 ms | 71857.0 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 94952.9 ms | 93386.7 ms | 1566.2 ms | 74848.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 93778.1 ms | 92088.3 ms | 1689.8 ms | 70232.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 89686.2 ms | 87997.5 ms | 1688.7 ms | 67445.8 ms |
| Aws_restjson | LLGoNoLTO | 78189.5 ms | 76216.5 ms | 1973.0 ms | 36868.3 ms |
| Aws_restjson | LLGoDeadcodeDrop | 78113.1 ms | 76141.5 ms | 1971.6 ms | 36154.1 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 60813.6 ms | 59560.7 ms | 1252.9 ms | 43323.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 59650.5 ms | 58368.8 ms | 1281.7 ms | 42046.1 ms |
| Uber_zap | LLGoDeadcodeDrop | 51474.9 ms | 49907.9 ms | 1567.0 ms | 21784.1 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 49768.3 ms | 48549.8 ms | 1218.6 ms | 31956.6 ms |
| Toml | LLGoFullLTONoGlobalDCE | 49476.7 ms | 48503.9 ms | 972.8 ms | 38526.8 ms |
| Uber_zap | LLGoNoLTO | 49132.6 ms | 47735.6 ms | 1397.0 ms | 20836.5 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 44499.4 ms | 43140.9 ms | 1358.5 ms | 19743.1 ms |
| K8s_workqueue | LLGoNoLTO | 44172.6 ms | 42837.7 ms | 1334.9 ms | 19585.9 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 41295.6 ms | 40342.4 ms | 953.2 ms | 30011.4 ms |
| Toml | LLGoFullLTOGlobalDCE | 40977.0 ms | 40053.8 ms | 923.2 ms | 30158.9 ms |
| IXGo | Go | 40127.0 ms | 37189.1 ms | 2937.9 ms | 11610.2 ms |
| Gorm_schema | LLGoDeadcodeDrop | 35962.4 ms | 34815.2 ms | 1147.2 ms | 11761.7 ms |
| Gorm_schema | LLGoNoLTO | 35121.0 ms | 33993.6 ms | 1127.4 ms | 11577.3 ms |
| Etcdctl | Go | 31949.2 ms | 29799.5 ms | 2149.7 ms | 9532.6 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 30928.9 ms | 30155.1 ms | 773.8 ms | 24624.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 22873.8 ms | 22223.5 ms | 650.3 ms | 16499.5 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 22692.1 ms | 21991.7 ms | 700.4 ms | 16369.6 ms |
| Toml | LLGoDeadcodeDrop | 22383.9 ms | 21505.7 ms | 878.3 ms | 8240.4 ms |
| Toml | LLGoNoLTO | 20503.3 ms | 19730.8 ms | 772.4 ms | 8171.5 ms |
| XGo | Go | 17806.9 ms | 16590.8 ms | 1216.1 ms | 5145.6 ms |
| Dustin_humanize | LLGoNoLTO | 12333.8 ms | 11708.0 ms | 625.8 ms | 5430.0 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 12018.1 ms | 11387.4 ms | 630.7 ms | 5256.9 ms |
| Aws_restjson | Go | 7360.4 ms | 6754.2 ms | 606.2 ms | 2875.3 ms |
| Gorm_schema | Go | 5523.0 ms | 5136.4 ms | 386.5 ms | 2072.9 ms |
| Uber_zap | Go | 4829.5 ms | 4480.7 ms | 348.8 ms | 1876.8 ms |
| K8s_workqueue | Go | 4394.1 ms | 3995.2 ms | 398.9 ms | 1562.7 ms |
| Toml | Go | 1867.0 ms | 1681.4 ms | 185.6 ms | 835.7 ms |
| Dustin_humanize | Go | 758.4 ms | 628.9 ms | 129.6 ms | 352.9 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1450896.6 ms | 1028690.3 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1426177.6 ms | 985187.0 ms | 9 |
| LLGoFullLTOGlobalDCE | 1403773.7 ms | 978157.4 ms | 9 |
| LLGoDeadcodeDrop | 865868.3 ms | 326635.4 ms | 9 |
| LLGoNoLTO | 848647.9 ms | 321090.7 ms | 9 |
| Go | 114615.5 ms | 35864.7 ms | 9 |

Dependency download details are in `download-timings.log`.
