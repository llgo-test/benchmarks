## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 706875.6 ms | 696145.7 ms | 10730.0 ms | 351099.3 ms |
| IXGo | LLGoFullLTOGlobalDCE | 668189.7 ms | 657199.4 ms | 10990.3 ms | 350648.5 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 645774.6 ms | 634707.8 ms | 11066.7 ms | 336585.0 ms |
| IXGo | LLGoDeadcodeDrop | 538650.5 ms | 524488.0 ms | 14162.5 ms | 158643.1 ms |
| IXGo | LLGoNoLTO | 518554.7 ms | 508492.9 ms | 10061.8 ms | 148957.2 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 304015.6 ms | 298989.1 ms | 5026.6 ms | 191228.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 300534.4 ms | 295472.7 ms | 5061.7 ms | 187387.5 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 293888.5 ms | 288563.4 ms | 5325.1 ms | 183505.6 ms |
| Aws_restjson | LLGoNoLTO | 239867.8 ms | 236527.4 ms | 3340.5 ms | 84003.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 239152.1 ms | 235507.7 ms | 3644.4 ms | 132113.6 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 237646.4 ms | 233794.9 ms | 3851.5 ms | 142148.9 ms |
| Aws_restjson | LLGoDeadcodeDrop | 237281.8 ms | 234114.6 ms | 3167.1 ms | 82612.1 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 229573.5 ms | 225822.1 ms | 3751.4 ms | 128254.9 ms |
| Etcdctl | LLGoDeadcodeDrop | 223505.0 ms | 218149.5 ms | 5355.4 ms | 74496.4 ms |
| Etcdctl | LLGoNoLTO | 222473.4 ms | 218136.8 ms | 4336.6 ms | 72931.7 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 222107.2 ms | 218328.6 ms | 3778.7 ms | 157431.5 ms |
| XGo | LLGoFullLTONoGlobalDCE | 216884.9 ms | 213376.4 ms | 3508.5 ms | 154703.1 ms |
| XGo | LLGoFullLTOGlobalDCE | 207256.0 ms | 203859.5 ms | 3396.5 ms | 145739.7 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 204166.7 ms | 200911.8 ms | 3254.9 ms | 130229.4 ms |
| Uber_zap | LLGoDeadcodeDrop | 203148.9 ms | 200336.2 ms | 2812.7 ms | 75667.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 194935.5 ms | 191575.3 ms | 3360.2 ms | 117440.7 ms |
| Uber_zap | LLGoNoLTO | 193810.5 ms | 191086.6 ms | 2723.9 ms | 71902.1 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 192700.8 ms | 189473.6 ms | 3227.1 ms | 121325.4 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 191499.5 ms | 188209.8 ms | 3289.7 ms | 120966.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 190182.0 ms | 187054.4 ms | 3127.6 ms | 116426.5 ms |
| K8s_workqueue | LLGoNoLTO | 186660.2 ms | 183855.9 ms | 2804.3 ms | 69537.7 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 185939.9 ms | 183210.1 ms | 2729.9 ms | 69539.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 180026.1 ms | 176771.2 ms | 3254.9 ms | 107245.7 ms |
| XGo | LLGoDeadcodeDrop | 129113.8 ms | 125505.0 ms | 3608.8 ms | 47680.2 ms |
| XGo | LLGoNoLTO | 123048.4 ms | 120518.6 ms | 2529.8 ms | 45197.0 ms |
| Gorm_schema | LLGoDeadcodeDrop | 104098.0 ms | 102241.2 ms | 1856.8 ms | 34129.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 102992.3 ms | 100969.1 ms | 2023.2 ms | 60299.3 ms |
| Gorm_schema | LLGoNoLTO | 102327.9 ms | 100501.0 ms | 1826.9 ms | 33690.6 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 102216.9 ms | 100142.5 ms | 2074.4 ms | 61453.4 ms |
| Toml | LLGoNoLTO | 96429.1 ms | 94569.4 ms | 1859.7 ms | 31660.1 ms |
| Toml | LLGoDeadcodeDrop | 95949.1 ms | 94104.5 ms | 1844.6 ms | 31356.9 ms |
| Toml | LLGoFullLTONoGlobalDCE | 92198.6 ms | 90104.2 ms | 2094.4 ms | 54762.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 89321.5 ms | 87381.2 ms | 1940.2 ms | 46938.7 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 84719.8 ms | 82699.0 ms | 2020.8 ms | 46159.7 ms |
| Toml | LLGoFullLTOGlobalDCE | 83874.4 ms | 81900.4 ms | 1974.0 ms | 45737.4 ms |
| IXGo | Go | 83201.5 ms | 78167.3 ms | 5034.2 ms | 22829.9 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 69649.9 ms | 68100.2 ms | 1549.7 ms | 43290.1 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 65867.1 ms | 64610.6 ms | 1256.5 ms | 23415.1 ms |
| Dustin_humanize | LLGoNoLTO | 65698.3 ms | 64503.3 ms | 1195.0 ms | 23228.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 59260.7 ms | 57792.4 ms | 1468.3 ms | 32811.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 56752.0 ms | 55367.0 ms | 1384.9 ms | 31346.2 ms |
| Etcdctl | Go | 34507.7 ms | 32414.8 ms | 2092.9 ms | 10414.3 ms |
| XGo | Go | 19188.0 ms | 17986.0 ms | 1202.0 ms | 5596.2 ms |
| Aws_restjson | Go | 8359.8 ms | 7648.6 ms | 711.2 ms | 3525.2 ms |
| Gorm_schema | Go | 5946.5 ms | 5531.2 ms | 415.3 ms | 2283.0 ms |
| Uber_zap | Go | 5344.6 ms | 4911.1 ms | 433.5 ms | 2087.4 ms |
| K8s_workqueue | Go | 4751.9 ms | 4280.3 ms | 471.6 ms | 1767.4 ms |
| Toml | Go | 2017.1 ms | 1783.5 ms | 233.6 ms | 922.9 ms |
| Dustin_humanize | Go | 860.4 ms | 689.8 ms | 170.6 ms | 442.9 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTOGlobalDCEPlugin | 2074424.2 ms | 1177162.9 ms | 9 |
| LLGoFullLTONoGlobalDCE | 2064053.2 ms | 1235366.9 ms | 9 |
| LLGoFullLTOGlobalDCE | 2027917.8 ms | 1184748.9 ms | 9 |
| LLGoDeadcodeDrop | 1783554.0 ms | 597539.6 ms | 9 |
| LLGoNoLTO | 1748870.4 ms | 581108.6 ms | 9 |
| Go | 164177.5 ms | 49869.2 ms | 9 |

Dependency download details are in `download-timings.log`.
