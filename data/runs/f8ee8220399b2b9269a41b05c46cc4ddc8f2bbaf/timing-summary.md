## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 630379.1 ms | 617673.4 ms | 12705.7 ms | 316641.4 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 614711.1 ms | 603705.0 ms | 11006.1 ms | 311639.4 ms |
| IXGo | LLGoFullLTOGlobalDCE | 609244.2 ms | 597658.6 ms | 11585.7 ms | 308245.8 ms |
| IXGo | LLGoDeadcodeDrop | 498782.5 ms | 488400.0 ms | 10382.5 ms | 149747.4 ms |
| IXGo | LLGoNoLTO | 453244.9 ms | 443465.0 ms | 9779.9 ms | 131820.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 302680.9 ms | 296879.6 ms | 5801.3 ms | 173982.5 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 294139.5 ms | 288997.4 ms | 5142.2 ms | 170981.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 292618.2 ms | 287898.1 ms | 4720.0 ms | 168795.2 ms |
| Etcdctl | LLGoDeadcodeDrop | 226398.0 ms | 221723.0 ms | 4675.0 ms | 72823.3 ms |
| Etcdctl | LLGoNoLTO | 223325.4 ms | 218947.9 ms | 4377.6 ms | 70922.2 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 195895.5 ms | 193542.9 ms | 2352.6 ms | 158510.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 189193.1 ms | 186918.7 ms | 2274.4 ms | 151673.1 ms |
| XGo | LLGoFullLTONoGlobalDCE | 185193.9 ms | 181789.8 ms | 3404.1 ms | 127559.8 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 184382.2 ms | 181023.9 ms | 3358.2 ms | 127306.5 ms |
| XGo | LLGoFullLTOGlobalDCE | 183945.0 ms | 180597.0 ms | 3348.0 ms | 126560.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 174238.4 ms | 171880.0 ms | 2358.3 ms | 136119.9 ms |
| Aws_restjson | LLGoDeadcodeDrop | 153663.0 ms | 151499.8 ms | 2163.2 ms | 108329.8 ms |
| Aws_restjson | LLGoNoLTO | 151385.1 ms | 149307.1 ms | 2078.0 ms | 106793.8 ms |
| XGo | LLGoDeadcodeDrop | 113224.9 ms | 110128.7 ms | 3096.2 ms | 42112.8 ms |
| XGo | LLGoNoLTO | 110964.6 ms | 108123.3 ms | 2841.3 ms | 40794.9 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 110726.9 ms | 108960.8 ms | 1766.1 ms | 83829.6 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 105339.7 ms | 103449.4 ms | 1890.3 ms | 82178.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 104918.3 ms | 103118.6 ms | 1799.8 ms | 80739.9 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 103282.9 ms | 101475.6 ms | 1807.4 ms | 74631.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 101732.9 ms | 99963.9 ms | 1768.9 ms | 74479.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 91610.3 ms | 89432.6 ms | 2177.7 ms | 68299.5 ms |
| IXGo | Go | 84295.3 ms | 79196.2 ms | 5099.2 ms | 23189.5 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 64834.1 ms | 63477.0 ms | 1357.1 ms | 44112.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 64307.0 ms | 62808.6 ms | 1498.4 ms | 43487.6 ms |
| Uber_zap | LLGoDeadcodeDrop | 58415.4 ms | 56906.3 ms | 1509.1 ms | 24831.6 ms |
| Uber_zap | LLGoNoLTO | 56981.1 ms | 55408.5 ms | 1572.6 ms | 24664.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 53928.8 ms | 52579.5 ms | 1349.3 ms | 32793.4 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 51205.7 ms | 49633.4 ms | 1572.3 ms | 23470.7 ms |
| Toml | LLGoFullLTONoGlobalDCE | 50827.5 ms | 49682.3 ms | 1145.2 ms | 38331.7 ms |
| K8s_workqueue | LLGoNoLTO | 49535.8 ms | 48147.7 ms | 1388.1 ms | 22090.0 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 42655.5 ms | 41604.1 ms | 1051.5 ms | 29573.1 ms |
| Toml | LLGoFullLTOGlobalDCE | 42553.9 ms | 41488.0 ms | 1065.9 ms | 29869.1 ms |
| Gorm_schema | LLGoDeadcodeDrop | 41910.0 ms | 40617.6 ms | 1292.4 ms | 13931.4 ms |
| Gorm_schema | LLGoNoLTO | 40877.9 ms | 39703.7 ms | 1174.1 ms | 13404.8 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 35819.6 ms | 34906.7 ms | 913.0 ms | 28149.8 ms |
| Etcdctl | Go | 33662.3 ms | 31610.7 ms | 2051.6 ms | 10271.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 26923.6 ms | 26022.1 ms | 901.5 ms | 18956.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 26206.2 ms | 25351.5 ms | 854.7 ms | 18523.1 ms |
| Toml | LLGoDeadcodeDrop | 25877.5 ms | 24835.1 ms | 1042.4 ms | 9574.7 ms |
| Toml | LLGoNoLTO | 24522.9 ms | 23534.3 ms | 988.7 ms | 9371.7 ms |
| XGo | Go | 19137.6 ms | 17918.5 ms | 1219.1 ms | 5720.4 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 14205.9 ms | 13428.4 ms | 777.5 ms | 6139.8 ms |
| Dustin_humanize | LLGoNoLTO | 13887.4 ms | 13132.4 ms | 755.0 ms | 5932.5 ms |
| Aws_restjson | Go | 8110.5 ms | 7444.8 ms | 665.8 ms | 3302.8 ms |
| Gorm_schema | Go | 5813.7 ms | 5427.2 ms | 386.5 ms | 2219.2 ms |
| Uber_zap | Go | 5389.6 ms | 4951.1 ms | 438.4 ms | 2153.0 ms |
| K8s_workqueue | Go | 5082.3 ms | 4453.7 ms | 628.6 ms | 2208.2 ms |
| Toml | Go | 2206.4 ms | 1877.5 ms | 329.0 ms | 1241.8 ms |
| Dustin_humanize | Go | 831.0 ms | 682.1 ms | 148.9 ms | 389.6 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1657487.8 ms | 1045292.8 ms | 9 |
| LLGoFullLTOGlobalDCE | 1614718.8 ms | 1002373.8 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1610081.7 ms | 978305.0 ms | 9 |
| LLGoDeadcodeDrop | 1183682.9 ms | 450961.6 ms | 9 |
| LLGoNoLTO | 1124725.2 ms | 425794.0 ms | 9 |
| Go | 164528.7 ms | 50696.2 ms | 9 |

Dependency download details are in `download-timings.log`.
