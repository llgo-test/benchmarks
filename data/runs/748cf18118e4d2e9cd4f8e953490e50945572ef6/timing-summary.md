## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 850814.6 ms | 838935.1 ms | 11879.5 ms | 553221.9 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 831312.3 ms | 819292.8 ms | 12019.5 ms | 539122.6 ms |
| IXGo | LLGoFullLTOGlobalDCE | 822319.3 ms | 810356.5 ms | 11962.7 ms | 532382.8 ms |
| IXGo | LLGoDeadcodeDrop | 496183.7 ms | 481852.3 ms | 14331.4 ms | 157814.7 ms |
| IXGo | LLGoNoLTO | 485126.5 ms | 475096.0 ms | 10030.5 ms | 151255.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 432177.7 ms | 425497.2 ms | 6680.5 ms | 317810.8 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 430048.4 ms | 424211.9 ms | 5836.5 ms | 319119.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 425615.7 ms | 419730.5 ms | 5885.2 ms | 312400.1 ms |
| XGo | LLGoFullLTONoGlobalDCE | 322137.0 ms | 317764.7 ms | 4372.3 ms | 259746.2 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 321531.9 ms | 317558.9 ms | 3973.0 ms | 223261.3 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 297071.1 ms | 293083.2 ms | 3987.9 ms | 196897.3 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 289969.6 ms | 286097.0 ms | 3872.7 ms | 190934.8 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 284178.5 ms | 280198.1 ms | 3980.4 ms | 220838.2 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 283443.1 ms | 279931.0 ms | 3512.1 ms | 206972.9 ms |
| XGo | LLGoFullLTOGlobalDCE | 282456.4 ms | 278484.4 ms | 3972.0 ms | 219496.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 265325.5 ms | 261626.4 ms | 3699.0 ms | 191906.6 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 265015.5 ms | 261299.4 ms | 3716.1 ms | 192056.2 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 248569.8 ms | 245277.7 ms | 3292.1 ms | 171271.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 248130.3 ms | 244810.1 ms | 3320.2 ms | 171631.6 ms |
| Aws_restjson | LLGoNoLTO | 235959.5 ms | 232766.9 ms | 3192.7 ms | 83003.3 ms |
| Aws_restjson | LLGoDeadcodeDrop | 235704.7 ms | 232211.8 ms | 3493.0 ms | 83233.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 232670.4 ms | 229280.9 ms | 3389.5 ms | 158888.0 ms |
| Etcdctl | LLGoDeadcodeDrop | 226963.6 ms | 221142.7 ms | 5821.0 ms | 81062.5 ms |
| Etcdctl | LLGoNoLTO | 223648.3 ms | 219371.6 ms | 4276.7 ms | 79541.6 ms |
| Uber_zap | LLGoNoLTO | 197619.3 ms | 194903.2 ms | 2716.1 ms | 74130.1 ms |
| Uber_zap | LLGoDeadcodeDrop | 196107.6 ms | 193108.9 ms | 2998.7 ms | 73844.2 ms |
| K8s_workqueue | LLGoNoLTO | 190004.7 ms | 187253.9 ms | 2750.8 ms | 71430.7 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 189344.2 ms | 186374.0 ms | 2970.2 ms | 71785.3 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 142994.7 ms | 140783.0 ms | 2211.7 ms | 100516.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 141062.7 ms | 138844.8 ms | 2217.9 ms | 98422.3 ms |
| Toml | LLGoFullLTONoGlobalDCE | 130175.8 ms | 127934.0 ms | 2241.8 ms | 90944.6 ms |
| XGo | LLGoNoLTO | 129829.3 ms | 127074.6 ms | 2754.7 ms | 50979.6 ms |
| XGo | LLGoDeadcodeDrop | 128046.5 ms | 124447.7 ms | 3598.8 ms | 49577.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 116671.2 ms | 114675.3 ms | 1995.9 ms | 73716.2 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 112443.4 ms | 110300.4 ms | 2143.0 ms | 72248.6 ms |
| Toml | LLGoFullLTOGlobalDCE | 111645.2 ms | 109392.9 ms | 2252.2 ms | 71637.9 ms |
| Gorm_schema | LLGoDeadcodeDrop | 104800.2 ms | 102872.5 ms | 1927.7 ms | 35925.8 ms |
| Gorm_schema | LLGoNoLTO | 104431.7 ms | 102733.6 ms | 1698.1 ms | 35231.0 ms |
| Toml | LLGoNoLTO | 97504.0 ms | 95690.7 ms | 1813.3 ms | 32659.1 ms |
| Toml | LLGoDeadcodeDrop | 97427.7 ms | 95447.2 ms | 1980.6 ms | 32955.8 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 93637.2 ms | 91976.2 ms | 1661.0 ms | 68087.8 ms |
| IXGo | Go | 83556.8 ms | 78525.2 ms | 5031.6 ms | 22891.9 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 73139.1 ms | 71672.6 ms | 1466.5 ms | 47274.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 72976.8 ms | 71550.0 ms | 1426.8 ms | 47340.4 ms |
| Dustin_humanize | LLGoNoLTO | 67709.5 ms | 66442.2 ms | 1267.3 ms | 24724.1 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 67675.6 ms | 66258.3 ms | 1417.3 ms | 24779.3 ms |
| Etcdctl | Go | 33143.9 ms | 31066.8 ms | 2077.1 ms | 10074.9 ms |
| XGo | Go | 19058.0 ms | 17839.5 ms | 1218.5 ms | 5667.5 ms |
| Aws_restjson | Go | 7996.4 ms | 7154.5 ms | 841.9 ms | 3633.6 ms |
| Gorm_schema | Go | 5719.1 ms | 5319.8 ms | 399.2 ms | 2165.4 ms |
| Uber_zap | Go | 5265.1 ms | 4874.3 ms | 390.7 ms | 2032.9 ms |
| K8s_workqueue | Go | 4793.8 ms | 4270.5 ms | 523.3 ms | 2178.9 ms |
| Toml | Go | 2022.3 ms | 1781.2 ms | 241.1 ms | 922.3 ms |
| Dustin_humanize | Go | 801.8 ms | 643.1 ms | 158.7 ms | 380.6 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2820295.9 ms | 1999827.9 ms | 9 |
| LLGoFullLTOGlobalDCE | 2666602.8 ms | 1842115.7 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2640634.3 ms | 1806204.0 ms | 9 |
| LLGoDeadcodeDrop | 1742253.9 ms | 610978.9 ms | 9 |
| LLGoNoLTO | 1731832.8 ms | 602954.4 ms | 9 |
| Go | 162357.0 ms | 49948.1 ms | 9 |

Dependency download details are in `download-timings.log`.
