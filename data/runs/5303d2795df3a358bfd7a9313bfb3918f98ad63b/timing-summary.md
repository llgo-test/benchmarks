## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 611982.0 ms | 602296.5 ms | 9685.5 ms | 317776.4 ms |
| IXGo | LLGoFullLTOGlobalDCE | 523062.6 ms | 513051.5 ms | 10011.1 ms | 277192.8 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 521845.4 ms | 512310.4 ms | 9535.0 ms | 277457.5 ms |
| IXGo | LLGoDeadcodeDrop | 474966.2 ms | 462967.6 ms | 11998.6 ms | 144996.9 ms |
| IXGo | LLGoNoLTO | 400791.0 ms | 391779.2 ms | 9011.8 ms | 114829.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 242360.5 ms | 237854.6 ms | 4505.9 ms | 157239.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 232427.6 ms | 227388.4 ms | 5039.2 ms | 149833.6 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 230141.6 ms | 225791.3 ms | 4350.3 ms | 149578.5 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 194626.1 ms | 191560.2 ms | 3065.9 ms | 118003.2 ms |
| Aws_restjson | LLGoDeadcodeDrop | 188833.4 ms | 185818.7 ms | 3014.7 ms | 65639.3 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 183255.4 ms | 180245.3 ms | 3010.1 ms | 102649.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 176609.0 ms | 173700.4 ms | 2908.6 ms | 101251.6 ms |
| Aws_restjson | LLGoNoLTO | 175408.8 ms | 172702.9 ms | 2705.9 ms | 61045.4 ms |
| XGo | LLGoFullLTOGlobalDCE | 167559.7 ms | 164556.9 ms | 3002.8 ms | 122863.3 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 163675.1 ms | 160704.5 ms | 2970.6 ms | 117735.8 ms |
| XGo | LLGoFullLTONoGlobalDCE | 162188.3 ms | 159235.6 ms | 2952.7 ms | 118785.7 ms |
| Etcdctl | LLGoDeadcodeDrop | 160680.3 ms | 156161.8 ms | 4518.6 ms | 54606.9 ms |
| Etcdctl | LLGoNoLTO | 160499.7 ms | 156742.3 ms | 3757.4 ms | 53400.6 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 154616.3 ms | 152072.0 ms | 2544.3 ms | 99790.8 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 151392.0 ms | 148745.1 ms | 2646.9 ms | 97466.4 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 149445.9 ms | 146892.7 ms | 2553.2 ms | 96361.4 ms |
| Uber_zap | LLGoDeadcodeDrop | 147860.2 ms | 145192.1 ms | 2668.2 ms | 56554.0 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 146580.7 ms | 144004.6 ms | 2576.1 ms | 90397.2 ms |
| Uber_zap | LLGoNoLTO | 143735.3 ms | 141532.7 ms | 2202.6 ms | 53821.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 143607.3 ms | 140905.9 ms | 2701.4 ms | 87914.9 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 142527.9 ms | 139997.7 ms | 2530.3 ms | 87592.0 ms |
| K8s_workqueue | LLGoNoLTO | 138831.8 ms | 136408.6 ms | 2423.2 ms | 52323.4 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 138245.0 ms | 135624.0 ms | 2621.0 ms | 52974.4 ms |
| XGo | LLGoDeadcodeDrop | 94116.5 ms | 91119.3 ms | 2997.2 ms | 35893.6 ms |
| XGo | LLGoNoLTO | 93048.2 ms | 90524.2 ms | 2524.0 ms | 35382.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 79094.7 ms | 77443.4 ms | 1651.3 ms | 48135.8 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 78173.3 ms | 76536.3 ms | 1637.1 ms | 48089.3 ms |
| Gorm_schema | LLGoDeadcodeDrop | 76911.1 ms | 75208.0 ms | 1703.1 ms | 25796.7 ms |
| Gorm_schema | LLGoNoLTO | 75360.4 ms | 73930.4 ms | 1430.0 ms | 25045.7 ms |
| Toml | LLGoFullLTONoGlobalDCE | 71871.8 ms | 70154.5 ms | 1717.3 ms | 43520.9 ms |
| Toml | LLGoNoLTO | 71451.6 ms | 69922.8 ms | 1528.8 ms | 23581.2 ms |
| Toml | LLGoDeadcodeDrop | 70744.9 ms | 68995.0 ms | 1749.9 ms | 23778.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 69837.9 ms | 68252.4 ms | 1585.4 ms | 37961.6 ms |
| Toml | LLGoFullLTOGlobalDCE | 66942.9 ms | 65262.0 ms | 1680.9 ms | 36903.2 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 65484.1 ms | 63825.7 ms | 1658.4 ms | 36512.0 ms |
| IXGo | Go | 62571.9 ms | 58441.8 ms | 4130.1 ms | 17256.5 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 50794.4 ms | 49615.5 ms | 1178.9 ms | 32785.3 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 50227.7 ms | 48986.1 ms | 1241.7 ms | 18413.9 ms |
| Dustin_humanize | LLGoNoLTO | 48693.6 ms | 47610.3 ms | 1083.2 ms | 17598.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 42745.4 ms | 41599.6 ms | 1145.8 ms | 24265.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 42663.4 ms | 41536.1 ms | 1127.3 ms | 24710.6 ms |
| Etcdctl | Go | 25483.5 ms | 23724.0 ms | 1759.6 ms | 8063.5 ms |
| XGo | Go | 14393.8 ms | 13447.6 ms | 946.2 ms | 4304.3 ms |
| Aws_restjson | Go | 6095.9 ms | 5495.9 ms | 600.0 ms | 2656.5 ms |
| Gorm_schema | Go | 4359.2 ms | 4018.8 ms | 340.4 ms | 1821.2 ms |
| Uber_zap | Go | 4041.2 ms | 3692.9 ms | 348.3 ms | 1882.3 ms |
| K8s_workqueue | Go | 3531.4 ms | 3122.1 ms | 409.2 ms | 1272.6 ms |
| Toml | Go | 1579.0 ms | 1352.9 ms | 226.1 ms | 773.9 ms |
| Dustin_humanize | Go | 610.4 ms | 477.3 ms | 133.0 ms | 311.6 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTOGlobalDCEPlugin | 1652949.1 ms | 963648.5 ms | 9 |
| LLGoFullLTONoGlobalDCE | 1613703.2 ms | 984372.8 ms | 9 |
| LLGoFullLTOGlobalDCE | 1598859.1 ms | 954753.7 ms | 9 |
| LLGoDeadcodeDrop | 1402585.5 ms | 478654.0 ms | 9 |
| LLGoNoLTO | 1307820.3 ms | 437027.8 ms | 9 |
| Go | 122666.2 ms | 38342.4 ms | 9 |

Dependency download details are in `download-timings.log`.
