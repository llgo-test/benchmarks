## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 659390.4 ms | 642245.2 ms | 17145.2 ms | 438140.0 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 655712.4 ms | 639095.6 ms | 16616.9 ms | 437467.2 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 627499.1 ms | 611497.0 ms | 16002.1 ms | 421026.3 ms |
| IXGo | LLGoDeadcodeDrop | 371817.9 ms | 355102.1 ms | 16715.8 ms | 119819.4 ms |
| IXGo | LLGoNoLTO | 359861.1 ms | 345175.6 ms | 14685.5 ms | 112563.8 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 338761.0 ms | 331375.5 ms | 7385.5 ms | 253182.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 332428.6 ms | 325049.7 ms | 7378.9 ms | 247621.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 328475.9 ms | 321471.2 ms | 7004.7 ms | 245882.2 ms |
| XGo | LLGoFullLTONoGlobalDCE | 246343.6 ms | 241184.2 ms | 5159.3 ms | 199208.7 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 234144.1 ms | 229846.4 ms | 4297.7 ms | 161187.8 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 215878.6 ms | 210920.1 ms | 4958.5 ms | 168007.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 214464.8 ms | 210423.5 ms | 4041.3 ms | 139812.0 ms |
| XGo | LLGoFullLTOGlobalDCE | 214109.3 ms | 209346.7 ms | 4762.6 ms | 166552.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 209386.6 ms | 205119.2 ms | 4267.4 ms | 136261.6 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 198895.5 ms | 195203.8 ms | 3691.7 ms | 143469.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 192694.5 ms | 188965.5 ms | 3729.1 ms | 139372.6 ms |
| Aws_restjson | LLGoNoLTO | 184481.4 ms | 180835.8 ms | 3645.6 ms | 57548.4 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 184394.0 ms | 180708.8 ms | 3685.2 ms | 133730.2 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 175401.6 ms | 171966.5 ms | 3435.1 ms | 121168.9 ms |
| Aws_restjson | LLGoDeadcodeDrop | 175058.7 ms | 171272.4 ms | 3786.4 ms | 56241.9 ms |
| Etcdctl | LLGoDeadcodeDrop | 172877.3 ms | 166558.8 ms | 6318.4 ms | 60313.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 169483.6 ms | 165993.2 ms | 3490.4 ms | 115376.3 ms |
| Etcdctl | LLGoNoLTO | 168699.3 ms | 162749.6 ms | 5949.7 ms | 58761.1 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 155809.2 ms | 152437.2 ms | 3372.0 ms | 104409.2 ms |
| Uber_zap | LLGoDeadcodeDrop | 146194.3 ms | 142957.7 ms | 3236.6 ms | 48447.7 ms |
| Uber_zap | LLGoNoLTO | 146044.9 ms | 143056.6 ms | 2988.3 ms | 47110.9 ms |
| K8s_workqueue | LLGoNoLTO | 137716.9 ms | 134603.8 ms | 3113.2 ms | 44697.3 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 136817.6 ms | 133649.7 ms | 3167.8 ms | 45545.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 111572.1 ms | 109055.9 ms | 2516.2 ms | 78944.5 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 108785.0 ms | 106305.2 ms | 2479.8 ms | 77800.1 ms |
| Toml | LLGoFullLTONoGlobalDCE | 106282.5 ms | 103962.1 ms | 2320.3 ms | 75310.7 ms |
| XGo | LLGoNoLTO | 96405.4 ms | 92668.0 ms | 3737.4 ms | 36000.6 ms |
| XGo | LLGoDeadcodeDrop | 92539.4 ms | 88458.8 ms | 4080.5 ms | 34646.7 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 90013.5 ms | 87828.6 ms | 2184.9 ms | 59402.1 ms |
| Toml | LLGoFullLTOGlobalDCE | 89891.4 ms | 87608.3 ms | 2283.1 ms | 59356.7 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 88567.1 ms | 86186.5 ms | 2380.6 ms | 56747.0 ms |
| Gorm_schema | LLGoDeadcodeDrop | 79957.7 ms | 77637.3 ms | 2320.3 ms | 28434.7 ms |
| Gorm_schema | LLGoNoLTO | 79562.8 ms | 77473.3 ms | 2089.5 ms | 27838.9 ms |
| Toml | LLGoDeadcodeDrop | 74663.0 ms | 72788.6 ms | 1874.4 ms | 26138.6 ms |
| Toml | LLGoNoLTO | 73269.1 ms | 71482.4 ms | 1786.7 ms | 25459.6 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 72719.9 ms | 71111.6 ms | 1608.2 ms | 53596.5 ms |
| IXGo | Go | 62049.4 ms | 54296.3 ms | 7753.1 ms | 17224.5 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 58485.3 ms | 57047.1 ms | 1438.2 ms | 38911.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 58090.9 ms | 56571.3 ms | 1519.6 ms | 38156.3 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 52787.9 ms | 51376.4 ms | 1411.5 ms | 20011.8 ms |
| Dustin_humanize | LLGoNoLTO | 51493.9 ms | 50236.7 ms | 1257.1 ms | 19311.5 ms |
| Etcdctl | Go | 24768.0 ms | 22007.6 ms | 2760.4 ms | 7672.9 ms |
| XGo | Go | 14520.1 ms | 12881.7 ms | 1638.4 ms | 4360.2 ms |
| Aws_restjson | Go | 6075.6 ms | 5207.4 ms | 868.1 ms | 2605.2 ms |
| Gorm_schema | Go | 4590.1 ms | 3980.2 ms | 609.9 ms | 1890.1 ms |
| Uber_zap | Go | 4078.2 ms | 3579.2 ms | 499.0 ms | 1626.5 ms |
| K8s_workqueue | Go | 3597.1 ms | 3105.7 ms | 491.4 ms | 1458.3 ms |
| Toml | Go | 1547.2 ms | 1325.9 ms | 221.3 ms | 712.9 ms |
| Dustin_humanize | Go | 603.6 ms | 500.1 ms | 103.6 ms | 300.1 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2117824.6 ms | 1518512.8 ms | 9 |
| LLGoFullLTOGlobalDCE | 2048043.5 ms | 1429124.6 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1971812.1 ms | 1362464.9 ms | 9 |
| LLGoDeadcodeDrop | 1302713.7 ms | 439599.4 ms | 9 |
| LLGoNoLTO | 1297534.7 ms | 429292.0 ms | 9 |
| Go | 121829.4 ms | 37850.6 ms | 9 |

Dependency download details are in `download-timings.log`.
