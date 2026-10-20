## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 859004.2 ms | 846099.1 ms | 12905.2 ms | 543438.6 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 842288.1 ms | 828971.4 ms | 13316.7 ms | 539748.1 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 839948.0 ms | 827646.4 ms | 12301.6 ms | 542336.5 ms |
| IXGo | LLGoDeadcodeDrop | 513784.8 ms | 499484.5 ms | 14300.3 ms | 161759.0 ms |
| IXGo | LLGoNoLTO | 507037.7 ms | 497868.5 ms | 9169.2 ms | 155859.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 429547.0 ms | 423883.8 ms | 5663.2 ms | 315312.3 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 426909.0 ms | 421177.1 ms | 5732.0 ms | 318063.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 425192.0 ms | 419302.8 ms | 5889.3 ms | 312554.1 ms |
| XGo | LLGoFullLTONoGlobalDCE | 322122.3 ms | 317786.8 ms | 4335.6 ms | 260098.7 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 320647.8 ms | 316603.5 ms | 4044.3 ms | 223840.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 290090.6 ms | 286322.6 ms | 3768.0 ms | 191455.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 289834.8 ms | 286073.9 ms | 3760.8 ms | 191467.4 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 282643.9 ms | 278585.0 ms | 4058.9 ms | 219584.8 ms |
| XGo | LLGoFullLTOGlobalDCE | 280873.1 ms | 277028.0 ms | 3845.0 ms | 218175.7 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 273851.9 ms | 270520.9 ms | 3331.1 ms | 198359.7 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 266112.2 ms | 262587.7 ms | 3524.5 ms | 192855.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 264899.9 ms | 261354.2 ms | 3545.6 ms | 191739.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 249220.4 ms | 245891.1 ms | 3329.2 ms | 171802.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 247631.4 ms | 244387.4 ms | 3244.0 ms | 171280.0 ms |
| Aws_restjson | LLGoNoLTO | 236173.4 ms | 233116.2 ms | 3057.2 ms | 82593.4 ms |
| Aws_restjson | LLGoDeadcodeDrop | 235446.7 ms | 231987.0 ms | 3459.7 ms | 82770.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 231840.4 ms | 228532.6 ms | 3307.8 ms | 158396.4 ms |
| Etcdctl | LLGoDeadcodeDrop | 225035.4 ms | 219731.4 ms | 5304.0 ms | 80181.5 ms |
| Etcdctl | LLGoNoLTO | 223196.5 ms | 218895.8 ms | 4300.6 ms | 78384.2 ms |
| Uber_zap | LLGoNoLTO | 196399.5 ms | 193922.5 ms | 2477.0 ms | 73249.4 ms |
| Uber_zap | LLGoDeadcodeDrop | 196092.2 ms | 193275.9 ms | 2816.3 ms | 73441.1 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 189311.4 ms | 186425.3 ms | 2886.1 ms | 71884.0 ms |
| K8s_workqueue | LLGoNoLTO | 189095.3 ms | 186404.6 ms | 2690.8 ms | 70599.0 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 142125.2 ms | 139986.1 ms | 2139.2 ms | 100052.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 140286.8 ms | 138184.0 ms | 2102.8 ms | 98134.6 ms |
| Toml | LLGoFullLTONoGlobalDCE | 129612.6 ms | 127288.3 ms | 2324.4 ms | 90511.7 ms |
| XGo | LLGoNoLTO | 127974.8 ms | 125140.6 ms | 2834.2 ms | 50054.7 ms |
| XGo | LLGoDeadcodeDrop | 127244.0 ms | 123645.7 ms | 3598.2 ms | 48735.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 116000.3 ms | 114038.2 ms | 1962.1 ms | 73269.0 ms |
| Toml | LLGoFullLTOGlobalDCE | 111280.4 ms | 109289.8 ms | 1990.6 ms | 71359.8 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 111277.9 ms | 109219.7 ms | 2058.2 ms | 71600.1 ms |
| Gorm_schema | LLGoDeadcodeDrop | 104877.5 ms | 102885.2 ms | 1992.3 ms | 35329.2 ms |
| Gorm_schema | LLGoNoLTO | 103292.3 ms | 101643.4 ms | 1649.0 ms | 34530.6 ms |
| Toml | LLGoDeadcodeDrop | 97919.1 ms | 95913.8 ms | 2005.3 ms | 32712.9 ms |
| Toml | LLGoNoLTO | 97564.6 ms | 95719.1 ms | 1845.5 ms | 32275.9 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 93377.5 ms | 91762.1 ms | 1615.4 ms | 67936.6 ms |
| IXGo | Go | 83204.1 ms | 78276.8 ms | 4927.3 ms | 22932.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 73125.3 ms | 71653.7 ms | 1471.7 ms | 47245.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 72934.1 ms | 71514.5 ms | 1419.5 ms | 47301.4 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 66929.5 ms | 65565.8 ms | 1363.7 ms | 24176.0 ms |
| Dustin_humanize | LLGoNoLTO | 66826.6 ms | 65562.1 ms | 1264.5 ms | 23866.2 ms |
| Etcdctl | Go | 33326.6 ms | 31246.6 ms | 2080.0 ms | 10245.4 ms |
| XGo | Go | 18868.1 ms | 17707.3 ms | 1160.8 ms | 5588.6 ms |
| Aws_restjson | Go | 7893.7 ms | 7187.2 ms | 706.5 ms | 3238.4 ms |
| Gorm_schema | Go | 5746.7 ms | 5366.9 ms | 379.8 ms | 2166.8 ms |
| Uber_zap | Go | 5308.2 ms | 4910.8 ms | 397.4 ms | 2047.6 ms |
| K8s_workqueue | Go | 4694.1 ms | 4244.2 ms | 449.9 ms | 1674.7 ms |
| Toml | Go | 2026.4 ms | 1800.9 ms | 225.4 ms | 930.1 ms |
| Dustin_humanize | Go | 794.1 ms | 659.5 ms | 134.6 ms | 389.1 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2817046.7 ms | 1991465.9 ms | 9 |
| LLGoFullLTOGlobalDCE | 2691936.7 ms | 1845451.0 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2623693.8 ms | 1791002.6 ms | 9 |
| LLGoDeadcodeDrop | 1756640.5 ms | 610989.6 ms | 9 |
| LLGoNoLTO | 1747560.7 ms | 601413.2 ms | 9 |
| Go | 161862.0 ms | 49213.3 ms | 9 |

Dependency download details are in `download-timings.log`.
