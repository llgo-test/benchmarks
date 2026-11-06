## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| Etcdctl | LLGoFullLTONoGlobalDCE | 437778.3 ms | 428251.6 ms | 9526.8 ms | 307537.6 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 425631.0 ms | 415954.9 ms | 9676.1 ms | 307079.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 419357.2 ms | 410035.2 ms | 9322.0 ms | 300680.8 ms |
| XGo | LLGoFullLTONoGlobalDCE | 303157.6 ms | 296807.2 ms | 6350.4 ms | 240226.2 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 301554.9 ms | 296031.0 ms | 5524.0 ms | 201007.8 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 271485.1 ms | 265069.8 ms | 6415.3 ms | 205081.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 270463.8 ms | 265511.4 ms | 4952.4 ms | 169519.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 270020.5 ms | 264814.4 ms | 5206.1 ms | 168943.6 ms |
| XGo | LLGoFullLTOGlobalDCE | 264082.0 ms | 257948.7 ms | 6133.3 ms | 199102.8 ms |
| Etcdctl | LLGoDeadcodeDrop | 247042.2 ms | 238245.9 ms | 8796.4 ms | 82637.2 ms |
| Etcdctl | LLGoNoLTO | 246181.5 ms | 238393.3 ms | 7788.2 ms | 81386.0 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 244896.0 ms | 240361.1 ms | 4534.9 ms | 169122.8 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 234270.4 ms | 229686.0 ms | 4584.4 ms | 163220.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 233394.6 ms | 228921.3 ms | 4473.3 ms | 161399.3 ms |
| Aws_restjson | LLGoNoLTO | 224525.3 ms | 220093.5 ms | 4431.8 ms | 69429.2 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 221665.5 ms | 217336.7 ms | 4328.8 ms | 146985.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 218360.2 ms | 213900.1 ms | 4460.1 ms | 142321.7 ms |
| Aws_restjson | LLGoDeadcodeDrop | 212190.0 ms | 207714.0 ms | 4476.0 ms | 66267.8 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 201294.1 ms | 196946.5 ms | 4347.7 ms | 129975.8 ms |
| Uber_zap | LLGoNoLTO | 174013.0 ms | 170339.1 ms | 3673.9 ms | 55572.0 ms |
| Uber_zap | LLGoDeadcodeDrop | 170760.4 ms | 166984.5 ms | 3776.0 ms | 54974.8 ms |
| K8s_workqueue | LLGoNoLTO | 163008.1 ms | 159547.0 ms | 3461.1 ms | 52276.4 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 162815.7 ms | 159077.2 ms | 3738.5 ms | 52669.5 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 142881.3 ms | 139784.1 ms | 3097.2 ms | 98113.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 142180.1 ms | 139107.6 ms | 3072.5 ms | 96532.5 ms |
| Toml | LLGoFullLTONoGlobalDCE | 131279.5 ms | 128315.3 ms | 2964.2 ms | 90081.1 ms |
| XGo | LLGoNoLTO | 125226.9 ms | 120456.0 ms | 4770.9 ms | 45010.1 ms |
| XGo | LLGoDeadcodeDrop | 123783.2 ms | 118176.1 ms | 5607.1 ms | 43978.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 122476.8 ms | 119449.2 ms | 3027.6 ms | 75986.3 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 120562.4 ms | 117622.9 ms | 2939.5 ms | 77067.9 ms |
| Toml | LLGoFullLTOGlobalDCE | 116064.9 ms | 113141.1 ms | 2923.8 ms | 73949.0 ms |
| Gorm_schema | LLGoNoLTO | 108560.2 ms | 105930.3 ms | 2629.9 ms | 36575.4 ms |
| Gorm_schema | LLGoDeadcodeDrop | 105512.1 ms | 102722.7 ms | 2789.4 ms | 36314.8 ms |
| Toml | LLGoNoLTO | 101800.2 ms | 99449.1 ms | 2351.1 ms | 34167.6 ms |
| Toml | LLGoDeadcodeDrop | 99270.0 ms | 96834.6 ms | 2435.4 ms | 33591.0 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 93445.9 ms | 91421.7 ms | 2024.2 ms | 66426.1 ms |
| IXGo | Go | 88980.6 ms | 77883.0 ms | 11097.6 ms | 24543.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 75594.3 ms | 73617.2 ms | 1977.1 ms | 48132.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 74288.4 ms | 72451.5 ms | 1836.9 ms | 47319.0 ms |
| Dustin_humanize | LLGoNoLTO | 69438.6 ms | 67794.3 ms | 1644.3 ms | 25377.9 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 66544.0 ms | 64858.1 ms | 1685.9 ms | 24480.5 ms |
| Etcdctl | Go | 35335.0 ms | 31363.6 ms | 3971.4 ms | 10547.8 ms |
| XGo | Go | 20533.5 ms | 18241.0 ms | 2292.4 ms | 6502.1 ms |
| Aws_restjson | Go | 8487.9 ms | 7351.2 ms | 1136.7 ms | 3501.7 ms |
| Gorm_schema | Go | 6095.0 ms | 5343.2 ms | 751.8 ms | 2328.1 ms |
| Uber_zap | Go | 5566.8 ms | 4906.3 ms | 660.4 ms | 2206.9 ms |
| K8s_workqueue | Go | 5004.0 ms | 4343.9 ms | 660.1 ms | 1762.7 ms |
| Toml | Go | 2091.5 ms | 1808.6 ms | 282.9 ms | 1024.2 ms |
| Dustin_humanize | Go | 810.4 ms | 652.5 ms | 157.9 ms | 386.2 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1889264.0 ms | 1335735.8 ms | 8 |
| LLGoFullLTOGlobalDCE | 1747770.2 ms | 1201886.9 ms | 8 |
| LLGoFullLTOGlobalDCEPlugin | 1699150.6 ms | 1148190.3 ms | 8 |
| LLGoNoLTO | 1212753.8 ms | 399794.5 ms | 8 |
| LLGoDeadcodeDrop | 1187917.7 ms | 394913.9 ms | 8 |
| Go | 172904.6 ms | 52803.5 ms | 9 |

Dependency download details are in `download-timings.log`.
