## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 677033.3 ms | 653551.7 ms | 23481.6 ms | 454013.2 ms |
| IXGo | LLGoFullLTOGlobalDCE | 654851.5 ms | 631892.9 ms | 22958.6 ms | 431779.0 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 637329.9 ms | 614676.1 ms | 22653.7 ms | 420384.3 ms |
| IXGo | LLGoDeadcodeDrop | 384216.2 ms | 360759.3 ms | 23457.0 ms | 125411.5 ms |
| IXGo | LLGoNoLTO | 364000.1 ms | 344265.7 ms | 19734.4 ms | 114571.5 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 356267.4 ms | 345248.2 ms | 11019.2 ms | 263558.5 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 354034.7 ms | 342871.9 ms | 11162.8 ms | 259508.5 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 348391.2 ms | 337743.2 ms | 10648.0 ms | 256679.9 ms |
| XGo | LLGoFullLTONoGlobalDCE | 250202.8 ms | 242828.3 ms | 7374.5 ms | 201348.3 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 238039.0 ms | 231851.4 ms | 6187.5 ms | 163652.7 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 226824.7 ms | 219577.9 ms | 7246.8 ms | 174733.0 ms |
| XGo | LLGoFullLTOGlobalDCE | 220231.7 ms | 213027.0 ms | 7204.7 ms | 168941.3 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 218230.2 ms | 212244.1 ms | 5986.2 ms | 140893.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 214595.9 ms | 208512.3 ms | 6083.6 ms | 139265.8 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 204019.0 ms | 198696.1 ms | 5323.0 ms | 144929.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 201810.9 ms | 196576.4 ms | 5234.5 ms | 144608.2 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 195700.7 ms | 190598.4 ms | 5102.3 ms | 139768.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 188650.9 ms | 183572.4 ms | 5078.5 ms | 126634.3 ms |
| Aws_restjson | LLGoNoLTO | 187506.4 ms | 182070.9 ms | 5435.5 ms | 59658.1 ms |
| Aws_restjson | LLGoDeadcodeDrop | 184964.2 ms | 179295.2 ms | 5669.1 ms | 60560.0 ms |
| Etcdctl | LLGoNoLTO | 182551.6 ms | 174038.8 ms | 8512.8 ms | 63775.6 ms |
| Etcdctl | LLGoDeadcodeDrop | 182450.4 ms | 172964.9 ms | 9485.5 ms | 65742.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 182351.8 ms | 177217.2 ms | 5134.6 ms | 122323.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 164533.8 ms | 159806.2 ms | 4727.6 ms | 108731.4 ms |
| Uber_zap | LLGoDeadcodeDrop | 155475.2 ms | 150721.0 ms | 4754.3 ms | 51571.8 ms |
| Uber_zap | LLGoNoLTO | 155456.6 ms | 151008.5 ms | 4448.1 ms | 50622.8 ms |
| K8s_workqueue | LLGoNoLTO | 150706.1 ms | 146359.4 ms | 4346.7 ms | 48874.4 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 147479.6 ms | 142823.0 ms | 4656.6 ms | 49359.9 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 116944.9 ms | 113446.6 ms | 3498.2 ms | 82664.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 113028.9 ms | 109556.9 ms | 3472.0 ms | 78439.8 ms |
| Toml | LLGoFullLTONoGlobalDCE | 107499.4 ms | 104153.6 ms | 3345.7 ms | 74581.6 ms |
| XGo | LLGoNoLTO | 105068.3 ms | 99407.6 ms | 5660.8 ms | 39549.4 ms |
| XGo | LLGoDeadcodeDrop | 104353.8 ms | 98038.4 ms | 6315.4 ms | 38905.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 98437.3 ms | 95020.9 ms | 3416.3 ms | 62573.2 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 94558.2 ms | 91442.3 ms | 3116.0 ms | 61058.2 ms |
| Toml | LLGoFullLTOGlobalDCE | 93947.4 ms | 90820.0 ms | 3127.4 ms | 60704.4 ms |
| Gorm_schema | LLGoDeadcodeDrop | 85567.8 ms | 82294.2 ms | 3273.6 ms | 30747.1 ms |
| Gorm_schema | LLGoNoLTO | 84123.5 ms | 81108.1 ms | 3015.4 ms | 29954.0 ms |
| Toml | LLGoDeadcodeDrop | 82202.8 ms | 79229.5 ms | 2973.3 ms | 28984.5 ms |
| Toml | LLGoNoLTO | 79486.3 ms | 76888.3 ms | 2598.0 ms | 27732.7 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 75683.6 ms | 73387.3 ms | 2296.2 ms | 54895.0 ms |
| IXGo | Go | 73517.3 ms | 60828.0 ms | 12689.4 ms | 20615.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 61332.3 ms | 59251.2 ms | 2081.2 ms | 39944.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 60437.3 ms | 58263.1 ms | 2174.2 ms | 39252.9 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 55778.7 ms | 53765.7 ms | 2013.0 ms | 21458.1 ms |
| Dustin_humanize | LLGoNoLTO | 54231.4 ms | 52410.6 ms | 1820.8 ms | 20610.0 ms |
| Etcdctl | Go | 28954.2 ms | 24384.6 ms | 4569.6 ms | 8784.6 ms |
| XGo | Go | 16256.3 ms | 13601.6 ms | 2654.6 ms | 4870.2 ms |
| Aws_restjson | Go | 6847.0 ms | 5500.0 ms | 1347.0 ms | 2874.2 ms |
| Gorm_schema | Go | 4878.9 ms | 4042.3 ms | 836.6 ms | 2150.6 ms |
| Uber_zap | Go | 4579.0 ms | 3759.3 ms | 819.6 ms | 2230.8 ms |
| K8s_workqueue | Go | 4093.5 ms | 3329.1 ms | 764.4 ms | 1488.9 ms |
| Toml | Go | 1713.7 ms | 1378.6 ms | 335.1 ms | 828.6 ms |
| Dustin_humanize | Go | 701.2 ms | 524.1 ms | 177.1 ms | 344.0 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2181686.6 ms | 1545783.1 ms | 9 |
| LLGoFullLTOGlobalDCE | 2099580.0 ms | 1447932.8 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2073701.9 ms | 1422150.7 ms | 9 |
| LLGoDeadcodeDrop | 1382488.7 ms | 472741.0 ms | 9 |
| LLGoNoLTO | 1363130.3 ms | 455348.5 ms | 9 |
| Go | 141541.1 ms | 44187.6 ms | 9 |

Dependency download details are in `download-timings.log`.
