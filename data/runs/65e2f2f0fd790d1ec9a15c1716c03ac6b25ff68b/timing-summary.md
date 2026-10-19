## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 773163.6 ms | 759557.9 ms | 13605.6 ms | 390516.7 ms |
| IXGo | LLGoFullLTOGlobalDCE | 772526.9 ms | 760162.9 ms | 12364.0 ms | 384809.9 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 733749.4 ms | 721158.8 ms | 12590.6 ms | 374367.8 ms |
| IXGo | LLGoDeadcodeDrop | 632813.2 ms | 618881.9 ms | 13931.3 ms | 180499.2 ms |
| IXGo | LLGoNoLTO | 604545.5 ms | 593016.4 ms | 11529.1 ms | 170678.6 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 322491.6 ms | 316554.9 ms | 5936.6 ms | 202730.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 316790.5 ms | 310779.0 ms | 6011.5 ms | 201400.2 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 307880.4 ms | 302202.9 ms | 5677.5 ms | 199066.6 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 252680.6 ms | 249031.4 ms | 3649.3 ms | 149787.3 ms |
| Aws_restjson | LLGoNoLTO | 251442.9 ms | 248017.1 ms | 3425.8 ms | 82963.9 ms |
| Aws_restjson | LLGoDeadcodeDrop | 246896.8 ms | 243425.4 ms | 3471.4 ms | 83541.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 239966.6 ms | 236523.8 ms | 3442.8 ms | 134984.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 236332.6 ms | 232840.4 ms | 3492.1 ms | 133206.1 ms |
| XGo | LLGoFullLTONoGlobalDCE | 221688.7 ms | 217872.1 ms | 3816.5 ms | 159317.2 ms |
| Etcdctl | LLGoDeadcodeDrop | 220891.8 ms | 215011.1 ms | 5880.6 ms | 72398.0 ms |
| Etcdctl | LLGoNoLTO | 214267.1 ms | 209367.5 ms | 4899.6 ms | 68641.4 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 204148.5 ms | 200860.4 ms | 3288.1 ms | 130721.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 202027.9 ms | 198748.6 ms | 3279.3 ms | 128212.9 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 201553.0 ms | 198327.5 ms | 3225.4 ms | 128869.9 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 200230.6 ms | 196428.7 ms | 3801.9 ms | 137867.0 ms |
| XGo | LLGoFullLTOGlobalDCE | 198283.7 ms | 194576.7 ms | 3707.0 ms | 137091.8 ms |
| Uber_zap | LLGoNoLTO | 195412.7 ms | 192675.1 ms | 2737.6 ms | 71220.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 195275.3 ms | 192085.2 ms | 3190.2 ms | 118143.4 ms |
| Uber_zap | LLGoDeadcodeDrop | 192742.3 ms | 189843.7 ms | 2898.5 ms | 71358.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 192254.4 ms | 189163.6 ms | 3090.8 ms | 116261.6 ms |
| K8s_workqueue | LLGoNoLTO | 191897.3 ms | 189082.9 ms | 2814.4 ms | 69099.8 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 186640.0 ms | 183751.8 ms | 2888.3 ms | 69013.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 184125.9 ms | 180861.7 ms | 3264.2 ms | 110754.3 ms |
| XGo | LLGoDeadcodeDrop | 124734.1 ms | 120865.8 ms | 3868.3 ms | 45301.6 ms |
| XGo | LLGoNoLTO | 122786.1 ms | 119742.1 ms | 3044.0 ms | 43086.1 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 106073.4 ms | 104098.5 ms | 1974.9 ms | 64013.5 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 106052.5 ms | 104129.9 ms | 1922.6 ms | 64661.5 ms |
| Gorm_schema | LLGoDeadcodeDrop | 102556.6 ms | 100603.3 ms | 1953.2 ms | 34252.3 ms |
| Gorm_schema | LLGoNoLTO | 102046.2 ms | 100236.9 ms | 1809.4 ms | 33888.3 ms |
| Toml | LLGoFullLTONoGlobalDCE | 98867.6 ms | 96910.6 ms | 1956.9 ms | 58943.5 ms |
| Toml | LLGoDeadcodeDrop | 97362.8 ms | 95463.1 ms | 1899.7 ms | 32270.7 ms |
| Toml | LLGoNoLTO | 96013.1 ms | 94242.8 ms | 1770.3 ms | 31621.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 94653.8 ms | 92768.6 ms | 1885.1 ms | 51178.9 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 89007.4 ms | 87101.1 ms | 1906.4 ms | 48967.4 ms |
| Toml | LLGoFullLTOGlobalDCE | 88915.5 ms | 87012.0 ms | 1903.5 ms | 48911.0 ms |
| IXGo | Go | 86752.6 ms | 80425.4 ms | 6327.2 ms | 23839.4 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 69676.6 ms | 68265.3 ms | 1411.3 ms | 44487.7 ms |
| Dustin_humanize | LLGoNoLTO | 67678.3 ms | 66342.9 ms | 1335.4 ms | 24094.0 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 66703.1 ms | 65330.8 ms | 1372.2 ms | 24137.5 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 59055.5 ms | 57687.5 ms | 1368.0 ms | 33206.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 58704.9 ms | 57343.0 ms | 1361.8 ms | 32912.8 ms |
| Etcdctl | Go | 35046.8 ms | 32609.2 ms | 2437.6 ms | 10558.9 ms |
| XGo | Go | 20420.1 ms | 18944.1 ms | 1476.1 ms | 5910.2 ms |
| Aws_restjson | Go | 8636.4 ms | 7901.0 ms | 735.4 ms | 3566.2 ms |
| Gorm_schema | Go | 5999.0 ms | 5569.9 ms | 429.2 ms | 2345.4 ms |
| Uber_zap | Go | 5615.7 ms | 5195.1 ms | 420.6 ms | 2210.7 ms |
| K8s_workqueue | Go | 4817.1 ms | 4356.0 ms | 461.1 ms | 1705.4 ms |
| Toml | Go | 2189.1 ms | 1944.8 ms | 244.3 ms | 1004.2 ms |
| Dustin_humanize | Go | 827.5 ms | 698.5 ms | 129.0 ms | 395.5 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2196297.2 ms | 1310222.5 ms | 9 |
| LLGoFullLTOGlobalDCE | 2171909.8 ms | 1246819.7 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2157970.3 ms | 1228349.2 ms | 9 |
| LLGoDeadcodeDrop | 1871340.5 ms | 612772.3 ms | 9 |
| LLGoNoLTO | 1846089.3 ms | 595293.7 ms | 9 |
| Go | 170304.2 ms | 51535.8 ms | 9 |

Dependency download details are in `download-timings.log`.
