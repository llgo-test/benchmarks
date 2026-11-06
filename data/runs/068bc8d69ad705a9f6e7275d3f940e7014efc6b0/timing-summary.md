## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| Etcdctl | LLGoFullLTONoGlobalDCE | 447165.8 ms | 435169.8 ms | 11996.0 ms | 314953.6 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 431983.5 ms | 419764.9 ms | 12218.6 ms | 307526.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 426415.3 ms | 414135.3 ms | 12279.9 ms | 304644.4 ms |
| XGo | LLGoFullLTONoGlobalDCE | 313517.5 ms | 305247.5 ms | 8270.0 ms | 246419.6 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 301970.4 ms | 295146.1 ms | 6824.2 ms | 201035.1 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 279109.0 ms | 271103.9 ms | 8005.1 ms | 209816.1 ms |
| XGo | LLGoFullLTOGlobalDCE | 276055.3 ms | 268330.1 ms | 7725.3 ms | 206961.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 271684.5 ms | 265256.2 ms | 6428.4 ms | 169579.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 269616.6 ms | 263026.8 ms | 6589.9 ms | 168296.9 ms |
| Etcdctl | LLGoDeadcodeDrop | 254903.6 ms | 244173.1 ms | 10730.5 ms | 83902.4 ms |
| Etcdctl | LLGoNoLTO | 253844.9 ms | 243874.4 ms | 9970.5 ms | 82757.1 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 251555.1 ms | 245749.8 ms | 5805.2 ms | 172934.9 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 242707.2 ms | 236773.1 ms | 5934.1 ms | 167825.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 242549.3 ms | 236818.2 ms | 5731.2 ms | 166817.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 230052.0 ms | 224513.9 ms | 5538.1 ms | 150890.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 228091.4 ms | 222452.0 ms | 5639.4 ms | 147629.5 ms |
| Aws_restjson | LLGoDeadcodeDrop | 227306.2 ms | 221706.5 ms | 5599.6 ms | 70434.2 ms |
| Aws_restjson | LLGoNoLTO | 220494.3 ms | 214977.5 ms | 5516.8 ms | 68621.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 207397.9 ms | 201938.6 ms | 5459.4 ms | 132436.0 ms |
| Uber_zap | LLGoDeadcodeDrop | 179487.8 ms | 174879.6 ms | 4608.3 ms | 57538.1 ms |
| Uber_zap | LLGoNoLTO | 178976.2 ms | 174494.3 ms | 4481.9 ms | 57045.0 ms |
| K8s_workqueue | LLGoNoLTO | 170181.4 ms | 165736.1 ms | 4445.3 ms | 54426.8 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 169879.8 ms | 165049.6 ms | 4830.2 ms | 55024.2 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 148562.0 ms | 144521.2 ms | 4040.8 ms | 101450.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 145808.4 ms | 141854.8 ms | 3953.7 ms | 98533.3 ms |
| Toml | LLGoFullLTONoGlobalDCE | 139083.7 ms | 135259.9 ms | 3823.8 ms | 94884.5 ms |
| XGo | LLGoNoLTO | 131303.8 ms | 125021.3 ms | 6282.6 ms | 46422.8 ms |
| XGo | LLGoDeadcodeDrop | 129203.1 ms | 122030.1 ms | 7173.0 ms | 45353.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 124291.8 ms | 120478.3 ms | 3813.6 ms | 76534.2 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 120761.9 ms | 117288.9 ms | 3473.0 ms | 76668.6 ms |
| Toml | LLGoFullLTOGlobalDCE | 120570.0 ms | 117172.6 ms | 3397.4 ms | 76772.0 ms |
| Gorm_schema | LLGoDeadcodeDrop | 112646.2 ms | 109146.3 ms | 3499.9 ms | 38624.8 ms |
| Gorm_schema | LLGoNoLTO | 112112.0 ms | 108798.9 ms | 3313.0 ms | 37786.0 ms |
| Toml | LLGoNoLTO | 103007.1 ms | 100114.5 ms | 2892.6 ms | 34668.6 ms |
| Toml | LLGoDeadcodeDrop | 102925.0 ms | 99876.5 ms | 3048.5 ms | 34810.2 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 98199.6 ms | 95655.4 ms | 2544.2 ms | 69750.2 ms |
| IXGo | Go | 97123.9 ms | 82253.6 ms | 14870.3 ms | 26425.9 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 80046.4 ms | 77670.0 ms | 2376.4 ms | 50654.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 77875.7 ms | 75483.7 ms | 2391.9 ms | 49242.7 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 71048.9 ms | 68851.9 ms | 2197.0 ms | 26132.5 ms |
| Dustin_humanize | LLGoNoLTO | 70638.9 ms | 68553.1 ms | 2085.8 ms | 25769.9 ms |
| Etcdctl | Go | 38195.6 ms | 32951.9 ms | 5243.7 ms | 11520.4 ms |
| XGo | Go | 21884.3 ms | 18825.5 ms | 3058.8 ms | 6338.7 ms |
| Aws_restjson | Go | 9182.4 ms | 7633.1 ms | 1549.3 ms | 3827.3 ms |
| Gorm_schema | Go | 6755.0 ms | 5792.8 ms | 962.2 ms | 2647.7 ms |
| Uber_zap | Go | 5907.5 ms | 5044.5 ms | 863.0 ms | 2357.4 ms |
| K8s_workqueue | Go | 5278.4 ms | 4427.2 ms | 851.2 ms | 1853.7 ms |
| Toml | Go | 2275.3 ms | 1886.2 ms | 389.0 ms | 1079.9 ms |
| Dustin_humanize | Go | 899.9 ms | 676.2 ms | 223.7 ms | 432.3 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1942761.3 ms | 1369253.7 ms | 8 |
| LLGoFullLTOGlobalDCE | 1791010.5 ms | 1223441.3 ms | 8 |
| LLGoFullLTOGlobalDCEPlugin | 1741298.5 ms | 1169561.5 ms | 8 |
| LLGoDeadcodeDrop | 1247400.5 ms | 411819.9 ms | 8 |
| LLGoNoLTO | 1240558.5 ms | 407497.8 ms | 8 |
| Go | 187502.5 ms | 56483.2 ms | 9 |

Dependency download details are in `download-timings.log`.
