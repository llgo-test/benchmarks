## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 852892.9 ms | 826385.8 ms | 26507.0 ms | 546177.5 ms |
| IXGo | LLGoFullLTOGlobalDCE | 826918.6 ms | 800794.6 ms | 26124.0 ms | 531441.5 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 809234.1 ms | 783707.9 ms | 25526.2 ms | 521616.2 ms |
| IXGo | LLGoDeadcodeDrop | 511956.8 ms | 485046.5 ms | 26910.3 ms | 164448.8 ms |
| IXGo | LLGoNoLTO | 488175.9 ms | 465789.8 ms | 22386.0 ms | 153233.3 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 441652.7 ms | 429139.2 ms | 12513.5 ms | 318930.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 441155.5 ms | 429121.0 ms | 12034.5 ms | 315312.5 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 440071.7 ms | 428115.8 ms | 11955.9 ms | 315062.1 ms |
| XGo | LLGoFullLTONoGlobalDCE | 322703.7 ms | 314420.2 ms | 8283.5 ms | 252637.2 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 312242.3 ms | 305537.6 ms | 6704.7 ms | 208547.5 ms |
| XGo | LLGoFullLTOGlobalDCE | 286431.7 ms | 278462.6 ms | 7969.1 ms | 215611.9 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 284165.4 ms | 276169.6 ms | 7995.8 ms | 212906.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 281785.4 ms | 275265.4 ms | 6520.1 ms | 176641.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 279452.6 ms | 273185.8 ms | 6266.8 ms | 175753.6 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 262568.5 ms | 256981.2 ms | 5587.3 ms | 180259.6 ms |
| Aws_restjson | LLGoNoLTO | 257624.0 ms | 251734.4 ms | 5889.6 ms | 80430.4 ms |
| Aws_restjson | LLGoDeadcodeDrop | 257129.2 ms | 250889.6 ms | 6239.6 ms | 81770.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 253935.1 ms | 248243.6 ms | 5691.4 ms | 174989.6 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 253862.0 ms | 248123.1 ms | 5738.9 ms | 175502.7 ms |
| Etcdctl | LLGoDeadcodeDrop | 248013.6 ms | 237206.0 ms | 10807.7 ms | 85868.5 ms |
| Etcdctl | LLGoNoLTO | 247472.0 ms | 237726.6 ms | 9745.3 ms | 84326.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 241375.8 ms | 235860.8 ms | 5515.0 ms | 158859.9 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 237682.8 ms | 232017.3 ms | 5665.5 ms | 155114.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 219177.9 ms | 213789.6 ms | 5388.3 ms | 141230.3 ms |
| Uber_zap | LLGoNoLTO | 213949.6 ms | 209104.3 ms | 4845.3 ms | 68315.8 ms |
| Uber_zap | LLGoDeadcodeDrop | 212341.6 ms | 207167.4 ms | 5174.2 ms | 69080.3 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 204231.0 ms | 198756.4 ms | 5474.6 ms | 67284.4 ms |
| K8s_workqueue | LLGoNoLTO | 203994.7 ms | 199039.1 ms | 4955.6 ms | 65134.8 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 152608.2 ms | 148748.2 ms | 3860.0 ms | 104254.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 151979.4 ms | 148128.2 ms | 3851.2 ms | 102912.9 ms |
| Toml | LLGoFullLTONoGlobalDCE | 142933.6 ms | 139335.4 ms | 3598.2 ms | 96578.5 ms |
| XGo | LLGoDeadcodeDrop | 141064.7 ms | 133451.7 ms | 7613.0 ms | 51598.6 ms |
| XGo | LLGoNoLTO | 140016.9 ms | 133820.6 ms | 6196.3 ms | 51128.7 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 127551.2 ms | 124037.8 ms | 3513.5 ms | 78685.5 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 126726.2 ms | 123252.0 ms | 3474.2 ms | 79189.9 ms |
| Toml | LLGoFullLTOGlobalDCE | 126426.9 ms | 122760.2 ms | 3666.7 ms | 79134.7 ms |
| Gorm_schema | LLGoDeadcodeDrop | 118627.6 ms | 115067.5 ms | 3560.1 ms | 41544.1 ms |
| Gorm_schema | LLGoNoLTO | 116942.7 ms | 113822.4 ms | 3120.3 ms | 40232.4 ms |
| Toml | LLGoDeadcodeDrop | 111301.6 ms | 108123.3 ms | 3178.3 ms | 38244.2 ms |
| Toml | LLGoNoLTO | 110413.5 ms | 107521.9 ms | 2891.6 ms | 37779.7 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 100140.0 ms | 97606.1 ms | 2533.9 ms | 70452.5 ms |
| IXGo | Go | 99582.1 ms | 84170.1 ms | 15411.9 ms | 27792.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 81947.8 ms | 79577.8 ms | 2370.1 ms | 51501.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 81206.3 ms | 78896.0 ms | 2310.3 ms | 51347.3 ms |
| Dustin_humanize | LLGoNoLTO | 75738.2 ms | 73765.1 ms | 1973.1 ms | 27935.0 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 75723.0 ms | 73555.3 ms | 2167.7 ms | 28293.1 ms |
| Etcdctl | Go | 38660.0 ms | 33290.7 ms | 5369.3 ms | 11658.0 ms |
| XGo | Go | 22250.4 ms | 18993.5 ms | 3256.9 ms | 6718.5 ms |
| Aws_restjson | Go | 9274.9 ms | 7762.8 ms | 1512.1 ms | 3793.0 ms |
| Gorm_schema | Go | 6598.1 ms | 5635.4 ms | 962.7 ms | 2606.1 ms |
| Uber_zap | Go | 6040.4 ms | 5164.5 ms | 875.9 ms | 2423.7 ms |
| K8s_workqueue | Go | 5372.2 ms | 4447.8 ms | 924.3 ms | 1911.5 ms |
| Toml | Go | 2330.5 ms | 1917.8 ms | 412.7 ms | 1156.8 ms |
| Dustin_humanize | Go | 933.7 ms | 722.4 ms | 211.4 ms | 453.1 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2797945.1 ms | 1928779.4 ms | 9 |
| LLGoFullLTOGlobalDCE | 2690872.5 ms | 1806155.8 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2650010.7 ms | 1755717.3 ms | 9 |
| LLGoDeadcodeDrop | 1880389.0 ms | 628132.3 ms | 9 |
| LLGoNoLTO | 1854327.5 ms | 608516.9 ms | 9 |
| Go | 191042.2 ms | 58512.9 ms | 9 |

Dependency download details are in `download-timings.log`.
