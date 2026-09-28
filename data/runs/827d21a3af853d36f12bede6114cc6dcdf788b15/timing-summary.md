## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 542293.9 ms | 529375.9 ms | 12918.0 ms | 283229.7 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 541157.9 ms | 525971.9 ms | 15186.0 ms | 302567.8 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 524204.4 ms | 513133.0 ms | 11071.4 ms | 277767.2 ms |
| IXGo | LLGoDeadcodeDrop | 424210.3 ms | 414091.8 ms | 10118.5 ms | 126080.4 ms |
| IXGo | LLGoNoLTO | 413799.6 ms | 403768.9 ms | 10030.8 ms | 123660.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 262236.3 ms | 257495.6 ms | 4740.7 ms | 160614.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 258882.9 ms | 254162.5 ms | 4720.4 ms | 159156.4 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 257295.2 ms | 252701.8 ms | 4593.4 ms | 159259.3 ms |
| Etcdctl | LLGoDeadcodeDrop | 196742.3 ms | 192493.9 ms | 4248.4 ms | 66609.0 ms |
| Etcdctl | LLGoNoLTO | 191302.6 ms | 186616.6 ms | 4686.1 ms | 63959.9 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 182591.5 ms | 179215.7 ms | 3375.8 ms | 125732.4 ms |
| XGo | LLGoFullLTONoGlobalDCE | 181593.4 ms | 178187.6 ms | 3405.8 ms | 125435.8 ms |
| XGo | LLGoFullLTOGlobalDCE | 181119.1 ms | 177887.9 ms | 3231.2 ms | 124695.8 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 139090.5 ms | 136654.5 ms | 2436.0 ms | 100801.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 127111.3 ms | 124507.8 ms | 2603.5 ms | 88276.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 127077.1 ms | 124582.6 ms | 2494.5 ms | 87809.8 ms |
| XGo | LLGoDeadcodeDrop | 115478.4 ms | 112489.1 ms | 2989.4 ms | 43784.7 ms |
| XGo | LLGoNoLTO | 111079.4 ms | 108149.3 ms | 2930.1 ms | 42022.6 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 110861.2 ms | 109080.2 ms | 1781.0 ms | 84387.0 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 104396.6 ms | 102431.6 ms | 1965.0 ms | 81369.8 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 104185.4 ms | 102277.7 ms | 1907.7 ms | 80683.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 101774.6 ms | 99673.1 ms | 2101.6 ms | 73716.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 99864.7 ms | 97949.1 ms | 1915.6 ms | 72802.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 90580.4 ms | 88761.0 ms | 1819.4 ms | 66483.8 ms |
| Aws_restjson | LLGoDeadcodeDrop | 85420.6 ms | 83211.1 ms | 2209.6 ms | 38941.0 ms |
| IXGo | Go | 85373.0 ms | 79807.3 ms | 5565.7 ms | 24065.8 ms |
| Aws_restjson | LLGoNoLTO | 84694.1 ms | 82528.9 ms | 2165.2 ms | 38654.7 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 62818.9 ms | 61391.8 ms | 1427.1 ms | 43122.1 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 62544.9 ms | 61095.1 ms | 1449.8 ms | 42618.9 ms |
| Uber_zap | LLGoDeadcodeDrop | 59451.4 ms | 57932.8 ms | 1518.7 ms | 25992.6 ms |
| Uber_zap | LLGoNoLTO | 58952.8 ms | 57349.7 ms | 1603.2 ms | 25775.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 53194.4 ms | 51771.6 ms | 1422.8 ms | 32312.2 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 51363.8 ms | 49837.6 ms | 1526.2 ms | 23725.1 ms |
| K8s_workqueue | LLGoNoLTO | 50725.9 ms | 49194.0 ms | 1531.9 ms | 23340.0 ms |
| Toml | LLGoFullLTONoGlobalDCE | 49209.2 ms | 48026.1 ms | 1183.1 ms | 37008.3 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 42721.1 ms | 41590.9 ms | 1130.2 ms | 29585.5 ms |
| Toml | LLGoFullLTOGlobalDCE | 41870.1 ms | 40668.3 ms | 1201.8 ms | 29596.2 ms |
| Gorm_schema | LLGoDeadcodeDrop | 40750.6 ms | 39440.9 ms | 1309.8 ms | 13807.4 ms |
| Gorm_schema | LLGoNoLTO | 39963.2 ms | 38662.0 ms | 1301.3 ms | 13455.1 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 35057.5 ms | 34080.5 ms | 976.9 ms | 27220.0 ms |
| Etcdctl | Go | 33745.9 ms | 31735.3 ms | 2010.6 ms | 10114.5 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 26694.1 ms | 25781.3 ms | 912.8 ms | 18659.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 26495.1 ms | 25508.6 ms | 986.5 ms | 18465.8 ms |
| Toml | LLGoDeadcodeDrop | 25160.5 ms | 24158.2 ms | 1002.3 ms | 9440.9 ms |
| Toml | LLGoNoLTO | 24495.0 ms | 23408.4 ms | 1086.6 ms | 9393.4 ms |
| XGo | Go | 19199.9 ms | 17984.9 ms | 1215.0 ms | 5658.9 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 14523.5 ms | 13705.0 ms | 818.5 ms | 6121.2 ms |
| Dustin_humanize | LLGoNoLTO | 14326.3 ms | 13570.8 ms | 755.5 ms | 6069.2 ms |
| Aws_restjson | Go | 8196.2 ms | 7306.0 ms | 890.2 ms | 3520.7 ms |
| Gorm_schema | Go | 5772.1 ms | 5351.7 ms | 420.4 ms | 2215.2 ms |
| Uber_zap | Go | 5602.4 ms | 5012.2 ms | 590.1 ms | 2429.9 ms |
| K8s_workqueue | Go | 4745.0 ms | 4288.7 ms | 456.3 ms | 1663.3 ms |
| Toml | Go | 2026.8 ms | 1793.5 ms | 233.3 ms | 931.8 ms |
| Dustin_humanize | Go | 960.9 ms | 707.8 ms | 253.1 ms | 703.2 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1464526.9 ms | 936370.9 ms | 9 |
| LLGoFullLTOGlobalDCE | 1444367.5 ms | 899524.3 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1428027.4 ms | 897481.9 ms | 9 |
| LLGoDeadcodeDrop | 1013101.6 ms | 354502.3 ms | 9 |
| LLGoNoLTO | 989339.0 ms | 346331.0 ms | 9 |
| Go | 165622.3 ms | 51303.3 ms | 9 |

Dependency download details are in `download-timings.log`.
