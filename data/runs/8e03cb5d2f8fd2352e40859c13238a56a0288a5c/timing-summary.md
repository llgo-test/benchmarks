## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 665280.3 ms | 648519.7 ms | 16760.6 ms | 441835.4 ms |
| IXGo | LLGoFullLTOGlobalDCE | 640591.8 ms | 624634.4 ms | 15957.4 ms | 426416.2 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 623071.6 ms | 607474.0 ms | 15597.6 ms | 423002.1 ms |
| IXGo | LLGoDeadcodeDrop | 366488.0 ms | 350460.3 ms | 16027.7 ms | 118512.8 ms |
| IXGo | LLGoNoLTO | 356324.6 ms | 342736.7 ms | 13588.0 ms | 111567.7 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 349296.0 ms | 341698.8 ms | 7597.2 ms | 263230.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 340545.3 ms | 333125.8 ms | 7419.4 ms | 253277.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 337747.1 ms | 330316.2 ms | 7430.8 ms | 251068.8 ms |
| XGo | LLGoFullLTONoGlobalDCE | 245077.9 ms | 240169.8 ms | 4908.1 ms | 198944.7 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 228191.6 ms | 224151.5 ms | 4040.1 ms | 156590.5 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 222485.1 ms | 217509.0 ms | 4976.1 ms | 173264.3 ms |
| XGo | LLGoFullLTOGlobalDCE | 216505.5 ms | 211771.1 ms | 4734.4 ms | 168554.3 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 211883.0 ms | 207839.8 ms | 4043.2 ms | 137773.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 204954.1 ms | 201070.7 ms | 3883.4 ms | 132640.9 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 193392.0 ms | 189761.7 ms | 3630.3 ms | 137852.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 191998.4 ms | 188233.3 ms | 3765.1 ms | 138922.8 ms |
| Aws_restjson | LLGoNoLTO | 182975.5 ms | 179263.9 ms | 3711.6 ms | 57678.3 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 182382.1 ms | 178823.9 ms | 3558.2 ms | 131838.9 ms |
| Aws_restjson | LLGoDeadcodeDrop | 179945.9 ms | 176177.1 ms | 3768.8 ms | 58040.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 177466.1 ms | 173999.1 ms | 3467.1 ms | 122192.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 175888.9 ms | 172347.8 ms | 3541.2 ms | 120169.1 ms |
| Etcdctl | LLGoDeadcodeDrop | 175760.2 ms | 169286.5 ms | 6473.7 ms | 61239.3 ms |
| Etcdctl | LLGoNoLTO | 168501.1 ms | 162920.8 ms | 5580.3 ms | 58378.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 165796.6 ms | 162492.6 ms | 3304.0 ms | 111676.5 ms |
| Uber_zap | LLGoDeadcodeDrop | 148008.1 ms | 144857.8 ms | 3150.3 ms | 49114.2 ms |
| Uber_zap | LLGoNoLTO | 145204.1 ms | 142337.3 ms | 2866.9 ms | 46772.5 ms |
| K8s_workqueue | LLGoNoLTO | 139007.2 ms | 136163.6 ms | 2843.6 ms | 44826.7 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 138842.2 ms | 135740.6 ms | 3101.6 ms | 46067.8 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 114975.9 ms | 112380.2 ms | 2595.7 ms | 81876.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 108882.9 ms | 106457.7 ms | 2425.2 ms | 76525.9 ms |
| Toml | LLGoFullLTONoGlobalDCE | 104661.0 ms | 102348.5 ms | 2312.5 ms | 74473.1 ms |
| XGo | LLGoDeadcodeDrop | 95917.9 ms | 91755.6 ms | 4162.3 ms | 35326.7 ms |
| XGo | LLGoNoLTO | 95525.1 ms | 91751.8 ms | 3773.3 ms | 35363.4 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 94671.9 ms | 92330.8 ms | 2341.1 ms | 62377.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 94508.6 ms | 92150.4 ms | 2358.2 ms | 60823.1 ms |
| Toml | LLGoFullLTOGlobalDCE | 93578.2 ms | 91270.5 ms | 2307.7 ms | 61722.1 ms |
| Gorm_schema | LLGoDeadcodeDrop | 83158.9 ms | 80890.9 ms | 2268.0 ms | 29497.6 ms |
| Gorm_schema | LLGoNoLTO | 82033.8 ms | 79931.0 ms | 2102.8 ms | 28634.4 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 75983.6 ms | 74398.0 ms | 1585.6 ms | 55745.2 ms |
| Toml | LLGoDeadcodeDrop | 75921.1 ms | 74013.2 ms | 1907.9 ms | 26563.3 ms |
| Toml | LLGoNoLTO | 74350.2 ms | 72551.7 ms | 1798.5 ms | 25762.8 ms |
| IXGo | Go | 61422.8 ms | 53665.8 ms | 7757.0 ms | 17079.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 59513.4 ms | 58015.9 ms | 1497.4 ms | 39093.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 56696.1 ms | 55237.0 ms | 1459.1 ms | 37021.0 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 54193.4 ms | 52743.8 ms | 1449.6 ms | 20814.1 ms |
| Dustin_humanize | LLGoNoLTO | 52363.3 ms | 51049.9 ms | 1313.4 ms | 19737.3 ms |
| Etcdctl | Go | 25000.5 ms | 22215.8 ms | 2784.7 ms | 7536.4 ms |
| XGo | Go | 14586.2 ms | 12848.7 ms | 1737.6 ms | 4410.6 ms |
| Aws_restjson | Go | 6121.5 ms | 5313.3 ms | 808.2 ms | 2487.8 ms |
| Gorm_schema | Go | 4426.6 ms | 3891.2 ms | 535.4 ms | 1704.4 ms |
| Uber_zap | Go | 4197.7 ms | 3681.0 ms | 516.8 ms | 1691.8 ms |
| K8s_workqueue | Go | 3531.8 ms | 3028.7 ms | 503.1 ms | 1415.6 ms |
| Toml | Go | 1559.1 ms | 1352.3 ms | 206.7 ms | 725.1 ms |
| Dustin_humanize | Go | 611.6 ms | 508.2 ms | 103.4 ms | 302.6 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2117031.7 ms | 1523553.8 ms | 9 |
| LLGoFullLTOGlobalDCE | 2038166.5 ms | 1422269.4 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2020826.9 ms | 1393084.7 ms | 9 |
| LLGoDeadcodeDrop | 1318235.8 ms | 445176.0 ms | 9 |
| LLGoNoLTO | 1296285.0 ms | 428721.7 ms | 9 |
| Go | 121457.7 ms | 37353.3 ms | 9 |

Dependency download details are in `download-timings.log`.
