## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 563688.1 ms | 553144.3 ms | 10543.8 ms | 294388.1 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 489837.2 ms | 479244.3 ms | 10592.9 ms | 269133.2 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 478383.6 ms | 467616.8 ms | 10766.7 ms | 261634.8 ms |
| IXGo | LLGoDeadcodeDrop | 407926.2 ms | 398747.4 ms | 9178.8 ms | 124672.8 ms |
| IXGo | LLGoNoLTO | 401452.1 ms | 392354.4 ms | 9097.7 ms | 121926.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 251267.1 ms | 246694.3 ms | 4572.8 ms | 161827.5 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 240999.5 ms | 236499.4 ms | 4500.1 ms | 155302.1 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 237350.6 ms | 233069.1 ms | 4281.4 ms | 153396.4 ms |
| Aws_restjson | LLGoNoLTO | 201267.1 ms | 198586.5 ms | 2680.6 ms | 73466.4 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 198513.6 ms | 195541.3 ms | 2972.3 ms | 120452.8 ms |
| Aws_restjson | LLGoDeadcodeDrop | 197699.3 ms | 195000.5 ms | 2698.9 ms | 71896.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 186728.5 ms | 183829.3 ms | 2899.2 ms | 107169.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 186198.6 ms | 183207.6 ms | 2991.0 ms | 107274.0 ms |
| Etcdctl | LLGoDeadcodeDrop | 177596.8 ms | 173711.2 ms | 3885.5 ms | 62062.8 ms |
| Etcdctl | LLGoNoLTO | 174479.9 ms | 170518.3 ms | 3961.7 ms | 60385.9 ms |
| XGo | LLGoFullLTOGlobalDCE | 173484.4 ms | 170291.6 ms | 3192.8 ms | 124345.6 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 172136.2 ms | 169599.6 ms | 2536.6 ms | 110291.9 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 169545.0 ms | 166372.6 ms | 3172.3 ms | 121413.2 ms |
| XGo | LLGoFullLTONoGlobalDCE | 168693.1 ms | 165663.0 ms | 3030.1 ms | 121515.4 ms |
| Uber_zap | LLGoDeadcodeDrop | 165486.5 ms | 163221.4 ms | 2265.1 ms | 63760.7 ms |
| Uber_zap | LLGoNoLTO | 165233.3 ms | 162980.0 ms | 2253.3 ms | 64667.1 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 162937.0 ms | 160274.3 ms | 2662.7 ms | 103438.5 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 160930.6 ms | 158338.1 ms | 2592.5 ms | 102720.0 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 160697.7 ms | 158328.0 ms | 2369.8 ms | 62188.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 160134.4 ms | 157655.2 ms | 2479.2 ms | 97452.1 ms |
| K8s_workqueue | LLGoNoLTO | 157913.3 ms | 155519.0 ms | 2394.3 ms | 61703.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 157623.4 ms | 155189.9 ms | 2433.5 ms | 95674.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 151241.3 ms | 148522.4 ms | 2718.9 ms | 90869.6 ms |
| XGo | LLGoDeadcodeDrop | 103615.3 ms | 100821.9 ms | 2793.4 ms | 41601.7 ms |
| XGo | LLGoNoLTO | 99585.1 ms | 97035.1 ms | 2550.0 ms | 39186.5 ms |
| Gorm_schema | LLGoDeadcodeDrop | 87315.1 ms | 85800.5 ms | 1514.6 ms | 29361.3 ms |
| Gorm_schema | LLGoNoLTO | 87298.3 ms | 85759.2 ms | 1539.1 ms | 29163.4 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 85549.7 ms | 83951.9 ms | 1597.8 ms | 50927.9 ms |
| IXGo | Go | 84290.6 ms | 79140.5 ms | 5150.0 ms | 24316.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 83725.7 ms | 82138.2 ms | 1587.6 ms | 49346.7 ms |
| Toml | LLGoDeadcodeDrop | 83264.0 ms | 81729.5 ms | 1534.5 ms | 27483.3 ms |
| Toml | LLGoNoLTO | 80468.9 ms | 78919.7 ms | 1549.2 ms | 26600.4 ms |
| Toml | LLGoFullLTONoGlobalDCE | 77983.7 ms | 76331.9 ms | 1651.8 ms | 45776.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 75482.7 ms | 73888.0 ms | 1594.7 ms | 40241.3 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 72573.1 ms | 70916.9 ms | 1656.2 ms | 39333.6 ms |
| Toml | LLGoFullLTOGlobalDCE | 71961.2 ms | 70387.1 ms | 1574.1 ms | 38874.9 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 55149.2 ms | 54183.0 ms | 966.2 ms | 19666.2 ms |
| Dustin_humanize | LLGoNoLTO | 54012.8 ms | 53058.9 ms | 953.9 ms | 19166.7 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 53923.7 ms | 52833.5 ms | 1090.2 ms | 33552.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 45671.8 ms | 44607.4 ms | 1064.4 ms | 24911.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 44954.3 ms | 43913.5 ms | 1040.9 ms | 24512.1 ms |
| Etcdctl | Go | 33326.4 ms | 31382.1 ms | 1944.3 ms | 9970.2 ms |
| XGo | Go | 19378.7 ms | 18148.2 ms | 1230.5 ms | 6069.4 ms |
| Aws_restjson | Go | 8011.9 ms | 7378.6 ms | 633.3 ms | 3223.7 ms |
| Gorm_schema | Go | 5747.7 ms | 5349.9 ms | 397.8 ms | 2215.6 ms |
| Uber_zap | Go | 5427.3 ms | 4946.8 ms | 480.5 ms | 2409.5 ms |
| K8s_workqueue | Go | 4694.7 ms | 4245.7 ms | 449.0 ms | 1653.0 ms |
| Toml | Go | 2003.8 ms | 1781.0 ms | 222.9 ms | 913.4 ms |
| Dustin_humanize | Go | 808.7 ms | 647.9 ms | 160.8 ms | 388.1 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTOGlobalDCE | 1688613.2 ms | 994829.3 ms | 9 |
| LLGoFullLTONoGlobalDCE | 1633464.8 ms | 1000268.1 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1599440.3 ms | 950678.2 ms | 9 |
| LLGoDeadcodeDrop | 1438750.1 ms | 502693.7 ms | 9 |
| LLGoNoLTO | 1421710.8 ms | 496266.0 ms | 9 |
| Go | 163689.8 ms | 51158.9 ms | 9 |

Dependency download details are in `download-timings.log`.
