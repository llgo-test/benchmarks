## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 633750.4 ms | 622700.2 ms | 11050.2 ms | 327823.5 ms |
| IXGo | LLGoFullLTOGlobalDCE | 621254.1 ms | 611322.3 ms | 9931.8 ms | 321663.3 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 612876.6 ms | 602666.0 ms | 10210.6 ms | 322269.2 ms |
| IXGo | LLGoDeadcodeDrop | 500201.0 ms | 486351.4 ms | 13849.6 ms | 150725.0 ms |
| IXGo | LLGoNoLTO | 487876.5 ms | 479492.1 ms | 8384.4 ms | 143381.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 333291.5 ms | 328410.1 ms | 4881.3 ms | 194566.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 329949.6 ms | 325021.6 ms | 4928.0 ms | 192715.2 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 325692.7 ms | 320888.6 ms | 4804.1 ms | 192726.5 ms |
| Aws_restjson | LLGoDeadcodeDrop | 262604.0 ms | 259285.0 ms | 3319.0 ms | 88010.5 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 261310.3 ms | 257465.7 ms | 3844.6 ms | 144528.0 ms |
| Etcdctl | LLGoDeadcodeDrop | 257146.4 ms | 251192.1 ms | 5954.3 ms | 85392.2 ms |
| Aws_restjson | LLGoNoLTO | 256576.0 ms | 253202.5 ms | 3373.5 ms | 86381.4 ms |
| Etcdctl | LLGoNoLTO | 254277.3 ms | 249992.0 ms | 4285.4 ms | 83226.3 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 245922.2 ms | 242244.9 ms | 3677.3 ms | 128880.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 245179.6 ms | 241395.5 ms | 3784.1 ms | 129347.5 ms |
| XGo | LLGoFullLTONoGlobalDCE | 237427.7 ms | 233980.7 ms | 3447.0 ms | 155987.1 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 235664.8 ms | 232376.3 ms | 3288.6 ms | 153960.0 ms |
| XGo | LLGoFullLTOGlobalDCE | 235086.9 ms | 231919.4 ms | 3167.5 ms | 153446.3 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 224922.1 ms | 221764.0 ms | 3158.1 ms | 128187.7 ms |
| Uber_zap | LLGoDeadcodeDrop | 223456.6 ms | 220659.9 ms | 2796.7 ms | 78320.5 ms |
| Uber_zap | LLGoNoLTO | 221881.9 ms | 219195.6 ms | 2686.3 ms | 77969.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 220529.5 ms | 217186.5 ms | 3343.0 ms | 125237.7 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 220482.3 ms | 217079.9 ms | 3402.4 ms | 126066.3 ms |
| K8s_workqueue | LLGoNoLTO | 216391.3 ms | 213566.9 ms | 2824.4 ms | 75844.5 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 216377.7 ms | 213415.5 ms | 2962.3 ms | 76839.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 216213.1 ms | 212877.4 ms | 3335.7 ms | 117065.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 215388.4 ms | 212080.0 ms | 3308.4 ms | 116503.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 204548.9 ms | 201315.1 ms | 3233.8 ms | 109471.0 ms |
| XGo | LLGoDeadcodeDrop | 158086.9 ms | 154486.7 ms | 3600.2 ms | 58032.7 ms |
| XGo | LLGoNoLTO | 156562.0 ms | 153906.9 ms | 2655.0 ms | 56423.9 ms |
| Gorm_schema | LLGoDeadcodeDrop | 106630.7 ms | 104908.3 ms | 1722.4 ms | 35195.5 ms |
| Gorm_schema | LLGoNoLTO | 105602.6 ms | 103900.3 ms | 1702.3 ms | 34973.2 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 104626.8 ms | 102643.9 ms | 1982.9 ms | 60787.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 104527.1 ms | 102504.4 ms | 2022.7 ms | 59835.4 ms |
| Toml | LLGoDeadcodeDrop | 99450.6 ms | 97662.7 ms | 1787.9 ms | 32806.1 ms |
| Toml | LLGoNoLTO | 98193.4 ms | 96522.6 ms | 1670.8 ms | 32210.2 ms |
| Toml | LLGoFullLTONoGlobalDCE | 96713.8 ms | 94685.0 ms | 2028.8 ms | 55251.1 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 92285.8 ms | 90407.0 ms | 1878.7 ms | 47406.3 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 88402.0 ms | 86448.1 ms | 1953.9 ms | 46116.9 ms |
| Toml | LLGoFullLTOGlobalDCE | 87887.8 ms | 85980.0 ms | 1907.8 ms | 45916.7 ms |
| IXGo | Go | 83971.7 ms | 78961.0 ms | 5010.7 ms | 23181.5 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 69420.7 ms | 68258.1 ms | 1162.6 ms | 24676.8 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 68983.8 ms | 67594.4 ms | 1389.4 ms | 41658.7 ms |
| Dustin_humanize | LLGoNoLTO | 67735.4 ms | 66532.1 ms | 1203.3 ms | 24122.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 59491.0 ms | 58112.0 ms | 1379.1 ms | 31732.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 58981.0 ms | 57628.0 ms | 1353.0 ms | 31533.3 ms |
| Etcdctl | Go | 33223.8 ms | 31268.9 ms | 1954.9 ms | 9922.5 ms |
| XGo | Go | 18754.1 ms | 17599.3 ms | 1154.7 ms | 5613.0 ms |
| Aws_restjson | Go | 7682.3 ms | 7050.0 ms | 632.2 ms | 3090.7 ms |
| Gorm_schema | Go | 5713.6 ms | 5355.4 ms | 358.2 ms | 2248.4 ms |
| Uber_zap | Go | 5220.0 ms | 4793.1 ms | 426.9 ms | 2013.8 ms |
| K8s_workqueue | Go | 4732.8 ms | 4275.8 ms | 457.0 ms | 1672.6 ms |
| Toml | Go | 1999.8 ms | 1771.3 ms | 228.5 ms | 982.7 ms |
| Dustin_humanize | Go | 836.2 ms | 680.2 ms | 156.0 ms | 460.7 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2153036.0 ms | 1227461.8 ms | 9 |
| LLGoFullLTOGlobalDCE | 2118784.0 ms | 1176198.5 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2109569.7 ms | 1157022.8 ms | 9 |
| LLGoDeadcodeDrop | 1893374.5 ms | 629998.3 ms | 9 |
| LLGoNoLTO | 1865096.5 ms | 614532.3 ms | 9 |
| Go | 162134.2 ms | 49185.8 ms | 9 |

Dependency download details are in `download-timings.log`.
