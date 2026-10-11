## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 565783.1 ms | 556535.4 ms | 9247.7 ms | 288723.5 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 563330.2 ms | 553046.1 ms | 10284.1 ms | 291240.5 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 506624.1 ms | 496796.2 ms | 9827.9 ms | 274079.1 ms |
| IXGo | LLGoNoLTO | 498256.4 ms | 488764.3 ms | 9492.2 ms | 149269.6 ms |
| IXGo | LLGoDeadcodeDrop | 442581.3 ms | 431003.1 ms | 11578.1 ms | 135645.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 241131.4 ms | 236299.3 ms | 4832.1 ms | 155224.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 238053.8 ms | 233506.6 ms | 4547.2 ms | 152028.0 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 236217.3 ms | 231782.4 ms | 4434.9 ms | 154756.5 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 198910.7 ms | 195526.2 ms | 3384.5 ms | 122822.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 177683.5 ms | 174446.5 ms | 3237.0 ms | 104607.5 ms |
| Aws_restjson | LLGoDeadcodeDrop | 176744.3 ms | 173755.2 ms | 2989.1 ms | 63809.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 176030.6 ms | 172701.2 ms | 3329.4 ms | 104139.2 ms |
| Aws_restjson | LLGoNoLTO | 174163.4 ms | 171170.9 ms | 2992.4 ms | 63003.8 ms |
| XGo | LLGoFullLTONoGlobalDCE | 169609.2 ms | 166523.9 ms | 3085.3 ms | 124042.8 ms |
| XGo | LLGoFullLTOGlobalDCE | 168405.1 ms | 165298.7 ms | 3106.4 ms | 123111.8 ms |
| Etcdctl | LLGoDeadcodeDrop | 167371.1 ms | 162771.4 ms | 4599.7 ms | 57574.3 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 167200.0 ms | 164133.4 ms | 3066.7 ms | 123042.2 ms |
| Etcdctl | LLGoNoLTO | 162799.0 ms | 159065.5 ms | 3733.5 ms | 54809.1 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 151421.0 ms | 148643.4 ms | 2777.6 ms | 99565.2 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 149986.8 ms | 147103.4 ms | 2883.4 ms | 94423.2 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 149156.3 ms | 146275.9 ms | 2880.4 ms | 98615.6 ms |
| Uber_zap | LLGoDeadcodeDrop | 147836.5 ms | 145231.3 ms | 2605.3 ms | 57932.8 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 147737.6 ms | 144715.1 ms | 3022.5 ms | 97060.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 145648.6 ms | 142723.7 ms | 2924.9 ms | 91240.5 ms |
| Uber_zap | LLGoNoLTO | 144363.6 ms | 141870.2 ms | 2493.4 ms | 55618.9 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 141733.3 ms | 139092.2 ms | 2641.1 ms | 54926.7 ms |
| K8s_workqueue | LLGoNoLTO | 139633.0 ms | 136951.5 ms | 2681.5 ms | 54020.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 133245.3 ms | 130411.0 ms | 2834.3 ms | 82411.4 ms |
| XGo | LLGoNoLTO | 96530.3 ms | 94086.1 ms | 2444.2 ms | 37355.3 ms |
| XGo | LLGoDeadcodeDrop | 95910.9 ms | 92843.8 ms | 3067.1 ms | 37775.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 79742.2 ms | 77917.0 ms | 1825.2 ms | 49193.7 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 77449.5 ms | 75586.2 ms | 1863.3 ms | 48028.6 ms |
| Gorm_schema | LLGoNoLTO | 75703.5 ms | 74079.0 ms | 1624.6 ms | 25487.6 ms |
| Gorm_schema | LLGoDeadcodeDrop | 75491.3 ms | 73838.2 ms | 1653.1 ms | 25276.5 ms |
| Toml | LLGoFullLTONoGlobalDCE | 73365.3 ms | 71421.3 ms | 1943.9 ms | 44573.1 ms |
| Toml | LLGoDeadcodeDrop | 73112.2 ms | 71389.8 ms | 1722.4 ms | 24678.1 ms |
| Toml | LLGoNoLTO | 71381.5 ms | 69672.6 ms | 1708.9 ms | 24135.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 69218.4 ms | 67420.5 ms | 1797.9 ms | 38270.8 ms |
| IXGo | Go | 65967.7 ms | 61656.8 ms | 4310.9 ms | 18445.9 ms |
| Toml | LLGoFullLTOGlobalDCE | 64987.7 ms | 63175.8 ms | 1811.9 ms | 36700.5 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 64513.4 ms | 62798.7 ms | 1714.7 ms | 36099.7 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 50682.5 ms | 49398.3 ms | 1284.2 ms | 32825.1 ms |
| Dustin_humanize | LLGoNoLTO | 49373.7 ms | 48202.8 ms | 1170.9 ms | 17953.9 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 48480.6 ms | 47273.8 ms | 1206.9 ms | 17799.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 44171.8 ms | 42849.4 ms | 1322.4 ms | 25763.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 42186.3 ms | 40952.7 ms | 1233.6 ms | 24367.6 ms |
| Etcdctl | Go | 25300.1 ms | 23611.2 ms | 1688.9 ms | 8096.1 ms |
| XGo | Go | 14622.7 ms | 13589.8 ms | 1032.9 ms | 5079.0 ms |
| Aws_restjson | Go | 6367.3 ms | 5779.6 ms | 587.7 ms | 2730.1 ms |
| Gorm_schema | Go | 4315.4 ms | 3977.8 ms | 337.6 ms | 2485.8 ms |
| Uber_zap | Go | 4160.3 ms | 3740.9 ms | 419.3 ms | 4204.1 ms |
| K8s_workqueue | Go | 3632.8 ms | 3249.8 ms | 383.0 ms | 1446.5 ms |
| Toml | Go | 1574.2 ms | 1366.3 ms | 207.9 ms | 794.2 ms |
| Dustin_humanize | Go | 607.8 ms | 501.9 ms | 106.0 ms | 292.0 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1670142.0 ms | 1016469.6 ms | 9 |
| LLGoFullLTOGlobalDCE | 1633305.4 ms | 970229.2 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1549044.1 ms | 930257.5 ms | 9 |
| LLGoNoLTO | 1412204.4 ms | 481654.4 ms | 9 |
| LLGoDeadcodeDrop | 1369261.5 ms | 475417.7 ms | 9 |
| Go | 126548.3 ms | 43573.6 ms | 9 |

Dependency download details are in `download-timings.log`.
