## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 624216.4 ms | 612285.9 ms | 11930.5 ms | 327176.2 ms |
| IXGo | LLGoFullLTOGlobalDCE | 623496.0 ms | 613371.3 ms | 10124.7 ms | 325546.6 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 600005.7 ms | 589264.6 ms | 10741.1 ms | 320183.8 ms |
| IXGo | LLGoDeadcodeDrop | 481646.6 ms | 469220.2 ms | 12426.5 ms | 142755.5 ms |
| IXGo | LLGoNoLTO | 463195.4 ms | 453206.8 ms | 9988.5 ms | 134069.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 294739.9 ms | 290011.4 ms | 4728.4 ms | 182978.5 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 290241.8 ms | 285793.9 ms | 4447.8 ms | 180894.3 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 289838.2 ms | 285174.5 ms | 4663.7 ms | 182648.4 ms |
| Aws_restjson | LLGoDeadcodeDrop | 230933.8 ms | 227720.5 ms | 3213.3 ms | 79870.6 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 230495.9 ms | 226908.2 ms | 3587.7 ms | 138348.9 ms |
| Aws_restjson | LLGoNoLTO | 228418.4 ms | 225307.5 ms | 3110.9 ms | 78934.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 216150.9 ms | 212597.7 ms | 3553.2 ms | 122771.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 215574.4 ms | 211985.7 ms | 3588.7 ms | 122814.3 ms |
| Etcdctl | LLGoDeadcodeDrop | 214337.0 ms | 209204.6 ms | 5132.4 ms | 70784.7 ms |
| Etcdctl | LLGoNoLTO | 211700.3 ms | 207760.9 ms | 3939.4 ms | 68723.6 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 205546.8 ms | 202411.5 ms | 3135.3 ms | 144513.7 ms |
| XGo | LLGoFullLTONoGlobalDCE | 205049.5 ms | 201892.0 ms | 3157.5 ms | 145332.0 ms |
| XGo | LLGoFullLTOGlobalDCE | 204971.0 ms | 201757.3 ms | 3213.6 ms | 144123.4 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 195278.1 ms | 192255.3 ms | 3022.8 ms | 123055.0 ms |
| Uber_zap | LLGoDeadcodeDrop | 191014.9 ms | 188449.8 ms | 2565.1 ms | 70430.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 188837.3 ms | 185667.8 ms | 3169.5 ms | 118407.5 ms |
| Uber_zap | LLGoNoLTO | 188655.8 ms | 186162.4 ms | 2493.5 ms | 69724.8 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 188642.1 ms | 185429.9 ms | 3212.2 ms | 119455.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 184577.2 ms | 181560.7 ms | 3016.5 ms | 110527.3 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 183821.6 ms | 181082.6 ms | 2739.0 ms | 67838.9 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 183133.9 ms | 180104.5 ms | 3029.4 ms | 109784.2 ms |
| K8s_workqueue | LLGoNoLTO | 181783.3 ms | 178932.7 ms | 2850.6 ms | 67729.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 173712.8 ms | 170413.7 ms | 3299.1 ms | 103412.7 ms |
| XGo | LLGoDeadcodeDrop | 122018.9 ms | 118720.3 ms | 3298.7 ms | 44895.6 ms |
| XGo | LLGoNoLTO | 120444.4 ms | 117940.3 ms | 2504.1 ms | 43676.7 ms |
| Gorm_schema | LLGoDeadcodeDrop | 101591.2 ms | 99878.4 ms | 1712.8 ms | 33373.3 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 99837.6 ms | 97845.4 ms | 1992.1 ms | 59691.6 ms |
| Gorm_schema | LLGoNoLTO | 99750.8 ms | 98066.8 ms | 1684.1 ms | 32666.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 99652.2 ms | 97673.5 ms | 1978.6 ms | 58678.1 ms |
| Toml | LLGoDeadcodeDrop | 95062.2 ms | 93330.1 ms | 1732.1 ms | 31009.9 ms |
| Toml | LLGoNoLTO | 94186.9 ms | 92446.3 ms | 1740.6 ms | 30743.5 ms |
| Toml | LLGoFullLTONoGlobalDCE | 91721.9 ms | 89830.5 ms | 1891.3 ms | 54453.7 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 88980.0 ms | 87040.8 ms | 1939.2 ms | 47110.6 ms |
| IXGo | Go | 83268.6 ms | 78297.2 ms | 4971.4 ms | 23023.5 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 82960.0 ms | 81035.2 ms | 1924.8 ms | 44982.2 ms |
| Toml | LLGoFullLTOGlobalDCE | 82821.6 ms | 80974.8 ms | 1846.7 ms | 45085.2 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 65354.6 ms | 64094.8 ms | 1259.8 ms | 23178.3 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 65197.6 ms | 63795.5 ms | 1402.1 ms | 40617.8 ms |
| Dustin_humanize | LLGoNoLTO | 64547.1 ms | 63337.6 ms | 1209.6 ms | 22877.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 55375.5 ms | 53974.6 ms | 1401.0 ms | 30334.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 55051.2 ms | 53663.4 ms | 1387.9 ms | 30293.8 ms |
| Etcdctl | Go | 33181.6 ms | 31226.1 ms | 1955.6 ms | 9973.3 ms |
| XGo | Go | 18918.3 ms | 17786.0 ms | 1132.3 ms | 5555.6 ms |
| Aws_restjson | Go | 7965.1 ms | 7235.4 ms | 729.6 ms | 3337.3 ms |
| Gorm_schema | Go | 5726.4 ms | 5332.5 ms | 393.9 ms | 2236.3 ms |
| Uber_zap | Go | 5283.4 ms | 4846.3 ms | 437.1 ms | 2015.7 ms |
| K8s_workqueue | Go | 4675.8 ms | 4227.5 ms | 448.3 ms | 1649.5 ms |
| Toml | Go | 1993.7 ms | 1749.7 ms | 244.0 ms | 911.5 ms |
| Dustin_humanize | Go | 807.1 ms | 670.6 ms | 136.5 ms | 380.9 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1966066.5 ms | 1183786.9 ms | 9 |
| LLGoFullLTOGlobalDCE | 1943779.3 ms | 1135627.5 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1926259.4 ms | 1113807.8 ms | 9 |
| LLGoDeadcodeDrop | 1685780.9 ms | 564137.6 ms | 9 |
| LLGoNoLTO | 1652682.4 ms | 549146.5 ms | 9 |
| Go | 161820.0 ms | 49083.6 ms | 9 |

Dependency download details are in `download-timings.log`.
