## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| Etcdctl | LLGoFullLTONoGlobalDCE | 271470.9 ms | 263229.2 ms | 8241.7 ms | 196968.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 262454.2 ms | 254591.6 ms | 7862.7 ms | 193534.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 258800.1 ms | 250831.9 ms | 7968.3 ms | 190957.8 ms |
| XGo | LLGoFullLTONoGlobalDCE | 191328.0 ms | 185820.9 ms | 5507.1 ms | 153474.6 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 180448.6 ms | 175801.6 ms | 4647.1 ms | 123713.0 ms |
| XGo | LLGoFullLTOGlobalDCE | 167685.4 ms | 162492.9 ms | 5192.5 ms | 129726.5 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 166614.0 ms | 161217.4 ms | 5396.6 ms | 129169.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 161641.2 ms | 157214.3 ms | 4426.9 ms | 103700.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 159214.5 ms | 154704.9 ms | 4509.6 ms | 102717.4 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 147908.2 ms | 143943.4 ms | 3964.8 ms | 105199.6 ms |
| Etcdctl | LLGoDeadcodeDrop | 143739.0 ms | 136875.2 ms | 6863.8 ms | 48924.8 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 143038.1 ms | 139197.7 ms | 3840.4 ms | 102443.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 142695.8 ms | 138790.2 ms | 3905.5 ms | 101301.4 ms |
| Etcdctl | LLGoNoLTO | 142529.0 ms | 136138.2 ms | 6390.7 ms | 47802.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 135384.8 ms | 131678.7 ms | 3706.1 ms | 92034.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 132570.6 ms | 128809.5 ms | 3761.1 ms | 88921.7 ms |
| Aws_restjson | LLGoNoLTO | 127413.2 ms | 123967.1 ms | 3446.1 ms | 40128.9 ms |
| Aws_restjson | LLGoDeadcodeDrop | 124791.9 ms | 120915.2 ms | 3876.7 ms | 39911.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 121694.2 ms | 118199.1 ms | 3495.1 ms | 80550.2 ms |
| Uber_zap | LLGoDeadcodeDrop | 100531.2 ms | 97508.8 ms | 3022.4 ms | 32952.2 ms |
| Uber_zap | LLGoNoLTO | 100253.4 ms | 97304.5 ms | 2949.0 ms | 32647.6 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 95626.1 ms | 92479.3 ms | 3146.9 ms | 31638.4 ms |
| K8s_workqueue | LLGoNoLTO | 95269.2 ms | 92243.9 ms | 3025.3 ms | 31437.7 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 87004.3 ms | 84299.8 ms | 2704.4 ms | 61628.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 86369.1 ms | 83589.2 ms | 2780.0 ms | 60473.9 ms |
| Toml | LLGoFullLTONoGlobalDCE | 80198.4 ms | 77612.4 ms | 2586.0 ms | 56450.1 ms |
| XGo | LLGoNoLTO | 74207.8 ms | 70181.1 ms | 4026.7 ms | 27144.5 ms |
| XGo | LLGoDeadcodeDrop | 73541.1 ms | 68981.2 ms | 4559.8 ms | 27246.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 71984.9 ms | 69398.4 ms | 2586.6 ms | 45955.6 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 69910.4 ms | 67504.6 ms | 2405.8 ms | 45733.4 ms |
| Toml | LLGoFullLTOGlobalDCE | 69500.0 ms | 67071.0 ms | 2429.0 ms | 45391.6 ms |
| Gorm_schema | LLGoDeadcodeDrop | 62260.3 ms | 59913.8 ms | 2346.4 ms | 22011.3 ms |
| Gorm_schema | LLGoNoLTO | 61748.1 ms | 59507.4 ms | 2240.7 ms | 21407.8 ms |
| Toml | LLGoNoLTO | 57671.1 ms | 55706.7 ms | 1964.4 ms | 19847.5 ms |
| Toml | LLGoDeadcodeDrop | 57208.4 ms | 55177.0 ms | 2031.4 ms | 19995.5 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 56873.8 ms | 55150.0 ms | 1723.7 ms | 41518.4 ms |
| IXGo | Go | 54175.5 ms | 44860.6 ms | 9314.9 ms | 15010.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 44901.9 ms | 43298.8 ms | 1603.0 ms | 29303.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 44728.1 ms | 43150.3 ms | 1577.8 ms | 29311.5 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 40147.5 ms | 38674.2 ms | 1473.3 ms | 15126.3 ms |
| Dustin_humanize | LLGoNoLTO | 39360.4 ms | 37980.7 ms | 1379.7 ms | 14777.0 ms |
| Etcdctl | Go | 22037.3 ms | 18629.1 ms | 3408.2 ms | 6692.2 ms |
| XGo | Go | 12483.3 ms | 10519.1 ms | 1964.2 ms | 3696.2 ms |
| Aws_restjson | Go | 5223.4 ms | 4279.5 ms | 943.9 ms | 2154.5 ms |
| Gorm_schema | Go | 3710.5 ms | 3135.0 ms | 575.5 ms | 1493.6 ms |
| Uber_zap | Go | 3450.3 ms | 2931.0 ms | 519.3 ms | 1402.3 ms |
| K8s_workqueue | Go | 3037.2 ms | 2461.7 ms | 575.5 ms | 1099.0 ms |
| Toml | Go | 1317.2 ms | 1060.4 ms | 256.8 ms | 625.8 ms |
| Dustin_humanize | Go | 520.4 ms | 380.7 ms | 139.6 ms | 259.7 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1158270.3 ms | 841395.5 ms | 8 |
| LLGoFullLTOGlobalDCE | 1066804.5 ms | 752898.2 ms | 8 |
| LLGoFullLTOGlobalDCEPlugin | 1029344.7 ms | 715885.0 ms | 8 |
| LLGoNoLTO | 698452.2 ms | 235193.7 ms | 8 |
| LLGoDeadcodeDrop | 697845.5 ms | 237806.3 ms | 8 |
| Go | 105955.1 ms | 32433.6 ms | 9 |

Dependency download details are in `download-timings.log`.
