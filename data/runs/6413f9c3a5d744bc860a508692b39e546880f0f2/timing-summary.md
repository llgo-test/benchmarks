## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 547095.0 ms | 529321.2 ms | 17773.8 ms | 359517.0 ms |
| IXGo | LLGoFullLTOGlobalDCE | 540338.2 ms | 522548.5 ms | 17789.6 ms | 354249.9 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 534421.6 ms | 516998.9 ms | 17422.7 ms | 354368.4 ms |
| IXGo | LLGoDeadcodeDrop | 311077.1 ms | 293651.9 ms | 17425.2 ms | 100731.8 ms |
| IXGo | LLGoNoLTO | 304197.5 ms | 289367.2 ms | 14830.3 ms | 94171.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 278349.5 ms | 269683.2 ms | 8666.4 ms | 208879.6 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 276075.2 ms | 267951.1 ms | 8124.1 ms | 208639.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 274806.0 ms | 266369.7 ms | 8436.2 ms | 205627.1 ms |
| XGo | LLGoFullLTONoGlobalDCE | 206918.5 ms | 200808.3 ms | 6110.2 ms | 169695.5 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 197857.9 ms | 192893.8 ms | 4964.1 ms | 141279.3 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 181163.4 ms | 175594.7 ms | 5568.7 ms | 143500.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 180415.0 ms | 175600.7 ms | 4814.3 ms | 122003.2 ms |
| XGo | LLGoFullLTOGlobalDCE | 180119.5 ms | 174517.8 ms | 5601.8 ms | 142444.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 179080.8 ms | 174220.3 ms | 4860.6 ms | 121567.6 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 167258.7 ms | 162956.3 ms | 4302.4 ms | 124202.1 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 163908.1 ms | 159693.2 ms | 4214.9 ms | 122496.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 163140.5 ms | 158862.0 ms | 4278.5 ms | 121040.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 152398.9 ms | 148212.0 ms | 4186.9 ms | 108353.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 151156.9 ms | 146867.9 ms | 4288.9 ms | 107216.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 141364.6 ms | 137341.9 ms | 4022.7 ms | 99361.5 ms |
| Aws_restjson | LLGoDeadcodeDrop | 140756.2 ms | 136646.3 ms | 4109.9 ms | 50142.4 ms |
| Aws_restjson | LLGoNoLTO | 140705.2 ms | 136793.7 ms | 3911.5 ms | 50088.4 ms |
| Etcdctl | LLGoDeadcodeDrop | 138750.8 ms | 131381.1 ms | 7369.8 ms | 50811.2 ms |
| Etcdctl | LLGoNoLTO | 136078.6 ms | 129854.4 ms | 6224.2 ms | 48964.9 ms |
| Uber_zap | LLGoNoLTO | 115617.4 ms | 112518.1 ms | 3099.3 ms | 44014.1 ms |
| Uber_zap | LLGoDeadcodeDrop | 114897.7 ms | 111310.7 ms | 3587.0 ms | 43714.9 ms |
| K8s_workqueue | LLGoNoLTO | 111218.7 ms | 107989.0 ms | 3229.7 ms | 42662.7 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 110633.8 ms | 107130.5 ms | 3503.3 ms | 42508.6 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 87008.8 ms | 84336.6 ms | 2672.2 ms | 63169.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 86595.5 ms | 83936.7 ms | 2658.8 ms | 62034.6 ms |
| Toml | LLGoFullLTONoGlobalDCE | 78997.5 ms | 76565.2 ms | 2432.3 ms | 56458.0 ms |
| XGo | LLGoDeadcodeDrop | 78193.9 ms | 73430.4 ms | 4763.5 ms | 31436.4 ms |
| XGo | LLGoNoLTO | 77944.6 ms | 73851.4 ms | 4093.2 ms | 30689.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 70149.0 ms | 67608.2 ms | 2540.8 ms | 45800.1 ms |
| Toml | LLGoFullLTOGlobalDCE | 67499.1 ms | 65197.1 ms | 2301.9 ms | 44842.7 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 67373.7 ms | 65138.1 ms | 2235.6 ms | 44437.9 ms |
| Gorm_schema | LLGoDeadcodeDrop | 61743.2 ms | 59352.7 ms | 2390.5 ms | 21510.6 ms |
| Gorm_schema | LLGoNoLTO | 60519.3 ms | 58329.7 ms | 2189.6 ms | 20762.3 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 57150.4 ms | 55408.5 ms | 1741.8 ms | 42825.2 ms |
| Toml | LLGoDeadcodeDrop | 56651.5 ms | 54693.2 ms | 1958.3 ms | 19495.1 ms |
| Toml | LLGoNoLTO | 56408.8 ms | 54525.4 ms | 1883.4 ms | 19186.5 ms |
| IXGo | Go | 55328.8 ms | 45571.2 ms | 9757.6 ms | 15280.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 44464.7 ms | 42925.1 ms | 1539.5 ms | 29706.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 43916.7 ms | 42348.4 ms | 1568.3 ms | 29295.0 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 39414.8 ms | 37989.7 ms | 1425.0 ms | 14680.3 ms |
| Dustin_humanize | LLGoNoLTO | 39050.2 ms | 37701.0 ms | 1349.3 ms | 14483.8 ms |
| Etcdctl | Go | 22097.9 ms | 18665.9 ms | 3432.1 ms | 6907.9 ms |
| XGo | Go | 12896.0 ms | 10866.5 ms | 2029.5 ms | 3815.7 ms |
| Aws_restjson | Go | 5259.5 ms | 4287.0 ms | 972.5 ms | 2336.7 ms |
| Gorm_schema | Go | 3767.7 ms | 3142.6 ms | 625.0 ms | 1479.9 ms |
| Uber_zap | Go | 3430.9 ms | 2825.5 ms | 605.4 ms | 1423.1 ms |
| K8s_workqueue | Go | 3090.5 ms | 2507.6 ms | 582.9 ms | 1141.9 ms |
| Toml | Go | 1325.1 ms | 1060.6 ms | 264.5 ms | 648.1 ms |
| Dustin_humanize | Go | 641.2 ms | 433.8 ms | 207.3 ms | 307.5 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1769596.7 ms | 1283133.9 ms | 9 |
| LLGoFullLTOGlobalDCE | 1687987.4 ms | 1188754.4 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1661439.5 ms | 1161124.2 ms | 9 |
| LLGoDeadcodeDrop | 1052119.0 ms | 375031.4 ms | 9 |
| LLGoNoLTO | 1041740.3 ms | 365023.6 ms | 9 |
| Go | 107837.6 ms | 33341.4 ms | 9 |

Dependency download details are in `download-timings.log`.
