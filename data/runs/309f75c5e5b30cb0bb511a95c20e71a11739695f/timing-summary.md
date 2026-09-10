## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 857649.0 ms | 850349.5 ms | 7299.5 ms | 614034.3 ms |
| IXGo | LLGoFullLTOGlobalDCE | 696867.6 ms | 689684.2 ms | 7183.4 ms | 474574.9 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 692535.2 ms | 685738.5 ms | 6796.7 ms | 480209.2 ms |
| IXGo | LLGoDeadcodeDrop | 418799.3 ms | 412338.9 ms | 6460.4 ms | 136284.7 ms |
| IXGo | LLGoNoLTO | 417685.4 ms | 411664.7 ms | 6020.7 ms | 138895.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 267514.9 ms | 262090.5 ms | 5424.5 ms | 166115.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 261747.7 ms | 256570.4 ms | 5177.3 ms | 161726.3 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 261697.2 ms | 256721.8 ms | 4975.4 ms | 164479.1 ms |
| Etcdctl | LLGoNoLTO | 193692.8 ms | 189132.4 ms | 4560.4 ms | 64837.7 ms |
| Etcdctl | LLGoDeadcodeDrop | 193012.6 ms | 188374.3 ms | 4638.3 ms | 64014.6 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 181617.2 ms | 178194.0 ms | 3423.2 ms | 129184.6 ms |
| XGo | LLGoFullLTOGlobalDCE | 180004.0 ms | 176645.4 ms | 3358.6 ms | 127371.1 ms |
| XGo | LLGoFullLTONoGlobalDCE | 179413.8 ms | 175992.3 ms | 3421.5 ms | 128304.8 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 142787.1 ms | 140378.7 ms | 2408.4 ms | 107544.1 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 130516.6 ms | 128019.3 ms | 2497.2 ms | 94833.3 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 129591.3 ms | 127098.4 ms | 2492.9 ms | 93049.1 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 114112.1 ms | 112231.0 ms | 1881.1 ms | 89592.7 ms |
| XGo | LLGoDeadcodeDrop | 106767.3 ms | 103888.9 ms | 2878.4 ms | 41938.1 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 105278.1 ms | 103475.1 ms | 1803.0 ms | 83368.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 103999.7 ms | 101970.6 ms | 2029.0 ms | 82235.2 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 103116.0 ms | 101232.1 ms | 1883.9 ms | 77186.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 101940.7 ms | 100124.0 ms | 1816.7 ms | 76676.5 ms |
| XGo | LLGoNoLTO | 101722.6 ms | 98966.0 ms | 2756.6 ms | 38793.1 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 94553.6 ms | 92823.3 ms | 1730.4 ms | 72440.8 ms |
| Aws_restjson | LLGoDeadcodeDrop | 83180.2 ms | 80992.0 ms | 2188.2 ms | 40477.8 ms |
| Aws_restjson | LLGoNoLTO | 79933.3 ms | 77781.8 ms | 2151.4 ms | 37880.1 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 64849.6 ms | 63498.0 ms | 1351.6 ms | 46090.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 62722.0 ms | 61240.7 ms | 1481.3 ms | 44110.0 ms |
| Uber_zap | LLGoDeadcodeDrop | 55131.5 ms | 53611.9 ms | 1519.6 ms | 24543.3 ms |
| Uber_zap | LLGoNoLTO | 55112.8 ms | 53667.9 ms | 1444.9 ms | 25217.7 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 53564.7 ms | 52187.9 ms | 1376.7 ms | 34370.2 ms |
| Toml | LLGoFullLTONoGlobalDCE | 50843.6 ms | 49722.0 ms | 1121.6 ms | 39838.6 ms |
| K8s_workqueue | LLGoNoLTO | 49821.3 ms | 48181.9 ms | 1639.4 ms | 24687.4 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 48326.4 ms | 46688.9 ms | 1637.5 ms | 22670.1 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 44770.9 ms | 43650.6 ms | 1120.3 ms | 32869.1 ms |
| IXGo | Go | 44342.8 ms | 41033.4 ms | 3309.4 ms | 12880.5 ms |
| Toml | LLGoFullLTOGlobalDCE | 43437.0 ms | 42307.4 ms | 1129.6 ms | 32176.7 ms |
| Gorm_schema | LLGoDeadcodeDrop | 36315.6 ms | 35118.2 ms | 1197.3 ms | 12035.3 ms |
| Gorm_schema | LLGoNoLTO | 35825.0 ms | 34631.4 ms | 1193.6 ms | 11891.8 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 32109.2 ms | 31279.8 ms | 829.4 ms | 25558.6 ms |
| Etcdctl | Go | 32049.9 ms | 29877.6 ms | 2172.3 ms | 9726.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 24748.5 ms | 23884.6 ms | 863.9 ms | 17779.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 24537.0 ms | 23655.5 ms | 881.5 ms | 17732.2 ms |
| Toml | LLGoDeadcodeDrop | 23100.6 ms | 22016.9 ms | 1083.7 ms | 8715.4 ms |
| Toml | LLGoNoLTO | 22543.9 ms | 21570.7 ms | 973.2 ms | 8663.0 ms |
| XGo | Go | 18489.2 ms | 17203.3 ms | 1285.9 ms | 5432.9 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 12480.0 ms | 11771.9 ms | 708.2 ms | 5417.2 ms |
| Dustin_humanize | LLGoNoLTO | 12180.6 ms | 11414.3 ms | 766.2 ms | 5233.3 ms |
| Aws_restjson | Go | 8046.2 ms | 7306.2 ms | 740.0 ms | 3388.7 ms |
| Gorm_schema | Go | 5643.3 ms | 5246.2 ms | 397.1 ms | 2159.1 ms |
| Uber_zap | Go | 5236.9 ms | 4774.5 ms | 462.5 ms | 2083.3 ms |
| K8s_workqueue | Go | 4523.5 ms | 4055.8 ms | 467.8 ms | 1634.0 ms |
| Toml | Go | 2035.4 ms | 1779.4 ms | 256.0 ms | 945.8 ms |
| Dustin_humanize | Go | 814.9 ms | 653.3 ms | 161.6 ms | 382.5 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTOGlobalDCEPlugin | 1757126.1 ms | 1237028.6 ms | 9 |
| LLGoFullLTONoGlobalDCE | 1643625.9 ms | 1164986.7 ms | 9 |
| LLGoFullLTOGlobalDCE | 1605772.2 ms | 1111436.2 ms | 9 |
| LLGoDeadcodeDrop | 977113.4 ms | 356096.6 ms | 9 |
| LLGoNoLTO | 968517.7 ms | 356099.5 ms | 9 |
| Go | 121182.2 ms | 38632.7 ms | 9 |

Dependency download details are in `download-timings.log`.
