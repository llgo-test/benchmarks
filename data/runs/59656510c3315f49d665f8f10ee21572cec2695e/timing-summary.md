## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 588072.1 ms | 567676.1 ms | 20396.0 ms | 381985.0 ms |
| IXGo | LLGoFullLTOGlobalDCE | 565014.1 ms | 545535.8 ms | 19478.3 ms | 374698.0 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 558978.6 ms | 540073.2 ms | 18905.4 ms | 375231.2 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 320260.4 ms | 310652.9 ms | 9607.5 ms | 237240.0 ms |
| IXGo | LLGoDeadcodeDrop | 306907.8 ms | 288249.7 ms | 18658.1 ms | 98275.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 306257.4 ms | 296933.7 ms | 9323.7 ms | 225587.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 303187.3 ms | 294037.7 ms | 9149.6 ms | 224477.8 ms |
| IXGo | LLGoNoLTO | 301667.9 ms | 285519.8 ms | 16148.2 ms | 92411.7 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 229995.1 ms | 224342.1 ms | 5653.0 ms | 159925.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 223305.4 ms | 217863.9 ms | 5441.5 ms | 142790.1 ms |
| XGo | LLGoFullLTONoGlobalDCE | 222290.2 ms | 215975.0 ms | 6315.2 ms | 180674.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 197997.7 ms | 192503.4 ms | 5494.3 ms | 128580.7 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 197952.9 ms | 191834.4 ms | 6118.4 ms | 155076.8 ms |
| XGo | LLGoFullLTOGlobalDCE | 196981.9 ms | 190932.7 ms | 6049.2 ms | 154682.7 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 192956.5 ms | 188037.2 ms | 4919.3 ms | 138834.1 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 177947.4 ms | 173155.5 ms | 4792.0 ms | 126884.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 175496.1 ms | 170771.7 ms | 4724.4 ms | 125147.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 170039.5 ms | 165332.4 ms | 4707.1 ms | 116487.9 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 169300.5 ms | 164693.6 ms | 4606.9 ms | 114940.0 ms |
| Aws_restjson | LLGoDeadcodeDrop | 163130.0 ms | 158310.4 ms | 4819.6 ms | 51837.8 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 154196.9 ms | 149788.8 ms | 4408.1 ms | 102949.1 ms |
| Etcdctl | LLGoDeadcodeDrop | 153737.9 ms | 145637.0 ms | 8100.8 ms | 52990.2 ms |
| Etcdctl | LLGoNoLTO | 149805.0 ms | 142672.9 ms | 7132.1 ms | 50687.2 ms |
| Aws_restjson | LLGoNoLTO | 149465.8 ms | 145297.3 ms | 4168.5 ms | 46549.3 ms |
| Uber_zap | LLGoNoLTO | 134752.0 ms | 130928.6 ms | 3823.5 ms | 42957.3 ms |
| Uber_zap | LLGoDeadcodeDrop | 131934.2 ms | 127984.0 ms | 3950.2 ms | 42736.6 ms |
| K8s_workqueue | LLGoNoLTO | 127416.2 ms | 123628.8 ms | 3787.3 ms | 40426.4 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 121867.7 ms | 117863.7 ms | 4004.0 ms | 40072.8 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 97946.1 ms | 94972.5 ms | 2973.6 ms | 69266.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 95314.5 ms | 92524.5 ms | 2790.0 ms | 67169.8 ms |
| Toml | LLGoFullLTONoGlobalDCE | 94429.6 ms | 91622.4 ms | 2807.2 ms | 67117.5 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 85906.4 ms | 83108.8 ms | 2797.5 ms | 56644.7 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 83464.2 ms | 80632.3 ms | 2831.9 ms | 53940.8 ms |
| XGo | LLGoNoLTO | 83265.0 ms | 78693.2 ms | 4571.7 ms | 30456.4 ms |
| XGo | LLGoDeadcodeDrop | 80401.2 ms | 75180.1 ms | 5221.1 ms | 29511.8 ms |
| Toml | LLGoFullLTOGlobalDCE | 77011.0 ms | 74452.8 ms | 2558.1 ms | 50972.2 ms |
| Gorm_schema | LLGoNoLTO | 70475.7 ms | 68035.2 ms | 2440.6 ms | 24380.5 ms |
| Gorm_schema | LLGoDeadcodeDrop | 66619.2 ms | 64140.1 ms | 2479.0 ms | 23457.4 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 65585.0 ms | 63563.9 ms | 2021.2 ms | 47651.6 ms |
| IXGo | Go | 64556.3 ms | 53576.5 ms | 10979.8 ms | 17782.8 ms |
| Toml | LLGoDeadcodeDrop | 61553.3 ms | 59382.6 ms | 2170.7 ms | 21456.6 ms |
| Toml | LLGoNoLTO | 60775.3 ms | 58576.7 ms | 2198.7 ms | 20962.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 50883.2 ms | 49117.1 ms | 1766.1 ms | 33272.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 49133.5 ms | 47376.6 ms | 1756.9 ms | 32163.5 ms |
| Dustin_humanize | LLGoNoLTO | 46961.1 ms | 45476.9 ms | 1484.2 ms | 17700.0 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 42826.3 ms | 41273.2 ms | 1553.1 ms | 16279.2 ms |
| Etcdctl | Go | 23632.7 ms | 19979.3 ms | 3653.3 ms | 7213.3 ms |
| XGo | Go | 13544.7 ms | 11475.0 ms | 2069.7 ms | 4098.3 ms |
| Aws_restjson | Go | 5824.1 ms | 4627.6 ms | 1196.6 ms | 2510.8 ms |
| Gorm_schema | Go | 3896.7 ms | 3238.6 ms | 658.1 ms | 1623.2 ms |
| Uber_zap | Go | 3884.6 ms | 3259.7 ms | 625.0 ms | 1626.0 ms |
| K8s_workqueue | Go | 3744.3 ms | 3054.6 ms | 689.8 ms | 1370.4 ms |
| Toml | Go | 1479.4 ms | 1207.0 ms | 272.4 ms | 730.6 ms |
| Dustin_humanize | Go | 581.2 ms | 435.3 ms | 145.9 ms | 293.8 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1960388.9 ms | 1402825.8 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1857589.2 ms | 1266077.8 ms | 9 |
| LLGoFullLTOGlobalDCE | 1831925.4 ms | 1275488.4 ms | 9 |
| LLGoDeadcodeDrop | 1128977.5 ms | 376618.3 ms | 9 |
| LLGoNoLTO | 1124584.0 ms | 366531.7 ms | 9 |
| Go | 121144.0 ms | 37249.3 ms | 9 |

Dependency download details are in `download-timings.log`.
