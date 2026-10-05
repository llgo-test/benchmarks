## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 739348.9 ms | 728696.7 ms | 10652.2 ms | 366642.3 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 698470.9 ms | 688095.7 ms | 10375.2 ms | 357006.7 ms |
| IXGo | LLGoFullLTOGlobalDCE | 687093.0 ms | 677056.3 ms | 10036.7 ms | 350801.6 ms |
| IXGo | LLGoNoLTO | 563107.8 ms | 553770.0 ms | 9337.8 ms | 162611.1 ms |
| IXGo | LLGoDeadcodeDrop | 529890.3 ms | 515503.2 ms | 14387.1 ms | 157911.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 352927.8 ms | 347636.9 ms | 5290.9 ms | 206339.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 352845.4 ms | 347595.6 ms | 5249.8 ms | 206692.9 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 349063.9 ms | 343732.9 ms | 5331.0 ms | 207489.9 ms |
| Aws_restjson | LLGoDeadcodeDrop | 277803.1 ms | 274410.3 ms | 3392.8 ms | 92756.7 ms |
| Aws_restjson | LLGoNoLTO | 265970.3 ms | 262650.3 ms | 3320.1 ms | 89206.7 ms |
| Etcdctl | LLGoNoLTO | 265057.4 ms | 260208.8 ms | 4848.6 ms | 86686.5 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 263150.0 ms | 259352.1 ms | 3797.9 ms | 146181.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 262241.3 ms | 258333.5 ms | 3907.8 ms | 138163.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 261278.5 ms | 257269.2 ms | 4009.2 ms | 136604.9 ms |
| Etcdctl | LLGoDeadcodeDrop | 260587.5 ms | 254524.9 ms | 6062.7 ms | 86476.9 ms |
| XGo | LLGoFullLTONoGlobalDCE | 253015.2 ms | 249509.1 ms | 3506.1 ms | 166543.2 ms |
| XGo | LLGoFullLTOGlobalDCE | 252574.9 ms | 249019.9 ms | 3555.0 ms | 164993.2 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 249838.5 ms | 246419.9 ms | 3418.6 ms | 162721.8 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 240228.9 ms | 236732.3 ms | 3496.6 ms | 137800.3 ms |
| Uber_zap | LLGoNoLTO | 231381.8 ms | 228515.1 ms | 2866.7 ms | 81203.4 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 228735.5 ms | 225259.9 ms | 3475.6 ms | 131878.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 228047.9 ms | 224654.2 ms | 3393.7 ms | 124928.9 ms |
| Uber_zap | LLGoDeadcodeDrop | 227406.7 ms | 224641.8 ms | 2764.9 ms | 79727.3 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 226141.7 ms | 223187.2 ms | 2954.5 ms | 80195.2 ms |
| K8s_workqueue | LLGoNoLTO | 224133.0 ms | 221065.2 ms | 3067.8 ms | 79095.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 223250.5 ms | 219896.3 ms | 3354.2 ms | 126957.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 217600.8 ms | 214403.9 ms | 3196.9 ms | 118113.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 215884.8 ms | 212357.6 ms | 3527.3 ms | 116136.6 ms |
| XGo | LLGoDeadcodeDrop | 175960.0 ms | 171913.0 ms | 4047.0 ms | 64001.3 ms |
| XGo | LLGoNoLTO | 162455.8 ms | 159622.3 ms | 2833.5 ms | 58613.7 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 111008.6 ms | 108886.8 ms | 2121.8 ms | 64149.6 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 110593.3 ms | 108547.7 ms | 2045.6 ms | 64610.0 ms |
| Gorm_schema | LLGoNoLTO | 109883.0 ms | 108049.7 ms | 1833.4 ms | 36467.4 ms |
| Gorm_schema | LLGoDeadcodeDrop | 107986.6 ms | 106274.9 ms | 1711.8 ms | 35642.5 ms |
| Toml | LLGoDeadcodeDrop | 104454.0 ms | 102525.2 ms | 1928.8 ms | 34789.6 ms |
| Toml | LLGoNoLTO | 103410.3 ms | 101551.7 ms | 1858.6 ms | 34072.2 ms |
| Toml | LLGoFullLTONoGlobalDCE | 97920.5 ms | 95943.3 ms | 1977.3 ms | 55853.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 97804.3 ms | 95819.1 ms | 1985.2 ms | 51083.8 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 92605.7 ms | 90540.1 ms | 2065.6 ms | 49018.3 ms |
| Toml | LLGoFullLTOGlobalDCE | 88961.8 ms | 87026.0 ms | 1935.7 ms | 46486.7 ms |
| IXGo | Go | 86671.6 ms | 81246.5 ms | 5425.2 ms | 23862.8 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 72591.7 ms | 71121.8 ms | 1469.9 ms | 44003.6 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 72539.2 ms | 71325.8 ms | 1213.4 ms | 25929.5 ms |
| Dustin_humanize | LLGoNoLTO | 69700.7 ms | 68505.1 ms | 1195.6 ms | 25073.9 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 62895.0 ms | 61442.5 ms | 1452.5 ms | 33964.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 62383.2 ms | 61020.3 ms | 1363.0 ms | 33609.1 ms |
| Etcdctl | Go | 34324.6 ms | 32267.2 ms | 2057.4 ms | 10356.6 ms |
| XGo | Go | 19816.2 ms | 18575.4 ms | 1240.7 ms | 5923.0 ms |
| Aws_restjson | Go | 8396.3 ms | 7666.1 ms | 730.2 ms | 3682.1 ms |
| Gorm_schema | Go | 5928.8 ms | 5494.7 ms | 434.2 ms | 2483.6 ms |
| Uber_zap | Go | 5484.6 ms | 5060.0 ms | 424.6 ms | 2155.0 ms |
| K8s_workqueue | Go | 4645.7 ms | 4202.9 ms | 442.8 ms | 1629.5 ms |
| Toml | Go | 2128.1 ms | 1859.7 ms | 268.5 ms | 1050.8 ms |
| Dustin_humanize | Go | 809.7 ms | 653.4 ms | 156.4 ms | 383.2 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2313770.0 ms | 1311367.6 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2300549.1 ms | 1247793.6 ms | 9 |
| LLGoFullLTOGlobalDCE | 2258041.8 ms | 1249614.2 ms | 9 |
| LLGoNoLTO | 1995100.2 ms | 653029.8 ms | 9 |
| LLGoDeadcodeDrop | 1982769.2 ms | 657430.8 ms | 9 |
| Go | 168205.7 ms | 51526.6 ms | 9 |

Dependency download details are in `download-timings.log`.
