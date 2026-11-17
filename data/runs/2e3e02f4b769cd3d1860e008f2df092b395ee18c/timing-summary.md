## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 651756.0 ms | 635742.6 ms | 16013.5 ms | 434496.3 ms |
| IXGo | LLGoFullLTOGlobalDCE | 631031.5 ms | 614407.1 ms | 16624.4 ms | 417474.9 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 630424.4 ms | 614500.6 ms | 15923.8 ms | 423727.7 ms |
| IXGo | LLGoDeadcodeDrop | 367317.3 ms | 350019.2 ms | 17298.1 ms | 119520.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 343686.6 ms | 335942.1 ms | 7744.5 ms | 256182.1 ms |
| IXGo | LLGoNoLTO | 341084.6 ms | 327768.7 ms | 13315.9 ms | 106912.9 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 336675.9 ms | 329255.0 ms | 7420.9 ms | 253820.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 333577.3 ms | 326343.1 ms | 7234.1 ms | 249711.1 ms |
| XGo | LLGoFullLTONoGlobalDCE | 253143.1 ms | 248029.0 ms | 5114.1 ms | 205291.2 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 227453.6 ms | 223372.9 ms | 4080.8 ms | 156707.5 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 227082.0 ms | 221908.6 ms | 5173.4 ms | 176879.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 216863.8 ms | 212533.3 ms | 4330.5 ms | 140070.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 213791.9 ms | 209723.6 ms | 4068.3 ms | 139572.2 ms |
| XGo | LLGoFullLTOGlobalDCE | 211424.4 ms | 206862.2 ms | 4562.2 ms | 164857.4 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 191614.4 ms | 188001.3 ms | 3613.1 ms | 138412.1 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 189601.3 ms | 185833.0 ms | 3768.3 ms | 137040.9 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 188550.5 ms | 184931.6 ms | 3618.9 ms | 136579.5 ms |
| Aws_restjson | LLGoNoLTO | 182088.7 ms | 178304.0 ms | 3784.7 ms | 57221.2 ms |
| Aws_restjson | LLGoDeadcodeDrop | 178912.3 ms | 175068.5 ms | 3843.7 ms | 57590.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 176873.9 ms | 173281.4 ms | 3592.5 ms | 120304.2 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 176863.0 ms | 173186.3 ms | 3676.7 ms | 121874.1 ms |
| Etcdctl | LLGoNoLTO | 175264.0 ms | 169220.9 ms | 6043.2 ms | 60639.6 ms |
| Etcdctl | LLGoDeadcodeDrop | 168340.5 ms | 162016.9 ms | 6323.6 ms | 59056.8 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 159553.3 ms | 156200.8 ms | 3352.5 ms | 107761.0 ms |
| Uber_zap | LLGoNoLTO | 150678.2 ms | 147519.6 ms | 3158.7 ms | 48652.3 ms |
| Uber_zap | LLGoDeadcodeDrop | 145407.4 ms | 142140.0 ms | 3267.4 ms | 48203.9 ms |
| K8s_workqueue | LLGoNoLTO | 140592.2 ms | 137450.3 ms | 3141.9 ms | 45275.0 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 135285.2 ms | 132180.8 ms | 3104.4 ms | 45421.4 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 114734.6 ms | 112038.9 ms | 2695.7 ms | 81989.7 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 109941.4 ms | 107457.9 ms | 2483.5 ms | 77462.1 ms |
| Toml | LLGoFullLTONoGlobalDCE | 108578.2 ms | 106143.1 ms | 2435.1 ms | 76575.1 ms |
| XGo | LLGoNoLTO | 97968.5 ms | 94203.0 ms | 3765.5 ms | 36486.4 ms |
| XGo | LLGoDeadcodeDrop | 96155.9 ms | 91935.0 ms | 4220.9 ms | 35438.8 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 93138.5 ms | 90852.0 ms | 2286.5 ms | 61436.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 90421.2 ms | 88162.7 ms | 2258.5 ms | 58106.0 ms |
| Toml | LLGoFullLTOGlobalDCE | 89454.6 ms | 87243.8 ms | 2210.8 ms | 59007.0 ms |
| Gorm_schema | LLGoDeadcodeDrop | 82057.9 ms | 79762.3 ms | 2295.6 ms | 29048.8 ms |
| Gorm_schema | LLGoNoLTO | 80633.6 ms | 78457.6 ms | 2176.0 ms | 28155.1 ms |
| Toml | LLGoDeadcodeDrop | 76402.8 ms | 74326.4 ms | 2076.5 ms | 26689.2 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 74752.4 ms | 73103.0 ms | 1649.5 ms | 55058.7 ms |
| Toml | LLGoNoLTO | 73401.9 ms | 71672.6 ms | 1729.3 ms | 25714.8 ms |
| IXGo | Go | 63264.8 ms | 55113.7 ms | 8151.2 ms | 17647.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 57518.6 ms | 56063.7 ms | 1454.9 ms | 37898.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 56336.6 ms | 54924.5 ms | 1412.1 ms | 36945.1 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 52520.4 ms | 51022.3 ms | 1498.1 ms | 19953.9 ms |
| Dustin_humanize | LLGoNoLTO | 51095.8 ms | 49806.2 ms | 1289.6 ms | 19197.0 ms |
| Etcdctl | Go | 25031.4 ms | 22264.8 ms | 2766.7 ms | 7722.4 ms |
| XGo | Go | 14857.5 ms | 13157.1 ms | 1700.4 ms | 4368.3 ms |
| Aws_restjson | Go | 5938.6 ms | 5116.8 ms | 821.8 ms | 2566.3 ms |
| Gorm_schema | Go | 4511.9 ms | 3933.3 ms | 578.6 ms | 1774.3 ms |
| Uber_zap | Go | 4136.7 ms | 3637.5 ms | 499.2 ms | 1745.3 ms |
| K8s_workqueue | Go | 3557.4 ms | 3081.6 ms | 475.8 ms | 1435.8 ms |
| Toml | Go | 1555.9 ms | 1343.2 ms | 212.6 ms | 720.0 ms |
| Dustin_humanize | Go | 599.2 ms | 508.7 ms | 90.5 ms | 291.6 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2125927.3 ms | 1528161.8 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2016893.9 ms | 1393134.3 ms | 9 |
| LLGoFullLTOGlobalDCE | 2012022.0 ms | 1403944.9 ms | 9 |
| LLGoDeadcodeDrop | 1302399.7 ms | 440923.9 ms | 9 |
| LLGoNoLTO | 1292807.5 ms | 428254.2 ms | 9 |
| Go | 123453.4 ms | 38271.3 ms | 9 |

Dependency download details are in `download-timings.log`.
