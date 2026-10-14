## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 663650.6 ms | 651771.5 ms | 11879.1 ms | 350032.3 ms |
| IXGo | LLGoFullLTOGlobalDCE | 650516.3 ms | 638678.3 ms | 11838.0 ms | 342555.0 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 626618.4 ms | 614561.9 ms | 12056.5 ms | 339462.6 ms |
| IXGo | LLGoDeadcodeDrop | 481732.5 ms | 466684.9 ms | 15047.5 ms | 143094.6 ms |
| IXGo | LLGoNoLTO | 479234.6 ms | 469461.6 ms | 9773.0 ms | 137126.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 294209.7 ms | 288633.4 ms | 5576.3 ms | 187386.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 292527.8 ms | 287240.5 ms | 5287.3 ms | 186313.6 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 287457.7 ms | 282207.2 ms | 5250.5 ms | 185162.6 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 232655.3 ms | 229328.6 ms | 3326.6 ms | 140660.9 ms |
| Aws_restjson | LLGoNoLTO | 220857.5 ms | 217869.2 ms | 2988.3 ms | 74715.1 ms |
| Aws_restjson | LLGoDeadcodeDrop | 220552.3 ms | 217280.1 ms | 3272.2 ms | 75919.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 218450.0 ms | 214972.4 ms | 3477.6 ms | 124347.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 217842.9 ms | 214660.9 ms | 3182.1 ms | 124582.8 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 205399.0 ms | 201896.3 ms | 3502.7 ms | 147304.8 ms |
| XGo | LLGoFullLTONoGlobalDCE | 204018.4 ms | 200501.1 ms | 3517.4 ms | 148578.3 ms |
| Etcdctl | LLGoDeadcodeDrop | 203600.4 ms | 198170.1 ms | 5430.4 ms | 67024.8 ms |
| XGo | LLGoFullLTOGlobalDCE | 203257.7 ms | 199781.3 ms | 3476.3 ms | 146781.1 ms |
| Etcdctl | LLGoNoLTO | 201708.1 ms | 196893.8 ms | 4814.3 ms | 65130.4 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 190337.9 ms | 187585.3 ms | 2752.6 ms | 122131.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 187370.2 ms | 184499.7 ms | 2870.5 ms | 119619.6 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 185583.3 ms | 182782.8 ms | 2800.5 ms | 119316.5 ms |
| Uber_zap | LLGoNoLTO | 180883.8 ms | 178284.2 ms | 2599.6 ms | 65685.6 ms |
| Uber_zap | LLGoDeadcodeDrop | 180551.3 ms | 177740.3 ms | 2811.0 ms | 66612.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 180436.7 ms | 177675.0 ms | 2761.7 ms | 109514.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 177652.4 ms | 174915.0 ms | 2737.4 ms | 108432.3 ms |
| K8s_workqueue | LLGoNoLTO | 172859.6 ms | 170347.3 ms | 2512.3 ms | 63449.4 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 172123.6 ms | 169392.6 ms | 2731.0 ms | 63926.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 170167.4 ms | 167310.7 ms | 2856.7 ms | 102237.4 ms |
| XGo | LLGoDeadcodeDrop | 114354.1 ms | 111109.8 ms | 3244.2 ms | 41880.3 ms |
| XGo | LLGoNoLTO | 113630.4 ms | 110704.4 ms | 2925.9 ms | 41307.5 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 99159.8 ms | 97300.7 ms | 1859.2 ms | 60411.7 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 98020.2 ms | 96198.2 ms | 1822.0 ms | 59047.2 ms |
| Gorm_schema | LLGoDeadcodeDrop | 96381.5 ms | 94581.0 ms | 1800.5 ms | 32170.6 ms |
| Gorm_schema | LLGoNoLTO | 95357.0 ms | 93762.4 ms | 1594.6 ms | 31478.2 ms |
| Toml | LLGoFullLTONoGlobalDCE | 90075.5 ms | 88357.1 ms | 1718.4 ms | 54417.8 ms |
| Toml | LLGoNoLTO | 89996.0 ms | 88374.5 ms | 1621.6 ms | 29644.1 ms |
| Toml | LLGoDeadcodeDrop | 89509.5 ms | 87808.7 ms | 1700.8 ms | 29809.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 85855.1 ms | 84118.4 ms | 1736.6 ms | 46765.5 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 82522.9 ms | 80841.8 ms | 1681.1 ms | 45445.1 ms |
| Toml | LLGoFullLTOGlobalDCE | 80822.3 ms | 79134.6 ms | 1687.7 ms | 44794.6 ms |
| IXGo | Go | 80107.0 ms | 74454.7 ms | 5652.3 ms | 21827.6 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 64713.5 ms | 63456.4 ms | 1257.1 ms | 41121.9 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 61915.2 ms | 60803.7 ms | 1111.5 ms | 22427.7 ms |
| Dustin_humanize | LLGoNoLTO | 61669.6 ms | 60558.3 ms | 1111.3 ms | 21969.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 53843.6 ms | 52662.4 ms | 1181.1 ms | 30101.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 53621.4 ms | 52470.8 ms | 1150.6 ms | 30234.7 ms |
| Etcdctl | Go | 32312.9 ms | 30180.4 ms | 2132.5 ms | 9661.0 ms |
| XGo | Go | 18378.1 ms | 17117.4 ms | 1260.7 ms | 5567.5 ms |
| Aws_restjson | Go | 7767.9 ms | 7136.3 ms | 631.6 ms | 3059.9 ms |
| Gorm_schema | Go | 5613.4 ms | 5197.8 ms | 415.5 ms | 2149.9 ms |
| Uber_zap | Go | 5280.9 ms | 4851.8 ms | 429.0 ms | 2109.8 ms |
| K8s_workqueue | Go | 4589.9 ms | 4141.5 ms | 448.4 ms | 1733.7 ms |
| Toml | Go | 1986.6 ms | 1770.0 ms | 216.5 ms | 1324.4 ms |
| Dustin_humanize | Go | 832.9 ms | 681.7 ms | 151.1 ms | 1156.1 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1980620.0 ms | 1211263.6 ms | 9 |
| LLGoFullLTOGlobalDCE | 1962238.4 ms | 1162125.6 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1953927.8 ms | 1143371.3 ms | 9 |
| LLGoDeadcodeDrop | 1620720.5 ms | 542865.0 ms | 9 |
| LLGoNoLTO | 1616196.6 ms | 530506.5 ms | 9 |
| Go | 156869.4 ms | 48589.9 ms | 9 |

Dependency download details are in `download-timings.log`.
