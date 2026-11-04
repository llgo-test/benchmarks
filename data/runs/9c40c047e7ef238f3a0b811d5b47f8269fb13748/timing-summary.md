## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTONoGlobalDCE | 680352.3 ms | 663428.4 ms | 16923.9 ms | 448851.6 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 672277.0 ms | 655342.3 ms | 16934.7 ms | 437507.7 ms |
| IXGo | LLGoFullLTOGlobalDCE | 665159.7 ms | 647982.6 ms | 17177.1 ms | 428562.4 ms |
| IXGo | LLGoNoLTO | 392991.0 ms | 378280.7 ms | 14710.3 ms | 118476.8 ms |
| IXGo | LLGoDeadcodeDrop | 390429.3 ms | 373947.1 ms | 16482.2 ms | 121667.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 325938.8 ms | 317884.2 ms | 8054.6 ms | 245040.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 318024.7 ms | 310200.5 ms | 7824.1 ms | 239299.4 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 309549.3 ms | 301874.6 ms | 7674.7 ms | 234948.5 ms |
| XGo | LLGoFullLTONoGlobalDCE | 233175.2 ms | 227912.0 ms | 5263.2 ms | 191250.0 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 224791.5 ms | 220636.1 ms | 4155.3 ms | 157566.1 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 209805.7 ms | 204644.4 ms | 5161.3 ms | 164149.5 ms |
| XGo | LLGoFullLTOGlobalDCE | 206494.7 ms | 201330.2 ms | 5164.4 ms | 163031.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 200064.5 ms | 195953.3 ms | 4111.2 ms | 133441.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 193424.8 ms | 189589.1 ms | 3835.7 ms | 127500.3 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 184972.8 ms | 181308.7 ms | 3664.1 ms | 136524.5 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 180522.1 ms | 176928.0 ms | 3594.2 ms | 133287.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 171873.1 ms | 168363.4 ms | 3509.7 ms | 127387.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 165734.9 ms | 162326.6 ms | 3408.3 ms | 115202.3 ms |
| Etcdctl | LLGoDeadcodeDrop | 158297.1 ms | 151237.4 ms | 7059.8 ms | 55696.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 156805.4 ms | 153392.8 ms | 3412.6 ms | 108738.4 ms |
| Etcdctl | LLGoNoLTO | 154403.8 ms | 148244.0 ms | 6159.8 ms | 53284.8 ms |
| Aws_restjson | LLGoNoLTO | 149722.0 ms | 146487.5 ms | 3234.6 ms | 47606.8 ms |
| Aws_restjson | LLGoDeadcodeDrop | 148696.3 ms | 145155.8 ms | 3540.5 ms | 47668.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 146353.6 ms | 143031.7 ms | 3321.8 ms | 99623.1 ms |
| Uber_zap | LLGoDeadcodeDrop | 118174.0 ms | 115150.8 ms | 3023.2 ms | 39333.9 ms |
| Uber_zap | LLGoNoLTO | 116054.0 ms | 113385.2 ms | 2668.8 ms | 38064.3 ms |
| K8s_workqueue | LLGoNoLTO | 110087.8 ms | 107379.7 ms | 2708.1 ms | 35950.7 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 109703.8 ms | 106882.9 ms | 2820.8 ms | 36350.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 103182.0 ms | 100637.7 ms | 2544.4 ms | 74325.1 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 102320.5 ms | 99862.6 ms | 2457.9 ms | 74937.7 ms |
| Toml | LLGoFullLTONoGlobalDCE | 94308.1 ms | 92042.8 ms | 2265.3 ms | 67929.5 ms |
| XGo | LLGoDeadcodeDrop | 87006.5 ms | 82484.7 ms | 4521.7 ms | 32201.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 86480.6 ms | 84037.5 ms | 2443.1 ms | 57438.1 ms |
| XGo | LLGoNoLTO | 85512.5 ms | 81524.0 ms | 3988.5 ms | 31912.2 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 82726.7 ms | 80596.9 ms | 2129.8 ms | 54379.6 ms |
| Toml | LLGoFullLTOGlobalDCE | 79672.4 ms | 77648.5 ms | 2023.9 ms | 53262.1 ms |
| Gorm_schema | LLGoDeadcodeDrop | 70383.4 ms | 68323.2 ms | 2060.2 ms | 24952.0 ms |
| Gorm_schema | LLGoNoLTO | 69246.6 ms | 67217.1 ms | 2029.4 ms | 23960.3 ms |
| Toml | LLGoNoLTO | 67834.2 ms | 65979.6 ms | 1854.6 ms | 23198.7 ms |
| Toml | LLGoDeadcodeDrop | 67075.6 ms | 65192.2 ms | 1883.4 ms | 23468.7 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 65648.9 ms | 64094.0 ms | 1554.9 ms | 48788.7 ms |
| IXGo | Go | 64491.3 ms | 55238.1 ms | 9253.2 ms | 17686.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 52613.2 ms | 51133.2 ms | 1480.0 ms | 35520.5 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 50813.4 ms | 49399.3 ms | 1414.1 ms | 34057.7 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 46404.5 ms | 45072.5 ms | 1332.1 ms | 17431.5 ms |
| Dustin_humanize | LLGoNoLTO | 44189.4 ms | 42899.5 ms | 1289.9 ms | 16880.1 ms |
| Etcdctl | Go | 27390.8 ms | 23928.4 ms | 3462.4 ms | 8255.3 ms |
| XGo | Go | 14540.7 ms | 12622.5 ms | 1918.2 ms | 4391.1 ms |
| Aws_restjson | Go | 6034.6 ms | 5104.7 ms | 929.9 ms | 2773.6 ms |
| Gorm_schema | Go | 4422.5 ms | 3780.0 ms | 642.5 ms | 1731.5 ms |
| Uber_zap | Go | 3986.8 ms | 3450.2 ms | 536.5 ms | 1618.2 ms |
| K8s_workqueue | Go | 3436.8 ms | 2921.8 ms | 515.0 ms | 1243.3 ms |
| Toml | Go | 1522.4 ms | 1274.6 ms | 247.8 ms | 722.5 ms |
| Dustin_humanize | Go | 607.9 ms | 480.6 ms | 127.3 ms | 302.3 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2075640.6 ms | 1494084.2 ms | 9 |
| LLGoFullLTOGlobalDCE | 1961019.3 ms | 1368569.6 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1926425.9 ms | 1329898.0 ms | 9 |
| LLGoDeadcodeDrop | 1196170.4 ms | 398770.5 ms | 9 |
| LLGoNoLTO | 1190041.3 ms | 389334.6 ms | 9 |
| Go | 126433.7 ms | 38724.5 ms | 9 |

Dependency download details are in `download-timings.log`.
