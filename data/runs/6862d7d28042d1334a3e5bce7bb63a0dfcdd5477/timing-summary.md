## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 963930.1 ms | 950060.6 ms | 13869.6 ms | 589807.9 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 954071.2 ms | 942013.8 ms | 12057.5 ms | 592725.2 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 888851.1 ms | 876226.5 ms | 12624.6 ms | 573172.2 ms |
| IXGo | LLGoNoLTO | 627061.7 ms | 617009.7 ms | 10052.0 ms | 190031.3 ms |
| IXGo | LLGoDeadcodeDrop | 603234.8 ms | 587654.7 ms | 15580.2 ms | 184773.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 451072.6 ms | 444937.2 ms | 6135.4 ms | 332213.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 450138.5 ms | 444204.5 ms | 5934.1 ms | 331325.2 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 447041.7 ms | 441200.7 ms | 5841.0 ms | 334910.4 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 345665.3 ms | 341527.9 ms | 4137.5 ms | 238859.6 ms |
| XGo | LLGoFullLTONoGlobalDCE | 336205.6 ms | 331755.6 ms | 4450.0 ms | 271120.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 313003.8 ms | 309031.6 ms | 3972.2 ms | 208798.9 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 294903.6 ms | 290846.5 ms | 4057.1 ms | 229221.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 294852.7 ms | 290943.6 ms | 3909.1 ms | 196314.9 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 294296.3 ms | 290664.6 ms | 3631.7 ms | 215682.6 ms |
| XGo | LLGoFullLTOGlobalDCE | 289519.0 ms | 285422.1 ms | 4096.9 ms | 225434.0 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 284514.4 ms | 280959.3 ms | 3555.0 ms | 209047.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 279573.2 ms | 276017.3 ms | 3555.8 ms | 203182.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 274545.7 ms | 270918.9 ms | 3626.8 ms | 191626.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 260217.0 ms | 256782.2 ms | 3434.8 ms | 179044.5 ms |
| Aws_restjson | LLGoNoLTO | 255113.7 ms | 251979.0 ms | 3134.7 ms | 88024.8 ms |
| Aws_restjson | LLGoDeadcodeDrop | 245774.1 ms | 242050.8 ms | 3723.2 ms | 86052.2 ms |
| Etcdctl | LLGoDeadcodeDrop | 242316.9 ms | 236540.0 ms | 5776.9 ms | 85652.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 236769.8 ms | 233321.1 ms | 3448.7 ms | 162053.8 ms |
| Etcdctl | LLGoNoLTO | 236280.8 ms | 231466.8 ms | 4813.9 ms | 82533.8 ms |
| Uber_zap | LLGoNoLTO | 204554.3 ms | 201879.1 ms | 2675.2 ms | 76209.4 ms |
| K8s_workqueue | LLGoNoLTO | 203530.1 ms | 200626.5 ms | 2903.7 ms | 75629.7 ms |
| Uber_zap | LLGoDeadcodeDrop | 202797.5 ms | 199726.6 ms | 3071.0 ms | 76488.3 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 200978.9 ms | 197836.9 ms | 3142.0 ms | 75663.2 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 151924.5 ms | 149590.5 ms | 2334.0 ms | 108096.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 151169.1 ms | 148818.4 ms | 2350.7 ms | 105941.7 ms |
| Toml | LLGoFullLTONoGlobalDCE | 137701.9 ms | 135287.1 ms | 2414.9 ms | 97211.4 ms |
| XGo | LLGoNoLTO | 133649.7 ms | 130722.1 ms | 2927.7 ms | 51401.4 ms |
| XGo | LLGoDeadcodeDrop | 131728.2 ms | 127898.9 ms | 3829.3 ms | 50347.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 120074.5 ms | 118097.2 ms | 1977.3 ms | 76409.2 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 119660.4 ms | 117434.0 ms | 2226.4 ms | 77450.7 ms |
| Toml | LLGoFullLTOGlobalDCE | 115487.8 ms | 113407.0 ms | 2080.8 ms | 74436.8 ms |
| Gorm_schema | LLGoDeadcodeDrop | 111503.1 ms | 109462.7 ms | 2040.4 ms | 37744.9 ms |
| Gorm_schema | LLGoNoLTO | 106695.5 ms | 104996.9 ms | 1698.6 ms | 35736.2 ms |
| Toml | LLGoDeadcodeDrop | 102407.3 ms | 100328.3 ms | 2078.9 ms | 34270.1 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 100844.2 ms | 99133.6 ms | 1710.6 ms | 74398.8 ms |
| Toml | LLGoNoLTO | 100334.9 ms | 98457.8 ms | 1877.1 ms | 33320.7 ms |
| IXGo | Go | 87371.6 ms | 82248.8 ms | 5122.8 ms | 24119.5 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 76831.5 ms | 75321.4 ms | 1510.1 ms | 50107.9 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 75932.2 ms | 74428.4 ms | 1503.9 ms | 49457.7 ms |
| Dustin_humanize | LLGoNoLTO | 68897.1 ms | 67676.8 ms | 1220.4 ms | 24889.9 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 68684.6 ms | 67274.3 ms | 1410.3 ms | 24896.7 ms |
| Etcdctl | Go | 34914.6 ms | 32783.7 ms | 2130.9 ms | 10679.1 ms |
| XGo | Go | 19506.9 ms | 18379.4 ms | 1127.6 ms | 5758.6 ms |
| Aws_restjson | Go | 8604.8 ms | 7887.5 ms | 717.3 ms | 3649.4 ms |
| Gorm_schema | Go | 6145.8 ms | 5701.7 ms | 444.1 ms | 2432.5 ms |
| Uber_zap | Go | 5467.8 ms | 5011.3 ms | 456.4 ms | 2191.0 ms |
| K8s_workqueue | Go | 4902.5 ms | 4439.8 ms | 462.7 ms | 1736.0 ms |
| Toml | Go | 2165.1 ms | 1902.0 ms | 263.0 ms | 1152.8 ms |
| Dustin_humanize | Go | 853.1 ms | 693.9 ms | 159.2 ms | 414.8 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 3052265.1 ms | 2142052.6 ms | 9 |
| LLGoFullLTOGlobalDCE | 2899904.8 ms | 1968316.8 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2756627.9 ms | 1887682.4 ms | 9 |
| LLGoNoLTO | 1936117.8 ms | 657777.2 ms | 9 |
| LLGoDeadcodeDrop | 1909425.2 ms | 655888.7 ms | 9 |
| Go | 169932.1 ms | 52133.5 ms | 9 |

Dependency download details are in `download-timings.log`.
