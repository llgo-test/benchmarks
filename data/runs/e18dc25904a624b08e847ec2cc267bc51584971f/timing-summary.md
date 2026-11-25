## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 611919.0 ms | 592257.6 ms | 19661.4 ms | 402712.0 ms |
| IXGo | LLGoFullLTOGlobalDCE | 578377.2 ms | 558951.3 ms | 19426.0 ms | 390384.7 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 547612.9 ms | 529535.9 ms | 18076.9 ms | 372283.9 ms |
| IXGo | LLGoDeadcodeDrop | 338908.8 ms | 319452.0 ms | 19456.9 ms | 111156.4 ms |
| IXGo | LLGoNoLTO | 317496.2 ms | 301561.3 ms | 15934.9 ms | 99414.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 314621.1 ms | 305577.9 ms | 9043.2 ms | 232342.5 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 314584.1 ms | 305367.1 ms | 9217.0 ms | 232462.1 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 313986.0 ms | 304704.5 ms | 9281.6 ms | 234870.1 ms |
| XGo | LLGoFullLTONoGlobalDCE | 234118.8 ms | 227728.8 ms | 6390.0 ms | 187225.5 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 216000.5 ms | 210979.7 ms | 5020.8 ms | 147138.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 210936.2 ms | 205666.7 ms | 5269.5 ms | 134437.0 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 205586.6 ms | 199546.3 ms | 6040.3 ms | 159446.8 ms |
| XGo | LLGoFullLTOGlobalDCE | 205015.5 ms | 199022.2 ms | 5993.3 ms | 158054.5 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 185409.5 ms | 180846.6 ms | 4562.9 ms | 132559.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 182388.5 ms | 177578.8 ms | 4809.6 ms | 118884.5 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 180614.7 ms | 176145.3 ms | 4469.5 ms | 130809.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 174831.4 ms | 170328.2 ms | 4503.2 ms | 125194.4 ms |
| Etcdctl | LLGoNoLTO | 169044.1 ms | 162015.4 ms | 7028.6 ms | 58026.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 168128.5 ms | 163830.6 ms | 4297.9 ms | 113768.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 162875.4 ms | 158841.3 ms | 4034.1 ms | 111701.9 ms |
| Etcdctl | LLGoDeadcodeDrop | 161565.8 ms | 153905.8 ms | 7660.0 ms | 57605.1 ms |
| Aws_restjson | LLGoDeadcodeDrop | 159507.5 ms | 155024.9 ms | 4482.6 ms | 51986.9 ms |
| Aws_restjson | LLGoNoLTO | 155945.4 ms | 151570.2 ms | 4375.2 ms | 50135.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 146531.3 ms | 142446.4 ms | 4084.9 ms | 98608.9 ms |
| Uber_zap | LLGoNoLTO | 142378.2 ms | 138775.9 ms | 3602.3 ms | 46422.7 ms |
| Uber_zap | LLGoDeadcodeDrop | 134839.3 ms | 130895.5 ms | 3943.8 ms | 45449.7 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 131991.0 ms | 128034.4 ms | 3956.7 ms | 45004.7 ms |
| K8s_workqueue | LLGoNoLTO | 130544.1 ms | 126920.0 ms | 3624.0 ms | 42349.9 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 117683.1 ms | 114415.3 ms | 3267.7 ms | 84401.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 100513.6 ms | 97665.5 ms | 2848.0 ms | 70635.4 ms |
| XGo | LLGoNoLTO | 94751.8 ms | 89838.0 ms | 4913.7 ms | 35424.4 ms |
| XGo | LLGoDeadcodeDrop | 92016.3 ms | 86765.5 ms | 5250.9 ms | 34448.6 ms |
| Toml | LLGoFullLTONoGlobalDCE | 91479.1 ms | 88703.7 ms | 2775.4 ms | 63498.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 89203.0 ms | 86273.6 ms | 2929.3 ms | 57211.8 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 88708.6 ms | 85892.2 ms | 2816.4 ms | 57952.9 ms |
| Toml | LLGoFullLTOGlobalDCE | 87156.7 ms | 84299.1 ms | 2857.6 ms | 57059.8 ms |
| Gorm_schema | LLGoDeadcodeDrop | 80980.7 ms | 78114.0 ms | 2866.7 ms | 28653.9 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 76347.6 ms | 74220.3 ms | 2127.3 ms | 56348.2 ms |
| Gorm_schema | LLGoNoLTO | 75698.2 ms | 73150.9 ms | 2547.3 ms | 26788.7 ms |
| Toml | LLGoDeadcodeDrop | 73871.6 ms | 71474.2 ms | 2397.3 ms | 26437.8 ms |
| Toml | LLGoNoLTO | 67900.5 ms | 65755.5 ms | 2145.0 ms | 24081.2 ms |
| IXGo | Go | 62305.9 ms | 51665.7 ms | 10640.2 ms | 17294.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 59059.7 ms | 57144.6 ms | 1915.1 ms | 38904.5 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 52727.2 ms | 51030.7 ms | 1696.5 ms | 34630.0 ms |
| Dustin_humanize | LLGoNoLTO | 50484.2 ms | 48805.5 ms | 1678.8 ms | 19401.8 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 46774.9 ms | 45082.2 ms | 1692.7 ms | 18342.8 ms |
| Etcdctl | Go | 25594.5 ms | 21697.8 ms | 3896.7 ms | 7835.4 ms |
| XGo | Go | 14451.8 ms | 12194.2 ms | 2257.6 ms | 4343.5 ms |
| Aws_restjson | Go | 6039.5 ms | 4992.3 ms | 1047.2 ms | 2590.7 ms |
| Gorm_schema | Go | 4227.1 ms | 3542.3 ms | 684.8 ms | 1709.5 ms |
| Uber_zap | Go | 3865.4 ms | 3229.7 ms | 635.7 ms | 1626.6 ms |
| K8s_workqueue | Go | 3539.4 ms | 2843.5 ms | 695.9 ms | 1282.9 ms |
| Toml | Go | 1711.4 ms | 1413.5 ms | 297.9 ms | 810.6 ms |
| Dustin_humanize | Go | 601.0 ms | 453.0 ms | 148.0 ms | 351.2 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1963252.2 ms | 1409136.0 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1888324.5 ms | 1291230.0 ms | 9 |
| LLGoFullLTOGlobalDCE | 1864839.1 ms | 1303162.3 ms | 9 |
| LLGoDeadcodeDrop | 1220455.9 ms | 419085.8 ms | 9 |
| LLGoNoLTO | 1204242.6 ms | 402044.0 ms | 9 |
| Go | 122335.9 ms | 37845.3 ms | 9 |

Dependency download details are in `download-timings.log`.
