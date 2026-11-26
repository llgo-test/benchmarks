## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 673709.0 ms | 656739.6 ms | 16969.4 ms | 451030.7 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 663701.2 ms | 647621.1 ms | 16080.1 ms | 447559.4 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 631784.4 ms | 615881.5 ms | 15903.0 ms | 423296.7 ms |
| IXGo | LLGoNoLTO | 376251.8 ms | 361744.4 ms | 14507.4 ms | 117445.3 ms |
| IXGo | LLGoDeadcodeDrop | 371736.9 ms | 355287.5 ms | 16449.4 ms | 120348.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 345675.1 ms | 338256.1 ms | 7419.0 ms | 256908.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 343825.1 ms | 336507.3 ms | 7317.8 ms | 256327.1 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 333680.4 ms | 326650.3 ms | 7030.2 ms | 251636.7 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 252505.7 ms | 247884.9 ms | 4620.7 ms | 173436.7 ms |
| XGo | LLGoFullLTONoGlobalDCE | 251344.0 ms | 246355.4 ms | 4988.6 ms | 204457.2 ms |
| XGo | LLGoFullLTOGlobalDCE | 227710.4 ms | 222774.3 ms | 4936.1 ms | 177775.0 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 224591.7 ms | 219775.3 ms | 4816.4 ms | 175647.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 219708.3 ms | 215517.1 ms | 4191.2 ms | 141606.1 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 213091.2 ms | 208905.3 ms | 4185.9 ms | 138933.2 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 196922.2 ms | 193244.4 ms | 3677.8 ms | 141829.8 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 191448.7 ms | 187912.4 ms | 3536.3 ms | 139036.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 184463.7 ms | 180835.2 ms | 3628.4 ms | 133390.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 183890.9 ms | 180229.4 ms | 3661.5 ms | 124766.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 181015.6 ms | 177527.9 ms | 3487.7 ms | 124983.7 ms |
| Aws_restjson | LLGoDeadcodeDrop | 180900.2 ms | 177070.9 ms | 3829.3 ms | 58192.7 ms |
| Aws_restjson | LLGoNoLTO | 179225.6 ms | 175781.5 ms | 3444.1 ms | 56109.8 ms |
| Etcdctl | LLGoDeadcodeDrop | 177855.3 ms | 171371.8 ms | 6483.5 ms | 61775.2 ms |
| Etcdctl | LLGoNoLTO | 174770.2 ms | 168955.8 ms | 5814.4 ms | 60401.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 160863.6 ms | 157727.6 ms | 3136.0 ms | 108033.7 ms |
| Uber_zap | LLGoNoLTO | 153046.3 ms | 149992.2 ms | 3054.2 ms | 49226.1 ms |
| Uber_zap | LLGoDeadcodeDrop | 150540.1 ms | 147198.2 ms | 3341.9 ms | 49871.1 ms |
| K8s_workqueue | LLGoNoLTO | 148758.4 ms | 145337.7 ms | 3420.7 ms | 48281.2 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 138581.0 ms | 135479.2 ms | 3101.8 ms | 46062.3 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 119589.0 ms | 117036.8 ms | 2552.3 ms | 85561.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 117988.3 ms | 115381.7 ms | 2606.6 ms | 83139.0 ms |
| Toml | LLGoFullLTONoGlobalDCE | 107903.7 ms | 105516.8 ms | 2387.0 ms | 76312.9 ms |
| XGo | LLGoDeadcodeDrop | 98366.3 ms | 94043.8 ms | 4322.4 ms | 36392.5 ms |
| XGo | LLGoNoLTO | 96923.2 ms | 93263.6 ms | 3659.7 ms | 35881.5 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 93449.1 ms | 91197.6 ms | 2251.5 ms | 61627.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 93318.2 ms | 91008.6 ms | 2309.6 ms | 59691.4 ms |
| Toml | LLGoFullLTOGlobalDCE | 93174.9 ms | 90869.2 ms | 2305.7 ms | 61764.0 ms |
| Gorm_schema | LLGoNoLTO | 85034.8 ms | 82856.2 ms | 2178.6 ms | 29548.9 ms |
| Gorm_schema | LLGoDeadcodeDrop | 82920.6 ms | 80743.4 ms | 2177.2 ms | 29345.2 ms |
| Toml | LLGoNoLTO | 76293.3 ms | 74487.8 ms | 1805.5 ms | 26430.2 ms |
| Toml | LLGoDeadcodeDrop | 76030.2 ms | 74135.3 ms | 1894.9 ms | 26832.7 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 74465.2 ms | 72812.3 ms | 1652.9 ms | 54886.6 ms |
| IXGo | Go | 63553.7 ms | 55473.5 ms | 8080.2 ms | 17525.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 61580.4 ms | 60046.4 ms | 1534.0 ms | 40521.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 61453.0 ms | 59976.6 ms | 1476.4 ms | 40406.3 ms |
| Dustin_humanize | LLGoNoLTO | 54706.9 ms | 53292.7 ms | 1414.2 ms | 20710.7 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 53940.5 ms | 52523.5 ms | 1417.0 ms | 20565.5 ms |
| Etcdctl | Go | 24733.8 ms | 21940.8 ms | 2793.0 ms | 7404.2 ms |
| XGo | Go | 14703.3 ms | 12984.4 ms | 1718.8 ms | 4330.5 ms |
| Aws_restjson | Go | 6156.6 ms | 5353.7 ms | 803.0 ms | 2511.1 ms |
| Gorm_schema | Go | 4416.1 ms | 3882.2 ms | 533.9 ms | 1729.2 ms |
| Uber_zap | Go | 3989.0 ms | 3544.4 ms | 444.6 ms | 1566.4 ms |
| K8s_workqueue | Go | 3536.6 ms | 3028.3 ms | 508.3 ms | 1389.0 ms |
| Toml | Go | 1530.8 ms | 1334.7 ms | 196.1 ms | 715.9 ms |
| Dustin_humanize | Go | 609.8 ms | 491.3 ms | 118.4 ms | 302.3 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2159643.5 ms | 1550455.2 ms | 9 |
| LLGoFullLTOGlobalDCE | 2098281.4 ms | 1468331.1 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2044928.5 ms | 1415781.8 ms | 9 |
| LLGoNoLTO | 1345010.7 ms | 444035.1 ms | 9 |
| LLGoDeadcodeDrop | 1330871.1 ms | 449385.5 ms | 9 |
| Go | 123229.6 ms | 37473.6 ms | 9 |

Dependency download details are in `download-timings.log`.
