## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 552786.3 ms | 539865.3 ms | 12921.0 ms | 340683.3 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 515029.5 ms | 502491.9 ms | 12537.7 ms | 311423.4 ms |
| IXGo | LLGoFullLTOGlobalDCE | 504137.0 ms | 493641.2 ms | 10495.8 ms | 304848.0 ms |
| IXGo | LLGoDeadcodeDrop | 380749.1 ms | 363636.3 ms | 17112.8 ms | 144415.9 ms |
| IXGo | LLGoNoLTO | 377618.4 ms | 367494.5 ms | 10123.9 ms | 138453.5 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 237463.0 ms | 232313.6 ms | 5149.4 ms | 165563.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 236126.0 ms | 231054.6 ms | 5071.4 ms | 163941.6 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 233619.0 ms | 228822.4 ms | 4796.6 ms | 164798.9 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 183620.3 ms | 180432.7 ms | 3187.6 ms | 121500.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 174505.8 ms | 171316.1 ms | 3189.7 ms | 111019.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 172131.0 ms | 169041.8 ms | 3089.2 ms | 106399.6 ms |
| Aws_restjson | LLGoDeadcodeDrop | 170261.4 ms | 167221.8 ms | 3039.6 ms | 71393.1 ms |
| XGo | LLGoFullLTOGlobalDCE | 169423.6 ms | 166094.1 ms | 3329.4 ms | 130631.9 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 167779.2 ms | 164382.0 ms | 3397.2 ms | 128556.2 ms |
| Aws_restjson | LLGoNoLTO | 167410.9 ms | 164666.5 ms | 2744.4 ms | 69958.4 ms |
| XGo | LLGoFullLTONoGlobalDCE | 166448.2 ms | 163062.1 ms | 3386.1 ms | 127644.4 ms |
| Etcdctl | LLGoDeadcodeDrop | 155833.1 ms | 150700.5 ms | 5132.6 ms | 64417.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 154685.4 ms | 151790.9 ms | 2894.5 ms | 111294.3 ms |
| Etcdctl | LLGoNoLTO | 154285.1 ms | 150073.0 ms | 4212.1 ms | 62698.2 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 152610.7 ms | 149717.7 ms | 2893.0 ms | 107686.7 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 147195.3 ms | 144276.4 ms | 2919.0 ms | 103956.9 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 146544.0 ms | 143800.4 ms | 2743.6 ms | 102411.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 140290.6 ms | 137394.3 ms | 2896.3 ms | 95077.6 ms |
| Uber_zap | LLGoDeadcodeDrop | 136142.4 ms | 133802.7 ms | 2339.7 ms | 60315.6 ms |
| Uber_zap | LLGoNoLTO | 133498.6 ms | 131127.4 ms | 2371.2 ms | 59403.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 128843.8 ms | 126116.5 ms | 2727.4 ms | 85743.2 ms |
| K8s_workqueue | LLGoNoLTO | 128747.2 ms | 126342.0 ms | 2405.2 ms | 57417.0 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 128564.2 ms | 126161.8 ms | 2402.4 ms | 57446.9 ms |
| XGo | LLGoDeadcodeDrop | 90863.4 ms | 87564.9 ms | 3298.4 ms | 40251.2 ms |
| XGo | LLGoNoLTO | 88150.5 ms | 85601.9 ms | 2548.6 ms | 38698.0 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 76510.4 ms | 74603.9 ms | 1906.6 ms | 51870.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 76103.1 ms | 74320.6 ms | 1782.5 ms | 50812.4 ms |
| Gorm_schema | LLGoDeadcodeDrop | 72384.8 ms | 70803.7 ms | 1581.1 ms | 30232.3 ms |
| Gorm_schema | LLGoNoLTO | 71141.9 ms | 69535.7 ms | 1606.1 ms | 29697.7 ms |
| Toml | LLGoFullLTONoGlobalDCE | 69493.4 ms | 67851.7 ms | 1641.7 ms | 46481.8 ms |
| Toml | LLGoFullLTOGlobalDCE | 67008.6 ms | 65336.5 ms | 1672.0 ms | 43309.7 ms |
| Toml | LLGoDeadcodeDrop | 66792.1 ms | 65364.2 ms | 1427.9 ms | 27759.0 ms |
| Toml | LLGoNoLTO | 65590.6 ms | 64156.9 ms | 1433.7 ms | 27141.7 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 65275.8 ms | 63554.1 ms | 1721.7 ms | 40112.1 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 61365.1 ms | 59802.2 ms | 1562.8 ms | 38339.0 ms |
| IXGo | Go | 60542.6 ms | 55757.8 ms | 4784.8 ms | 22121.2 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 48761.9 ms | 47517.7 ms | 1244.3 ms | 34235.0 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 47376.2 ms | 46282.5 ms | 1093.6 ms | 21187.8 ms |
| Dustin_humanize | LLGoNoLTO | 45609.9 ms | 44626.5 ms | 983.4 ms | 20258.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 40773.4 ms | 39630.4 ms | 1143.0 ms | 25938.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 40763.6 ms | 39598.1 ms | 1165.5 ms | 26010.1 ms |
| Etcdctl | Go | 25216.6 ms | 23131.9 ms | 2084.8 ms | 10281.4 ms |
| XGo | Go | 14415.5 ms | 13250.3 ms | 1165.2 ms | 5778.7 ms |
| Aws_restjson | Go | 6323.2 ms | 5642.8 ms | 680.4 ms | 3635.7 ms |
| Gorm_schema | Go | 4300.8 ms | 3940.0 ms | 360.8 ms | 2032.4 ms |
| Uber_zap | Go | 4018.5 ms | 3688.4 ms | 330.1 ms | 1951.2 ms |
| K8s_workqueue | Go | 3675.2 ms | 3223.3 ms | 451.9 ms | 2531.2 ms |
| Toml | Go | 1497.6 ms | 1335.2 ms | 162.4 ms | 818.7 ms |
| Dustin_humanize | Go | 623.5 ms | 503.9 ms | 119.5 ms | 359.6 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1593288.8 ms | 1069598.3 ms | 9 |
| LLGoFullLTOGlobalDCE | 1569306.8 ms | 1044207.3 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1566698.5 ms | 1026484.8 ms | 9 |
| LLGoDeadcodeDrop | 1248966.7 ms | 517419.3 ms | 9 |
| LLGoNoLTO | 1232052.9 ms | 503726.3 ms | 9 |
| Go | 120613.6 ms | 49510.3 ms | 9 |

Dependency download details are in `download-timings.log`.
