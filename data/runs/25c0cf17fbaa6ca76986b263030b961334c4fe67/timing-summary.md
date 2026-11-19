## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 901373.3 ms | 874123.1 ms | 27250.2 ms | 576831.4 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 862402.8 ms | 836469.9 ms | 25932.9 ms | 552411.8 ms |
| IXGo | LLGoFullLTOGlobalDCE | 846683.9 ms | 820333.6 ms | 26350.3 ms | 546576.4 ms |
| IXGo | LLGoDeadcodeDrop | 531251.7 ms | 503120.7 ms | 28131.1 ms | 170652.7 ms |
| IXGo | LLGoNoLTO | 508502.2 ms | 485448.2 ms | 23054.0 ms | 159779.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 454490.2 ms | 442328.4 ms | 12161.8 ms | 323271.4 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 452745.3 ms | 440904.4 ms | 11840.9 ms | 325358.6 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 449522.7 ms | 437293.9 ms | 12228.8 ms | 323969.1 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 345083.4 ms | 338182.5 ms | 6900.9 ms | 227719.4 ms |
| XGo | LLGoFullLTONoGlobalDCE | 325114.6 ms | 316606.1 ms | 8508.5 ms | 255874.0 ms |
| XGo | LLGoFullLTOGlobalDCE | 303923.5 ms | 295422.6 ms | 8500.9 ms | 229767.0 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 303738.5 ms | 295624.5 ms | 8114.0 ms | 229189.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 298855.2 ms | 292229.2 ms | 6626.0 ms | 189018.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 280794.9 ms | 274472.8 ms | 6322.2 ms | 176473.7 ms |
| Aws_restjson | LLGoDeadcodeDrop | 271174.3 ms | 264512.2 ms | 6662.1 ms | 86825.9 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 270811.3 ms | 265015.8 ms | 5795.5 ms | 186090.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 270603.1 ms | 264719.9 ms | 5883.2 ms | 187180.6 ms |
| Aws_restjson | LLGoNoLTO | 269401.0 ms | 263116.0 ms | 6285.1 ms | 84008.2 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 262447.1 ms | 256625.3 ms | 5821.9 ms | 181284.3 ms |
| Etcdctl | LLGoDeadcodeDrop | 259874.9 ms | 248778.8 ms | 11096.2 ms | 89606.5 ms |
| Etcdctl | LLGoNoLTO | 255202.9 ms | 245448.1 ms | 9754.8 ms | 87684.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 254849.6 ms | 249056.4 ms | 5793.1 ms | 167889.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 252543.6 ms | 246778.6 ms | 5765.0 ms | 164961.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 226949.5 ms | 221439.5 ms | 5510.0 ms | 146659.6 ms |
| Uber_zap | LLGoDeadcodeDrop | 221629.1 ms | 216163.3 ms | 5465.8 ms | 72100.5 ms |
| Uber_zap | LLGoNoLTO | 215197.0 ms | 210075.1 ms | 5121.8 ms | 68738.3 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 209367.6 ms | 203832.3 ms | 5535.4 ms | 68954.3 ms |
| K8s_workqueue | LLGoNoLTO | 209269.5 ms | 204156.4 ms | 5113.1 ms | 66884.3 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 161174.2 ms | 157131.2 ms | 4043.0 ms | 110613.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 154137.2 ms | 150087.3 ms | 4049.9 ms | 103908.5 ms |
| Toml | LLGoFullLTONoGlobalDCE | 151297.1 ms | 147398.6 ms | 3898.5 ms | 102415.9 ms |
| XGo | LLGoNoLTO | 143165.4 ms | 136875.2 ms | 6290.2 ms | 52070.2 ms |
| XGo | LLGoDeadcodeDrop | 143021.6 ms | 135438.2 ms | 7583.4 ms | 51771.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 133145.0 ms | 129416.6 ms | 3728.5 ms | 82059.1 ms |
| Toml | LLGoFullLTOGlobalDCE | 131894.6 ms | 128059.1 ms | 3835.5 ms | 83075.3 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 130586.3 ms | 127074.5 ms | 3511.7 ms | 82096.4 ms |
| Gorm_schema | LLGoDeadcodeDrop | 122289.1 ms | 118681.9 ms | 3607.2 ms | 42663.1 ms |
| Gorm_schema | LLGoNoLTO | 119973.4 ms | 116784.7 ms | 3188.7 ms | 41213.6 ms |
| Toml | LLGoDeadcodeDrop | 111966.7 ms | 108689.9 ms | 3276.9 ms | 38387.7 ms |
| Toml | LLGoNoLTO | 111705.4 ms | 108645.1 ms | 3060.4 ms | 37969.5 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 107765.8 ms | 105179.2 ms | 2586.6 ms | 76498.7 ms |
| IXGo | Go | 97511.4 ms | 82572.6 ms | 14938.8 ms | 26683.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 86059.1 ms | 83592.2 ms | 2466.9 ms | 54765.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 84851.7 ms | 82551.0 ms | 2300.7 ms | 54114.7 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 75825.3 ms | 73626.4 ms | 2198.9 ms | 28293.5 ms |
| Dustin_humanize | LLGoNoLTO | 75718.7 ms | 73665.8 ms | 2052.9 ms | 27839.8 ms |
| Etcdctl | Go | 38546.6 ms | 33112.3 ms | 5434.3 ms | 11674.7 ms |
| XGo | Go | 22575.4 ms | 19390.3 ms | 3185.1 ms | 6827.8 ms |
| Aws_restjson | Go | 9099.9 ms | 7631.2 ms | 1468.8 ms | 3674.0 ms |
| Gorm_schema | Go | 6699.0 ms | 5710.2 ms | 988.8 ms | 2636.1 ms |
| Uber_zap | Go | 6186.6 ms | 5260.6 ms | 926.0 ms | 2604.5 ms |
| K8s_workqueue | Go | 5455.1 ms | 4520.6 ms | 934.6 ms | 1963.6 ms |
| Toml | Go | 2247.8 ms | 1862.0 ms | 385.8 ms | 1065.9 ms |
| Dustin_humanize | Go | 908.8 ms | 684.9 ms | 223.9 ms | 446.9 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2938841.5 ms | 2018266.5 ms | 9 |
| LLGoFullLTOGlobalDCE | 2800289.0 ms | 1884801.5 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2764712.9 ms | 1837005.8 ms | 9 |
| LLGoDeadcodeDrop | 1946400.5 ms | 649256.0 ms | 9 |
| LLGoNoLTO | 1908135.6 ms | 626187.1 ms | 9 |
| Go | 189230.7 ms | 57576.6 ms | 9 |

Dependency download details are in `download-timings.log`.
