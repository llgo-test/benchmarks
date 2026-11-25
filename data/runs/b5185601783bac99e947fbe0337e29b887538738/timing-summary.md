## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 657487.5 ms | 641700.4 ms | 15787.1 ms | 442951.4 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 648082.7 ms | 631581.8 ms | 16500.9 ms | 435373.6 ms |
| IXGo | LLGoFullLTOGlobalDCE | 642367.2 ms | 625893.8 ms | 16473.4 ms | 428878.2 ms |
| IXGo | LLGoDeadcodeDrop | 374277.3 ms | 357225.6 ms | 17051.7 ms | 121418.2 ms |
| IXGo | LLGoNoLTO | 355235.2 ms | 340832.5 ms | 14402.7 ms | 111488.6 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 346143.0 ms | 338596.0 ms | 7547.0 ms | 259572.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 344114.9 ms | 336710.4 ms | 7404.5 ms | 256292.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 337073.9 ms | 329634.9 ms | 7439.1 ms | 251413.4 ms |
| XGo | LLGoFullLTONoGlobalDCE | 251146.5 ms | 246194.2 ms | 4952.3 ms | 203560.5 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 236121.1 ms | 231967.6 ms | 4153.5 ms | 162420.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 213219.2 ms | 209090.7 ms | 4128.4 ms | 137972.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 212663.4 ms | 208540.4 ms | 4123.0 ms | 137206.3 ms |
| XGo | LLGoFullLTOGlobalDCE | 212064.0 ms | 207353.8 ms | 4710.2 ms | 165113.0 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 206948.4 ms | 202273.6 ms | 4674.8 ms | 160431.7 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 199720.4 ms | 196045.5 ms | 3675.0 ms | 143118.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 190119.7 ms | 186517.9 ms | 3601.7 ms | 137982.5 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 189199.3 ms | 185590.8 ms | 3608.5 ms | 137058.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 181177.3 ms | 177595.6 ms | 3581.7 ms | 124138.5 ms |
| Aws_restjson | LLGoDeadcodeDrop | 180395.7 ms | 176484.6 ms | 3911.1 ms | 57842.6 ms |
| Aws_restjson | LLGoNoLTO | 180137.7 ms | 176631.0 ms | 3506.7 ms | 56521.1 ms |
| Etcdctl | LLGoDeadcodeDrop | 177297.1 ms | 170892.8 ms | 6404.4 ms | 61594.7 ms |
| Etcdctl | LLGoNoLTO | 175468.2 ms | 169372.3 ms | 6096.0 ms | 60391.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 168938.9 ms | 165535.0 ms | 3403.9 ms | 114997.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 160243.6 ms | 156769.2 ms | 3474.4 ms | 107390.9 ms |
| Uber_zap | LLGoNoLTO | 146598.9 ms | 143502.7 ms | 3096.2 ms | 47410.0 ms |
| Uber_zap | LLGoDeadcodeDrop | 145009.9 ms | 141762.6 ms | 3247.3 ms | 48012.6 ms |
| K8s_workqueue | LLGoNoLTO | 142182.1 ms | 139198.4 ms | 2983.7 ms | 45583.3 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 138804.3 ms | 135711.2 ms | 3093.1 ms | 46389.1 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 113199.4 ms | 110716.2 ms | 2483.1 ms | 80564.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 109829.2 ms | 107441.4 ms | 2387.8 ms | 77685.7 ms |
| Toml | LLGoFullLTONoGlobalDCE | 102115.7 ms | 99811.4 ms | 2304.3 ms | 72201.1 ms |
| XGo | LLGoDeadcodeDrop | 98079.4 ms | 93939.9 ms | 4139.5 ms | 36092.5 ms |
| XGo | LLGoNoLTO | 97512.4 ms | 93723.0 ms | 3789.4 ms | 36165.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 93892.0 ms | 91563.7 ms | 2328.3 ms | 60368.3 ms |
| Toml | LLGoFullLTOGlobalDCE | 92177.4 ms | 89893.3 ms | 2284.0 ms | 60747.7 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 90823.0 ms | 88586.2 ms | 2236.8 ms | 59764.8 ms |
| Gorm_schema | LLGoDeadcodeDrop | 81769.1 ms | 79486.1 ms | 2283.0 ms | 28951.3 ms |
| Gorm_schema | LLGoNoLTO | 81659.0 ms | 79580.3 ms | 2078.7 ms | 28491.6 ms |
| Toml | LLGoNoLTO | 74066.7 ms | 72276.1 ms | 1790.6 ms | 25810.1 ms |
| Toml | LLGoDeadcodeDrop | 73990.1 ms | 72091.2 ms | 1898.8 ms | 25949.7 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 72456.6 ms | 70885.9 ms | 1570.7 ms | 53366.6 ms |
| IXGo | Go | 62087.0 ms | 54228.0 ms | 7859.1 ms | 16907.9 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 59175.5 ms | 57679.3 ms | 1496.1 ms | 39004.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 58467.7 ms | 56965.6 ms | 1502.2 ms | 38892.2 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 52680.0 ms | 51295.7 ms | 1384.4 ms | 20201.3 ms |
| Dustin_humanize | LLGoNoLTO | 51828.2 ms | 50550.3 ms | 1277.9 ms | 19547.2 ms |
| Etcdctl | Go | 24678.5 ms | 21894.3 ms | 2784.2 ms | 7597.2 ms |
| XGo | Go | 14517.9 ms | 12859.0 ms | 1658.8 ms | 4315.1 ms |
| Aws_restjson | Go | 5720.2 ms | 4957.8 ms | 762.4 ms | 2352.9 ms |
| Gorm_schema | Go | 4382.1 ms | 3862.3 ms | 519.7 ms | 1702.6 ms |
| Uber_zap | Go | 3993.2 ms | 3528.7 ms | 464.5 ms | 1610.3 ms |
| K8s_workqueue | Go | 3468.8 ms | 3008.0 ms | 460.8 ms | 1392.5 ms |
| Toml | Go | 1583.4 ms | 1363.6 ms | 219.8 ms | 737.0 ms |
| Dustin_humanize | Go | 589.7 ms | 480.3 ms | 109.4 ms | 291.1 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2158184.8 ms | 1547237.0 ms | 9 |
| LLGoFullLTOGlobalDCE | 2036495.6 ms | 1422823.9 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1994287.0 ms | 1378408.7 ms | 9 |
| LLGoDeadcodeDrop | 1322303.0 ms | 446452.1 ms | 9 |
| LLGoNoLTO | 1304688.4 ms | 431408.6 ms | 9 |
| Go | 121020.7 ms | 36906.7 ms | 9 |

Dependency download details are in `download-timings.log`.
