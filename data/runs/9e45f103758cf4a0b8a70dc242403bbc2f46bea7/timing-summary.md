## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 661820.2 ms | 645158.3 ms | 16661.8 ms | 440180.3 ms |
| IXGo | LLGoFullLTOGlobalDCE | 626598.8 ms | 610014.2 ms | 16584.6 ms | 413876.8 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 594482.2 ms | 579480.3 ms | 15002.0 ms | 396118.5 ms |
| IXGo | LLGoDeadcodeDrop | 360700.7 ms | 344714.4 ms | 15986.2 ms | 117748.7 ms |
| IXGo | LLGoNoLTO | 337325.2 ms | 323989.2 ms | 13336.0 ms | 106140.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 328824.4 ms | 321543.1 ms | 7281.3 ms | 245638.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 328234.5 ms | 321071.5 ms | 7162.9 ms | 244219.7 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 317536.0 ms | 310591.7 ms | 6944.3 ms | 238012.0 ms |
| XGo | LLGoFullLTONoGlobalDCE | 239947.8 ms | 234953.4 ms | 4994.4 ms | 193960.6 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 239322.3 ms | 235078.4 ms | 4244.0 ms | 165495.2 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 206687.9 ms | 202157.0 ms | 4530.9 ms | 159412.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 202951.0 ms | 199018.6 ms | 3932.3 ms | 132276.5 ms |
| XGo | LLGoFullLTOGlobalDCE | 202467.6 ms | 197747.6 ms | 4720.0 ms | 156139.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 197048.3 ms | 193148.5 ms | 3899.8 ms | 127716.7 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 196859.4 ms | 193112.8 ms | 3746.6 ms | 142436.0 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 183864.2 ms | 180251.4 ms | 3612.8 ms | 132636.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 182024.2 ms | 178630.5 ms | 3393.7 ms | 131721.4 ms |
| Aws_restjson | LLGoDeadcodeDrop | 179976.7 ms | 176095.8 ms | 3880.9 ms | 57863.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 178701.1 ms | 175014.5 ms | 3686.7 ms | 123867.5 ms |
| Aws_restjson | LLGoNoLTO | 175223.3 ms | 171703.5 ms | 3519.8 ms | 55167.4 ms |
| Etcdctl | LLGoDeadcodeDrop | 170882.9 ms | 164695.9 ms | 6187.0 ms | 59972.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 165467.6 ms | 162126.1 ms | 3341.4 ms | 112703.5 ms |
| Etcdctl | LLGoNoLTO | 164050.2 ms | 158498.6 ms | 5551.7 ms | 56707.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 150282.2 ms | 147113.6 ms | 3168.7 ms | 100019.8 ms |
| Uber_zap | LLGoDeadcodeDrop | 142645.9 ms | 139452.2 ms | 3193.7 ms | 47289.8 ms |
| Uber_zap | LLGoNoLTO | 142398.9 ms | 139408.4 ms | 2990.5 ms | 45940.0 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 137355.1 ms | 134154.7 ms | 3200.4 ms | 45796.8 ms |
| K8s_workqueue | LLGoNoLTO | 136090.7 ms | 133273.8 ms | 2816.9 ms | 43769.6 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 110628.2 ms | 108156.8 ms | 2471.3 ms | 79074.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 106745.2 ms | 104184.7 ms | 2560.5 ms | 74776.5 ms |
| Toml | LLGoFullLTONoGlobalDCE | 101984.6 ms | 99716.3 ms | 2268.2 ms | 72172.1 ms |
| XGo | LLGoNoLTO | 94817.6 ms | 91102.7 ms | 3714.9 ms | 35151.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 92869.4 ms | 90520.3 ms | 2349.1 ms | 59775.6 ms |
| XGo | LLGoDeadcodeDrop | 91503.4 ms | 87451.0 ms | 4052.4 ms | 34060.1 ms |
| Toml | LLGoFullLTOGlobalDCE | 88937.3 ms | 86774.8 ms | 2162.5 ms | 58644.5 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 88673.2 ms | 86630.1 ms | 2043.1 ms | 58357.8 ms |
| Gorm_schema | LLGoDeadcodeDrop | 78200.6 ms | 76124.5 ms | 2076.1 ms | 27618.9 ms |
| Gorm_schema | LLGoNoLTO | 77394.5 ms | 75386.4 ms | 2008.1 ms | 27066.5 ms |
| Toml | LLGoDeadcodeDrop | 75138.8 ms | 73158.3 ms | 1980.6 ms | 26540.0 ms |
| Toml | LLGoNoLTO | 71446.7 ms | 69711.2 ms | 1735.6 ms | 24758.5 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 69717.1 ms | 68240.6 ms | 1476.6 ms | 51006.0 ms |
| IXGo | Go | 61948.9 ms | 53997.3 ms | 7951.6 ms | 17222.5 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 56249.5 ms | 54819.1 ms | 1430.3 ms | 37235.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 53709.7 ms | 52309.1 ms | 1400.6 ms | 35163.6 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 50997.4 ms | 49684.4 ms | 1313.0 ms | 19393.2 ms |
| Dustin_humanize | LLGoNoLTO | 50192.8 ms | 49002.7 ms | 1190.1 ms | 18937.5 ms |
| Etcdctl | Go | 24672.8 ms | 21926.5 ms | 2746.3 ms | 7478.4 ms |
| XGo | Go | 14374.7 ms | 12639.6 ms | 1735.1 ms | 4296.5 ms |
| Aws_restjson | Go | 5976.9 ms | 5156.7 ms | 820.2 ms | 2435.5 ms |
| Gorm_schema | Go | 4296.2 ms | 3821.2 ms | 474.9 ms | 1652.5 ms |
| Uber_zap | Go | 4005.7 ms | 3544.2 ms | 461.6 ms | 1587.4 ms |
| K8s_workqueue | Go | 3488.3 ms | 3011.2 ms | 477.1 ms | 1249.6 ms |
| Toml | Go | 1495.5 ms | 1304.1 ms | 191.4 ms | 686.0 ms |
| Dustin_humanize | Go | 630.9 ms | 504.8 ms | 126.1 ms | 390.8 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2054341.7 ms | 1470910.6 ms | 9 |
| LLGoFullLTOGlobalDCE | 1972909.2 ms | 1372757.4 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1945382.7 ms | 1338967.8 ms | 9 |
| LLGoDeadcodeDrop | 1287401.7 ms | 436283.5 ms | 9 |
| LLGoNoLTO | 1248939.9 ms | 413638.7 ms | 9 |
| Go | 120890.0 ms | 36999.3 ms | 9 |

Dependency download details are in `download-timings.log`.
