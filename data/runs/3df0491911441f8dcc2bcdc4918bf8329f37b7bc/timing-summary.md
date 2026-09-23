## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 584899.9 ms | 572652.4 ms | 12247.5 ms | 300446.5 ms |
| IXGo | LLGoFullLTOGlobalDCE | 580458.8 ms | 568513.4 ms | 11945.4 ms | 294243.5 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 579901.0 ms | 568943.4 ms | 10957.7 ms | 295290.8 ms |
| IXGo | LLGoDeadcodeDrop | 446379.2 ms | 435510.2 ms | 10869.1 ms | 132725.1 ms |
| IXGo | LLGoNoLTO | 424284.2 ms | 414393.9 ms | 9890.3 ms | 126667.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 265894.6 ms | 261067.3 ms | 4827.3 ms | 163178.5 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 262176.9 ms | 257511.1 ms | 4665.8 ms | 160532.6 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 258973.1 ms | 254171.5 ms | 4801.6 ms | 160841.3 ms |
| Etcdctl | LLGoDeadcodeDrop | 196793.5 ms | 192546.0 ms | 4247.6 ms | 65730.7 ms |
| Etcdctl | LLGoNoLTO | 193909.8 ms | 189579.3 ms | 4330.5 ms | 65235.7 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 186115.3 ms | 182810.8 ms | 3304.5 ms | 127811.7 ms |
| XGo | LLGoFullLTOGlobalDCE | 183917.5 ms | 180597.0 ms | 3320.5 ms | 126812.4 ms |
| XGo | LLGoFullLTONoGlobalDCE | 183178.4 ms | 179900.3 ms | 3278.0 ms | 126950.4 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 140840.7 ms | 138447.2 ms | 2393.5 ms | 102612.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 129976.0 ms | 127318.5 ms | 2657.5 ms | 90426.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 129000.9 ms | 126459.5 ms | 2541.5 ms | 89476.9 ms |
| XGo | LLGoDeadcodeDrop | 115416.4 ms | 112617.1 ms | 2799.3 ms | 43028.2 ms |
| XGo | LLGoNoLTO | 112758.2 ms | 109942.5 ms | 2815.7 ms | 42220.9 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 111629.2 ms | 109735.9 ms | 1893.4 ms | 84296.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 102562.0 ms | 100666.9 ms | 1895.1 ms | 74321.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 101511.3 ms | 99601.3 ms | 1910.0 ms | 73514.4 ms |
| Aws_restjson | LLGoDeadcodeDrop | 88749.7 ms | 86592.8 ms | 2156.9 ms | 41299.8 ms |
| Aws_restjson | LLGoNoLTO | 86009.0 ms | 83796.8 ms | 2212.3 ms | 40355.4 ms |
| IXGo | Go | 84864.1 ms | 79843.5 ms | 5020.6 ms | 23427.7 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 64121.7 ms | 62692.8 ms | 1428.9 ms | 43292.0 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 62845.6 ms | 61492.4 ms | 1353.2 ms | 43133.7 ms |
| Uber_zap | LLGoDeadcodeDrop | 59913.8 ms | 58275.5 ms | 1638.3 ms | 26488.6 ms |
| Uber_zap | LLGoNoLTO | 59153.8 ms | 57654.9 ms | 1499.0 ms | 25696.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 53669.4 ms | 52310.5 ms | 1358.8 ms | 32559.7 ms |
| Toml | LLGoFullLTONoGlobalDCE | 50033.9 ms | 48879.8 ms | 1154.0 ms | 37510.9 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 43085.7 ms | 41942.2 ms | 1143.5 ms | 29635.8 ms |
| Toml | LLGoFullLTOGlobalDCE | 42580.4 ms | 41446.4 ms | 1133.9 ms | 29595.1 ms |
| Gorm_schema | LLGoDeadcodeDrop | 41190.4 ms | 39931.6 ms | 1258.9 ms | 14016.5 ms |
| Gorm_schema | LLGoNoLTO | 40368.4 ms | 39121.8 ms | 1246.5 ms | 13505.2 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 35322.7 ms | 34457.4 ms | 865.3 ms | 27321.5 ms |
| Etcdctl | Go | 34258.4 ms | 32178.9 ms | 2079.4 ms | 10377.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 26903.4 ms | 26017.1 ms | 886.3 ms | 18700.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 26600.6 ms | 25754.8 ms | 845.7 ms | 18551.7 ms |
| Toml | LLGoDeadcodeDrop | 25203.8 ms | 24144.0 ms | 1059.8 ms | 9386.6 ms |
| Toml | LLGoNoLTO | 24762.2 ms | 23761.8 ms | 1000.3 ms | 9235.6 ms |
| XGo | Go | 19529.1 ms | 18245.6 ms | 1283.5 ms | 5986.2 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 14455.1 ms | 13689.6 ms | 765.5 ms | 6163.0 ms |
| Dustin_humanize | LLGoNoLTO | 14369.4 ms | 13523.0 ms | 846.5 ms | 6016.1 ms |
| Aws_restjson | Go | 8367.8 ms | 7471.4 ms | 896.4 ms | 3831.1 ms |
| Gorm_schema | Go | 5892.6 ms | 5458.6 ms | 434.1 ms | 2384.1 ms |
| Uber_zap | Go | 5344.7 ms | 4942.3 ms | 402.4 ms | 2061.1 ms |
| K8s_workqueue | Go | 4837.5 ms | 4305.2 ms | 532.2 ms | 2224.6 ms |
| Toml | Go | 2113.9 ms | 1850.3 ms | 263.5 ms | 1102.5 ms |
| Dustin_humanize | Go | 845.7 ms | 669.0 ms | 176.7 ms | 402.9 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1422724.7 ms | 877957.5 ms | 8 |
| LLGoFullLTOGlobalDCEPlugin | 1393106.1 ms | 837081.2 ms | 8 |
| LLGoFullLTOGlobalDCE | 1390368.2 ms | 836018.8 ms | 8 |
| LLGoDeadcodeDrop | 988101.9 ms | 338838.5 ms | 8 |
| LLGoNoLTO | 955615.0 ms | 328932.7 ms | 8 |
| Go | 166053.7 ms | 51798.0 ms | 9 |

Dependency download details are in `download-timings.log`.
