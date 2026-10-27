## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 828235.6 ms | 816606.9 ms | 11628.7 ms | 537718.3 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 823353.6 ms | 809534.6 ms | 13819.0 ms | 532487.1 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 818037.3 ms | 806070.0 ms | 11967.3 ms | 532201.7 ms |
| IXGo | LLGoNoLTO | 510778.9 ms | 501160.2 ms | 9618.7 ms | 158032.5 ms |
| IXGo | LLGoDeadcodeDrop | 488672.3 ms | 474804.2 ms | 13868.1 ms | 156430.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 438012.9 ms | 431816.9 ms | 6195.9 ms | 322658.1 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 424230.2 ms | 418495.4 ms | 5734.8 ms | 315608.6 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 424208.6 ms | 418190.9 ms | 6017.7 ms | 311707.1 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 324632.1 ms | 320457.7 ms | 4174.4 ms | 226447.3 ms |
| XGo | LLGoFullLTONoGlobalDCE | 319596.6 ms | 315275.3 ms | 4321.3 ms | 257328.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 288859.0 ms | 284995.0 ms | 3864.0 ms | 191163.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 286852.9 ms | 282833.1 ms | 4019.8 ms | 189806.3 ms |
| XGo | LLGoFullLTOGlobalDCE | 280128.7 ms | 276250.9 ms | 3877.8 ms | 217824.9 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 279912.6 ms | 276034.9 ms | 3877.7 ms | 217115.7 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 278474.2 ms | 274921.4 ms | 3552.7 ms | 202452.9 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 262115.2 ms | 258614.5 ms | 3500.7 ms | 190105.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 260972.8 ms | 257499.0 ms | 3473.8 ms | 188434.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 245195.4 ms | 241913.0 ms | 3282.4 ms | 169592.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 244151.3 ms | 240826.4 ms | 3324.9 ms | 169297.3 ms |
| Aws_restjson | LLGoDeadcodeDrop | 233409.5 ms | 229985.6 ms | 3423.9 ms | 82434.2 ms |
| Aws_restjson | LLGoNoLTO | 233052.5 ms | 230034.7 ms | 3017.8 ms | 82416.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 228328.1 ms | 224902.6 ms | 3425.5 ms | 156180.0 ms |
| Etcdctl | LLGoNoLTO | 225496.0 ms | 221017.9 ms | 4478.1 ms | 80092.2 ms |
| Etcdctl | LLGoDeadcodeDrop | 223009.2 ms | 217626.0 ms | 5383.2 ms | 79891.2 ms |
| Uber_zap | LLGoDeadcodeDrop | 199381.1 ms | 196199.0 ms | 3182.1 ms | 75255.0 ms |
| Uber_zap | LLGoNoLTO | 194661.3 ms | 191927.3 ms | 2734.0 ms | 73142.7 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 187286.3 ms | 184361.0 ms | 2925.3 ms | 71081.5 ms |
| K8s_workqueue | LLGoNoLTO | 186761.0 ms | 184087.5 ms | 2673.5 ms | 70729.1 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 140877.6 ms | 138695.4 ms | 2182.3 ms | 99019.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 139352.3 ms | 137083.9 ms | 2268.4 ms | 97315.7 ms |
| Toml | LLGoFullLTONoGlobalDCE | 129032.5 ms | 126735.8 ms | 2296.8 ms | 89983.7 ms |
| XGo | LLGoNoLTO | 128027.5 ms | 125200.2 ms | 2827.3 ms | 50377.6 ms |
| XGo | LLGoDeadcodeDrop | 126927.0 ms | 123373.5 ms | 3553.5 ms | 49231.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 115136.6 ms | 113233.3 ms | 1903.2 ms | 72610.5 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 114344.4 ms | 112097.2 ms | 2247.2 ms | 74112.3 ms |
| Toml | LLGoFullLTOGlobalDCE | 109925.7 ms | 107793.9 ms | 2131.7 ms | 70694.1 ms |
| Gorm_schema | LLGoNoLTO | 104157.6 ms | 102439.0 ms | 1718.7 ms | 34932.6 ms |
| Gorm_schema | LLGoDeadcodeDrop | 103595.3 ms | 101672.8 ms | 1922.5 ms | 35382.5 ms |
| Toml | LLGoNoLTO | 97062.9 ms | 95188.2 ms | 1874.7 ms | 32323.6 ms |
| Toml | LLGoDeadcodeDrop | 96923.2 ms | 94898.0 ms | 2025.2 ms | 32817.3 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 92962.4 ms | 91369.2 ms | 1593.2 ms | 67677.5 ms |
| IXGo | Go | 82934.9 ms | 78069.0 ms | 4865.9 ms | 22677.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 72695.8 ms | 71218.6 ms | 1477.3 ms | 47065.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 72412.6 ms | 70947.0 ms | 1465.6 ms | 46916.7 ms |
| Dustin_humanize | LLGoNoLTO | 66674.9 ms | 65455.0 ms | 1219.9 ms | 24230.1 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 66674.2 ms | 65263.9 ms | 1410.3 ms | 24376.9 ms |
| Etcdctl | Go | 32910.8 ms | 30946.4 ms | 1964.4 ms | 9810.8 ms |
| XGo | Go | 18951.3 ms | 17810.7 ms | 1140.6 ms | 5458.2 ms |
| Aws_restjson | Go | 7837.3 ms | 7212.8 ms | 624.5 ms | 3130.2 ms |
| Gorm_schema | Go | 5681.1 ms | 5294.4 ms | 386.7 ms | 2140.0 ms |
| Uber_zap | Go | 5196.4 ms | 4777.9 ms | 418.5 ms | 2057.0 ms |
| K8s_workqueue | Go | 4619.5 ms | 4185.7 ms | 433.8 ms | 1638.7 ms |
| Toml | Go | 1997.3 ms | 1780.0 ms | 217.3 ms | 895.8 ms |
| Dustin_humanize | Go | 799.4 ms | 639.7 ms | 159.8 ms | 384.7 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2789958.2 ms | 1980825.5 ms | 9 |
| LLGoFullLTOGlobalDCE | 2648246.6 ms | 1831071.1 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2603832.3 ms | 1781628.3 ms | 9 |
| LLGoNoLTO | 1746672.7 ms | 606276.6 ms | 9 |
| LLGoDeadcodeDrop | 1725878.2 ms | 606900.4 ms | 9 |
| Go | 160927.9 ms | 48192.8 ms | 9 |

Dependency download details are in `download-timings.log`.
