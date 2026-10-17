## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 680776.9 ms | 667492.4 ms | 13284.4 ms | 357962.8 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 620651.2 ms | 608637.3 ms | 12013.8 ms | 337540.2 ms |
| IXGo | LLGoFullLTOGlobalDCE | 619245.5 ms | 605633.7 ms | 13611.9 ms | 330105.4 ms |
| IXGo | LLGoNoLTO | 581012.8 ms | 571065.9 ms | 9946.9 ms | 172675.6 ms |
| IXGo | LLGoDeadcodeDrop | 540977.7 ms | 527302.3 ms | 13675.4 ms | 157574.9 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 298114.3 ms | 292622.7 ms | 5491.6 ms | 191928.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 291100.1 ms | 284905.6 ms | 6194.6 ms | 185187.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 287759.6 ms | 282327.0 ms | 5432.6 ms | 183914.1 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 230504.3 ms | 226782.6 ms | 3721.7 ms | 139865.0 ms |
| Aws_restjson | LLGoNoLTO | 224310.5 ms | 220846.8 ms | 3463.7 ms | 78396.1 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 223715.6 ms | 219903.4 ms | 3812.3 ms | 127645.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 221806.3 ms | 218126.9 ms | 3679.3 ms | 127287.5 ms |
| Aws_restjson | LLGoDeadcodeDrop | 221252.8 ms | 217606.6 ms | 3646.2 ms | 78085.6 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 213289.1 ms | 209313.7 ms | 3975.3 ms | 153287.2 ms |
| Etcdctl | LLGoNoLTO | 209946.5 ms | 204886.7 ms | 5059.8 ms | 69061.4 ms |
| XGo | LLGoFullLTOGlobalDCE | 205747.0 ms | 201842.5 ms | 3904.5 ms | 147342.7 ms |
| XGo | LLGoFullLTONoGlobalDCE | 204970.5 ms | 201317.2 ms | 3653.3 ms | 148779.7 ms |
| Etcdctl | LLGoDeadcodeDrop | 204828.0 ms | 199111.5 ms | 5716.6 ms | 68811.3 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 196628.1 ms | 193470.2 ms | 3157.9 ms | 125737.7 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 189968.8 ms | 186692.0 ms | 3276.8 ms | 122631.2 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 186323.6 ms | 183051.3 ms | 3272.3 ms | 112986.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 185145.3 ms | 181854.8 ms | 3290.5 ms | 119047.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 184640.6 ms | 181435.9 ms | 3204.7 ms | 111990.2 ms |
| Uber_zap | LLGoNoLTO | 184024.9 ms | 181116.6 ms | 2908.3 ms | 68601.4 ms |
| Uber_zap | LLGoDeadcodeDrop | 183355.5 ms | 180130.7 ms | 3224.8 ms | 69389.5 ms |
| K8s_workqueue | LLGoNoLTO | 181173.0 ms | 178138.3 ms | 3034.7 ms | 67936.7 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 175313.0 ms | 172121.1 ms | 3191.9 ms | 66477.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 175287.9 ms | 171941.1 ms | 3346.9 ms | 106890.1 ms |
| XGo | LLGoDeadcodeDrop | 116642.8 ms | 112978.9 ms | 3663.9 ms | 44281.4 ms |
| XGo | LLGoNoLTO | 115774.7 ms | 112780.1 ms | 2994.7 ms | 43059.4 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 98808.7 ms | 96768.8 ms | 2039.8 ms | 60386.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 97238.6 ms | 95218.9 ms | 2019.7 ms | 58179.8 ms |
| Gorm_schema | LLGoDeadcodeDrop | 96276.1 ms | 94264.3 ms | 2011.8 ms | 32121.1 ms |
| Gorm_schema | LLGoNoLTO | 95668.5 ms | 93759.6 ms | 1908.8 ms | 31528.6 ms |
| Toml | LLGoDeadcodeDrop | 91850.4 ms | 89699.4 ms | 2151.0 ms | 30614.3 ms |
| Toml | LLGoNoLTO | 90181.3 ms | 88223.4 ms | 1958.0 ms | 29461.5 ms |
| Toml | LLGoFullLTONoGlobalDCE | 89810.4 ms | 87725.6 ms | 2084.8 ms | 54205.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 86185.5 ms | 84210.1 ms | 1975.4 ms | 46844.7 ms |
| Toml | LLGoFullLTOGlobalDCE | 84538.3 ms | 82422.0 ms | 2116.3 ms | 46553.8 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 81167.0 ms | 79116.1 ms | 2050.9 ms | 44437.7 ms |
| IXGo | Go | 79223.3 ms | 74058.1 ms | 5165.2 ms | 21703.1 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 65168.7 ms | 63659.9 ms | 1508.8 ms | 41273.5 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 62919.4 ms | 61391.3 ms | 1528.1 ms | 22770.0 ms |
| Dustin_humanize | LLGoNoLTO | 61155.0 ms | 59856.2 ms | 1298.8 ms | 21825.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 53083.7 ms | 51724.8 ms | 1359.0 ms | 29780.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 53040.7 ms | 51624.5 ms | 1416.2 ms | 29783.7 ms |
| Etcdctl | Go | 31826.6 ms | 29807.8 ms | 2018.9 ms | 9509.9 ms |
| XGo | Go | 18391.0 ms | 17097.0 ms | 1294.0 ms | 5440.2 ms |
| Aws_restjson | Go | 7605.2 ms | 6881.0 ms | 724.2 ms | 3100.9 ms |
| Gorm_schema | Go | 5611.4 ms | 5203.0 ms | 408.4 ms | 2181.3 ms |
| Uber_zap | Go | 5110.7 ms | 4701.4 ms | 409.3 ms | 1984.5 ms |
| K8s_workqueue | Go | 4799.2 ms | 4191.3 ms | 607.9 ms | 2114.9 ms |
| Toml | Go | 1984.9 ms | 1740.3 ms | 244.6 ms | 900.7 ms |
| Dustin_humanize | Go | 791.3 ms | 645.2 ms | 146.1 ms | 387.2 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1994625.0 ms | 1222348.4 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1990886.4 ms | 1165026.2 ms | 9 |
| LLGoFullLTOGlobalDCE | 1939204.9 ms | 1154201.9 ms | 9 |
| LLGoNoLTO | 1743247.2 ms | 582545.9 ms | 9 |
| LLGoDeadcodeDrop | 1693415.8 ms | 570126.0 ms | 9 |
| Go | 155343.7 ms | 47322.5 ms | 9 |

Dependency download details are in `download-timings.log`.
