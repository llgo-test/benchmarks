## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTONoGlobalDCE | 986691.8 ms | 974387.7 ms | 12304.1 ms | 597054.0 ms |
| IXGo | LLGoFullLTOGlobalDCE | 928763.8 ms | 916032.8 ms | 12731.0 ms | 575601.4 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 850150.9 ms | 837507.1 ms | 12643.8 ms | 547623.8 ms |
| IXGo | LLGoDeadcodeDrop | 598035.3 ms | 583691.7 ms | 14343.6 ms | 183442.3 ms |
| IXGo | LLGoNoLTO | 496468.8 ms | 487091.0 ms | 9377.7 ms | 153022.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 454640.2 ms | 448623.8 ms | 6016.5 ms | 334259.6 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 453279.2 ms | 447092.6 ms | 6186.6 ms | 334784.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 439952.4 ms | 433300.9 ms | 6651.5 ms | 323004.6 ms |
| XGo | LLGoFullLTONoGlobalDCE | 347111.5 ms | 342497.9 ms | 4613.6 ms | 280778.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 326044.0 ms | 322028.4 ms | 4015.6 ms | 210034.3 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 324365.2 ms | 320320.8 ms | 4044.3 ms | 226405.3 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 323134.2 ms | 319073.2 ms | 4060.9 ms | 206200.8 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 310422.4 ms | 305990.0 ms | 4432.4 ms | 242233.7 ms |
| XGo | LLGoFullLTOGlobalDCE | 298520.2 ms | 294427.7 ms | 4092.6 ms | 232965.3 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 293513.3 ms | 289848.0 ms | 3665.3 ms | 213087.1 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 282258.8 ms | 278562.6 ms | 3696.3 ms | 204871.5 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 274184.1 ms | 270631.8 ms | 3552.3 ms | 198993.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 258624.5 ms | 255176.2 ms | 3448.3 ms | 178481.3 ms |
| Aws_restjson | LLGoNoLTO | 257095.7 ms | 253675.8 ms | 3419.8 ms | 89009.7 ms |
| Aws_restjson | LLGoDeadcodeDrop | 253369.1 ms | 249713.3 ms | 3655.8 ms | 88075.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 252967.7 ms | 249567.5 ms | 3400.2 ms | 174510.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 238731.0 ms | 235345.3 ms | 3385.7 ms | 162647.9 ms |
| Etcdctl | LLGoNoLTO | 236012.1 ms | 231472.8 ms | 4539.3 ms | 82508.4 ms |
| Etcdctl | LLGoDeadcodeDrop | 234617.6 ms | 228829.3 ms | 5788.4 ms | 83681.1 ms |
| Uber_zap | LLGoDeadcodeDrop | 206556.7 ms | 203395.8 ms | 3160.9 ms | 77261.7 ms |
| Uber_zap | LLGoNoLTO | 204498.8 ms | 201741.7 ms | 2757.1 ms | 75825.7 ms |
| K8s_workqueue | LLGoNoLTO | 198760.2 ms | 195797.1 ms | 2963.1 ms | 74672.3 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 190173.9 ms | 186976.6 ms | 3197.3 ms | 72142.7 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 145759.7 ms | 143494.0 ms | 2265.7 ms | 103579.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 140800.8 ms | 138646.3 ms | 2154.5 ms | 97677.0 ms |
| XGo | LLGoDeadcodeDrop | 135220.0 ms | 131425.7 ms | 3794.3 ms | 51411.3 ms |
| XGo | LLGoNoLTO | 133674.2 ms | 130697.9 ms | 2976.3 ms | 52050.4 ms |
| Toml | LLGoFullLTONoGlobalDCE | 131707.1 ms | 129332.3 ms | 2374.8 ms | 91945.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 126179.8 ms | 123992.5 ms | 2187.3 ms | 80618.4 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 114838.6 ms | 112729.9 ms | 2108.6 ms | 73831.5 ms |
| Toml | LLGoFullLTOGlobalDCE | 112254.8 ms | 110157.8 ms | 2097.0 ms | 72245.0 ms |
| Gorm_schema | LLGoDeadcodeDrop | 110610.4 ms | 108534.2 ms | 2076.2 ms | 37301.0 ms |
| Gorm_schema | LLGoNoLTO | 107373.8 ms | 105585.6 ms | 1788.1 ms | 35939.4 ms |
| Toml | LLGoDeadcodeDrop | 102338.0 ms | 100311.6 ms | 2026.4 ms | 34273.7 ms |
| Toml | LLGoNoLTO | 100987.7 ms | 99028.5 ms | 1959.2 ms | 33729.3 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 100983.7 ms | 99254.9 ms | 1728.8 ms | 74088.4 ms |
| IXGo | Go | 83508.6 ms | 78514.5 ms | 4994.1 ms | 23050.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 79951.9 ms | 78371.3 ms | 1580.7 ms | 52373.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 74677.8 ms | 73136.0 ms | 1541.8 ms | 48492.1 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 74047.2 ms | 72498.5 ms | 1548.7 ms | 27402.5 ms |
| Dustin_humanize | LLGoNoLTO | 69657.2 ms | 68357.5 ms | 1299.6 ms | 25083.4 ms |
| Etcdctl | Go | 34481.0 ms | 32347.9 ms | 2133.1 ms | 10514.4 ms |
| XGo | Go | 19624.5 ms | 18423.5 ms | 1201.0 ms | 5767.3 ms |
| Aws_restjson | Go | 7971.9 ms | 7315.2 ms | 656.7 ms | 3194.4 ms |
| Gorm_schema | Go | 5848.4 ms | 5349.7 ms | 498.7 ms | 2453.3 ms |
| Uber_zap | Go | 5410.5 ms | 4982.5 ms | 428.0 ms | 2106.5 ms |
| K8s_workqueue | Go | 4887.9 ms | 4373.1 ms | 514.8 ms | 1767.3 ms |
| Toml | Go | 2022.9 ms | 1801.6 ms | 221.3 ms | 934.6 ms |
| Dustin_humanize | Go | 831.0 ms | 682.0 ms | 149.0 ms | 394.9 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 3057595.7 ms | 2120716.2 ms | 9 |
| LLGoFullLTOGlobalDCE | 2881859.1 ms | 1958508.8 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2731054.7 ms | 1859163.2 ms | 9 |
| LLGoDeadcodeDrop | 1904968.2 ms | 654991.8 ms | 9 |
| LLGoNoLTO | 1804528.4 ms | 621840.9 ms | 9 |
| Go | 164586.7 ms | 50183.5 ms | 9 |

Dependency download details are in `download-timings.log`.
