## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 673033.6 ms | 656100.4 ms | 16933.2 ms | 447851.4 ms |
| IXGo | LLGoFullLTOGlobalDCE | 650968.5 ms | 634520.8 ms | 16447.7 ms | 436261.0 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 648475.6 ms | 631588.0 ms | 16887.6 ms | 431744.2 ms |
| IXGo | LLGoDeadcodeDrop | 383041.7 ms | 365278.2 ms | 17763.5 ms | 124160.9 ms |
| IXGo | LLGoNoLTO | 360494.3 ms | 346173.4 ms | 14320.9 ms | 112878.9 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 353611.5 ms | 345984.4 ms | 7627.2 ms | 265642.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 348318.1 ms | 341027.4 ms | 7290.7 ms | 261883.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 338265.1 ms | 331088.2 ms | 7176.9 ms | 252831.5 ms |
| XGo | LLGoFullLTONoGlobalDCE | 262366.0 ms | 256955.8 ms | 5410.2 ms | 211563.6 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 238404.4 ms | 234157.2 ms | 4247.2 ms | 163980.5 ms |
| XGo | LLGoFullLTOGlobalDCE | 228163.8 ms | 222969.5 ms | 5194.3 ms | 177766.4 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 219257.3 ms | 214267.3 ms | 4990.0 ms | 169027.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 214775.5 ms | 210513.0 ms | 4262.5 ms | 139138.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 209419.7 ms | 205405.5 ms | 4014.1 ms | 136562.7 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 195408.2 ms | 191836.1 ms | 3572.1 ms | 140399.2 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 190720.6 ms | 186970.3 ms | 3750.3 ms | 137826.1 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 186311.5 ms | 182638.3 ms | 3673.2 ms | 134464.0 ms |
| Aws_restjson | LLGoNoLTO | 179826.8 ms | 176269.9 ms | 3556.9 ms | 56581.3 ms |
| Aws_restjson | LLGoDeadcodeDrop | 177816.8 ms | 174061.7 ms | 3755.1 ms | 57299.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 177354.0 ms | 173936.2 ms | 3417.8 ms | 122280.3 ms |
| Etcdctl | LLGoDeadcodeDrop | 174744.5 ms | 168361.0 ms | 6383.5 ms | 61260.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 174641.7 ms | 171264.9 ms | 3376.8 ms | 118921.6 ms |
| Etcdctl | LLGoNoLTO | 172047.7 ms | 166210.9 ms | 5836.8 ms | 59367.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 159831.2 ms | 156491.5 ms | 3339.7 ms | 107430.5 ms |
| Uber_zap | LLGoDeadcodeDrop | 146590.7 ms | 143403.5 ms | 3187.2 ms | 48396.3 ms |
| Uber_zap | LLGoNoLTO | 145336.7 ms | 142375.0 ms | 2961.7 ms | 46894.2 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 142585.3 ms | 139235.6 ms | 3349.8 ms | 47706.9 ms |
| K8s_workqueue | LLGoNoLTO | 141108.9 ms | 138194.0 ms | 2914.8 ms | 45542.1 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 111914.7 ms | 109411.5 ms | 2503.2 ms | 80248.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 111275.0 ms | 108839.8 ms | 2435.2 ms | 78289.3 ms |
| Toml | LLGoFullLTONoGlobalDCE | 103635.2 ms | 101310.2 ms | 2325.0 ms | 73215.3 ms |
| XGo | LLGoNoLTO | 97572.2 ms | 93619.2 ms | 3952.9 ms | 36466.9 ms |
| XGo | LLGoDeadcodeDrop | 95660.7 ms | 91568.4 ms | 4092.3 ms | 35427.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 93338.2 ms | 90961.0 ms | 2377.3 ms | 60163.9 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 90811.0 ms | 88647.6 ms | 2163.4 ms | 59845.4 ms |
| Toml | LLGoFullLTOGlobalDCE | 90576.5 ms | 88343.2 ms | 2233.3 ms | 59899.1 ms |
| Gorm_schema | LLGoDeadcodeDrop | 83575.6 ms | 81350.9 ms | 2224.6 ms | 29602.8 ms |
| Gorm_schema | LLGoNoLTO | 80844.3 ms | 78745.9 ms | 2098.4 ms | 28238.1 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 77219.0 ms | 75509.5 ms | 1709.5 ms | 56861.0 ms |
| Toml | LLGoNoLTO | 76272.3 ms | 74392.5 ms | 1879.8 ms | 26621.3 ms |
| Toml | LLGoDeadcodeDrop | 75814.0 ms | 73803.1 ms | 2010.9 ms | 26666.9 ms |
| IXGo | Go | 63204.4 ms | 55188.7 ms | 8015.7 ms | 17373.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 59357.0 ms | 57804.2 ms | 1552.8 ms | 39251.9 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 59033.8 ms | 57495.5 ms | 1538.3 ms | 38904.6 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 53552.8 ms | 52099.5 ms | 1453.3 ms | 20460.0 ms |
| Dustin_humanize | LLGoNoLTO | 51944.3 ms | 50681.9 ms | 1262.4 ms | 19540.6 ms |
| Etcdctl | Go | 25240.7 ms | 22322.7 ms | 2918.0 ms | 7674.0 ms |
| XGo | Go | 14445.7 ms | 12752.5 ms | 1693.2 ms | 4308.1 ms |
| Aws_restjson | Go | 6185.6 ms | 5354.5 ms | 831.1 ms | 2532.8 ms |
| Gorm_schema | Go | 4429.7 ms | 3864.1 ms | 565.6 ms | 1801.6 ms |
| Uber_zap | Go | 4179.0 ms | 3722.1 ms | 456.9 ms | 1684.5 ms |
| K8s_workqueue | Go | 3787.3 ms | 3260.4 ms | 527.0 ms | 1633.0 ms |
| Toml | Go | 1547.8 ms | 1322.0 ms | 225.8 ms | 717.0 ms |
| Dustin_humanize | Go | 614.0 ms | 489.6 ms | 124.4 ms | 305.1 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2181755.2 ms | 1561480.9 ms | 9 |
| LLGoFullLTOGlobalDCE | 2061421.0 ms | 1446311.0 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2023310.7 ms | 1394462.2 ms | 9 |
| LLGoDeadcodeDrop | 1333382.1 ms | 450979.9 ms | 9 |
| LLGoNoLTO | 1305447.4 ms | 432131.3 ms | 9 |
| Go | 123634.3 ms | 38029.9 ms | 9 |

Dependency download details are in `download-timings.log`.
