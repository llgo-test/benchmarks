## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 568340.2 ms | 549945.9 ms | 18394.3 ms | 371544.6 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 540948.5 ms | 522873.2 ms | 18075.3 ms | 354723.5 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 537754.1 ms | 520062.7 ms | 17691.4 ms | 358028.5 ms |
| IXGo | LLGoDeadcodeDrop | 312119.2 ms | 293861.5 ms | 18257.7 ms | 98166.5 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 294730.7 ms | 286104.7 ms | 8626.0 ms | 220808.9 ms |
| IXGo | LLGoNoLTO | 291964.2 ms | 277206.7 ms | 14757.5 ms | 88972.7 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 289463.5 ms | 280716.1 ms | 8747.4 ms | 216768.6 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 284381.0 ms | 275598.4 ms | 8782.6 ms | 212187.2 ms |
| XGo | LLGoFullLTONoGlobalDCE | 213190.7 ms | 207175.3 ms | 6015.5 ms | 174311.9 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 208063.3 ms | 203065.5 ms | 4997.8 ms | 140402.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 202583.6 ms | 197502.2 ms | 5081.4 ms | 131194.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 198899.5 ms | 193793.2 ms | 5106.3 ms | 128812.5 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 195601.8 ms | 189731.2 ms | 5870.6 ms | 153816.9 ms |
| XGo | LLGoFullLTOGlobalDCE | 184972.8 ms | 179188.5 ms | 5784.3 ms | 145547.5 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 174763.6 ms | 170336.7 ms | 4426.8 ms | 124481.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 169475.8 ms | 164974.8 ms | 4500.9 ms | 120883.3 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 168869.3 ms | 164339.0 ms | 4530.3 ms | 120789.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 159877.2 ms | 155460.1 ms | 4417.1 ms | 109513.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 157711.9 ms | 153414.3 ms | 4297.6 ms | 106600.2 ms |
| Aws_restjson | LLGoNoLTO | 154222.7 ms | 150169.4 ms | 4053.4 ms | 47602.2 ms |
| Etcdctl | LLGoNoLTO | 144375.6 ms | 137527.6 ms | 6848.1 ms | 49124.3 ms |
| Aws_restjson | LLGoDeadcodeDrop | 143626.8 ms | 139362.8 ms | 4264.0 ms | 45991.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 142513.4 ms | 138251.6 ms | 4261.8 ms | 94606.4 ms |
| Etcdctl | LLGoDeadcodeDrop | 141780.0 ms | 134430.4 ms | 7349.7 ms | 49127.4 ms |
| Uber_zap | LLGoDeadcodeDrop | 124859.5 ms | 120985.9 ms | 3873.6 ms | 40782.4 ms |
| Uber_zap | LLGoNoLTO | 122838.3 ms | 119421.1 ms | 3417.2 ms | 39001.9 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 112888.5 ms | 109376.1 ms | 3512.4 ms | 37217.0 ms |
| K8s_workqueue | LLGoNoLTO | 110910.0 ms | 107584.6 ms | 3325.4 ms | 35250.4 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 90976.9 ms | 88211.1 ms | 2765.7 ms | 64490.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 88179.1 ms | 85564.5 ms | 2614.6 ms | 61427.5 ms |
| Toml | LLGoFullLTONoGlobalDCE | 82427.4 ms | 79839.0 ms | 2588.3 ms | 58361.1 ms |
| XGo | LLGoDeadcodeDrop | 79356.2 ms | 74379.8 ms | 4976.5 ms | 28770.5 ms |
| XGo | LLGoNoLTO | 79113.3 ms | 74854.5 ms | 4258.8 ms | 28854.7 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 77821.2 ms | 75240.9 ms | 2580.3 ms | 49972.6 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 73342.2 ms | 70847.9 ms | 2494.3 ms | 48155.6 ms |
| Toml | LLGoFullLTOGlobalDCE | 72428.7 ms | 70069.9 ms | 2358.7 ms | 47636.3 ms |
| Gorm_schema | LLGoNoLTO | 65747.4 ms | 63412.0 ms | 2335.5 ms | 22677.4 ms |
| Gorm_schema | LLGoDeadcodeDrop | 64259.4 ms | 61934.3 ms | 2325.1 ms | 22667.4 ms |
| Toml | LLGoDeadcodeDrop | 60236.0 ms | 58055.5 ms | 2180.5 ms | 21039.2 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 60019.4 ms | 58195.0 ms | 1824.4 ms | 43635.6 ms |
| Toml | LLGoNoLTO | 59173.0 ms | 57122.2 ms | 2050.7 ms | 20403.4 ms |
| IXGo | Go | 57211.0 ms | 47457.6 ms | 9753.4 ms | 15750.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 48314.1 ms | 46693.5 ms | 1620.7 ms | 31774.9 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 46003.2 ms | 44400.5 ms | 1602.7 ms | 30153.7 ms |
| Dustin_humanize | LLGoNoLTO | 42506.3 ms | 41079.3 ms | 1427.0 ms | 15939.2 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 42181.0 ms | 40636.5 ms | 1544.5 ms | 15983.7 ms |
| Etcdctl | Go | 22947.4 ms | 19408.8 ms | 3538.6 ms | 7032.0 ms |
| XGo | Go | 13166.0 ms | 11077.0 ms | 2089.0 ms | 4117.7 ms |
| Aws_restjson | Go | 5302.1 ms | 4313.9 ms | 988.2 ms | 2195.3 ms |
| Gorm_schema | Go | 3766.0 ms | 3109.2 ms | 656.8 ms | 1540.9 ms |
| Uber_zap | Go | 3510.1 ms | 2946.4 ms | 563.7 ms | 1449.9 ms |
| K8s_workqueue | Go | 3086.4 ms | 2524.9 ms | 561.5 ms | 1129.1 ms |
| Toml | Go | 1346.1 ms | 1102.5 ms | 243.6 ms | 644.5 ms |
| Dustin_humanize | Go | 542.6 ms | 383.2 ms | 159.4 ms | 282.8 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1825528.3 ms | 1301269.2 ms | 9 |
| LLGoFullLTOGlobalDCE | 1782907.0 ms | 1236327.9 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1723217.9 ms | 1183032.2 ms | 9 |
| LLGoDeadcodeDrop | 1081306.7 ms | 359745.5 ms | 9 |
| LLGoNoLTO | 1070851.0 ms | 347826.3 ms | 9 |
| Go | 110877.7 ms | 34142.5 ms | 9 |

Dependency download details are in `download-timings.log`.
