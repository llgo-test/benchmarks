## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 662620.9 ms | 639417.1 ms | 23203.8 ms | 438583.6 ms |
| IXGo | LLGoFullLTOGlobalDCE | 647907.4 ms | 624609.8 ms | 23297.7 ms | 428279.7 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 644501.0 ms | 621231.0 ms | 23270.0 ms | 425696.2 ms |
| IXGo | LLGoDeadcodeDrop | 368054.3 ms | 344897.6 ms | 23156.7 ms | 118027.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 358026.0 ms | 347006.2 ms | 11019.9 ms | 264926.3 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 355532.2 ms | 344507.4 ms | 11024.8 ms | 265120.5 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 355346.5 ms | 344206.7 ms | 11139.8 ms | 263071.7 ms |
| IXGo | LLGoNoLTO | 354007.3 ms | 334707.6 ms | 19299.7 ms | 110178.1 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 268246.9 ms | 261609.3 ms | 6637.6 ms | 180803.7 ms |
| XGo | LLGoFullLTONoGlobalDCE | 263603.3 ms | 255890.2 ms | 7713.1 ms | 212985.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 239610.8 ms | 233350.1 ms | 6260.7 ms | 155297.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 239536.1 ms | 233085.4 ms | 6450.7 ms | 156000.0 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 234089.3 ms | 226903.1 ms | 7186.2 ms | 182360.2 ms |
| XGo | LLGoFullLTOGlobalDCE | 233685.5 ms | 226352.2 ms | 7333.3 ms | 182449.8 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 222503.2 ms | 216849.0 ms | 5654.2 ms | 157341.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 215911.6 ms | 210202.3 ms | 5709.3 ms | 152381.2 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 215287.8 ms | 209662.2 ms | 5625.6 ms | 152937.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 207850.9 ms | 202326.0 ms | 5524.9 ms | 141371.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 202381.8 ms | 196797.9 ms | 5583.9 ms | 136688.9 ms |
| Aws_restjson | LLGoNoLTO | 190533.0 ms | 185438.3 ms | 5094.6 ms | 59295.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 188722.1 ms | 183240.1 ms | 5482.0 ms | 126359.1 ms |
| Aws_restjson | LLGoDeadcodeDrop | 183168.7 ms | 177737.0 ms | 5431.7 ms | 58408.6 ms |
| Etcdctl | LLGoDeadcodeDrop | 178404.5 ms | 169267.0 ms | 9137.5 ms | 62400.9 ms |
| Etcdctl | LLGoNoLTO | 177344.2 ms | 168856.6 ms | 8487.6 ms | 61111.8 ms |
| Uber_zap | LLGoNoLTO | 151757.4 ms | 147582.0 ms | 4175.4 ms | 48438.3 ms |
| Uber_zap | LLGoDeadcodeDrop | 151062.0 ms | 146426.3 ms | 4635.8 ms | 49597.4 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 144911.1 ms | 140309.8 ms | 4601.3 ms | 47797.5 ms |
| K8s_workqueue | LLGoNoLTO | 144688.3 ms | 140624.7 ms | 4063.7 ms | 46092.7 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 113082.7 ms | 109652.2 ms | 3430.5 ms | 78595.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 112828.0 ms | 109322.1 ms | 3505.9 ms | 77201.0 ms |
| Toml | LLGoFullLTONoGlobalDCE | 106697.8 ms | 103436.5 ms | 3261.3 ms | 73227.2 ms |
| XGo | LLGoNoLTO | 100661.1 ms | 95124.5 ms | 5536.6 ms | 37379.0 ms |
| XGo | LLGoDeadcodeDrop | 99893.1 ms | 93565.0 ms | 6328.1 ms | 37278.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 95345.1 ms | 92083.6 ms | 3261.5 ms | 59662.3 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 94296.2 ms | 91179.6 ms | 3116.6 ms | 60052.2 ms |
| Toml | LLGoFullLTOGlobalDCE | 93456.0 ms | 90423.0 ms | 3033.0 ms | 60044.1 ms |
| Gorm_schema | LLGoDeadcodeDrop | 83840.0 ms | 80617.5 ms | 3222.4 ms | 29689.5 ms |
| Gorm_schema | LLGoNoLTO | 81850.0 ms | 78968.1 ms | 2881.9 ms | 28584.0 ms |
| Toml | LLGoDeadcodeDrop | 78250.6 ms | 75444.9 ms | 2805.7 ms | 27475.4 ms |
| Toml | LLGoNoLTO | 77496.2 ms | 74925.4 ms | 2570.8 ms | 26779.7 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 74170.5 ms | 71848.3 ms | 2322.2 ms | 53066.4 ms |
| IXGo | Go | 72093.5 ms | 59495.1 ms | 12598.4 ms | 20302.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 60137.8 ms | 58021.0 ms | 2116.8 ms | 38596.5 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 59535.9 ms | 57510.5 ms | 2025.4 ms | 38379.4 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 53357.9 ms | 51418.8 ms | 1939.1 ms | 20551.0 ms |
| Dustin_humanize | LLGoNoLTO | 52957.3 ms | 51143.0 ms | 1814.4 ms | 19943.9 ms |
| Etcdctl | Go | 28364.7 ms | 23834.9 ms | 4529.8 ms | 8570.3 ms |
| XGo | Go | 16249.1 ms | 13634.0 ms | 2615.1 ms | 4885.6 ms |
| Aws_restjson | Go | 6833.9 ms | 5532.2 ms | 1301.7 ms | 2867.9 ms |
| Gorm_schema | Go | 4929.8 ms | 4073.2 ms | 856.6 ms | 1946.5 ms |
| Uber_zap | Go | 4527.3 ms | 3770.8 ms | 756.5 ms | 1849.9 ms |
| K8s_workqueue | Go | 3975.5 ms | 3196.9 ms | 778.6 ms | 1649.0 ms |
| Toml | Go | 1716.1 ms | 1374.4 ms | 341.7 ms | 825.8 ms |
| Dustin_humanize | Go | 694.1 ms | 503.5 ms | 190.6 ms | 347.2 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2263625.5 ms | 1599774.3 ms | 9 |
| LLGoFullLTOGlobalDCE | 2166659.7 ms | 1499395.1 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2134628.2 ms | 1462309.7 ms | 9 |
| LLGoDeadcodeDrop | 1340942.1 ms | 451227.0 ms | 9 |
| LLGoNoLTO | 1331295.0 ms | 437802.9 ms | 9 |
| Go | 139384.1 ms | 43244.8 ms | 9 |

Dependency download details are in `download-timings.log`.
