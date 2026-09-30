## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 532822.1 ms | 521223.6 ms | 11598.5 ms | 284951.3 ms |
| IXGo | LLGoFullLTOGlobalDCE | 512218.2 ms | 501287.5 ms | 10930.7 ms | 276824.9 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 511741.9 ms | 501259.7 ms | 10482.2 ms | 274967.1 ms |
| IXGo | LLGoDeadcodeDrop | 402645.1 ms | 393484.7 ms | 9160.4 ms | 122485.7 ms |
| IXGo | LLGoNoLTO | 374685.3 ms | 365648.0 ms | 9037.2 ms | 114905.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 246451.3 ms | 241988.2 ms | 4463.1 ms | 158483.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 243809.5 ms | 239273.7 ms | 4535.8 ms | 157165.0 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 241877.9 ms | 237272.2 ms | 4605.7 ms | 157036.7 ms |
| Aws_restjson | LLGoDeadcodeDrop | 203396.9 ms | 200592.2 ms | 2804.7 ms | 73747.1 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 202153.5 ms | 199152.1 ms | 3001.3 ms | 122078.7 ms |
| Aws_restjson | LLGoNoLTO | 198036.0 ms | 195361.0 ms | 2675.1 ms | 71908.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 191905.0 ms | 188733.7 ms | 3171.3 ms | 110805.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 189772.6 ms | 186756.2 ms | 3016.5 ms | 108840.7 ms |
| Etcdctl | LLGoDeadcodeDrop | 178623.2 ms | 174686.3 ms | 3936.9 ms | 61882.2 ms |
| Etcdctl | LLGoNoLTO | 175845.5 ms | 172040.9 ms | 3804.5 ms | 61388.5 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 173400.5 ms | 170130.0 ms | 3270.5 ms | 124080.9 ms |
| XGo | LLGoFullLTOGlobalDCE | 171972.9 ms | 168692.4 ms | 3280.5 ms | 123171.8 ms |
| XGo | LLGoFullLTONoGlobalDCE | 170609.3 ms | 167517.9 ms | 3091.4 ms | 123463.8 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 170605.9 ms | 168188.2 ms | 2417.6 ms | 109128.9 ms |
| Uber_zap | LLGoDeadcodeDrop | 168262.6 ms | 165970.4 ms | 2292.2 ms | 64768.3 ms |
| Uber_zap | LLGoNoLTO | 166705.9 ms | 164424.9 ms | 2281.0 ms | 65557.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 165347.5 ms | 162588.4 ms | 2759.1 ms | 105018.8 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 164185.2 ms | 161531.4 ms | 2653.7 ms | 105113.5 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 162884.8 ms | 160326.4 ms | 2558.4 ms | 63719.6 ms |
| K8s_workqueue | LLGoNoLTO | 160094.5 ms | 157749.8 ms | 2344.7 ms | 62394.2 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 160017.0 ms | 157496.1 ms | 2520.9 ms | 97698.9 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 159291.3 ms | 156787.1 ms | 2504.2 ms | 96992.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 152843.5 ms | 150209.0 ms | 2634.5 ms | 92120.7 ms |
| XGo | LLGoDeadcodeDrop | 103303.8 ms | 100413.5 ms | 2890.4 ms | 40862.6 ms |
| XGo | LLGoNoLTO | 100523.1 ms | 97819.8 ms | 2703.3 ms | 39907.0 ms |
| Gorm_schema | LLGoDeadcodeDrop | 86634.3 ms | 85126.4 ms | 1507.8 ms | 28944.2 ms |
| Gorm_schema | LLGoNoLTO | 85996.6 ms | 84526.1 ms | 1470.6 ms | 28703.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 85173.8 ms | 83553.0 ms | 1620.8 ms | 50261.8 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 85005.9 ms | 83335.6 ms | 1670.3 ms | 50814.0 ms |
| IXGo | Go | 84732.4 ms | 79603.7 ms | 5128.7 ms | 23491.5 ms |
| Toml | LLGoDeadcodeDrop | 82351.8 ms | 80678.5 ms | 1673.2 ms | 27292.9 ms |
| Toml | LLGoNoLTO | 80810.9 ms | 79333.4 ms | 1477.5 ms | 26736.4 ms |
| Toml | LLGoFullLTONoGlobalDCE | 78961.8 ms | 77286.8 ms | 1675.0 ms | 46240.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 75796.9 ms | 74228.9 ms | 1568.0 ms | 40334.4 ms |
| Toml | LLGoFullLTOGlobalDCE | 71646.6 ms | 69966.7 ms | 1679.9 ms | 38572.9 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 71637.4 ms | 69968.8 ms | 1668.5 ms | 38711.9 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 56497.2 ms | 55383.6 ms | 1113.6 ms | 20274.1 ms |
| Dustin_humanize | LLGoNoLTO | 55085.6 ms | 54041.3 ms | 1044.3 ms | 19660.7 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 55060.8 ms | 53913.4 ms | 1147.4 ms | 34195.5 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 46981.3 ms | 45891.6 ms | 1089.7 ms | 25674.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 46602.0 ms | 45529.7 ms | 1072.3 ms | 25725.3 ms |
| Etcdctl | Go | 33864.8 ms | 31808.0 ms | 2056.9 ms | 10158.7 ms |
| XGo | Go | 18936.3 ms | 17789.9 ms | 1146.4 ms | 5598.3 ms |
| Aws_restjson | Go | 7910.7 ms | 7243.3 ms | 667.4 ms | 3207.5 ms |
| Gorm_schema | Go | 5796.1 ms | 5374.8 ms | 421.3 ms | 2268.7 ms |
| Uber_zap | Go | 5544.4 ms | 5002.0 ms | 542.4 ms | 2460.0 ms |
| K8s_workqueue | Go | 4759.7 ms | 4241.0 ms | 518.8 ms | 1718.1 ms |
| Toml | Go | 2044.5 ms | 1784.8 ms | 259.6 ms | 939.5 ms |
| Dustin_humanize | Go | 819.1 ms | 664.3 ms | 154.9 ms | 385.7 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1680202.1 ms | 1023038.5 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1651129.3 ms | 972154.0 ms | 9 |
| LLGoFullLTOGlobalDCE | 1646560.1 ms | 983280.1 ms | 9 |
| LLGoDeadcodeDrop | 1444599.7 ms | 503976.6 ms | 9 |
| LLGoNoLTO | 1397783.5 ms | 491162.9 ms | 9 |
| Go | 164408.0 ms | 50228.0 ms | 9 |

Dependency download details are in `download-timings.log`.
