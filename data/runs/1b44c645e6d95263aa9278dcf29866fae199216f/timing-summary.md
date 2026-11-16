## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 623313.0 ms | 604289.4 ms | 19023.7 ms | 401752.3 ms |
| IXGo | LLGoFullLTOGlobalDCE | 587624.1 ms | 568847.4 ms | 18776.7 ms | 381372.1 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 523374.9 ms | 505820.2 ms | 17554.7 ms | 353795.5 ms |
| IXGo | LLGoNoLTO | 317772.3 ms | 301523.8 ms | 16248.4 ms | 100567.1 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 306228.9 ms | 297052.6 ms | 9176.3 ms | 227799.0 ms |
| IXGo | LLGoDeadcodeDrop | 304171.7 ms | 285321.4 ms | 18850.3 ms | 100898.5 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 293209.6 ms | 284535.4 ms | 8674.1 ms | 217886.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 287104.1 ms | 278446.3 ms | 8657.8 ms | 212093.3 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 233556.2 ms | 228421.7 ms | 5134.5 ms | 159201.8 ms |
| XGo | LLGoFullLTONoGlobalDCE | 219858.4 ms | 213699.8 ms | 6158.6 ms | 175392.7 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 203498.6 ms | 197556.5 ms | 5942.1 ms | 157602.5 ms |
| XGo | LLGoFullLTOGlobalDCE | 198508.4 ms | 192567.3 ms | 5941.1 ms | 154124.3 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 194062.3 ms | 189257.4 ms | 4804.9 ms | 123824.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 191731.6 ms | 186964.4 ms | 4767.3 ms | 124158.1 ms |
| Aws_restjson | LLGoNoLTO | 182738.2 ms | 178599.8 ms | 4138.4 ms | 61998.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 174414.5 ms | 170028.3 ms | 4386.2 ms | 124866.0 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 166473.1 ms | 162284.3 ms | 4188.8 ms | 119783.7 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 162629.3 ms | 158387.4 ms | 4241.9 ms | 116560.1 ms |
| Etcdctl | LLGoDeadcodeDrop | 159536.7 ms | 151696.5 ms | 7840.2 ms | 56591.9 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 156122.1 ms | 152078.2 ms | 4043.8 ms | 107381.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 151133.9 ms | 146845.8 ms | 4288.2 ms | 103442.8 ms |
| Etcdctl | LLGoNoLTO | 150234.1 ms | 143297.7 ms | 6936.3 ms | 52223.2 ms |
| Aws_restjson | LLGoDeadcodeDrop | 150104.2 ms | 145744.2 ms | 4360.0 ms | 49104.6 ms |
| Uber_zap | LLGoNoLTO | 142543.6 ms | 138905.7 ms | 3637.9 ms | 46355.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 139126.5 ms | 135193.2 ms | 3933.3 ms | 93183.4 ms |
| Uber_zap | LLGoDeadcodeDrop | 133604.0 ms | 129682.5 ms | 3921.4 ms | 44550.1 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 133033.4 ms | 129097.7 ms | 3935.8 ms | 44798.4 ms |
| K8s_workqueue | LLGoNoLTO | 122584.2 ms | 119082.6 ms | 3501.5 ms | 39929.2 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 94489.2 ms | 91654.7 ms | 2834.5 ms | 66467.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 92151.1 ms | 89245.0 ms | 2906.2 ms | 64850.0 ms |
| XGo | LLGoDeadcodeDrop | 92102.3 ms | 86823.7 ms | 5278.6 ms | 34026.1 ms |
| XGo | LLGoNoLTO | 87292.3 ms | 82614.1 ms | 4678.2 ms | 33320.2 ms |
| Toml | LLGoFullLTONoGlobalDCE | 86675.8 ms | 84072.6 ms | 2603.2 ms | 60519.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 81590.0 ms | 78816.4 ms | 2773.6 ms | 52826.5 ms |
| Gorm_schema | LLGoDeadcodeDrop | 77629.2 ms | 74832.1 ms | 2797.1 ms | 27732.5 ms |
| Toml | LLGoFullLTOGlobalDCE | 76786.3 ms | 74273.6 ms | 2512.7 ms | 50056.5 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 75992.6 ms | 73431.4 ms | 2561.2 ms | 49051.8 ms |
| Gorm_schema | LLGoNoLTO | 70516.4 ms | 68195.2 ms | 2321.1 ms | 24929.4 ms |
| Toml | LLGoNoLTO | 68809.3 ms | 66495.7 ms | 2313.6 ms | 24170.7 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 67672.0 ms | 65825.6 ms | 1846.4 ms | 49670.0 ms |
| Toml | LLGoDeadcodeDrop | 66784.4 ms | 64497.3 ms | 2287.1 ms | 23554.6 ms |
| IXGo | Go | 57917.3 ms | 47888.1 ms | 10029.3 ms | 16271.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 52415.1 ms | 50533.8 ms | 1881.2 ms | 34133.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 50256.3 ms | 48514.7 ms | 1741.6 ms | 32828.1 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 48210.2 ms | 46513.7 ms | 1696.5 ms | 18505.0 ms |
| Dustin_humanize | LLGoNoLTO | 46440.1 ms | 44868.0 ms | 1572.1 ms | 17951.3 ms |
| Etcdctl | Go | 25405.3 ms | 21585.4 ms | 3819.8 ms | 7793.4 ms |
| XGo | Go | 13195.5 ms | 11103.5 ms | 2092.0 ms | 3945.3 ms |
| Aws_restjson | Go | 6115.3 ms | 5005.1 ms | 1110.2 ms | 2642.0 ms |
| Gorm_schema | Go | 4050.2 ms | 3418.5 ms | 631.7 ms | 1606.9 ms |
| Uber_zap | Go | 3722.5 ms | 3079.1 ms | 643.5 ms | 1519.6 ms |
| K8s_workqueue | Go | 3696.9 ms | 2991.5 ms | 705.5 ms | 2007.7 ms |
| Toml | Go | 1360.4 ms | 1082.3 ms | 278.1 ms | 658.3 ms |
| Dustin_humanize | Go | 561.6 ms | 441.4 ms | 120.2 ms | 289.8 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1860957.8 ms | 1329189.3 ms | 9 |
| LLGoFullLTOGlobalDCE | 1822962.7 ms | 1258827.5 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1806077.2 ms | 1226605.6 ms | 9 |
| LLGoNoLTO | 1188930.4 ms | 401444.9 ms | 9 |
| LLGoDeadcodeDrop | 1165176.0 ms | 399761.6 ms | 9 |
| Go | 116025.0 ms | 36734.4 ms | 9 |

Dependency download details are in `download-timings.log`.
