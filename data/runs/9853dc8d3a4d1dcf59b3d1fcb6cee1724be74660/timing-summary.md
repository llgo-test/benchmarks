## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 584669.5 ms | 567884.3 ms | 16785.2 ms | 320956.0 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 545086.1 ms | 532300.4 ms | 12785.7 ms | 284642.7 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 516108.9 ms | 504149.0 ms | 11959.9 ms | 275566.0 ms |
| IXGo | LLGoDeadcodeDrop | 445042.1 ms | 434512.7 ms | 10529.4 ms | 131733.9 ms |
| IXGo | LLGoNoLTO | 410906.9 ms | 400813.6 ms | 10093.2 ms | 123042.6 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 265881.7 ms | 260937.8 ms | 4944.0 ms | 163144.3 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 265016.2 ms | 260113.3 ms | 4902.9 ms | 164549.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 263248.9 ms | 258406.6 ms | 4842.3 ms | 161632.8 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 214470.1 ms | 211248.5 ms | 3221.6 ms | 125701.4 ms |
| Aws_restjson | LLGoDeadcodeDrop | 210423.4 ms | 207407.0 ms | 3016.3 ms | 75177.2 ms |
| Aws_restjson | LLGoNoLTO | 208008.0 ms | 204942.0 ms | 3066.0 ms | 74413.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 202110.2 ms | 198864.9 ms | 3245.3 ms | 112809.3 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 199779.1 ms | 196638.4 ms | 3140.7 ms | 112272.4 ms |
| Etcdctl | LLGoDeadcodeDrop | 197100.0 ms | 192893.1 ms | 4206.9 ms | 65776.5 ms |
| Etcdctl | LLGoNoLTO | 193578.9 ms | 189338.9 ms | 4240.0 ms | 64533.6 ms |
| XGo | LLGoFullLTONoGlobalDCE | 185995.5 ms | 182603.0 ms | 3392.5 ms | 128827.1 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 185037.3 ms | 181562.0 ms | 3475.4 ms | 126914.3 ms |
| XGo | LLGoFullLTOGlobalDCE | 183193.6 ms | 179787.6 ms | 3406.1 ms | 126009.6 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 174095.3 ms | 171355.5 ms | 2739.8 ms | 108583.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 173133.9 ms | 170193.3 ms | 2940.6 ms | 108644.2 ms |
| Uber_zap | LLGoNoLTO | 172431.8 ms | 169923.7 ms | 2508.1 ms | 66236.0 ms |
| Uber_zap | LLGoDeadcodeDrop | 172329.7 ms | 169817.8 ms | 2511.9 ms | 65906.1 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 170687.2 ms | 167815.3 ms | 2871.8 ms | 107096.4 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 168446.6 ms | 165865.2 ms | 2581.4 ms | 64734.8 ms |
| K8s_workqueue | LLGoNoLTO | 166813.6 ms | 164348.8 ms | 2464.8 ms | 64135.9 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 164570.9 ms | 161666.1 ms | 2904.8 ms | 98754.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 164044.9 ms | 161259.0 ms | 2785.9 ms | 98254.8 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 156486.3 ms | 153593.3 ms | 2893.0 ms | 92954.5 ms |
| XGo | LLGoDeadcodeDrop | 114514.4 ms | 111455.9 ms | 3058.5 ms | 42928.0 ms |
| XGo | LLGoNoLTO | 111697.8 ms | 108752.7 ms | 2945.0 ms | 42109.2 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 89293.6 ms | 87530.3 ms | 1763.4 ms | 52393.6 ms |
| Gorm_schema | LLGoNoLTO | 88522.1 ms | 86917.6 ms | 1604.5 ms | 29307.2 ms |
| Gorm_schema | LLGoDeadcodeDrop | 88452.7 ms | 86812.0 ms | 1640.8 ms | 29517.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 86949.9 ms | 85312.1 ms | 1637.7 ms | 50307.0 ms |
| IXGo | Go | 86140.5 ms | 80757.4 ms | 5383.1 ms | 24570.6 ms |
| Toml | LLGoDeadcodeDrop | 83679.9 ms | 82009.3 ms | 1670.6 ms | 27406.1 ms |
| Toml | LLGoNoLTO | 83045.6 ms | 81426.6 ms | 1619.0 ms | 27347.0 ms |
| Toml | LLGoFullLTONoGlobalDCE | 80677.1 ms | 78939.4 ms | 1737.8 ms | 46694.1 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 78560.9 ms | 76863.0 ms | 1697.9 ms | 41242.6 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 74705.1 ms | 72929.8 ms | 1775.3 ms | 39621.9 ms |
| Toml | LLGoFullLTOGlobalDCE | 73248.1 ms | 71520.8 ms | 1727.3 ms | 38771.2 ms |
| Dustin_humanize | LLGoNoLTO | 56767.4 ms | 55648.4 ms | 1119.0 ms | 20316.6 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 56675.2 ms | 55579.5 ms | 1095.7 ms | 20217.2 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 56669.6 ms | 55359.6 ms | 1310.0 ms | 34811.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 48826.3 ms | 47619.2 ms | 1207.1 ms | 26337.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 47178.5 ms | 46075.1 ms | 1103.4 ms | 25468.8 ms |
| Etcdctl | Go | 34300.4 ms | 32122.9 ms | 2177.5 ms | 10565.6 ms |
| XGo | Go | 19298.0 ms | 17935.0 ms | 1363.1 ms | 6099.9 ms |
| Aws_restjson | Go | 8159.6 ms | 7339.7 ms | 819.8 ms | 3709.1 ms |
| Gorm_schema | Go | 5930.2 ms | 5414.0 ms | 516.2 ms | 2599.7 ms |
| Uber_zap | Go | 5356.5 ms | 4891.3 ms | 465.2 ms | 2100.9 ms |
| K8s_workqueue | Go | 4944.8 ms | 4307.3 ms | 637.5 ms | 2293.9 ms |
| Toml | Go | 2085.3 ms | 1836.4 ms | 248.9 ms | 955.4 ms |
| Dustin_humanize | Go | 831.0 ms | 662.5 ms | 168.5 ms | 416.1 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTOGlobalDCE | 1775446.5 ms | 1042316.9 ms | 9 |
| LLGoFullLTONoGlobalDCE | 1753013.5 ms | 1044222.9 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1721265.0 ms | 986421.3 ms | 9 |
| LLGoDeadcodeDrop | 1536663.9 ms | 523397.2 ms | 9 |
| LLGoNoLTO | 1491772.1 ms | 511441.3 ms | 9 |
| Go | 167046.4 ms | 53311.0 ms | 9 |

Dependency download details are in `download-timings.log`.
