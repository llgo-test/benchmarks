## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 727674.5 ms | 709560.2 ms | 18114.3 ms | 479197.0 ms |
| IXGo | LLGoFullLTOGlobalDCE | 688862.9 ms | 671016.0 ms | 17847.0 ms | 461662.0 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 666739.2 ms | 649417.3 ms | 17321.9 ms | 446554.1 ms |
| IXGo | LLGoNoLTO | 375771.3 ms | 360722.4 ms | 15048.9 ms | 117573.6 ms |
| IXGo | LLGoDeadcodeDrop | 372004.7 ms | 354734.2 ms | 17270.5 ms | 120653.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 349548.4 ms | 341865.2 ms | 7683.2 ms | 259596.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 341019.5 ms | 333711.3 ms | 7308.1 ms | 254975.1 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 329971.6 ms | 322867.8 ms | 7103.8 ms | 247713.1 ms |
| XGo | LLGoFullLTONoGlobalDCE | 261186.6 ms | 255868.7 ms | 5317.9 ms | 211116.8 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 241161.3 ms | 236815.7 ms | 4345.7 ms | 166695.4 ms |
| XGo | LLGoFullLTOGlobalDCE | 235883.6 ms | 230458.7 ms | 5424.8 ms | 183503.9 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 225241.6 ms | 220233.2 ms | 5008.4 ms | 174588.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 215017.1 ms | 210782.7 ms | 4234.4 ms | 139321.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 210305.6 ms | 206306.6 ms | 3999.0 ms | 137350.8 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 206705.2 ms | 202768.6 ms | 3936.6 ms | 148772.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 200377.3 ms | 196430.8 ms | 3946.5 ms | 144658.0 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 197446.9 ms | 193648.0 ms | 3798.9 ms | 143059.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 183789.8 ms | 180094.8 ms | 3695.0 ms | 126636.4 ms |
| Aws_restjson | LLGoDeadcodeDrop | 182648.0 ms | 178662.8 ms | 3985.2 ms | 58675.2 ms |
| Etcdctl | LLGoDeadcodeDrop | 180808.8 ms | 174146.6 ms | 6662.2 ms | 63607.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 180741.6 ms | 177038.8 ms | 3702.8 ms | 124085.6 ms |
| Etcdctl | LLGoNoLTO | 180011.8 ms | 173621.8 ms | 6390.0 ms | 62146.6 ms |
| Aws_restjson | LLGoNoLTO | 177180.5 ms | 173761.8 ms | 3418.7 ms | 55466.1 ms |
| Uber_zap | LLGoDeadcodeDrop | 156540.7 ms | 152891.0 ms | 3649.7 ms | 52085.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 156467.8 ms | 153216.6 ms | 3251.2 ms | 105044.4 ms |
| Uber_zap | LLGoNoLTO | 148331.4 ms | 145162.5 ms | 3168.9 ms | 47833.4 ms |
| K8s_workqueue | LLGoNoLTO | 143895.0 ms | 140822.4 ms | 3072.7 ms | 46415.0 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 140374.1 ms | 137160.4 ms | 3213.7 ms | 46773.1 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 120678.1 ms | 117927.4 ms | 2750.7 ms | 86290.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 118527.5 ms | 115921.2 ms | 2606.3 ms | 83535.3 ms |
| Toml | LLGoFullLTONoGlobalDCE | 106860.8 ms | 104504.5 ms | 2356.3 ms | 75317.2 ms |
| XGo | LLGoNoLTO | 103862.7 ms | 99559.6 ms | 4303.1 ms | 38533.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 98234.1 ms | 95714.0 ms | 2520.1 ms | 63409.7 ms |
| XGo | LLGoDeadcodeDrop | 97583.9 ms | 93234.2 ms | 4349.7 ms | 36348.1 ms |
| Toml | LLGoFullLTOGlobalDCE | 95315.4 ms | 92900.3 ms | 2415.1 ms | 63088.0 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 91602.5 ms | 89389.8 ms | 2212.6 ms | 60425.3 ms |
| Gorm_schema | LLGoDeadcodeDrop | 86102.8 ms | 83554.8 ms | 2548.0 ms | 30710.4 ms |
| Gorm_schema | LLGoNoLTO | 83806.2 ms | 81636.0 ms | 2170.2 ms | 29373.1 ms |
| Toml | LLGoDeadcodeDrop | 79900.1 ms | 77786.6 ms | 2113.6 ms | 28202.1 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 78675.4 ms | 76856.0 ms | 1819.4 ms | 57927.8 ms |
| Toml | LLGoNoLTO | 78544.6 ms | 76589.9 ms | 1954.7 ms | 27448.6 ms |
| IXGo | Go | 63788.7 ms | 55502.7 ms | 8286.1 ms | 17667.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 61357.3 ms | 59753.5 ms | 1603.7 ms | 40885.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 59422.0 ms | 57962.0 ms | 1459.9 ms | 38963.6 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 53740.7 ms | 52270.1 ms | 1470.6 ms | 20569.2 ms |
| Dustin_humanize | LLGoNoLTO | 52236.9 ms | 50937.6 ms | 1299.3 ms | 19675.5 ms |
| Etcdctl | Go | 25847.4 ms | 22866.6 ms | 2980.8 ms | 8039.2 ms |
| XGo | Go | 14566.4 ms | 12995.4 ms | 1571.0 ms | 4298.1 ms |
| Aws_restjson | Go | 6311.4 ms | 5458.0 ms | 853.4 ms | 2583.6 ms |
| Gorm_schema | Go | 4615.6 ms | 4026.0 ms | 589.6 ms | 1834.6 ms |
| Uber_zap | Go | 4070.2 ms | 3613.8 ms | 456.4 ms | 1591.6 ms |
| K8s_workqueue | Go | 3575.1 ms | 3090.6 ms | 484.6 ms | 1266.2 ms |
| Toml | Go | 1624.7 ms | 1391.7 ms | 233.0 ms | 796.2 ms |
| Dustin_humanize | Go | 637.0 ms | 515.6 ms | 121.3 ms | 310.9 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2209425.2 ms | 1583447.0 ms | 9 |
| LLGoFullLTOGlobalDCE | 2143967.8 ms | 1500916.1 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2095420.7 ms | 1440010.4 ms | 9 |
| LLGoDeadcodeDrop | 1349703.9 ms | 457623.7 ms | 9 |
| LLGoNoLTO | 1343640.5 ms | 444465.3 ms | 9 |
| Go | 125036.6 ms | 38388.1 ms | 9 |

Dependency download details are in `download-timings.log`.
