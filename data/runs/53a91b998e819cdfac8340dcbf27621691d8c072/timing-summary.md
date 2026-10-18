## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 638287.4 ms | 627483.1 ms | 10804.3 ms | 319825.8 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 629272.5 ms | 619237.6 ms | 10034.9 ms | 327140.0 ms |
| IXGo | LLGoFullLTOGlobalDCE | 613543.7 ms | 604625.0 ms | 8918.7 ms | 303791.0 ms |
| IXGo | LLGoDeadcodeDrop | 508847.3 ms | 497181.6 ms | 11665.6 ms | 153855.7 ms |
| IXGo | LLGoNoLTO | 469026.3 ms | 460413.8 ms | 8612.5 ms | 140751.6 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 244490.2 ms | 239952.1 ms | 4538.1 ms | 157865.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 237407.6 ms | 233017.3 ms | 4390.3 ms | 152804.8 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 237155.5 ms | 232701.2 ms | 4454.3 ms | 154224.1 ms |
| Aws_restjson | LLGoNoLTO | 201997.8 ms | 199302.2 ms | 2695.6 ms | 66539.3 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 201477.7 ms | 198525.9 ms | 2951.8 ms | 118847.3 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 193286.8 ms | 190262.6 ms | 3024.2 ms | 107533.1 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 193269.3 ms | 190248.9 ms | 3020.4 ms | 106559.3 ms |
| Aws_restjson | LLGoDeadcodeDrop | 193033.5 ms | 189947.7 ms | 3085.8 ms | 65583.0 ms |
| XGo | LLGoFullLTOGlobalDCE | 174159.4 ms | 170911.4 ms | 3248.0 ms | 126988.8 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 170810.3 ms | 167719.2 ms | 3091.0 ms | 124121.6 ms |
| XGo | LLGoFullLTONoGlobalDCE | 166100.4 ms | 163044.6 ms | 3055.8 ms | 121298.8 ms |
| Etcdctl | LLGoDeadcodeDrop | 164992.9 ms | 160326.6 ms | 4666.3 ms | 55922.1 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 163629.5 ms | 161014.0 ms | 2615.5 ms | 106110.6 ms |
| Etcdctl | LLGoNoLTO | 162094.5 ms | 158375.3 ms | 3719.1 ms | 53684.5 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 155726.0 ms | 153072.3 ms | 2653.7 ms | 101191.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 153282.3 ms | 150610.1 ms | 2672.2 ms | 98729.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 151058.6 ms | 148404.9 ms | 2653.6 ms | 92413.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 148415.9 ms | 145809.8 ms | 2606.0 ms | 91606.8 ms |
| Uber_zap | LLGoDeadcodeDrop | 148027.3 ms | 145289.2 ms | 2738.1 ms | 56445.7 ms |
| Uber_zap | LLGoNoLTO | 146747.9 ms | 144453.0 ms | 2294.9 ms | 55269.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 145946.6 ms | 143199.0 ms | 2747.6 ms | 90381.1 ms |
| K8s_workqueue | LLGoNoLTO | 144650.0 ms | 142138.8 ms | 2511.1 ms | 54334.2 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 141158.2 ms | 138430.6 ms | 2727.6 ms | 53673.1 ms |
| XGo | LLGoDeadcodeDrop | 96899.6 ms | 93621.8 ms | 3277.8 ms | 36781.3 ms |
| XGo | LLGoNoLTO | 93428.3 ms | 91005.0 ms | 2423.3 ms | 34589.0 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 82459.8 ms | 80745.4 ms | 1714.4 ms | 50999.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 81067.3 ms | 79323.5 ms | 1743.8 ms | 49249.8 ms |
| Gorm_schema | LLGoNoLTO | 80040.6 ms | 78503.5 ms | 1537.1 ms | 26589.8 ms |
| Gorm_schema | LLGoDeadcodeDrop | 78255.3 ms | 76448.3 ms | 1807.0 ms | 26336.6 ms |
| Toml | LLGoNoLTO | 73758.9 ms | 72186.3 ms | 1572.6 ms | 24269.0 ms |
| Toml | LLGoFullLTONoGlobalDCE | 73575.6 ms | 71836.1 ms | 1739.6 ms | 44521.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 71910.8 ms | 70275.1 ms | 1635.6 ms | 39471.0 ms |
| Toml | LLGoDeadcodeDrop | 71762.9 ms | 70047.6 ms | 1715.3 ms | 24181.4 ms |
| Toml | LLGoFullLTOGlobalDCE | 69958.3 ms | 68308.6 ms | 1649.7 ms | 39325.6 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 66453.5 ms | 64717.7 ms | 1735.8 ms | 36807.4 ms |
| IXGo | Go | 64920.7 ms | 60587.6 ms | 4333.1 ms | 19323.4 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 53675.2 ms | 52428.9 ms | 1246.3 ms | 34596.1 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 50718.8 ms | 49504.0 ms | 1214.7 ms | 18651.5 ms |
| Dustin_humanize | LLGoNoLTO | 49511.3 ms | 48393.1 ms | 1118.3 ms | 17901.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 46520.3 ms | 45313.7 ms | 1206.6 ms | 26785.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 43390.3 ms | 42214.3 ms | 1176.0 ms | 24763.0 ms |
| Etcdctl | Go | 25918.5 ms | 24116.6 ms | 1802.0 ms | 8385.9 ms |
| XGo | Go | 14447.4 ms | 13431.4 ms | 1016.1 ms | 4352.5 ms |
| Aws_restjson | Go | 6257.9 ms | 5660.7 ms | 597.2 ms | 3072.8 ms |
| Gorm_schema | Go | 4329.7 ms | 4001.1 ms | 328.6 ms | 1686.1 ms |
| Uber_zap | Go | 4118.3 ms | 3772.8 ms | 345.5 ms | 1655.5 ms |
| K8s_workqueue | Go | 3608.2 ms | 3205.0 ms | 403.1 ms | 1697.6 ms |
| Toml | Go | 1624.4 ms | 1427.4 ms | 196.9 ms | 786.5 ms |
| Dustin_humanize | Go | 619.5 ms | 512.1 ms | 107.3 ms | 304.5 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1763072.3 ms | 1058928.9 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1721681.9 ms | 990143.8 ms | 9 |
| LLGoFullLTOGlobalDCE | 1721576.7 ms | 998879.6 ms | 9 |
| LLGoDeadcodeDrop | 1453695.7 ms | 491430.2 ms | 9 |
| LLGoNoLTO | 1421255.6 ms | 473928.5 ms | 9 |
| Go | 125844.6 ms | 41264.8 ms | 9 |

Dependency download details are in `download-timings.log`.
