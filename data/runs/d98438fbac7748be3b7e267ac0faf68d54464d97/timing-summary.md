## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 660788.5 ms | 653842.1 ms | 6946.4 ms | 444017.3 ms |
| IXGo | LLGoFullLTOGlobalDCE | 655717.2 ms | 648789.4 ms | 6927.8 ms | 438849.7 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 644861.5 ms | 638114.2 ms | 6747.3 ms | 435866.0 ms |
| IXGo | LLGoDeadcodeDrop | 412054.1 ms | 405797.6 ms | 6256.5 ms | 139618.3 ms |
| IXGo | LLGoNoLTO | 395094.6 ms | 389049.3 ms | 6045.3 ms | 133264.6 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 264117.1 ms | 258855.5 ms | 5261.6 ms | 163240.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 262164.9 ms | 257223.0 ms | 4941.8 ms | 162168.5 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 259689.2 ms | 254933.8 ms | 4755.4 ms | 162525.0 ms |
| Etcdctl | LLGoDeadcodeDrop | 188949.7 ms | 184534.9 ms | 4414.9 ms | 62817.4 ms |
| Etcdctl | LLGoNoLTO | 188484.5 ms | 183516.7 ms | 4967.7 ms | 63260.8 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 175362.5 ms | 172071.5 ms | 3291.0 ms | 124094.2 ms |
| XGo | LLGoFullLTONoGlobalDCE | 174914.5 ms | 171619.9 ms | 3294.6 ms | 124323.5 ms |
| XGo | LLGoFullLTOGlobalDCE | 174556.9 ms | 171164.7 ms | 3392.2 ms | 123821.1 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 138499.4 ms | 136118.8 ms | 2380.6 ms | 103299.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 126760.2 ms | 124288.3 ms | 2471.9 ms | 91477.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 126423.6 ms | 123974.0 ms | 2449.5 ms | 91168.4 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 108463.5 ms | 106668.8 ms | 1794.7 ms | 84445.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 105642.8 ms | 103854.9 ms | 1788.0 ms | 84254.4 ms |
| XGo | LLGoDeadcodeDrop | 102983.8 ms | 100112.3 ms | 2871.4 ms | 39338.7 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 102835.7 ms | 101038.9 ms | 1796.8 ms | 81677.9 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 100901.8 ms | 99124.5 ms | 1777.3 ms | 75429.4 ms |
| XGo | LLGoNoLTO | 100520.1 ms | 97676.6 ms | 2843.5 ms | 38011.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 99018.7 ms | 97289.6 ms | 1729.1 ms | 74685.1 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 90464.8 ms | 88645.5 ms | 1819.4 ms | 68702.1 ms |
| Aws_restjson | LLGoDeadcodeDrop | 81206.4 ms | 79180.2 ms | 2026.1 ms | 38750.8 ms |
| Aws_restjson | LLGoNoLTO | 79275.6 ms | 77053.8 ms | 2221.8 ms | 37468.6 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 62824.3 ms | 61439.7 ms | 1384.6 ms | 44598.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 62055.6 ms | 60638.5 ms | 1417.1 ms | 43969.6 ms |
| Uber_zap | LLGoDeadcodeDrop | 55081.3 ms | 53501.5 ms | 1579.8 ms | 24441.8 ms |
| Uber_zap | LLGoNoLTO | 53588.9 ms | 52060.8 ms | 1528.1 ms | 23933.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 53039.4 ms | 51651.0 ms | 1388.4 ms | 34156.7 ms |
| Toml | LLGoFullLTONoGlobalDCE | 50644.2 ms | 49596.3 ms | 1048.0 ms | 39612.5 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 47298.2 ms | 45718.0 ms | 1580.2 ms | 22273.0 ms |
| K8s_workqueue | LLGoNoLTO | 47216.1 ms | 45715.3 ms | 1500.8 ms | 22367.3 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 44172.2 ms | 43013.0 ms | 1159.2 ms | 32188.0 ms |
| Toml | LLGoFullLTOGlobalDCE | 43122.7 ms | 42024.0 ms | 1098.7 ms | 31806.2 ms |
| IXGo | Go | 42913.9 ms | 39809.3 ms | 3104.6 ms | 12311.2 ms |
| Gorm_schema | LLGoDeadcodeDrop | 36051.3 ms | 34857.7 ms | 1193.6 ms | 11855.3 ms |
| Gorm_schema | LLGoNoLTO | 35426.2 ms | 34215.2 ms | 1211.0 ms | 11623.3 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 33081.0 ms | 32192.9 ms | 888.1 ms | 25955.1 ms |
| Etcdctl | Go | 31882.7 ms | 29711.8 ms | 2171.0 ms | 9575.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 23972.6 ms | 23158.5 ms | 814.1 ms | 17282.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 23945.9 ms | 23125.0 ms | 820.9 ms | 17138.9 ms |
| Toml | LLGoDeadcodeDrop | 22442.5 ms | 21503.6 ms | 938.9 ms | 8542.4 ms |
| Toml | LLGoNoLTO | 21594.5 ms | 20605.3 ms | 989.2 ms | 8311.8 ms |
| XGo | Go | 18278.6 ms | 17038.0 ms | 1240.6 ms | 5356.4 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 12353.5 ms | 11630.1 ms | 723.4 ms | 5370.4 ms |
| Dustin_humanize | LLGoNoLTO | 12304.5 ms | 11591.1 ms | 713.4 ms | 5253.2 ms |
| Aws_restjson | Go | 7643.3 ms | 6898.8 ms | 744.4 ms | 3167.6 ms |
| Gorm_schema | Go | 5512.9 ms | 5117.3 ms | 395.6 ms | 2116.0 ms |
| Uber_zap | Go | 5121.5 ms | 4736.6 ms | 384.9 ms | 1983.2 ms |
| K8s_workqueue | Go | 4562.9 ms | 4063.6 ms | 499.3 ms | 1726.7 ms |
| Toml | Go | 1983.0 ms | 1717.5 ms | 265.5 ms | 944.5 ms |
| Dustin_humanize | Go | 781.7 ms | 639.6 ms | 142.1 ms | 365.3 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1575813.4 ms | 1102303.0 ms | 9 |
| LLGoFullLTOGlobalDCE | 1552674.9 ms | 1068005.2 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1539552.4 ms | 1050445.3 ms | 9 |
| LLGoDeadcodeDrop | 958420.9 ms | 353008.1 ms | 9 |
| LLGoNoLTO | 933505.0 ms | 343494.7 ms | 9 |
| Go | 118680.5 ms | 37546.0 ms | 9 |

Dependency download details are in `download-timings.log`.
