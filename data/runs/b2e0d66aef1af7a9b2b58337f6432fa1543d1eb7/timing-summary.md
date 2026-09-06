## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 614752.1 ms | 608267.6 ms | 6484.6 ms | 394475.3 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 609594.0 ms | 603288.2 ms | 6305.8 ms | 391505.2 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 608524.9 ms | 602357.6 ms | 6167.2 ms | 390413.5 ms |
| IXGo | LLGoDeadcodeDrop | 393469.8 ms | 388060.7 ms | 5409.1 ms | 129205.6 ms |
| IXGo | LLGoNoLTO | 392819.8 ms | 387220.7 ms | 5599.1 ms | 130071.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 268888.2 ms | 264409.4 ms | 4478.8 ms | 163405.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 266371.0 ms | 261942.5 ms | 4428.5 ms | 161101.9 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 263899.8 ms | 259431.3 ms | 4468.5 ms | 161614.6 ms |
| Etcdctl | LLGoDeadcodeDrop | 197871.6 ms | 193722.2 ms | 4149.4 ms | 66020.5 ms |
| Etcdctl | LLGoNoLTO | 194451.3 ms | 190631.6 ms | 3819.7 ms | 64468.3 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 179039.1 ms | 176031.2 ms | 3007.9 ms | 124375.5 ms |
| XGo | LLGoFullLTOGlobalDCE | 177995.9 ms | 175033.4 ms | 2962.6 ms | 123551.8 ms |
| XGo | LLGoFullLTONoGlobalDCE | 177026.3 ms | 174076.3 ms | 2950.0 ms | 124674.7 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 139894.4 ms | 137645.4 ms | 2249.1 ms | 102682.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 129197.9 ms | 126932.1 ms | 2265.8 ms | 91082.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 127097.5 ms | 124897.1 ms | 2200.4 ms | 90098.7 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 110955.7 ms | 109299.1 ms | 1656.5 ms | 85426.5 ms |
| XGo | LLGoDeadcodeDrop | 107769.4 ms | 105127.4 ms | 2642.0 ms | 40844.8 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 106772.5 ms | 105074.9 ms | 1697.6 ms | 83813.9 ms |
| XGo | LLGoNoLTO | 105556.3 ms | 103019.0 ms | 2537.3 ms | 39508.3 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 104791.8 ms | 103106.2 ms | 1685.6 ms | 82273.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 103242.2 ms | 101606.6 ms | 1635.6 ms | 77151.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 102377.5 ms | 100673.4 ms | 1704.1 ms | 75988.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 92821.8 ms | 91203.0 ms | 1618.9 ms | 69748.1 ms |
| Aws_restjson | LLGoDeadcodeDrop | 82475.0 ms | 80579.1 ms | 1895.9 ms | 37783.7 ms |
| Aws_restjson | LLGoNoLTO | 81743.9 ms | 79840.6 ms | 1903.3 ms | 37518.7 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 65204.6 ms | 64057.8 ms | 1146.8 ms | 45766.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 64143.4 ms | 62804.5 ms | 1338.8 ms | 44945.8 ms |
| Uber_zap | LLGoDeadcodeDrop | 57448.3 ms | 56084.4 ms | 1363.9 ms | 25140.7 ms |
| Uber_zap | LLGoNoLTO | 56023.3 ms | 54732.9 ms | 1290.4 ms | 24697.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 55077.9 ms | 53804.1 ms | 1273.9 ms | 35125.5 ms |
| Toml | LLGoFullLTONoGlobalDCE | 52386.3 ms | 51338.5 ms | 1047.8 ms | 40577.6 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 49584.5 ms | 48182.7 ms | 1401.8 ms | 22927.9 ms |
| K8s_workqueue | LLGoNoLTO | 48908.7 ms | 47551.5 ms | 1357.1 ms | 22701.8 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 45720.3 ms | 44710.5 ms | 1009.8 ms | 33114.1 ms |
| Toml | LLGoFullLTOGlobalDCE | 44690.5 ms | 43700.1 ms | 990.4 ms | 32876.3 ms |
| IXGo | Go | 44457.9 ms | 41608.5 ms | 2849.4 ms | 12763.5 ms |
| Gorm_schema | LLGoDeadcodeDrop | 37792.9 ms | 36671.1 ms | 1121.8 ms | 12312.9 ms |
| Gorm_schema | LLGoNoLTO | 37375.5 ms | 36302.2 ms | 1073.3 ms | 12081.2 ms |
| Etcdctl | Go | 32791.8 ms | 30817.2 ms | 1974.7 ms | 9836.8 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 32640.3 ms | 31889.7 ms | 750.6 ms | 25542.5 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 24497.9 ms | 23698.4 ms | 799.5 ms | 17158.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 24317.2 ms | 23518.7 ms | 798.5 ms | 17177.4 ms |
| Toml | LLGoDeadcodeDrop | 23954.9 ms | 22992.2 ms | 962.7 ms | 8836.5 ms |
| Toml | LLGoNoLTO | 22728.7 ms | 21865.5 ms | 863.2 ms | 8567.4 ms |
| XGo | Go | 18919.2 ms | 17809.3 ms | 1109.9 ms | 5580.9 ms |
| Dustin_humanize | LLGoNoLTO | 13073.5 ms | 12399.6 ms | 673.9 ms | 5467.4 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 12926.3 ms | 12212.9 ms | 713.4 ms | 5462.4 ms |
| Aws_restjson | Go | 7872.3 ms | 7233.6 ms | 638.7 ms | 3181.4 ms |
| Gorm_schema | Go | 5630.8 ms | 5287.2 ms | 343.6 ms | 2156.4 ms |
| Uber_zap | Go | 5184.6 ms | 4816.0 ms | 368.6 ms | 2030.3 ms |
| K8s_workqueue | Go | 4651.4 ms | 4229.9 ms | 421.5 ms | 1665.9 ms |
| Toml | Go | 1985.9 ms | 1771.3 ms | 214.6 ms | 899.7 ms |
| Dustin_humanize | Go | 786.4 ms | 639.7 ms | 146.7 ms | 363.5 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1555324.2 ms | 1058971.7 ms | 9 |
| LLGoFullLTOGlobalDCE | 1529382.4 ms | 1025192.6 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1507214.8 ms | 1001504.2 ms | 9 |
| LLGoDeadcodeDrop | 963292.9 ms | 348535.0 ms | 9 |
| LLGoNoLTO | 952680.9 ms | 345081.6 ms | 9 |
| Go | 122280.4 ms | 38478.3 ms | 9 |

Dependency download details are in `download-timings.log`.
