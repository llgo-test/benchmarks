## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 519418.0 ms | 509927.9 ms | 9490.0 ms | 274782.2 ms |
| IXGo | LLGoFullLTOGlobalDCE | 496524.1 ms | 486499.5 ms | 10024.5 ms | 268012.3 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 486773.1 ms | 477241.4 ms | 9531.7 ms | 264738.5 ms |
| IXGo | LLGoNoLTO | 396180.6 ms | 388159.3 ms | 8021.3 ms | 114783.8 ms |
| IXGo | LLGoDeadcodeDrop | 373964.4 ms | 361789.2 ms | 12175.3 ms | 112626.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 230389.1 ms | 225973.9 ms | 4415.3 ms | 148201.1 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 227395.1 ms | 223118.3 ms | 4276.7 ms | 149265.6 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 226436.4 ms | 222199.9 ms | 4236.5 ms | 145286.0 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 179651.3 ms | 176400.8 ms | 3250.5 ms | 111974.5 ms |
| Aws_restjson | LLGoDeadcodeDrop | 177150.8 ms | 174280.9 ms | 2869.9 ms | 63504.9 ms |
| Aws_restjson | LLGoNoLTO | 169770.0 ms | 166995.3 ms | 2774.6 ms | 61600.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 167769.2 ms | 164714.6 ms | 3054.6 ms | 98855.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 166731.2 ms | 163661.3 ms | 3069.9 ms | 98262.3 ms |
| Etcdctl | LLGoDeadcodeDrop | 162700.1 ms | 158234.3 ms | 4465.9 ms | 56018.9 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 161853.2 ms | 158860.7 ms | 2992.5 ms | 117149.3 ms |
| XGo | LLGoFullLTONoGlobalDCE | 161231.8 ms | 158268.5 ms | 2963.3 ms | 117450.5 ms |
| XGo | LLGoFullLTOGlobalDCE | 161203.2 ms | 158163.0 ms | 3040.2 ms | 117107.7 ms |
| Etcdctl | LLGoNoLTO | 160189.1 ms | 156376.4 ms | 3812.6 ms | 54219.0 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 150777.3 ms | 147968.8 ms | 2808.5 ms | 99046.8 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 146833.5 ms | 143955.0 ms | 2878.5 ms | 95431.4 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 145046.6 ms | 142264.1 ms | 2782.5 ms | 95088.5 ms |
| Uber_zap | LLGoDeadcodeDrop | 144338.3 ms | 141930.9 ms | 2407.4 ms | 55570.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 141991.6 ms | 139186.9 ms | 2804.7 ms | 88719.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 140965.4 ms | 138174.4 ms | 2791.0 ms | 87975.4 ms |
| Uber_zap | LLGoNoLTO | 139454.7 ms | 137142.4 ms | 2312.4 ms | 53803.1 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 138751.0 ms | 136288.6 ms | 2462.4 ms | 54105.5 ms |
| K8s_workqueue | LLGoNoLTO | 136787.2 ms | 134315.7 ms | 2471.5 ms | 52954.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 133332.6 ms | 130542.4 ms | 2790.2 ms | 82109.4 ms |
| XGo | LLGoDeadcodeDrop | 93297.1 ms | 90298.1 ms | 2999.1 ms | 36595.3 ms |
| XGo | LLGoNoLTO | 91776.2 ms | 89327.4 ms | 2448.8 ms | 35425.1 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 77303.7 ms | 75437.2 ms | 1866.5 ms | 46869.9 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 75463.7 ms | 73699.0 ms | 1764.8 ms | 46384.9 ms |
| Gorm_schema | LLGoDeadcodeDrop | 73966.1 ms | 72410.4 ms | 1555.7 ms | 24877.4 ms |
| Gorm_schema | LLGoNoLTO | 72837.0 ms | 71251.4 ms | 1585.5 ms | 24425.9 ms |
| Toml | LLGoFullLTONoGlobalDCE | 69330.1 ms | 67601.0 ms | 1729.1 ms | 42166.2 ms |
| Toml | LLGoDeadcodeDrop | 68880.4 ms | 67276.3 ms | 1604.1 ms | 23121.8 ms |
| Toml | LLGoNoLTO | 68151.0 ms | 66558.0 ms | 1593.0 ms | 22975.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 66283.3 ms | 64533.3 ms | 1750.0 ms | 36154.1 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 62162.0 ms | 60390.2 ms | 1771.8 ms | 34743.7 ms |
| Toml | LLGoFullLTOGlobalDCE | 61660.5 ms | 59949.5 ms | 1711.0 ms | 34591.8 ms |
| IXGo | Go | 61481.2 ms | 57379.9 ms | 4101.3 ms | 17093.6 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 50150.3 ms | 48877.1 ms | 1273.2 ms | 32327.2 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 47481.8 ms | 46309.8 ms | 1172.0 ms | 17241.6 ms |
| Dustin_humanize | LLGoNoLTO | 47135.6 ms | 45978.1 ms | 1157.5 ms | 17140.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 41428.3 ms | 40140.9 ms | 1287.4 ms | 23555.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 40950.9 ms | 39712.1 ms | 1238.8 ms | 23301.5 ms |
| Etcdctl | Go | 24988.3 ms | 23298.2 ms | 1690.0 ms | 7542.6 ms |
| XGo | Go | 14242.9 ms | 13290.1 ms | 952.8 ms | 4258.6 ms |
| Aws_restjson | Go | 5982.3 ms | 5415.3 ms | 567.0 ms | 2779.7 ms |
| Gorm_schema | Go | 4296.3 ms | 3968.8 ms | 327.5 ms | 1697.9 ms |
| Uber_zap | Go | 3995.9 ms | 3655.5 ms | 340.4 ms | 1578.9 ms |
| K8s_workqueue | Go | 3757.2 ms | 3232.8 ms | 524.4 ms | 1990.9 ms |
| Toml | Go | 1552.7 ms | 1357.2 ms | 195.5 ms | 725.4 ms |
| Dustin_humanize | Go | 615.1 ms | 483.9 ms | 131.2 ms | 313.3 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1545819.4 ms | 958442.8 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1524627.3 ms | 904270.4 ms | 9 |
| LLGoFullLTOGlobalDCE | 1518608.8 ms | 916838.3 ms | 9 |
| LLGoNoLTO | 1282281.4 ms | 437328.6 ms | 9 |
| LLGoDeadcodeDrop | 1280530.1 ms | 443662.5 ms | 9 |
| Go | 120911.9 ms | 37980.9 ms | 9 |

Dependency download details are in `download-timings.log`.
