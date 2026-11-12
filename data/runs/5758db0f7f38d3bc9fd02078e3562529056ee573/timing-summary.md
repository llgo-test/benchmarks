## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 672317.2 ms | 648733.5 ms | 23583.7 ms | 446851.9 ms |
| IXGo | LLGoFullLTOGlobalDCE | 663389.7 ms | 639825.0 ms | 23564.7 ms | 438888.7 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 652324.2 ms | 628975.1 ms | 23349.1 ms | 433803.1 ms |
| IXGo | LLGoDeadcodeDrop | 372262.3 ms | 349203.3 ms | 23059.1 ms | 121795.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 360567.7 ms | 349439.3 ms | 11128.4 ms | 267137.7 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 358124.0 ms | 346950.2 ms | 11173.8 ms | 266853.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 358027.0 ms | 346965.3 ms | 11061.6 ms | 264785.8 ms |
| IXGo | LLGoNoLTO | 357541.1 ms | 337602.2 ms | 19938.8 ms | 113147.5 ms |
| XGo | LLGoFullLTONoGlobalDCE | 266278.4 ms | 258557.0 ms | 7721.3 ms | 215605.4 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 266211.1 ms | 259310.8 ms | 6900.3 ms | 181580.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 240982.5 ms | 234721.5 ms | 6261.0 ms | 156464.1 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 239552.5 ms | 233204.5 ms | 6348.0 ms | 156512.2 ms |
| XGo | LLGoFullLTOGlobalDCE | 236449.0 ms | 229007.5 ms | 7441.5 ms | 184676.1 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 236090.6 ms | 228700.8 ms | 7389.7 ms | 183814.0 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 225191.7 ms | 219386.8 ms | 5805.0 ms | 159212.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 217714.9 ms | 211902.8 ms | 5812.2 ms | 154694.4 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 217523.7 ms | 211622.0 ms | 5901.8 ms | 155038.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 208764.4 ms | 203086.3 ms | 5678.1 ms | 142831.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 205215.4 ms | 199463.9 ms | 5751.6 ms | 138352.4 ms |
| Aws_restjson | LLGoNoLTO | 195346.2 ms | 190180.1 ms | 5166.1 ms | 61166.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 189646.9 ms | 184085.8 ms | 5561.1 ms | 126829.5 ms |
| Aws_restjson | LLGoDeadcodeDrop | 182438.3 ms | 176876.9 ms | 5561.4 ms | 59453.0 ms |
| Etcdctl | LLGoDeadcodeDrop | 181444.2 ms | 171767.3 ms | 9677.0 ms | 64306.1 ms |
| Etcdctl | LLGoNoLTO | 179491.8 ms | 170742.1 ms | 8749.7 ms | 62653.5 ms |
| Uber_zap | LLGoNoLTO | 153142.9 ms | 148782.5 ms | 4360.4 ms | 49494.3 ms |
| Uber_zap | LLGoDeadcodeDrop | 151956.3 ms | 147252.9 ms | 4703.4 ms | 50462.4 ms |
| K8s_workqueue | LLGoNoLTO | 146466.7 ms | 142093.3 ms | 4373.4 ms | 47410.9 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 145701.9 ms | 140994.4 ms | 4707.4 ms | 48956.2 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 114712.0 ms | 111331.3 ms | 3380.7 ms | 79663.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 114302.0 ms | 110830.9 ms | 3471.1 ms | 78502.5 ms |
| Toml | LLGoFullLTONoGlobalDCE | 107651.8 ms | 104360.3 ms | 3291.5 ms | 73780.3 ms |
| XGo | LLGoNoLTO | 101203.3 ms | 95697.5 ms | 5505.8 ms | 37788.5 ms |
| XGo | LLGoDeadcodeDrop | 100251.3 ms | 93865.0 ms | 6386.3 ms | 37638.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 95915.7 ms | 92640.7 ms | 3275.1 ms | 60261.2 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 94834.8 ms | 91711.1 ms | 3123.7 ms | 60655.8 ms |
| Toml | LLGoFullLTOGlobalDCE | 94446.2 ms | 91312.4 ms | 3133.8 ms | 60546.6 ms |
| Gorm_schema | LLGoDeadcodeDrop | 83897.8 ms | 80756.8 ms | 3141.0 ms | 30006.1 ms |
| Gorm_schema | LLGoNoLTO | 82477.9 ms | 79533.7 ms | 2944.2 ms | 29135.9 ms |
| Toml | LLGoDeadcodeDrop | 78842.1 ms | 76035.9 ms | 2806.3 ms | 27691.1 ms |
| Toml | LLGoNoLTO | 78107.3 ms | 75563.5 ms | 2543.8 ms | 27181.5 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 74826.7 ms | 72504.6 ms | 2322.1 ms | 53467.0 ms |
| IXGo | Go | 73095.9 ms | 60366.8 ms | 12729.1 ms | 20028.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 60618.4 ms | 58399.7 ms | 2218.7 ms | 39045.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 59955.3 ms | 57935.5 ms | 2019.8 ms | 38795.0 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 53785.8 ms | 51827.8 ms | 1958.1 ms | 20454.2 ms |
| Dustin_humanize | LLGoNoLTO | 52814.7 ms | 51024.7 ms | 1789.9 ms | 20052.1 ms |
| Etcdctl | Go | 28853.7 ms | 24266.2 ms | 4587.6 ms | 8769.2 ms |
| XGo | Go | 16607.8 ms | 13950.9 ms | 2656.9 ms | 4852.0 ms |
| Aws_restjson | Go | 6883.9 ms | 5521.9 ms | 1362.0 ms | 3040.2 ms |
| Gorm_schema | Go | 5083.2 ms | 4172.4 ms | 910.8 ms | 2140.3 ms |
| Uber_zap | Go | 4526.0 ms | 3778.6 ms | 747.4 ms | 1856.6 ms |
| K8s_workqueue | Go | 4043.4 ms | 3291.2 ms | 752.2 ms | 1466.0 ms |
| Toml | Go | 1746.7 ms | 1386.0 ms | 360.7 ms | 840.3 ms |
| Dustin_humanize | Go | 733.5 ms | 533.1 ms | 200.4 ms | 467.8 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2282843.7 ms | 1619004.5 ms | 9 |
| LLGoFullLTOGlobalDCE | 2192601.0 ms | 1520232.6 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2156189.2 ms | 1479412.1 ms | 9 |
| LLGoDeadcodeDrop | 1350580.1 ms | 460762.7 ms | 9 |
| LLGoNoLTO | 1346591.8 ms | 448030.7 ms | 9 |
| Go | 141574.2 ms | 43460.4 ms | 9 |

Dependency download details are in `download-timings.log`.
