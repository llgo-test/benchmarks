## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 527945.0 ms | 517101.5 ms | 10843.5 ms | 277477.7 ms |
| IXGo | LLGoFullLTOGlobalDCE | 516264.9 ms | 507073.4 ms | 9191.6 ms | 275225.0 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 497892.5 ms | 488850.2 ms | 9042.3 ms | 266460.7 ms |
| IXGo | LLGoNoLTO | 486157.6 ms | 476892.1 ms | 9265.5 ms | 140602.3 ms |
| IXGo | LLGoDeadcodeDrop | 399462.2 ms | 388086.0 ms | 11376.1 ms | 119311.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 231079.3 ms | 226775.9 ms | 4303.4 ms | 149027.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 227407.3 ms | 223141.6 ms | 4265.8 ms | 145703.0 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 227315.1 ms | 222999.5 ms | 4315.6 ms | 147175.9 ms |
| Aws_restjson | LLGoDeadcodeDrop | 205765.1 ms | 202602.0 ms | 3163.2 ms | 69290.9 ms |
| Aws_restjson | LLGoNoLTO | 187400.6 ms | 184619.3 ms | 2781.3 ms | 64373.3 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 181227.1 ms | 178350.3 ms | 2876.8 ms | 110254.7 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 180738.1 ms | 177593.5 ms | 3144.7 ms | 132539.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 180498.7 ms | 177611.1 ms | 2887.5 ms | 99994.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 171489.0 ms | 168522.6 ms | 2966.4 ms | 99239.2 ms |
| XGo | LLGoFullLTOGlobalDCE | 171432.4 ms | 168276.2 ms | 3156.2 ms | 124019.2 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 168706.7 ms | 165961.5 ms | 2745.2 ms | 109679.8 ms |
| XGo | LLGoFullLTONoGlobalDCE | 162940.4 ms | 159904.4 ms | 3036.0 ms | 118120.2 ms |
| Etcdctl | LLGoNoLTO | 159726.1 ms | 155638.9 ms | 4087.1 ms | 53510.5 ms |
| Etcdctl | LLGoDeadcodeDrop | 159722.6 ms | 155268.1 ms | 4454.5 ms | 54252.6 ms |
| Uber_zap | LLGoNoLTO | 155414.2 ms | 153083.4 ms | 2330.8 ms | 58808.6 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 153565.5 ms | 150932.6 ms | 2632.8 ms | 100340.0 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 150600.0 ms | 147807.4 ms | 2792.6 ms | 57706.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 149436.8 ms | 146764.8 ms | 2672.0 ms | 96163.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 146478.8 ms | 143966.5 ms | 2512.2 ms | 89690.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 144605.4 ms | 142047.8 ms | 2557.6 ms | 89346.2 ms |
| Uber_zap | LLGoDeadcodeDrop | 143415.8 ms | 140983.5 ms | 2432.3 ms | 54425.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 138300.2 ms | 135668.5 ms | 2631.8 ms | 84946.6 ms |
| K8s_workqueue | LLGoNoLTO | 137304.6 ms | 134990.0 ms | 2314.6 ms | 51820.8 ms |
| XGo | LLGoNoLTO | 92357.1 ms | 89971.2 ms | 2385.9 ms | 34237.0 ms |
| XGo | LLGoDeadcodeDrop | 91882.5 ms | 88886.4 ms | 2996.1 ms | 35280.6 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 81516.9 ms | 79858.5 ms | 1658.4 ms | 50118.7 ms |
| Gorm_schema | LLGoDeadcodeDrop | 78525.9 ms | 76850.6 ms | 1675.3 ms | 26444.1 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 78101.4 ms | 76518.3 ms | 1583.1 ms | 47534.7 ms |
| Gorm_schema | LLGoNoLTO | 74437.8 ms | 72957.5 ms | 1480.4 ms | 24871.6 ms |
| Toml | LLGoDeadcodeDrop | 70566.7 ms | 68928.1 ms | 1638.6 ms | 23667.1 ms |
| Toml | LLGoNoLTO | 70340.3 ms | 68764.1 ms | 1576.2 ms | 23169.2 ms |
| Toml | LLGoFullLTONoGlobalDCE | 70149.9 ms | 68452.8 ms | 1697.1 ms | 42349.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 67525.3 ms | 65968.1 ms | 1557.3 ms | 36704.4 ms |
| Toml | LLGoFullLTOGlobalDCE | 67141.3 ms | 65426.6 ms | 1714.7 ms | 37416.9 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 63761.4 ms | 62091.9 ms | 1669.5 ms | 35147.7 ms |
| IXGo | Go | 61900.6 ms | 57733.3 ms | 4167.3 ms | 17160.1 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 54834.0 ms | 53612.0 ms | 1222.0 ms | 35191.3 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 51877.2 ms | 50595.1 ms | 1282.1 ms | 19112.3 ms |
| Dustin_humanize | LLGoNoLTO | 49547.5 ms | 48408.0 ms | 1139.5 ms | 17850.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 43099.3 ms | 41964.9 ms | 1134.3 ms | 24364.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 41953.6 ms | 40814.4 ms | 1139.3 ms | 23651.9 ms |
| Etcdctl | Go | 24995.1 ms | 23218.9 ms | 1776.3 ms | 7896.4 ms |
| XGo | Go | 14272.7 ms | 13274.5 ms | 998.2 ms | 4308.3 ms |
| Aws_restjson | Go | 6476.3 ms | 5865.6 ms | 610.7 ms | 2790.7 ms |
| Gorm_schema | Go | 4304.9 ms | 3983.4 ms | 321.5 ms | 1695.4 ms |
| Uber_zap | Go | 3982.3 ms | 3632.7 ms | 349.6 ms | 1561.3 ms |
| K8s_workqueue | Go | 3683.0 ms | 3289.2 ms | 393.8 ms | 1357.8 ms |
| Toml | Go | 1538.3 ms | 1346.4 ms | 191.8 ms | 728.5 ms |
| Dustin_humanize | Go | 609.2 ms | 490.4 ms | 118.8 ms | 308.3 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1598148.1 ms | 979690.2 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1579426.1 ms | 929892.6 ms | 9 |
| LLGoFullLTOGlobalDCE | 1567832.2 ms | 938299.5 ms | 9 |
| LLGoNoLTO | 1412685.8 ms | 469243.9 ms | 9 |
| LLGoDeadcodeDrop | 1351818.0 ms | 459492.1 ms | 9 |
| Go | 121762.4 ms | 37806.8 ms | 9 |

Dependency download details are in `download-timings.log`.
