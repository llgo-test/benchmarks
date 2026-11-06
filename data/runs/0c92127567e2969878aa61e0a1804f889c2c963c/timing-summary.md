## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| Etcdctl | LLGoFullLTOGlobalDCE | 373521.9 ms | 361969.5 ms | 11552.4 ms | 275388.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 367515.8 ms | 355725.8 ms | 11790.1 ms | 273335.8 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 365766.5 ms | 354572.9 ms | 11193.6 ms | 264781.1 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 300263.4 ms | 293032.2 ms | 7231.2 ms | 206671.3 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 262916.3 ms | 256532.5 ms | 6383.8 ms | 168695.3 ms |
| XGo | LLGoFullLTONoGlobalDCE | 260443.3 ms | 252756.2 ms | 7687.1 ms | 209476.1 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 241577.6 ms | 234921.7 ms | 6655.9 ms | 154720.7 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 234655.9 ms | 227054.6 ms | 7601.3 ms | 182339.2 ms |
| XGo | LLGoFullLTOGlobalDCE | 230205.0 ms | 222758.6 ms | 7446.3 ms | 179569.1 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 224484.6 ms | 218423.4 ms | 6061.2 ms | 158177.1 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 215177.9 ms | 209092.0 ms | 6085.9 ms | 150134.8 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 214937.7 ms | 209027.3 ms | 5910.4 ms | 150264.4 ms |
| Etcdctl | LLGoNoLTO | 200089.8 ms | 191227.7 ms | 8862.1 ms | 66257.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 199808.4 ms | 194129.9 ms | 5678.5 ms | 134181.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 199481.0 ms | 193752.3 ms | 5728.7 ms | 133895.6 ms |
| Aws_restjson | LLGoNoLTO | 195852.7 ms | 190546.1 ms | 5306.6 ms | 60150.1 ms |
| Etcdctl | LLGoDeadcodeDrop | 192692.3 ms | 183221.0 ms | 9471.3 ms | 64823.8 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 186297.2 ms | 180801.3 ms | 5495.9 ms | 123284.4 ms |
| Aws_restjson | LLGoDeadcodeDrop | 183511.5 ms | 178111.4 ms | 5400.1 ms | 57801.1 ms |
| Uber_zap | LLGoNoLTO | 157418.3 ms | 152742.4 ms | 4675.9 ms | 50363.7 ms |
| Uber_zap | LLGoDeadcodeDrop | 150522.7 ms | 145985.3 ms | 4537.4 ms | 49260.3 ms |
| K8s_workqueue | LLGoNoLTO | 147321.1 ms | 142954.0 ms | 4367.1 ms | 46408.7 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 144519.5 ms | 139780.1 ms | 4739.3 ms | 48030.6 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 122612.8 ms | 118947.2 ms | 3665.6 ms | 85847.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 119971.5 ms | 116295.1 ms | 3676.4 ms | 83382.7 ms |
| Toml | LLGoFullLTONoGlobalDCE | 114326.0 ms | 110788.5 ms | 3537.5 ms | 80319.9 ms |
| XGo | LLGoNoLTO | 102992.2 ms | 97348.3 ms | 5643.9 ms | 37800.7 ms |
| XGo | LLGoDeadcodeDrop | 96902.9 ms | 90532.2 ms | 6370.7 ms | 35072.5 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 96124.0 ms | 92862.0 ms | 3262.0 ms | 62322.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 94917.9 ms | 91484.4 ms | 3433.5 ms | 61213.6 ms |
| Toml | LLGoFullLTOGlobalDCE | 93722.6 ms | 90404.2 ms | 3318.5 ms | 60700.2 ms |
| Gorm_schema | LLGoDeadcodeDrop | 83839.2 ms | 80674.4 ms | 3164.8 ms | 29392.2 ms |
| Gorm_schema | LLGoNoLTO | 81381.7 ms | 78361.3 ms | 3020.4 ms | 28084.8 ms |
| Toml | LLGoDeadcodeDrop | 79640.8 ms | 76890.4 ms | 2750.4 ms | 27887.5 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 78999.3 ms | 76498.8 ms | 2500.4 ms | 57296.2 ms |
| Toml | LLGoNoLTO | 76508.0 ms | 73775.9 ms | 2732.0 ms | 26177.3 ms |
| IXGo | Go | 74194.3 ms | 61372.2 ms | 12822.1 ms | 20416.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 63709.1 ms | 61349.0 ms | 2360.2 ms | 41164.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 61466.5 ms | 59217.9 ms | 2248.7 ms | 39694.4 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 56716.6 ms | 54646.9 ms | 2069.6 ms | 21608.9 ms |
| Dustin_humanize | LLGoNoLTO | 53555.8 ms | 51690.9 ms | 1864.8 ms | 19998.2 ms |
| Etcdctl | Go | 28734.4 ms | 24141.1 ms | 4593.4 ms | 8935.6 ms |
| XGo | Go | 16349.3 ms | 13761.9 ms | 2587.4 ms | 4887.4 ms |
| Aws_restjson | Go | 7213.4 ms | 5819.0 ms | 1394.3 ms | 3062.6 ms |
| Gorm_schema | Go | 5013.5 ms | 4160.3 ms | 853.2 ms | 1985.9 ms |
| Uber_zap | Go | 4650.1 ms | 3867.4 ms | 782.7 ms | 1955.1 ms |
| K8s_workqueue | Go | 3985.4 ms | 3219.1 ms | 766.3 ms | 1444.6 ms |
| Toml | Go | 1727.5 ms | 1403.3 ms | 324.2 ms | 828.4 ms |
| Dustin_humanize | Go | 726.7 ms | 538.6 ms | 188.1 ms | 368.0 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1672526.7 ms | 1204791.1 ms | 8 |
| LLGoFullLTOGlobalDCE | 1544430.8 ms | 1085527.8 ms | 8 |
| LLGoFullLTOGlobalDCEPlugin | 1505944.6 ms | 1046536.2 ms | 8 |
| LLGoNoLTO | 1015119.5 ms | 335241.0 ms | 8 |
| LLGoDeadcodeDrop | 988345.4 ms | 333876.9 ms | 8 |
| Go | 142594.5 ms | 43884.1 ms | 9 |

Dependency download details are in `download-timings.log`.
