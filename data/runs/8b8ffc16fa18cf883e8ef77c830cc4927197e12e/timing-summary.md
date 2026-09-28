## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 638570.6 ms | 625381.3 ms | 13189.4 ms | 319964.9 ms |
| IXGo | LLGoFullLTOGlobalDCE | 562734.1 ms | 550644.3 ms | 12089.8 ms | 291447.2 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 533098.6 ms | 522084.3 ms | 11014.3 ms | 282515.5 ms |
| IXGo | LLGoDeadcodeDrop | 484438.1 ms | 473810.4 ms | 10627.7 ms | 142520.3 ms |
| IXGo | LLGoNoLTO | 407027.3 ms | 397227.5 ms | 9799.8 ms | 121330.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 270906.3 ms | 266120.7 ms | 4785.7 ms | 166500.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 269741.7 ms | 264636.8 ms | 5105.0 ms | 166749.9 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 258682.7 ms | 254276.3 ms | 4406.4 ms | 159718.1 ms |
| Etcdctl | LLGoDeadcodeDrop | 198195.3 ms | 193886.7 ms | 4308.6 ms | 66420.8 ms |
| Etcdctl | LLGoNoLTO | 192376.5 ms | 188063.7 ms | 4312.8 ms | 65264.1 ms |
| XGo | LLGoFullLTONoGlobalDCE | 191195.1 ms | 187631.2 ms | 3563.9 ms | 132596.4 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 188164.7 ms | 184404.0 ms | 3760.7 ms | 129981.4 ms |
| XGo | LLGoFullLTOGlobalDCE | 186545.1 ms | 183063.9 ms | 3481.2 ms | 128179.1 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 150263.1 ms | 147749.6 ms | 2513.5 ms | 111126.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 129307.7 ms | 126674.3 ms | 2633.3 ms | 90071.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 126225.4 ms | 123800.7 ms | 2424.7 ms | 87151.9 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 113359.7 ms | 111486.4 ms | 1873.4 ms | 86329.3 ms |
| XGo | LLGoDeadcodeDrop | 112917.2 ms | 109961.4 ms | 2955.8 ms | 42568.5 ms |
| XGo | LLGoNoLTO | 110661.0 ms | 107835.0 ms | 2826.1 ms | 41709.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 108655.6 ms | 106748.4 ms | 1907.3 ms | 84360.3 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 106383.7 ms | 104443.4 ms | 1940.3 ms | 83161.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 102278.5 ms | 100355.2 ms | 1923.3 ms | 74518.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 99778.8 ms | 97930.5 ms | 1848.3 ms | 72707.8 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 92386.9 ms | 90552.7 ms | 1834.2 ms | 67890.2 ms |
| Aws_restjson | LLGoNoLTO | 88008.0 ms | 85934.0 ms | 2074.0 ms | 41664.5 ms |
| Aws_restjson | LLGoDeadcodeDrop | 85209.7 ms | 82990.5 ms | 2219.3 ms | 38640.3 ms |
| IXGo | Go | 84378.4 ms | 79431.3 ms | 4947.1 ms | 23342.0 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 66282.4 ms | 64780.6 ms | 1501.8 ms | 45751.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 63257.9 ms | 61824.9 ms | 1433.0 ms | 42937.1 ms |
| Uber_zap | LLGoDeadcodeDrop | 60012.0 ms | 58518.5 ms | 1493.5 ms | 26395.3 ms |
| Uber_zap | LLGoNoLTO | 58919.5 ms | 57365.8 ms | 1553.7 ms | 25937.1 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 55106.1 ms | 53624.0 ms | 1482.1 ms | 33870.9 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 51650.3 ms | 49929.6 ms | 1720.7 ms | 24535.4 ms |
| K8s_workqueue | LLGoNoLTO | 51271.0 ms | 49711.4 ms | 1559.6 ms | 23581.7 ms |
| Toml | LLGoFullLTONoGlobalDCE | 50553.9 ms | 49384.9 ms | 1169.0 ms | 38109.6 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 42534.7 ms | 41430.4 ms | 1104.3 ms | 29583.1 ms |
| Gorm_schema | LLGoDeadcodeDrop | 42474.1 ms | 41101.5 ms | 1372.6 ms | 14264.9 ms |
| Toml | LLGoFullLTOGlobalDCE | 42207.3 ms | 40986.7 ms | 1220.6 ms | 29691.7 ms |
| Gorm_schema | LLGoNoLTO | 40491.7 ms | 39243.3 ms | 1248.3 ms | 13702.6 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 35581.6 ms | 34709.6 ms | 872.0 ms | 27838.3 ms |
| Etcdctl | Go | 33798.2 ms | 31826.5 ms | 1971.7 ms | 10101.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 27198.5 ms | 26278.2 ms | 920.3 ms | 19105.9 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 26371.7 ms | 25489.2 ms | 882.5 ms | 18451.7 ms |
| Toml | LLGoDeadcodeDrop | 25361.6 ms | 24275.0 ms | 1086.6 ms | 9431.1 ms |
| Toml | LLGoNoLTO | 24723.4 ms | 23700.3 ms | 1023.1 ms | 9394.2 ms |
| XGo | Go | 19783.3 ms | 18614.4 ms | 1168.9 ms | 5853.8 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 14547.3 ms | 13709.8 ms | 837.5 ms | 6169.4 ms |
| Dustin_humanize | LLGoNoLTO | 14327.0 ms | 13572.6 ms | 754.4 ms | 6119.4 ms |
| Aws_restjson | Go | 8486.3 ms | 7781.7 ms | 704.6 ms | 3499.6 ms |
| Gorm_schema | Go | 5871.6 ms | 5482.6 ms | 389.0 ms | 2271.4 ms |
| Uber_zap | Go | 5482.2 ms | 4991.6 ms | 490.6 ms | 2379.4 ms |
| K8s_workqueue | Go | 4816.4 ms | 4367.9 ms | 448.5 ms | 1731.8 ms |
| Toml | Go | 2070.5 ms | 1823.4 ms | 247.2 ms | 944.2 ms |
| Dustin_humanize | Go | 940.0 ms | 738.1 ms | 201.9 ms | 635.6 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTOGlobalDCEPlugin | 1546454.1 ms | 931487.5 ms | 9 |
| LLGoFullLTONoGlobalDCE | 1505400.8 ms | 967146.0 ms | 9 |
| LLGoFullLTOGlobalDCE | 1485517.8 ms | 921677.0 ms | 9 |
| LLGoDeadcodeDrop | 1074805.6 ms | 370946.1 ms | 9 |
| LLGoNoLTO | 987805.5 ms | 348703.2 ms | 9 |
| Go | 165627.1 ms | 50759.4 ms | 9 |

Dependency download details are in `download-timings.log`.
