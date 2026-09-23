## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 717880.0 ms | 705051.6 ms | 12828.4 ms | 367082.2 ms |
| IXGo | LLGoFullLTOGlobalDCE | 699487.8 ms | 687786.2 ms | 11701.6 ms | 361891.5 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 677830.0 ms | 666213.5 ms | 11616.5 ms | 353810.5 ms |
| IXGo | LLGoDeadcodeDrop | 576609.4 ms | 566054.2 ms | 10555.2 ms | 175535.9 ms |
| IXGo | LLGoNoLTO | 532412.0 ms | 521919.2 ms | 10492.8 ms | 164054.3 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 305507.1 ms | 300367.2 ms | 5139.9 ms | 191206.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 296282.6 ms | 290941.8 ms | 5340.8 ms | 185549.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 276570.0 ms | 271265.5 ms | 5304.5 ms | 170768.1 ms |
| Etcdctl | LLGoDeadcodeDrop | 211371.7 ms | 206932.7 ms | 4439.1 ms | 69776.1 ms |
| Etcdctl | LLGoNoLTO | 209376.1 ms | 204847.6 ms | 4528.5 ms | 69459.1 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 207259.0 ms | 203578.3 ms | 3680.7 ms | 145521.9 ms |
| XGo | LLGoFullLTOGlobalDCE | 201343.4 ms | 197807.0 ms | 3536.4 ms | 140055.9 ms |
| XGo | LLGoFullLTONoGlobalDCE | 198765.7 ms | 195382.2 ms | 3383.5 ms | 139687.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 157862.8 ms | 155199.8 ms | 2663.0 ms | 116208.4 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 155414.1 ms | 152894.4 ms | 2519.7 ms | 115133.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 152082.5 ms | 149533.2 ms | 2549.4 ms | 110067.7 ms |
| XGo | LLGoNoLTO | 128887.4 ms | 125503.9 ms | 3383.5 ms | 48728.9 ms |
| XGo | LLGoDeadcodeDrop | 121517.0 ms | 118360.2 ms | 3156.9 ms | 45002.5 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 120710.7 ms | 118762.8 ms | 1947.8 ms | 91857.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 109558.0 ms | 107433.7 ms | 2124.3 ms | 79904.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 108271.6 ms | 106296.7 ms | 1974.9 ms | 79472.3 ms |
| Aws_restjson | LLGoDeadcodeDrop | 103957.2 ms | 101603.3 ms | 2353.8 ms | 54001.9 ms |
| Aws_restjson | LLGoNoLTO | 91356.1 ms | 89032.8 ms | 2323.4 ms | 43465.8 ms |
| IXGo | Go | 89471.3 ms | 83917.9 ms | 5553.4 ms | 25408.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 68460.7 ms | 66928.3 ms | 1532.4 ms | 46512.6 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 67992.1 ms | 66601.5 ms | 1390.7 ms | 46772.2 ms |
| Uber_zap | LLGoDeadcodeDrop | 67230.1 ms | 65542.6 ms | 1687.5 ms | 29481.7 ms |
| Uber_zap | LLGoNoLTO | 62237.8 ms | 60645.1 ms | 1592.7 ms | 27194.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 56675.3 ms | 55170.4 ms | 1504.9 ms | 34633.6 ms |
| Toml | LLGoFullLTONoGlobalDCE | 52599.4 ms | 51382.8 ms | 1216.6 ms | 39829.8 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 46514.8 ms | 45287.4 ms | 1227.4 ms | 32421.3 ms |
| Toml | LLGoFullLTOGlobalDCE | 45243.0 ms | 44076.9 ms | 1166.1 ms | 32013.5 ms |
| Gorm_schema | LLGoDeadcodeDrop | 43742.7 ms | 42491.5 ms | 1251.2 ms | 14621.5 ms |
| Gorm_schema | LLGoNoLTO | 42287.9 ms | 40925.0 ms | 1363.0 ms | 14310.4 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 39918.7 ms | 38951.8 ms | 966.9 ms | 31556.4 ms |
| Etcdctl | Go | 35268.4 ms | 32856.4 ms | 2412.0 ms | 11031.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 29595.2 ms | 28670.3 ms | 924.8 ms | 20924.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 29479.6 ms | 28505.0 ms | 974.6 ms | 20818.6 ms |
| Toml | LLGoDeadcodeDrop | 26551.5 ms | 25418.9 ms | 1132.6 ms | 9939.4 ms |
| Toml | LLGoNoLTO | 25858.0 ms | 24850.2 ms | 1007.9 ms | 9741.5 ms |
| XGo | Go | 21027.8 ms | 19617.1 ms | 1410.7 ms | 6201.1 ms |
| Dustin_humanize | LLGoNoLTO | 15296.4 ms | 14504.7 ms | 791.8 ms | 6469.2 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 15041.9 ms | 14287.3 ms | 754.7 ms | 6423.9 ms |
| Aws_restjson | Go | 8757.4 ms | 7969.2 ms | 788.3 ms | 3795.6 ms |
| Gorm_schema | Go | 6676.3 ms | 6167.2 ms | 509.1 ms | 2597.3 ms |
| Uber_zap | Go | 5717.9 ms | 5243.3 ms | 474.6 ms | 2363.9 ms |
| K8s_workqueue | Go | 5237.2 ms | 4538.7 ms | 698.6 ms | 2428.3 ms |
| Toml | Go | 2380.6 ms | 1996.9 ms | 383.6 ms | 1324.0 ms |
| Dustin_humanize | Go | 900.6 ms | 750.5 ms | 150.2 ms | 434.1 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1618737.8 ms | 1009852.7 ms | 8 |
| LLGoFullLTOGlobalDCEPlugin | 1615847.4 ms | 976105.1 ms | 8 |
| LLGoFullLTOGlobalDCE | 1586719.0 ms | 967740.9 ms | 8 |
| LLGoDeadcodeDrop | 1166021.6 ms | 404782.9 ms | 8 |
| LLGoNoLTO | 1107711.9 ms | 383423.2 ms | 8 |
| Go | 175437.6 ms | 55583.9 ms | 9 |

Dependency download details are in `download-timings.log`.
