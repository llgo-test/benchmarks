## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 645783.2 ms | 630884.1 ms | 14899.1 ms | 339378.2 ms |
| IXGo | LLGoFullLTOGlobalDCE | 619873.4 ms | 607654.2 ms | 12219.3 ms | 311768.7 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 610279.6 ms | 597673.9 ms | 12605.7 ms | 310688.9 ms |
| IXGo | LLGoDeadcodeDrop | 499380.6 ms | 488718.8 ms | 10661.7 ms | 149528.0 ms |
| IXGo | LLGoNoLTO | 480580.0 ms | 470460.9 ms | 10119.1 ms | 143518.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 272302.8 ms | 266948.0 ms | 5354.8 ms | 167021.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 270322.9 ms | 264896.8 ms | 5426.1 ms | 167106.5 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 262650.6 ms | 257515.0 ms | 5135.6 ms | 163608.0 ms |
| Etcdctl | LLGoDeadcodeDrop | 204747.6 ms | 200064.8 ms | 4682.8 ms | 68670.4 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 194339.9 ms | 190784.5 ms | 3555.4 ms | 134051.0 ms |
| Etcdctl | LLGoNoLTO | 194095.7 ms | 189728.4 ms | 4367.2 ms | 64620.0 ms |
| XGo | LLGoFullLTONoGlobalDCE | 187580.6 ms | 184236.1 ms | 3344.5 ms | 130934.9 ms |
| XGo | LLGoFullLTOGlobalDCE | 187418.3 ms | 183935.2 ms | 3483.1 ms | 129129.5 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 142699.8 ms | 140234.5 ms | 2465.4 ms | 104988.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 129303.5 ms | 126766.5 ms | 2536.9 ms | 90435.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 129267.7 ms | 126869.6 ms | 2398.1 ms | 89933.2 ms |
| XGo | LLGoDeadcodeDrop | 116469.4 ms | 113523.8 ms | 2945.5 ms | 44326.4 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 116246.8 ms | 114297.7 ms | 1949.1 ms | 88724.9 ms |
| XGo | LLGoNoLTO | 112505.9 ms | 109475.5 ms | 3030.4 ms | 42887.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 107517.6 ms | 105432.0 ms | 2085.5 ms | 83307.9 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 107234.0 ms | 105348.5 ms | 1885.5 ms | 83252.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 104877.6 ms | 102959.1 ms | 1918.5 ms | 76010.2 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 102715.0 ms | 100795.6 ms | 1919.4 ms | 74578.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 92946.3 ms | 91084.7 ms | 1861.6 ms | 68713.3 ms |
| Aws_restjson | LLGoDeadcodeDrop | 90990.4 ms | 88652.2 ms | 2338.2 ms | 44012.0 ms |
| Aws_restjson | LLGoNoLTO | 86971.7 ms | 84603.9 ms | 2367.8 ms | 40745.4 ms |
| IXGo | Go | 86473.3 ms | 81002.6 ms | 5470.7 ms | 24391.1 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 65536.3 ms | 64067.3 ms | 1469.0 ms | 44807.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 65532.9 ms | 64029.8 ms | 1503.1 ms | 44295.8 ms |
| Uber_zap | LLGoDeadcodeDrop | 60917.5 ms | 59309.4 ms | 1608.1 ms | 26801.0 ms |
| Uber_zap | LLGoNoLTO | 58470.1 ms | 56755.1 ms | 1715.0 ms | 25940.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 54304.7 ms | 52870.3 ms | 1434.5 ms | 33211.6 ms |
| K8s_workqueue | LLGoNoLTO | 52057.6 ms | 50433.6 ms | 1624.0 ms | 23838.4 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 52036.6 ms | 50399.9 ms | 1636.7 ms | 23989.3 ms |
| Toml | LLGoFullLTONoGlobalDCE | 50363.7 ms | 49232.4 ms | 1131.3 ms | 37776.1 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 44015.3 ms | 42885.3 ms | 1130.0 ms | 30494.7 ms |
| Toml | LLGoFullLTOGlobalDCE | 42682.8 ms | 41571.2 ms | 1111.6 ms | 30103.0 ms |
| Gorm_schema | LLGoNoLTO | 41743.4 ms | 40416.3 ms | 1327.1 ms | 13860.2 ms |
| Gorm_schema | LLGoDeadcodeDrop | 41409.3 ms | 40082.5 ms | 1326.7 ms | 13851.3 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 36419.6 ms | 35439.8 ms | 979.8 ms | 28334.6 ms |
| Etcdctl | Go | 34183.9 ms | 32080.5 ms | 2103.4 ms | 10367.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 27504.0 ms | 26622.8 ms | 881.2 ms | 19364.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 27467.2 ms | 26529.4 ms | 937.8 ms | 19259.0 ms |
| Toml | LLGoDeadcodeDrop | 25473.6 ms | 24393.8 ms | 1079.8 ms | 9559.2 ms |
| Toml | LLGoNoLTO | 25008.2 ms | 23941.1 ms | 1067.1 ms | 9436.6 ms |
| XGo | Go | 19664.6 ms | 18434.0 ms | 1230.6 ms | 5908.1 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 14570.7 ms | 13746.3 ms | 824.4 ms | 6228.8 ms |
| Dustin_humanize | LLGoNoLTO | 14286.4 ms | 13497.9 ms | 788.5 ms | 6064.1 ms |
| Aws_restjson | Go | 8226.3 ms | 7588.4 ms | 637.8 ms | 3349.9 ms |
| Gorm_schema | Go | 5877.3 ms | 5502.5 ms | 374.8 ms | 2241.2 ms |
| Uber_zap | Go | 5419.0 ms | 4999.6 ms | 419.4 ms | 2132.2 ms |
| K8s_workqueue | Go | 4813.2 ms | 4358.1 ms | 455.1 ms | 1704.9 ms |
| Toml | Go | 2100.5 ms | 1853.8 ms | 246.7 ms | 962.5 ms |
| Dustin_humanize | Go | 843.8 ms | 685.9 ms | 157.9 ms | 410.2 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1579010.9 ms | 993116.0 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1565304.6 ms | 958072.2 ms | 9 |
| LLGoFullLTOGlobalDCE | 1552870.4 ms | 950089.2 ms | 9 |
| LLGoDeadcodeDrop | 1105995.7 ms | 386966.5 ms | 9 |
| LLGoNoLTO | 1065719.0 ms | 370911.9 ms | 9 |
| Go | 167601.9 ms | 51467.6 ms | 9 |

Dependency download details are in `download-timings.log`.
