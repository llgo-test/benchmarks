## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 660521.9 ms | 644423.8 ms | 16098.1 ms | 442454.2 ms |
| IXGo | LLGoFullLTOGlobalDCE | 641226.2 ms | 625161.7 ms | 16064.5 ms | 427034.1 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 627377.7 ms | 611757.5 ms | 15620.1 ms | 420737.8 ms |
| IXGo | LLGoDeadcodeDrop | 368096.2 ms | 351609.5 ms | 16486.6 ms | 119522.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 354592.5 ms | 347049.2 ms | 7543.2 ms | 265045.4 ms |
| IXGo | LLGoNoLTO | 350098.0 ms | 336362.3 ms | 13735.7 ms | 110189.0 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 336448.1 ms | 329439.1 ms | 7009.0 ms | 252886.5 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 329454.9 ms | 322535.3 ms | 6919.6 ms | 243899.7 ms |
| XGo | LLGoFullLTONoGlobalDCE | 253619.0 ms | 248520.9 ms | 5098.1 ms | 205655.4 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 236025.6 ms | 231722.9 ms | 4302.7 ms | 162451.0 ms |
| XGo | LLGoFullLTOGlobalDCE | 220853.5 ms | 215926.6 ms | 4926.9 ms | 172905.5 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 220673.7 ms | 215827.1 ms | 4846.6 ms | 171865.1 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 210908.9 ms | 206866.8 ms | 4042.1 ms | 135360.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 209318.8 ms | 205203.8 ms | 4114.9 ms | 135390.7 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 195473.6 ms | 191780.3 ms | 3693.3 ms | 141614.3 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 191075.4 ms | 187401.6 ms | 3673.7 ms | 137554.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 184687.2 ms | 181175.3 ms | 3511.9 ms | 133317.8 ms |
| Aws_restjson | LLGoNoLTO | 181627.9 ms | 178080.2 ms | 3547.7 ms | 56761.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 178095.7 ms | 174603.2 ms | 3492.6 ms | 122806.8 ms |
| Aws_restjson | LLGoDeadcodeDrop | 176072.0 ms | 172373.5 ms | 3698.5 ms | 56469.3 ms |
| Etcdctl | LLGoDeadcodeDrop | 175258.0 ms | 168868.4 ms | 6389.6 ms | 61236.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 173386.8 ms | 170002.6 ms | 3384.2 ms | 117628.1 ms |
| Etcdctl | LLGoNoLTO | 172895.3 ms | 167181.8 ms | 5713.5 ms | 59356.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 166096.8 ms | 162662.0 ms | 3434.8 ms | 111472.4 ms |
| Uber_zap | LLGoNoLTO | 146315.9 ms | 143248.5 ms | 3067.3 ms | 47076.5 ms |
| Uber_zap | LLGoDeadcodeDrop | 145498.1 ms | 142235.5 ms | 3262.6 ms | 48098.9 ms |
| K8s_workqueue | LLGoNoLTO | 139299.5 ms | 136299.7 ms | 2999.9 ms | 44867.9 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 137796.2 ms | 134497.7 ms | 3298.5 ms | 46115.8 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 110562.8 ms | 108108.4 ms | 2454.3 ms | 79125.1 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 109287.9 ms | 106926.2 ms | 2361.8 ms | 77173.5 ms |
| Toml | LLGoFullLTONoGlobalDCE | 103556.2 ms | 101278.1 ms | 2278.2 ms | 73112.5 ms |
| XGo | LLGoNoLTO | 98641.1 ms | 94827.4 ms | 3813.6 ms | 36322.9 ms |
| XGo | LLGoDeadcodeDrop | 97693.6 ms | 93556.2 ms | 4137.4 ms | 36232.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 96768.5 ms | 94331.7 ms | 2436.8 ms | 62443.7 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 92063.2 ms | 89772.1 ms | 2291.1 ms | 60862.0 ms |
| Toml | LLGoFullLTOGlobalDCE | 90043.6 ms | 87901.6 ms | 2142.0 ms | 59447.0 ms |
| Gorm_schema | LLGoDeadcodeDrop | 81252.0 ms | 78946.2 ms | 2305.8 ms | 28822.3 ms |
| Gorm_schema | LLGoNoLTO | 80593.5 ms | 78622.0 ms | 1971.5 ms | 28028.2 ms |
| Toml | LLGoDeadcodeDrop | 75047.5 ms | 73158.4 ms | 1889.1 ms | 26361.3 ms |
| Toml | LLGoNoLTO | 74667.3 ms | 72838.6 ms | 1828.6 ms | 26063.2 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 72030.2 ms | 70429.7 ms | 1600.5 ms | 52806.1 ms |
| IXGo | Go | 61688.2 ms | 53998.5 ms | 7689.7 ms | 16886.5 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 57361.7 ms | 55880.1 ms | 1481.7 ms | 37627.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 56702.1 ms | 55251.7 ms | 1450.5 ms | 37023.4 ms |
| Dustin_humanize | LLGoNoLTO | 51818.2 ms | 50554.6 ms | 1263.6 ms | 19498.2 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 51807.8 ms | 50494.9 ms | 1312.9 ms | 19792.3 ms |
| Etcdctl | Go | 24724.9 ms | 21953.3 ms | 2771.6 ms | 7495.9 ms |
| XGo | Go | 13978.6 ms | 12399.4 ms | 1579.2 ms | 4158.2 ms |
| Aws_restjson | Go | 6205.8 ms | 5349.4 ms | 856.4 ms | 2522.2 ms |
| Gorm_schema | Go | 4349.8 ms | 3879.0 ms | 470.8 ms | 1696.8 ms |
| Uber_zap | Go | 4019.2 ms | 3560.9 ms | 458.3 ms | 1587.9 ms |
| K8s_workqueue | Go | 3518.3 ms | 3036.1 ms | 482.2 ms | 1427.5 ms |
| Toml | Go | 1580.8 ms | 1345.6 ms | 235.2 ms | 809.0 ms |
| Dustin_humanize | Go | 609.9 ms | 495.2 ms | 114.6 ms | 333.4 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2126168.5 ms | 1525943.0 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2030124.3 ms | 1404185.1 ms | 9 |
| LLGoFullLTOGlobalDCE | 2021919.8 ms | 1409572.3 ms | 9 |
| LLGoDeadcodeDrop | 1308521.4 ms | 442651.4 ms | 9 |
| LLGoNoLTO | 1295956.6 ms | 428163.6 ms | 9 |
| Go | 120675.6 ms | 36917.5 ms | 9 |

Dependency download details are in `download-timings.log`.
