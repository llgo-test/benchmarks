## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 676219.5 ms | 659613.0 ms | 16606.5 ms | 447108.6 ms |
| IXGo | LLGoFullLTOGlobalDCE | 648737.2 ms | 632903.4 ms | 15833.8 ms | 433141.6 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 632520.0 ms | 616867.0 ms | 15653.0 ms | 424701.2 ms |
| IXGo | LLGoDeadcodeDrop | 365251.8 ms | 349166.0 ms | 16085.8 ms | 118364.6 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 353763.0 ms | 346088.5 ms | 7674.5 ms | 265112.4 ms |
| IXGo | LLGoNoLTO | 351994.7 ms | 338077.2 ms | 13917.5 ms | 110537.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 345270.6 ms | 337655.5 ms | 7615.1 ms | 258347.5 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 335462.8 ms | 328231.9 ms | 7230.9 ms | 250801.7 ms |
| XGo | LLGoFullLTONoGlobalDCE | 251717.3 ms | 246697.4 ms | 5019.9 ms | 203535.4 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 248774.1 ms | 244301.1 ms | 4473.0 ms | 170978.3 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 221862.4 ms | 217512.5 ms | 4349.9 ms | 144246.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 220588.3 ms | 216341.8 ms | 4246.5 ms | 142367.7 ms |
| XGo | LLGoFullLTOGlobalDCE | 220324.9 ms | 215423.6 ms | 4901.2 ms | 172330.2 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 218406.4 ms | 213494.5 ms | 4911.9 ms | 170305.4 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 200278.7 ms | 196482.2 ms | 3796.5 ms | 143756.8 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 189435.3 ms | 185826.3 ms | 3609.1 ms | 137178.3 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 188706.9 ms | 185082.3 ms | 3624.6 ms | 136545.3 ms |
| Aws_restjson | LLGoNoLTO | 182817.8 ms | 178993.5 ms | 3824.4 ms | 57400.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 180527.2 ms | 176850.8 ms | 3676.5 ms | 122403.1 ms |
| Aws_restjson | LLGoDeadcodeDrop | 177798.1 ms | 174038.7 ms | 3759.3 ms | 57188.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 177731.5 ms | 174305.6 ms | 3425.9 ms | 122325.5 ms |
| Etcdctl | LLGoDeadcodeDrop | 175922.8 ms | 169497.4 ms | 6425.4 ms | 61565.9 ms |
| Etcdctl | LLGoNoLTO | 170305.4 ms | 164552.9 ms | 5752.5 ms | 58852.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 158707.3 ms | 155416.7 ms | 3290.5 ms | 107384.9 ms |
| Uber_zap | LLGoNoLTO | 146336.8 ms | 143250.9 ms | 3085.9 ms | 46951.3 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 144074.7 ms | 140659.8 ms | 3414.9 ms | 48284.6 ms |
| Uber_zap | LLGoDeadcodeDrop | 143552.9 ms | 140246.8 ms | 3306.1 ms | 47633.1 ms |
| K8s_workqueue | LLGoNoLTO | 142188.1 ms | 139102.1 ms | 3086.0 ms | 45778.9 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 119379.2 ms | 116800.7 ms | 2578.5 ms | 85261.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 111313.3 ms | 108846.3 ms | 2467.0 ms | 78567.4 ms |
| Toml | LLGoFullLTONoGlobalDCE | 103079.5 ms | 100788.2 ms | 2291.3 ms | 72879.8 ms |
| XGo | LLGoNoLTO | 98097.9 ms | 94355.4 ms | 3742.6 ms | 36199.5 ms |
| XGo | LLGoDeadcodeDrop | 97646.7 ms | 93452.3 ms | 4194.4 ms | 35930.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 96885.1 ms | 94334.1 ms | 2551.1 ms | 61905.1 ms |
| Toml | LLGoFullLTOGlobalDCE | 92956.8 ms | 90703.5 ms | 2253.2 ms | 61330.5 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 92955.0 ms | 90702.0 ms | 2253.0 ms | 61530.2 ms |
| Gorm_schema | LLGoNoLTO | 82210.0 ms | 80074.7 ms | 2135.3 ms | 28659.2 ms |
| Gorm_schema | LLGoDeadcodeDrop | 80857.3 ms | 78695.6 ms | 2161.7 ms | 28634.5 ms |
| Toml | LLGoDeadcodeDrop | 76036.4 ms | 74086.7 ms | 1949.7 ms | 26634.4 ms |
| Toml | LLGoNoLTO | 75788.8 ms | 74076.6 ms | 1712.2 ms | 26383.7 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 72566.2 ms | 71030.4 ms | 1535.9 ms | 53175.5 ms |
| IXGo | Go | 62633.5 ms | 54626.0 ms | 8007.5 ms | 17078.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 60898.8 ms | 59418.8 ms | 1479.9 ms | 40316.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 56051.0 ms | 54629.8 ms | 1421.2 ms | 36819.0 ms |
| Dustin_humanize | LLGoNoLTO | 53055.9 ms | 51635.7 ms | 1420.2 ms | 20107.6 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 52799.4 ms | 51392.8 ms | 1406.6 ms | 20105.0 ms |
| Etcdctl | Go | 24736.2 ms | 21897.5 ms | 2838.7 ms | 7637.3 ms |
| XGo | Go | 14666.0 ms | 12948.0 ms | 1718.0 ms | 4361.0 ms |
| Aws_restjson | Go | 5979.5 ms | 5183.4 ms | 796.1 ms | 2587.5 ms |
| Gorm_schema | Go | 4340.6 ms | 3825.5 ms | 515.1 ms | 1700.3 ms |
| Uber_zap | Go | 4117.5 ms | 3603.2 ms | 514.3 ms | 1631.6 ms |
| K8s_workqueue | Go | 3592.8 ms | 3061.4 ms | 531.5 ms | 1537.5 ms |
| Toml | Go | 1551.2 ms | 1333.1 ms | 218.1 ms | 727.1 ms |
| Dustin_humanize | Go | 624.4 ms | 505.3 ms | 119.1 ms | 303.5 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2170784.9 ms | 1555946.2 ms | 9 |
| LLGoFullLTOGlobalDCE | 2057448.8 ms | 1438359.2 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2046884.6 ms | 1410050.4 ms | 9 |
| LLGoDeadcodeDrop | 1313940.0 ms | 444340.8 ms | 9 |
| LLGoNoLTO | 1302795.3 ms | 430870.5 ms | 9 |
| Go | 122241.6 ms | 37563.8 ms | 9 |

Dependency download details are in `download-timings.log`.
