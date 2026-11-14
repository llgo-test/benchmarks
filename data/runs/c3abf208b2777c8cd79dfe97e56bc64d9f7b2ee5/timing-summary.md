## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 915805.0 ms | 888843.1 ms | 26961.9 ms | 577865.2 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 858664.7 ms | 832694.3 ms | 25970.3 ms | 553019.3 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 816593.0 ms | 790398.6 ms | 26194.4 ms | 535157.6 ms |
| IXGo | LLGoDeadcodeDrop | 522621.1 ms | 495213.8 ms | 27407.3 ms | 167280.5 ms |
| IXGo | LLGoNoLTO | 476438.2 ms | 453937.1 ms | 22501.2 ms | 150408.1 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 463938.5 ms | 451400.0 ms | 12538.6 ms | 338495.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 460160.8 ms | 447805.4 ms | 12355.3 ms | 333169.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 455623.1 ms | 443382.9 ms | 12240.2 ms | 331515.2 ms |
| XGo | LLGoFullLTONoGlobalDCE | 363970.7 ms | 355262.0 ms | 8708.7 ms | 290899.3 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 341459.8 ms | 334051.9 ms | 7407.9 ms | 227337.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 330271.6 ms | 322964.7 ms | 7307.0 ms | 205974.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 317853.2 ms | 310610.9 ms | 7242.4 ms | 199418.6 ms |
| XGo | LLGoFullLTOGlobalDCE | 308691.5 ms | 300536.7 ms | 8154.8 ms | 237924.1 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 306592.8 ms | 299827.6 ms | 6765.2 ms | 211289.8 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 306501.7 ms | 298153.1 ms | 8348.6 ms | 235020.3 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 290548.5 ms | 284040.6 ms | 6507.8 ms | 203150.8 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 282374.0 ms | 275955.3 ms | 6418.6 ms | 195647.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 276803.1 ms | 270391.9 ms | 6411.2 ms | 184136.9 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 261684.4 ms | 255551.6 ms | 6132.7 ms | 171797.4 ms |
| Aws_restjson | LLGoNoLTO | 252658.7 ms | 247163.4 ms | 5495.3 ms | 79084.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 252129.2 ms | 245822.8 ms | 6306.3 ms | 163726.2 ms |
| Aws_restjson | LLGoDeadcodeDrop | 247551.4 ms | 241574.3 ms | 5977.1 ms | 79380.1 ms |
| Etcdctl | LLGoDeadcodeDrop | 246643.6 ms | 235848.9 ms | 10794.7 ms | 85873.9 ms |
| Etcdctl | LLGoNoLTO | 238390.6 ms | 228930.0 ms | 9460.6 ms | 81814.2 ms |
| Uber_zap | LLGoNoLTO | 213404.2 ms | 208802.4 ms | 4601.8 ms | 68136.1 ms |
| Uber_zap | LLGoDeadcodeDrop | 205047.8 ms | 199788.6 ms | 5259.2 ms | 66693.4 ms |
| K8s_workqueue | LLGoNoLTO | 198489.4 ms | 193640.9 ms | 4848.6 ms | 63040.3 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 197237.0 ms | 192179.5 ms | 5057.5 ms | 64229.9 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 154951.7 ms | 151101.4 ms | 3850.2 ms | 105011.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 154769.7 ms | 150907.7 ms | 3862.0 ms | 104210.3 ms |
| Toml | LLGoFullLTONoGlobalDCE | 148796.0 ms | 145083.0 ms | 3713.0 ms | 100157.8 ms |
| XGo | LLGoNoLTO | 138665.0 ms | 132363.9 ms | 6301.1 ms | 51063.9 ms |
| XGo | LLGoDeadcodeDrop | 138208.1 ms | 130951.8 ms | 7256.3 ms | 50306.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 131327.2 ms | 127762.4 ms | 3564.8 ms | 80154.7 ms |
| Toml | LLGoFullLTOGlobalDCE | 129125.9 ms | 125601.3 ms | 3524.5 ms | 80845.5 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 127754.6 ms | 124235.5 ms | 3519.1 ms | 79327.1 ms |
| Gorm_schema | LLGoNoLTO | 114516.3 ms | 111393.7 ms | 3122.6 ms | 39544.5 ms |
| Gorm_schema | LLGoDeadcodeDrop | 113821.9 ms | 110283.6 ms | 3538.3 ms | 39425.7 ms |
| Toml | LLGoNoLTO | 108014.1 ms | 105098.4 ms | 2915.7 ms | 36720.1 ms |
| Toml | LLGoDeadcodeDrop | 106843.9 ms | 103730.2 ms | 3113.7 ms | 36612.0 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 99459.5 ms | 96952.6 ms | 2506.9 ms | 69840.2 ms |
| IXGo | Go | 98880.6 ms | 83792.3 ms | 15088.3 ms | 26898.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 81081.1 ms | 78788.0 ms | 2293.0 ms | 50859.5 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 80871.8 ms | 78483.6 ms | 2388.1 ms | 50640.1 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 74240.1 ms | 72027.1 ms | 2212.9 ms | 27541.7 ms |
| Dustin_humanize | LLGoNoLTO | 74135.0 ms | 72098.6 ms | 2036.5 ms | 27441.3 ms |
| Etcdctl | Go | 38901.4 ms | 33571.6 ms | 5329.7 ms | 11793.3 ms |
| XGo | Go | 21909.8 ms | 18777.0 ms | 3132.8 ms | 6486.5 ms |
| Aws_restjson | Go | 9341.8 ms | 7683.0 ms | 1658.8 ms | 3897.8 ms |
| Gorm_schema | Go | 6550.2 ms | 5628.4 ms | 921.8 ms | 2572.3 ms |
| Uber_zap | Go | 6048.7 ms | 5172.9 ms | 875.8 ms | 2451.3 ms |
| K8s_workqueue | Go | 5387.7 ms | 4433.8 ms | 953.9 ms | 1932.4 ms |
| Toml | Go | 2291.9 ms | 1906.1 ms | 385.8 ms | 1103.4 ms |
| Dustin_humanize | Go | 949.3 ms | 707.9 ms | 241.3 ms | 510.7 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2986310.6 ms | 2081340.0 ms | 9 |
| LLGoFullLTOGlobalDCE | 2921917.2 ms | 1962203.3 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2809575.2 ms | 1873049.2 ms | 9 |
| LLGoDeadcodeDrop | 1852215.0 ms | 617343.4 ms | 9 |
| LLGoNoLTO | 1814711.5 ms | 597253.4 ms | 9 |
| Go | 190261.4 ms | 57646.5 ms | 9 |

Dependency download details are in `download-timings.log`.
