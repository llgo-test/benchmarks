## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTONoGlobalDCE | 654707.1 ms | 644576.2 ms | 10130.9 ms | 334993.2 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 643139.1 ms | 631086.2 ms | 12053.0 ms | 335117.6 ms |
| IXGo | LLGoDeadcodeDrop | 640571.1 ms | 627232.1 ms | 13339.0 ms | 190669.6 ms |
| IXGo | LLGoFullLTOGlobalDCE | 617315.7 ms | 607224.5 ms | 10091.2 ms | 324288.9 ms |
| IXGo | LLGoNoLTO | 606170.3 ms | 596723.6 ms | 9446.7 ms | 171501.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 329797.6 ms | 324496.5 ms | 5301.1 ms | 206502.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 305892.9 ms | 301123.6 ms | 4769.3 ms | 190578.0 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 302061.0 ms | 297142.7 ms | 4918.4 ms | 191096.8 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 250136.9 ms | 246901.9 ms | 3234.9 ms | 144622.9 ms |
| Aws_restjson | LLGoNoLTO | 248560.2 ms | 245549.3 ms | 3010.9 ms | 84466.6 ms |
| Aws_restjson | LLGoDeadcodeDrop | 236407.5 ms | 233075.0 ms | 3332.5 ms | 82785.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 231943.0 ms | 228573.7 ms | 3369.3 ms | 129605.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 230473.5 ms | 227196.9 ms | 3276.7 ms | 128329.0 ms |
| XGo | LLGoFullLTONoGlobalDCE | 225770.5 ms | 222019.6 ms | 3750.9 ms | 162004.2 ms |
| Etcdctl | LLGoDeadcodeDrop | 219715.6 ms | 214278.9 ms | 5436.6 ms | 74370.4 ms |
| Etcdctl | LLGoNoLTO | 218499.0 ms | 214320.2 ms | 4178.8 ms | 71755.9 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 217488.3 ms | 214019.2 ms | 3469.1 ms | 154479.3 ms |
| XGo | LLGoFullLTOGlobalDCE | 210063.0 ms | 206641.8 ms | 3421.2 ms | 147563.6 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 207998.8 ms | 204835.9 ms | 3162.9 ms | 132021.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 202734.0 ms | 199772.8 ms | 2961.1 ms | 121457.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 201184.5 ms | 198062.4 ms | 3122.1 ms | 126490.3 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 200187.0 ms | 197204.8 ms | 2982.2 ms | 125127.3 ms |
| Uber_zap | LLGoNoLTO | 198583.7 ms | 196181.0 ms | 2402.7 ms | 72949.0 ms |
| Uber_zap | LLGoDeadcodeDrop | 195292.9 ms | 192436.7 ms | 2856.2 ms | 72849.7 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 194356.2 ms | 191438.4 ms | 2917.8 ms | 72958.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 193902.5 ms | 190973.1 ms | 2929.3 ms | 115352.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 192317.4 ms | 189292.3 ms | 3025.1 ms | 113643.8 ms |
| K8s_workqueue | LLGoNoLTO | 189899.0 ms | 187040.2 ms | 2858.8 ms | 70585.1 ms |
| XGo | LLGoDeadcodeDrop | 126830.8 ms | 123216.2 ms | 3614.6 ms | 47296.6 ms |
| XGo | LLGoNoLTO | 126371.9 ms | 123696.7 ms | 2675.2 ms | 46078.8 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 104654.6 ms | 102867.1 ms | 1787.6 ms | 61757.3 ms |
| Gorm_schema | LLGoDeadcodeDrop | 103224.1 ms | 101377.4 ms | 1846.8 ms | 34118.7 ms |
| Gorm_schema | LLGoNoLTO | 102873.0 ms | 101294.9 ms | 1578.1 ms | 33475.9 ms |
| Toml | LLGoFullLTONoGlobalDCE | 102544.7 ms | 100451.2 ms | 2093.5 ms | 60714.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 101714.2 ms | 99943.5 ms | 1770.7 ms | 59335.8 ms |
| Toml | LLGoDeadcodeDrop | 97480.7 ms | 95581.1 ms | 1899.6 ms | 32021.4 ms |
| Toml | LLGoNoLTO | 97170.8 ms | 95460.6 ms | 1710.2 ms | 31514.3 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 92047.6 ms | 90155.0 ms | 1892.6 ms | 49771.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 91493.4 ms | 89729.4 ms | 1764.0 ms | 48162.8 ms |
| Toml | LLGoFullLTOGlobalDCE | 87016.4 ms | 85164.0 ms | 1852.4 ms | 46509.4 ms |
| IXGo | Go | 84260.8 ms | 79172.6 ms | 5088.1 ms | 23232.4 ms |
| Dustin_humanize | LLGoNoLTO | 70889.1 ms | 69658.1 ms | 1231.0 ms | 24999.2 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 68066.3 ms | 66696.4 ms | 1369.9 ms | 24391.2 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 66366.6 ms | 65077.3 ms | 1289.4 ms | 40820.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 57934.7 ms | 56650.6 ms | 1284.1 ms | 31453.9 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 56841.1 ms | 55619.3 ms | 1221.8 ms | 30954.7 ms |
| Etcdctl | Go | 35320.6 ms | 33151.0 ms | 2169.6 ms | 10750.7 ms |
| XGo | Go | 19463.6 ms | 18206.8 ms | 1256.8 ms | 5964.6 ms |
| Aws_restjson | Go | 8089.7 ms | 7408.6 ms | 681.1 ms | 3258.4 ms |
| Gorm_schema | Go | 5714.6 ms | 5327.6 ms | 387.0 ms | 2169.6 ms |
| Uber_zap | Go | 5383.0 ms | 4950.8 ms | 432.2 ms | 2103.3 ms |
| K8s_workqueue | Go | 4794.3 ms | 4321.0 ms | 473.3 ms | 1691.0 ms |
| Toml | Go | 2064.3 ms | 1819.9 ms | 244.4 ms | 944.5 ms |
| Dustin_humanize | Go | 803.3 ms | 659.7 ms | 143.6 ms | 387.1 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2114427.2 ms | 1253158.6 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2048970.0 ms | 1183590.3 ms | 9 |
| LLGoFullLTOGlobalDCE | 2014328.8 ms | 1176006.2 ms | 9 |
| LLGoDeadcodeDrop | 1881945.2 ms | 631461.0 ms | 9 |
| LLGoNoLTO | 1859017.0 ms | 607325.6 ms | 9 |
| Go | 165894.2 ms | 50501.5 ms | 9 |

Dependency download details are in `download-timings.log`.
