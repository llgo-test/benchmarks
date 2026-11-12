## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 589469.8 ms | 570116.1 ms | 19353.7 ms | 400489.4 ms |
| IXGo | LLGoFullLTOGlobalDCE | 557330.3 ms | 537748.5 ms | 19581.8 ms | 374567.4 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 546786.7 ms | 528006.0 ms | 18780.7 ms | 368453.2 ms |
| IXGo | LLGoNoLTO | 331643.9 ms | 315264.0 ms | 16379.9 ms | 104316.7 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 327084.3 ms | 317890.6 ms | 9193.7 ms | 244848.5 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 325822.3 ms | 316493.3 ms | 9328.9 ms | 245431.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 311820.3 ms | 302446.1 ms | 9374.2 ms | 231589.6 ms |
| IXGo | LLGoDeadcodeDrop | 308830.9 ms | 290338.8 ms | 18492.1 ms | 103219.7 ms |
| XGo | LLGoFullLTONoGlobalDCE | 229235.4 ms | 222830.9 ms | 6404.5 ms | 186628.2 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 224859.2 ms | 219321.3 ms | 5538.0 ms | 154410.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 223040.5 ms | 217720.4 ms | 5320.0 ms | 145043.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 215299.9 ms | 209745.7 ms | 5554.2 ms | 139503.6 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 212534.1 ms | 206336.0 ms | 6198.1 ms | 167381.1 ms |
| XGo | LLGoFullLTOGlobalDCE | 209796.2 ms | 203835.0 ms | 5961.2 ms | 167037.3 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 200497.0 ms | 195633.6 ms | 4863.4 ms | 145766.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 184909.5 ms | 180001.9 ms | 4907.6 ms | 125700.0 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 183579.9 ms | 178763.3 ms | 4816.6 ms | 132390.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 180652.9 ms | 175979.5 ms | 4673.4 ms | 128640.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 171248.0 ms | 166725.3 ms | 4522.7 ms | 116964.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 164638.8 ms | 160173.7 ms | 4465.2 ms | 111135.9 ms |
| Etcdctl | LLGoNoLTO | 158875.4 ms | 151697.4 ms | 7178.0 ms | 55326.8 ms |
| Aws_restjson | LLGoNoLTO | 157604.1 ms | 153292.3 ms | 4311.9 ms | 49925.2 ms |
| Aws_restjson | LLGoDeadcodeDrop | 156725.1 ms | 152157.1 ms | 4568.1 ms | 51122.4 ms |
| Etcdctl | LLGoDeadcodeDrop | 155187.0 ms | 147578.2 ms | 7608.9 ms | 55214.9 ms |
| Uber_zap | LLGoDeadcodeDrop | 131639.0 ms | 128024.7 ms | 3614.3 ms | 43981.5 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 126796.5 ms | 122848.5 ms | 3948.1 ms | 43357.1 ms |
| Uber_zap | LLGoNoLTO | 125517.8 ms | 122143.7 ms | 3374.2 ms | 40677.5 ms |
| K8s_workqueue | LLGoNoLTO | 123226.5 ms | 119746.3 ms | 3480.1 ms | 39817.5 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 117808.2 ms | 114579.1 ms | 3229.1 ms | 82711.6 ms |
| Toml | LLGoFullLTONoGlobalDCE | 96728.9 ms | 93861.1 ms | 2867.8 ms | 68631.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 95422.1 ms | 92528.4 ms | 2893.7 ms | 66353.3 ms |
| XGo | LLGoNoLTO | 89781.6 ms | 85084.3 ms | 4697.3 ms | 33479.7 ms |
| XGo | LLGoDeadcodeDrop | 85368.0 ms | 80212.0 ms | 5155.9 ms | 32161.9 ms |
| Toml | LLGoFullLTOGlobalDCE | 83361.4 ms | 80753.7 ms | 2607.8 ms | 54897.1 ms |
| Toml | LLGoNoLTO | 80439.1 ms | 77930.9 ms | 2508.2 ms | 28239.6 ms |
| Gorm_schema | LLGoNoLTO | 79695.0 ms | 77109.5 ms | 2585.5 ms | 28154.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 79418.4 ms | 76761.9 ms | 2656.5 ms | 50269.9 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 79263.2 ms | 76329.5 ms | 2933.7 ms | 50915.9 ms |
| Gorm_schema | LLGoDeadcodeDrop | 70782.7 ms | 68057.9 ms | 2724.7 ms | 25182.4 ms |
| Toml | LLGoDeadcodeDrop | 64509.9 ms | 62228.4 ms | 2281.6 ms | 23010.2 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 63775.7 ms | 61860.4 ms | 1915.3 ms | 46294.6 ms |
| IXGo | Go | 58119.8 ms | 47851.1 ms | 10268.7 ms | 16325.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 53972.9 ms | 52226.4 ms | 1746.6 ms | 35434.5 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 50128.5 ms | 48382.4 ms | 1746.1 ms | 32516.6 ms |
| Dustin_humanize | LLGoNoLTO | 49437.3 ms | 47861.5 ms | 1575.8 ms | 18954.8 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 44936.5 ms | 43375.7 ms | 1560.8 ms | 17143.7 ms |
| Etcdctl | Go | 25040.7 ms | 21319.9 ms | 3720.9 ms | 7980.9 ms |
| XGo | Go | 12907.6 ms | 10925.9 ms | 1981.6 ms | 3814.2 ms |
| Aws_restjson | Go | 5823.4 ms | 4726.3 ms | 1097.1 ms | 2530.2 ms |
| Gorm_schema | Go | 3883.2 ms | 3252.7 ms | 630.5 ms | 1548.4 ms |
| K8s_workqueue | Go | 3789.9 ms | 3078.1 ms | 711.8 ms | 1420.5 ms |
| Uber_zap | Go | 3500.7 ms | 2909.9 ms | 590.8 ms | 1434.5 ms |
| Toml | Go | 1450.0 ms | 1186.6 ms | 263.4 ms | 697.8 ms |
| Dustin_humanize | Go | 567.9 ms | 425.7 ms | 142.1 ms | 290.8 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1990355.4 ms | 1430134.9 ms | 9 |
| LLGoFullLTOGlobalDCE | 1906567.5 ms | 1337565.6 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1881561.5 ms | 1306306.0 ms | 9 |
| LLGoNoLTO | 1196220.6 ms | 398892.4 ms | 9 |
| LLGoDeadcodeDrop | 1144775.7 ms | 394393.6 ms | 9 |
| Go | 115083.2 ms | 36042.8 ms | 9 |

Dependency download details are in `download-timings.log`.
