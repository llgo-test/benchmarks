## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 641734.2 ms | 635035.1 ms | 6699.1 ms | 410379.6 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 635785.2 ms | 628966.8 ms | 6818.3 ms | 409535.3 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 621138.2 ms | 614900.5 ms | 6237.7 ms | 407928.2 ms |
| IXGo | LLGoNoLTO | 402872.3 ms | 397242.6 ms | 5629.7 ms | 132594.5 ms |
| IXGo | LLGoDeadcodeDrop | 398453.1 ms | 392568.0 ms | 5885.1 ms | 131565.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 275678.0 ms | 271094.7 ms | 4583.2 ms | 168390.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 273709.1 ms | 268873.4 ms | 4835.6 ms | 165884.6 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 270246.7 ms | 265880.9 ms | 4365.8 ms | 166120.8 ms |
| Etcdctl | LLGoDeadcodeDrop | 201568.7 ms | 197627.7 ms | 3941.0 ms | 66691.6 ms |
| Etcdctl | LLGoNoLTO | 200987.9 ms | 196984.9 ms | 4003.0 ms | 66371.9 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 189620.7 ms | 186438.7 ms | 3182.1 ms | 132042.6 ms |
| XGo | LLGoFullLTOGlobalDCE | 188736.9 ms | 185526.1 ms | 3210.9 ms | 131561.6 ms |
| XGo | LLGoFullLTONoGlobalDCE | 186831.6 ms | 183656.2 ms | 3175.4 ms | 131130.9 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 144008.3 ms | 141598.1 ms | 2410.2 ms | 105939.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 131669.1 ms | 129307.0 ms | 2362.1 ms | 92209.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 131559.6 ms | 129243.1 ms | 2316.6 ms | 92506.8 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 115378.7 ms | 113407.4 ms | 1971.2 ms | 88470.6 ms |
| XGo | LLGoDeadcodeDrop | 113242.3 ms | 110549.1 ms | 2693.2 ms | 42549.8 ms |
| XGo | LLGoNoLTO | 111367.7 ms | 108722.5 ms | 2645.2 ms | 42169.1 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 110245.7 ms | 108460.1 ms | 1785.6 ms | 86407.4 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 108596.9 ms | 106872.7 ms | 1724.2 ms | 85419.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 106793.8 ms | 105049.1 ms | 1744.6 ms | 79217.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 105405.1 ms | 103778.9 ms | 1626.3 ms | 78861.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 95321.6 ms | 93619.1 ms | 1702.5 ms | 71520.6 ms |
| Aws_restjson | LLGoDeadcodeDrop | 84707.9 ms | 82759.4 ms | 1948.5 ms | 38506.7 ms |
| Aws_restjson | LLGoNoLTO | 82970.8 ms | 81025.2 ms | 1945.7 ms | 37411.7 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 66875.5 ms | 65558.4 ms | 1317.1 ms | 46455.2 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 66664.9 ms | 65352.0 ms | 1313.0 ms | 47180.5 ms |
| Uber_zap | LLGoDeadcodeDrop | 58466.8 ms | 57065.2 ms | 1401.7 ms | 25620.1 ms |
| Uber_zap | LLGoNoLTO | 58306.7 ms | 56902.9 ms | 1403.8 ms | 26240.1 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 56863.4 ms | 55540.9 ms | 1322.5 ms | 36189.6 ms |
| Toml | LLGoFullLTONoGlobalDCE | 53970.1 ms | 52913.0 ms | 1057.1 ms | 41809.0 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 51454.8 ms | 50016.1 ms | 1438.7 ms | 23582.7 ms |
| K8s_workqueue | LLGoNoLTO | 50587.5 ms | 49118.4 ms | 1469.1 ms | 23135.8 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 46863.5 ms | 45791.7 ms | 1071.8 ms | 33685.7 ms |
| Toml | LLGoFullLTOGlobalDCE | 46083.0 ms | 45048.9 ms | 1034.1 ms | 33620.4 ms |
| IXGo | Go | 44687.0 ms | 41854.1 ms | 2832.9 ms | 12830.8 ms |
| Gorm_schema | LLGoDeadcodeDrop | 39438.5 ms | 38307.3 ms | 1131.3 ms | 12809.4 ms |
| Gorm_schema | LLGoNoLTO | 38726.8 ms | 37598.6 ms | 1128.2 ms | 12514.0 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 33951.2 ms | 33113.6 ms | 837.6 ms | 26702.5 ms |
| Etcdctl | Go | 33135.9 ms | 31153.5 ms | 1982.4 ms | 9883.5 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 25521.7 ms | 24721.5 ms | 800.2 ms | 17931.9 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 25017.4 ms | 24197.7 ms | 819.7 ms | 17680.1 ms |
| Toml | LLGoDeadcodeDrop | 24557.5 ms | 23624.6 ms | 932.9 ms | 9112.2 ms |
| Toml | LLGoNoLTO | 23849.4 ms | 22942.0 ms | 907.3 ms | 8789.3 ms |
| XGo | Go | 18976.6 ms | 17860.8 ms | 1115.8 ms | 5556.0 ms |
| Dustin_humanize | LLGoNoLTO | 13397.0 ms | 12663.7 ms | 733.2 ms | 5686.0 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 13386.7 ms | 12661.7 ms | 725.0 ms | 5791.9 ms |
| Aws_restjson | Go | 8129.3 ms | 7446.3 ms | 683.0 ms | 3335.8 ms |
| Gorm_schema | Go | 5795.4 ms | 5433.1 ms | 362.3 ms | 2222.0 ms |
| Uber_zap | Go | 5285.3 ms | 4879.5 ms | 405.9 ms | 2036.7 ms |
| K8s_workqueue | Go | 4675.3 ms | 4238.3 ms | 436.9 ms | 1638.3 ms |
| Toml | Go | 2030.7 ms | 1801.1 ms | 229.6 ms | 918.2 ms |
| Dustin_humanize | Go | 803.2 ms | 669.6 ms | 133.7 ms | 383.2 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1600786.7 ms | 1100701.0 ms | 9 |
| LLGoFullLTOGlobalDCE | 1589366.6 ms | 1063356.7 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1564117.0 ms | 1040723.5 ms | 9 |
| LLGoDeadcodeDrop | 985276.3 ms | 356229.7 ms | 9 |
| LLGoNoLTO | 983066.0 ms | 354912.5 ms | 9 |
| Go | 123518.7 ms | 38804.6 ms | 9 |

Dependency download details are in `download-timings.log`.
