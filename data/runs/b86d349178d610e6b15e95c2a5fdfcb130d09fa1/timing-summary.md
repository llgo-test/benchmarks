## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 634487.4 ms | 623843.2 ms | 10644.2 ms | 334097.8 ms |
| IXGo | LLGoFullLTOGlobalDCE | 623724.6 ms | 612762.4 ms | 10962.2 ms | 327791.9 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 611811.3 ms | 601683.6 ms | 10127.6 ms | 325590.7 ms |
| IXGo | LLGoNoLTO | 491734.3 ms | 482358.2 ms | 9376.1 ms | 143426.3 ms |
| IXGo | LLGoDeadcodeDrop | 489406.7 ms | 476468.9 ms | 12937.8 ms | 147311.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 323258.7 ms | 318066.2 ms | 5192.4 ms | 194191.5 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 320951.9 ms | 315858.3 ms | 5093.6 ms | 193615.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 320455.7 ms | 314952.5 ms | 5503.3 ms | 191955.8 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 250276.7 ms | 246641.0 ms | 3635.7 ms | 141241.4 ms |
| Aws_restjson | LLGoDeadcodeDrop | 244430.5 ms | 241422.2 ms | 3008.3 ms | 81227.4 ms |
| Aws_restjson | LLGoNoLTO | 240963.5 ms | 237904.7 ms | 3058.8 ms | 80317.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 237227.6 ms | 233788.8 ms | 3438.8 ms | 127077.1 ms |
| Etcdctl | LLGoNoLTO | 236377.2 ms | 232066.0 ms | 4311.2 ms | 77079.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 234798.1 ms | 231402.4 ms | 3395.7 ms | 125278.9 ms |
| XGo | LLGoFullLTONoGlobalDCE | 234403.7 ms | 230954.3 ms | 3449.4 ms | 157785.9 ms |
| Etcdctl | LLGoDeadcodeDrop | 233982.3 ms | 228703.6 ms | 5278.7 ms | 77359.7 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 231645.6 ms | 228189.0 ms | 3456.7 ms | 153429.3 ms |
| XGo | LLGoFullLTOGlobalDCE | 230071.7 ms | 226639.6 ms | 3432.1 ms | 153239.0 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 213247.4 ms | 210109.5 ms | 3137.9 ms | 125260.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 209447.5 ms | 206268.9 ms | 3178.5 ms | 122939.9 ms |
| Uber_zap | LLGoNoLTO | 208915.4 ms | 206171.5 ms | 2743.9 ms | 73680.9 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 205457.5 ms | 202404.3 ms | 3053.2 ms | 121472.4 ms |
| Uber_zap | LLGoDeadcodeDrop | 205110.2 ms | 202473.4 ms | 2636.8 ms | 71953.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 202713.7 ms | 199708.2 ms | 3005.5 ms | 112967.0 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 202235.9 ms | 199288.5 ms | 2947.4 ms | 71581.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 197150.7 ms | 194250.6 ms | 2900.1 ms | 110286.5 ms |
| K8s_workqueue | LLGoNoLTO | 196017.3 ms | 193431.7 ms | 2585.6 ms | 69065.8 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 195952.7 ms | 192785.8 ms | 3166.8 ms | 108246.2 ms |
| XGo | LLGoDeadcodeDrop | 146497.8 ms | 143176.9 ms | 3320.8 ms | 53492.8 ms |
| XGo | LLGoNoLTO | 144956.1 ms | 142201.3 ms | 2754.9 ms | 52197.7 ms |
| Gorm_schema | LLGoDeadcodeDrop | 100053.7 ms | 98374.3 ms | 1679.4 ms | 33478.5 ms |
| Gorm_schema | LLGoNoLTO | 99037.6 ms | 97362.2 ms | 1675.4 ms | 33203.8 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 98849.6 ms | 97054.1 ms | 1795.5 ms | 59208.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 96430.7 ms | 94595.7 ms | 1835.0 ms | 56652.8 ms |
| Toml | LLGoNoLTO | 93166.1 ms | 91576.7 ms | 1589.4 ms | 31057.2 ms |
| Toml | LLGoDeadcodeDrop | 92097.6 ms | 90504.4 ms | 1593.2 ms | 30693.7 ms |
| Toml | LLGoFullLTONoGlobalDCE | 91645.8 ms | 89970.6 ms | 1675.2 ms | 53748.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 89213.6 ms | 87409.7 ms | 1803.9 ms | 47846.9 ms |
| Toml | LLGoFullLTOGlobalDCE | 82580.5 ms | 80929.5 ms | 1650.9 ms | 44564.5 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 82267.8 ms | 80638.2 ms | 1629.6 ms | 44272.7 ms |
| IXGo | Go | 77965.2 ms | 72605.3 ms | 5359.9 ms | 21485.8 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 65709.7 ms | 64485.3 ms | 1224.4 ms | 40704.1 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 64833.1 ms | 63750.8 ms | 1082.3 ms | 23473.4 ms |
| Dustin_humanize | LLGoNoLTO | 63690.5 ms | 62640.5 ms | 1050.0 ms | 23066.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 56812.1 ms | 55661.7 ms | 1150.4 ms | 31343.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 56188.5 ms | 54992.8 ms | 1195.7 ms | 31026.5 ms |
| Etcdctl | Go | 31491.6 ms | 29479.1 ms | 2012.4 ms | 9438.0 ms |
| XGo | Go | 17986.3 ms | 16879.9 ms | 1106.4 ms | 5173.2 ms |
| Aws_restjson | Go | 7413.5 ms | 6770.4 ms | 643.1 ms | 2881.0 ms |
| Gorm_schema | Go | 5510.6 ms | 5120.9 ms | 389.7 ms | 2132.2 ms |
| Uber_zap | Go | 5121.6 ms | 4716.4 ms | 405.2 ms | 1964.7 ms |
| K8s_workqueue | Go | 4389.9 ms | 4022.5 ms | 367.4 ms | 1542.1 ms |
| Toml | Go | 1919.7 ms | 1728.0 ms | 191.7 ms | 854.8 ms |
| Dustin_humanize | Go | 748.5 ms | 641.1 ms | 107.4 ms | 348.2 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2092353.6 ms | 1218626.9 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2052955.6 ms | 1153154.8 ms | 9 |
| LLGoFullLTOGlobalDCE | 2051471.6 ms | 1164052.8 ms | 9 |
| LLGoDeadcodeDrop | 1778647.8 ms | 590571.9 ms | 9 |
| LLGoNoLTO | 1774858.1 ms | 583094.7 ms | 9 |
| Go | 152547.0 ms | 45820.1 ms | 9 |

Dependency download details are in `download-timings.log`.
