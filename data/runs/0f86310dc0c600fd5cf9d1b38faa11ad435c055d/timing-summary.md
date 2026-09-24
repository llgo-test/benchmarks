## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 579577.8 ms | 566032.8 ms | 13545.0 ms | 297818.9 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 562383.5 ms | 550379.2 ms | 12004.3 ms | 292505.8 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 530880.4 ms | 518040.8 ms | 12839.6 ms | 281966.0 ms |
| IXGo | LLGoDeadcodeDrop | 486333.5 ms | 475654.9 ms | 10678.6 ms | 149615.4 ms |
| IXGo | LLGoNoLTO | 466549.3 ms | 456075.2 ms | 10474.0 ms | 141869.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 254753.0 ms | 249630.1 ms | 5122.9 ms | 159676.3 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 253853.8 ms | 248613.5 ms | 5240.3 ms | 160873.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 251763.8 ms | 246819.2 ms | 4944.5 ms | 157964.1 ms |
| Etcdctl | LLGoDeadcodeDrop | 185245.9 ms | 180590.8 ms | 4655.1 ms | 63559.2 ms |
| XGo | LLGoFullLTOGlobalDCE | 183756.5 ms | 180173.3 ms | 3583.2 ms | 130978.4 ms |
| Etcdctl | LLGoNoLTO | 179422.2 ms | 175139.3 ms | 4282.9 ms | 60418.3 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 176728.7 ms | 173240.6 ms | 3488.1 ms | 124201.5 ms |
| XGo | LLGoFullLTONoGlobalDCE | 176377.9 ms | 172879.8 ms | 3498.0 ms | 124682.1 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 136064.5 ms | 133506.7 ms | 2557.8 ms | 101190.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 129335.5 ms | 126762.3 ms | 2573.2 ms | 92430.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 124387.1 ms | 121975.4 ms | 2411.6 ms | 88877.0 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 106997.7 ms | 105087.4 ms | 1910.3 ms | 82571.3 ms |
| XGo | LLGoDeadcodeDrop | 106784.5 ms | 103612.1 ms | 3172.4 ms | 41929.7 ms |
| XGo | LLGoNoLTO | 104305.4 ms | 101390.9 ms | 2914.6 ms | 40351.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 99569.2 ms | 97603.8 ms | 1965.4 ms | 73471.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 99030.1 ms | 97124.8 ms | 1905.3 ms | 72725.5 ms |
| Aws_restjson | LLGoDeadcodeDrop | 83973.8 ms | 81725.1 ms | 2248.7 ms | 40945.0 ms |
| Aws_restjson | LLGoNoLTO | 81262.7 ms | 79140.9 ms | 2121.8 ms | 39390.7 ms |
| IXGo | Go | 80109.3 ms | 74619.5 ms | 5489.8 ms | 22773.7 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 61706.7 ms | 60288.4 ms | 1418.3 ms | 43384.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 60808.3 ms | 59350.0 ms | 1458.3 ms | 42200.7 ms |
| Uber_zap | LLGoDeadcodeDrop | 56363.9 ms | 54764.2 ms | 1599.7 ms | 25082.7 ms |
| Uber_zap | LLGoNoLTO | 54507.3 ms | 52980.5 ms | 1526.7 ms | 24440.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 50026.9 ms | 48633.9 ms | 1393.0 ms | 31051.3 ms |
| Toml | LLGoFullLTONoGlobalDCE | 47184.8 ms | 46083.7 ms | 1101.1 ms | 36056.2 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 42089.9 ms | 40923.6 ms | 1166.3 ms | 29635.7 ms |
| Toml | LLGoFullLTOGlobalDCE | 40001.5 ms | 38842.4 ms | 1159.2 ms | 28738.1 ms |
| Gorm_schema | LLGoDeadcodeDrop | 37852.5 ms | 36593.2 ms | 1259.3 ms | 12911.7 ms |
| Gorm_schema | LLGoNoLTO | 36253.0 ms | 35004.9 ms | 1248.0 ms | 12415.5 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 33616.9 ms | 32699.1 ms | 917.8 ms | 27029.1 ms |
| Etcdctl | Go | 31831.6 ms | 29663.6 ms | 2168.0 ms | 9630.5 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 25416.4 ms | 24454.2 ms | 962.2 ms | 18160.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 25410.4 ms | 24502.0 ms | 908.5 ms | 18048.0 ms |
| Toml | LLGoDeadcodeDrop | 23232.3 ms | 22146.1 ms | 1086.2 ms | 8727.6 ms |
| Toml | LLGoNoLTO | 22534.6 ms | 21531.0 ms | 1003.6 ms | 8677.7 ms |
| XGo | Go | 18508.3 ms | 17143.3 ms | 1365.1 ms | 5511.3 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 13260.2 ms | 12498.0 ms | 762.2 ms | 5769.4 ms |
| Dustin_humanize | LLGoNoLTO | 13130.8 ms | 12368.9 ms | 761.9 ms | 5669.5 ms |
| Aws_restjson | Go | 7832.7 ms | 7091.9 ms | 740.8 ms | 3188.6 ms |
| Gorm_schema | Go | 5512.6 ms | 5095.1 ms | 417.5 ms | 2128.5 ms |
| Uber_zap | Go | 5328.2 ms | 4741.2 ms | 587.0 ms | 2301.0 ms |
| K8s_workqueue | Go | 4844.1 ms | 4161.4 ms | 682.7 ms | 2090.1 ms |
| Toml | Go | 2043.0 ms | 1780.0 ms | 263.0 ms | 1032.0 ms |
| Dustin_humanize | Go | 814.1 ms | 659.9 ms | 154.2 ms | 385.0 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1378185.7 ms | 868292.8 ms | 8 |
| LLGoFullLTOGlobalDCE | 1364735.5 ms | 837350.6 ms | 8 |
| LLGoFullLTOGlobalDCEPlugin | 1308800.0 ms | 810593.5 ms | 8 |
| LLGoDeadcodeDrop | 993046.7 ms | 348540.7 ms | 8 |
| LLGoNoLTO | 957965.2 ms | 333232.9 ms | 8 |
| Go | 156823.9 ms | 49040.7 ms | 9 |

Dependency download details are in `download-timings.log`.
