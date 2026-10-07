## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 782014.8 ms | 771238.0 ms | 10776.8 ms | 374462.0 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 716219.2 ms | 705734.2 ms | 10484.9 ms | 361871.1 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 658824.4 ms | 647368.8 ms | 11455.6 ms | 344470.1 ms |
| IXGo | LLGoDeadcodeDrop | 610394.8 ms | 595751.2 ms | 14643.6 ms | 179351.2 ms |
| IXGo | LLGoNoLTO | 572309.1 ms | 563012.4 ms | 9296.6 ms | 164953.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 363111.2 ms | 357644.7 ms | 5466.5 ms | 210726.5 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 354737.3 ms | 349295.9 ms | 5441.4 ms | 207641.0 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 344072.3 ms | 338897.6 ms | 5174.8 ms | 203318.3 ms |
| Aws_restjson | LLGoDeadcodeDrop | 285880.0 ms | 282124.2 ms | 3755.8 ms | 95299.3 ms |
| Aws_restjson | LLGoNoLTO | 279342.4 ms | 275906.0 ms | 3436.4 ms | 93246.8 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 270818.5 ms | 266605.2 ms | 4213.3 ms | 150589.6 ms |
| Etcdctl | LLGoNoLTO | 267902.2 ms | 263319.4 ms | 4582.7 ms | 87234.4 ms |
| Etcdctl | LLGoDeadcodeDrop | 265523.1 ms | 260119.4 ms | 5403.7 ms | 87703.0 ms |
| XGo | LLGoFullLTONoGlobalDCE | 264722.2 ms | 260988.1 ms | 3734.1 ms | 175101.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 259279.7 ms | 255526.1 ms | 3753.6 ms | 135610.4 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 256547.4 ms | 252974.3 ms | 3573.2 ms | 168614.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 255530.9 ms | 251549.7 ms | 3981.2 ms | 134392.5 ms |
| XGo | LLGoFullLTOGlobalDCE | 248927.5 ms | 245490.5 ms | 3437.0 ms | 161829.9 ms |
| Uber_zap | LLGoDeadcodeDrop | 244256.4 ms | 241193.8 ms | 3062.5 ms | 85901.1 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 243692.9 ms | 239970.6 ms | 3722.3 ms | 138866.9 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 239971.1 ms | 236546.4 ms | 3424.7 ms | 139330.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 237886.4 ms | 234049.1 ms | 3837.3 ms | 136112.4 ms |
| Uber_zap | LLGoNoLTO | 229844.8 ms | 227039.0 ms | 2805.7 ms | 80910.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 228462.2 ms | 224450.8 ms | 4011.4 ms | 122944.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 226138.7 ms | 222736.0 ms | 3402.7 ms | 123703.2 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 225967.2 ms | 222807.8 ms | 3159.4 ms | 79975.9 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 222653.9 ms | 219270.8 ms | 3383.1 ms | 121602.6 ms |
| K8s_workqueue | LLGoNoLTO | 220912.1 ms | 217908.0 ms | 3004.0 ms | 77681.5 ms |
| XGo | LLGoNoLTO | 169973.4 ms | 166967.8 ms | 3005.6 ms | 60719.9 ms |
| XGo | LLGoDeadcodeDrop | 164360.0 ms | 160728.1 ms | 3632.0 ms | 59846.4 ms |
| Gorm_schema | LLGoNoLTO | 116020.3 ms | 114073.5 ms | 1946.8 ms | 38352.3 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 108591.4 ms | 106541.0 ms | 2050.4 ms | 63406.7 ms |
| Toml | LLGoDeadcodeDrop | 108552.8 ms | 106534.2 ms | 2018.6 ms | 36035.6 ms |
| Gorm_schema | LLGoDeadcodeDrop | 108179.1 ms | 106442.8 ms | 1736.3 ms | 35880.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 107057.8 ms | 105003.4 ms | 2054.5 ms | 61622.1 ms |
| Toml | LLGoFullLTONoGlobalDCE | 103384.7 ms | 101275.2 ms | 2109.4 ms | 59748.6 ms |
| Toml | LLGoNoLTO | 101023.8 ms | 99186.7 ms | 1837.2 ms | 33218.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 97215.3 ms | 95116.6 ms | 2098.8 ms | 51026.2 ms |
| Toml | LLGoFullLTOGlobalDCE | 92892.1 ms | 90872.3 ms | 2019.9 ms | 48873.4 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 92772.0 ms | 90752.2 ms | 2019.8 ms | 49009.0 ms |
| IXGo | Go | 84328.9 ms | 79161.5 ms | 5167.4 ms | 23131.1 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 70596.1 ms | 69294.5 ms | 1301.6 ms | 25293.6 ms |
| Dustin_humanize | LLGoNoLTO | 70201.1 ms | 69012.3 ms | 1188.8 ms | 25178.3 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 69806.2 ms | 68468.8 ms | 1337.4 ms | 42312.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 65594.0 ms | 64128.0 ms | 1466.0 ms | 35520.5 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 62678.3 ms | 61291.2 ms | 1387.0 ms | 33659.7 ms |
| Etcdctl | Go | 34173.2 ms | 32170.7 ms | 2002.5 ms | 10463.8 ms |
| XGo | Go | 19350.4 ms | 18118.6 ms | 1231.8 ms | 5620.9 ms |
| Aws_restjson | Go | 8070.1 ms | 7361.3 ms | 708.8 ms | 3314.5 ms |
| Gorm_schema | Go | 6260.9 ms | 5843.5 ms | 417.5 ms | 2460.7 ms |
| Uber_zap | Go | 5456.5 ms | 5010.6 ms | 445.9 ms | 2127.6 ms |
| K8s_workqueue | Go | 4781.9 ms | 4343.2 ms | 438.7 ms | 1705.3 ms |
| Toml | Go | 2077.7 ms | 1841.8 ms | 236.0 ms | 953.9 ms |
| Dustin_humanize | Go | 825.5 ms | 675.8 ms | 149.6 ms | 388.4 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTOGlobalDCE | 2379417.5 ms | 1286359.7 ms | 9 |
| LLGoFullLTONoGlobalDCE | 2361278.5 ms | 1334545.6 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2232906.5 ms | 1235460.3 ms | 9 |
| LLGoDeadcodeDrop | 2083709.5 ms | 685286.3 ms | 9 |
| LLGoNoLTO | 2027529.1 ms | 661495.3 ms | 9 |
| Go | 165325.1 ms | 50166.1 ms | 9 |

Dependency download details are in `download-timings.log`.
