## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 654407.7 ms | 644503.0 ms | 9904.7 ms | 338926.8 ms |
| IXGo | LLGoFullLTOGlobalDCE | 653941.6 ms | 642333.1 ms | 11608.5 ms | 338264.4 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 652058.3 ms | 641934.8 ms | 10123.5 ms | 339310.3 ms |
| IXGo | LLGoDeadcodeDrop | 529165.8 ms | 514887.0 ms | 14278.8 ms | 157763.2 ms |
| IXGo | LLGoNoLTO | 508294.7 ms | 499495.7 ms | 8799.0 ms | 148715.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 342729.7 ms | 337488.0 ms | 5241.7 ms | 200342.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 338777.6 ms | 333598.8 ms | 5178.8 ms | 197852.0 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 338492.7 ms | 333388.9 ms | 5103.8 ms | 199786.1 ms |
| Aws_restjson | LLGoDeadcodeDrop | 268331.4 ms | 264765.1 ms | 3566.3 ms | 89490.9 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 268056.2 ms | 264084.2 ms | 3972.0 ms | 148768.2 ms |
| Aws_restjson | LLGoNoLTO | 264461.5 ms | 261107.4 ms | 3354.1 ms | 89221.7 ms |
| Etcdctl | LLGoDeadcodeDrop | 260546.8 ms | 254804.1 ms | 5742.7 ms | 86520.6 ms |
| Etcdctl | LLGoNoLTO | 259713.9 ms | 255028.3 ms | 4685.6 ms | 84796.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 255457.9 ms | 251594.5 ms | 3863.4 ms | 133637.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 254767.8 ms | 250912.8 ms | 3855.0 ms | 133590.3 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 245039.0 ms | 241642.0 ms | 3397.1 ms | 159542.5 ms |
| XGo | LLGoFullLTOGlobalDCE | 244427.2 ms | 241061.7 ms | 3365.6 ms | 159033.0 ms |
| XGo | LLGoFullLTONoGlobalDCE | 243752.7 ms | 240282.2 ms | 3470.5 ms | 159739.5 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 232655.1 ms | 229317.8 ms | 3337.3 ms | 133007.1 ms |
| Uber_zap | LLGoDeadcodeDrop | 228894.8 ms | 225952.9 ms | 2942.0 ms | 80543.0 ms |
| Uber_zap | LLGoNoLTO | 226578.2 ms | 223786.0 ms | 2792.2 ms | 79637.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 225972.0 ms | 222673.6 ms | 3298.4 ms | 129034.3 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 225339.5 ms | 221751.1 ms | 3588.4 ms | 129858.5 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 221454.8 ms | 218423.3 ms | 3031.6 ms | 77881.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 221377.5 ms | 217963.1 ms | 3414.5 ms | 120279.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 219500.6 ms | 216090.4 ms | 3410.1 ms | 119924.3 ms |
| K8s_workqueue | LLGoNoLTO | 218235.2 ms | 215183.5 ms | 3051.7 ms | 77004.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 210599.4 ms | 207191.3 ms | 3408.1 ms | 112749.7 ms |
| XGo | LLGoDeadcodeDrop | 160924.2 ms | 157197.5 ms | 3726.7 ms | 58993.8 ms |
| XGo | LLGoNoLTO | 158516.3 ms | 155871.3 ms | 2645.0 ms | 57312.6 ms |
| Gorm_schema | LLGoDeadcodeDrop | 108517.3 ms | 106787.7 ms | 1729.6 ms | 35894.7 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 107606.9 ms | 105573.0 ms | 2034.0 ms | 62548.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 107102.2 ms | 105074.4 ms | 2027.8 ms | 61441.7 ms |
| Gorm_schema | LLGoNoLTO | 107049.1 ms | 105329.0 ms | 1720.1 ms | 35440.2 ms |
| Toml | LLGoDeadcodeDrop | 102155.5 ms | 100204.7 ms | 1950.7 ms | 33677.5 ms |
| Toml | LLGoNoLTO | 100961.1 ms | 99197.4 ms | 1763.7 ms | 33471.4 ms |
| Toml | LLGoFullLTONoGlobalDCE | 99291.0 ms | 97260.9 ms | 2030.1 ms | 56870.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 96181.8 ms | 94214.3 ms | 1967.5 ms | 49572.3 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 91083.1 ms | 89013.4 ms | 2069.7 ms | 47453.9 ms |
| Toml | LLGoFullLTOGlobalDCE | 90604.1 ms | 88594.8 ms | 2009.4 ms | 47492.0 ms |
| IXGo | Go | 83854.6 ms | 78766.3 ms | 5088.3 ms | 23087.9 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 71937.7 ms | 70641.8 ms | 1295.9 ms | 25588.2 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 70466.2 ms | 69084.1 ms | 1382.2 ms | 42529.1 ms |
| Dustin_humanize | LLGoNoLTO | 70162.7 ms | 68921.3 ms | 1241.4 ms | 24990.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 60806.8 ms | 59450.8 ms | 1355.9 ms | 32640.9 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 60714.7 ms | 59374.3 ms | 1340.4 ms | 32390.8 ms |
| Etcdctl | Go | 33368.3 ms | 31378.8 ms | 1989.5 ms | 10010.2 ms |
| XGo | Go | 19052.0 ms | 17877.6 ms | 1174.4 ms | 5581.1 ms |
| Aws_restjson | Go | 7980.9 ms | 7220.8 ms | 760.1 ms | 3592.1 ms |
| Gorm_schema | Go | 5742.0 ms | 5372.1 ms | 369.9 ms | 2289.1 ms |
| Uber_zap | Go | 5291.7 ms | 4898.5 ms | 393.2 ms | 2050.0 ms |
| K8s_workqueue | Go | 4713.7 ms | 4251.9 ms | 461.8 ms | 1671.9 ms |
| Toml | Go | 2079.9 ms | 1830.1 ms | 249.7 ms | 1095.6 ms |
| Dustin_humanize | Go | 823.7 ms | 675.2 ms | 148.5 ms | 379.1 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2237718.7 ms | 1272417.5 ms | 9 |
| LLGoFullLTOGlobalDCE | 2196498.0 ms | 1219070.2 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2176992.9 ms | 1195097.9 ms | 9 |
| LLGoDeadcodeDrop | 1951928.3 ms | 646353.3 ms | 9 |
| LLGoNoLTO | 1913972.7 ms | 630589.3 ms | 9 |
| Go | 162906.8 ms | 49757.0 ms | 9 |

Dependency download details are in `download-timings.log`.
