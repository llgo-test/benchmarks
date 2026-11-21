## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 649303.3 ms | 632610.0 ms | 16693.3 ms | 426651.9 ms |
| IXGo | LLGoFullLTOGlobalDCE | 624879.1 ms | 609122.7 ms | 15756.4 ms | 415187.5 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 613059.5 ms | 597714.1 ms | 15345.4 ms | 404987.1 ms |
| IXGo | LLGoDeadcodeDrop | 381383.2 ms | 364594.4 ms | 16788.8 ms | 123000.2 ms |
| IXGo | LLGoNoLTO | 349050.4 ms | 335665.0 ms | 13385.4 ms | 108815.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 329048.8 ms | 322026.9 ms | 7021.9 ms | 244347.4 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 325783.9 ms | 318742.8 ms | 7041.1 ms | 244642.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 320466.5 ms | 313582.9 ms | 6883.7 ms | 237955.1 ms |
| XGo | LLGoFullLTONoGlobalDCE | 243326.0 ms | 238540.2 ms | 4785.8 ms | 197052.9 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 225020.5 ms | 220952.7 ms | 4067.8 ms | 152979.7 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 212233.6 ms | 207386.7 ms | 4846.9 ms | 164359.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 211286.2 ms | 207260.9 ms | 4025.3 ms | 136911.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 207732.5 ms | 203667.4 ms | 4065.0 ms | 133769.2 ms |
| XGo | LLGoFullLTOGlobalDCE | 205911.4 ms | 201277.0 ms | 4634.4 ms | 159328.8 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 186477.3 ms | 182925.6 ms | 3551.7 ms | 133612.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 180208.9 ms | 176654.9 ms | 3554.0 ms | 130015.4 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 177276.8 ms | 173801.6 ms | 3475.3 ms | 127765.8 ms |
| Aws_restjson | LLGoNoLTO | 176064.9 ms | 172649.2 ms | 3415.7 ms | 55099.4 ms |
| Aws_restjson | LLGoDeadcodeDrop | 174928.1 ms | 171257.2 ms | 3670.9 ms | 56047.2 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 170010.1 ms | 166645.5 ms | 3364.6 ms | 116166.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 169248.0 ms | 165878.8 ms | 3369.2 ms | 115645.4 ms |
| Etcdctl | LLGoDeadcodeDrop | 168069.4 ms | 162156.7 ms | 5912.6 ms | 58949.5 ms |
| Etcdctl | LLGoNoLTO | 167450.6 ms | 161846.9 ms | 5603.7 ms | 57850.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 153983.7 ms | 150748.2 ms | 3235.5 ms | 103273.3 ms |
| Uber_zap | LLGoNoLTO | 147965.0 ms | 144951.3 ms | 3013.7 ms | 47494.5 ms |
| Uber_zap | LLGoDeadcodeDrop | 143741.6 ms | 140681.3 ms | 3060.3 ms | 47233.0 ms |
| K8s_workqueue | LLGoNoLTO | 136673.4 ms | 133857.6 ms | 2815.8 ms | 44122.3 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 136473.7 ms | 133518.6 ms | 2955.1 ms | 45467.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 108163.1 ms | 105697.8 ms | 2465.3 ms | 75370.5 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 106046.2 ms | 103686.4 ms | 2359.8 ms | 75108.2 ms |
| XGo | LLGoNoLTO | 99721.6 ms | 95933.1 ms | 3788.5 ms | 36639.8 ms |
| Toml | LLGoFullLTONoGlobalDCE | 98644.5 ms | 96436.0 ms | 2208.5 ms | 69388.1 ms |
| XGo | LLGoDeadcodeDrop | 98058.5 ms | 93781.1 ms | 4277.4 ms | 35968.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 87820.2 ms | 85587.0 ms | 2233.2 ms | 55671.1 ms |
| Toml | LLGoFullLTOGlobalDCE | 87783.1 ms | 85731.9 ms | 2051.2 ms | 57570.1 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 85161.6 ms | 83057.5 ms | 2104.1 ms | 55559.9 ms |
| Gorm_schema | LLGoDeadcodeDrop | 79313.5 ms | 77203.0 ms | 2110.4 ms | 28002.9 ms |
| Gorm_schema | LLGoNoLTO | 78332.8 ms | 76412.4 ms | 1920.4 ms | 27209.7 ms |
| Toml | LLGoNoLTO | 73960.1 ms | 72198.1 ms | 1762.0 ms | 25516.3 ms |
| Toml | LLGoDeadcodeDrop | 73323.2 ms | 71439.4 ms | 1883.9 ms | 25655.1 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 69217.9 ms | 67701.7 ms | 1516.3 ms | 50097.8 ms |
| IXGo | Go | 59944.9 ms | 52726.2 ms | 7218.7 ms | 16630.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 56447.0 ms | 55057.7 ms | 1389.4 ms | 36982.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 55353.9 ms | 53915.1 ms | 1438.8 ms | 35975.4 ms |
| Dustin_humanize | LLGoNoLTO | 51100.7 ms | 49872.3 ms | 1228.4 ms | 19194.5 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 50886.4 ms | 49563.4 ms | 1323.0 ms | 19298.0 ms |
| Etcdctl | Go | 24189.3 ms | 21519.1 ms | 2670.2 ms | 7361.4 ms |
| XGo | Go | 13929.4 ms | 12397.8 ms | 1531.6 ms | 4170.2 ms |
| Aws_restjson | Go | 6071.0 ms | 5255.8 ms | 815.3 ms | 2488.2 ms |
| Gorm_schema | Go | 4427.3 ms | 3878.9 ms | 548.3 ms | 1698.9 ms |
| Uber_zap | Go | 3976.4 ms | 3529.8 ms | 446.6 ms | 1564.3 ms |
| K8s_workqueue | Go | 3430.3 ms | 2999.2 ms | 431.1 ms | 1215.4 ms |
| Toml | Go | 1511.6 ms | 1305.8 ms | 205.8 ms | 699.1 ms |
| Dustin_humanize | Go | 611.2 ms | 491.1 ms | 120.1 ms | 291.8 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2044852.6 ms | 1455634.8 ms | 9 |
| LLGoFullLTOGlobalDCE | 1972975.7 ms | 1371359.0 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1942065.4 ms | 1329382.1 ms | 9 |
| LLGoDeadcodeDrop | 1306177.6 ms | 439621.3 ms | 9 |
| LLGoNoLTO | 1280319.4 ms | 421942.2 ms | 9 |
| Go | 118091.4 ms | 36119.3 ms | 9 |

Dependency download details are in `download-timings.log`.
