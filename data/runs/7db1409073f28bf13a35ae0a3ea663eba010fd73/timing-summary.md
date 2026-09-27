## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 529107.8 ms | 516930.4 ms | 12177.4 ms | 278161.9 ms |
| IXGo | LLGoFullLTOGlobalDCE | 522775.0 ms | 509617.8 ms | 13157.3 ms | 288099.5 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 500141.8 ms | 488558.9 ms | 11583.0 ms | 268426.5 ms |
| IXGo | LLGoDeadcodeDrop | 414450.8 ms | 402960.3 ms | 11490.6 ms | 124083.7 ms |
| IXGo | LLGoNoLTO | 390325.5 ms | 380361.9 ms | 9963.6 ms | 116503.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 259709.0 ms | 254672.5 ms | 5036.5 ms | 158713.5 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 253010.7 ms | 248307.8 ms | 4702.9 ms | 156056.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 250780.5 ms | 246240.2 ms | 4540.3 ms | 153807.5 ms |
| Etcdctl | LLGoDeadcodeDrop | 191165.1 ms | 187028.0 ms | 4137.1 ms | 63503.0 ms |
| Etcdctl | LLGoNoLTO | 185175.0 ms | 181282.5 ms | 3892.5 ms | 61054.8 ms |
| XGo | LLGoFullLTONoGlobalDCE | 178510.2 ms | 175114.8 ms | 3395.4 ms | 122795.7 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 177356.4 ms | 174027.6 ms | 3328.8 ms | 120845.0 ms |
| XGo | LLGoFullLTOGlobalDCE | 176046.0 ms | 172792.4 ms | 3253.6 ms | 120555.9 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 134237.5 ms | 131795.1 ms | 2442.4 ms | 96972.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 124112.0 ms | 121604.8 ms | 2507.3 ms | 85909.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 122757.2 ms | 120357.2 ms | 2400.0 ms | 84502.6 ms |
| XGo | LLGoDeadcodeDrop | 110815.4 ms | 107841.4 ms | 2974.0 ms | 41208.5 ms |
| XGo | LLGoNoLTO | 108576.8 ms | 105558.0 ms | 3018.8 ms | 40510.7 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 107359.6 ms | 105553.2 ms | 1806.4 ms | 81428.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 101769.2 ms | 99817.3 ms | 1951.8 ms | 78862.2 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 100407.5 ms | 98475.0 ms | 1932.5 ms | 78087.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 99124.3 ms | 97057.8 ms | 2066.5 ms | 71190.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 97923.9 ms | 96113.6 ms | 1810.3 ms | 70542.8 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 88050.3 ms | 85959.6 ms | 2090.7 ms | 64971.3 ms |
| IXGo | Go | 83431.2 ms | 78574.3 ms | 4856.9 ms | 22868.3 ms |
| Aws_restjson | LLGoDeadcodeDrop | 81786.8 ms | 79755.0 ms | 2031.7 ms | 36429.5 ms |
| Aws_restjson | LLGoNoLTO | 80364.9 ms | 78412.6 ms | 1952.3 ms | 35923.2 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 62481.3 ms | 61113.4 ms | 1368.0 ms | 42424.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 61812.7 ms | 60453.3 ms | 1359.4 ms | 41569.2 ms |
| Uber_zap | LLGoDeadcodeDrop | 57502.2 ms | 56005.7 ms | 1496.5 ms | 24576.4 ms |
| Uber_zap | LLGoNoLTO | 55771.5 ms | 54226.7 ms | 1544.8 ms | 24185.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 52154.4 ms | 50829.7 ms | 1324.6 ms | 31552.4 ms |
| K8s_workqueue | LLGoNoLTO | 49401.4 ms | 47800.2 ms | 1601.2 ms | 22167.7 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 49277.3 ms | 47799.0 ms | 1478.3 ms | 22221.7 ms |
| Toml | LLGoFullLTONoGlobalDCE | 48006.2 ms | 46875.5 ms | 1130.6 ms | 36045.1 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 41506.6 ms | 40326.9 ms | 1179.6 ms | 28522.6 ms |
| Toml | LLGoFullLTOGlobalDCE | 40791.5 ms | 39666.6 ms | 1125.0 ms | 28768.0 ms |
| Gorm_schema | LLGoDeadcodeDrop | 39872.7 ms | 38652.5 ms | 1220.2 ms | 13259.5 ms |
| Gorm_schema | LLGoNoLTO | 38741.2 ms | 37488.8 ms | 1252.3 ms | 13159.8 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 34688.7 ms | 33739.0 ms | 949.8 ms | 26928.0 ms |
| Etcdctl | Go | 33717.7 ms | 31535.1 ms | 2182.6 ms | 10000.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 26148.1 ms | 25265.2 ms | 882.9 ms | 18192.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 26035.4 ms | 25110.1 ms | 925.3 ms | 18198.3 ms |
| Toml | LLGoDeadcodeDrop | 24403.1 ms | 23300.9 ms | 1102.2 ms | 9284.8 ms |
| Toml | LLGoNoLTO | 23739.0 ms | 22806.1 ms | 932.8 ms | 9023.7 ms |
| XGo | Go | 19255.7 ms | 17957.0 ms | 1298.7 ms | 5669.3 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 14219.7 ms | 13407.3 ms | 812.4 ms | 6023.2 ms |
| Dustin_humanize | LLGoNoLTO | 14171.9 ms | 13408.5 ms | 763.3 ms | 5867.7 ms |
| Aws_restjson | Go | 7912.6 ms | 7204.4 ms | 708.2 ms | 3177.0 ms |
| Gorm_schema | Go | 5729.9 ms | 5301.1 ms | 428.9 ms | 2192.2 ms |
| Uber_zap | Go | 5439.0 ms | 4974.0 ms | 464.9 ms | 2153.0 ms |
| K8s_workqueue | Go | 4959.3 ms | 4327.1 ms | 632.2 ms | 2135.2 ms |
| Toml | Go | 2059.3 ms | 1814.3 ms | 244.9 ms | 947.1 ms |
| Dustin_humanize | Go | 883.8 ms | 661.3 ms | 222.5 ms | 677.4 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1418843.5 ms | 909165.4 ms | 9 |
| LLGoFullLTOGlobalDCE | 1402046.3 ms | 886312.6 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1395914.0 ms | 856652.0 ms | 9 |
| LLGoDeadcodeDrop | 983493.1 ms | 340590.4 ms | 9 |
| LLGoNoLTO | 946267.0 ms | 328396.6 ms | 9 |
| Go | 163388.5 ms | 49819.6 ms | 9 |

Dependency download details are in `download-timings.log`.
