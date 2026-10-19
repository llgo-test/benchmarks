## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 683748.0 ms | 673523.9 ms | 10224.1 ms | 347032.7 ms |
| IXGo | LLGoFullLTOGlobalDCE | 661529.6 ms | 650751.4 ms | 10778.2 ms | 343382.9 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 645314.3 ms | 635469.2 ms | 9845.2 ms | 336382.7 ms |
| IXGo | LLGoDeadcodeDrop | 512584.3 ms | 498311.5 ms | 14272.9 ms | 150621.3 ms |
| IXGo | LLGoNoLTO | 504858.4 ms | 495549.0 ms | 9309.4 ms | 144675.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 317165.7 ms | 312049.5 ms | 5116.3 ms | 198102.8 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 301587.5 ms | 296678.6 ms | 4908.9 ms | 190151.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 300182.8 ms | 295283.4 ms | 4899.4 ms | 188061.0 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 246144.9 ms | 242787.3 ms | 3357.6 ms | 144602.7 ms |
| Aws_restjson | LLGoNoLTO | 244248.7 ms | 241308.4 ms | 2940.4 ms | 82715.1 ms |
| Aws_restjson | LLGoDeadcodeDrop | 243272.3 ms | 239982.3 ms | 3290.0 ms | 84062.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 238691.6 ms | 235454.9 ms | 3236.7 ms | 131900.1 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 221921.4 ms | 218707.0 ms | 3214.4 ms | 124975.4 ms |
| Etcdctl | LLGoDeadcodeDrop | 221526.7 ms | 216315.6 ms | 5211.1 ms | 73242.9 ms |
| Etcdctl | LLGoNoLTO | 216974.2 ms | 212822.5 ms | 4151.7 ms | 70207.1 ms |
| XGo | LLGoFullLTONoGlobalDCE | 213123.2 ms | 209620.6 ms | 3502.6 ms | 150988.1 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 207168.5 ms | 204254.0 ms | 2914.5 ms | 128504.6 ms |
| Uber_zap | LLGoNoLTO | 200018.1 ms | 197448.2 ms | 2569.9 ms | 72819.7 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 197863.2 ms | 194519.9 ms | 3343.3 ms | 133832.8 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 196907.0 ms | 193888.4 ms | 3018.6 ms | 123077.3 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 195203.4 ms | 192228.1 ms | 2975.3 ms | 123088.2 ms |
| Uber_zap | LLGoDeadcodeDrop | 194790.4 ms | 191986.2 ms | 2804.2 ms | 71690.2 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 193242.5 ms | 190269.6 ms | 2972.9 ms | 114916.6 ms |
| XGo | LLGoFullLTOGlobalDCE | 191851.3 ms | 188533.4 ms | 3317.9 ms | 129515.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 188710.9 ms | 185910.4 ms | 2800.6 ms | 112806.1 ms |
| K8s_workqueue | LLGoNoLTO | 187961.4 ms | 185334.5 ms | 2626.9 ms | 68691.5 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 186722.5 ms | 183818.6 ms | 2903.9 ms | 68974.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 179685.6 ms | 176911.3 ms | 2774.3 ms | 104930.4 ms |
| XGo | LLGoNoLTO | 125903.9 ms | 123182.6 ms | 2721.3 ms | 45235.0 ms |
| XGo | LLGoDeadcodeDrop | 124969.4 ms | 121441.3 ms | 3528.1 ms | 45987.3 ms |
| Gorm_schema | LLGoDeadcodeDrop | 106381.6 ms | 104551.2 ms | 1830.4 ms | 34942.6 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 103772.6 ms | 101968.2 ms | 1804.4 ms | 61556.4 ms |
| Gorm_schema | LLGoNoLTO | 103501.2 ms | 101953.4 ms | 1547.8 ms | 33832.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 102120.7 ms | 100394.9 ms | 1725.7 ms | 59628.8 ms |
| Toml | LLGoNoLTO | 101024.0 ms | 99270.7 ms | 1753.3 ms | 32475.2 ms |
| Toml | LLGoFullLTONoGlobalDCE | 98770.9 ms | 96853.2 ms | 1917.8 ms | 57790.7 ms |
| Toml | LLGoDeadcodeDrop | 98262.5 ms | 96439.9 ms | 1822.5 ms | 32516.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 91688.4 ms | 89943.4 ms | 1745.1 ms | 48378.4 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 87060.1 ms | 85223.7 ms | 1836.4 ms | 46499.0 ms |
| Toml | LLGoFullLTOGlobalDCE | 86482.4 ms | 84681.8 ms | 1800.6 ms | 46441.9 ms |
| IXGo | Go | 85033.2 ms | 79934.6 ms | 5098.7 ms | 23294.1 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 68600.7 ms | 67305.3 ms | 1295.4 ms | 24435.7 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 67965.6 ms | 66622.0 ms | 1343.6 ms | 41981.1 ms |
| Dustin_humanize | LLGoNoLTO | 66461.8 ms | 65189.4 ms | 1272.4 ms | 23474.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 59444.9 ms | 58226.8 ms | 1218.1 ms | 32562.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 57684.3 ms | 56449.0 ms | 1235.3 ms | 31446.5 ms |
| Etcdctl | Go | 33668.1 ms | 31367.2 ms | 2300.9 ms | 10806.9 ms |
| XGo | Go | 19468.2 ms | 18217.4 ms | 1250.8 ms | 5916.4 ms |
| Aws_restjson | Go | 7997.1 ms | 7319.2 ms | 678.0 ms | 3256.5 ms |
| Gorm_schema | Go | 5860.3 ms | 5472.5 ms | 387.8 ms | 2284.3 ms |
| Uber_zap | Go | 5319.1 ms | 4928.4 ms | 390.7 ms | 2074.5 ms |
| K8s_workqueue | Go | 4740.2 ms | 4292.0 ms | 448.2 ms | 1679.9 ms |
| Toml | Go | 2070.9 ms | 1837.8 ms | 233.1 ms | 947.4 ms |
| Dustin_humanize | Go | 837.3 ms | 676.2 ms | 161.1 ms | 400.7 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2079050.9 ms | 1235046.2 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2046829.5 ms | 1157039.2 ms | 9 |
| LLGoFullLTOGlobalDCE | 2009150.9 ms | 1160450.8 ms | 9 |
| LLGoDeadcodeDrop | 1757110.5 ms | 586473.1 ms | 9 |
| LLGoNoLTO | 1750951.7 ms | 574126.3 ms | 9 |
| Go | 164994.5 ms | 50660.6 ms | 9 |

Dependency download details are in `download-timings.log`.
