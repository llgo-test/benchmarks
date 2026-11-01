## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoDeadcodeDrop | 507940.1 ms | 481150.6 ms | 26789.5 ms | 157634.3 ms |
| IXGo | LLGoNoLTO | 500659.8 ms | 478395.6 ms | 22264.2 ms | 151437.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 419825.0 ms | 407726.6 ms | 12098.4 ms | 304544.4 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 418395.0 ms | 406576.6 ms | 11818.4 ms | 305759.6 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 416412.3 ms | 404495.3 ms | 11917.0 ms | 301102.1 ms |
| XGo | LLGoFullLTONoGlobalDCE | 310658.1 ms | 302521.0 ms | 8137.1 ms | 247435.1 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 302684.8 ms | 296306.6 ms | 6378.1 ms | 207076.4 ms |
| XGo | LLGoFullLTOGlobalDCE | 279644.7 ms | 271729.8 ms | 7914.9 ms | 214322.7 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 270981.3 ms | 263323.5 ms | 7657.9 ms | 206511.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 268343.4 ms | 262204.5 ms | 6138.9 ms | 171820.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 262039.1 ms | 255729.3 ms | 6309.8 ms | 168186.6 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 243311.0 ms | 237862.6 ms | 5448.4 ms | 171424.1 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 239329.0 ms | 233870.8 ms | 5458.3 ms | 168681.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 237511.0 ms | 231889.0 ms | 5622.0 ms | 166779.1 ms |
| Etcdctl | LLGoDeadcodeDrop | 226078.5 ms | 215364.5 ms | 10714.1 ms | 76825.4 ms |
| Etcdctl | LLGoNoLTO | 220036.6 ms | 210240.3 ms | 9796.3 ms | 74670.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 217584.6 ms | 212347.5 ms | 5237.1 ms | 144635.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 215847.0 ms | 210595.0 ms | 5252.0 ms | 144203.1 ms |
| Aws_restjson | LLGoNoLTO | 208654.3 ms | 203549.6 ms | 5104.6 ms | 65021.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 207887.5 ms | 202811.6 ms | 5075.9 ms | 136455.7 ms |
| Aws_restjson | LLGoDeadcodeDrop | 207426.1 ms | 201728.0 ms | 5698.1 ms | 65170.0 ms |
| Uber_zap | LLGoDeadcodeDrop | 170751.3 ms | 166150.7 ms | 4600.5 ms | 54985.1 ms |
| Uber_zap | LLGoNoLTO | 169842.2 ms | 165695.9 ms | 4146.3 ms | 54323.1 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 166456.0 ms | 161729.2 ms | 4726.9 ms | 54126.3 ms |
| K8s_workqueue | LLGoNoLTO | 165608.5 ms | 161420.3 ms | 4188.3 ms | 53064.0 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 142779.5 ms | 139053.0 ms | 3726.5 ms | 99623.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 142011.1 ms | 138247.8 ms | 3763.3 ms | 97885.1 ms |
| Toml | LLGoFullLTONoGlobalDCE | 132717.2 ms | 129219.3 ms | 3497.9 ms | 92170.5 ms |
| XGo | LLGoDeadcodeDrop | 126721.5 ms | 119126.0 ms | 7595.4 ms | 44880.2 ms |
| XGo | LLGoNoLTO | 123907.5 ms | 117871.8 ms | 6035.7 ms | 44572.1 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 119073.4 ms | 115762.7 ms | 3310.7 ms | 76728.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 118963.3 ms | 115247.3 ms | 3716.0 ms | 74560.9 ms |
| Toml | LLGoFullLTOGlobalDCE | 117641.7 ms | 114310.3 ms | 3331.3 ms | 75979.2 ms |
| Gorm_schema | LLGoNoLTO | 107621.9 ms | 104438.7 ms | 3183.2 ms | 36422.0 ms |
| Gorm_schema | LLGoDeadcodeDrop | 105500.8 ms | 102100.2 ms | 3400.6 ms | 36216.7 ms |
| Toml | LLGoDeadcodeDrop | 101792.4 ms | 98837.1 ms | 2955.3 ms | 34455.5 ms |
| Toml | LLGoNoLTO | 100960.9 ms | 98152.9 ms | 2807.9 ms | 33900.9 ms |
| IXGo | Go | 96109.8 ms | 81246.9 ms | 14862.9 ms | 26213.1 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 94297.6 ms | 91816.2 ms | 2481.4 ms | 67987.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 75689.5 ms | 73442.0 ms | 2247.5 ms | 48785.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 73879.6 ms | 71722.2 ms | 2157.4 ms | 47673.0 ms |
| Dustin_humanize | LLGoNoLTO | 68695.0 ms | 66790.8 ms | 1904.2 ms | 25169.7 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 67336.1 ms | 65174.1 ms | 2162.1 ms | 24716.7 ms |
| Etcdctl | Go | 37796.6 ms | 32577.2 ms | 5219.4 ms | 11247.1 ms |
| XGo | Go | 22161.1 ms | 19050.2 ms | 3110.9 ms | 6527.1 ms |
| Aws_restjson | Go | 9310.5 ms | 7754.9 ms | 1555.7 ms | 3888.6 ms |
| Gorm_schema | Go | 6516.2 ms | 5542.9 ms | 973.3 ms | 2548.6 ms |
| Uber_zap | Go | 6028.0 ms | 5113.9 ms | 914.1 ms | 2472.1 ms |
| K8s_workqueue | Go | 5437.4 ms | 4459.7 ms | 977.7 ms | 1999.2 ms |
| Toml | Go | 2335.5 ms | 1898.7 ms | 436.9 ms | 1338.2 ms |
| Dustin_humanize | Go | 899.1 ms | 677.1 ms | 222.0 ms | 430.6 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1884172.1 ms | 1360158.7 ms | 8 |
| LLGoFullLTOGlobalDCE | 1744986.5 ms | 1216131.0 ms | 8 |
| LLGoFullLTOGlobalDCEPlugin | 1698348.0 ms | 1164042.7 ms | 8 |
| LLGoDeadcodeDrop | 1680002.8 ms | 549010.1 ms | 9 |
| LLGoNoLTO | 1665986.7 ms | 538581.3 ms | 9 |
| Go | 186594.3 ms | 56664.5 ms | 9 |

Dependency download details are in `download-timings.log`.
