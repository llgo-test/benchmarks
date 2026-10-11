## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 558650.0 ms | 549069.2 ms | 9580.9 ms | 285145.7 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 498671.5 ms | 489321.4 ms | 9350.1 ms | 269355.8 ms |
| IXGo | LLGoFullLTOGlobalDCE | 495993.2 ms | 485699.6 ms | 10293.6 ms | 265397.5 ms |
| IXGo | LLGoNoLTO | 400497.5 ms | 392436.2 ms | 8061.3 ms | 115667.3 ms |
| IXGo | LLGoDeadcodeDrop | 369589.1 ms | 358433.6 ms | 11155.5 ms | 111878.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 230996.8 ms | 226365.4 ms | 4631.4 ms | 149670.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 229415.7 ms | 225080.7 ms | 4335.0 ms | 148252.1 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 226602.4 ms | 222396.2 ms | 4206.1 ms | 147914.5 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 182964.5 ms | 179753.5 ms | 3211.0 ms | 113212.7 ms |
| Aws_restjson | LLGoDeadcodeDrop | 174725.1 ms | 171751.1 ms | 2974.0 ms | 63103.5 ms |
| Aws_restjson | LLGoNoLTO | 170542.0 ms | 167572.3 ms | 2969.7 ms | 61301.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 168743.9 ms | 165479.0 ms | 3264.8 ms | 99311.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 167554.3 ms | 164398.4 ms | 3155.9 ms | 99512.9 ms |
| XGo | LLGoFullLTONoGlobalDCE | 164041.9 ms | 161060.1 ms | 2981.9 ms | 119979.5 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 163336.6 ms | 160361.0 ms | 2975.6 ms | 118320.5 ms |
| XGo | LLGoFullLTOGlobalDCE | 161427.6 ms | 158459.4 ms | 2968.1 ms | 117212.3 ms |
| Etcdctl | LLGoDeadcodeDrop | 161136.4 ms | 156665.5 ms | 4470.9 ms | 55841.5 ms |
| Etcdctl | LLGoNoLTO | 158459.3 ms | 154750.1 ms | 3709.2 ms | 53405.1 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 150109.9 ms | 147372.7 ms | 2737.2 ms | 97948.4 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 145013.7 ms | 142150.9 ms | 2862.8 ms | 96001.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 144718.4 ms | 141906.7 ms | 2811.7 ms | 94739.3 ms |
| Uber_zap | LLGoDeadcodeDrop | 142418.6 ms | 139970.1 ms | 2448.5 ms | 54814.1 ms |
| Uber_zap | LLGoNoLTO | 141695.1 ms | 139321.2 ms | 2373.9 ms | 54721.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 141545.1 ms | 138710.0 ms | 2835.1 ms | 88393.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 141455.9 ms | 138779.3 ms | 2676.6 ms | 88831.5 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 141102.6 ms | 138540.7 ms | 2561.8 ms | 54337.1 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 136695.4 ms | 133883.9 ms | 2811.5 ms | 86193.1 ms |
| K8s_workqueue | LLGoNoLTO | 135855.8 ms | 133361.2 ms | 2494.5 ms | 52560.4 ms |
| XGo | LLGoDeadcodeDrop | 92407.2 ms | 89411.7 ms | 2995.5 ms | 36420.8 ms |
| XGo | LLGoNoLTO | 90749.4 ms | 88396.9 ms | 2352.5 ms | 34371.5 ms |
| Gorm_schema | LLGoDeadcodeDrop | 74956.7 ms | 73352.4 ms | 1604.2 ms | 25085.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 74934.2 ms | 73099.5 ms | 1834.7 ms | 45715.3 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 74850.9 ms | 73166.4 ms | 1684.5 ms | 46233.7 ms |
| Gorm_schema | LLGoNoLTO | 72851.2 ms | 71285.4 ms | 1565.8 ms | 24428.4 ms |
| Toml | LLGoDeadcodeDrop | 69408.2 ms | 67768.3 ms | 1639.9 ms | 23225.0 ms |
| Toml | LLGoFullLTONoGlobalDCE | 69295.8 ms | 67519.2 ms | 1776.7 ms | 42655.9 ms |
| Toml | LLGoNoLTO | 68415.4 ms | 66665.9 ms | 1749.5 ms | 23115.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 66817.5 ms | 65122.8 ms | 1694.7 ms | 37165.2 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 62810.0 ms | 61032.4 ms | 1777.6 ms | 35247.4 ms |
| Toml | LLGoFullLTOGlobalDCE | 62672.0 ms | 60845.4 ms | 1826.6 ms | 34888.5 ms |
| IXGo | Go | 61895.5 ms | 57714.9 ms | 4180.6 ms | 17676.4 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 48583.0 ms | 47303.1 ms | 1279.9 ms | 31375.9 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 47498.8 ms | 46362.2 ms | 1136.5 ms | 17299.5 ms |
| Dustin_humanize | LLGoNoLTO | 47019.5 ms | 45911.3 ms | 1108.2 ms | 17144.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 41042.0 ms | 39857.3 ms | 1184.7 ms | 23400.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 40639.6 ms | 39422.8 ms | 1216.8 ms | 23246.6 ms |
| Etcdctl | Go | 24857.3 ms | 23251.7 ms | 1605.5 ms | 7503.1 ms |
| XGo | Go | 14553.5 ms | 13494.5 ms | 1059.1 ms | 4365.2 ms |
| Aws_restjson | Go | 5970.7 ms | 5404.4 ms | 566.3 ms | 2478.1 ms |
| Gorm_schema | Go | 4328.3 ms | 3971.0 ms | 357.4 ms | 1867.8 ms |
| Uber_zap | Go | 3952.3 ms | 3616.1 ms | 336.2 ms | 1569.6 ms |
| K8s_workqueue | Go | 3498.8 ms | 3144.7 ms | 354.1 ms | 1265.4 ms |
| Toml | Go | 1536.2 ms | 1341.4 ms | 194.8 ms | 703.7 ms |
| Dustin_humanize | Go | 670.7 ms | 528.6 ms | 142.0 ms | 352.7 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTOGlobalDCEPlugin | 1570548.2 ms | 923284.8 ms | 9 |
| LLGoFullLTONoGlobalDCE | 1560133.6 ms | 964678.0 ms | 9 |
| LLGoFullLTOGlobalDCE | 1518900.0 ms | 917357.6 ms | 9 |
| LLGoNoLTO | 1286085.2 ms | 436714.7 ms | 9 |
| LLGoDeadcodeDrop | 1273242.6 ms | 442004.6 ms | 9 |
| Go | 121263.2 ms | 37781.9 ms | 9 |

Dependency download details are in `download-timings.log`.
