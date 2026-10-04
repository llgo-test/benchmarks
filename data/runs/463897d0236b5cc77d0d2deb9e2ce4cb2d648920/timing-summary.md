## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 675817.4 ms | 665216.0 ms | 10601.4 ms | 347025.5 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 652611.8 ms | 641997.5 ms | 10614.2 ms | 337827.6 ms |
| IXGo | LLGoFullLTOGlobalDCE | 649000.6 ms | 638480.2 ms | 10520.4 ms | 335598.3 ms |
| IXGo | LLGoDeadcodeDrop | 534908.1 ms | 520725.5 ms | 14182.6 ms | 159138.7 ms |
| IXGo | LLGoNoLTO | 518522.2 ms | 509242.5 ms | 9279.7 ms | 151125.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 344577.0 ms | 338989.6 ms | 5587.4 ms | 201641.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 340581.3 ms | 335208.2 ms | 5373.1 ms | 199533.2 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 337346.8 ms | 332355.2 ms | 4991.6 ms | 198763.5 ms |
| Aws_restjson | LLGoDeadcodeDrop | 268768.6 ms | 265379.3 ms | 3389.3 ms | 89870.9 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 268174.0 ms | 264485.6 ms | 3688.4 ms | 148713.2 ms |
| Aws_restjson | LLGoNoLTO | 264803.7 ms | 261558.5 ms | 3245.2 ms | 88372.9 ms |
| Etcdctl | LLGoDeadcodeDrop | 262923.6 ms | 256828.4 ms | 6095.2 ms | 87093.4 ms |
| Etcdctl | LLGoNoLTO | 258945.6 ms | 254506.6 ms | 4439.0 ms | 84713.1 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 257521.9 ms | 253768.1 ms | 3753.8 ms | 134985.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 255575.1 ms | 251847.2 ms | 3727.9 ms | 134220.2 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 244333.6 ms | 240938.6 ms | 3394.9 ms | 159340.9 ms |
| XGo | LLGoFullLTONoGlobalDCE | 243996.2 ms | 240791.1 ms | 3205.2 ms | 160724.0 ms |
| XGo | LLGoFullLTOGlobalDCE | 242993.6 ms | 239724.6 ms | 3269.0 ms | 158349.3 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 231729.3 ms | 228554.0 ms | 3175.3 ms | 133016.3 ms |
| Uber_zap | LLGoDeadcodeDrop | 229629.5 ms | 226669.6 ms | 2959.9 ms | 80904.8 ms |
| Uber_zap | LLGoNoLTO | 225767.5 ms | 222860.2 ms | 2907.4 ms | 79703.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 225651.5 ms | 222198.7 ms | 3452.8 ms | 129204.0 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 225379.6 ms | 221808.7 ms | 3570.9 ms | 129156.9 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 222370.3 ms | 219404.6 ms | 2965.8 ms | 78040.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 221855.9 ms | 218456.5 ms | 3399.4 ms | 120839.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 220581.8 ms | 217418.8 ms | 3163.0 ms | 119918.9 ms |
| K8s_workqueue | LLGoNoLTO | 219324.6 ms | 216313.2 ms | 3011.4 ms | 77274.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 210170.3 ms | 206835.1 ms | 3335.2 ms | 112953.5 ms |
| XGo | LLGoDeadcodeDrop | 159863.0 ms | 156394.9 ms | 3468.1 ms | 58750.0 ms |
| XGo | LLGoNoLTO | 158612.7 ms | 155965.7 ms | 2647.0 ms | 57136.0 ms |
| Gorm_schema | LLGoDeadcodeDrop | 108751.4 ms | 107070.8 ms | 1680.7 ms | 35956.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 107657.7 ms | 105631.4 ms | 2026.3 ms | 62041.1 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 107136.2 ms | 105156.7 ms | 1979.5 ms | 62398.0 ms |
| Gorm_schema | LLGoNoLTO | 106722.1 ms | 104948.5 ms | 1773.6 ms | 35291.5 ms |
| Toml | LLGoDeadcodeDrop | 101953.5 ms | 100176.4 ms | 1777.1 ms | 33524.5 ms |
| Toml | LLGoNoLTO | 101110.9 ms | 99332.6 ms | 1778.3 ms | 33258.0 ms |
| Toml | LLGoFullLTONoGlobalDCE | 99423.6 ms | 97441.1 ms | 1982.5 ms | 57021.1 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 95466.0 ms | 93482.1 ms | 1983.9 ms | 49458.7 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 90916.1 ms | 88989.4 ms | 1926.7 ms | 47847.5 ms |
| Toml | LLGoFullLTOGlobalDCE | 90770.7 ms | 88835.2 ms | 1935.5 ms | 47647.6 ms |
| IXGo | Go | 83685.3 ms | 78654.9 ms | 5030.3 ms | 23102.1 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 71089.2 ms | 69932.2 ms | 1157.0 ms | 25450.5 ms |
| Dustin_humanize | LLGoNoLTO | 70728.4 ms | 69507.2 ms | 1221.1 ms | 25294.9 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 70713.0 ms | 69338.7 ms | 1374.3 ms | 42671.9 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 60943.8 ms | 59567.0 ms | 1376.8 ms | 32594.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 60416.6 ms | 59055.1 ms | 1361.5 ms | 32447.8 ms |
| Etcdctl | Go | 33470.7 ms | 31458.2 ms | 2012.5 ms | 10074.3 ms |
| XGo | Go | 19202.9 ms | 18123.8 ms | 1079.1 ms | 5652.1 ms |
| Aws_restjson | Go | 7850.3 ms | 7176.4 ms | 674.0 ms | 3181.3 ms |
| Gorm_schema | Go | 5757.5 ms | 5353.1 ms | 404.3 ms | 2202.2 ms |
| Uber_zap | Go | 5286.6 ms | 4869.1 ms | 417.5 ms | 2048.8 ms |
| K8s_workqueue | Go | 4691.7 ms | 4202.4 ms | 489.2 ms | 1633.0 ms |
| Toml | Go | 2032.5 ms | 1804.6 ms | 228.0 ms | 918.2 ms |
| Dustin_humanize | Go | 819.7 ms | 667.9 ms | 151.7 ms | 384.0 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2236510.4 ms | 1270292.8 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2201602.0 ms | 1206686.0 ms | 9 |
| LLGoFullLTOGlobalDCE | 2193228.8 ms | 1218960.5 ms | 9 |
| LLGoDeadcodeDrop | 1960257.3 ms | 648729.5 ms | 9 |
| LLGoNoLTO | 1924537.8 ms | 632170.7 ms | 9 |
| Go | 162797.1 ms | 49196.1 ms | 9 |

Dependency download details are in `download-timings.log`.
