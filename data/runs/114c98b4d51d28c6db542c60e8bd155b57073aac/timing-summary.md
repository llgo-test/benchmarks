## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 756775.1 ms | 738511.9 ms | 18263.2 ms | 494658.1 ms |
| IXGo | LLGoFullLTOGlobalDCE | 716609.6 ms | 698297.0 ms | 18312.6 ms | 473312.8 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 711852.4 ms | 694013.2 ms | 17839.2 ms | 475685.4 ms |
| IXGo | LLGoDeadcodeDrop | 437576.3 ms | 418964.5 ms | 18611.9 ms | 139147.8 ms |
| IXGo | LLGoNoLTO | 385626.0 ms | 369806.7 ms | 15819.2 ms | 120393.5 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 372699.3 ms | 364400.8 ms | 8298.5 ms | 276728.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 369418.3 ms | 361355.0 ms | 8063.3 ms | 274117.6 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 359998.7 ms | 352213.6 ms | 7785.1 ms | 268595.6 ms |
| XGo | LLGoFullLTONoGlobalDCE | 270742.0 ms | 264873.3 ms | 5868.7 ms | 218482.5 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 264138.7 ms | 259226.5 ms | 4912.2 ms | 180832.0 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 239257.1 ms | 233811.1 ms | 5446.0 ms | 186540.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 237301.7 ms | 232755.6 ms | 4546.1 ms | 153782.3 ms |
| XGo | LLGoFullLTOGlobalDCE | 235794.8 ms | 230438.3 ms | 5356.5 ms | 183529.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 231223.7 ms | 226789.1 ms | 4434.6 ms | 149707.3 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 210430.1 ms | 206248.5 ms | 4181.6 ms | 151042.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 206710.9 ms | 202637.5 ms | 4073.4 ms | 149292.5 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 206030.0 ms | 201858.0 ms | 4172.0 ms | 149272.3 ms |
| Aws_restjson | LLGoNoLTO | 193457.6 ms | 189601.3 ms | 3856.3 ms | 60482.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 192242.1 ms | 188356.7 ms | 3885.4 ms | 132987.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 190993.2 ms | 186977.2 ms | 4015.9 ms | 130172.8 ms |
| Aws_restjson | LLGoDeadcodeDrop | 189495.3 ms | 185398.9 ms | 4096.4 ms | 61245.2 ms |
| Etcdctl | LLGoDeadcodeDrop | 186724.1 ms | 179613.3 ms | 7110.7 ms | 65784.7 ms |
| Etcdctl | LLGoNoLTO | 183058.0 ms | 176545.8 ms | 6512.2 ms | 62961.8 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 175680.1 ms | 171703.8 ms | 3976.4 ms | 118115.5 ms |
| Uber_zap | LLGoDeadcodeDrop | 155593.0 ms | 152016.9 ms | 3576.1 ms | 51551.5 ms |
| Uber_zap | LLGoNoLTO | 154547.3 ms | 151256.4 ms | 3290.9 ms | 50032.5 ms |
| K8s_workqueue | LLGoNoLTO | 152899.1 ms | 149412.5 ms | 3486.7 ms | 49361.6 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 146516.6 ms | 143149.0 ms | 3367.6 ms | 48977.9 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 122741.7 ms | 119896.2 ms | 2845.5 ms | 87448.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 121193.5 ms | 118374.1 ms | 2819.4 ms | 85275.1 ms |
| Toml | LLGoFullLTONoGlobalDCE | 113956.8 ms | 111307.6 ms | 2649.2 ms | 80695.8 ms |
| XGo | LLGoDeadcodeDrop | 102950.6 ms | 98162.3 ms | 4788.3 ms | 38336.7 ms |
| XGo | LLGoNoLTO | 102554.3 ms | 98354.0 ms | 4200.3 ms | 38215.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 101418.1 ms | 98729.5 ms | 2688.7 ms | 65327.6 ms |
| Toml | LLGoFullLTOGlobalDCE | 98621.4 ms | 96135.1 ms | 2486.3 ms | 65316.2 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 98180.0 ms | 95696.3 ms | 2483.7 ms | 64753.8 ms |
| Gorm_schema | LLGoDeadcodeDrop | 86911.8 ms | 84315.8 ms | 2596.0 ms | 31129.9 ms |
| Gorm_schema | LLGoNoLTO | 84362.9 ms | 82054.3 ms | 2308.5 ms | 29604.7 ms |
| Toml | LLGoNoLTO | 80999.6 ms | 78855.6 ms | 2144.1 ms | 28273.9 ms |
| Toml | LLGoDeadcodeDrop | 80546.1 ms | 78348.6 ms | 2197.5 ms | 28350.1 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 79894.7 ms | 78017.4 ms | 1877.2 ms | 58674.3 ms |
| IXGo | Go | 66751.3 ms | 57924.6 ms | 8826.7 ms | 18382.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 64415.0 ms | 62705.8 ms | 1709.2 ms | 42782.5 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 63601.2 ms | 61972.5 ms | 1628.7 ms | 42482.3 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 55559.8 ms | 54062.2 ms | 1497.7 ms | 21229.8 ms |
| Dustin_humanize | LLGoNoLTO | 54245.5 ms | 52811.9 ms | 1433.6 ms | 20733.0 ms |
| Etcdctl | Go | 26836.9 ms | 23627.1 ms | 3209.8 ms | 8197.4 ms |
| XGo | Go | 15387.3 ms | 13571.6 ms | 1815.7 ms | 4604.1 ms |
| Aws_restjson | Go | 6569.3 ms | 5653.0 ms | 916.3 ms | 2743.8 ms |
| Gorm_schema | Go | 4636.2 ms | 4041.2 ms | 594.9 ms | 1829.6 ms |
| Uber_zap | Go | 4318.9 ms | 3781.0 ms | 537.9 ms | 1750.8 ms |
| K8s_workqueue | Go | 3815.8 ms | 3238.3 ms | 577.6 ms | 1580.9 ms |
| Toml | Go | 1655.5 ms | 1437.7 ms | 217.8 ms | 790.3 ms |
| Dustin_humanize | Go | 670.8 ms | 531.1 ms | 139.7 ms | 397.7 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2339785.1 ms | 1670728.2 ms | 9 |
| LLGoFullLTOGlobalDCE | 2244774.5 ms | 1562707.2 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2227360.6 ms | 1526175.4 ms | 9 |
| LLGoDeadcodeDrop | 1441873.7 ms | 485753.6 ms | 9 |
| LLGoNoLTO | 1391750.3 ms | 460058.7 ms | 9 |
| Go | 130641.9 ms | 40276.5 ms | 9 |

Dependency download details are in `download-timings.log`.
