## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTONoGlobalDCE | 680222.0 ms | 670336.6 ms | 9885.4 ms | 346378.0 ms |
| IXGo | LLGoFullLTOGlobalDCE | 667284.2 ms | 656178.8 ms | 11105.4 ms | 347325.7 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 651512.6 ms | 641438.8 ms | 10073.8 ms | 337109.9 ms |
| IXGo | LLGoDeadcodeDrop | 631890.2 ms | 617651.3 ms | 14238.9 ms | 183851.8 ms |
| IXGo | LLGoNoLTO | 529712.2 ms | 519632.3 ms | 10079.9 ms | 153967.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 354431.3 ms | 348963.7 ms | 5467.7 ms | 207049.6 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 339424.4 ms | 334252.5 ms | 5171.9 ms | 198470.9 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 337893.3 ms | 332899.0 ms | 4994.4 ms | 199190.3 ms |
| Aws_restjson | LLGoNoLTO | 278059.1 ms | 274587.6 ms | 3471.6 ms | 92727.3 ms |
| Aws_restjson | LLGoDeadcodeDrop | 267228.3 ms | 263820.1 ms | 3408.2 ms | 89379.0 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 266178.9 ms | 262492.1 ms | 3686.8 ms | 147362.5 ms |
| Etcdctl | LLGoDeadcodeDrop | 263767.8 ms | 257965.5 ms | 5802.3 ms | 87253.4 ms |
| Etcdctl | LLGoNoLTO | 258340.3 ms | 254069.4 ms | 4270.9 ms | 84439.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 256616.7 ms | 252719.9 ms | 3896.8 ms | 135846.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 254381.7 ms | 250687.5 ms | 3694.2 ms | 133899.3 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 249557.1 ms | 246121.8 ms | 3435.3 ms | 162926.7 ms |
| XGo | LLGoFullLTONoGlobalDCE | 242796.5 ms | 239493.3 ms | 3303.3 ms | 159035.4 ms |
| XGo | LLGoFullLTOGlobalDCE | 242218.9 ms | 238814.5 ms | 3404.4 ms | 157049.9 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 235375.3 ms | 231804.5 ms | 3570.8 ms | 135028.1 ms |
| Uber_zap | LLGoDeadcodeDrop | 234332.2 ms | 231439.0 ms | 2893.2 ms | 82252.3 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 230325.1 ms | 226861.5 ms | 3463.6 ms | 132008.6 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 229442.8 ms | 226185.3 ms | 3257.5 ms | 80747.2 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 227912.4 ms | 224542.4 ms | 3370.1 ms | 124113.9 ms |
| K8s_workqueue | LLGoNoLTO | 226045.8 ms | 223162.3 ms | 2883.5 ms | 79631.7 ms |
| Uber_zap | LLGoNoLTO | 224649.5 ms | 221802.1 ms | 2847.4 ms | 79081.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 224163.3 ms | 220904.1 ms | 3259.2 ms | 127867.9 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 219322.1 ms | 215992.2 ms | 3329.9 ms | 119306.1 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 210851.2 ms | 207504.0 ms | 3347.1 ms | 112786.4 ms |
| XGo | LLGoDeadcodeDrop | 160362.9 ms | 156650.0 ms | 3712.9 ms | 59332.6 ms |
| XGo | LLGoNoLTO | 159264.0 ms | 156647.1 ms | 2616.9 ms | 57517.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 112469.3 ms | 110385.9 ms | 2083.4 ms | 65116.3 ms |
| Gorm_schema | LLGoDeadcodeDrop | 109243.6 ms | 107426.7 ms | 1816.9 ms | 36144.9 ms |
| Gorm_schema | LLGoNoLTO | 107404.4 ms | 105458.5 ms | 1945.9 ms | 36454.2 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 106108.5 ms | 104072.4 ms | 2036.0 ms | 61677.3 ms |
| Toml | LLGoFullLTONoGlobalDCE | 103847.2 ms | 101749.8 ms | 2097.3 ms | 59696.8 ms |
| Toml | LLGoDeadcodeDrop | 101199.5 ms | 99427.1 ms | 1772.4 ms | 33415.3 ms |
| Toml | LLGoNoLTO | 100879.1 ms | 99079.8 ms | 1799.3 ms | 33258.1 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 99337.0 ms | 97367.1 ms | 1969.9 ms | 51874.5 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 92647.7 ms | 90622.6 ms | 2025.1 ms | 48595.0 ms |
| Toml | LLGoFullLTOGlobalDCE | 90987.8 ms | 89024.7 ms | 1963.1 ms | 48005.2 ms |
| IXGo | Go | 84564.1 ms | 79472.0 ms | 5092.1 ms | 23147.8 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 73500.4 ms | 72159.4 ms | 1340.9 ms | 26343.2 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 70773.0 ms | 69327.4 ms | 1445.6 ms | 42817.1 ms |
| Dustin_humanize | LLGoNoLTO | 70250.5 ms | 68976.2 ms | 1274.3 ms | 25086.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 61126.7 ms | 59753.5 ms | 1373.1 ms | 32788.9 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 60831.1 ms | 59502.0 ms | 1329.0 ms | 32400.8 ms |
| Etcdctl | Go | 32999.7 ms | 31041.2 ms | 1958.5 ms | 9872.6 ms |
| XGo | Go | 19375.2 ms | 18216.9 ms | 1158.3 ms | 5634.4 ms |
| Aws_restjson | Go | 8261.7 ms | 7532.6 ms | 729.1 ms | 3410.5 ms |
| Gorm_schema | Go | 5720.3 ms | 5357.5 ms | 362.8 ms | 2162.0 ms |
| Uber_zap | Go | 5591.2 ms | 5080.4 ms | 510.7 ms | 2365.6 ms |
| K8s_workqueue | Go | 4831.6 ms | 4359.1 ms | 472.5 ms | 1711.5 ms |
| Toml | Go | 2019.2 ms | 1806.4 ms | 212.9 ms | 943.2 ms |
| Dustin_humanize | Go | 811.8 ms | 672.8 ms | 139.0 ms | 384.2 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2273519.9 ms | 1283194.0 ms | 9 |
| LLGoFullLTOGlobalDCE | 2228324.7 ms | 1239968.2 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2186750.7 ms | 1202565.5 ms | 9 |
| LLGoDeadcodeDrop | 2070967.7 ms | 678719.7 ms | 9 |
| LLGoNoLTO | 1954604.9 ms | 642163.8 ms | 9 |
| Go | 164174.8 ms | 49631.8 ms | 9 |

Dependency download details are in `download-timings.log`.
