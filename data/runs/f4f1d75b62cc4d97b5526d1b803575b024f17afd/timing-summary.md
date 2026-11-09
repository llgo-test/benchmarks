## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 741824.0 ms | 723249.4 ms | 18574.7 ms | 490503.0 ms |
| IXGo | LLGoFullLTOGlobalDCE | 734439.4 ms | 715212.9 ms | 19226.5 ms | 481379.7 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 710849.0 ms | 692013.4 ms | 18835.6 ms | 473329.1 ms |
| IXGo | LLGoDeadcodeDrop | 406887.1 ms | 387810.7 ms | 19076.4 ms | 130688.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 398776.2 ms | 389996.0 ms | 8780.3 ms | 294983.0 ms |
| IXGo | LLGoNoLTO | 396824.8 ms | 381022.5 ms | 15802.4 ms | 123243.1 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 389732.3 ms | 381144.3 ms | 8588.0 ms | 290535.6 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 389296.5 ms | 380540.4 ms | 8756.1 ms | 288743.3 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 292853.4 ms | 287398.5 ms | 5454.9 ms | 199518.6 ms |
| XGo | LLGoFullLTONoGlobalDCE | 292367.6 ms | 286254.6 ms | 6113.0 ms | 236725.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 267010.0 ms | 261826.4 ms | 5183.6 ms | 173015.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 261067.7 ms | 256058.3 ms | 5009.4 ms | 167983.9 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 259712.4 ms | 253684.2 ms | 6028.2 ms | 202368.5 ms |
| XGo | LLGoFullLTOGlobalDCE | 257374.8 ms | 251319.1 ms | 6055.6 ms | 200571.6 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 246125.2 ms | 241422.5 ms | 4702.6 ms | 174331.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 237758.1 ms | 233355.3 ms | 4402.8 ms | 169587.6 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 237604.3 ms | 232934.4 ms | 4669.9 ms | 170008.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 229465.5 ms | 225206.3 ms | 4259.1 ms | 156826.2 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 221736.1 ms | 217437.9 ms | 4298.3 ms | 150148.2 ms |
| Aws_restjson | LLGoNoLTO | 206300.5 ms | 202293.5 ms | 4007.0 ms | 63687.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 206208.7 ms | 201974.9 ms | 4233.8 ms | 137920.6 ms |
| Aws_restjson | LLGoDeadcodeDrop | 198665.0 ms | 194393.8 ms | 4271.2 ms | 63229.2 ms |
| Etcdctl | LLGoNoLTO | 193881.0 ms | 187111.7 ms | 6769.3 ms | 66094.1 ms |
| Etcdctl | LLGoDeadcodeDrop | 192347.2 ms | 185246.2 ms | 7101.1 ms | 66578.7 ms |
| Uber_zap | LLGoNoLTO | 166103.7 ms | 162736.6 ms | 3367.1 ms | 52872.1 ms |
| Uber_zap | LLGoDeadcodeDrop | 164416.2 ms | 160879.6 ms | 3536.6 ms | 53559.1 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 161092.1 ms | 157336.4 ms | 3755.6 ms | 53093.7 ms |
| K8s_workqueue | LLGoNoLTO | 158422.2 ms | 154948.2 ms | 3474.0 ms | 50930.1 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 126314.3 ms | 123505.1 ms | 2809.2 ms | 88241.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 121656.2 ms | 118875.9 ms | 2780.3 ms | 83953.4 ms |
| Toml | LLGoFullLTONoGlobalDCE | 114848.0 ms | 112349.0 ms | 2499.0 ms | 79138.4 ms |
| XGo | LLGoNoLTO | 110362.5 ms | 106099.1 ms | 4263.4 ms | 40349.3 ms |
| XGo | LLGoDeadcodeDrop | 107402.5 ms | 102583.3 ms | 4819.2 ms | 39493.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 106585.3 ms | 103858.6 ms | 2726.7 ms | 67148.1 ms |
| Toml | LLGoFullLTOGlobalDCE | 105403.4 ms | 102863.9 ms | 2539.5 ms | 67833.5 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 100107.9 ms | 97708.8 ms | 2399.1 ms | 63997.8 ms |
| Gorm_schema | LLGoDeadcodeDrop | 90856.1 ms | 88432.1 ms | 2423.9 ms | 31691.8 ms |
| Gorm_schema | LLGoNoLTO | 90211.2 ms | 87920.7 ms | 2290.5 ms | 31149.7 ms |
| Toml | LLGoDeadcodeDrop | 85733.7 ms | 83632.1 ms | 2101.6 ms | 29597.0 ms |
| Toml | LLGoNoLTO | 84460.9 ms | 82541.1 ms | 1919.7 ms | 28990.1 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 80563.1 ms | 78804.3 ms | 1758.8 ms | 57945.2 ms |
| IXGo | Go | 73224.3 ms | 63628.3 ms | 9596.0 ms | 19804.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 66336.2 ms | 64681.2 ms | 1655.0 ms | 42809.5 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 63965.6 ms | 62362.9 ms | 1602.7 ms | 41099.7 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 58624.6 ms | 57114.7 ms | 1509.9 ms | 21856.8 ms |
| Dustin_humanize | LLGoNoLTO | 58111.3 ms | 56705.1 ms | 1406.2 ms | 21702.7 ms |
| Etcdctl | Go | 29999.3 ms | 26493.5 ms | 3505.8 ms | 8945.2 ms |
| XGo | Go | 17236.8 ms | 15167.7 ms | 2069.2 ms | 5020.8 ms |
| Aws_restjson | Go | 7204.9 ms | 6089.0 ms | 1115.8 ms | 2932.6 ms |
| Gorm_schema | Go | 5162.2 ms | 4491.1 ms | 671.1 ms | 1960.8 ms |
| Uber_zap | Go | 4810.3 ms | 4197.0 ms | 613.2 ms | 1894.9 ms |
| K8s_workqueue | Go | 4145.1 ms | 3547.8 ms | 597.3 ms | 1442.4 ms |
| Toml | Go | 1792.7 ms | 1537.0 ms | 255.6 ms | 820.3 ms |
| Dustin_humanize | Go | 694.2 ms | 566.1 ms | 128.1 ms | 334.4 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2491257.1 ms | 1769773.5 ms | 9 |
| LLGoFullLTOGlobalDCE | 2406369.4 ms | 1663010.5 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2362354.6 ms | 1617862.6 ms | 9 |
| LLGoDeadcodeDrop | 1466024.6 ms | 489788.4 ms | 9 |
| LLGoNoLTO | 1464678.2 ms | 479018.4 ms | 9 |
| Go | 144269.8 ms | 43156.1 ms | 9 |

Dependency download details are in `download-timings.log`.
