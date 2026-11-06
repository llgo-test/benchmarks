## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 893655.9 ms | 867568.8 ms | 26087.1 ms | 560501.0 ms |
| IXGo | LLGoFullLTOGlobalDCE | 885808.2 ms | 859661.2 ms | 26147.0 ms | 559170.5 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 871236.2 ms | 844795.9 ms | 26440.3 ms | 549563.8 ms |
| IXGo | LLGoDeadcodeDrop | 547796.9 ms | 520110.2 ms | 27686.7 ms | 169304.6 ms |
| IXGo | LLGoNoLTO | 525137.9 ms | 501918.3 ms | 23219.6 ms | 158118.1 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 441190.9 ms | 429258.4 ms | 11932.5 ms | 322207.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 437427.9 ms | 425428.8 ms | 11999.1 ms | 315381.6 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 433015.0 ms | 420895.9 ms | 12119.1 ms | 313807.4 ms |
| XGo | LLGoFullLTONoGlobalDCE | 317776.8 ms | 309577.5 ms | 8199.3 ms | 252207.0 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 316845.6 ms | 310361.3 ms | 6484.3 ms | 212569.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 292321.0 ms | 285776.3 ms | 6544.6 ms | 183916.2 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 282073.6 ms | 274184.6 ms | 7889.0 ms | 214884.2 ms |
| XGo | LLGoFullLTOGlobalDCE | 281708.2 ms | 273746.2 ms | 7962.0 ms | 215723.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 278776.2 ms | 272344.1 ms | 6432.1 ms | 178819.9 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 252830.1 ms | 247311.5 ms | 5518.6 ms | 178283.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 245769.5 ms | 240145.3 ms | 5624.2 ms | 172323.9 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 242966.4 ms | 237444.0 ms | 5522.4 ms | 171122.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 232687.7 ms | 227207.1 ms | 5480.6 ms | 156075.5 ms |
| Etcdctl | LLGoNoLTO | 229852.1 ms | 220041.6 ms | 9810.4 ms | 77377.3 ms |
| Etcdctl | LLGoDeadcodeDrop | 229187.4 ms | 218165.3 ms | 11022.1 ms | 77828.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 225942.5 ms | 220495.4 ms | 5447.2 ms | 150265.3 ms |
| Aws_restjson | LLGoNoLTO | 224530.7 ms | 219190.1 ms | 5340.6 ms | 69494.0 ms |
| Aws_restjson | LLGoDeadcodeDrop | 219983.7 ms | 214186.5 ms | 5797.1 ms | 69400.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 213370.5 ms | 208227.7 ms | 5142.8 ms | 141449.3 ms |
| Uber_zap | LLGoNoLTO | 178220.2 ms | 174028.8 ms | 4191.4 ms | 57052.1 ms |
| Uber_zap | LLGoDeadcodeDrop | 177333.4 ms | 172220.5 ms | 5112.8 ms | 58264.3 ms |
| K8s_workqueue | LLGoNoLTO | 169015.4 ms | 164684.6 ms | 4330.9 ms | 54037.6 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 166056.6 ms | 161349.7 ms | 4706.9 ms | 54128.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 148740.5 ms | 144843.0 ms | 3897.5 ms | 102973.1 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 146255.9 ms | 142411.9 ms | 3844.0 ms | 102451.1 ms |
| Toml | LLGoFullLTONoGlobalDCE | 137929.9 ms | 134266.7 ms | 3663.2 ms | 96041.8 ms |
| XGo | LLGoDeadcodeDrop | 129943.7 ms | 122553.4 ms | 7390.3 ms | 45772.9 ms |
| XGo | LLGoNoLTO | 127685.3 ms | 121442.1 ms | 6243.2 ms | 45930.7 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 127022.7 ms | 123376.0 ms | 3646.7 ms | 80701.7 ms |
| Toml | LLGoFullLTOGlobalDCE | 119266.0 ms | 115949.7 ms | 3316.4 ms | 76690.2 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 117507.1 ms | 114156.1 ms | 3351.1 ms | 75113.9 ms |
| Gorm_schema | LLGoDeadcodeDrop | 109443.7 ms | 105816.6 ms | 3627.0 ms | 37889.5 ms |
| Gorm_schema | LLGoNoLTO | 107483.9 ms | 104346.7 ms | 3137.3 ms | 36318.3 ms |
| Toml | LLGoNoLTO | 104825.4 ms | 101882.7 ms | 2942.7 ms | 35217.8 ms |
| Toml | LLGoDeadcodeDrop | 100925.5 ms | 97951.2 ms | 2974.4 ms | 34271.7 ms |
| IXGo | Go | 99261.1 ms | 84260.7 ms | 15000.4 ms | 27029.9 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 97577.0 ms | 95021.4 ms | 2555.6 ms | 70358.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 76950.3 ms | 74637.2 ms | 2313.1 ms | 49749.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 76521.3 ms | 74285.0 ms | 2236.2 ms | 49388.5 ms |
| Dustin_humanize | LLGoNoLTO | 68718.1 ms | 66695.1 ms | 2023.1 ms | 25120.7 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 68707.2 ms | 66523.1 ms | 2184.1 ms | 25374.0 ms |
| Etcdctl | Go | 38747.1 ms | 33337.4 ms | 5409.7 ms | 11679.5 ms |
| XGo | Go | 22192.7 ms | 19123.8 ms | 3068.9 ms | 6548.9 ms |
| Aws_restjson | Go | 9384.6 ms | 7809.5 ms | 1575.0 ms | 3931.3 ms |
| Gorm_schema | Go | 6862.2 ms | 5807.7 ms | 1054.5 ms | 2912.0 ms |
| Uber_zap | Go | 6140.4 ms | 5187.2 ms | 953.2 ms | 2557.8 ms |
| K8s_workqueue | Go | 5604.6 ms | 4646.2 ms | 958.5 ms | 2502.4 ms |
| Toml | Go | 2284.8 ms | 1891.2 ms | 393.6 ms | 1081.4 ms |
| Dustin_humanize | Go | 928.6 ms | 722.7 ms | 206.0 ms | 466.8 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2824608.9 ms | 1954805.6 ms | 9 |
| LLGoFullLTOGlobalDCE | 2715837.4 ms | 1830068.7 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2652726.7 ms | 1766865.9 ms | 9 |
| LLGoDeadcodeDrop | 1749377.9 ms | 572234.0 ms | 9 |
| LLGoNoLTO | 1735469.1 ms | 558666.7 ms | 9 |
| Go | 191406.2 ms | 58710.0 ms | 9 |

Dependency download details are in `download-timings.log`.
