## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| Etcdctl | LLGoFullLTONoGlobalDCE | 320230.5 ms | 310505.9 ms | 9724.6 ms | 231601.6 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 298458.2 ms | 289118.3 ms | 9339.8 ms | 221432.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 297126.0 ms | 288221.0 ms | 8905.0 ms | 222131.1 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 243256.1 ms | 237440.2 ms | 5815.9 ms | 165769.7 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 229553.3 ms | 223046.9 ms | 6506.4 ms | 180971.0 ms |
| XGo | LLGoFullLTONoGlobalDCE | 220061.2 ms | 213807.3 ms | 6253.9 ms | 178509.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 205090.0 ms | 199735.0 ms | 5355.0 ms | 143161.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 199003.9 ms | 193782.7 ms | 5221.2 ms | 123898.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 196904.5 ms | 191705.6 ms | 5198.9 ms | 126817.4 ms |
| XGo | LLGoFullLTOGlobalDCE | 191005.0 ms | 185206.4 ms | 5798.6 ms | 149193.8 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 190502.6 ms | 185562.9 ms | 4939.8 ms | 135840.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 182570.3 ms | 177818.1 ms | 4752.2 ms | 128319.5 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 172876.0 ms | 168104.6 ms | 4771.4 ms | 122650.1 ms |
| Aws_restjson | LLGoNoLTO | 164737.4 ms | 160385.2 ms | 4352.1 ms | 50562.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 163406.8 ms | 158725.5 ms | 4681.2 ms | 109746.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 158592.2 ms | 154177.9 ms | 4414.3 ms | 104575.2 ms |
| Etcdctl | LLGoDeadcodeDrop | 156814.5 ms | 149308.8 ms | 7505.7 ms | 52923.3 ms |
| Etcdctl | LLGoNoLTO | 156803.3 ms | 149800.0 ms | 7003.4 ms | 52378.1 ms |
| Aws_restjson | LLGoDeadcodeDrop | 146253.2 ms | 142125.0 ms | 4128.2 ms | 46393.8 ms |
| Uber_zap | LLGoDeadcodeDrop | 132519.8 ms | 128578.1 ms | 3941.8 ms | 43443.8 ms |
| Uber_zap | LLGoNoLTO | 121877.6 ms | 118360.9 ms | 3516.7 ms | 38522.2 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 119620.0 ms | 115843.0 ms | 3777.0 ms | 39365.7 ms |
| K8s_workqueue | LLGoNoLTO | 113999.5 ms | 110559.2 ms | 3440.3 ms | 36314.1 ms |
| Toml | LLGoFullLTONoGlobalDCE | 98596.9 ms | 95543.4 ms | 3053.5 ms | 67523.3 ms |
| XGo | LLGoDeadcodeDrop | 93013.1 ms | 87539.4 ms | 5473.7 ms | 33570.6 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 92832.1 ms | 89918.4 ms | 2913.7 ms | 65147.1 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 92349.5 ms | 89426.9 ms | 2922.6 ms | 64200.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 87178.3 ms | 84239.1 ms | 2939.3 ms | 55856.8 ms |
| Toml | LLGoFullLTOGlobalDCE | 77851.2 ms | 75218.8 ms | 2632.4 ms | 50815.5 ms |
| XGo | LLGoNoLTO | 77484.7 ms | 73433.5 ms | 4051.2 ms | 28090.1 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 75619.9 ms | 73018.0 ms | 2601.9 ms | 49607.4 ms |
| Gorm_schema | LLGoDeadcodeDrop | 69794.3 ms | 67221.0 ms | 2573.3 ms | 24515.1 ms |
| Gorm_schema | LLGoNoLTO | 68685.8 ms | 66209.2 ms | 2476.6 ms | 23621.6 ms |
| Toml | LLGoNoLTO | 63546.5 ms | 61305.3 ms | 2241.3 ms | 22003.1 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 62669.9 ms | 60743.5 ms | 1926.5 ms | 45433.1 ms |
| Toml | LLGoDeadcodeDrop | 61053.5 ms | 58839.7 ms | 2213.9 ms | 21296.6 ms |
| IXGo | Go | 60116.1 ms | 49819.8 ms | 10296.3 ms | 16575.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 57559.0 ms | 55671.9 ms | 1887.1 ms | 38687.9 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 50259.4 ms | 48487.9 ms | 1771.5 ms | 32666.2 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 44737.9 ms | 43113.3 ms | 1624.6 ms | 17137.5 ms |
| Dustin_humanize | LLGoNoLTO | 42788.9 ms | 41348.5 ms | 1440.4 ms | 16094.1 ms |
| Etcdctl | Go | 24497.2 ms | 20751.6 ms | 3745.6 ms | 7487.0 ms |
| XGo | Go | 13497.2 ms | 11415.3 ms | 2081.9 ms | 4044.2 ms |
| Aws_restjson | Go | 5351.1 ms | 4327.2 ms | 1023.8 ms | 2292.4 ms |
| Uber_zap | Go | 3978.2 ms | 3334.9 ms | 643.3 ms | 1647.3 ms |
| Gorm_schema | Go | 3857.7 ms | 3230.4 ms | 627.3 ms | 1531.4 ms |
| K8s_workqueue | Go | 3448.9 ms | 2834.3 ms | 614.6 ms | 1285.2 ms |
| Toml | Go | 1389.2 ms | 1120.5 ms | 268.7 ms | 663.7 ms |
| Dustin_humanize | Go | 642.7 ms | 469.8 ms | 173.0 ms | 336.6 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1401025.3 ms | 1012474.8 ms | 8 |
| LLGoFullLTOGlobalDCE | 1301787.7 ms | 922628.0 ms | 8 |
| LLGoFullLTOGlobalDCEPlugin | 1260739.9 ms | 879452.4 ms | 8 |
| LLGoDeadcodeDrop | 823806.4 ms | 278646.2 ms | 8 |
| LLGoNoLTO | 809923.8 ms | 267585.6 ms | 8 |
| Go | 116778.2 ms | 35863.1 ms | 9 |

Dependency download details are in `download-timings.log`.
