## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 713322.7 ms | 702787.1 ms | 10535.6 ms | 358195.8 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 708435.3 ms | 697800.9 ms | 10634.4 ms | 355759.1 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 706776.4 ms | 695483.4 ms | 11293.0 ms | 355716.3 ms |
| IXGo | LLGoNoLTO | 562818.5 ms | 553360.4 ms | 9458.1 ms | 159123.9 ms |
| IXGo | LLGoDeadcodeDrop | 548662.9 ms | 534969.2 ms | 13693.7 ms | 160327.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 307129.7 ms | 302278.1 ms | 4851.6 ms | 191225.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 303127.8 ms | 297643.9 ms | 5484.0 ms | 187805.1 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 300488.3 ms | 295628.4 ms | 4859.9 ms | 189807.6 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 242534.7 ms | 239234.9 ms | 3299.8 ms | 143334.2 ms |
| Aws_restjson | LLGoDeadcodeDrop | 241776.6 ms | 238312.5 ms | 3464.1 ms | 83549.4 ms |
| Aws_restjson | LLGoNoLTO | 239760.1 ms | 236883.3 ms | 2876.8 ms | 81698.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 234313.8 ms | 231082.1 ms | 3231.7 ms | 130051.1 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 233745.4 ms | 230543.8 ms | 3201.6 ms | 129575.3 ms |
| Etcdctl | LLGoDeadcodeDrop | 222438.2 ms | 217258.6 ms | 5179.6 ms | 73310.9 ms |
| Etcdctl | LLGoNoLTO | 219193.8 ms | 214926.7 ms | 4267.1 ms | 71027.6 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 214785.5 ms | 211378.1 ms | 3407.4 ms | 151072.6 ms |
| XGo | LLGoFullLTONoGlobalDCE | 213696.5 ms | 210344.9 ms | 3351.6 ms | 151960.8 ms |
| XGo | LLGoFullLTOGlobalDCE | 213599.7 ms | 210130.4 ms | 3469.4 ms | 150126.1 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 204615.3 ms | 201624.0 ms | 2991.3 ms | 127243.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 198765.7 ms | 195754.5 ms | 3011.2 ms | 123710.3 ms |
| Uber_zap | LLGoDeadcodeDrop | 197883.3 ms | 194992.2 ms | 2891.1 ms | 72960.1 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 197742.2 ms | 194678.7 ms | 3063.6 ms | 124104.9 ms |
| Uber_zap | LLGoNoLTO | 197615.8 ms | 195228.7 ms | 2387.1 ms | 71574.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 192692.6 ms | 189714.7 ms | 2977.8 ms | 114201.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 192437.7 ms | 189665.0 ms | 2772.7 ms | 114090.4 ms |
| K8s_workqueue | LLGoNoLTO | 190840.0 ms | 188167.1 ms | 2672.9 ms | 69503.3 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 190701.2 ms | 187745.3 ms | 2955.9 ms | 70608.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 182025.9 ms | 179127.1 ms | 2898.8 ms | 106587.5 ms |
| XGo | LLGoNoLTO | 127190.4 ms | 124422.0 ms | 2768.4 ms | 45532.1 ms |
| XGo | LLGoDeadcodeDrop | 126951.3 ms | 123263.9 ms | 3687.4 ms | 46501.7 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 107399.1 ms | 105463.8 ms | 1935.3 ms | 63051.9 ms |
| Gorm_schema | LLGoDeadcodeDrop | 106056.7 ms | 104302.9 ms | 1753.8 ms | 34837.3 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 104691.3 ms | 102848.7 ms | 1842.5 ms | 62009.2 ms |
| Gorm_schema | LLGoNoLTO | 104410.3 ms | 102783.3 ms | 1627.1 ms | 34134.9 ms |
| Toml | LLGoDeadcodeDrop | 98881.1 ms | 96935.7 ms | 1945.4 ms | 32628.2 ms |
| Toml | LLGoNoLTO | 98635.0 ms | 96856.8 ms | 1778.2 ms | 31916.0 ms |
| Toml | LLGoFullLTONoGlobalDCE | 96957.2 ms | 95028.1 ms | 1929.1 ms | 56629.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 95704.8 ms | 93909.4 ms | 1795.4 ms | 50420.0 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 88659.4 ms | 86767.5 ms | 1891.9 ms | 47502.2 ms |
| Toml | LLGoFullLTOGlobalDCE | 87363.9 ms | 85542.5 ms | 1821.3 ms | 47290.9 ms |
| IXGo | Go | 85826.7 ms | 80551.5 ms | 5275.1 ms | 24021.2 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 68220.7 ms | 66920.5 ms | 1300.3 ms | 42073.8 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 67767.9 ms | 66447.8 ms | 1320.1 ms | 24240.5 ms |
| Dustin_humanize | LLGoNoLTO | 67024.7 ms | 65872.4 ms | 1152.3 ms | 23590.5 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 58333.6 ms | 57072.8 ms | 1260.8 ms | 31802.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 57742.9 ms | 56499.7 ms | 1243.1 ms | 31646.3 ms |
| Etcdctl | Go | 34360.3 ms | 32217.7 ms | 2142.6 ms | 10664.1 ms |
| XGo | Go | 19563.3 ms | 18304.3 ms | 1259.0 ms | 5909.2 ms |
| Aws_restjson | Go | 8184.1 ms | 7471.9 ms | 712.2 ms | 3355.7 ms |
| Gorm_schema | Go | 5903.8 ms | 5506.8 ms | 397.0 ms | 2362.4 ms |
| Uber_zap | Go | 5367.8 ms | 4947.6 ms | 420.1 ms | 2089.7 ms |
| K8s_workqueue | Go | 4802.3 ms | 4365.8 ms | 436.5 ms | 1811.6 ms |
| Toml | Go | 2066.5 ms | 1830.3 ms | 236.3 ms | 949.6 ms |
| Dustin_humanize | Go | 823.9 ms | 682.8 ms | 141.1 ms | 388.2 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2137381.6 ms | 1252921.9 ms | 9 |
| LLGoFullLTOGlobalDCE | 2107505.0 ms | 1205492.1 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2080421.7 ms | 1178578.9 ms | 9 |
| LLGoNoLTO | 1807488.6 ms | 588101.5 ms | 9 |
| LLGoDeadcodeDrop | 1801119.2 ms | 598963.7 ms | 9 |
| Go | 166898.6 ms | 51551.6 ms | 9 |

Dependency download details are in `download-timings.log`.
