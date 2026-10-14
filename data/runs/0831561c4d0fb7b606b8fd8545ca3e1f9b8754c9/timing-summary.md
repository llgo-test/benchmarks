## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 703756.6 ms | 693278.4 ms | 10478.2 ms | 351154.7 ms |
| IXGo | LLGoFullLTOGlobalDCE | 653774.4 ms | 643494.4 ms | 10279.9 ms | 336968.3 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 632281.6 ms | 621098.0 ms | 11183.6 ms | 329773.2 ms |
| IXGo | LLGoDeadcodeDrop | 535789.0 ms | 520870.8 ms | 14918.2 ms | 156599.3 ms |
| IXGo | LLGoNoLTO | 488632.8 ms | 479320.1 ms | 9312.8 ms | 140674.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 302052.4 ms | 297177.9 ms | 4874.5 ms | 187857.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 301453.3 ms | 296593.6 ms | 4859.7 ms | 186656.9 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 293927.6 ms | 289172.0 ms | 4755.6 ms | 185413.4 ms |
| Aws_restjson | LLGoNoLTO | 239548.4 ms | 236610.8 ms | 2937.6 ms | 82019.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 239088.9 ms | 235701.3 ms | 3387.7 ms | 130067.1 ms |
| Aws_restjson | LLGoDeadcodeDrop | 238899.5 ms | 235428.7 ms | 3470.7 ms | 82442.8 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 237813.8 ms | 234578.1 ms | 3235.7 ms | 140973.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 231440.2 ms | 228159.3 ms | 3280.9 ms | 126449.9 ms |
| Etcdctl | LLGoDeadcodeDrop | 218245.2 ms | 213371.6 ms | 4873.6 ms | 71886.8 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 216447.3 ms | 212954.9 ms | 3492.4 ms | 152370.0 ms |
| XGo | LLGoFullLTONoGlobalDCE | 215884.2 ms | 212439.4 ms | 3444.7 ms | 154344.1 ms |
| Etcdctl | LLGoNoLTO | 214788.7 ms | 210372.5 ms | 4416.2 ms | 70276.7 ms |
| XGo | LLGoFullLTOGlobalDCE | 207608.0 ms | 204291.2 ms | 3316.8 ms | 145899.1 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 197534.5 ms | 194744.5 ms | 2790.0 ms | 123677.8 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 196790.5 ms | 193714.6 ms | 3075.9 ms | 124585.4 ms |
| Uber_zap | LLGoNoLTO | 196176.0 ms | 193567.9 ms | 2608.1 ms | 71350.2 ms |
| Uber_zap | LLGoDeadcodeDrop | 195694.9 ms | 192781.5 ms | 2913.4 ms | 72060.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 193928.5 ms | 191003.9 ms | 2924.6 ms | 120548.9 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 191229.6 ms | 188428.4 ms | 2801.3 ms | 113164.1 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 191085.8 ms | 188172.9 ms | 2912.8 ms | 70534.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 189434.0 ms | 186683.8 ms | 2750.2 ms | 111951.4 ms |
| K8s_workqueue | LLGoNoLTO | 186993.7 ms | 184446.5 ms | 2547.2 ms | 68089.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 178426.0 ms | 175669.9 ms | 2756.1 ms | 104030.8 ms |
| XGo | LLGoNoLTO | 124446.6 ms | 121685.2 ms | 2761.4 ms | 44672.9 ms |
| XGo | LLGoDeadcodeDrop | 124421.5 ms | 121009.1 ms | 3412.4 ms | 45528.5 ms |
| Gorm_schema | LLGoDeadcodeDrop | 103443.2 ms | 101661.2 ms | 1782.1 ms | 34039.2 ms |
| Gorm_schema | LLGoNoLTO | 103103.3 ms | 101449.5 ms | 1653.8 ms | 33537.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 103051.9 ms | 101162.8 ms | 1889.1 ms | 60439.5 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 102740.9 ms | 100961.1 ms | 1779.7 ms | 60504.4 ms |
| Toml | LLGoDeadcodeDrop | 97642.9 ms | 95709.2 ms | 1933.7 ms | 32007.5 ms |
| Toml | LLGoNoLTO | 96859.8 ms | 95159.8 ms | 1700.0 ms | 31265.8 ms |
| Toml | LLGoFullLTONoGlobalDCE | 96187.6 ms | 94219.8 ms | 1967.7 ms | 55930.1 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 90283.7 ms | 88595.8 ms | 1687.9 ms | 47556.5 ms |
| Toml | LLGoFullLTOGlobalDCE | 88362.0 ms | 86518.1 ms | 1843.9 ms | 47652.4 ms |
| IXGo | Go | 86868.9 ms | 81402.2 ms | 5466.7 ms | 25135.0 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 86119.0 ms | 84237.8 ms | 1881.2 ms | 46096.5 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 67008.1 ms | 65684.4 ms | 1323.6 ms | 23776.6 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 66821.4 ms | 65494.0 ms | 1327.4 ms | 41266.2 ms |
| Dustin_humanize | LLGoNoLTO | 66514.9 ms | 65380.8 ms | 1134.1 ms | 23435.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 57883.1 ms | 56593.2 ms | 1289.9 ms | 31703.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 56512.9 ms | 55272.0 ms | 1241.0 ms | 30743.0 ms |
| Etcdctl | Go | 33761.6 ms | 31702.3 ms | 2059.3 ms | 10499.9 ms |
| XGo | Go | 19155.1 ms | 17957.1 ms | 1198.0 ms | 5643.0 ms |
| Aws_restjson | Go | 7849.4 ms | 7129.7 ms | 719.7 ms | 3154.7 ms |
| Gorm_schema | Go | 5835.7 ms | 5446.2 ms | 389.6 ms | 2210.0 ms |
| Uber_zap | Go | 5317.4 ms | 4924.7 ms | 392.8 ms | 2071.6 ms |
| K8s_workqueue | Go | 4814.3 ms | 4324.2 ms | 490.1 ms | 1717.1 ms |
| Toml | Go | 2031.7 ms | 1817.5 ms | 214.2 ms | 931.2 ms |
| Dustin_humanize | Go | 819.4 ms | 666.9 ms | 152.5 ms | 390.1 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTOGlobalDCEPlugin | 2056267.8 ms | 1159422.5 ms | 9 |
| LLGoFullLTONoGlobalDCE | 2039982.0 ms | 1216468.2 ms | 9 |
| LLGoFullLTOGlobalDCE | 2034584.1 ms | 1171887.4 ms | 9 |
| LLGoDeadcodeDrop | 1772230.0 ms | 588874.8 ms | 9 |
| LLGoNoLTO | 1717064.2 ms | 565322.8 ms | 9 |
| Go | 166453.5 ms | 51752.7 ms | 9 |

Dependency download details are in `download-timings.log`.
