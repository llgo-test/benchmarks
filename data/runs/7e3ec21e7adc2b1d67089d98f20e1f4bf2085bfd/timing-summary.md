## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 667271.1 ms | 654251.8 ms | 13019.3 ms | 345291.2 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 645025.9 ms | 631860.3 ms | 13165.6 ms | 326922.1 ms |
| IXGo | LLGoDeadcodeDrop | 546482.7 ms | 535822.1 ms | 10660.5 ms | 168038.4 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 538149.5 ms | 526567.7 ms | 11581.8 ms | 286925.0 ms |
| IXGo | LLGoNoLTO | 487387.7 ms | 477439.0 ms | 9948.7 ms | 143892.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 263699.5 ms | 258777.6 ms | 4921.9 ms | 162561.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 262912.6 ms | 258245.7 ms | 4666.9 ms | 162059.9 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 258389.4 ms | 253929.4 ms | 4460.0 ms | 160223.2 ms |
| Etcdctl | LLGoDeadcodeDrop | 196027.1 ms | 191462.4 ms | 4564.8 ms | 64360.0 ms |
| Etcdctl | LLGoNoLTO | 195517.8 ms | 190792.2 ms | 4725.5 ms | 64269.0 ms |
| XGo | LLGoFullLTOGlobalDCE | 193092.7 ms | 189479.9 ms | 3612.8 ms | 134116.2 ms |
| XGo | LLGoFullLTONoGlobalDCE | 184362.7 ms | 180709.8 ms | 3652.9 ms | 128221.9 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 183721.5 ms | 180380.8 ms | 3340.7 ms | 126919.9 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 140328.0 ms | 137707.5 ms | 2620.5 ms | 103330.1 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 134496.2 ms | 132000.8 ms | 2495.5 ms | 93923.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 130302.4 ms | 127793.1 ms | 2509.3 ms | 90899.9 ms |
| XGo | LLGoDeadcodeDrop | 117954.8 ms | 114653.6 ms | 3301.2 ms | 43000.0 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 110699.6 ms | 108829.4 ms | 1870.2 ms | 84066.5 ms |
| XGo | LLGoNoLTO | 109957.8 ms | 107084.5 ms | 2873.3 ms | 40416.4 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 108361.2 ms | 106452.8 ms | 1908.4 ms | 84228.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 106966.9 ms | 104891.5 ms | 2075.4 ms | 83560.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 103633.8 ms | 101502.3 ms | 2131.5 ms | 75456.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 101181.1 ms | 99323.7 ms | 1857.4 ms | 73745.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 91942.7 ms | 90035.5 ms | 1907.2 ms | 67907.2 ms |
| Aws_restjson | LLGoDeadcodeDrop | 91623.4 ms | 89434.3 ms | 2189.1 ms | 44306.9 ms |
| Aws_restjson | LLGoNoLTO | 87359.8 ms | 85041.0 ms | 2318.7 ms | 40360.4 ms |
| IXGo | Go | 84737.7 ms | 79504.9 ms | 5232.7 ms | 23938.1 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 66514.4 ms | 65107.8 ms | 1406.6 ms | 46163.1 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 64056.4 ms | 62654.0 ms | 1402.4 ms | 42949.0 ms |
| Uber_zap | LLGoDeadcodeDrop | 58915.9 ms | 57336.7 ms | 1579.2 ms | 25053.0 ms |
| Uber_zap | LLGoNoLTO | 56916.9 ms | 55312.4 ms | 1604.5 ms | 24490.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 55100.8 ms | 53716.0 ms | 1384.8 ms | 33823.6 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 51420.6 ms | 49825.5 ms | 1595.1 ms | 22881.9 ms |
| Toml | LLGoFullLTONoGlobalDCE | 50155.2 ms | 49006.4 ms | 1148.8 ms | 37864.4 ms |
| K8s_workqueue | LLGoNoLTO | 49961.9 ms | 48400.3 ms | 1561.7 ms | 22279.6 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 44518.3 ms | 43387.9 ms | 1130.4 ms | 31560.1 ms |
| Toml | LLGoFullLTOGlobalDCE | 42234.8 ms | 41128.6 ms | 1106.2 ms | 29533.0 ms |
| Gorm_schema | LLGoDeadcodeDrop | 41406.6 ms | 40199.3 ms | 1207.3 ms | 13853.0 ms |
| Gorm_schema | LLGoNoLTO | 40827.8 ms | 39563.1 ms | 1264.7 ms | 13762.3 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 36140.6 ms | 35236.4 ms | 904.2 ms | 28192.2 ms |
| Etcdctl | Go | 34770.7 ms | 32624.3 ms | 2146.4 ms | 10393.5 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 27504.3 ms | 26629.2 ms | 875.1 ms | 19307.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 26863.6 ms | 25980.5 ms | 883.2 ms | 18807.4 ms |
| Toml | LLGoDeadcodeDrop | 24931.4 ms | 23954.2 ms | 977.2 ms | 9388.5 ms |
| Toml | LLGoNoLTO | 24659.4 ms | 23690.7 ms | 968.7 ms | 9336.1 ms |
| XGo | Go | 20116.9 ms | 18880.7 ms | 1236.2 ms | 5978.4 ms |
| Dustin_humanize | LLGoNoLTO | 14616.6 ms | 13834.9 ms | 781.7 ms | 6121.0 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 14572.3 ms | 13741.9 ms | 830.4 ms | 6217.4 ms |
| Aws_restjson | Go | 8285.7 ms | 7413.9 ms | 871.8 ms | 3822.1 ms |
| Gorm_schema | Go | 6051.6 ms | 5544.4 ms | 507.1 ms | 2605.9 ms |
| Uber_zap | Go | 5479.6 ms | 5057.5 ms | 422.1 ms | 2143.6 ms |
| K8s_workqueue | Go | 4864.2 ms | 4404.2 ms | 460.0 ms | 1718.3 ms |
| Toml | Go | 2057.1 ms | 1826.2 ms | 231.0 ms | 969.7 ms |
| Dustin_humanize | Go | 905.1 ms | 704.5 ms | 200.6 ms | 604.1 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTOGlobalDCE | 1595668.5 ms | 981463.2 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1548856.0 ms | 937879.9 ms | 9 |
| LLGoFullLTONoGlobalDCE | 1493100.8 ms | 959215.1 ms | 9 |
| LLGoDeadcodeDrop | 1143334.7 ms | 397099.2 ms | 9 |
| LLGoNoLTO | 1067205.6 ms | 364927.8 ms | 9 |
| Go | 167268.6 ms | 52173.8 ms | 9 |

Dependency download details are in `download-timings.log`.
