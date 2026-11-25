## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 782698.3 ms | 758873.7 ms | 23824.6 ms | 498836.4 ms |
| IXGo | LLGoFullLTOGlobalDCE | 695988.6 ms | 671747.0 ms | 24241.6 ms | 457387.3 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 653757.0 ms | 630363.8 ms | 23393.2 ms | 440663.5 ms |
| IXGo | LLGoDeadcodeDrop | 397450.0 ms | 373719.2 ms | 23730.9 ms | 128841.7 ms |
| IXGo | LLGoNoLTO | 380710.4 ms | 360472.3 ms | 20238.0 ms | 119873.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 369316.2 ms | 358203.4 ms | 11112.8 ms | 270215.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 361780.7 ms | 350954.4 ms | 10826.3 ms | 265390.8 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 350363.1 ms | 339960.4 ms | 10402.8 ms | 259415.9 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 259806.4 ms | 253406.4 ms | 6400.0 ms | 176951.6 ms |
| XGo | LLGoFullLTONoGlobalDCE | 259508.9 ms | 251886.8 ms | 7622.0 ms | 207786.4 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 240887.5 ms | 233581.8 ms | 7305.8 ms | 186525.2 ms |
| XGo | LLGoFullLTOGlobalDCE | 229299.3 ms | 222297.2 ms | 7002.1 ms | 177087.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 227183.4 ms | 221091.7 ms | 6091.8 ms | 148165.1 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 225557.3 ms | 219723.2 ms | 5834.1 ms | 149365.9 ms |
| Aws_restjson | LLGoNoLTO | 216652.0 ms | 211357.9 ms | 5294.1 ms | 67857.0 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 212962.4 ms | 207559.8 ms | 5402.6 ms | 151157.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 203891.3 ms | 198516.1 ms | 5375.2 ms | 145337.1 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 202334.8 ms | 197149.2 ms | 5185.6 ms | 144536.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 196085.5 ms | 191095.9 ms | 4989.7 ms | 132161.6 ms |
| Etcdctl | LLGoNoLTO | 195625.9 ms | 186574.4 ms | 9051.5 ms | 68237.1 ms |
| Etcdctl | LLGoDeadcodeDrop | 195058.3 ms | 185315.4 ms | 9742.9 ms | 69265.4 ms |
| Aws_restjson | LLGoDeadcodeDrop | 192446.3 ms | 186816.8 ms | 5629.5 ms | 62415.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 189613.5 ms | 184520.7 ms | 5092.9 ms | 128616.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 168370.7 ms | 163515.8 ms | 4854.9 ms | 111493.9 ms |
| Uber_zap | LLGoDeadcodeDrop | 167448.0 ms | 162470.7 ms | 4977.4 ms | 56045.1 ms |
| Uber_zap | LLGoNoLTO | 161553.6 ms | 157091.0 ms | 4462.5 ms | 52839.3 ms |
| K8s_workqueue | LLGoNoLTO | 156421.7 ms | 151832.6 ms | 4589.1 ms | 51221.7 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 151463.2 ms | 146655.5 ms | 4807.7 ms | 50809.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 124939.9 ms | 121208.4 ms | 3731.5 ms | 87198.2 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 120138.0 ms | 116487.1 ms | 3650.9 ms | 84113.4 ms |
| Toml | LLGoFullLTONoGlobalDCE | 119037.9 ms | 115578.5 ms | 3459.4 ms | 83332.1 ms |
| XGo | LLGoDeadcodeDrop | 110167.0 ms | 103277.9 ms | 6889.0 ms | 41017.4 ms |
| XGo | LLGoNoLTO | 106541.8 ms | 100815.5 ms | 5726.3 ms | 39457.0 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 105897.7 ms | 102578.5 ms | 3319.2 ms | 69153.6 ms |
| Toml | LLGoFullLTOGlobalDCE | 101315.3 ms | 97997.9 ms | 3317.4 ms | 65770.1 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 100817.8 ms | 97349.1 ms | 3468.7 ms | 64290.6 ms |
| Gorm_schema | LLGoNoLTO | 91638.4 ms | 88574.9 ms | 3063.5 ms | 32203.4 ms |
| Gorm_schema | LLGoDeadcodeDrop | 90092.9 ms | 86657.5 ms | 3435.3 ms | 32199.8 ms |
| Toml | LLGoNoLTO | 83904.6 ms | 81118.7 ms | 2785.9 ms | 29537.8 ms |
| Toml | LLGoDeadcodeDrop | 83323.6 ms | 80431.0 ms | 2892.6 ms | 29288.8 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 78300.7 ms | 75947.8 ms | 2353.0 ms | 56834.6 ms |
| IXGo | Go | 74021.9 ms | 61123.5 ms | 12898.4 ms | 20363.5 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 65057.0 ms | 62823.0 ms | 2234.0 ms | 41962.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 62579.2 ms | 60350.1 ms | 2229.1 ms | 40644.3 ms |
| Dustin_humanize | LLGoNoLTO | 59952.6 ms | 58059.0 ms | 1893.6 ms | 22711.6 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 58699.8 ms | 56645.0 ms | 2054.8 ms | 22671.0 ms |
| Etcdctl | Go | 30333.6 ms | 25555.3 ms | 4778.3 ms | 9252.0 ms |
| XGo | Go | 17153.2 ms | 14379.8 ms | 2773.3 ms | 5213.7 ms |
| Aws_restjson | Go | 7405.4 ms | 5926.7 ms | 1478.6 ms | 3693.1 ms |
| Gorm_schema | Go | 5075.6 ms | 4224.9 ms | 850.8 ms | 2101.6 ms |
| Uber_zap | Go | 4642.2 ms | 3873.7 ms | 768.5 ms | 1953.3 ms |
| K8s_workqueue | Go | 4112.1 ms | 3307.1 ms | 805.0 ms | 1510.4 ms |
| Toml | Go | 1795.1 ms | 1411.3 ms | 383.9 ms | 880.5 ms |
| Dustin_humanize | Go | 717.6 ms | 520.1 ms | 197.5 ms | 358.0 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2256209.3 ms | 1604791.6 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2245738.4 ms | 1519142.1 ms | 9 |
| LLGoFullLTOGlobalDCE | 2205541.0 ms | 1520459.8 ms | 9 |
| LLGoNoLTO | 1453001.0 ms | 483937.9 ms | 9 |
| LLGoDeadcodeDrop | 1446149.0 ms | 492554.1 ms | 9 |
| Go | 145256.7 ms | 45326.0 ms | 9 |

Dependency download details are in `download-timings.log`.
