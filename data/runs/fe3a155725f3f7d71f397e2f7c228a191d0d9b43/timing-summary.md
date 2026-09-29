## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 651716.8 ms | 638946.5 ms | 12770.3 ms | 337877.4 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 647507.4 ms | 631254.6 ms | 16252.8 ms | 326245.6 ms |
| IXGo | LLGoFullLTOGlobalDCE | 614390.4 ms | 601317.7 ms | 13072.7 ms | 308400.7 ms |
| IXGo | LLGoDeadcodeDrop | 544675.1 ms | 533364.2 ms | 11310.9 ms | 175475.1 ms |
| IXGo | LLGoNoLTO | 508917.1 ms | 497726.4 ms | 11190.7 ms | 157807.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 271592.1 ms | 266777.2 ms | 4814.9 ms | 166962.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 266456.7 ms | 261623.6 ms | 4833.1 ms | 163743.3 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 264636.9 ms | 259738.3 ms | 4898.6 ms | 163733.1 ms |
| Aws_restjson | LLGoNoLTO | 233324.8 ms | 230362.6 ms | 2962.1 ms | 78723.5 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 231194.7 ms | 227961.5 ms | 3233.3 ms | 128721.7 ms |
| Aws_restjson | LLGoDeadcodeDrop | 229495.2 ms | 226551.6 ms | 2943.6 ms | 78334.3 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 216516.4 ms | 213431.5 ms | 3084.9 ms | 115701.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 213186.6 ms | 209921.9 ms | 3264.7 ms | 115795.7 ms |
| Etcdctl | LLGoDeadcodeDrop | 198955.8 ms | 194553.2 ms | 4402.6 ms | 65621.6 ms |
| Etcdctl | LLGoNoLTO | 192825.2 ms | 188259.4 ms | 4565.8 ms | 64157.4 ms |
| XGo | LLGoFullLTOGlobalDCE | 188298.2 ms | 184574.5 ms | 3723.8 ms | 129013.8 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 186819.4 ms | 183574.0 ms | 3245.4 ms | 128564.5 ms |
| XGo | LLGoFullLTONoGlobalDCE | 185940.0 ms | 182618.5 ms | 3321.5 ms | 129059.8 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 173807.6 ms | 171184.8 ms | 2622.8 ms | 109174.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 172731.7 ms | 170015.6 ms | 2716.2 ms | 108695.8 ms |
| Uber_zap | LLGoDeadcodeDrop | 172362.9 ms | 169863.6 ms | 2499.3 ms | 65898.3 ms |
| Uber_zap | LLGoNoLTO | 169379.8 ms | 167043.1 ms | 2336.7 ms | 65222.7 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 168811.4 ms | 166120.8 ms | 2690.6 ms | 107209.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 168142.0 ms | 165501.6 ms | 2640.4 ms | 100856.8 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 166978.2 ms | 164398.2 ms | 2580.0 ms | 64432.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 165796.3 ms | 163152.4 ms | 2643.8 ms | 99830.5 ms |
| K8s_workqueue | LLGoNoLTO | 162283.0 ms | 159913.3 ms | 2369.7 ms | 62597.1 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 157727.7 ms | 155113.5 ms | 2614.2 ms | 93702.1 ms |
| XGo | LLGoDeadcodeDrop | 114161.4 ms | 111257.0 ms | 2904.4 ms | 41940.6 ms |
| XGo | LLGoNoLTO | 114069.4 ms | 110876.9 ms | 3192.6 ms | 41818.7 ms |
| Gorm_schema | LLGoDeadcodeDrop | 90412.0 ms | 88785.4 ms | 1626.7 ms | 29970.6 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 90363.5 ms | 88561.2 ms | 1802.4 ms | 53692.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 90091.6 ms | 88343.8 ms | 1747.9 ms | 53057.1 ms |
| Gorm_schema | LLGoNoLTO | 89052.6 ms | 87414.0 ms | 1638.6 ms | 29514.0 ms |
| IXGo | Go | 85283.8 ms | 79429.1 ms | 5854.7 ms | 24217.6 ms |
| Toml | LLGoFullLTONoGlobalDCE | 83526.8 ms | 81885.6 ms | 1641.2 ms | 48832.8 ms |
| Toml | LLGoDeadcodeDrop | 82835.5 ms | 81302.3 ms | 1533.2 ms | 27150.4 ms |
| Toml | LLGoNoLTO | 81816.9 ms | 80391.6 ms | 1425.3 ms | 26690.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 76833.2 ms | 75193.8 ms | 1639.4 ms | 40749.1 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 74227.7 ms | 72645.0 ms | 1582.6 ms | 40042.6 ms |
| Toml | LLGoFullLTOGlobalDCE | 73024.1 ms | 71474.4 ms | 1549.7 ms | 38992.2 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 56389.2 ms | 55404.6 ms | 984.6 ms | 20180.2 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 56305.6 ms | 55212.3 ms | 1093.3 ms | 35014.8 ms |
| Dustin_humanize | LLGoNoLTO | 56140.0 ms | 55102.1 ms | 1038.0 ms | 19964.5 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 48193.8 ms | 47090.2 ms | 1103.7 ms | 26535.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 47033.3 ms | 45936.2 ms | 1097.2 ms | 25791.5 ms |
| Etcdctl | Go | 33551.6 ms | 31411.3 ms | 2140.2 ms | 10045.8 ms |
| XGo | Go | 19508.3 ms | 18269.1 ms | 1239.2 ms | 5643.6 ms |
| Aws_restjson | Go | 8195.0 ms | 7507.3 ms | 687.7 ms | 3399.9 ms |
| Gorm_schema | Go | 5738.3 ms | 5320.1 ms | 418.2 ms | 2207.8 ms |
| Uber_zap | Go | 5421.6 ms | 5003.8 ms | 417.8 ms | 2165.4 ms |
| K8s_workqueue | Go | 4627.4 ms | 4233.2 ms | 394.1 ms | 1666.0 ms |
| Toml | Go | 2049.9 ms | 1860.9 ms | 189.0 ms | 934.3 ms |
| Dustin_humanize | Go | 816.4 ms | 677.6 ms | 138.8 ms | 388.1 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1902093.9 ms | 1101684.3 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1846093.6 ms | 1050059.4 ms | 9 |
| LLGoFullLTOGlobalDCE | 1836684.6 ms | 1044252.6 ms | 9 |
| LLGoDeadcodeDrop | 1656265.4 ms | 569003.5 ms | 9 |
| LLGoNoLTO | 1607808.9 ms | 546495.0 ms | 9 |
| Go | 165192.3 ms | 50668.5 ms | 9 |

Dependency download details are in `download-timings.log`.
