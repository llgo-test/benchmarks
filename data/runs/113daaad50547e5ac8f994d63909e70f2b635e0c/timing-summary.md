## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 825470.0 ms | 799907.6 ms | 25562.4 ms | 530136.7 ms |
| IXGo | LLGoFullLTOGlobalDCE | 808885.0 ms | 782693.5 ms | 26191.5 ms | 519199.5 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 795553.2 ms | 769983.4 ms | 25569.7 ms | 511084.1 ms |
| IXGo | LLGoDeadcodeDrop | 497291.5 ms | 470803.8 ms | 26487.7 ms | 161030.8 ms |
| IXGo | LLGoNoLTO | 474292.8 ms | 452636.8 ms | 21656.0 ms | 148823.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 438249.0 ms | 426190.2 ms | 12058.8 ms | 314343.4 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 433614.3 ms | 421308.4 ms | 12305.9 ms | 314525.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 432448.8 ms | 420530.9 ms | 11917.9 ms | 310078.7 ms |
| XGo | LLGoFullLTONoGlobalDCE | 314337.0 ms | 306057.1 ms | 8279.9 ms | 246931.9 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 301239.0 ms | 294546.0 ms | 6693.0 ms | 202554.6 ms |
| XGo | LLGoFullLTOGlobalDCE | 277410.5 ms | 269276.8 ms | 8133.7 ms | 208859.7 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 277142.2 ms | 269480.4 ms | 7661.7 ms | 207946.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 277134.6 ms | 270224.8 ms | 6909.8 ms | 174916.1 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 271920.8 ms | 265429.6 ms | 6491.2 ms | 171948.0 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 255319.1 ms | 249825.9 ms | 5493.2 ms | 176411.0 ms |
| Aws_restjson | LLGoNoLTO | 254354.0 ms | 248590.1 ms | 5763.9 ms | 79686.8 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 251125.4 ms | 245274.4 ms | 5851.0 ms | 173206.3 ms |
| Aws_restjson | LLGoDeadcodeDrop | 247274.8 ms | 241117.9 ms | 6156.9 ms | 78883.7 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 245386.1 ms | 239729.3 ms | 5656.7 ms | 170216.5 ms |
| Etcdctl | LLGoNoLTO | 243982.9 ms | 234193.8 ms | 9789.1 ms | 84081.4 ms |
| Etcdctl | LLGoDeadcodeDrop | 242448.5 ms | 231656.4 ms | 10792.1 ms | 84610.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 235339.2 ms | 229949.8 ms | 5389.4 ms | 155502.2 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 230304.6 ms | 224852.6 ms | 5451.9 ms | 150221.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 215551.6 ms | 210073.2 ms | 5478.4 ms | 138726.9 ms |
| Uber_zap | LLGoDeadcodeDrop | 208873.8 ms | 203681.0 ms | 5192.8 ms | 67830.9 ms |
| Uber_zap | LLGoNoLTO | 208222.5 ms | 203329.1 ms | 4893.4 ms | 66596.0 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 201707.5 ms | 196239.6 ms | 5468.0 ms | 66230.0 ms |
| K8s_workqueue | LLGoNoLTO | 198556.3 ms | 193875.8 ms | 4680.5 ms | 63309.2 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 147352.7 ms | 143521.4 ms | 3831.3 ms | 100994.1 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 146858.9 ms | 143119.1 ms | 3739.9 ms | 99437.3 ms |
| Toml | LLGoFullLTONoGlobalDCE | 141065.6 ms | 137305.8 ms | 3759.8 ms | 95628.6 ms |
| XGo | LLGoNoLTO | 137715.5 ms | 131552.6 ms | 6162.9 ms | 50690.8 ms |
| XGo | LLGoDeadcodeDrop | 137351.6 ms | 129812.7 ms | 7538.9 ms | 49936.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 126689.0 ms | 123058.2 ms | 3630.8 ms | 78160.6 ms |
| Toml | LLGoFullLTOGlobalDCE | 125063.0 ms | 121423.9 ms | 3639.0 ms | 78448.9 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 123339.6 ms | 120000.3 ms | 3339.2 ms | 76978.9 ms |
| Gorm_schema | LLGoDeadcodeDrop | 115537.4 ms | 112098.3 ms | 3439.0 ms | 40341.8 ms |
| Gorm_schema | LLGoNoLTO | 115043.5 ms | 111740.0 ms | 3303.6 ms | 39903.9 ms |
| Toml | LLGoNoLTO | 109888.6 ms | 106837.0 ms | 3051.6 ms | 37525.0 ms |
| Toml | LLGoDeadcodeDrop | 108703.9 ms | 105510.1 ms | 3193.8 ms | 37318.9 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 97491.7 ms | 94908.0 ms | 2583.8 ms | 69105.6 ms |
| IXGo | Go | 96677.8 ms | 82034.2 ms | 14643.6 ms | 26251.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 78933.5 ms | 76582.6 ms | 2350.9 ms | 49781.5 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 78252.8 ms | 75984.2 ms | 2268.6 ms | 49433.6 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 74348.6 ms | 72180.3 ms | 2168.3 ms | 27642.5 ms |
| Dustin_humanize | LLGoNoLTO | 73582.2 ms | 71583.1 ms | 1999.2 ms | 27229.4 ms |
| Etcdctl | Go | 37962.5 ms | 32607.7 ms | 5354.8 ms | 11439.8 ms |
| XGo | Go | 21699.6 ms | 18630.8 ms | 3068.8 ms | 6288.5 ms |
| Aws_restjson | Go | 9191.2 ms | 7621.9 ms | 1569.4 ms | 3859.8 ms |
| Gorm_schema | Go | 6578.0 ms | 5615.9 ms | 962.2 ms | 2572.6 ms |
| Uber_zap | Go | 5901.0 ms | 5037.0 ms | 864.0 ms | 2384.4 ms |
| K8s_workqueue | Go | 5258.0 ms | 4371.7 ms | 886.3 ms | 1855.7 ms |
| Toml | Go | 2234.1 ms | 1815.7 ms | 418.4 ms | 1049.1 ms |
| Dustin_humanize | Go | 885.4 ms | 681.2 ms | 204.2 ms | 424.5 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2731358.6 ms | 1887451.9 ms | 9 |
| LLGoFullLTOGlobalDCE | 2633785.4 ms | 1770726.8 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2586333.1 ms | 1716599.4 ms | 9 |
| LLGoDeadcodeDrop | 1833537.6 ms | 613826.0 ms | 9 |
| LLGoNoLTO | 1815638.4 ms | 597846.0 ms | 9 |
| Go | 186387.6 ms | 56125.7 ms | 9 |

Dependency download details are in `download-timings.log`.
