## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 458141.3 ms | 446626.1 ms | 11515.2 ms | 243351.3 ms |
| IXGo | LLGoFullLTOGlobalDCE | 451106.0 ms | 439335.6 ms | 11770.4 ms | 241159.4 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 436759.2 ms | 426380.6 ms | 10378.6 ms | 233442.7 ms |
| IXGo | LLGoDeadcodeDrop | 356775.1 ms | 347083.2 ms | 9691.9 ms | 105579.8 ms |
| IXGo | LLGoNoLTO | 337295.4 ms | 328664.9 ms | 8630.5 ms | 99673.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 214934.7 ms | 210765.0 ms | 4169.7 ms | 134170.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 211581.2 ms | 207262.6 ms | 4318.6 ms | 132881.5 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 209507.8 ms | 205539.9 ms | 3967.8 ms | 132069.9 ms |
| Etcdctl | LLGoDeadcodeDrop | 153219.9 ms | 149568.8 ms | 3651.1 ms | 50438.6 ms |
| Etcdctl | LLGoNoLTO | 150807.2 ms | 147103.3 ms | 3703.9 ms | 49578.3 ms |
| XGo | LLGoFullLTONoGlobalDCE | 148601.9 ms | 145864.2 ms | 2737.6 ms | 104806.3 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 148246.9 ms | 145404.5 ms | 2842.4 ms | 103508.7 ms |
| XGo | LLGoFullLTOGlobalDCE | 146579.9 ms | 143737.6 ms | 2842.2 ms | 101946.8 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 115158.3 ms | 113114.3 ms | 2044.0 ms | 85545.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 106174.3 ms | 104101.0 ms | 2073.3 ms | 75718.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 103608.9 ms | 101554.7 ms | 2054.2 ms | 73370.6 ms |
| XGo | LLGoDeadcodeDrop | 88700.1 ms | 86177.1 ms | 2523.0 ms | 32473.4 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 88067.6 ms | 86531.5 ms | 1536.1 ms | 66943.7 ms |
| XGo | LLGoNoLTO | 86364.6 ms | 83923.6 ms | 2441.0 ms | 31616.2 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 80973.6 ms | 79383.3 ms | 1590.3 ms | 58847.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 79707.5 ms | 78004.9 ms | 1702.6 ms | 58072.7 ms |
| Aws_restjson | LLGoNoLTO | 68097.1 ms | 66289.7 ms | 1807.5 ms | 32642.2 ms |
| Aws_restjson | LLGoDeadcodeDrop | 68096.6 ms | 66394.0 ms | 1702.5 ms | 32039.4 ms |
| IXGo | Go | 67227.4 ms | 62297.4 ms | 4930.0 ms | 19262.7 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 50986.2 ms | 49799.5 ms | 1186.7 ms | 34722.9 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 50123.6 ms | 48934.1 ms | 1189.5 ms | 34783.2 ms |
| Uber_zap | LLGoDeadcodeDrop | 44739.2 ms | 43439.7 ms | 1299.5 ms | 18848.0 ms |
| Uber_zap | LLGoNoLTO | 44407.9 ms | 43130.1 ms | 1277.8 ms | 18400.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 42772.1 ms | 41564.1 ms | 1208.0 ms | 26368.9 ms |
| Toml | LLGoFullLTONoGlobalDCE | 39287.4 ms | 38404.3 ms | 883.1 ms | 29811.4 ms |
| Toml | LLGoFullLTOGlobalDCE | 33660.7 ms | 32826.1 ms | 834.7 ms | 23745.6 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 33632.1 ms | 32746.8 ms | 885.2 ms | 23351.0 ms |
| Gorm_schema | LLGoDeadcodeDrop | 31963.9 ms | 30875.2 ms | 1088.7 ms | 10625.5 ms |
| Gorm_schema | LLGoNoLTO | 30576.2 ms | 29581.9 ms | 994.3 ms | 10331.4 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 28925.9 ms | 28276.4 ms | 649.5 ms | 22694.7 ms |
| Etcdctl | Go | 26831.2 ms | 24933.0 ms | 1898.1 ms | 8638.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 21319.5 ms | 20660.1 ms | 659.4 ms | 14932.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 20942.8 ms | 20277.0 ms | 665.7 ms | 14928.6 ms |
| Toml | LLGoDeadcodeDrop | 19498.3 ms | 18640.5 ms | 857.8 ms | 7467.7 ms |
| Toml | LLGoNoLTO | 18962.8 ms | 18184.1 ms | 778.7 ms | 7369.6 ms |
| XGo | Go | 15155.3 ms | 14093.3 ms | 1062.0 ms | 4553.0 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 11017.3 ms | 10384.1 ms | 633.1 ms | 5002.5 ms |
| Dustin_humanize | LLGoNoLTO | 10749.4 ms | 10154.7 ms | 594.7 ms | 4706.4 ms |
| Aws_restjson | Go | 6327.9 ms | 5765.8 ms | 562.1 ms | 2886.4 ms |
| Gorm_schema | Go | 4579.5 ms | 4275.0 ms | 304.5 ms | 1708.0 ms |
| Uber_zap | Go | 4366.1 ms | 4037.6 ms | 328.6 ms | 1637.9 ms |
| K8s_workqueue | Go | 3808.5 ms | 3447.6 ms | 360.9 ms | 1343.6 ms |
| Toml | Go | 1713.5 ms | 1510.9 ms | 202.6 ms | 1138.2 ms |
| Dustin_humanize | Go | 657.7 ms | 555.0 ms | 102.7 ms | 309.2 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1116431.7 ms | 710097.2 ms | 8 |
| LLGoFullLTOGlobalDCEPlugin | 1106194.5 ms | 680248.5 ms | 8 |
| LLGoFullLTOGlobalDCE | 1098173.2 ms | 680828.3 ms | 8 |
| LLGoDeadcodeDrop | 774010.3 ms | 262474.9 ms | 8 |
| LLGoNoLTO | 747260.7 ms | 254318.0 ms | 8 |
| Go | 130667.2 ms | 41477.5 ms | 9 |

Dependency download details are in `download-timings.log`.
