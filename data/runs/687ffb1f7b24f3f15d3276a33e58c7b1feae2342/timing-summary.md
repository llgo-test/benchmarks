## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTONoGlobalDCE | 843854.2 ms | 836746.4 ms | 7107.8 ms | 576735.5 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 839434.7 ms | 831937.9 ms | 7496.7 ms | 570203.4 ms |
| IXGo | LLGoFullLTOGlobalDCE | 795597.4 ms | 788805.8 ms | 6791.6 ms | 542624.0 ms |
| IXGo | LLGoDeadcodeDrop | 475881.8 ms | 469462.6 ms | 6419.2 ms | 159438.8 ms |
| IXGo | LLGoNoLTO | 443830.9 ms | 438066.9 ms | 5764.0 ms | 150790.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 297896.9 ms | 292844.5 ms | 5052.4 ms | 182550.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 293745.7 ms | 288868.6 ms | 4877.1 ms | 180379.8 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 290118.8 ms | 285424.7 ms | 4694.1 ms | 179246.3 ms |
| Etcdctl | LLGoDeadcodeDrop | 211312.2 ms | 207092.6 ms | 4219.6 ms | 69350.1 ms |
| Etcdctl | LLGoNoLTO | 210376.7 ms | 206142.2 ms | 4234.5 ms | 68905.3 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 203466.9 ms | 200025.9 ms | 3441.0 ms | 143095.4 ms |
| XGo | LLGoFullLTOGlobalDCE | 200175.1 ms | 196774.7 ms | 3400.5 ms | 140278.5 ms |
| XGo | LLGoFullLTONoGlobalDCE | 198086.8 ms | 194837.3 ms | 3249.5 ms | 139967.2 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 153677.5 ms | 151277.8 ms | 2399.7 ms | 114221.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 144459.4 ms | 141988.0 ms | 2471.4 ms | 104350.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 139854.9 ms | 137409.7 ms | 2445.2 ms | 99545.3 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 122282.1 ms | 120436.3 ms | 1845.8 ms | 94927.6 ms |
| XGo | LLGoDeadcodeDrop | 118066.8 ms | 115055.2 ms | 3011.5 ms | 44452.1 ms |
| XGo | LLGoNoLTO | 117231.9 ms | 114313.1 ms | 2918.8 ms | 43761.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 114521.6 ms | 112679.1 ms | 1842.5 ms | 90078.5 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 114002.2 ms | 112162.2 ms | 1840.0 ms | 89838.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 111402.6 ms | 109612.8 ms | 1789.8 ms | 83661.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 109899.4 ms | 108086.0 ms | 1813.4 ms | 82093.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 99076.8 ms | 97312.7 ms | 1764.1 ms | 74792.6 ms |
| Aws_restjson | LLGoDeadcodeDrop | 90912.2 ms | 88769.5 ms | 2142.6 ms | 42946.2 ms |
| Aws_restjson | LLGoNoLTO | 88586.3 ms | 86573.5 ms | 2012.7 ms | 42411.0 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 69170.0 ms | 67851.4 ms | 1318.6 ms | 49142.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 69106.8 ms | 67711.1 ms | 1395.7 ms | 48679.2 ms |
| Uber_zap | LLGoDeadcodeDrop | 61388.2 ms | 59644.1 ms | 1744.0 ms | 26698.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 60125.4 ms | 58749.9 ms | 1375.4 ms | 38639.2 ms |
| Uber_zap | LLGoNoLTO | 59005.4 ms | 57442.8 ms | 1562.6 ms | 25837.3 ms |
| Toml | LLGoFullLTONoGlobalDCE | 56514.0 ms | 55384.9 ms | 1129.1 ms | 43911.6 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 54042.8 ms | 52483.7 ms | 1559.1 ms | 25020.9 ms |
| K8s_workqueue | LLGoNoLTO | 52516.8 ms | 50952.6 ms | 1564.2 ms | 23793.6 ms |
| Toml | LLGoFullLTOGlobalDCE | 49479.6 ms | 48364.8 ms | 1114.8 ms | 35919.1 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 49117.5 ms | 48018.8 ms | 1098.7 ms | 36069.1 ms |
| IXGo | Go | 47332.2 ms | 44250.2 ms | 3082.0 ms | 13628.6 ms |
| Gorm_schema | LLGoDeadcodeDrop | 41344.3 ms | 40078.8 ms | 1265.5 ms | 13492.6 ms |
| Gorm_schema | LLGoNoLTO | 40075.3 ms | 38814.1 ms | 1261.2 ms | 13073.9 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 36092.1 ms | 35236.9 ms | 855.2 ms | 28617.9 ms |
| Etcdctl | Go | 34256.5 ms | 32187.9 ms | 2068.7 ms | 10349.5 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 27060.7 ms | 26167.0 ms | 893.6 ms | 19503.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 27018.2 ms | 26128.4 ms | 889.8 ms | 19326.4 ms |
| Toml | LLGoDeadcodeDrop | 25363.9 ms | 24311.9 ms | 1052.0 ms | 9445.5 ms |
| Toml | LLGoNoLTO | 25169.6 ms | 24119.8 ms | 1049.8 ms | 9343.7 ms |
| XGo | Go | 20149.0 ms | 18889.3 ms | 1259.7 ms | 5898.5 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 14130.4 ms | 13370.6 ms | 759.8 ms | 6071.7 ms |
| Dustin_humanize | LLGoNoLTO | 14053.0 ms | 13326.3 ms | 726.7 ms | 6010.8 ms |
| Aws_restjson | Go | 8606.3 ms | 7866.7 ms | 739.6 ms | 3596.6 ms |
| Gorm_schema | Go | 5893.6 ms | 5515.3 ms | 378.4 ms | 2289.8 ms |
| Uber_zap | Go | 5516.0 ms | 5087.0 ms | 429.0 ms | 2214.5 ms |
| K8s_workqueue | Go | 4810.0 ms | 4331.4 ms | 478.6 ms | 1687.2 ms |
| Toml | Go | 2195.8 ms | 1934.1 ms | 261.7 ms | 1032.4 ms |
| Dustin_humanize | Go | 834.8 ms | 676.0 ms | 158.8 ms | 400.6 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1883797.6 ms | 1316608.9 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1825890.6 ms | 1246314.5 ms | 9 |
| LLGoFullLTOGlobalDCE | 1805548.9 ms | 1245474.1 ms | 9 |
| LLGoDeadcodeDrop | 1092442.5 ms | 396916.8 ms | 9 |
| LLGoNoLTO | 1050846.0 ms | 383927.5 ms | 9 |
| Go | 129594.2 ms | 41097.6 ms | 9 |

Dependency download details are in `download-timings.log`.
