## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 428882.4 ms | 419006.8 ms | 9875.6 ms | 241270.9 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 428470.8 ms | 418056.7 ms | 10414.1 ms | 237882.0 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 412881.4 ms | 403122.6 ms | 9758.9 ms | 230322.1 ms |
| IXGo | LLGoDeadcodeDrop | 321709.0 ms | 312997.4 ms | 8711.6 ms | 99404.1 ms |
| IXGo | LLGoNoLTO | 307697.0 ms | 298564.8 ms | 9132.3 ms | 93091.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 203461.2 ms | 199277.3 ms | 4184.0 ms | 131234.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 201949.6 ms | 197971.4 ms | 3978.3 ms | 125261.8 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 196620.6 ms | 192580.3 ms | 4040.4 ms | 135635.8 ms |
| Etcdctl | LLGoDeadcodeDrop | 140726.4 ms | 137137.7 ms | 3588.8 ms | 47183.5 ms |
| Etcdctl | LLGoNoLTO | 140424.1 ms | 136858.3 ms | 3565.8 ms | 49190.1 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 137414.1 ms | 135523.0 ms | 1891.1 ms | 108811.3 ms |
| XGo | LLGoFullLTONoGlobalDCE | 137173.6 ms | 134387.6 ms | 2786.0 ms | 101669.6 ms |
| XGo | LLGoFullLTOGlobalDCE | 135019.5 ms | 132233.9 ms | 2785.6 ms | 96844.5 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 131353.8 ms | 128827.8 ms | 2526.0 ms | 93293.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 126134.6 ms | 124154.5 ms | 1980.2 ms | 104337.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 123741.0 ms | 121707.0 ms | 2033.9 ms | 98810.3 ms |
| Aws_restjson | LLGoNoLTO | 96540.9 ms | 94942.7 ms | 1598.2 ms | 63916.9 ms |
| Aws_restjson | LLGoDeadcodeDrop | 91588.4 ms | 89982.7 ms | 1605.7 ms | 59618.4 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 79300.4 ms | 77822.1 ms | 1478.3 ms | 61299.2 ms |
| XGo | LLGoDeadcodeDrop | 79207.7 ms | 76844.4 ms | 2363.4 ms | 35301.7 ms |
| XGo | LLGoNoLTO | 77671.5 ms | 75415.0 ms | 2256.5 ms | 30879.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 74792.1 ms | 73421.5 ms | 1370.6 ms | 58809.0 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 74726.0 ms | 73290.7 ms | 1435.3 ms | 58575.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 73240.6 ms | 71709.7 ms | 1530.9 ms | 58000.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 71533.7 ms | 70026.7 ms | 1507.0 ms | 52836.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 64637.2 ms | 63271.9 ms | 1365.3 ms | 48259.1 ms |
| IXGo | Go | 58588.8 ms | 53745.6 ms | 4843.2 ms | 36684.8 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 45424.4 ms | 44293.4 ms | 1131.0 ms | 32092.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 44828.4 ms | 43709.0 ms | 1119.4 ms | 32020.2 ms |
| Uber_zap | LLGoDeadcodeDrop | 41039.0 ms | 39819.8 ms | 1219.1 ms | 17477.6 ms |
| Uber_zap | LLGoNoLTO | 40045.0 ms | 38711.7 ms | 1333.3 ms | 18424.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 39957.8 ms | 38788.2 ms | 1169.6 ms | 24976.0 ms |
| Toml | LLGoFullLTONoGlobalDCE | 36338.1 ms | 35474.3 ms | 863.9 ms | 30903.4 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 36034.0 ms | 34809.1 ms | 1224.9 ms | 21983.7 ms |
| K8s_workqueue | LLGoNoLTO | 35154.2 ms | 34007.7 ms | 1146.6 ms | 15766.1 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 31445.5 ms | 30599.1 ms | 846.4 ms | 22389.6 ms |
| Toml | LLGoFullLTOGlobalDCE | 31017.5 ms | 30213.0 ms | 804.4 ms | 21887.1 ms |
| Gorm_schema | LLGoDeadcodeDrop | 27659.4 ms | 26643.5 ms | 1016.0 ms | 9781.0 ms |
| Gorm_schema | LLGoNoLTO | 26655.0 ms | 25644.2 ms | 1010.8 ms | 12211.2 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 26128.3 ms | 25458.3 ms | 670.0 ms | 20906.3 ms |
| Etcdctl | Go | 23622.9 ms | 21762.9 ms | 1860.0 ms | 7105.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 19868.8 ms | 19228.6 ms | 640.2 ms | 14337.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 19056.3 ms | 18415.4 ms | 640.9 ms | 13865.0 ms |
| Toml | LLGoDeadcodeDrop | 18318.2 ms | 17548.7 ms | 769.5 ms | 8332.6 ms |
| Toml | LLGoNoLTO | 16605.3 ms | 15852.3 ms | 752.9 ms | 9944.1 ms |
| XGo | Go | 13157.4 ms | 12120.9 ms | 1036.6 ms | 5402.3 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 10183.1 ms | 9617.4 ms | 565.6 ms | 4947.2 ms |
| Dustin_humanize | LLGoNoLTO | 9635.7 ms | 9121.1 ms | 514.5 ms | 4344.5 ms |
| Aws_restjson | Go | 5882.4 ms | 5260.6 ms | 621.8 ms | 2762.2 ms |
| Gorm_schema | Go | 3978.9 ms | 3663.3 ms | 315.6 ms | 1540.7 ms |
| Uber_zap | Go | 3759.3 ms | 3436.0 ms | 323.3 ms | 1737.3 ms |
| K8s_workqueue | Go | 3682.1 ms | 3214.0 ms | 468.1 ms | 10702.0 ms |
| Toml | Go | 1385.6 ms | 1242.6 ms | 143.1 ms | 635.2 ms |
| Dustin_humanize | Go | 568.6 ms | 460.7 ms | 107.9 ms | 277.9 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1146007.2 ms | 780215.3 ms | 9 |
| LLGoFullLTOGlobalDCE | 1133144.6 ms | 748050.7 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1116246.3 ms | 728264.3 ms | 9 |
| LLGoDeadcodeDrop | 766465.3 ms | 304029.8 ms | 9 |
| LLGoNoLTO | 750428.6 ms | 297768.3 ms | 9 |
| Go | 114626.1 ms | 66847.5 ms | 9 |

Dependency download details are in `download-timings.log`.
