## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 1022948.2 ms | 993698.5 ms | 29249.7 ms | 616368.8 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 892347.9 ms | 862508.8 ms | 29839.1 ms | 555272.5 ms |
| IXGo | LLGoFullLTOGlobalDCE | 876337.3 ms | 846711.0 ms | 29626.4 ms | 542876.0 ms |
| IXGo | LLGoNoLTO | 576776.4 ms | 552329.5 ms | 24446.9 ms | 168290.0 ms |
| IXGo | LLGoDeadcodeDrop | 549617.5 ms | 520493.2 ms | 29124.3 ms | 166010.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 423961.1 ms | 410730.9 ms | 13230.2 ms | 313109.0 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 418455.2 ms | 405255.1 ms | 13200.0 ms | 311115.5 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 414065.8 ms | 400766.2 ms | 13299.6 ms | 304783.2 ms |
| XGo | LLGoFullLTONoGlobalDCE | 307110.9 ms | 298049.4 ms | 9061.5 ms | 247701.0 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 283392.0 ms | 276180.1 ms | 7211.9 ms | 197109.2 ms |
| XGo | LLGoFullLTOGlobalDCE | 271139.6 ms | 262156.3 ms | 8983.3 ms | 210121.6 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 270601.3 ms | 261837.7 ms | 8763.7 ms | 209576.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 264345.8 ms | 256962.5 ms | 7383.3 ms | 173985.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 256010.2 ms | 248916.2 ms | 7094.0 ms | 167080.0 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 237156.4 ms | 231088.9 ms | 6067.5 ms | 170111.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 236248.0 ms | 230135.2 ms | 6112.8 ms | 171325.9 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 235943.0 ms | 229402.6 ms | 6540.4 ms | 170635.8 ms |
| Etcdctl | LLGoNoLTO | 218035.2 ms | 206997.8 ms | 11037.4 ms | 74151.9 ms |
| Etcdctl | LLGoDeadcodeDrop | 216206.6 ms | 203985.3 ms | 12221.3 ms | 74583.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 213561.5 ms | 207554.1 ms | 6007.4 ms | 145521.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 210621.6 ms | 204764.5 ms | 5857.0 ms | 143344.3 ms |
| Aws_restjson | LLGoNoLTO | 200194.2 ms | 194264.6 ms | 5929.7 ms | 62904.5 ms |
| Aws_restjson | LLGoDeadcodeDrop | 197612.1 ms | 191217.5 ms | 6394.6 ms | 62876.8 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 195410.5 ms | 189382.3 ms | 6028.2 ms | 130559.1 ms |
| Uber_zap | LLGoDeadcodeDrop | 163616.8 ms | 158409.0 ms | 5207.8 ms | 53531.6 ms |
| Uber_zap | LLGoNoLTO | 161436.3 ms | 156781.2 ms | 4655.1 ms | 52415.6 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 154892.5 ms | 149678.3 ms | 5214.3 ms | 51185.7 ms |
| K8s_workqueue | LLGoNoLTO | 154052.1 ms | 149066.2 ms | 4986.0 ms | 49976.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 143448.5 ms | 138881.1 ms | 4567.4 ms | 100906.5 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 142081.6 ms | 137486.9 ms | 4594.7 ms | 101589.4 ms |
| Toml | LLGoFullLTONoGlobalDCE | 127659.5 ms | 123583.7 ms | 4075.8 ms | 90045.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 121062.4 ms | 116916.5 ms | 4146.0 ms | 78685.3 ms |
| XGo | LLGoDeadcodeDrop | 121056.2 ms | 113070.3 ms | 7985.9 ms | 43439.2 ms |
| XGo | LLGoNoLTO | 117064.8 ms | 110322.5 ms | 6742.3 ms | 42676.6 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 115087.3 ms | 111356.4 ms | 3730.9 ms | 76037.1 ms |
| Toml | LLGoFullLTOGlobalDCE | 110589.3 ms | 106807.6 ms | 3781.7 ms | 72863.5 ms |
| Gorm_schema | LLGoNoLTO | 101808.7 ms | 98190.9 ms | 3617.7 ms | 35193.2 ms |
| Gorm_schema | LLGoDeadcodeDrop | 99907.1 ms | 96001.7 ms | 3905.4 ms | 35067.5 ms |
| Toml | LLGoNoLTO | 95016.0 ms | 91822.8 ms | 3193.2 ms | 32466.8 ms |
| IXGo | Go | 94840.0 ms | 78705.5 ms | 16134.5 ms | 25975.8 ms |
| Toml | LLGoDeadcodeDrop | 94818.1 ms | 91377.6 ms | 3440.5 ms | 32915.8 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 91935.1 ms | 89022.2 ms | 2912.8 ms | 67446.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 75430.5 ms | 72884.5 ms | 2545.9 ms | 50348.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 73665.1 ms | 71093.5 ms | 2571.5 ms | 48683.0 ms |
| Dustin_humanize | LLGoNoLTO | 65209.2 ms | 62885.7 ms | 2323.5 ms | 24371.7 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 64444.8 ms | 61892.9 ms | 2551.9 ms | 24220.2 ms |
| Etcdctl | Go | 36150.1 ms | 30389.2 ms | 5760.8 ms | 11281.2 ms |
| XGo | Go | 20828.4 ms | 17525.1 ms | 3303.3 ms | 6138.7 ms |
| Aws_restjson | Go | 8804.9 ms | 7179.5 ms | 1625.4 ms | 3687.1 ms |
| Gorm_schema | Go | 6497.7 ms | 5429.6 ms | 1068.1 ms | 2571.3 ms |
| Uber_zap | Go | 5833.3 ms | 4927.8 ms | 905.5 ms | 2351.4 ms |
| K8s_workqueue | Go | 5245.0 ms | 4286.8 ms | 958.2 ms | 1937.6 ms |
| Toml | Go | 2251.1 ms | 1833.9 ms | 417.1 ms | 1090.9 ms |
| Dustin_humanize | Go | 910.6 ms | 682.1 ms | 228.5 ms | 445.4 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2736081.6 ms | 1911025.7 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2689367.6 ms | 1783442.6 ms | 9 |
| LLGoFullLTOGlobalDCE | 2605166.4 ms | 1772732.8 ms | 9 |
| LLGoNoLTO | 1689593.0 ms | 542447.1 ms | 9 |
| LLGoDeadcodeDrop | 1662171.8 ms | 543830.8 ms | 9 |
| Go | 181361.1 ms | 55479.4 ms | 9 |

Dependency download details are in `download-timings.log`.
