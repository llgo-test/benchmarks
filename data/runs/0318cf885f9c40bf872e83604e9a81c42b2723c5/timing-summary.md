## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTONoGlobalDCE | 424345.7 ms | 415498.6 ms | 8847.1 ms | 221573.3 ms |
| IXGo | LLGoFullLTOGlobalDCE | 359388.2 ms | 350462.0 ms | 8926.2 ms | 196376.7 ms |
| IXGo | LLGoNoLTO | 359262.8 ms | 352002.9 ms | 7259.8 ms | 116182.3 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 355754.5 ms | 347105.4 ms | 8649.1 ms | 193994.5 ms |
| IXGo | LLGoDeadcodeDrop | 319068.0 ms | 311092.3 ms | 7975.6 ms | 94197.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 174177.1 ms | 170820.3 ms | 3356.8 ms | 110185.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 173501.8 ms | 170038.0 ms | 3463.8 ms | 109703.5 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 162476.4 ms | 159155.2 ms | 3321.2 ms | 102881.0 ms |
| Etcdctl | LLGoDeadcodeDrop | 127219.2 ms | 123985.6 ms | 3233.7 ms | 43530.5 ms |
| Etcdctl | LLGoNoLTO | 124865.5 ms | 121903.9 ms | 2961.5 ms | 42307.6 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 124285.9 ms | 121880.7 ms | 2405.2 ms | 88156.9 ms |
| XGo | LLGoFullLTOGlobalDCE | 120336.5 ms | 117962.0 ms | 2374.5 ms | 84076.9 ms |
| XGo | LLGoFullLTONoGlobalDCE | 116681.6 ms | 114375.3 ms | 2306.2 ms | 82030.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 95621.2 ms | 93764.5 ms | 1856.7 ms | 70200.6 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 92338.4 ms | 90663.1 ms | 1675.3 ms | 69391.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 84822.5 ms | 83081.9 ms | 1740.6 ms | 60855.1 ms |
| XGo | LLGoDeadcodeDrop | 72083.1 ms | 70079.4 ms | 2003.7 ms | 28343.7 ms |
| XGo | LLGoNoLTO | 69727.7 ms | 67837.1 ms | 1890.6 ms | 26812.2 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 69606.8 ms | 68361.8 ms | 1245.0 ms | 53313.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 64969.7 ms | 63716.4 ms | 1253.4 ms | 47666.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 63179.0 ms | 61960.4 ms | 1218.7 ms | 46656.5 ms |
| Aws_restjson | LLGoDeadcodeDrop | 53538.6 ms | 52180.3 ms | 1358.3 ms | 26118.5 ms |
| Aws_restjson | LLGoNoLTO | 53423.4 ms | 51991.2 ms | 1432.2 ms | 26486.8 ms |
| IXGo | Go | 52410.1 ms | 48228.3 ms | 4181.8 ms | 15218.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 41415.9 ms | 40388.0 ms | 1027.9 ms | 28576.2 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 39402.4 ms | 38474.1 ms | 928.2 ms | 27768.8 ms |
| Uber_zap | LLGoDeadcodeDrop | 36675.5 ms | 35665.7 ms | 1009.8 ms | 16892.8 ms |
| Uber_zap | LLGoNoLTO | 36515.0 ms | 35524.6 ms | 990.3 ms | 16493.7 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 32082.4 ms | 31139.5 ms | 942.9 ms | 19934.3 ms |
| Toml | LLGoFullLTONoGlobalDCE | 30716.3 ms | 29949.9 ms | 766.4 ms | 23342.7 ms |
| Toml | LLGoFullLTOGlobalDCE | 28201.2 ms | 27454.9 ms | 746.4 ms | 19748.6 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 28102.9 ms | 27352.6 ms | 750.2 ms | 19891.5 ms |
| Gorm_schema | LLGoDeadcodeDrop | 25003.6 ms | 24142.2 ms | 861.4 ms | 8634.8 ms |
| Gorm_schema | LLGoNoLTO | 24490.1 ms | 23581.3 ms | 908.9 ms | 8524.3 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 22775.8 ms | 22173.3 ms | 602.5 ms | 17986.0 ms |
| Etcdctl | Go | 22286.8 ms | 20519.3 ms | 1767.5 ms | 6839.9 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 16760.0 ms | 16159.4 ms | 600.6 ms | 12064.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 16316.5 ms | 15735.8 ms | 580.7 ms | 11770.8 ms |
| Toml | LLGoDeadcodeDrop | 16190.4 ms | 15447.8 ms | 742.6 ms | 6322.8 ms |
| Toml | LLGoNoLTO | 14867.3 ms | 14218.7 ms | 648.6 ms | 5751.0 ms |
| XGo | Go | 11909.2 ms | 10974.2 ms | 934.9 ms | 3578.9 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 9130.1 ms | 8594.7 ms | 535.4 ms | 4152.7 ms |
| Dustin_humanize | LLGoNoLTO | 8923.6 ms | 8434.8 ms | 488.7 ms | 3853.7 ms |
| Aws_restjson | Go | 5078.8 ms | 4555.1 ms | 523.7 ms | 2106.2 ms |
| Gorm_schema | Go | 3600.8 ms | 3308.7 ms | 292.1 ms | 1367.6 ms |
| Uber_zap | Go | 3546.5 ms | 3246.6 ms | 299.9 ms | 1426.2 ms |
| K8s_workqueue | Go | 3456.5 ms | 2992.4 ms | 464.1 ms | 2161.5 ms |
| Toml | Go | 1297.6 ms | 1111.3 ms | 186.3 ms | 700.1 ms |
| Dustin_humanize | Go | 525.2 ms | 414.0 ms | 111.2 ms | 260.2 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 958343.4 ms | 598286.8 ms | 8 |
| LLGoFullLTOGlobalDCEPlugin | 891753.7 ms | 562093.5 ms | 8 |
| LLGoFullLTOGlobalDCE | 887161.7 ms | 557764.2 ms | 8 |
| LLGoNoLTO | 692075.2 ms | 246411.6 ms | 8 |
| LLGoDeadcodeDrop | 658908.6 ms | 228193.2 ms | 8 |
| Go | 104111.5 ms | 33659.4 ms | 9 |

Dependency download details are in `download-timings.log`.
