## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 659059.2 ms | 642007.2 ms | 17052.0 ms | 438733.0 ms |
| IXGo | LLGoFullLTOGlobalDCE | 656531.0 ms | 638872.8 ms | 17658.2 ms | 440117.9 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 644517.0 ms | 627029.0 ms | 17488.0 ms | 431504.6 ms |
| IXGo | LLGoDeadcodeDrop | 359173.5 ms | 341693.0 ms | 17480.5 ms | 117171.5 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 343861.7 ms | 335856.3 ms | 8005.4 ms | 258752.6 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 342156.1 ms | 334349.6 ms | 7806.5 ms | 258997.3 ms |
| IXGo | LLGoNoLTO | 337149.1 ms | 323333.5 ms | 13815.6 ms | 107542.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 337084.7 ms | 329181.8 ms | 7902.9 ms | 253450.8 ms |
| XGo | LLGoFullLTONoGlobalDCE | 257391.2 ms | 251826.2 ms | 5565.0 ms | 211295.2 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 254253.4 ms | 249571.2 ms | 4682.2 ms | 174024.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 231777.2 ms | 227179.5 ms | 4597.7 ms | 151812.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 229070.8 ms | 224464.5 ms | 4606.3 ms | 151003.1 ms |
| XGo | LLGoFullLTOGlobalDCE | 224317.9 ms | 218801.7 ms | 5516.2 ms | 176972.2 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 222876.3 ms | 217592.5 ms | 5283.8 ms | 176439.4 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 215154.2 ms | 210901.2 ms | 4253.0 ms | 154397.6 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 206337.6 ms | 202176.1 ms | 4161.5 ms | 148822.8 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 200462.7 ms | 196503.8 ms | 3958.9 ms | 144249.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 199270.4 ms | 194982.9 ms | 4287.6 ms | 138340.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 189500.1 ms | 185564.5 ms | 3935.6 ms | 130332.1 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 177351.1 ms | 173540.9 ms | 3810.2 ms | 120321.7 ms |
| Aws_restjson | LLGoNoLTO | 170502.9 ms | 166910.0 ms | 3592.9 ms | 54256.2 ms |
| Aws_restjson | LLGoDeadcodeDrop | 169348.8 ms | 165597.9 ms | 3750.9 ms | 54832.6 ms |
| Etcdctl | LLGoNoLTO | 166153.0 ms | 160072.5 ms | 6080.5 ms | 57970.0 ms |
| Etcdctl | LLGoDeadcodeDrop | 165613.3 ms | 159118.4 ms | 6494.9 ms | 58734.8 ms |
| Uber_zap | LLGoNoLTO | 141705.8 ms | 138637.4 ms | 3068.4 ms | 45583.9 ms |
| Uber_zap | LLGoDeadcodeDrop | 136227.9 ms | 133078.2 ms | 3149.8 ms | 45365.6 ms |
| K8s_workqueue | LLGoNoLTO | 130029.8 ms | 127163.7 ms | 2866.1 ms | 42397.3 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 129014.7 ms | 125835.0 ms | 3179.7 ms | 43460.1 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 105835.8 ms | 103305.4 ms | 2530.4 ms | 75353.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 105650.3 ms | 103102.4 ms | 2547.9 ms | 73927.5 ms |
| Toml | LLGoFullLTONoGlobalDCE | 100613.2 ms | 98262.7 ms | 2350.6 ms | 70247.1 ms |
| XGo | LLGoNoLTO | 93044.6 ms | 89161.3 ms | 3883.3 ms | 35599.3 ms |
| XGo | LLGoDeadcodeDrop | 92799.5 ms | 88402.6 ms | 4396.9 ms | 35055.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 88798.2 ms | 86420.2 ms | 2378.0 ms | 55580.0 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 88126.5 ms | 85776.8 ms | 2349.7 ms | 57994.1 ms |
| Toml | LLGoFullLTOGlobalDCE | 87050.0 ms | 84727.5 ms | 2322.5 ms | 57131.0 ms |
| Gorm_schema | LLGoDeadcodeDrop | 75251.2 ms | 73082.8 ms | 2168.4 ms | 26960.3 ms |
| Gorm_schema | LLGoNoLTO | 73870.8 ms | 71901.2 ms | 1969.6 ms | 25970.1 ms |
| Toml | LLGoDeadcodeDrop | 70446.9 ms | 68528.3 ms | 1918.6 ms | 25224.0 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 69465.2 ms | 67853.1 ms | 1612.0 ms | 50554.0 ms |
| Toml | LLGoNoLTO | 69374.6 ms | 67631.4 ms | 1743.2 ms | 24656.0 ms |
| IXGo | Go | 64687.4 ms | 55636.3 ms | 9051.1 ms | 17655.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 55016.3 ms | 53554.9 ms | 1461.5 ms | 35969.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 53408.1 ms | 52032.4 ms | 1375.7 ms | 35022.4 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 47567.1 ms | 46320.2 ms | 1246.9 ms | 18440.6 ms |
| Dustin_humanize | LLGoNoLTO | 47444.8 ms | 46222.2 ms | 1222.6 ms | 17985.9 ms |
| Etcdctl | Go | 24655.5 ms | 21501.6 ms | 3153.9 ms | 7487.9 ms |
| XGo | Go | 14510.0 ms | 12691.6 ms | 1818.4 ms | 4297.7 ms |
| Aws_restjson | Go | 5900.5 ms | 5011.6 ms | 889.0 ms | 2446.0 ms |
| Gorm_schema | Go | 4259.1 ms | 3664.9 ms | 594.2 ms | 1661.9 ms |
| Uber_zap | Go | 3945.5 ms | 3403.2 ms | 542.3 ms | 1556.1 ms |
| K8s_workqueue | Go | 3403.5 ms | 2923.6 ms | 480.0 ms | 1224.6 ms |
| Toml | Go | 1595.9 ms | 1364.7 ms | 231.3 ms | 746.3 ms |
| Dustin_humanize | Go | 598.9 ms | 479.1 ms | 119.8 ms | 299.0 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2195723.7 ms | 1575197.0 ms | 9 |
| LLGoFullLTOGlobalDCE | 2095552.4 ms | 1471024.4 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2053660.3 ms | 1425125.7 ms | 9 |
| LLGoDeadcodeDrop | 1245442.9 ms | 425245.3 ms | 9 |
| LLGoNoLTO | 1229275.5 ms | 411960.8 ms | 9 |
| Go | 123556.3 ms | 37375.4 ms | 9 |

Dependency download details are in `download-timings.log`.
