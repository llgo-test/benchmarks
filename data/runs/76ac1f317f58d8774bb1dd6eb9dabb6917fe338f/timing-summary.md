## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 740105.9 ms | 733438.4 ms | 6667.5 ms | 496313.7 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 690986.4 ms | 684648.6 ms | 6337.8 ms | 462803.1 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 678903.6 ms | 672278.1 ms | 6625.5 ms | 444740.1 ms |
| IXGo | LLGoDeadcodeDrop | 417663.3 ms | 411882.0 ms | 5781.3 ms | 138350.5 ms |
| IXGo | LLGoNoLTO | 404956.7 ms | 399335.1 ms | 5621.6 ms | 134637.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 273646.3 ms | 268923.7 ms | 4722.6 ms | 166874.6 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 271099.4 ms | 266590.2 ms | 4509.3 ms | 164647.8 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 270258.6 ms | 265455.1 ms | 4803.4 ms | 165342.4 ms |
| Etcdctl | LLGoDeadcodeDrop | 201660.8 ms | 197627.7 ms | 4033.1 ms | 66613.7 ms |
| Etcdctl | LLGoNoLTO | 199490.6 ms | 195472.2 ms | 4018.4 ms | 65837.0 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 183144.0 ms | 179993.8 ms | 3150.2 ms | 127673.3 ms |
| XGo | LLGoFullLTOGlobalDCE | 182666.5 ms | 179760.5 ms | 2906.0 ms | 127286.8 ms |
| XGo | LLGoFullLTONoGlobalDCE | 182159.9 ms | 179077.9 ms | 3081.9 ms | 128011.2 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 142661.5 ms | 140415.9 ms | 2245.6 ms | 105192.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 132418.3 ms | 130090.3 ms | 2328.0 ms | 93491.3 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 130815.4 ms | 128610.7 ms | 2204.8 ms | 92886.5 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 114582.6 ms | 112855.1 ms | 1727.5 ms | 88572.3 ms |
| XGo | LLGoDeadcodeDrop | 111429.4 ms | 108663.8 ms | 2765.6 ms | 41553.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 109996.8 ms | 108278.0 ms | 1718.8 ms | 86162.7 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 108175.6 ms | 106422.7 ms | 1752.9 ms | 85204.4 ms |
| XGo | LLGoNoLTO | 107350.7 ms | 104768.5 ms | 2582.1 ms | 40998.2 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 106437.8 ms | 104712.2 ms | 1725.6 ms | 79154.9 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 104396.8 ms | 102686.0 ms | 1710.8 ms | 77979.8 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 95760.4 ms | 94053.1 ms | 1707.3 ms | 72150.1 ms |
| Aws_restjson | LLGoNoLTO | 84069.4 ms | 82101.5 ms | 1967.9 ms | 39169.1 ms |
| Aws_restjson | LLGoDeadcodeDrop | 83917.7 ms | 81918.1 ms | 1999.5 ms | 39108.7 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 66444.1 ms | 65044.3 ms | 1399.8 ms | 46923.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 65598.8 ms | 64208.8 ms | 1390.0 ms | 45897.9 ms |
| Uber_zap | LLGoDeadcodeDrop | 58101.8 ms | 56693.4 ms | 1408.5 ms | 25344.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 56641.1 ms | 55391.7 ms | 1249.4 ms | 36258.2 ms |
| Uber_zap | LLGoNoLTO | 56571.0 ms | 55288.1 ms | 1282.9 ms | 24891.3 ms |
| Toml | LLGoFullLTONoGlobalDCE | 53684.6 ms | 52703.5 ms | 981.1 ms | 41712.4 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 50461.0 ms | 49000.3 ms | 1460.7 ms | 23305.8 ms |
| K8s_workqueue | LLGoNoLTO | 49919.8 ms | 48405.5 ms | 1514.2 ms | 22957.4 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 46804.4 ms | 45807.5 ms | 996.9 ms | 33936.3 ms |
| Toml | LLGoFullLTOGlobalDCE | 46026.6 ms | 45017.3 ms | 1009.3 ms | 34084.9 ms |
| IXGo | Go | 45702.9 ms | 42714.6 ms | 2988.3 ms | 13098.2 ms |
| Gorm_schema | LLGoDeadcodeDrop | 38653.4 ms | 37509.6 ms | 1143.8 ms | 12694.7 ms |
| Gorm_schema | LLGoNoLTO | 37532.5 ms | 36429.3 ms | 1103.2 ms | 12250.2 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 34490.5 ms | 33682.8 ms | 807.8 ms | 26876.5 ms |
| Etcdctl | Go | 33708.5 ms | 31733.5 ms | 1975.0 ms | 10152.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 25760.7 ms | 24952.1 ms | 808.7 ms | 17764.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 25216.1 ms | 24426.8 ms | 789.3 ms | 17802.7 ms |
| Toml | LLGoDeadcodeDrop | 24189.0 ms | 23234.5 ms | 954.5 ms | 9065.1 ms |
| Toml | LLGoNoLTO | 23502.7 ms | 22522.7 ms | 980.0 ms | 8850.1 ms |
| XGo | Go | 19147.3 ms | 18018.0 ms | 1129.3 ms | 5685.7 ms |
| Dustin_humanize | LLGoNoLTO | 13540.1 ms | 12798.2 ms | 742.0 ms | 5627.9 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 13369.5 ms | 12587.9 ms | 781.6 ms | 5695.2 ms |
| Aws_restjson | Go | 7995.7 ms | 7310.7 ms | 685.0 ms | 3223.6 ms |
| Gorm_schema | Go | 5806.1 ms | 5422.7 ms | 383.4 ms | 2193.2 ms |
| Uber_zap | Go | 5363.2 ms | 4980.0 ms | 383.3 ms | 2119.1 ms |
| K8s_workqueue | Go | 4774.6 ms | 4330.0 ms | 444.6 ms | 1683.7 ms |
| Toml | Go | 2034.3 ms | 1808.9 ms | 225.4 ms | 935.6 ms |
| Dustin_humanize | Go | 804.6 ms | 661.8 ms | 142.8 ms | 381.9 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTOGlobalDCE | 1675922.5 ms | 1143062.7 ms | 9 |
| LLGoFullLTONoGlobalDCE | 1663443.7 ms | 1150638.2 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1599516.6 ms | 1072042.8 ms | 9 |
| LLGoDeadcodeDrop | 999445.8 ms | 361731.4 ms | 9 |
| LLGoNoLTO | 976933.5 ms | 355218.4 ms | 9 |
| Go | 125337.1 ms | 39473.7 ms | 9 |

Dependency download details are in `download-timings.log`.
