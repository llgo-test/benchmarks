## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 547217.5 ms | 533658.8 ms | 13558.7 ms | 289723.5 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 520878.8 ms | 509515.5 ms | 11363.3 ms | 273554.3 ms |
| IXGo | LLGoFullLTOGlobalDCE | 519639.7 ms | 507552.6 ms | 12087.1 ms | 275331.2 ms |
| IXGo | LLGoDeadcodeDrop | 435147.8 ms | 425115.1 ms | 10032.7 ms | 129776.1 ms |
| IXGo | LLGoNoLTO | 403935.8 ms | 394183.7 ms | 9752.1 ms | 121007.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 291478.6 ms | 286350.9 ms | 5127.8 ms | 167807.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 291261.7 ms | 285742.2 ms | 5519.5 ms | 167440.9 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 285228.5 ms | 280495.1 ms | 4733.4 ms | 165179.9 ms |
| Etcdctl | LLGoDeadcodeDrop | 224221.6 ms | 219855.7 ms | 4365.9 ms | 72715.4 ms |
| Etcdctl | LLGoNoLTO | 223962.0 ms | 219513.1 ms | 4448.9 ms | 73112.1 ms |
| XGo | LLGoFullLTONoGlobalDCE | 187737.7 ms | 184373.4 ms | 3364.3 ms | 130053.0 ms |
| XGo | LLGoFullLTOGlobalDCE | 185654.6 ms | 182172.1 ms | 3482.5 ms | 127025.6 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 180443.2 ms | 177213.5 ms | 3229.7 ms | 124243.6 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 159661.7 ms | 157486.3 ms | 2175.4 ms | 122276.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 145511.9 ms | 143217.7 ms | 2294.3 ms | 106908.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 145450.5 ms | 143194.1 ms | 2256.5 ms | 107120.5 ms |
| Aws_restjson | LLGoDeadcodeDrop | 127859.7 ms | 125598.0 ms | 2261.7 ms | 82769.0 ms |
| XGo | LLGoDeadcodeDrop | 114248.0 ms | 111417.3 ms | 2830.7 ms | 43752.0 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 111274.6 ms | 109507.4 ms | 1767.3 ms | 84067.2 ms |
| XGo | LLGoNoLTO | 110782.3 ms | 107938.6 ms | 2843.7 ms | 41807.7 ms |
| Aws_restjson | LLGoNoLTO | 104872.8 ms | 102918.9 ms | 1954.0 ms | 60646.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 104333.3 ms | 102543.3 ms | 1790.0 ms | 80566.7 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 103291.8 ms | 101414.9 ms | 1876.9 ms | 80530.2 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 99630.9 ms | 97910.9 ms | 1720.0 ms | 72265.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 99003.6 ms | 97258.3 ms | 1745.3 ms | 72251.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 90798.5 ms | 89002.8 ms | 1795.6 ms | 66452.7 ms |
| IXGo | Go | 85022.5 ms | 79536.9 ms | 5485.6 ms | 23380.5 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 63313.3 ms | 61955.8 ms | 1357.5 ms | 43186.7 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 62770.9 ms | 61296.5 ms | 1474.4 ms | 42198.2 ms |
| Uber_zap | LLGoDeadcodeDrop | 60545.9 ms | 59091.4 ms | 1454.5 ms | 27010.7 ms |
| Uber_zap | LLGoNoLTO | 58920.2 ms | 57429.9 ms | 1490.2 ms | 26500.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 52979.0 ms | 51597.6 ms | 1381.5 ms | 31815.4 ms |
| K8s_workqueue | LLGoNoLTO | 52336.0 ms | 50835.6 ms | 1500.4 ms | 24379.7 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 52072.0 ms | 50422.9 ms | 1649.1 ms | 24488.5 ms |
| Toml | LLGoFullLTONoGlobalDCE | 48384.6 ms | 47340.9 ms | 1043.7 ms | 36127.6 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 42853.1 ms | 41676.7 ms | 1176.5 ms | 29644.3 ms |
| Toml | LLGoFullLTOGlobalDCE | 41470.7 ms | 40435.3 ms | 1035.5 ms | 28970.2 ms |
| Gorm_schema | LLGoNoLTO | 40598.5 ms | 39366.3 ms | 1232.2 ms | 13462.9 ms |
| Gorm_schema | LLGoDeadcodeDrop | 40544.2 ms | 39318.3 ms | 1225.9 ms | 13658.7 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 34258.8 ms | 33366.9 ms | 892.0 ms | 26705.6 ms |
| Etcdctl | Go | 33032.5 ms | 31077.8 ms | 1954.7 ms | 10154.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 26074.5 ms | 25188.0 ms | 886.5 ms | 18349.5 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 25462.0 ms | 24589.8 ms | 872.2 ms | 17934.6 ms |
| Toml | LLGoDeadcodeDrop | 24830.9 ms | 23816.2 ms | 1014.6 ms | 9290.6 ms |
| Toml | LLGoNoLTO | 24103.1 ms | 23184.0 ms | 919.1 ms | 9044.6 ms |
| XGo | Go | 19671.1 ms | 18174.0 ms | 1497.0 ms | 6251.9 ms |
| Dustin_humanize | LLGoNoLTO | 14045.4 ms | 13300.6 ms | 744.9 ms | 5917.9 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 13731.5 ms | 13022.7 ms | 708.8 ms | 5841.3 ms |
| Aws_restjson | Go | 8973.3 ms | 7994.4 ms | 978.9 ms | 4387.0 ms |
| Gorm_schema | Go | 5793.9 ms | 5366.6 ms | 427.4 ms | 2224.3 ms |
| Uber_zap | Go | 5686.6 ms | 5200.5 ms | 486.0 ms | 2302.8 ms |
| K8s_workqueue | Go | 4731.9 ms | 4255.8 ms | 476.1 ms | 1673.7 ms |
| Toml | Go | 2086.8 ms | 1853.3 ms | 233.5 ms | 1090.2 ms |
| Dustin_humanize | Go | 815.0 ms | 647.3 ms | 167.8 ms | 384.4 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1514029.9 ms | 961681.3 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1476770.4 ms | 906843.5 ms | 9 |
| LLGoFullLTOGlobalDCE | 1475264.0 ms | 919206.3 ms | 9 |
| LLGoDeadcodeDrop | 1093201.6 ms | 409302.6 ms | 9 |
| LLGoNoLTO | 1033556.2 ms | 375879.5 ms | 9 |
| Go | 165813.4 ms | 51849.1 ms | 9 |

Dependency download details are in `download-timings.log`.
