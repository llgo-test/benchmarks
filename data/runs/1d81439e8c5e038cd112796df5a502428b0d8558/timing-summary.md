## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 764272.9 ms | 757509.8 ms | 6763.0 ms | 540877.9 ms |
| IXGo | LLGoFullLTOGlobalDCE | 742114.4 ms | 735463.8 ms | 6650.5 ms | 520389.5 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 716705.7 ms | 710219.5 ms | 6486.3 ms | 499065.6 ms |
| IXGo | LLGoDeadcodeDrop | 425384.9 ms | 419606.7 ms | 5778.2 ms | 150744.3 ms |
| IXGo | LLGoNoLTO | 414590.7 ms | 408917.2 ms | 5673.5 ms | 149615.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 273587.4 ms | 268626.7 ms | 4960.7 ms | 164481.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 271242.5 ms | 266457.9 ms | 4784.6 ms | 162797.5 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 266832.8 ms | 262218.6 ms | 4614.2 ms | 161581.6 ms |
| Etcdctl | LLGoDeadcodeDrop | 199714.8 ms | 195638.4 ms | 4076.4 ms | 65453.6 ms |
| Etcdctl | LLGoNoLTO | 198968.4 ms | 194645.9 ms | 4322.6 ms | 64896.5 ms |
| XGo | LLGoFullLTOGlobalDCE | 182166.1 ms | 178852.2 ms | 3313.9 ms | 125079.8 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 178818.5 ms | 175660.9 ms | 3157.7 ms | 123953.2 ms |
| XGo | LLGoFullLTONoGlobalDCE | 177083.7 ms | 174019.5 ms | 3064.2 ms | 122918.0 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 143468.0 ms | 141096.2 ms | 2371.8 ms | 104685.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 132880.2 ms | 130544.2 ms | 2336.0 ms | 92560.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 131402.2 ms | 129160.4 ms | 2241.8 ms | 91451.4 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 110275.4 ms | 108552.5 ms | 1722.9 ms | 83662.3 ms |
| XGo | LLGoDeadcodeDrop | 109315.8 ms | 106381.4 ms | 2934.4 ms | 40318.6 ms |
| XGo | LLGoNoLTO | 106730.4 ms | 103878.4 ms | 2852.0 ms | 39583.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 104943.8 ms | 103226.2 ms | 1717.6 ms | 81140.8 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 103952.8 ms | 102059.4 ms | 1893.4 ms | 80269.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 101966.5 ms | 100252.7 ms | 1713.8 ms | 74060.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 101072.0 ms | 99360.5 ms | 1711.5 ms | 73912.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 94767.3 ms | 92946.1 ms | 1821.2 ms | 70156.0 ms |
| Aws_restjson | LLGoDeadcodeDrop | 84538.8 ms | 82503.0 ms | 2035.8 ms | 38615.4 ms |
| Aws_restjson | LLGoNoLTO | 82054.6 ms | 80028.7 ms | 2025.8 ms | 37831.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 66145.0 ms | 64713.9 ms | 1431.0 ms | 45542.5 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 64935.4 ms | 63587.2 ms | 1348.3 ms | 44839.8 ms |
| Uber_zap | LLGoDeadcodeDrop | 57891.2 ms | 56401.1 ms | 1490.1 ms | 24529.9 ms |
| Uber_zap | LLGoNoLTO | 55938.0 ms | 54478.6 ms | 1459.5 ms | 23880.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 55233.6 ms | 53861.7 ms | 1371.8 ms | 34247.2 ms |
| Toml | LLGoFullLTONoGlobalDCE | 51384.1 ms | 50394.7 ms | 989.4 ms | 39425.5 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 50172.7 ms | 48680.0 ms | 1492.7 ms | 22329.1 ms |
| K8s_workqueue | LLGoNoLTO | 49727.1 ms | 48201.0 ms | 1526.1 ms | 22021.8 ms |
| Toml | LLGoFullLTOGlobalDCE | 44941.1 ms | 43921.9 ms | 1019.2 ms | 31984.8 ms |
| IXGo | Go | 44267.4 ms | 41232.9 ms | 3034.5 ms | 12634.3 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 44174.6 ms | 43182.0 ms | 992.6 ms | 31355.1 ms |
| Gorm_schema | LLGoDeadcodeDrop | 38926.5 ms | 37680.7 ms | 1245.9 ms | 12722.2 ms |
| Gorm_schema | LLGoNoLTO | 37942.4 ms | 36802.8 ms | 1139.7 ms | 12235.0 ms |
| Etcdctl | Go | 33553.9 ms | 31468.9 ms | 2085.0 ms | 10131.0 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 33310.8 ms | 32497.8 ms | 813.0 ms | 25973.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 25932.0 ms | 25144.1 ms | 787.9 ms | 17957.8 ms |
| Toml | LLGoDeadcodeDrop | 24938.0 ms | 23966.0 ms | 972.0 ms | 9406.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 24764.8 ms | 23996.9 ms | 767.9 ms | 17133.9 ms |
| Toml | LLGoNoLTO | 23871.6 ms | 22960.1 ms | 911.5 ms | 8834.5 ms |
| XGo | Go | 18740.8 ms | 17565.0 ms | 1175.8 ms | 5486.9 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 13821.1 ms | 13117.1 ms | 704.0 ms | 5860.5 ms |
| Dustin_humanize | LLGoNoLTO | 13666.6 ms | 12969.2 ms | 697.5 ms | 5715.9 ms |
| Aws_restjson | Go | 7958.9 ms | 7328.6 ms | 630.4 ms | 3194.5 ms |
| Gorm_schema | Go | 5783.7 ms | 5358.0 ms | 425.7 ms | 2178.1 ms |
| Uber_zap | Go | 5738.9 ms | 5312.5 ms | 426.3 ms | 2219.9 ms |
| K8s_workqueue | Go | 4656.4 ms | 4260.6 ms | 395.8 ms | 1668.9 ms |
| Toml | Go | 2106.8 ms | 1889.0 ms | 217.8 ms | 964.7 ms |
| Dustin_humanize | Go | 843.5 ms | 723.7 ms | 119.8 ms | 408.4 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTOGlobalDCEPlugin | 1671633.0 ms | 1149649.1 ms | 9 |
| LLGoFullLTOGlobalDCE | 1668792.0 ms | 1149432.5 ms | 9 |
| LLGoFullLTONoGlobalDCE | 1667948.9 ms | 1162420.4 ms | 9 |
| LLGoDeadcodeDrop | 1004703.7 ms | 369980.1 ms | 9 |
| LLGoNoLTO | 983490.0 ms | 364614.6 ms | 9 |
| Go | 123650.3 ms | 38886.6 ms | 9 |

Dependency download details are in `download-timings.log`.
