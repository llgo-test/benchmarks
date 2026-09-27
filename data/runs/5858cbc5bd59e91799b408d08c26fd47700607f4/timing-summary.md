## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 722718.8 ms | 707357.5 ms | 15361.3 ms | 379196.2 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 695354.6 ms | 681366.6 ms | 13988.0 ms | 367232.4 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 667943.7 ms | 654882.6 ms | 13061.1 ms | 342880.5 ms |
| IXGo | LLGoDeadcodeDrop | 582959.7 ms | 571487.1 ms | 11472.5 ms | 208124.0 ms |
| IXGo | LLGoNoLTO | 519250.2 ms | 507618.8 ms | 11631.5 ms | 163731.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 271255.9 ms | 265694.2 ms | 5561.7 ms | 169391.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 270916.3 ms | 265162.2 ms | 5754.1 ms | 171650.7 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 260194.4 ms | 254370.4 ms | 5824.0 ms | 164378.6 ms |
| Etcdctl | LLGoDeadcodeDrop | 192759.2 ms | 187505.2 ms | 5254.0 ms | 65012.6 ms |
| Etcdctl | LLGoNoLTO | 192567.1 ms | 187652.7 ms | 4914.3 ms | 64095.0 ms |
| XGo | LLGoFullLTOGlobalDCE | 189118.9 ms | 185233.0 ms | 3885.9 ms | 133264.8 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 188607.7 ms | 184681.9 ms | 3925.8 ms | 133045.1 ms |
| XGo | LLGoFullLTONoGlobalDCE | 187012.8 ms | 183217.6 ms | 3795.2 ms | 132450.9 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 145353.4 ms | 142585.4 ms | 2768.0 ms | 109010.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 134636.9 ms | 131770.2 ms | 2866.7 ms | 96668.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 131578.7 ms | 128880.9 ms | 2697.7 ms | 94977.2 ms |
| XGo | LLGoNoLTO | 110568.6 ms | 107110.2 ms | 3458.3 ms | 42185.4 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 110334.9 ms | 108304.7 ms | 2030.2 ms | 85268.2 ms |
| XGo | LLGoDeadcodeDrop | 109245.9 ms | 105769.6 ms | 3476.2 ms | 41722.1 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 107000.7 ms | 104749.2 ms | 2251.5 ms | 83872.7 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 105979.5 ms | 103802.3 ms | 2177.2 ms | 84066.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 103301.2 ms | 101185.5 ms | 2115.8 ms | 76290.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 103236.7 ms | 101061.6 ms | 2175.1 ms | 77059.2 ms |
| Aws_restjson | LLGoDeadcodeDrop | 92814.9 ms | 90448.5 ms | 2366.3 ms | 48775.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 92576.6 ms | 90414.2 ms | 2162.4 ms | 69079.1 ms |
| Aws_restjson | LLGoNoLTO | 85400.0 ms | 82913.8 ms | 2486.2 ms | 42314.1 ms |
| IXGo | Go | 82597.6 ms | 76952.9 ms | 5644.7 ms | 23588.0 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 65173.7 ms | 63557.1 ms | 1616.6 ms | 45524.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 63545.7 ms | 61911.6 ms | 1634.1 ms | 44154.7 ms |
| Uber_zap | LLGoDeadcodeDrop | 58092.0 ms | 56288.9 ms | 1803.2 ms | 25795.4 ms |
| Uber_zap | LLGoNoLTO | 56758.2 ms | 54998.0 ms | 1760.2 ms | 25287.1 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 53103.4 ms | 51557.7 ms | 1545.6 ms | 33264.1 ms |
| Toml | LLGoFullLTONoGlobalDCE | 51117.7 ms | 49861.3 ms | 1256.4 ms | 39323.1 ms |
| K8s_workqueue | LLGoNoLTO | 49543.1 ms | 47754.1 ms | 1789.1 ms | 23145.8 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 49333.6 ms | 47586.7 ms | 1746.9 ms | 23139.2 ms |
| Toml | LLGoFullLTOGlobalDCE | 43042.6 ms | 41716.4 ms | 1326.3 ms | 30854.6 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 42792.0 ms | 41568.4 ms | 1223.6 ms | 30249.2 ms |
| Gorm_schema | LLGoDeadcodeDrop | 39570.9 ms | 38005.2 ms | 1565.7 ms | 13716.4 ms |
| Gorm_schema | LLGoNoLTO | 38283.3 ms | 36801.8 ms | 1481.6 ms | 13273.6 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 35997.1 ms | 34945.8 ms | 1051.3 ms | 28490.7 ms |
| Etcdctl | Go | 33048.1 ms | 30637.3 ms | 2410.7 ms | 10280.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 27374.9 ms | 26407.9 ms | 966.9 ms | 19864.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 26691.1 ms | 25685.8 ms | 1005.3 ms | 19106.5 ms |
| Toml | LLGoNoLTO | 24459.3 ms | 23333.5 ms | 1125.8 ms | 9241.0 ms |
| Toml | LLGoDeadcodeDrop | 23461.7 ms | 22343.0 ms | 1118.6 ms | 9027.9 ms |
| XGo | Go | 19377.5 ms | 17993.3 ms | 1384.2 ms | 5764.4 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 13818.4 ms | 12924.2 ms | 894.2 ms | 6372.7 ms |
| Dustin_humanize | LLGoNoLTO | 13799.7 ms | 12946.9 ms | 852.7 ms | 6025.5 ms |
| Aws_restjson | Go | 8280.8 ms | 7275.5 ms | 1005.3 ms | 4149.5 ms |
| Gorm_schema | Go | 5690.9 ms | 5238.3 ms | 452.6 ms | 2265.2 ms |
| Uber_zap | Go | 5380.6 ms | 4861.6 ms | 519.0 ms | 2193.7 ms |
| K8s_workqueue | Go | 4676.0 ms | 4165.9 ms | 510.0 ms | 1689.9 ms |
| Toml | Go | 2068.0 ms | 1779.1 ms | 288.8 ms | 976.2 ms |
| Dustin_humanize | Go | 959.0 ms | 709.4 ms | 249.6 ms | 601.1 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTOGlobalDCE | 1658872.8 ms | 1032635.0 ms | 9 |
| LLGoFullLTONoGlobalDCE | 1629107.1 ms | 1031393.4 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1607979.8 ms | 996585.1 ms | 9 |
| LLGoDeadcodeDrop | 1162056.2 ms | 441685.9 ms | 9 |
| LLGoNoLTO | 1090629.6 ms | 389298.9 ms | 9 |
| Go | 162078.3 ms | 51507.9 ms | 9 |

Dependency download details are in `download-timings.log`.
