## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 685227.7 ms | 661408.2 ms | 23819.5 ms | 453781.1 ms |
| IXGo | LLGoFullLTOGlobalDCE | 676961.8 ms | 653418.1 ms | 23543.6 ms | 441603.1 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 656656.8 ms | 633120.1 ms | 23536.7 ms | 432257.7 ms |
| IXGo | LLGoDeadcodeDrop | 395968.5 ms | 372523.3 ms | 23445.3 ms | 128018.7 ms |
| IXGo | LLGoNoLTO | 377552.2 ms | 357536.5 ms | 20015.8 ms | 117957.2 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 353463.4 ms | 342724.8 ms | 10738.6 ms | 261287.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 353017.9 ms | 342241.9 ms | 10775.9 ms | 259094.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 351766.4 ms | 341022.9 ms | 10743.5 ms | 259416.7 ms |
| XGo | LLGoFullLTONoGlobalDCE | 260432.5 ms | 253017.6 ms | 7414.9 ms | 208318.7 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 244965.2 ms | 238664.3 ms | 6300.9 ms | 168553.5 ms |
| XGo | LLGoFullLTOGlobalDCE | 231515.3 ms | 224575.1 ms | 6940.2 ms | 177787.8 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 229595.6 ms | 222433.9 ms | 7161.8 ms | 176184.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 221271.3 ms | 215481.8 ms | 5789.4 ms | 142851.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 220023.8 ms | 213767.7 ms | 6256.0 ms | 142618.7 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 204726.4 ms | 199483.6 ms | 5242.8 ms | 144780.8 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 200172.5 ms | 195000.7 ms | 5171.8 ms | 142597.4 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 197113.5 ms | 191918.3 ms | 5195.2 ms | 140318.2 ms |
| Aws_restjson | LLGoDeadcodeDrop | 196487.8 ms | 190844.1 ms | 5643.7 ms | 63814.2 ms |
| Aws_restjson | LLGoNoLTO | 193711.9 ms | 188352.6 ms | 5359.3 ms | 61413.2 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 189758.4 ms | 184370.8 ms | 5387.6 ms | 128487.3 ms |
| Etcdctl | LLGoDeadcodeDrop | 187627.8 ms | 177994.5 ms | 9633.3 ms | 66192.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 187225.5 ms | 182106.2 ms | 5119.3 ms | 125346.1 ms |
| Etcdctl | LLGoNoLTO | 186637.1 ms | 178046.9 ms | 8590.2 ms | 64676.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 169568.1 ms | 164676.1 ms | 4892.0 ms | 111961.1 ms |
| Uber_zap | LLGoDeadcodeDrop | 162471.7 ms | 157784.4 ms | 4687.4 ms | 53731.4 ms |
| Uber_zap | LLGoNoLTO | 160521.4 ms | 156141.9 ms | 4379.4 ms | 52024.5 ms |
| K8s_workqueue | LLGoNoLTO | 153174.6 ms | 148641.5 ms | 4533.1 ms | 49603.7 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 152428.5 ms | 147610.4 ms | 4818.1 ms | 51018.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 120194.8 ms | 116715.8 ms | 3478.9 ms | 83631.1 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 119309.6 ms | 115789.7 ms | 3520.0 ms | 83827.5 ms |
| Toml | LLGoFullLTONoGlobalDCE | 111897.7 ms | 108506.7 ms | 3391.0 ms | 77669.3 ms |
| XGo | LLGoNoLTO | 107328.5 ms | 101614.9 ms | 5713.6 ms | 39893.3 ms |
| XGo | LLGoDeadcodeDrop | 106427.7 ms | 99874.0 ms | 6553.8 ms | 39395.1 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 100402.3 ms | 97129.9 ms | 3272.4 ms | 63632.1 ms |
| Toml | LLGoFullLTOGlobalDCE | 97796.1 ms | 94469.7 ms | 3326.4 ms | 63217.8 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 97572.2 ms | 94389.1 ms | 3183.1 ms | 63180.5 ms |
| Gorm_schema | LLGoDeadcodeDrop | 90253.0 ms | 86950.1 ms | 3302.9 ms | 32253.9 ms |
| Gorm_schema | LLGoNoLTO | 89115.1 ms | 86179.6 ms | 2935.5 ms | 31143.0 ms |
| Toml | LLGoDeadcodeDrop | 83324.0 ms | 80491.6 ms | 2832.4 ms | 29286.9 ms |
| Toml | LLGoNoLTO | 82167.7 ms | 79389.2 ms | 2778.5 ms | 28637.5 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 78724.1 ms | 76454.3 ms | 2269.8 ms | 57089.6 ms |
| IXGo | Go | 72590.7 ms | 59960.1 ms | 12630.6 ms | 20089.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 63575.4 ms | 61428.6 ms | 2146.8 ms | 41600.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 62417.5 ms | 60265.1 ms | 2152.5 ms | 40657.8 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 56893.6 ms | 54884.7 ms | 2008.9 ms | 21767.5 ms |
| Dustin_humanize | LLGoNoLTO | 56041.6 ms | 54178.6 ms | 1863.0 ms | 21303.2 ms |
| Etcdctl | Go | 29092.1 ms | 24553.1 ms | 4539.0 ms | 8904.6 ms |
| XGo | Go | 16475.0 ms | 13809.2 ms | 2665.8 ms | 4913.5 ms |
| Aws_restjson | Go | 6969.5 ms | 5617.8 ms | 1351.7 ms | 2980.1 ms |
| Gorm_schema | Go | 5069.1 ms | 4191.8 ms | 877.3 ms | 2144.6 ms |
| Uber_zap | Go | 4615.7 ms | 3870.5 ms | 745.2 ms | 1894.8 ms |
| K8s_workqueue | Go | 4067.4 ms | 3272.4 ms | 795.0 ms | 1600.9 ms |
| Toml | Go | 1767.7 ms | 1415.0 ms | 352.7 ms | 869.5 ms |
| Dustin_humanize | Go | 705.8 ms | 515.9 ms | 189.8 ms | 348.7 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2227289.3 ms | 1574102.3 ms | 9 |
| LLGoFullLTOGlobalDCE | 2151764.5 ms | 1480959.9 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2106298.1 ms | 1436688.9 ms | 9 |
| LLGoDeadcodeDrop | 1431882.7 ms | 485478.6 ms | 9 |
| LLGoNoLTO | 1406250.2 ms | 466651.9 ms | 9 |
| Go | 141353.0 ms | 43745.6 ms | 9 |

Dependency download details are in `download-timings.log`.
