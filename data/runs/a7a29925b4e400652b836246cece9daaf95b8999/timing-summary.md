## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 830114.6 ms | 800597.1 ms | 29517.5 ms | 546077.3 ms |
| IXGo | LLGoFullLTOGlobalDCE | 809479.9 ms | 779404.3 ms | 30075.6 ms | 533750.9 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 793115.3 ms | 763430.3 ms | 29685.0 ms | 526179.9 ms |
| IXGo | LLGoDeadcodeDrop | 463577.4 ms | 434669.6 ms | 28907.7 ms | 150715.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 445234.7 ms | 431408.2 ms | 13826.5 ms | 328768.2 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 442904.6 ms | 429012.1 ms | 13892.4 ms | 329135.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 442775.7 ms | 429007.2 ms | 13768.5 ms | 326928.6 ms |
| IXGo | LLGoNoLTO | 440477.0 ms | 415817.5 ms | 24659.5 ms | 138732.7 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 331534.8 ms | 323169.8 ms | 8365.0 ms | 224556.3 ms |
| XGo | LLGoFullLTONoGlobalDCE | 327657.8 ms | 318209.3 ms | 9448.5 ms | 264789.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 297265.4 ms | 289124.4 ms | 8141.0 ms | 193311.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 296378.0 ms | 288255.3 ms | 8122.7 ms | 192901.3 ms |
| XGo | LLGoFullLTOGlobalDCE | 291217.2 ms | 282086.3 ms | 9130.8 ms | 227046.3 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 291153.3 ms | 281882.4 ms | 9270.9 ms | 226700.7 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 279001.6 ms | 271870.1 ms | 7131.5 ms | 197019.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 270528.2 ms | 263332.3 ms | 7195.9 ms | 191605.8 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 270051.1 ms | 262839.0 ms | 7212.1 ms | 191811.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 259145.6 ms | 252065.4 ms | 7080.2 ms | 176221.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 254652.3 ms | 247592.6 ms | 7059.7 ms | 171200.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 235155.3 ms | 228454.5 ms | 6700.8 ms | 156479.2 ms |
| Aws_restjson | LLGoNoLTO | 234576.8 ms | 228380.4 ms | 6196.5 ms | 74112.3 ms |
| Aws_restjson | LLGoDeadcodeDrop | 228443.0 ms | 221715.6 ms | 6727.4 ms | 73810.0 ms |
| Etcdctl | LLGoDeadcodeDrop | 227062.3 ms | 215413.6 ms | 11648.6 ms | 79422.7 ms |
| Etcdctl | LLGoNoLTO | 224091.9 ms | 213316.1 ms | 10775.8 ms | 78002.4 ms |
| Uber_zap | LLGoNoLTO | 191923.1 ms | 186518.9 ms | 5404.3 ms | 61917.4 ms |
| Uber_zap | LLGoDeadcodeDrop | 191390.8 ms | 185836.8 ms | 5554.0 ms | 62928.8 ms |
| K8s_workqueue | LLGoNoLTO | 183546.6 ms | 178045.7 ms | 5500.9 ms | 59409.2 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 182730.0 ms | 176835.7 ms | 5894.4 ms | 60824.3 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 143512.0 ms | 139264.4 ms | 4247.7 ms | 99671.7 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 141863.9 ms | 137589.9 ms | 4273.9 ms | 97430.8 ms |
| Toml | LLGoFullLTONoGlobalDCE | 134098.2 ms | 130009.0 ms | 4089.2 ms | 91947.2 ms |
| XGo | LLGoNoLTO | 126564.7 ms | 119536.4 ms | 7028.3 ms | 47094.0 ms |
| XGo | LLGoDeadcodeDrop | 125216.3 ms | 117508.4 ms | 7707.9 ms | 46276.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 119627.9 ms | 115546.4 ms | 4081.5 ms | 75016.0 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 118460.2 ms | 114472.2 ms | 3988.0 ms | 75551.9 ms |
| Toml | LLGoFullLTOGlobalDCE | 117952.4 ms | 114045.2 ms | 3907.2 ms | 75551.5 ms |
| Gorm_schema | LLGoDeadcodeDrop | 105864.4 ms | 101853.8 ms | 4010.6 ms | 37474.6 ms |
| Gorm_schema | LLGoNoLTO | 103406.4 ms | 99886.7 ms | 3519.7 ms | 36176.7 ms |
| Toml | LLGoDeadcodeDrop | 99717.8 ms | 96292.7 ms | 3425.1 ms | 34803.1 ms |
| Toml | LLGoNoLTO | 98748.3 ms | 95439.7 ms | 3308.6 ms | 34306.0 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 93170.3 ms | 90422.6 ms | 2747.7 ms | 66969.1 ms |
| IXGo | Go | 91119.6 ms | 75198.6 ms | 15921.1 ms | 24881.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 75325.9 ms | 72773.1 ms | 2552.8 ms | 48180.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 75092.3 ms | 72620.6 ms | 2471.8 ms | 48074.0 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 67901.5 ms | 65537.6 ms | 2364.0 ms | 25772.8 ms |
| Dustin_humanize | LLGoNoLTO | 66578.9 ms | 64455.0 ms | 2123.9 ms | 25079.9 ms |
| Etcdctl | Go | 36026.5 ms | 30350.4 ms | 5676.1 ms | 10859.5 ms |
| XGo | Go | 20741.5 ms | 17435.8 ms | 3305.7 ms | 6060.7 ms |
| Aws_restjson | Go | 8725.4 ms | 7076.4 ms | 1649.0 ms | 3598.8 ms |
| Gorm_schema | Go | 6264.6 ms | 5205.3 ms | 1059.2 ms | 2511.6 ms |
| Uber_zap | Go | 5750.5 ms | 4770.5 ms | 980.0 ms | 2332.4 ms |
| K8s_workqueue | Go | 5157.3 ms | 4163.9 ms | 993.4 ms | 2089.9 ms |
| Toml | Go | 2210.4 ms | 1755.9 ms | 454.5 ms | 1044.3 ms |
| Dustin_humanize | Go | 886.5 ms | 649.8 ms | 236.7 ms | 433.2 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2815045.7 ms | 1992079.7 ms | 9 |
| LLGoFullLTOGlobalDCE | 2705320.5 ms | 1869919.9 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2666102.2 ms | 1820875.9 ms | 9 |
| LLGoDeadcodeDrop | 1691903.5 ms | 572027.7 ms | 9 |
| LLGoNoLTO | 1669913.9 ms | 554830.6 ms | 9 |
| Go | 176882.3 ms | 53811.5 ms | 9 |

Dependency download details are in `download-timings.log`.
