## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 603536.2 ms | 591974.6 ms | 11561.5 ms | 296637.1 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 533844.2 ms | 518550.1 ms | 15294.1 ms | 281405.6 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 504886.5 ms | 493402.5 ms | 11484.0 ms | 269544.2 ms |
| IXGo | LLGoDeadcodeDrop | 451277.8 ms | 441168.7 ms | 10109.1 ms | 133236.3 ms |
| IXGo | LLGoNoLTO | 409783.8 ms | 400188.0 ms | 9595.8 ms | 122255.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 264171.9 ms | 259562.4 ms | 4609.5 ms | 163090.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 262091.0 ms | 257442.4 ms | 4648.6 ms | 161867.4 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 250973.0 ms | 246609.2 ms | 4363.8 ms | 155472.0 ms |
| Etcdctl | LLGoDeadcodeDrop | 194276.8 ms | 190065.7 ms | 4211.1 ms | 65315.6 ms |
| Etcdctl | LLGoNoLTO | 189333.2 ms | 185273.4 ms | 4059.9 ms | 63262.2 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 186513.6 ms | 183233.9 ms | 3279.7 ms | 128784.1 ms |
| XGo | LLGoFullLTOGlobalDCE | 186017.5 ms | 182530.4 ms | 3487.1 ms | 128333.5 ms |
| XGo | LLGoFullLTONoGlobalDCE | 178493.0 ms | 175240.7 ms | 3252.3 ms | 123467.0 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 136538.1 ms | 134121.5 ms | 2416.6 ms | 98720.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 124328.9 ms | 121913.8 ms | 2415.1 ms | 85600.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 124308.9 ms | 121770.1 ms | 2538.8 ms | 85761.8 ms |
| XGo | LLGoDeadcodeDrop | 112661.9 ms | 109806.0 ms | 2855.9 ms | 42269.1 ms |
| XGo | LLGoNoLTO | 110703.3 ms | 107852.2 ms | 2851.1 ms | 42225.5 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 107794.6 ms | 106011.1 ms | 1783.4 ms | 81665.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 101098.7 ms | 99309.2 ms | 1789.5 ms | 73669.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 99154.7 ms | 97306.7 ms | 1848.0 ms | 71748.0 ms |
| Aws_restjson | LLGoDeadcodeDrop | 88288.0 ms | 86261.7 ms | 2026.3 ms | 41344.0 ms |
| Aws_restjson | LLGoNoLTO | 83384.0 ms | 81338.5 ms | 2045.4 ms | 38843.3 ms |
| IXGo | Go | 83153.3 ms | 78133.9 ms | 5019.4 ms | 23468.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 61971.9 ms | 60528.8 ms | 1443.2 ms | 41734.7 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 61497.0 ms | 60113.9 ms | 1383.1 ms | 42086.2 ms |
| Uber_zap | LLGoDeadcodeDrop | 59144.4 ms | 57437.0 ms | 1707.4 ms | 25986.0 ms |
| Uber_zap | LLGoNoLTO | 58881.7 ms | 57346.3 ms | 1535.4 ms | 25842.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 52865.0 ms | 51425.7 ms | 1439.4 ms | 31956.0 ms |
| Toml | LLGoFullLTONoGlobalDCE | 48204.3 ms | 47062.4 ms | 1141.9 ms | 36238.4 ms |
| Toml | LLGoFullLTOGlobalDCE | 42539.3 ms | 41501.9 ms | 1037.3 ms | 29852.3 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 41431.4 ms | 40385.2 ms | 1046.2 ms | 28781.0 ms |
| Gorm_schema | LLGoDeadcodeDrop | 40590.3 ms | 39415.9 ms | 1174.4 ms | 13671.7 ms |
| Gorm_schema | LLGoNoLTO | 39281.0 ms | 38126.1 ms | 1154.9 ms | 13065.0 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 34454.7 ms | 33579.3 ms | 875.4 ms | 26674.5 ms |
| Etcdctl | Go | 34307.8 ms | 32220.9 ms | 2086.9 ms | 10340.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 27162.6 ms | 26261.7 ms | 900.9 ms | 19005.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 25761.5 ms | 24938.1 ms | 823.4 ms | 17995.3 ms |
| Toml | LLGoDeadcodeDrop | 24377.7 ms | 23430.5 ms | 947.2 ms | 9076.8 ms |
| Toml | LLGoNoLTO | 23902.3 ms | 22878.7 ms | 1023.5 ms | 9129.7 ms |
| XGo | Go | 18930.2 ms | 17778.8 ms | 1151.4 ms | 5738.3 ms |
| Dustin_humanize | LLGoNoLTO | 14220.4 ms | 13461.5 ms | 758.9 ms | 5974.3 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 14043.5 ms | 13318.8 ms | 724.7 ms | 5914.6 ms |
| Aws_restjson | Go | 7999.6 ms | 7175.6 ms | 824.1 ms | 3533.5 ms |
| Gorm_schema | Go | 5858.3 ms | 5349.1 ms | 509.2 ms | 2422.6 ms |
| Uber_zap | Go | 5415.9 ms | 4913.2 ms | 502.7 ms | 2304.2 ms |
| K8s_workqueue | Go | 5004.9 ms | 4422.0 ms | 582.9 ms | 1941.1 ms |
| Toml | Go | 2122.1 ms | 1868.1 ms | 254.0 ms | 984.9 ms |
| Dustin_humanize | Go | 812.4 ms | 653.1 ms | 159.4 ms | 394.6 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTOGlobalDCE | 1409405.8 ms | 837074.1 ms | 8 |
| LLGoFullLTOGlobalDCEPlugin | 1327391.4 ms | 809147.0 ms | 8 |
| LLGoFullLTONoGlobalDCE | 1322841.1 ms | 833868.4 ms | 8 |
| LLGoDeadcodeDrop | 984660.4 ms | 336814.0 ms | 8 |
| LLGoNoLTO | 929489.7 ms | 320598.1 ms | 8 |
| Go | 163604.5 ms | 51127.6 ms | 9 |

Dependency download details are in `download-timings.log`.
