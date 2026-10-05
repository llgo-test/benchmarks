## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 655096.0 ms | 645260.9 ms | 9835.2 ms | 314664.7 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 594056.7 ms | 584494.2 ms | 9562.5 ms | 298124.4 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 567020.3 ms | 557050.9 ms | 9969.4 ms | 288516.2 ms |
| IXGo | LLGoDeadcodeDrop | 468283.6 ms | 457526.6 ms | 10757.0 ms | 140821.8 ms |
| IXGo | LLGoNoLTO | 464650.8 ms | 456201.1 ms | 8449.7 ms | 132646.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 274795.8 ms | 269258.7 ms | 5537.1 ms | 165774.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 264206.4 ms | 259193.6 ms | 5012.8 ms | 159464.7 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 262613.4 ms | 257996.7 ms | 4616.7 ms | 161697.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 212087.9 ms | 208693.9 ms | 3394.0 ms | 111604.2 ms |
| Aws_restjson | LLGoDeadcodeDrop | 208453.3 ms | 205454.5 ms | 2998.8 ms | 70283.6 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 207581.7 ms | 204043.2 ms | 3538.5 ms | 119201.5 ms |
| Aws_restjson | LLGoNoLTO | 203957.4 ms | 200900.2 ms | 3057.2 ms | 69398.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 200998.2 ms | 197473.0 ms | 3525.2 ms | 109095.0 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 197808.4 ms | 194682.8 ms | 3125.6 ms | 134117.8 ms |
| Etcdctl | LLGoNoLTO | 195072.0 ms | 191205.5 ms | 3866.5 ms | 64666.4 ms |
| Etcdctl | LLGoDeadcodeDrop | 194763.9 ms | 190175.1 ms | 4588.9 ms | 65630.3 ms |
| XGo | LLGoFullLTOGlobalDCE | 190004.5 ms | 187054.6 ms | 2950.0 ms | 127841.1 ms |
| XGo | LLGoFullLTONoGlobalDCE | 188051.3 ms | 184987.0 ms | 3064.3 ms | 128120.5 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 183139.3 ms | 179885.7 ms | 3253.5 ms | 108953.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 175331.4 ms | 172322.2 ms | 3009.1 ms | 100701.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 173071.1 ms | 169965.9 ms | 3105.2 ms | 99103.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 172193.8 ms | 168984.3 ms | 3209.5 ms | 102547.5 ms |
| Uber_zap | LLGoDeadcodeDrop | 171467.1 ms | 168784.0 ms | 2683.1 ms | 61857.4 ms |
| Uber_zap | LLGoNoLTO | 170477.3 ms | 167750.8 ms | 2726.4 ms | 61725.3 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 170139.4 ms | 167013.6 ms | 3125.8 ms | 101987.9 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 166727.0 ms | 164172.2 ms | 2554.8 ms | 60318.5 ms |
| K8s_workqueue | LLGoNoLTO | 163561.7 ms | 160865.9 ms | 2695.8 ms | 59297.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 160261.3 ms | 157232.3 ms | 3028.9 ms | 89269.1 ms |
| XGo | LLGoDeadcodeDrop | 118748.4 ms | 115717.7 ms | 3030.7 ms | 46211.0 ms |
| XGo | LLGoNoLTO | 117884.7 ms | 115443.9 ms | 2440.8 ms | 44365.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 84443.9 ms | 82586.3 ms | 1857.6 ms | 50802.4 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 82506.3 ms | 80565.9 ms | 1940.4 ms | 50267.3 ms |
| Gorm_schema | LLGoDeadcodeDrop | 79715.9 ms | 78128.6 ms | 1587.3 ms | 26856.1 ms |
| Gorm_schema | LLGoNoLTO | 78123.0 ms | 76595.5 ms | 1527.5 ms | 26404.6 ms |
| Toml | LLGoDeadcodeDrop | 75603.2 ms | 73992.0 ms | 1611.2 ms | 25440.7 ms |
| Toml | LLGoNoLTO | 74756.2 ms | 73163.7 ms | 1592.4 ms | 25189.8 ms |
| Toml | LLGoFullLTONoGlobalDCE | 74345.7 ms | 72611.5 ms | 1734.2 ms | 44107.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 73942.8 ms | 72138.3 ms | 1804.5 ms | 40417.4 ms |
| Toml | LLGoFullLTOGlobalDCE | 67929.5 ms | 66188.1 ms | 1741.3 ms | 36899.5 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 67878.4 ms | 66130.7 ms | 1747.6 ms | 37148.2 ms |
| IXGo | Go | 62595.1 ms | 58363.9 ms | 4231.2 ms | 17898.4 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 53381.3 ms | 52125.2 ms | 1256.0 ms | 33832.9 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 52525.0 ms | 51348.8 ms | 1176.2 ms | 19460.1 ms |
| Dustin_humanize | LLGoNoLTO | 51566.2 ms | 50480.4 ms | 1085.7 ms | 18901.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 45558.1 ms | 44293.1 ms | 1265.0 ms | 25365.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 45441.9 ms | 44275.1 ms | 1166.8 ms | 25316.6 ms |
| Etcdctl | Go | 25238.1 ms | 23610.0 ms | 1628.1 ms | 7659.2 ms |
| XGo | Go | 14300.0 ms | 13328.5 ms | 971.5 ms | 4290.1 ms |
| Aws_restjson | Go | 6029.3 ms | 5465.8 ms | 563.5 ms | 2586.5 ms |
| Gorm_schema | Go | 4270.3 ms | 3967.0 ms | 303.3 ms | 2060.0 ms |
| Uber_zap | Go | 4079.0 ms | 3743.1 ms | 335.9 ms | 1625.0 ms |
| K8s_workqueue | Go | 3617.3 ms | 3234.2 ms | 383.0 ms | 1318.8 ms |
| Toml | Go | 1556.6 ms | 1369.5 ms | 187.1 ms | 762.8 ms |
| Dustin_humanize | Go | 621.7 ms | 496.2 ms | 125.6 ms | 301.7 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTOGlobalDCE | 1864475.1 ms | 1028243.9 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1790631.1 ms | 1000011.8 ms | 9 |
| LLGoFullLTONoGlobalDCE | 1788778.6 ms | 1036683.8 ms | 9 |
| LLGoDeadcodeDrop | 1536287.4 ms | 516879.5 ms | 9 |
| LLGoNoLTO | 1520049.1 ms | 502594.7 ms | 9 |
| Go | 122307.4 ms | 38502.4 ms | 9 |

Dependency download details are in `download-timings.log`.
