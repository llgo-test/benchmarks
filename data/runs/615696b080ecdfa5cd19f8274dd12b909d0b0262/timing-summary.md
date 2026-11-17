## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 677952.9 ms | 661126.2 ms | 16826.7 ms | 451305.5 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 653828.0 ms | 636798.9 ms | 17029.1 ms | 438982.1 ms |
| IXGo | LLGoFullLTOGlobalDCE | 645363.3 ms | 628805.3 ms | 16558.1 ms | 428539.2 ms |
| IXGo | LLGoDeadcodeDrop | 369722.2 ms | 353481.7 ms | 16240.5 ms | 119902.6 ms |
| IXGo | LLGoNoLTO | 354010.2 ms | 339637.1 ms | 14373.1 ms | 111541.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 345837.9 ms | 338370.0 ms | 7467.9 ms | 258926.8 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 344735.3 ms | 337296.2 ms | 7439.1 ms | 257711.6 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 339320.6 ms | 331836.9 ms | 7483.7 ms | 251749.7 ms |
| XGo | LLGoFullLTONoGlobalDCE | 251353.3 ms | 246033.5 ms | 5319.8 ms | 201873.8 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 236598.7 ms | 232342.4 ms | 4256.3 ms | 162250.9 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 224612.0 ms | 219555.4 ms | 5056.6 ms | 173782.2 ms |
| XGo | LLGoFullLTOGlobalDCE | 216147.7 ms | 211435.9 ms | 4711.8 ms | 168801.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 210467.1 ms | 206345.8 ms | 4121.2 ms | 136016.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 210386.9 ms | 206330.3 ms | 4056.7 ms | 134505.8 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 191756.8 ms | 188077.2 ms | 3679.6 ms | 138237.1 ms |
| Aws_restjson | LLGoNoLTO | 190061.4 ms | 186485.3 ms | 3576.1 ms | 59017.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 188683.2 ms | 185110.6 ms | 3572.6 ms | 136023.4 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 185413.3 ms | 181899.2 ms | 3514.2 ms | 135496.4 ms |
| Aws_restjson | LLGoDeadcodeDrop | 183289.6 ms | 179383.2 ms | 3906.4 ms | 58947.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 178323.6 ms | 174698.4 ms | 3625.1 ms | 122473.1 ms |
| Etcdctl | LLGoNoLTO | 175510.4 ms | 169488.2 ms | 6022.2 ms | 60418.2 ms |
| Etcdctl | LLGoDeadcodeDrop | 174344.6 ms | 168106.7 ms | 6237.9 ms | 60881.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 174083.4 ms | 170573.4 ms | 3510.0 ms | 118974.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 167477.6 ms | 163978.8 ms | 3498.7 ms | 112192.7 ms |
| Uber_zap | LLGoNoLTO | 145837.0 ms | 142949.5 ms | 2887.5 ms | 46932.3 ms |
| Uber_zap | LLGoDeadcodeDrop | 145591.3 ms | 142395.0 ms | 3196.3 ms | 47896.1 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 141776.9 ms | 138528.5 ms | 3248.5 ms | 47053.9 ms |
| K8s_workqueue | LLGoNoLTO | 138473.1 ms | 135532.0 ms | 2941.1 ms | 44598.9 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 113445.2 ms | 110966.7 ms | 2478.5 ms | 80979.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 112948.6 ms | 110460.7 ms | 2487.9 ms | 79731.6 ms |
| Toml | LLGoFullLTONoGlobalDCE | 106251.6 ms | 103870.2 ms | 2381.4 ms | 74796.6 ms |
| XGo | LLGoDeadcodeDrop | 98379.7 ms | 94079.9 ms | 4299.8 ms | 36263.0 ms |
| XGo | LLGoNoLTO | 96396.6 ms | 92642.4 ms | 3754.2 ms | 35569.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 94853.9 ms | 92554.6 ms | 2299.4 ms | 61253.5 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 94389.4 ms | 92041.2 ms | 2348.2 ms | 62486.0 ms |
| Toml | LLGoFullLTOGlobalDCE | 90420.5 ms | 88229.2 ms | 2191.3 ms | 59798.1 ms |
| Gorm_schema | LLGoDeadcodeDrop | 84114.2 ms | 81828.7 ms | 2285.5 ms | 29905.8 ms |
| Gorm_schema | LLGoNoLTO | 80010.6 ms | 78159.5 ms | 1851.1 ms | 27788.1 ms |
| Toml | LLGoNoLTO | 75937.7 ms | 74073.9 ms | 1863.8 ms | 26426.0 ms |
| Toml | LLGoDeadcodeDrop | 75520.2 ms | 73603.9 ms | 1916.3 ms | 26374.2 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 75371.4 ms | 73683.6 ms | 1687.8 ms | 55098.9 ms |
| IXGo | Go | 63682.9 ms | 55401.8 ms | 8281.0 ms | 17503.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 59359.4 ms | 57864.5 ms | 1494.8 ms | 39270.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 58640.3 ms | 57173.3 ms | 1467.0 ms | 38559.2 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 52906.6 ms | 51538.1 ms | 1368.5 ms | 20213.4 ms |
| Dustin_humanize | LLGoNoLTO | 51795.6 ms | 50464.9 ms | 1330.7 ms | 19499.0 ms |
| Etcdctl | Go | 24956.0 ms | 22181.8 ms | 2774.2 ms | 7514.9 ms |
| XGo | Go | 14422.6 ms | 12787.0 ms | 1635.6 ms | 4298.4 ms |
| Aws_restjson | Go | 6286.4 ms | 5417.6 ms | 868.8 ms | 2618.4 ms |
| Gorm_schema | Go | 4515.0 ms | 3983.2 ms | 531.8 ms | 1772.5 ms |
| Uber_zap | Go | 4205.3 ms | 3723.4 ms | 481.9 ms | 1673.5 ms |
| K8s_workqueue | Go | 3626.0 ms | 3094.5 ms | 531.5 ms | 1564.0 ms |
| Toml | Go | 1572.3 ms | 1360.7 ms | 211.6 ms | 733.5 ms |
| Dustin_humanize | Go | 614.8 ms | 505.7 ms | 109.1 ms | 296.0 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2158753.7 ms | 1545426.6 ms | 9 |
| LLGoFullLTOGlobalDCE | 2047471.1 ms | 1428070.3 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2041797.2 ms | 1406319.4 ms | 9 |
| LLGoDeadcodeDrop | 1325645.3 ms | 447438.5 ms | 9 |
| LLGoNoLTO | 1308032.7 ms | 431791.5 ms | 9 |
| Go | 123881.3 ms | 37974.6 ms | 9 |

Dependency download details are in `download-timings.log`.
