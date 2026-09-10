## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTONoGlobalDCE | 626599.4 ms | 619875.8 ms | 6723.6 ms | 410098.3 ms |
| IXGo | LLGoFullLTOGlobalDCE | 611135.8 ms | 604246.2 ms | 6889.6 ms | 403569.2 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 602308.1 ms | 595163.1 ms | 7145.0 ms | 386364.3 ms |
| IXGo | LLGoDeadcodeDrop | 427033.0 ms | 420482.1 ms | 6550.9 ms | 140166.9 ms |
| IXGo | LLGoNoLTO | 402468.1 ms | 396158.2 ms | 6309.9 ms | 131531.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 262260.8 ms | 257243.8 ms | 5017.0 ms | 162005.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 261296.5 ms | 256404.4 ms | 4892.1 ms | 162334.7 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 254185.4 ms | 249464.7 ms | 4720.6 ms | 158733.9 ms |
| Etcdctl | LLGoDeadcodeDrop | 189310.6 ms | 184885.6 ms | 4425.0 ms | 64616.6 ms |
| Etcdctl | LLGoNoLTO | 185732.7 ms | 181381.0 ms | 4351.6 ms | 62710.6 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 181916.5 ms | 178538.9 ms | 3377.7 ms | 127206.8 ms |
| XGo | LLGoFullLTOGlobalDCE | 174917.5 ms | 171709.6 ms | 3207.9 ms | 123812.3 ms |
| XGo | LLGoFullLTONoGlobalDCE | 174619.0 ms | 171453.4 ms | 3165.6 ms | 124586.8 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 136096.9 ms | 133714.6 ms | 2382.3 ms | 101377.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 126835.7 ms | 124531.7 ms | 2304.0 ms | 91158.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 125621.4 ms | 123130.2 ms | 2491.2 ms | 90254.4 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 108800.8 ms | 107019.6 ms | 1781.2 ms | 84724.2 ms |
| XGo | LLGoNoLTO | 106332.2 ms | 103362.7 ms | 2969.5 ms | 40633.9 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 103464.4 ms | 101625.1 ms | 1839.3 ms | 82251.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 102726.4 ms | 100936.1 ms | 1790.3 ms | 81163.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 102257.7 ms | 100339.7 ms | 1918.0 ms | 76026.0 ms |
| XGo | LLGoDeadcodeDrop | 101589.5 ms | 98747.1 ms | 2842.4 ms | 38535.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 99264.4 ms | 97438.7 ms | 1825.7 ms | 74903.1 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 89699.9 ms | 87916.6 ms | 1783.3 ms | 68022.3 ms |
| Aws_restjson | LLGoNoLTO | 79536.6 ms | 77468.0 ms | 2068.6 ms | 37414.0 ms |
| Aws_restjson | LLGoDeadcodeDrop | 79177.7 ms | 77054.3 ms | 2123.4 ms | 37822.1 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 62437.3 ms | 61100.5 ms | 1336.8 ms | 44333.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 62101.9 ms | 60623.3 ms | 1478.6 ms | 43663.7 ms |
| Uber_zap | LLGoDeadcodeDrop | 56947.4 ms | 55426.1 ms | 1521.3 ms | 26416.2 ms |
| Uber_zap | LLGoNoLTO | 54957.9 ms | 53451.2 ms | 1506.7 ms | 24734.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 52682.2 ms | 51249.9 ms | 1432.3 ms | 33966.9 ms |
| Toml | LLGoFullLTONoGlobalDCE | 50144.6 ms | 49006.4 ms | 1138.2 ms | 39210.5 ms |
| K8s_workqueue | LLGoNoLTO | 48446.0 ms | 46859.4 ms | 1586.6 ms | 22542.6 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 47200.3 ms | 45716.8 ms | 1483.5 ms | 22133.1 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 43748.4 ms | 42606.2 ms | 1142.1 ms | 31787.1 ms |
| IXGo | Go | 42422.2 ms | 39322.4 ms | 3099.8 ms | 12599.3 ms |
| Toml | LLGoFullLTOGlobalDCE | 42384.7 ms | 41331.1 ms | 1053.6 ms | 31289.7 ms |
| Gorm_schema | LLGoDeadcodeDrop | 35618.0 ms | 34347.0 ms | 1271.0 ms | 11806.2 ms |
| Gorm_schema | LLGoNoLTO | 35169.5 ms | 33959.1 ms | 1210.4 ms | 11489.0 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 34595.8 ms | 33682.3 ms | 913.6 ms | 27780.0 ms |
| Etcdctl | Go | 31746.2 ms | 29679.9 ms | 2066.3 ms | 9490.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 25445.1 ms | 24576.2 ms | 868.9 ms | 18463.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 23731.3 ms | 22879.8 ms | 851.4 ms | 16967.4 ms |
| Toml | LLGoDeadcodeDrop | 22294.6 ms | 21338.6 ms | 956.0 ms | 8495.6 ms |
| Toml | LLGoNoLTO | 22071.7 ms | 21089.4 ms | 982.3 ms | 8466.1 ms |
| XGo | Go | 18055.2 ms | 16798.7 ms | 1256.5 ms | 5334.7 ms |
| Dustin_humanize | LLGoNoLTO | 12405.5 ms | 11655.9 ms | 749.6 ms | 5551.8 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 12280.5 ms | 11550.1 ms | 730.3 ms | 5398.6 ms |
| Aws_restjson | Go | 7668.8 ms | 6954.4 ms | 714.5 ms | 3110.2 ms |
| Gorm_schema | Go | 5490.4 ms | 5093.6 ms | 396.9 ms | 2099.0 ms |
| Uber_zap | Go | 5075.8 ms | 4667.6 ms | 408.2 ms | 1966.9 ms |
| K8s_workqueue | Go | 4488.3 ms | 3998.1 ms | 490.2 ms | 1602.6 ms |
| Toml | Go | 1974.6 ms | 1746.4 ms | 228.2 ms | 926.6 ms |
| Dustin_humanize | Go | 776.6 ms | 629.5 ms | 147.1 ms | 372.2 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1550943.6 ms | 1073096.0 ms | 9 |
| LLGoFullLTOGlobalDCE | 1506108.0 ms | 1030357.9 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1484226.2 ms | 992600.4 ms | 9 |
| LLGoDeadcodeDrop | 971451.7 ms | 355390.9 ms | 9 |
| LLGoNoLTO | 947120.1 ms | 345073.6 ms | 9 |
| Go | 117698.2 ms | 37502.1 ms | 9 |

Dependency download details are in `download-timings.log`.
