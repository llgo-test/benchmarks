## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 635057.7 ms | 623238.8 ms | 11818.9 ms | 332181.1 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 620439.5 ms | 609418.0 ms | 11021.5 ms | 329508.5 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 611234.0 ms | 599753.4 ms | 11480.6 ms | 331079.7 ms |
| IXGo | LLGoNoLTO | 482116.2 ms | 471379.8 ms | 10736.4 ms | 138524.7 ms |
| IXGo | LLGoDeadcodeDrop | 463370.1 ms | 449895.4 ms | 13474.7 ms | 138978.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 293681.7 ms | 288270.2 ms | 5411.5 ms | 186971.6 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 289069.5 ms | 283895.9 ms | 5173.6 ms | 185821.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 281812.9 ms | 276856.1 ms | 4956.8 ms | 179576.8 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 227043.5 ms | 223993.7 ms | 3049.8 ms | 135532.8 ms |
| Aws_restjson | LLGoDeadcodeDrop | 215767.4 ms | 212506.0 ms | 3261.3 ms | 75774.5 ms |
| Aws_restjson | LLGoNoLTO | 215272.1 ms | 212514.4 ms | 2757.7 ms | 73654.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 211683.5 ms | 208489.7 ms | 3193.8 ms | 120614.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 209991.3 ms | 206855.6 ms | 3135.7 ms | 119767.9 ms |
| XGo | LLGoFullLTONoGlobalDCE | 200814.5 ms | 197317.3 ms | 3497.2 ms | 145740.8 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 200429.8 ms | 196946.6 ms | 3483.2 ms | 144672.3 ms |
| Etcdctl | LLGoDeadcodeDrop | 199277.2 ms | 194394.6 ms | 4882.6 ms | 65946.1 ms |
| XGo | LLGoFullLTOGlobalDCE | 198734.6 ms | 195301.0 ms | 3433.6 ms | 143227.3 ms |
| Etcdctl | LLGoNoLTO | 196856.0 ms | 192471.9 ms | 4384.1 ms | 65255.9 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 184526.0 ms | 181783.4 ms | 2742.6 ms | 118619.1 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 179876.2 ms | 177080.6 ms | 2795.7 ms | 116140.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 178888.3 ms | 176203.2 ms | 2685.1 ms | 114601.0 ms |
| Uber_zap | LLGoNoLTO | 177935.7 ms | 175569.2 ms | 2366.5 ms | 65011.9 ms |
| Uber_zap | LLGoDeadcodeDrop | 176294.2 ms | 173698.6 ms | 2595.6 ms | 65620.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 175770.4 ms | 173136.7 ms | 2633.6 ms | 107158.9 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 173544.7 ms | 170782.8 ms | 2761.9 ms | 105344.7 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 170125.9 ms | 167343.7 ms | 2782.2 ms | 64351.2 ms |
| K8s_workqueue | LLGoNoLTO | 168481.0 ms | 166059.2 ms | 2421.8 ms | 62363.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 162827.3 ms | 160198.0 ms | 2629.4 ms | 98971.1 ms |
| XGo | LLGoDeadcodeDrop | 112444.3 ms | 109216.4 ms | 3227.9 ms | 41803.6 ms |
| XGo | LLGoNoLTO | 111553.3 ms | 108793.7 ms | 2759.6 ms | 41649.6 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 95519.1 ms | 93768.1 ms | 1751.0 ms | 58372.9 ms |
| Gorm_schema | LLGoDeadcodeDrop | 95033.5 ms | 93318.4 ms | 1715.1 ms | 31575.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 94475.5 ms | 92708.9 ms | 1766.6 ms | 56919.3 ms |
| Gorm_schema | LLGoNoLTO | 93399.7 ms | 91798.5 ms | 1601.2 ms | 30723.8 ms |
| Toml | LLGoFullLTONoGlobalDCE | 88060.3 ms | 86310.7 ms | 1749.6 ms | 52754.4 ms |
| Toml | LLGoDeadcodeDrop | 87251.5 ms | 85645.8 ms | 1605.8 ms | 28991.4 ms |
| Toml | LLGoNoLTO | 87186.8 ms | 85629.1 ms | 1557.7 ms | 28658.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 83225.7 ms | 81565.5 ms | 1660.2 ms | 45044.2 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 81235.6 ms | 79546.1 ms | 1689.5 ms | 44384.6 ms |
| IXGo | Go | 78433.6 ms | 72794.0 ms | 5639.7 ms | 22145.7 ms |
| Toml | LLGoFullLTOGlobalDCE | 78113.3 ms | 76491.2 ms | 1622.1 ms | 43022.2 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 61535.7 ms | 60364.4 ms | 1171.3 ms | 38998.6 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 60750.9 ms | 59541.7 ms | 1209.1 ms | 21829.7 ms |
| Dustin_humanize | LLGoNoLTO | 60161.2 ms | 59105.2 ms | 1056.0 ms | 21326.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 53350.6 ms | 52238.5 ms | 1112.1 ms | 29734.9 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 51463.3 ms | 50368.8 ms | 1094.5 ms | 28928.7 ms |
| Etcdctl | Go | 31669.3 ms | 29558.8 ms | 2110.5 ms | 9404.4 ms |
| XGo | Go | 18259.2 ms | 16990.7 ms | 1268.5 ms | 5256.4 ms |
| Aws_restjson | Go | 7752.0 ms | 7002.7 ms | 749.3 ms | 3559.9 ms |
| Gorm_schema | Go | 5662.0 ms | 5276.4 ms | 385.7 ms | 2142.1 ms |
| Uber_zap | Go | 5155.7 ms | 4753.9 ms | 401.8 ms | 2007.3 ms |
| K8s_workqueue | Go | 4517.0 ms | 4098.4 ms | 418.7 ms | 1644.4 ms |
| Toml | Go | 1933.1 ms | 1714.2 ms | 218.9 ms | 871.6 ms |
| Dustin_humanize | Go | 759.6 ms | 644.0 ms | 115.6 ms | 356.1 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1937678.8 ms | 1183060.1 ms | 9 |
| LLGoFullLTOGlobalDCE | 1902081.7 ms | 1123569.0 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1882644.1 ms | 1107060.2 ms | 9 |
| LLGoNoLTO | 1592962.0 ms | 527167.8 ms | 9 |
| LLGoDeadcodeDrop | 1580315.1 ms | 534869.8 ms | 9 |
| Go | 154141.7 ms | 47387.7 ms | 9 |

Dependency download details are in `download-timings.log`.
