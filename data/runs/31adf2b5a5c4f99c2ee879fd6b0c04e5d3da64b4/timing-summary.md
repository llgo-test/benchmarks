## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTONoGlobalDCE | 875114.0 ms | 855070.9 ms | 20043.1 ms | 546645.9 ms |
| IXGo | LLGoFullLTOGlobalDCE | 833513.8 ms | 813468.6 ms | 20045.2 ms | 494462.2 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 727441.5 ms | 708250.4 ms | 19191.1 ms | 439937.5 ms |
| IXGo | LLGoDeadcodeDrop | 507992.2 ms | 489482.6 ms | 18509.6 ms | 167473.2 ms |
| IXGo | LLGoNoLTO | 443703.9 ms | 427238.0 ms | 16466.0 ms | 132988.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 328981.0 ms | 319189.7 ms | 9791.3 ms | 246011.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 324689.3 ms | 314932.4 ms | 9756.9 ms | 242898.4 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 317831.0 ms | 308466.7 ms | 9364.3 ms | 242430.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 263819.8 ms | 258106.4 ms | 5713.4 ms | 173509.9 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 262372.3 ms | 256575.2 ms | 5797.1 ms | 176852.4 ms |
| XGo | LLGoFullLTONoGlobalDCE | 255314.5 ms | 248551.7 ms | 6762.8 ms | 211355.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 223728.5 ms | 218390.6 ms | 5337.8 ms | 167393.5 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 220213.7 ms | 215032.1 ms | 5181.6 ms | 163710.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 217224.1 ms | 211656.5 ms | 5567.6 ms | 145942.7 ms |
| XGo | LLGoFullLTOGlobalDCE | 215138.7 ms | 208672.6 ms | 6466.0 ms | 170255.8 ms |
| Aws_restjson | LLGoNoLTO | 213152.7 ms | 208454.9 ms | 4697.8 ms | 69416.4 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 205806.3 ms | 199561.7 ms | 6244.6 ms | 162961.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 202483.0 ms | 197499.6 ms | 4983.4 ms | 146458.4 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 199254.0 ms | 194345.6 ms | 4908.4 ms | 148285.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 188589.2 ms | 183821.5 ms | 4767.7 ms | 136723.8 ms |
| Etcdctl | LLGoNoLTO | 176374.9 ms | 168469.2 ms | 7905.6 ms | 61488.0 ms |
| Aws_restjson | LLGoDeadcodeDrop | 175322.0 ms | 170646.3 ms | 4675.7 ms | 60354.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 173137.6 ms | 168381.4 ms | 4756.2 ms | 125046.5 ms |
| Etcdctl | LLGoDeadcodeDrop | 164098.3 ms | 155838.0 ms | 8260.3 ms | 59057.2 ms |
| Uber_zap | LLGoDeadcodeDrop | 136903.7 ms | 133037.2 ms | 3866.5 ms | 52110.6 ms |
| K8s_workqueue | LLGoNoLTO | 132151.6 ms | 128450.1 ms | 3701.4 ms | 49843.9 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 130459.7 ms | 126523.2 ms | 3936.6 ms | 50542.3 ms |
| Uber_zap | LLGoNoLTO | 129159.7 ms | 125630.8 ms | 3528.9 ms | 48902.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 108563.7 ms | 105480.2 ms | 3083.5 ms | 79217.8 ms |
| Toml | LLGoFullLTONoGlobalDCE | 108256.8 ms | 105330.5 ms | 2926.2 ms | 79423.2 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 104877.3 ms | 101803.0 ms | 3074.2 ms | 76042.9 ms |
| XGo | LLGoDeadcodeDrop | 90191.8 ms | 84774.4 ms | 5417.4 ms | 35324.3 ms |
| XGo | LLGoNoLTO | 89753.7 ms | 85117.7 ms | 4636.0 ms | 35708.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 82183.4 ms | 79530.7 ms | 2652.8 ms | 54138.5 ms |
| Toml | LLGoFullLTOGlobalDCE | 76341.4 ms | 73899.6 ms | 2441.9 ms | 51079.0 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 75828.6 ms | 73295.3 ms | 2533.3 ms | 49911.8 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 74867.5 ms | 72817.7 ms | 2049.8 ms | 56863.3 ms |
| Gorm_schema | LLGoDeadcodeDrop | 73193.5 ms | 70531.0 ms | 2662.5 ms | 25475.6 ms |
| Gorm_schema | LLGoNoLTO | 72594.9 ms | 70080.4 ms | 2514.5 ms | 24777.4 ms |
| Toml | LLGoNoLTO | 69701.4 ms | 67315.3 ms | 2386.1 ms | 23976.0 ms |
| Toml | LLGoDeadcodeDrop | 64681.5 ms | 62294.7 ms | 2386.8 ms | 22416.2 ms |
| IXGo | Go | 64135.0 ms | 53204.3 ms | 10930.7 ms | 17675.5 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 54288.6 ms | 52531.4 ms | 1757.2 ms | 37287.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 51368.8 ms | 49780.4 ms | 1588.3 ms | 34187.6 ms |
| Dustin_humanize | LLGoNoLTO | 50138.9 ms | 48518.1 ms | 1620.8 ms | 18449.2 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 48732.8 ms | 46996.1 ms | 1736.8 ms | 18559.3 ms |
| Etcdctl | Go | 26993.8 ms | 23007.0 ms | 3986.8 ms | 8317.5 ms |
| XGo | Go | 16179.1 ms | 13796.9 ms | 2382.2 ms | 4900.2 ms |
| Aws_restjson | Go | 6382.2 ms | 5176.6 ms | 1205.6 ms | 2731.4 ms |
| Gorm_schema | Go | 4293.6 ms | 3574.6 ms | 719.0 ms | 1751.5 ms |
| Uber_zap | Go | 4197.6 ms | 3506.9 ms | 690.6 ms | 1788.3 ms |
| K8s_workqueue | Go | 3593.7 ms | 2932.2 ms | 661.6 ms | 1304.3 ms |
| Toml | Go | 1540.0 ms | 1225.6 ms | 314.4 ms | 765.3 ms |
| Dustin_humanize | Go | 590.9 ms | 424.1 ms | 166.9 ms | 301.3 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2418101.1 ms | 1701610.2 ms | 9 |
| LLGoFullLTOGlobalDCE | 2306858.5 ms | 1565675.2 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2046268.8 ms | 1391748.4 ms | 9 |
| LLGoDeadcodeDrop | 1391575.6 ms | 491312.9 ms | 9 |
| LLGoNoLTO | 1376731.6 ms | 465551.2 ms | 9 |
| Go | 127905.9 ms | 39535.3 ms | 9 |

Dependency download details are in `download-timings.log`.
