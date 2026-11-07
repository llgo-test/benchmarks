## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 866437.5 ms | 839848.5 ms | 26589.1 ms | 545522.4 ms |
| IXGo | LLGoFullLTOGlobalDCE | 852245.0 ms | 826372.0 ms | 25873.0 ms | 533980.2 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 831199.4 ms | 805445.9 ms | 25753.5 ms | 527431.0 ms |
| IXGo | LLGoDeadcodeDrop | 520930.5 ms | 494058.6 ms | 26871.9 ms | 160653.8 ms |
| IXGo | LLGoNoLTO | 492690.2 ms | 470977.3 ms | 21712.9 ms | 149192.4 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 445694.3 ms | 433474.4 ms | 12219.8 ms | 324657.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 445470.0 ms | 432892.3 ms | 12577.7 ms | 321652.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 439994.4 ms | 428022.3 ms | 11972.0 ms | 317788.1 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 330511.8 ms | 322963.9 ms | 7547.9 ms | 218309.0 ms |
| XGo | LLGoFullLTONoGlobalDCE | 325308.4 ms | 316788.4 ms | 8520.0 ms | 259307.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 304623.3 ms | 297509.2 ms | 7114.1 ms | 188865.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 303988.8 ms | 296943.3 ms | 7045.5 ms | 187993.6 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 288967.7 ms | 280624.5 ms | 8343.2 ms | 221113.7 ms |
| XGo | LLGoFullLTOGlobalDCE | 288361.9 ms | 280077.5 ms | 8284.4 ms | 219846.6 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 277136.8 ms | 270637.7 ms | 6499.1 ms | 189742.8 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 267858.6 ms | 261440.5 ms | 6418.1 ms | 182965.2 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 267584.6 ms | 261132.8 ms | 6451.8 ms | 183641.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 256877.4 ms | 250852.8 ms | 6024.6 ms | 168249.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 250962.4 ms | 244822.7 ms | 6139.7 ms | 162981.6 ms |
| Aws_restjson | LLGoDeadcodeDrop | 243915.6 ms | 237608.6 ms | 6307.0 ms | 75998.7 ms |
| Aws_restjson | LLGoNoLTO | 242895.8 ms | 237230.2 ms | 5665.6 ms | 74441.7 ms |
| Etcdctl | LLGoDeadcodeDrop | 238019.3 ms | 227205.6 ms | 10813.7 ms | 80136.5 ms |
| Etcdctl | LLGoNoLTO | 233426.0 ms | 223707.4 ms | 9718.5 ms | 78256.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 232891.9 ms | 226969.8 ms | 5922.1 ms | 149402.8 ms |
| Uber_zap | LLGoNoLTO | 203225.1 ms | 198185.6 ms | 5039.5 ms | 63152.6 ms |
| Uber_zap | LLGoDeadcodeDrop | 201844.5 ms | 196727.5 ms | 5117.1 ms | 63951.0 ms |
| K8s_workqueue | LLGoNoLTO | 192515.3 ms | 187589.7 ms | 4925.6 ms | 60049.8 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 192436.5 ms | 187302.6 ms | 5133.9 ms | 61500.6 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 148775.1 ms | 144812.1 ms | 3963.0 ms | 101536.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 147751.2 ms | 143893.6 ms | 3857.7 ms | 99394.9 ms |
| Toml | LLGoFullLTONoGlobalDCE | 137344.9 ms | 133699.5 ms | 3645.3 ms | 93678.7 ms |
| XGo | LLGoNoLTO | 130349.4 ms | 124107.1 ms | 6242.3 ms | 46478.8 ms |
| XGo | LLGoDeadcodeDrop | 129838.5 ms | 122465.2 ms | 7373.3 ms | 45458.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 123771.3 ms | 120106.5 ms | 3664.8 ms | 76324.4 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 121138.5 ms | 117703.2 ms | 3435.3 ms | 76622.0 ms |
| Toml | LLGoFullLTOGlobalDCE | 120636.7 ms | 117171.2 ms | 3465.5 ms | 76467.3 ms |
| Gorm_schema | LLGoDeadcodeDrop | 111352.4 ms | 107904.7 ms | 3447.6 ms | 38031.8 ms |
| Gorm_schema | LLGoNoLTO | 110664.7 ms | 107604.2 ms | 3060.5 ms | 37280.5 ms |
| Toml | LLGoDeadcodeDrop | 105114.3 ms | 102093.7 ms | 3020.6 ms | 35518.6 ms |
| Toml | LLGoNoLTO | 103587.5 ms | 100720.7 ms | 2866.8 ms | 34666.0 ms |
| IXGo | Go | 97400.2 ms | 82514.2 ms | 14886.0 ms | 27130.1 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 96903.0 ms | 94533.1 ms | 2369.8 ms | 68401.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 78039.4 ms | 75746.2 ms | 2293.2 ms | 48989.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 77891.1 ms | 75677.8 ms | 2213.3 ms | 49137.9 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 71266.8 ms | 69098.9 ms | 2167.8 ms | 26079.2 ms |
| Dustin_humanize | LLGoNoLTO | 71245.0 ms | 69278.3 ms | 1966.7 ms | 25877.4 ms |
| Etcdctl | Go | 38121.4 ms | 32748.7 ms | 5372.8 ms | 11952.5 ms |
| XGo | Go | 21665.4 ms | 18606.3 ms | 3059.2 ms | 6424.2 ms |
| Aws_restjson | Go | 9394.9 ms | 7715.1 ms | 1679.8 ms | 4523.9 ms |
| Gorm_schema | Go | 6558.3 ms | 5605.5 ms | 952.8 ms | 2546.2 ms |
| Uber_zap | Go | 5931.7 ms | 5059.8 ms | 871.9 ms | 2382.2 ms |
| K8s_workqueue | Go | 5384.5 ms | 4403.8 ms | 980.7 ms | 2380.2 ms |
| Toml | Go | 2273.8 ms | 1878.4 ms | 395.4 ms | 1071.7 ms |
| Dustin_humanize | Go | 886.2 ms | 673.2 ms | 213.0 ms | 436.5 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2860458.3 ms | 1966705.5 ms | 9 |
| LLGoFullLTOGlobalDCE | 2756387.9 ms | 1836546.7 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2711519.3 ms | 1790751.2 ms | 9 |
| LLGoDeadcodeDrop | 1814718.4 ms | 587328.4 ms | 9 |
| LLGoNoLTO | 1780599.0 ms | 569395.7 ms | 9 |
| Go | 187616.6 ms | 58847.4 ms | 9 |

Dependency download details are in `download-timings.log`.
