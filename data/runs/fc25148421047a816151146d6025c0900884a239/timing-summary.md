## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 735436.9 ms | 711391.3 ms | 24045.6 ms | 472491.7 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 712909.8 ms | 689418.1 ms | 23491.7 ms | 461718.4 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 647909.5 ms | 624512.9 ms | 23396.6 ms | 427288.8 ms |
| IXGo | LLGoNoLTO | 400524.4 ms | 380248.7 ms | 20275.7 ms | 125411.8 ms |
| IXGo | LLGoDeadcodeDrop | 393276.0 ms | 369753.9 ms | 23522.2 ms | 128407.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 373147.5 ms | 362012.7 ms | 11134.9 ms | 276110.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 352980.7 ms | 342272.1 ms | 10708.5 ms | 259657.0 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 351459.0 ms | 340665.0 ms | 10794.1 ms | 260876.2 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 272980.3 ms | 266583.4 ms | 6396.9 ms | 186287.6 ms |
| XGo | LLGoFullLTONoGlobalDCE | 266841.2 ms | 259302.4 ms | 7538.8 ms | 214042.4 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 248908.0 ms | 241446.6 ms | 7461.3 ms | 192134.1 ms |
| XGo | LLGoFullLTOGlobalDCE | 238571.9 ms | 231280.5 ms | 7291.4 ms | 183385.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 234929.5 ms | 228903.0 ms | 6026.6 ms | 150474.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 226367.3 ms | 220372.5 ms | 5994.8 ms | 145320.8 ms |
| Aws_restjson | LLGoNoLTO | 224915.7 ms | 219736.2 ms | 5179.4 ms | 73805.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 211508.4 ms | 206059.3 ms | 5449.1 ms | 145490.1 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 206115.8 ms | 200680.7 ms | 5435.1 ms | 148234.0 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 202762.8 ms | 197478.1 ms | 5284.7 ms | 143613.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 201114.3 ms | 195845.7 ms | 5268.6 ms | 143793.5 ms |
| Etcdctl | LLGoDeadcodeDrop | 191104.7 ms | 181385.2 ms | 9719.5 ms | 68161.0 ms |
| Aws_restjson | LLGoDeadcodeDrop | 189654.8 ms | 184002.3 ms | 5652.5 ms | 61752.6 ms |
| Etcdctl | LLGoNoLTO | 183411.5 ms | 174634.0 ms | 8777.5 ms | 64634.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 183012.9 ms | 177987.1 ms | 5025.7 ms | 122778.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 174072.1 ms | 169170.6 ms | 4901.5 ms | 115630.7 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 165619.2 ms | 160717.5 ms | 4901.6 ms | 55652.1 ms |
| Uber_zap | LLGoDeadcodeDrop | 160928.8 ms | 156201.6 ms | 4727.2 ms | 53653.3 ms |
| Uber_zap | LLGoNoLTO | 160758.2 ms | 156240.3 ms | 4518.0 ms | 52267.2 ms |
| K8s_workqueue | LLGoNoLTO | 154791.1 ms | 150065.0 ms | 4726.1 ms | 50465.6 ms |
| Toml | LLGoFullLTONoGlobalDCE | 121549.3 ms | 117939.5 ms | 3609.8 ms | 85244.7 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 119464.2 ms | 115790.8 ms | 3673.4 ms | 83898.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 117692.7 ms | 114158.4 ms | 3534.3 ms | 82179.9 ms |
| XGo | LLGoNoLTO | 111079.2 ms | 105115.8 ms | 5963.5 ms | 42766.5 ms |
| XGo | LLGoDeadcodeDrop | 108931.6 ms | 102393.0 ms | 6538.6 ms | 40640.1 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 105449.7 ms | 102042.8 ms | 3406.8 ms | 69112.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 104300.1 ms | 100737.6 ms | 3562.5 ms | 67060.4 ms |
| Toml | LLGoFullLTOGlobalDCE | 101541.8 ms | 98261.5 ms | 3280.3 ms | 66179.0 ms |
| Gorm_schema | LLGoNoLTO | 90344.8 ms | 87258.1 ms | 3086.6 ms | 31913.9 ms |
| Gorm_schema | LLGoDeadcodeDrop | 86730.2 ms | 83484.8 ms | 3245.4 ms | 31005.3 ms |
| Toml | LLGoDeadcodeDrop | 83587.8 ms | 80765.9 ms | 2821.9 ms | 29691.1 ms |
| Toml | LLGoNoLTO | 81753.8 ms | 79014.4 ms | 2739.3 ms | 28679.9 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 76379.7 ms | 74057.8 ms | 2321.9 ms | 55193.4 ms |
| IXGo | Go | 74151.9 ms | 61088.2 ms | 13063.8 ms | 21565.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 61336.2 ms | 59144.0 ms | 2192.2 ms | 39952.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 60659.4 ms | 58463.6 ms | 2195.9 ms | 39653.2 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 57681.4 ms | 55590.9 ms | 2090.5 ms | 22315.4 ms |
| Dustin_humanize | LLGoNoLTO | 56900.8 ms | 54891.6 ms | 2009.2 ms | 22222.8 ms |
| Etcdctl | Go | 28842.2 ms | 24245.0 ms | 4597.2 ms | 8774.6 ms |
| XGo | Go | 16325.1 ms | 13710.6 ms | 2614.5 ms | 4794.7 ms |
| Aws_restjson | Go | 6972.5 ms | 5635.7 ms | 1336.8 ms | 2969.4 ms |
| Gorm_schema | Go | 4977.1 ms | 4154.1 ms | 823.0 ms | 1987.9 ms |
| Uber_zap | Go | 4856.7 ms | 4038.7 ms | 818.1 ms | 2051.1 ms |
| K8s_workqueue | Go | 4200.8 ms | 3441.0 ms | 759.7 ms | 1583.3 ms |
| Toml | Go | 1791.4 ms | 1422.2 ms | 369.2 ms | 978.6 ms |
| Dustin_humanize | Go | 711.9 ms | 517.3 ms | 194.6 ms | 370.6 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2265461.8 ms | 1604679.6 ms | 9 |
| LLGoFullLTOGlobalDCE | 2254435.6 ms | 1543304.8 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2189503.7 ms | 1489817.0 ms | 9 |
| LLGoNoLTO | 1464479.4 ms | 492168.1 ms | 9 |
| LLGoDeadcodeDrop | 1437514.5 ms | 491278.8 ms | 9 |
| Go | 142829.6 ms | 45075.4 ms | 9 |

Dependency download details are in `download-timings.log`.
