## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 463965.5 ms | 452905.4 ms | 11060.1 ms | 243746.0 ms |
| IXGo | LLGoFullLTOGlobalDCE | 456081.0 ms | 445429.2 ms | 10651.8 ms | 242106.4 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 447135.9 ms | 436298.1 ms | 10837.8 ms | 239726.6 ms |
| IXGo | LLGoDeadcodeDrop | 357589.8 ms | 348238.6 ms | 9351.3 ms | 105893.8 ms |
| IXGo | LLGoNoLTO | 338928.5 ms | 330003.3 ms | 8925.1 ms | 100864.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 216821.3 ms | 212745.0 ms | 4076.3 ms | 135088.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 213353.6 ms | 209186.2 ms | 4167.3 ms | 133936.1 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 209875.7 ms | 205602.6 ms | 4273.0 ms | 132135.0 ms |
| Etcdctl | LLGoDeadcodeDrop | 159172.8 ms | 155412.6 ms | 3760.2 ms | 53039.4 ms |
| Etcdctl | LLGoNoLTO | 158965.3 ms | 155221.7 ms | 3743.6 ms | 52139.0 ms |
| XGo | LLGoFullLTOGlobalDCE | 155322.4 ms | 152382.3 ms | 2940.1 ms | 108321.3 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 149165.5 ms | 146441.1 ms | 2724.4 ms | 103640.9 ms |
| XGo | LLGoFullLTONoGlobalDCE | 147536.1 ms | 144660.2 ms | 2875.9 ms | 103746.6 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 119291.6 ms | 117194.3 ms | 2097.3 ms | 88334.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 109831.5 ms | 107727.5 ms | 2104.0 ms | 77735.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 103893.9 ms | 101910.7 ms | 1983.2 ms | 73419.4 ms |
| XGo | LLGoNoLTO | 90004.4 ms | 87663.7 ms | 2340.8 ms | 32672.3 ms |
| XGo | LLGoDeadcodeDrop | 89071.6 ms | 86647.5 ms | 2424.1 ms | 33105.6 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 88111.8 ms | 86649.8 ms | 1462.0 ms | 66796.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 85443.2 ms | 83765.4 ms | 1677.7 ms | 61993.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 84696.0 ms | 83113.4 ms | 1582.6 ms | 62187.2 ms |
| Aws_restjson | LLGoNoLTO | 71441.5 ms | 69634.2 ms | 1807.3 ms | 33500.6 ms |
| Aws_restjson | LLGoDeadcodeDrop | 70203.0 ms | 68474.5 ms | 1728.5 ms | 33941.4 ms |
| IXGo | Go | 65779.3 ms | 61391.3 ms | 4388.0 ms | 17934.2 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 53152.3 ms | 51985.4 ms | 1166.9 ms | 37141.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 51007.2 ms | 49796.6 ms | 1210.6 ms | 34590.0 ms |
| Uber_zap | LLGoDeadcodeDrop | 45390.1 ms | 44089.2 ms | 1300.9 ms | 18898.2 ms |
| Uber_zap | LLGoNoLTO | 44401.6 ms | 43136.4 ms | 1265.3 ms | 18607.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 44061.2 ms | 42830.3 ms | 1231.0 ms | 26619.0 ms |
| Toml | LLGoFullLTONoGlobalDCE | 39611.3 ms | 38753.0 ms | 858.3 ms | 30063.4 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 33872.7 ms | 33002.8 ms | 869.9 ms | 23500.5 ms |
| Toml | LLGoFullLTOGlobalDCE | 33659.3 ms | 32808.8 ms | 850.5 ms | 23651.8 ms |
| Gorm_schema | LLGoDeadcodeDrop | 32080.7 ms | 31058.5 ms | 1022.2 ms | 10634.5 ms |
| Gorm_schema | LLGoNoLTO | 31114.4 ms | 30119.9 ms | 994.6 ms | 10439.9 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 28305.2 ms | 27605.4 ms | 699.8 ms | 22098.7 ms |
| Etcdctl | Go | 26878.4 ms | 25203.4 ms | 1675.0 ms | 7945.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 21427.4 ms | 20748.0 ms | 679.4 ms | 14926.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 20924.1 ms | 20269.8 ms | 654.3 ms | 14731.2 ms |
| Toml | LLGoDeadcodeDrop | 19869.5 ms | 19067.5 ms | 802.0 ms | 7567.9 ms |
| Toml | LLGoNoLTO | 19320.9 ms | 18464.9 ms | 856.0 ms | 7579.6 ms |
| XGo | Go | 15297.4 ms | 14282.3 ms | 1015.0 ms | 4483.4 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 11403.6 ms | 10834.7 ms | 569.0 ms | 4853.6 ms |
| Dustin_humanize | LLGoNoLTO | 11323.4 ms | 10721.4 ms | 602.0 ms | 4810.6 ms |
| Aws_restjson | Go | 6427.3 ms | 5838.6 ms | 588.7 ms | 2943.7 ms |
| Gorm_schema | Go | 4687.4 ms | 4347.1 ms | 340.4 ms | 1757.5 ms |
| Uber_zap | Go | 4393.3 ms | 4082.0 ms | 311.3 ms | 1636.5 ms |
| K8s_workqueue | Go | 3779.2 ms | 3441.8 ms | 337.4 ms | 1316.8 ms |
| Toml | Go | 1711.2 ms | 1543.0 ms | 168.2 ms | 777.1 ms |
| Dustin_humanize | Go | 736.2 ms | 593.2 ms | 143.0 ms | 771.5 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1133019.9 ms | 720043.2 ms | 8 |
| LLGoFullLTOGlobalDCEPlugin | 1124588.4 ms | 687248.9 ms | 8 |
| LLGoFullLTOGlobalDCE | 1118937.4 ms | 692943.3 ms | 8 |
| LLGoDeadcodeDrop | 784781.2 ms | 267934.5 ms | 8 |
| LLGoNoLTO | 765500.1 ms | 260614.1 ms | 8 |
| Go | 129689.7 ms | 39566.0 ms | 9 |

Dependency download details are in `download-timings.log`.
