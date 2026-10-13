## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 619418.5 ms | 608689.7 ms | 10728.8 ms | 325690.5 ms |
| IXGo | LLGoFullLTOGlobalDCE | 614847.2 ms | 604095.2 ms | 10752.0 ms | 323548.6 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 603984.9 ms | 593004.2 ms | 10980.7 ms | 320612.7 ms |
| IXGo | LLGoDeadcodeDrop | 485285.7 ms | 472236.1 ms | 13049.6 ms | 144202.8 ms |
| IXGo | LLGoNoLTO | 479096.5 ms | 469918.8 ms | 9177.8 ms | 139936.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 298974.7 ms | 294013.0 ms | 4961.6 ms | 186629.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 292758.6 ms | 287976.8 ms | 4781.8 ms | 181665.3 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 291676.9 ms | 286795.6 ms | 4881.3 ms | 183160.1 ms |
| Aws_restjson | LLGoNoLTO | 235913.0 ms | 233047.7 ms | 2865.4 ms | 81239.5 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 234792.6 ms | 231532.2 ms | 3260.5 ms | 139347.8 ms |
| Aws_restjson | LLGoDeadcodeDrop | 233607.0 ms | 230354.2 ms | 3252.9 ms | 81423.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 226160.3 ms | 222804.4 ms | 3355.9 ms | 126582.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 220818.2 ms | 217781.9 ms | 3036.3 ms | 124120.6 ms |
| Etcdctl | LLGoDeadcodeDrop | 217113.4 ms | 212024.7 ms | 5088.7 ms | 72455.0 ms |
| Etcdctl | LLGoNoLTO | 213914.0 ms | 209690.7 ms | 4223.3 ms | 70285.0 ms |
| XGo | LLGoFullLTOGlobalDCE | 209139.6 ms | 205757.5 ms | 3382.1 ms | 146646.8 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 207440.8 ms | 204089.9 ms | 3350.9 ms | 146010.0 ms |
| XGo | LLGoFullLTONoGlobalDCE | 205951.2 ms | 202723.0 ms | 3228.1 ms | 146010.5 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 198099.4 ms | 195316.4 ms | 2783.0 ms | 123506.2 ms |
| Uber_zap | LLGoNoLTO | 196501.5 ms | 194037.9 ms | 2463.6 ms | 72043.5 ms |
| Uber_zap | LLGoDeadcodeDrop | 193816.5 ms | 191106.9 ms | 2709.6 ms | 72286.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 192563.7 ms | 189489.7 ms | 3074.0 ms | 120589.4 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 190234.4 ms | 187412.3 ms | 2822.1 ms | 119633.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 186890.9 ms | 184211.7 ms | 2679.2 ms | 110836.3 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 186829.5 ms | 183957.4 ms | 2872.1 ms | 69667.5 ms |
| K8s_workqueue | LLGoNoLTO | 185580.6 ms | 183147.8 ms | 2432.7 ms | 68426.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 185408.5 ms | 182621.5 ms | 2786.9 ms | 110502.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 176401.5 ms | 173631.0 ms | 2770.5 ms | 103533.4 ms |
| XGo | LLGoDeadcodeDrop | 124502.0 ms | 121030.3 ms | 3471.7 ms | 46716.0 ms |
| XGo | LLGoNoLTO | 122677.8 ms | 120033.8 ms | 2644.1 ms | 45062.6 ms |
| Gorm_schema | LLGoDeadcodeDrop | 102598.8 ms | 100816.4 ms | 1782.4 ms | 33716.8 ms |
| Gorm_schema | LLGoNoLTO | 101424.8 ms | 99876.1 ms | 1548.7 ms | 33026.2 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 100776.4 ms | 99020.9 ms | 1755.5 ms | 59427.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 100677.8 ms | 98875.5 ms | 1802.3 ms | 58535.8 ms |
| Toml | LLGoDeadcodeDrop | 95926.3 ms | 94047.2 ms | 1879.1 ms | 31405.6 ms |
| Toml | LLGoNoLTO | 95740.4 ms | 94002.3 ms | 1738.2 ms | 31158.0 ms |
| Toml | LLGoFullLTONoGlobalDCE | 93065.4 ms | 91190.9 ms | 1874.5 ms | 54499.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 89186.7 ms | 87564.9 ms | 1621.8 ms | 46549.4 ms |
| Toml | LLGoFullLTOGlobalDCE | 85398.4 ms | 83576.9 ms | 1821.5 ms | 45343.5 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 85085.4 ms | 83303.0 ms | 1782.4 ms | 45433.2 ms |
| IXGo | Go | 83346.7 ms | 78379.8 ms | 4966.8 ms | 22906.7 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 65881.6 ms | 64555.0 ms | 1326.6 ms | 23484.5 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 65412.7 ms | 64104.3 ms | 1308.4 ms | 40206.6 ms |
| Dustin_humanize | LLGoNoLTO | 65027.1 ms | 63935.3 ms | 1091.8 ms | 22823.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 56213.4 ms | 54988.5 ms | 1224.9 ms | 30536.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 55985.2 ms | 54732.6 ms | 1252.6 ms | 30230.3 ms |
| Etcdctl | Go | 33029.7 ms | 30984.2 ms | 2045.5 ms | 10043.3 ms |
| XGo | Go | 18768.2 ms | 17636.2 ms | 1132.0 ms | 5517.9 ms |
| Aws_restjson | Go | 7869.2 ms | 7188.7 ms | 680.5 ms | 3163.4 ms |
| Gorm_schema | Go | 5843.2 ms | 5459.0 ms | 384.2 ms | 2264.1 ms |
| Uber_zap | Go | 5241.5 ms | 4849.8 ms | 391.7 ms | 2054.3 ms |
| K8s_workqueue | Go | 4709.8 ms | 4257.5 ms | 452.3 ms | 1641.1 ms |
| Toml | Go | 2006.3 ms | 1773.0 ms | 233.3 ms | 908.8 ms |
| Dustin_humanize | Go | 789.9 ms | 645.5 ms | 144.4 ms | 370.6 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1983993.8 ms | 1186404.3 ms | 9 |
| LLGoFullLTOGlobalDCE | 1957825.4 ms | 1141489.5 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1945544.0 ms | 1121495.0 ms | 9 |
| LLGoDeadcodeDrop | 1705560.7 ms | 575358.2 ms | 9 |
| LLGoNoLTO | 1695875.7 ms | 564001.3 ms | 9 |
| Go | 161604.3 ms | 48870.2 ms | 9 |

Dependency download details are in `download-timings.log`.
