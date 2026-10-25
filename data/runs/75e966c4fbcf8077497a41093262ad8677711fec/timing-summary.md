## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 789837.0 ms | 776548.3 ms | 13288.7 ms | 513621.6 ms |
| IXGo | LLGoFullLTOGlobalDCE | 779047.1 ms | 766090.5 ms | 12956.6 ms | 507125.7 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 776876.3 ms | 762971.2 ms | 13905.1 ms | 510677.9 ms |
| IXGo | LLGoDeadcodeDrop | 441916.1 ms | 428271.4 ms | 13644.8 ms | 139262.2 ms |
| IXGo | LLGoNoLTO | 441619.7 ms | 431933.0 ms | 9686.7 ms | 135094.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 393657.9 ms | 387745.1 ms | 5912.8 ms | 296141.9 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 390432.3 ms | 384526.4 ms | 5905.9 ms | 296465.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 388874.7 ms | 382860.4 ms | 6014.3 ms | 292381.7 ms |
| XGo | LLGoFullLTONoGlobalDCE | 294723.1 ms | 290439.8 ms | 4283.4 ms | 242906.0 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 290297.2 ms | 286519.0 ms | 3778.2 ms | 205682.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 267503.3 ms | 263800.2 ms | 3703.2 ms | 178874.7 ms |
| XGo | LLGoFullLTOGlobalDCE | 265146.9 ms | 261047.7 ms | 4099.2 ms | 209678.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 261050.8 ms | 257570.6 ms | 3480.2 ms | 173909.7 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 257721.5 ms | 253887.9 ms | 3833.6 ms | 203941.7 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 253379.0 ms | 250070.7 ms | 3308.4 ms | 186302.0 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 236079.2 ms | 232686.4 ms | 3392.8 ms | 176010.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 235355.6 ms | 231991.7 ms | 3363.9 ms | 174628.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 217953.2 ms | 214892.1 ms | 3061.1 ms | 154393.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 217555.5 ms | 214382.9 ms | 3172.5 ms | 154546.9 ms |
| Aws_restjson | LLGoDeadcodeDrop | 208226.7 ms | 204959.6 ms | 3267.1 ms | 73032.9 ms |
| Aws_restjson | LLGoNoLTO | 205838.9 ms | 202822.0 ms | 3016.9 ms | 72247.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 202861.7 ms | 199670.7 ms | 3191.0 ms | 142703.6 ms |
| Etcdctl | LLGoDeadcodeDrop | 190474.4 ms | 185506.7 ms | 4967.7 ms | 68447.6 ms |
| Etcdctl | LLGoNoLTO | 190122.2 ms | 185578.8 ms | 4543.5 ms | 66666.8 ms |
| Uber_zap | LLGoDeadcodeDrop | 171437.4 ms | 168736.4 ms | 2701.0 ms | 64613.2 ms |
| Uber_zap | LLGoNoLTO | 164116.4 ms | 161696.2 ms | 2420.2 ms | 61555.0 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 159173.0 ms | 156586.4 ms | 2586.6 ms | 61214.8 ms |
| K8s_workqueue | LLGoNoLTO | 158111.3 ms | 155694.8 ms | 2416.5 ms | 59535.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 126385.6 ms | 124253.1 ms | 2132.5 ms | 90221.1 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 125744.9 ms | 123609.9 ms | 2135.0 ms | 91212.0 ms |
| Toml | LLGoFullLTONoGlobalDCE | 117215.1 ms | 115304.8 ms | 1910.3 ms | 83585.6 ms |
| XGo | LLGoDeadcodeDrop | 110585.5 ms | 107316.5 ms | 3269.0 ms | 42911.9 ms |
| XGo | LLGoNoLTO | 108823.5 ms | 106003.0 ms | 2820.5 ms | 42307.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 102900.9 ms | 100990.4 ms | 1910.5 ms | 67145.0 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 98509.7 ms | 96721.2 ms | 1788.5 ms | 64881.8 ms |
| Toml | LLGoFullLTOGlobalDCE | 96649.3 ms | 94806.0 ms | 1843.3 ms | 64533.0 ms |
| Gorm_schema | LLGoNoLTO | 89633.7 ms | 87966.2 ms | 1667.5 ms | 30315.8 ms |
| Gorm_schema | LLGoDeadcodeDrop | 88984.0 ms | 87171.5 ms | 1812.4 ms | 30668.4 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 82359.4 ms | 80978.2 ms | 1381.2 ms | 61569.7 ms |
| Toml | LLGoDeadcodeDrop | 81235.9 ms | 79571.2 ms | 1664.7 ms | 27682.0 ms |
| Toml | LLGoNoLTO | 80647.0 ms | 79080.6 ms | 1566.4 ms | 27241.0 ms |
| IXGo | Go | 73017.4 ms | 67479.8 ms | 5537.5 ms | 20238.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 64955.7 ms | 63616.2 ms | 1339.6 ms | 43226.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 63931.0 ms | 62553.9 ms | 1377.1 ms | 42617.9 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 56285.7 ms | 55061.7 ms | 1224.0 ms | 20766.6 ms |
| Dustin_humanize | LLGoNoLTO | 56037.2 ms | 54920.0 ms | 1117.2 ms | 20512.9 ms |
| Etcdctl | Go | 28883.9 ms | 26799.1 ms | 2084.9 ms | 8611.4 ms |
| XGo | Go | 16335.2 ms | 15154.6 ms | 1180.6 ms | 4773.3 ms |
| Aws_restjson | Go | 6734.4 ms | 6095.7 ms | 638.7 ms | 2683.0 ms |
| Gorm_schema | Go | 5089.9 ms | 4722.2 ms | 367.7 ms | 1927.3 ms |
| Uber_zap | Go | 4755.7 ms | 4408.3 ms | 347.4 ms | 1835.7 ms |
| K8s_workqueue | Go | 4056.5 ms | 3670.1 ms | 386.4 ms | 1500.1 ms |
| Toml | Go | 1775.0 ms | 1604.5 ms | 170.5 ms | 844.3 ms |
| Dustin_humanize | Go | 722.6 ms | 612.6 ms | 110.0 ms | 343.6 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2567106.6 ms | 1854411.4 ms | 9 |
| LLGoFullLTOGlobalDCE | 2440846.7 ms | 1714454.3 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2389050.6 ms | 1660118.6 ms | 9 |
| LLGoDeadcodeDrop | 1508318.6 ms | 528599.7 ms | 9 |
| LLGoNoLTO | 1494949.9 ms | 515476.6 ms | 9 |
| Go | 141370.6 ms | 42756.9 ms | 9 |

Dependency download details are in `download-timings.log`.
