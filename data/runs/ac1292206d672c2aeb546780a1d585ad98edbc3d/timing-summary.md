## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 699382.6 ms | 682294.6 ms | 17088.0 ms | 465669.4 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 664661.8 ms | 647345.9 ms | 17316.0 ms | 449505.0 ms |
| IXGo | LLGoFullLTOGlobalDCE | 662200.2 ms | 645713.1 ms | 16487.1 ms | 447996.5 ms |
| IXGo | LLGoDeadcodeDrop | 377297.3 ms | 359716.5 ms | 17580.8 ms | 122873.4 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 365992.7 ms | 358056.4 ms | 7936.3 ms | 276519.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 365622.1 ms | 357742.2 ms | 7879.9 ms | 275621.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 364413.9 ms | 356665.8 ms | 7748.2 ms | 275097.7 ms |
| IXGo | LLGoNoLTO | 358631.0 ms | 344170.5 ms | 14460.5 ms | 112669.9 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 273624.1 ms | 268756.9 ms | 4867.2 ms | 188360.4 ms |
| XGo | LLGoFullLTONoGlobalDCE | 268995.9 ms | 263707.5 ms | 5288.4 ms | 220324.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 251877.9 ms | 247214.7 ms | 4663.2 ms | 164058.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 250497.3 ms | 245640.0 ms | 4857.3 ms | 164505.6 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 243433.3 ms | 238118.4 ms | 5314.9 ms | 192870.6 ms |
| XGo | LLGoFullLTOGlobalDCE | 236950.6 ms | 231878.6 ms | 5072.0 ms | 188047.2 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 225285.9 ms | 221050.1 ms | 4235.8 ms | 162273.8 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 224639.1 ms | 220416.7 ms | 4222.4 ms | 163212.1 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 223896.1 ms | 219677.1 ms | 4219.0 ms | 161710.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 214515.9 ms | 210380.2 ms | 4135.7 ms | 149456.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 205261.3 ms | 201209.0 ms | 4052.3 ms | 141665.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 194834.5 ms | 190872.0 ms | 3962.5 ms | 133165.0 ms |
| Aws_restjson | LLGoDeadcodeDrop | 182846.7 ms | 178882.3 ms | 3964.4 ms | 59016.8 ms |
| Aws_restjson | LLGoNoLTO | 176986.7 ms | 173478.5 ms | 3508.2 ms | 55349.8 ms |
| Etcdctl | LLGoDeadcodeDrop | 176906.9 ms | 170105.7 ms | 6801.2 ms | 62326.8 ms |
| Etcdctl | LLGoNoLTO | 176277.5 ms | 170166.6 ms | 6110.9 ms | 60822.6 ms |
| Uber_zap | LLGoNoLTO | 149741.4 ms | 146566.9 ms | 3174.5 ms | 48057.7 ms |
| Uber_zap | LLGoDeadcodeDrop | 146962.4 ms | 143526.1 ms | 3436.3 ms | 48959.0 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 139334.6 ms | 136271.3 ms | 3063.3 ms | 46320.9 ms |
| K8s_workqueue | LLGoNoLTO | 138085.2 ms | 135092.0 ms | 2993.3 ms | 44303.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 116652.4 ms | 114056.4 ms | 2596.0 ms | 81750.1 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 114281.8 ms | 111804.3 ms | 2477.5 ms | 81254.7 ms |
| Toml | LLGoFullLTONoGlobalDCE | 109380.5 ms | 106996.4 ms | 2384.1 ms | 76724.7 ms |
| XGo | LLGoDeadcodeDrop | 97947.3 ms | 93454.4 ms | 4492.9 ms | 36645.9 ms |
| Toml | LLGoFullLTOGlobalDCE | 95864.0 ms | 93525.0 ms | 2339.0 ms | 62690.4 ms |
| XGo | LLGoNoLTO | 95204.3 ms | 91585.6 ms | 3618.7 ms | 35577.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 94500.8 ms | 92203.6 ms | 2297.1 ms | 60434.7 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 90254.0 ms | 88115.2 ms | 2138.8 ms | 59052.5 ms |
| Gorm_schema | LLGoNoLTO | 81339.0 ms | 79194.7 ms | 2144.3 ms | 28469.6 ms |
| Gorm_schema | LLGoDeadcodeDrop | 80092.4 ms | 77960.5 ms | 2131.9 ms | 28318.2 ms |
| Toml | LLGoDeadcodeDrop | 74650.9 ms | 72763.4 ms | 1887.6 ms | 26084.8 ms |
| Toml | LLGoNoLTO | 74314.4 ms | 72376.9 ms | 1937.5 ms | 25844.1 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 74182.6 ms | 72577.8 ms | 1604.8 ms | 54195.4 ms |
| IXGo | Go | 64748.6 ms | 56063.9 ms | 8684.7 ms | 17953.9 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 61588.9 ms | 60044.7 ms | 1544.2 ms | 40625.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 61430.5 ms | 59937.5 ms | 1493.0 ms | 40459.3 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 52351.7 ms | 50901.2 ms | 1450.5 ms | 19961.9 ms |
| Dustin_humanize | LLGoNoLTO | 51843.5 ms | 50500.3 ms | 1343.2 ms | 19609.8 ms |
| Etcdctl | Go | 26273.5 ms | 23208.8 ms | 3064.8 ms | 7978.3 ms |
| XGo | Go | 14946.4 ms | 13150.0 ms | 1796.4 ms | 4570.1 ms |
| Aws_restjson | Go | 6101.0 ms | 5250.2 ms | 850.8 ms | 2488.9 ms |
| Gorm_schema | Go | 4495.2 ms | 3905.6 ms | 589.6 ms | 1757.3 ms |
| Uber_zap | Go | 4136.7 ms | 3620.3 ms | 516.4 ms | 1785.9 ms |
| K8s_workqueue | Go | 3615.4 ms | 3140.5 ms | 474.9 ms | 1434.1 ms |
| Toml | Go | 1558.8 ms | 1341.6 ms | 217.2 ms | 733.9 ms |
| Dustin_humanize | Go | 622.8 ms | 510.5 ms | 112.4 ms | 312.3 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2321044.5 ms | 1672369.3 ms | 9 |
| LLGoFullLTOGlobalDCE | 2227801.4 ms | 1571266.7 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2205374.8 ms | 1533610.3 ms | 9 |
| LLGoDeadcodeDrop | 1328390.3 ms | 450507.7 ms | 9 |
| LLGoNoLTO | 1302422.9 ms | 430704.7 ms | 9 |
| Go | 126498.4 ms | 39014.7 ms | 9 |

Dependency download details are in `download-timings.log`.
