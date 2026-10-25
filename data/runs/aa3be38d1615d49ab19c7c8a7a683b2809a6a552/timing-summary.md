## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 810266.9 ms | 799873.2 ms | 10393.7 ms | 496789.4 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 718911.1 ms | 707718.4 ms | 11192.6 ms | 465095.5 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 660486.5 ms | 649586.1 ms | 10900.4 ms | 440202.3 ms |
| IXGo | LLGoNoLTO | 400180.4 ms | 391799.8 ms | 8380.6 ms | 123482.1 ms |
| IXGo | LLGoDeadcodeDrop | 382692.2 ms | 370550.6 ms | 12141.6 ms | 123268.3 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 352019.2 ms | 346618.1 ms | 5401.1 ms | 267564.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 341013.0 ms | 335636.2 ms | 5376.9 ms | 257018.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 336860.8 ms | 331489.3 ms | 5371.5 ms | 254169.0 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 267397.6 ms | 263662.6 ms | 3735.0 ms | 187903.9 ms |
| XGo | LLGoFullLTONoGlobalDCE | 257280.7 ms | 253322.9 ms | 3957.9 ms | 211782.4 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 241254.5 ms | 237447.0 ms | 3807.5 ms | 191150.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 234148.3 ms | 230612.7 ms | 3535.5 ms | 155764.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 230103.8 ms | 226721.2 ms | 3382.7 ms | 154660.2 ms |
| XGo | LLGoFullLTOGlobalDCE | 223275.8 ms | 219744.7 ms | 3531.1 ms | 177351.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 213360.9 ms | 210128.4 ms | 3232.4 ms | 158623.7 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 213088.6 ms | 209941.2 ms | 3147.4 ms | 158077.3 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 207971.0 ms | 204760.4 ms | 3210.6 ms | 155283.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 193305.3 ms | 190252.6 ms | 3052.6 ms | 138212.2 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 192902.4 ms | 189734.1 ms | 3168.3 ms | 137052.3 ms |
| Aws_restjson | LLGoDeadcodeDrop | 192223.1 ms | 189040.8 ms | 3182.3 ms | 67368.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 179530.8 ms | 176448.1 ms | 3082.7 ms | 127228.0 ms |
| Aws_restjson | LLGoNoLTO | 176654.2 ms | 173727.3 ms | 2926.9 ms | 63502.7 ms |
| Etcdctl | LLGoNoLTO | 169947.7 ms | 165695.2 ms | 4252.5 ms | 63062.3 ms |
| Etcdctl | LLGoDeadcodeDrop | 168334.9 ms | 163529.4 ms | 4805.5 ms | 61513.8 ms |
| Uber_zap | LLGoDeadcodeDrop | 147549.4 ms | 144854.4 ms | 2694.9 ms | 57275.5 ms |
| Uber_zap | LLGoNoLTO | 146416.7 ms | 143989.6 ms | 2427.1 ms | 56375.1 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 144097.8 ms | 141315.6 ms | 2782.2 ms | 56276.6 ms |
| K8s_workqueue | LLGoNoLTO | 140498.3 ms | 138032.9 ms | 2465.4 ms | 54417.0 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 109981.3 ms | 107997.7 ms | 1983.6 ms | 80113.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 108729.6 ms | 106726.8 ms | 2002.7 ms | 78250.8 ms |
| Toml | LLGoFullLTONoGlobalDCE | 106803.0 ms | 104663.7 ms | 2139.3 ms | 77142.2 ms |
| XGo | LLGoNoLTO | 98843.5 ms | 96218.8 ms | 2624.7 ms | 40236.5 ms |
| XGo | LLGoDeadcodeDrop | 97286.7 ms | 93923.0 ms | 3363.7 ms | 39813.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 89172.4 ms | 87287.0 ms | 1885.5 ms | 57890.2 ms |
| Toml | LLGoFullLTOGlobalDCE | 88225.4 ms | 86180.7 ms | 2044.8 ms | 58359.0 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 87421.6 ms | 85412.8 ms | 2008.8 ms | 57701.6 ms |
| Gorm_schema | LLGoDeadcodeDrop | 79624.2 ms | 77789.4 ms | 1834.8 ms | 27491.0 ms |
| Gorm_schema | LLGoNoLTO | 75948.8 ms | 74433.9 ms | 1514.9 ms | 25789.3 ms |
| Toml | LLGoDeadcodeDrop | 74658.2 ms | 72770.3 ms | 1887.9 ms | 25676.7 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 72691.6 ms | 71150.8 ms | 1540.8 ms | 54331.0 ms |
| Toml | LLGoNoLTO | 71469.3 ms | 69783.1 ms | 1686.2 ms | 24371.7 ms |
| IXGo | Go | 64288.0 ms | 59956.7 ms | 4331.3 ms | 17978.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 57715.9 ms | 56367.3 ms | 1348.6 ms | 38702.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 57126.4 ms | 55687.1 ms | 1439.4 ms | 38602.6 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 50184.9 ms | 48829.0 ms | 1355.9 ms | 18900.8 ms |
| Dustin_humanize | LLGoNoLTO | 49122.4 ms | 47933.7 ms | 1188.7 ms | 18098.8 ms |
| Etcdctl | Go | 25670.5 ms | 23918.3 ms | 1752.3 ms | 7793.4 ms |
| XGo | Go | 14126.7 ms | 13197.9 ms | 928.8 ms | 4204.8 ms |
| Aws_restjson | Go | 5974.8 ms | 5390.1 ms | 584.7 ms | 2510.7 ms |
| Gorm_schema | Go | 4324.9 ms | 3986.0 ms | 339.0 ms | 1684.3 ms |
| Uber_zap | Go | 3960.0 ms | 3628.9 ms | 331.0 ms | 1563.2 ms |
| K8s_workqueue | Go | 3499.8 ms | 3124.2 ms | 375.7 ms | 1275.1 ms |
| Toml | Go | 1567.3 ms | 1353.5 ms | 213.9 ms | 733.8 ms |
| Dustin_humanize | Go | 706.1 ms | 553.7 ms | 152.5 ms | 354.9 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTOGlobalDCE | 2265888.8 ms | 1556222.3 ms | 9 |
| LLGoFullLTONoGlobalDCE | 2247719.5 ms | 1632401.1 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2137436.2 ms | 1486399.1 ms | 9 |
| LLGoDeadcodeDrop | 1336651.4 ms | 477584.4 ms | 9 |
| LLGoNoLTO | 1329081.3 ms | 469335.5 ms | 9 |
| Go | 124118.2 ms | 38098.9 ms | 9 |

Dependency download details are in `download-timings.log`.
