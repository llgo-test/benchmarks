## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 923887.8 ms | 901729.2 ms | 22158.7 ms | 584834.8 ms |
| IXGo | LLGoFullLTOGlobalDCE | 916224.8 ms | 893867.1 ms | 22357.6 ms | 575767.3 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 857877.1 ms | 836117.2 ms | 21759.9 ms | 548310.2 ms |
| IXGo | LLGoDeadcodeDrop | 557861.6 ms | 535340.9 ms | 22520.7 ms | 175296.4 ms |
| IXGo | LLGoNoLTO | 508888.1 ms | 490242.2 ms | 18645.9 ms | 157934.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 469598.9 ms | 459316.9 ms | 10282.0 ms | 341558.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 466557.0 ms | 456506.1 ms | 10050.9 ms | 339360.6 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 466185.1 ms | 455909.2 ms | 10275.8 ms | 340673.0 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 359289.6 ms | 353109.7 ms | 6179.9 ms | 238576.9 ms |
| XGo | LLGoFullLTONoGlobalDCE | 347444.3 ms | 340186.6 ms | 7257.7 ms | 277474.3 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 341418.9 ms | 335259.7 ms | 6159.1 ms | 214117.3 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 324931.2 ms | 319028.8 ms | 5902.3 ms | 204589.4 ms |
| XGo | LLGoFullLTOGlobalDCE | 312773.6 ms | 305955.4 ms | 6818.2 ms | 240669.7 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 306889.7 ms | 300112.9 ms | 6776.8 ms | 236600.4 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 293832.8 ms | 288500.9 ms | 5331.9 ms | 202666.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 293261.7 ms | 287658.7 ms | 5603.0 ms | 203861.5 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 283687.5 ms | 278448.6 ms | 5238.9 ms | 198143.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 277723.0 ms | 272453.1 ms | 5269.8 ms | 185318.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 277017.3 ms | 271935.5 ms | 5081.9 ms | 182799.4 ms |
| Aws_restjson | LLGoNoLTO | 276775.9 ms | 272028.5 ms | 4747.4 ms | 84699.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 258242.0 ms | 253411.4 ms | 4830.6 ms | 169353.5 ms |
| Aws_restjson | LLGoDeadcodeDrop | 249820.4 ms | 244707.8 ms | 5112.7 ms | 79319.4 ms |
| Etcdctl | LLGoDeadcodeDrop | 241156.9 ms | 232533.9 ms | 8622.9 ms | 84123.3 ms |
| Etcdctl | LLGoNoLTO | 239593.0 ms | 231730.7 ms | 7862.3 ms | 82554.8 ms |
| Uber_zap | LLGoNoLTO | 208094.3 ms | 204172.1 ms | 3922.2 ms | 66239.2 ms |
| Uber_zap | LLGoDeadcodeDrop | 202726.5 ms | 198669.8 ms | 4056.6 ms | 66029.6 ms |
| K8s_workqueue | LLGoNoLTO | 199159.0 ms | 195306.2 ms | 3852.8 ms | 63236.5 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 195062.7 ms | 190866.5 ms | 4196.2 ms | 63958.9 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 150860.9 ms | 147623.9 ms | 3237.0 ms | 102964.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 148941.1 ms | 145755.4 ms | 3185.7 ms | 100187.1 ms |
| Toml | LLGoFullLTONoGlobalDCE | 142955.1 ms | 139951.1 ms | 3004.0 ms | 96317.8 ms |
| XGo | LLGoNoLTO | 135672.0 ms | 130630.7 ms | 5041.3 ms | 50232.9 ms |
| XGo | LLGoDeadcodeDrop | 133482.2 ms | 127726.4 ms | 5755.8 ms | 48941.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 127814.0 ms | 124766.2 ms | 3047.8 ms | 78298.1 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 127548.6 ms | 124635.0 ms | 2913.5 ms | 79774.0 ms |
| Toml | LLGoFullLTOGlobalDCE | 124643.3 ms | 121768.2 ms | 2875.1 ms | 78249.6 ms |
| Gorm_schema | LLGoDeadcodeDrop | 113194.0 ms | 110185.8 ms | 3008.3 ms | 39342.0 ms |
| Gorm_schema | LLGoNoLTO | 111548.6 ms | 108861.8 ms | 2686.8 ms | 38428.5 ms |
| Toml | LLGoNoLTO | 107877.4 ms | 105526.4 ms | 2351.1 ms | 36663.0 ms |
| Toml | LLGoDeadcodeDrop | 106119.6 ms | 103617.5 ms | 2502.1 ms | 36222.6 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 97796.5 ms | 95780.7 ms | 2015.8 ms | 69039.8 ms |
| IXGo | Go | 91942.1 ms | 80308.9 ms | 11633.2 ms | 25050.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 82258.5 ms | 80329.5 ms | 1929.0 ms | 52147.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 80331.3 ms | 78404.3 ms | 1927.0 ms | 50949.1 ms |
| Dustin_humanize | LLGoNoLTO | 72993.7 ms | 71298.1 ms | 1695.7 ms | 26884.1 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 72303.7 ms | 70545.3 ms | 1758.4 ms | 26687.9 ms |
| Etcdctl | Go | 36930.2 ms | 32655.7 ms | 4274.5 ms | 11065.9 ms |
| XGo | Go | 21073.9 ms | 18612.1 ms | 2461.7 ms | 6210.0 ms |
| Aws_restjson | Go | 8877.7 ms | 7624.1 ms | 1253.6 ms | 3971.8 ms |
| Gorm_schema | Go | 6460.1 ms | 5643.3 ms | 816.8 ms | 2620.9 ms |
| Uber_zap | Go | 5665.9 ms | 5011.9 ms | 654.0 ms | 2246.3 ms |
| K8s_workqueue | Go | 4991.3 ms | 4310.9 ms | 680.5 ms | 1774.6 ms |
| Toml | Go | 2168.8 ms | 1871.6 ms | 297.2 ms | 1030.3 ms |
| Dustin_humanize | Go | 860.6 ms | 697.5 ms | 163.0 ms | 418.5 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2999928.7 ms | 2074166.0 ms | 9 |
| LLGoFullLTOGlobalDCE | 2961874.6 ms | 1988480.3 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2898187.9 ms | 1929955.2 ms | 9 |
| LLGoDeadcodeDrop | 1871727.7 ms | 619921.1 ms | 9 |
| LLGoNoLTO | 1860602.1 ms | 606872.4 ms | 9 |
| Go | 178970.7 ms | 54389.0 ms | 9 |

Dependency download details are in `download-timings.log`.
