## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 710195.1 ms | 691444.1 ms | 18750.9 ms | 470234.1 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 677987.3 ms | 660469.0 ms | 17518.3 ms | 450514.3 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 639630.1 ms | 622675.7 ms | 16954.5 ms | 432309.5 ms |
| IXGo | LLGoNoLTO | 380609.4 ms | 364665.0 ms | 15944.4 ms | 120318.2 ms |
| IXGo | LLGoDeadcodeDrop | 370566.0 ms | 353519.8 ms | 17046.2 ms | 121143.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 367831.3 ms | 359155.8 ms | 8675.5 ms | 273158.5 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 351566.9 ms | 343274.3 ms | 8292.6 ms | 260871.1 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 332208.3 ms | 324273.9 ms | 7934.3 ms | 249578.9 ms |
| XGo | LLGoFullLTONoGlobalDCE | 250773.5 ms | 245186.7 ms | 5586.8 ms | 203567.5 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 233900.9 ms | 228252.8 ms | 5648.1 ms | 182182.2 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 233887.2 ms | 229500.6 ms | 4386.7 ms | 161382.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 228724.9 ms | 224051.9 ms | 4673.1 ms | 148125.7 ms |
| XGo | LLGoFullLTOGlobalDCE | 218630.7 ms | 213085.6 ms | 5545.0 ms | 169948.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 216578.2 ms | 212158.5 ms | 4419.6 ms | 140678.6 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 212902.6 ms | 208596.5 ms | 4306.1 ms | 154357.5 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 212350.5 ms | 208085.9 ms | 4264.6 ms | 152106.2 ms |
| Aws_restjson | LLGoDeadcodeDrop | 194538.5 ms | 190082.0 ms | 4456.4 ms | 63417.1 ms |
| Etcdctl | LLGoDeadcodeDrop | 187044.7 ms | 179740.8 ms | 7303.9 ms | 66309.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 179597.8 ms | 175923.4 ms | 3674.4 ms | 130034.7 ms |
| Aws_restjson | LLGoNoLTO | 178564.5 ms | 174841.8 ms | 3722.7 ms | 56234.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 177861.3 ms | 174072.0 ms | 3789.4 ms | 123429.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 173730.6 ms | 170026.1 ms | 3704.4 ms | 118173.5 ms |
| Etcdctl | LLGoNoLTO | 171192.8 ms | 164953.6 ms | 6239.1 ms | 59644.9 ms |
| Uber_zap | LLGoNoLTO | 160711.1 ms | 157346.1 ms | 3365.0 ms | 52103.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 160441.1 ms | 156803.5 ms | 3637.6 ms | 107512.2 ms |
| Uber_zap | LLGoDeadcodeDrop | 142198.8 ms | 138974.1 ms | 3224.7 ms | 47591.9 ms |
| K8s_workqueue | LLGoNoLTO | 140105.0 ms | 136882.7 ms | 3222.3 ms | 45406.7 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 135853.9 ms | 132616.3 ms | 3237.7 ms | 45643.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 119117.8 ms | 116400.8 ms | 2717.0 ms | 83946.9 ms |
| Toml | LLGoFullLTONoGlobalDCE | 112951.2 ms | 110258.6 ms | 2692.6 ms | 80025.2 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 112751.0 ms | 110042.8 ms | 2708.3 ms | 80268.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 101996.2 ms | 99270.5 ms | 2725.7 ms | 65858.4 ms |
| XGo | LLGoNoLTO | 98540.9 ms | 94518.5 ms | 4022.4 ms | 37002.6 ms |
| XGo | LLGoDeadcodeDrop | 95429.6 ms | 90847.7 ms | 4581.9 ms | 35821.7 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 89870.6 ms | 87639.4 ms | 2231.2 ms | 59289.2 ms |
| Toml | LLGoFullLTOGlobalDCE | 89254.5 ms | 87006.6 ms | 2247.9 ms | 58742.5 ms |
| Gorm_schema | LLGoNoLTO | 85706.3 ms | 83419.1 ms | 2287.2 ms | 30149.5 ms |
| Gorm_schema | LLGoDeadcodeDrop | 78265.5 ms | 75759.3 ms | 2506.3 ms | 28297.3 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 74066.5 ms | 72293.4 ms | 1773.1 ms | 54227.7 ms |
| Toml | LLGoNoLTO | 73483.1 ms | 71651.2 ms | 1831.9 ms | 25872.0 ms |
| Toml | LLGoDeadcodeDrop | 73210.7 ms | 71140.4 ms | 2070.3 ms | 26122.7 ms |
| IXGo | Go | 63707.4 ms | 54518.1 ms | 9189.3 ms | 18318.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 58855.8 ms | 57287.6 ms | 1568.2 ms | 38955.5 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 56599.7 ms | 55057.3 ms | 1542.4 ms | 37236.3 ms |
| Dustin_humanize | LLGoNoLTO | 51149.0 ms | 49826.4 ms | 1322.6 ms | 19659.1 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 50563.9 ms | 49119.4 ms | 1444.5 ms | 19545.5 ms |
| Etcdctl | Go | 25418.8 ms | 22153.9 ms | 3264.9 ms | 7741.9 ms |
| XGo | Go | 14804.7 ms | 12882.0 ms | 1922.7 ms | 4416.3 ms |
| Aws_restjson | Go | 6806.4 ms | 5765.5 ms | 1040.9 ms | 2828.3 ms |
| Gorm_schema | Go | 4481.1 ms | 3853.0 ms | 628.1 ms | 1849.5 ms |
| Uber_zap | Go | 4015.5 ms | 3482.1 ms | 533.4 ms | 1635.8 ms |
| K8s_workqueue | Go | 3515.6 ms | 2993.8 ms | 521.8 ms | 1264.6 ms |
| Toml | Go | 1544.9 ms | 1299.3 ms | 245.6 ms | 734.5 ms |
| Dustin_humanize | Go | 712.3 ms | 571.2 ms | 141.1 ms | 362.9 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2181520.9 ms | 1567823.3 ms | 9 |
| LLGoFullLTOGlobalDCE | 2147813.0 ms | 1494856.0 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2064927.6 ms | 1424034.9 ms | 9 |
| LLGoNoLTO | 1340062.1 ms | 446391.8 ms | 9 |
| LLGoDeadcodeDrop | 1327671.6 ms | 453892.2 ms | 9 |
| Go | 125006.8 ms | 39152.6 ms | 9 |

Dependency download details are in `download-timings.log`.
