## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 554738.5 ms | 543429.9 ms | 11308.6 ms | 298204.9 ms |
| IXGo | LLGoFullLTOGlobalDCE | 546291.9 ms | 535819.1 ms | 10472.8 ms | 289857.9 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 539616.5 ms | 528764.5 ms | 10851.9 ms | 291661.9 ms |
| IXGo | LLGoDeadcodeDrop | 411135.2 ms | 398205.2 ms | 12930.0 ms | 121751.3 ms |
| IXGo | LLGoNoLTO | 409222.9 ms | 400398.6 ms | 8824.3 ms | 116676.5 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 254262.7 ms | 249367.4 ms | 4895.2 ms | 164385.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 249549.1 ms | 244587.0 ms | 4962.1 ms | 159757.4 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 246854.0 ms | 242114.0 ms | 4740.0 ms | 160074.8 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 198258.6 ms | 194907.4 ms | 3351.1 ms | 121553.7 ms |
| Aws_restjson | LLGoDeadcodeDrop | 188860.6 ms | 186038.0 ms | 2822.6 ms | 65507.9 ms |
| Aws_restjson | LLGoNoLTO | 184435.9 ms | 181620.6 ms | 2815.3 ms | 63991.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 184266.1 ms | 181064.8 ms | 3201.2 ms | 107057.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 181880.9 ms | 178829.0 ms | 3051.9 ms | 104949.6 ms |
| XGo | LLGoFullLTOGlobalDCE | 178168.8 ms | 175103.5 ms | 3065.2 ms | 128194.9 ms |
| XGo | LLGoFullLTONoGlobalDCE | 177104.9 ms | 173822.2 ms | 3282.7 ms | 128958.8 ms |
| Etcdctl | LLGoDeadcodeDrop | 175762.3 ms | 171163.8 ms | 4598.4 ms | 58444.4 ms |
| Etcdctl | LLGoNoLTO | 172152.6 ms | 168175.3 ms | 3977.4 ms | 55788.5 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 170504.7 ms | 167408.6 ms | 3096.2 ms | 122902.7 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 160654.7 ms | 157839.4 ms | 2815.3 ms | 104939.3 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 156505.1 ms | 153711.4 ms | 2793.7 ms | 102379.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 154865.0 ms | 152159.2 ms | 2705.8 ms | 100132.2 ms |
| Uber_zap | LLGoDeadcodeDrop | 154298.4 ms | 152053.1 ms | 2245.3 ms | 57345.4 ms |
| Uber_zap | LLGoNoLTO | 151467.1 ms | 149088.3 ms | 2378.9 ms | 56327.2 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 150492.4 ms | 147789.0 ms | 2703.4 ms | 93094.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 148996.0 ms | 146389.3 ms | 2606.8 ms | 92660.8 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 147850.2 ms | 145472.2 ms | 2378.1 ms | 55087.4 ms |
| K8s_workqueue | LLGoNoLTO | 144612.8 ms | 142131.7 ms | 2481.1 ms | 54253.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 143561.5 ms | 140767.0 ms | 2794.5 ms | 87785.5 ms |
| XGo | LLGoDeadcodeDrop | 99531.1 ms | 96458.5 ms | 3072.6 ms | 36992.2 ms |
| XGo | LLGoNoLTO | 97550.5 ms | 95076.1 ms | 2474.4 ms | 35228.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 82218.7 ms | 80477.8 ms | 1740.9 ms | 50080.2 ms |
| Gorm_schema | LLGoDeadcodeDrop | 81928.3 ms | 80361.4 ms | 1566.9 ms | 27384.2 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 81695.4 ms | 80014.0 ms | 1681.5 ms | 50334.0 ms |
| Gorm_schema | LLGoNoLTO | 79882.7 ms | 78395.9 ms | 1486.8 ms | 26832.6 ms |
| Toml | LLGoDeadcodeDrop | 76707.8 ms | 75170.4 ms | 1537.4 ms | 25536.5 ms |
| Toml | LLGoNoLTO | 75425.8 ms | 73927.5 ms | 1498.3 ms | 25319.8 ms |
| Toml | LLGoFullLTONoGlobalDCE | 72283.1 ms | 70668.7 ms | 1614.4 ms | 43941.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 71639.0 ms | 69966.7 ms | 1672.3 ms | 39557.5 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 68116.3 ms | 66529.7 ms | 1586.6 ms | 37907.6 ms |
| Toml | LLGoFullLTOGlobalDCE | 68072.8 ms | 66481.3 ms | 1591.5 ms | 38199.0 ms |
| IXGo | Go | 66449.3 ms | 61677.7 ms | 4771.6 ms | 18099.8 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 53128.9 ms | 51972.8 ms | 1156.1 ms | 34034.0 ms |
| Dustin_humanize | LLGoNoLTO | 52462.1 ms | 51400.9 ms | 1061.3 ms | 18857.6 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 51813.4 ms | 50767.8 ms | 1045.6 ms | 18749.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 45764.7 ms | 44638.6 ms | 1126.1 ms | 26018.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 45270.6 ms | 44160.6 ms | 1110.0 ms | 25764.7 ms |
| Etcdctl | Go | 27727.2 ms | 25751.6 ms | 1975.6 ms | 8210.6 ms |
| XGo | Go | 16198.1 ms | 15013.1 ms | 1185.0 ms | 4891.3 ms |
| Aws_restjson | Go | 6767.7 ms | 6175.6 ms | 592.1 ms | 2696.6 ms |
| Gorm_schema | Go | 4794.4 ms | 4432.6 ms | 361.8 ms | 1800.1 ms |
| Uber_zap | Go | 4521.3 ms | 4166.8 ms | 354.5 ms | 1706.4 ms |
| K8s_workqueue | Go | 3954.0 ms | 3585.6 ms | 368.5 ms | 1375.4 ms |
| Toml | Go | 1679.0 ms | 1504.9 ms | 174.2 ms | 755.4 ms |
| Dustin_humanize | Go | 666.1 ms | 549.8 ms | 116.3 ms | 316.7 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1686101.1 ms | 1037877.8 ms | 9 |
| LLGoFullLTOGlobalDCE | 1655807.9 ms | 989849.9 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1642851.7 ms | 976660.5 ms | 9 |
| LLGoDeadcodeDrop | 1387887.4 ms | 466798.5 ms | 9 |
| LLGoNoLTO | 1367212.5 ms | 453275.9 ms | 9 |
| Go | 132757.1 ms | 39852.4 ms | 9 |

Dependency download details are in `download-timings.log`.
