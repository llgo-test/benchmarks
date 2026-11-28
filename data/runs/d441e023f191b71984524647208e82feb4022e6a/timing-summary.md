## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 700802.6 ms | 683309.4 ms | 17493.2 ms | 464874.0 ms |
| IXGo | LLGoFullLTOGlobalDCE | 673422.1 ms | 656641.9 ms | 16780.2 ms | 449953.0 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 671828.7 ms | 654708.9 ms | 17119.8 ms | 452507.8 ms |
| IXGo | LLGoDeadcodeDrop | 385224.1 ms | 367759.2 ms | 17464.8 ms | 124822.0 ms |
| IXGo | LLGoNoLTO | 371817.9 ms | 357557.7 ms | 14260.2 ms | 115768.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 354958.4 ms | 347319.4 ms | 7638.9 ms | 265152.4 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 350428.8 ms | 342756.7 ms | 7672.1 ms | 261884.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 348210.2 ms | 340721.2 ms | 7489.0 ms | 258992.4 ms |
| XGo | LLGoFullLTONoGlobalDCE | 261155.3 ms | 255849.4 ms | 5306.0 ms | 211139.7 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 250348.3 ms | 245957.9 ms | 4390.4 ms | 171920.3 ms |
| XGo | LLGoFullLTOGlobalDCE | 226925.3 ms | 221923.0 ms | 5002.3 ms | 177024.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 226623.6 ms | 222296.3 ms | 4327.3 ms | 145379.0 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 226231.8 ms | 221179.6 ms | 5052.2 ms | 175602.1 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 226099.6 ms | 221697.1 ms | 4402.5 ms | 146754.6 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 203142.0 ms | 199281.0 ms | 3861.0 ms | 146106.3 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 197241.6 ms | 193532.8 ms | 3708.8 ms | 142007.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 194138.4 ms | 190460.3 ms | 3678.1 ms | 139227.6 ms |
| Aws_restjson | LLGoNoLTO | 191456.9 ms | 187622.3 ms | 3834.5 ms | 60274.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 190889.3 ms | 187106.0 ms | 3783.3 ms | 130394.7 ms |
| Aws_restjson | LLGoDeadcodeDrop | 190261.9 ms | 186164.3 ms | 4097.6 ms | 61216.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 181757.8 ms | 178221.5 ms | 3536.4 ms | 123507.0 ms |
| Etcdctl | LLGoNoLTO | 181259.3 ms | 174973.9 ms | 6285.4 ms | 62188.6 ms |
| Etcdctl | LLGoDeadcodeDrop | 180900.4 ms | 174448.8 ms | 6451.6 ms | 63105.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 166732.9 ms | 163251.1 ms | 3481.8 ms | 110974.6 ms |
| Uber_zap | LLGoNoLTO | 157552.5 ms | 154144.7 ms | 3407.8 ms | 50798.2 ms |
| Uber_zap | LLGoDeadcodeDrop | 154111.8 ms | 150618.0 ms | 3493.8 ms | 50944.7 ms |
| K8s_workqueue | LLGoNoLTO | 147782.6 ms | 144692.4 ms | 3090.2 ms | 47473.0 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 145149.8 ms | 141881.0 ms | 3268.9 ms | 48262.5 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 120438.7 ms | 117813.0 ms | 2625.7 ms | 85156.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 112707.4 ms | 110206.9 ms | 2500.6 ms | 78990.7 ms |
| Toml | LLGoFullLTONoGlobalDCE | 106981.1 ms | 104497.2 ms | 2483.9 ms | 75293.2 ms |
| XGo | LLGoNoLTO | 101053.8 ms | 97167.2 ms | 3886.6 ms | 37036.1 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 98758.5 ms | 96348.4 ms | 2410.1 ms | 62998.3 ms |
| XGo | LLGoDeadcodeDrop | 98159.7 ms | 93960.3 ms | 4199.4 ms | 36113.4 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 97488.3 ms | 95162.8 ms | 2325.5 ms | 63952.6 ms |
| Toml | LLGoFullLTOGlobalDCE | 90000.0 ms | 87773.3 ms | 2226.7 ms | 59124.7 ms |
| Gorm_schema | LLGoNoLTO | 84822.1 ms | 82681.9 ms | 2140.2 ms | 29558.6 ms |
| Gorm_schema | LLGoDeadcodeDrop | 84384.5 ms | 82035.0 ms | 2349.5 ms | 29812.7 ms |
| Toml | LLGoDeadcodeDrop | 80113.5 ms | 78075.5 ms | 2038.0 ms | 28092.5 ms |
| Toml | LLGoNoLTO | 79676.0 ms | 77728.4 ms | 1947.6 ms | 27800.3 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 77182.7 ms | 75454.6 ms | 1728.1 ms | 56497.5 ms |
| IXGo | Go | 64616.7 ms | 56191.4 ms | 8425.3 ms | 18081.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 63212.4 ms | 61611.6 ms | 1600.9 ms | 41368.9 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 59009.9 ms | 57476.7 ms | 1533.2 ms | 38847.0 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 55129.3 ms | 53664.3 ms | 1465.1 ms | 21167.8 ms |
| Dustin_humanize | LLGoNoLTO | 54486.4 ms | 53084.3 ms | 1402.1 ms | 20449.3 ms |
| Etcdctl | Go | 25266.3 ms | 22353.2 ms | 2913.1 ms | 7597.5 ms |
| XGo | Go | 14512.1 ms | 12840.8 ms | 1671.2 ms | 4319.0 ms |
| Aws_restjson | Go | 6146.9 ms | 5304.6 ms | 842.3 ms | 2525.1 ms |
| Gorm_schema | Go | 4514.0 ms | 3940.3 ms | 573.7 ms | 1738.5 ms |
| Uber_zap | Go | 4195.2 ms | 3657.4 ms | 537.8 ms | 1678.6 ms |
| K8s_workqueue | Go | 3585.0 ms | 3087.1 ms | 497.9 ms | 1497.5 ms |
| Toml | Go | 1595.1 ms | 1383.8 ms | 211.3 ms | 740.9 ms |
| Dustin_humanize | Go | 622.8 ms | 515.7 ms | 107.1 ms | 307.2 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2238747.2 ms | 1602513.2 ms | 9 |
| LLGoFullLTOGlobalDCE | 2121402.2 ms | 1479309.5 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2116566.2 ms | 1453808.9 ms | 9 |
| LLGoDeadcodeDrop | 1373435.0 ms | 463537.9 ms | 9 |
| LLGoNoLTO | 1369907.5 ms | 451346.6 ms | 9 |
| Go | 125054.3 ms | 38485.6 ms | 9 |

Dependency download details are in `download-timings.log`.
