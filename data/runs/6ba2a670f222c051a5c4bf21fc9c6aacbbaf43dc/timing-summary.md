## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 667510.0 ms | 651053.6 ms | 16456.3 ms | 442576.5 ms |
| IXGo | LLGoFullLTOGlobalDCE | 653341.9 ms | 636841.8 ms | 16500.1 ms | 434399.5 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 647321.1 ms | 630753.7 ms | 16567.4 ms | 434489.9 ms |
| IXGo | LLGoDeadcodeDrop | 375330.1 ms | 359251.1 ms | 16079.0 ms | 120948.6 ms |
| IXGo | LLGoNoLTO | 351018.9 ms | 337429.9 ms | 13589.0 ms | 110300.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 347969.8 ms | 340271.2 ms | 7698.5 ms | 259783.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 345973.3 ms | 338666.1 ms | 7307.2 ms | 259395.7 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 343289.8 ms | 336019.4 ms | 7270.3 ms | 258628.4 ms |
| XGo | LLGoFullLTONoGlobalDCE | 245686.5 ms | 240748.7 ms | 4937.7 ms | 199037.4 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 232057.3 ms | 227736.1 ms | 4321.2 ms | 159711.3 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 228972.7 ms | 223973.1 ms | 4999.6 ms | 178014.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 215721.6 ms | 211675.2 ms | 4046.3 ms | 140347.1 ms |
| XGo | LLGoFullLTOGlobalDCE | 214697.8 ms | 209906.0 ms | 4791.8 ms | 166623.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 210525.2 ms | 206395.5 ms | 4129.7 ms | 135188.3 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 197876.1 ms | 194110.2 ms | 3765.9 ms | 142230.5 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 192109.2 ms | 188434.5 ms | 3674.7 ms | 138261.3 ms |
| Aws_restjson | LLGoNoLTO | 191227.4 ms | 187534.5 ms | 3692.9 ms | 59502.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 188122.8 ms | 184501.1 ms | 3621.7 ms | 135619.7 ms |
| Aws_restjson | LLGoDeadcodeDrop | 181620.9 ms | 177792.2 ms | 3828.7 ms | 58552.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 181405.0 ms | 177830.1 ms | 3574.9 ms | 124829.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 176871.0 ms | 173313.9 ms | 3557.1 ms | 120902.8 ms |
| Etcdctl | LLGoDeadcodeDrop | 175531.1 ms | 169251.7 ms | 6279.4 ms | 61431.7 ms |
| Etcdctl | LLGoNoLTO | 172951.6 ms | 167280.9 ms | 5670.7 ms | 59765.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 164021.8 ms | 160752.0 ms | 3269.9 ms | 110211.7 ms |
| Uber_zap | LLGoNoLTO | 151685.6 ms | 148446.7 ms | 3238.9 ms | 48904.1 ms |
| Uber_zap | LLGoDeadcodeDrop | 145806.1 ms | 142614.6 ms | 3191.5 ms | 48229.3 ms |
| K8s_workqueue | LLGoNoLTO | 143981.4 ms | 140879.8 ms | 3101.5 ms | 46459.0 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 141654.6 ms | 138352.5 ms | 3302.1 ms | 47478.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 115867.2 ms | 113255.5 ms | 2611.7 ms | 81785.0 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 112684.9 ms | 110226.2 ms | 2458.6 ms | 79838.2 ms |
| Toml | LLGoFullLTONoGlobalDCE | 105247.7 ms | 102891.0 ms | 2356.6 ms | 74377.6 ms |
| XGo | LLGoNoLTO | 99712.8 ms | 96015.7 ms | 3697.1 ms | 36880.9 ms |
| XGo | LLGoDeadcodeDrop | 98611.6 ms | 94287.0 ms | 4324.6 ms | 36421.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 94186.7 ms | 91873.6 ms | 2313.0 ms | 60954.5 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 91279.8 ms | 89088.3 ms | 2191.5 ms | 60143.1 ms |
| Toml | LLGoFullLTOGlobalDCE | 90910.1 ms | 88727.1 ms | 2183.1 ms | 59888.0 ms |
| Gorm_schema | LLGoDeadcodeDrop | 82980.5 ms | 80856.7 ms | 2123.8 ms | 29230.5 ms |
| Gorm_schema | LLGoNoLTO | 82570.2 ms | 80466.0 ms | 2104.2 ms | 28646.3 ms |
| Toml | LLGoDeadcodeDrop | 76659.9 ms | 74767.9 ms | 1892.1 ms | 26822.0 ms |
| Toml | LLGoNoLTO | 76230.6 ms | 74455.5 ms | 1775.1 ms | 26515.3 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 75404.2 ms | 73746.3 ms | 1657.8 ms | 55441.3 ms |
| IXGo | Go | 63312.1 ms | 55247.5 ms | 8064.6 ms | 17580.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 59660.6 ms | 58177.7 ms | 1482.9 ms | 39551.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 59069.3 ms | 57515.1 ms | 1554.2 ms | 38786.1 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 53980.0 ms | 52566.4 ms | 1413.6 ms | 20448.1 ms |
| Dustin_humanize | LLGoNoLTO | 51935.4 ms | 50671.7 ms | 1263.7 ms | 19540.6 ms |
| Etcdctl | Go | 25271.8 ms | 22349.6 ms | 2922.2 ms | 7624.4 ms |
| XGo | Go | 14121.3 ms | 12608.8 ms | 1512.5 ms | 4220.7 ms |
| Aws_restjson | Go | 6018.3 ms | 5169.8 ms | 848.6 ms | 2445.0 ms |
| Gorm_schema | Go | 4433.6 ms | 3904.6 ms | 529.0 ms | 1708.6 ms |
| Uber_zap | Go | 4052.8 ms | 3545.0 ms | 507.8 ms | 1602.5 ms |
| K8s_workqueue | Go | 3642.4 ms | 3171.2 ms | 471.2 ms | 1594.3 ms |
| Toml | Go | 1579.8 ms | 1357.6 ms | 222.2 ms | 733.3 ms |
| Dustin_humanize | Go | 599.8 ms | 479.9 ms | 119.9 ms | 291.2 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2151676.6 ms | 1542016.0 ms | 9 |
| LLGoFullLTOGlobalDCE | 2067696.8 ms | 1442827.1 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2038409.8 ms | 1406173.2 ms | 9 |
| LLGoDeadcodeDrop | 1332174.9 ms | 449562.4 ms | 9 |
| LLGoNoLTO | 1321313.9 ms | 436514.5 ms | 9 |
| Go | 123032.0 ms | 37800.4 ms | 9 |

Dependency download details are in `download-timings.log`.
