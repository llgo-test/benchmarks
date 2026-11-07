## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 856950.8 ms | 831318.5 ms | 25632.3 ms | 537873.3 ms |
| IXGo | LLGoFullLTOGlobalDCE | 838050.9 ms | 811738.0 ms | 26312.9 ms | 531261.7 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 823357.1 ms | 797351.5 ms | 26005.6 ms | 530524.4 ms |
| IXGo | LLGoDeadcodeDrop | 529601.9 ms | 502131.5 ms | 27470.4 ms | 163754.2 ms |
| IXGo | LLGoNoLTO | 499692.5 ms | 477332.2 ms | 22360.3 ms | 152057.6 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 462285.0 ms | 449693.7 ms | 12591.3 ms | 334415.8 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 449105.6 ms | 436776.9 ms | 12328.7 ms | 328129.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 437197.3 ms | 425083.3 ms | 12114.0 ms | 314436.2 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 353258.5 ms | 345530.0 ms | 7728.5 ms | 232026.3 ms |
| XGo | LLGoFullLTONoGlobalDCE | 331821.1 ms | 323394.5 ms | 8426.6 ms | 264094.1 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 307198.2 ms | 300066.0 ms | 7132.2 ms | 190268.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 298364.0 ms | 291377.6 ms | 6986.5 ms | 185582.0 ms |
| XGo | LLGoFullLTOGlobalDCE | 293067.4 ms | 284949.4 ms | 8118.0 ms | 225937.5 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 288960.0 ms | 280678.9 ms | 8281.1 ms | 220312.8 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 278497.7 ms | 272242.0 ms | 6255.7 ms | 190792.2 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 276856.4 ms | 270374.8 ms | 6481.6 ms | 190882.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 270675.7 ms | 264390.9 ms | 6284.8 ms | 185389.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 261629.7 ms | 255576.4 ms | 6053.3 ms | 170625.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 252348.1 ms | 246085.2 ms | 6262.9 ms | 165163.7 ms |
| Aws_restjson | LLGoDeadcodeDrop | 248258.3 ms | 242100.6 ms | 6157.8 ms | 76910.7 ms |
| Aws_restjson | LLGoNoLTO | 246691.4 ms | 240788.2 ms | 5903.2 ms | 75352.8 ms |
| Etcdctl | LLGoDeadcodeDrop | 238897.4 ms | 228146.0 ms | 10751.5 ms | 80192.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 233976.4 ms | 227908.0 ms | 6068.4 ms | 150009.2 ms |
| Etcdctl | LLGoNoLTO | 233817.2 ms | 224488.7 ms | 9328.5 ms | 77995.6 ms |
| Uber_zap | LLGoDeadcodeDrop | 206542.8 ms | 201167.8 ms | 5375.1 ms | 65605.6 ms |
| Uber_zap | LLGoNoLTO | 198065.6 ms | 193364.8 ms | 4700.8 ms | 61739.8 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 194705.5 ms | 189340.0 ms | 5365.4 ms | 62376.0 ms |
| K8s_workqueue | LLGoNoLTO | 192634.6 ms | 188081.7 ms | 4552.8 ms | 59646.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 149946.0 ms | 145965.4 ms | 3980.6 ms | 101477.6 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 149023.4 ms | 145127.9 ms | 3895.5 ms | 101504.8 ms |
| Toml | LLGoFullLTONoGlobalDCE | 136236.9 ms | 132698.3 ms | 3538.6 ms | 92594.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 128866.8 ms | 125145.4 ms | 3721.4 ms | 79659.0 ms |
| XGo | LLGoNoLTO | 128488.8 ms | 122493.5 ms | 5995.2 ms | 45858.7 ms |
| XGo | LLGoDeadcodeDrop | 128009.9 ms | 120754.2 ms | 7255.8 ms | 44996.8 ms |
| Toml | LLGoFullLTOGlobalDCE | 121967.7 ms | 118471.7 ms | 3496.1 ms | 77028.5 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 121729.8 ms | 118202.9 ms | 3526.9 ms | 76616.8 ms |
| Gorm_schema | LLGoDeadcodeDrop | 110392.9 ms | 107046.6 ms | 3346.3 ms | 37740.3 ms |
| Gorm_schema | LLGoNoLTO | 109174.0 ms | 106051.6 ms | 3122.4 ms | 36776.4 ms |
| Toml | LLGoDeadcodeDrop | 101456.8 ms | 98458.8 ms | 2998.0 ms | 34312.0 ms |
| Toml | LLGoNoLTO | 100967.5 ms | 98154.9 ms | 2812.5 ms | 33802.6 ms |
| IXGo | Go | 96872.0 ms | 82000.9 ms | 14871.0 ms | 26362.1 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 95217.5 ms | 92752.5 ms | 2465.0 ms | 67182.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 77626.0 ms | 75314.1 ms | 2312.0 ms | 48579.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 77207.4 ms | 74942.3 ms | 2265.1 ms | 48580.2 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 70710.9 ms | 68524.7 ms | 2186.2 ms | 25985.0 ms |
| Dustin_humanize | LLGoNoLTO | 69902.1 ms | 67972.0 ms | 1930.2 ms | 25368.3 ms |
| Etcdctl | Go | 37441.8 ms | 32276.7 ms | 5165.1 ms | 11289.1 ms |
| XGo | Go | 21784.8 ms | 18696.1 ms | 3088.7 ms | 6332.4 ms |
| Aws_restjson | Go | 9245.3 ms | 7746.7 ms | 1498.5 ms | 3773.7 ms |
| Gorm_schema | Go | 6728.9 ms | 5728.4 ms | 1000.5 ms | 2670.7 ms |
| Uber_zap | Go | 5990.6 ms | 5090.1 ms | 900.5 ms | 2419.9 ms |
| K8s_workqueue | Go | 5253.2 ms | 4306.5 ms | 946.7 ms | 1892.1 ms |
| Toml | Go | 2272.2 ms | 1881.5 ms | 390.6 ms | 1075.0 ms |
| Dustin_humanize | Go | 891.2 ms | 692.0 ms | 199.3 ms | 439.7 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2893374.2 ms | 1997731.3 ms | 9 |
| LLGoFullLTOGlobalDCE | 2764331.0 ms | 1854835.6 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2713716.5 ms | 1788381.9 ms | 9 |
| LLGoDeadcodeDrop | 1828576.5 ms | 591873.4 ms | 9 |
| LLGoNoLTO | 1779433.7 ms | 568597.9 ms | 9 |
| Go | 186480.0 ms | 56254.6 ms | 9 |

Dependency download details are in `download-timings.log`.
