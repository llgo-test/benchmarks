## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 717209.7 ms | 693134.3 ms | 24075.4 ms | 467346.5 ms |
| IXGo | LLGoFullLTOGlobalDCE | 671580.7 ms | 648130.8 ms | 23449.9 ms | 445617.9 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 641536.8 ms | 618047.2 ms | 23489.6 ms | 429292.9 ms |
| IXGo | LLGoDeadcodeDrop | 372745.7 ms | 349200.9 ms | 23544.8 ms | 125813.5 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 367759.5 ms | 356741.5 ms | 11018.0 ms | 274413.9 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 361329.3 ms | 350279.0 ms | 11050.3 ms | 270371.0 ms |
| IXGo | LLGoNoLTO | 358154.2 ms | 338628.9 ms | 19525.3 ms | 113678.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 355340.7 ms | 344361.3 ms | 10979.3 ms | 263340.9 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 267932.2 ms | 261266.9 ms | 6665.4 ms | 185312.0 ms |
| XGo | LLGoFullLTONoGlobalDCE | 266951.8 ms | 259229.9 ms | 7721.9 ms | 216590.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 244821.6 ms | 238414.7 ms | 6406.9 ms | 158331.9 ms |
| XGo | LLGoFullLTOGlobalDCE | 243579.7 ms | 236043.9 ms | 7535.8 ms | 191840.1 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 240061.1 ms | 233434.4 ms | 6626.7 ms | 155962.9 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 234974.1 ms | 227753.9 ms | 7220.2 ms | 183559.6 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 227424.2 ms | 221717.8 ms | 5706.3 ms | 161515.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 216440.7 ms | 210751.5 ms | 5689.2 ms | 153876.3 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 215701.8 ms | 210105.5 ms | 5596.2 ms | 153622.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 213263.0 ms | 207465.7 ms | 5797.3 ms | 146151.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 205352.8 ms | 199792.9 ms | 5559.9 ms | 138908.3 ms |
| Aws_restjson | LLGoNoLTO | 199169.4 ms | 194108.0 ms | 5061.4 ms | 62276.4 ms |
| Aws_restjson | LLGoDeadcodeDrop | 191680.5 ms | 186012.6 ms | 5667.9 ms | 63638.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 188636.9 ms | 183081.5 ms | 5555.4 ms | 126269.3 ms |
| Etcdctl | LLGoDeadcodeDrop | 181322.7 ms | 172076.4 ms | 9246.3 ms | 63912.7 ms |
| Etcdctl | LLGoNoLTO | 178179.1 ms | 169629.5 ms | 8549.6 ms | 62005.4 ms |
| Uber_zap | LLGoDeadcodeDrop | 151843.0 ms | 147242.8 ms | 4600.3 ms | 50821.3 ms |
| Uber_zap | LLGoNoLTO | 151087.5 ms | 146684.0 ms | 4403.5 ms | 48804.0 ms |
| K8s_workqueue | LLGoNoLTO | 146990.1 ms | 142584.7 ms | 4405.4 ms | 48059.7 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 146383.5 ms | 141787.5 ms | 4595.9 ms | 48858.8 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 117644.8 ms | 113993.4 ms | 3651.4 ms | 82172.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 112684.2 ms | 109184.7 ms | 3499.5 ms | 77899.5 ms |
| Toml | LLGoFullLTONoGlobalDCE | 108620.8 ms | 105244.6 ms | 3376.2 ms | 74839.4 ms |
| XGo | LLGoDeadcodeDrop | 103043.5 ms | 96679.0 ms | 6364.5 ms | 38525.6 ms |
| XGo | LLGoNoLTO | 101306.8 ms | 95839.7 ms | 5467.1 ms | 38054.6 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 95169.6 ms | 91953.7 ms | 3215.9 ms | 61606.3 ms |
| Toml | LLGoFullLTOGlobalDCE | 95006.6 ms | 91850.0 ms | 3156.5 ms | 61250.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 94914.4 ms | 91588.2 ms | 3326.2 ms | 59665.5 ms |
| Gorm_schema | LLGoDeadcodeDrop | 85075.7 ms | 81789.4 ms | 3286.4 ms | 30258.3 ms |
| Gorm_schema | LLGoNoLTO | 82385.3 ms | 79574.2 ms | 2811.1 ms | 28990.8 ms |
| Toml | LLGoNoLTO | 78436.1 ms | 75840.9 ms | 2595.1 ms | 27232.8 ms |
| Toml | LLGoDeadcodeDrop | 78138.9 ms | 75502.9 ms | 2636.0 ms | 27428.3 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 73986.1 ms | 71672.1 ms | 2314.1 ms | 53267.3 ms |
| IXGo | Go | 71940.1 ms | 59340.6 ms | 12599.5 ms | 22526.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 60901.2 ms | 58783.8 ms | 2117.4 ms | 39340.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 59670.5 ms | 57571.7 ms | 2098.8 ms | 38737.2 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 53794.1 ms | 51835.8 ms | 1958.3 ms | 20455.9 ms |
| Dustin_humanize | LLGoNoLTO | 52537.2 ms | 50783.9 ms | 1753.3 ms | 19940.5 ms |
| Etcdctl | Go | 28351.5 ms | 23839.5 ms | 4512.0 ms | 8716.8 ms |
| XGo | Go | 16531.1 ms | 13865.5 ms | 2665.6 ms | 4853.0 ms |
| Aws_restjson | Go | 7052.6 ms | 5716.6 ms | 1336.1 ms | 2980.5 ms |
| Gorm_schema | Go | 4893.2 ms | 4104.4 ms | 788.8 ms | 2175.1 ms |
| Uber_zap | Go | 4487.0 ms | 3764.5 ms | 722.5 ms | 1840.8 ms |
| K8s_workqueue | Go | 4025.5 ms | 3222.4 ms | 803.0 ms | 3078.9 ms |
| Toml | Go | 1724.2 ms | 1395.2 ms | 329.0 ms | 829.3 ms |
| Dustin_humanize | Go | 688.2 ms | 497.8 ms | 190.4 ms | 342.6 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2281127.8 ms | 1626983.0 ms | 9 |
| LLGoFullLTOGlobalDCE | 2213618.2 ms | 1537648.7 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2203748.6 ms | 1506469.6 ms | 9 |
| LLGoDeadcodeDrop | 1364027.6 ms | 469713.1 ms | 9 |
| LLGoNoLTO | 1348245.6 ms | 449043.0 ms | 9 |
| Go | 139693.3 ms | 47343.4 ms | 9 |

Dependency download details are in `download-timings.log`.
