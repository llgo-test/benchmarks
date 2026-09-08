## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 637795.6 ms | 630750.6 ms | 7045.0 ms | 408038.5 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 635981.0 ms | 629153.1 ms | 6828.0 ms | 408226.2 ms |
| IXGo | LLGoFullLTOGlobalDCE | 628163.4 ms | 621727.1 ms | 6436.3 ms | 403639.7 ms |
| IXGo | LLGoNoLTO | 461011.4 ms | 455235.7 ms | 5775.6 ms | 150364.4 ms |
| IXGo | LLGoDeadcodeDrop | 429816.9 ms | 423885.6 ms | 5931.3 ms | 141648.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 283579.4 ms | 278614.1 ms | 4965.3 ms | 169209.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 281508.8 ms | 276154.6 ms | 5354.1 ms | 169202.9 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 273274.6 ms | 268851.7 ms | 4422.9 ms | 168092.5 ms |
| Etcdctl | LLGoNoLTO | 205851.0 ms | 201776.8 ms | 4074.2 ms | 67605.9 ms |
| Etcdctl | LLGoDeadcodeDrop | 201903.2 ms | 197689.2 ms | 4213.9 ms | 66705.8 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 190366.4 ms | 187132.1 ms | 3234.2 ms | 133401.8 ms |
| XGo | LLGoFullLTONoGlobalDCE | 183175.4 ms | 180173.1 ms | 3002.3 ms | 128924.5 ms |
| XGo | LLGoFullLTOGlobalDCE | 181960.1 ms | 178744.5 ms | 3215.6 ms | 126815.6 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 142454.7 ms | 140169.4 ms | 2285.3 ms | 104718.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 135280.2 ms | 132998.1 ms | 2282.0 ms | 95467.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 128750.6 ms | 126458.0 ms | 2292.6 ms | 90370.9 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 116170.9 ms | 114476.7 ms | 1694.2 ms | 90334.5 ms |
| XGo | LLGoDeadcodeDrop | 111304.2 ms | 108538.0 ms | 2766.2 ms | 41350.6 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 108335.4 ms | 106601.0 ms | 1734.4 ms | 85274.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 108076.4 ms | 106322.8 ms | 1753.7 ms | 84669.7 ms |
| XGo | LLGoNoLTO | 107942.1 ms | 105301.4 ms | 2640.8 ms | 40609.9 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 103401.9 ms | 101606.0 ms | 1795.9 ms | 76709.2 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 103247.4 ms | 101490.3 ms | 1757.1 ms | 76958.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 94406.3 ms | 92647.9 ms | 1758.4 ms | 70900.0 ms |
| Aws_restjson | LLGoDeadcodeDrop | 88105.6 ms | 86035.8 ms | 2069.8 ms | 41321.0 ms |
| Aws_restjson | LLGoNoLTO | 84077.4 ms | 82078.3 ms | 1999.1 ms | 38610.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 67222.3 ms | 65821.8 ms | 1400.5 ms | 46774.1 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 66829.3 ms | 65560.5 ms | 1268.8 ms | 47074.9 ms |
| Uber_zap | LLGoDeadcodeDrop | 59310.1 ms | 57891.5 ms | 1418.7 ms | 26541.3 ms |
| Uber_zap | LLGoNoLTO | 59211.4 ms | 57730.6 ms | 1480.8 ms | 25621.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 57414.9 ms | 56129.7 ms | 1285.2 ms | 37238.1 ms |
| Toml | LLGoFullLTONoGlobalDCE | 54369.3 ms | 53279.4 ms | 1089.9 ms | 42317.4 ms |
| K8s_workqueue | LLGoNoLTO | 52451.9 ms | 50847.1 ms | 1604.8 ms | 23875.5 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 51439.0 ms | 49854.9 ms | 1584.1 ms | 23838.4 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 47251.4 ms | 46184.8 ms | 1066.7 ms | 34230.4 ms |
| IXGo | Go | 46556.7 ms | 43552.1 ms | 3004.6 ms | 13453.0 ms |
| Toml | LLGoFullLTOGlobalDCE | 46057.2 ms | 45095.6 ms | 961.5 ms | 33953.5 ms |
| Gorm_schema | LLGoDeadcodeDrop | 38969.3 ms | 37798.9 ms | 1170.4 ms | 12644.3 ms |
| Gorm_schema | LLGoNoLTO | 38399.6 ms | 37208.2 ms | 1191.3 ms | 12537.0 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 34806.7 ms | 33953.7 ms | 853.0 ms | 26953.8 ms |
| Etcdctl | Go | 33438.5 ms | 31410.1 ms | 2028.4 ms | 10018.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 27249.7 ms | 26435.7 ms | 813.9 ms | 19189.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 25798.0 ms | 25005.4 ms | 792.6 ms | 17870.8 ms |
| Toml | LLGoDeadcodeDrop | 24139.5 ms | 23150.2 ms | 989.3 ms | 9042.8 ms |
| Toml | LLGoNoLTO | 23432.8 ms | 22485.7 ms | 947.1 ms | 8806.4 ms |
| XGo | Go | 19218.7 ms | 18060.9 ms | 1157.8 ms | 5737.3 ms |
| Dustin_humanize | LLGoNoLTO | 13635.2 ms | 12924.3 ms | 710.9 ms | 5646.2 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 13210.3 ms | 12502.4 ms | 707.9 ms | 5592.6 ms |
| Aws_restjson | Go | 7953.2 ms | 7307.4 ms | 645.8 ms | 3146.7 ms |
| Gorm_schema | Go | 5814.6 ms | 5414.8 ms | 399.8 ms | 2208.8 ms |
| Uber_zap | Go | 5280.7 ms | 4888.6 ms | 392.0 ms | 2075.9 ms |
| K8s_workqueue | Go | 4914.8 ms | 4429.9 ms | 485.0 ms | 1765.0 ms |
| Toml | Go | 2212.5 ms | 1949.1 ms | 263.4 ms | 1036.3 ms |
| Dustin_humanize | Go | 817.6 ms | 679.0 ms | 138.7 ms | 380.8 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1615397.4 ms | 1101916.6 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1575294.1 ms | 1043065.6 ms | 9 |
| LLGoFullLTOGlobalDCE | 1572235.8 ms | 1051573.8 ms | 9 |
| LLGoNoLTO | 1046012.7 ms | 373677.6 ms | 9 |
| LLGoDeadcodeDrop | 1018198.1 ms | 368685.2 ms | 9 |
| Go | 126207.3 ms | 39822.2 ms | 9 |

Dependency download details are in `download-timings.log`.
