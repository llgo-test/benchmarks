## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTONoGlobalDCE | 785632.6 ms | 773639.7 ms | 11992.9 ms | 485960.1 ms |
| IXGo | LLGoFullLTOGlobalDCE | 743250.6 ms | 731907.4 ms | 11343.2 ms | 463533.5 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 706234.1 ms | 694896.6 ms | 11337.5 ms | 454943.9 ms |
| IXGo | LLGoNoLTO | 469817.1 ms | 460563.9 ms | 9253.3 ms | 137417.0 ms |
| IXGo | LLGoDeadcodeDrop | 415658.8 ms | 403106.4 ms | 12552.4 ms | 128074.5 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 337400.1 ms | 332088.8 ms | 5311.3 ms | 256071.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 335748.7 ms | 330665.2 ms | 5083.6 ms | 255043.9 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 335533.9 ms | 330280.7 ms | 5253.3 ms | 257581.7 ms |
| XGo | LLGoFullLTONoGlobalDCE | 251481.5 ms | 247528.7 ms | 3952.8 ms | 207999.3 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 251274.4 ms | 247665.0 ms | 3609.4 ms | 178689.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 224823.3 ms | 221327.9 ms | 3495.5 ms | 152488.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 223365.9 ms | 219847.8 ms | 3518.1 ms | 150262.4 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 221387.3 ms | 217720.9 ms | 3666.4 ms | 176198.6 ms |
| XGo | LLGoFullLTOGlobalDCE | 220438.6 ms | 216731.5 ms | 3707.1 ms | 176633.1 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 208009.7 ms | 204851.9 ms | 3157.8 ms | 154705.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 205517.2 ms | 202175.6 ms | 3341.6 ms | 152978.0 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 204612.4 ms | 201294.9 ms | 3317.5 ms | 152518.2 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 188135.3 ms | 185085.1 ms | 3050.3 ms | 133474.9 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 186295.7 ms | 183195.4 ms | 3100.3 ms | 131905.0 ms |
| Aws_restjson | LLGoNoLTO | 176639.4 ms | 173827.8 ms | 2811.6 ms | 59038.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 174085.4 ms | 171078.1 ms | 3007.3 ms | 122530.3 ms |
| Aws_restjson | LLGoDeadcodeDrop | 169544.0 ms | 166431.8 ms | 3112.2 ms | 57591.0 ms |
| Etcdctl | LLGoNoLTO | 162789.9 ms | 158565.8 ms | 4224.1 ms | 55918.6 ms |
| Etcdctl | LLGoDeadcodeDrop | 159151.0 ms | 154496.6 ms | 4654.4 ms | 55829.6 ms |
| Uber_zap | LLGoDeadcodeDrop | 143955.3 ms | 141279.3 ms | 2676.0 ms | 52931.2 ms |
| Uber_zap | LLGoNoLTO | 138217.0 ms | 135733.1 ms | 2483.9 ms | 49864.3 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 132881.6 ms | 130146.7 ms | 2734.9 ms | 48607.0 ms |
| K8s_workqueue | LLGoNoLTO | 132090.1 ms | 129577.9 ms | 2512.2 ms | 47818.4 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 112005.8 ms | 109907.3 ms | 2098.5 ms | 81621.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 110942.0 ms | 108890.8 ms | 2051.1 ms | 80161.6 ms |
| Toml | LLGoFullLTONoGlobalDCE | 106671.9 ms | 104508.3 ms | 2163.6 ms | 76814.4 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 93455.9 ms | 91395.5 ms | 2060.4 ms | 62367.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 92532.4 ms | 90647.0 ms | 1885.4 ms | 61060.0 ms |
| Toml | LLGoFullLTOGlobalDCE | 88853.2 ms | 86800.7 ms | 2052.6 ms | 59011.5 ms |
| XGo | LLGoNoLTO | 88651.0 ms | 86042.2 ms | 2608.8 ms | 33478.0 ms |
| XGo | LLGoDeadcodeDrop | 88108.4 ms | 84840.0 ms | 3268.4 ms | 32714.7 ms |
| Gorm_schema | LLGoDeadcodeDrop | 79991.1 ms | 78034.4 ms | 1956.7 ms | 28146.0 ms |
| Gorm_schema | LLGoNoLTO | 77133.4 ms | 75547.1 ms | 1586.3 ms | 26634.4 ms |
| Toml | LLGoDeadcodeDrop | 74110.1 ms | 72263.4 ms | 1846.7 ms | 25783.9 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 73998.4 ms | 72487.2 ms | 1511.2 ms | 55486.7 ms |
| Toml | LLGoNoLTO | 73525.4 ms | 71722.2 ms | 1803.2 ms | 25331.3 ms |
| IXGo | Go | 62730.9 ms | 58507.6 ms | 4223.3 ms | 17448.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 57598.4 ms | 56222.8 ms | 1375.6 ms | 39050.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 57106.0 ms | 55669.0 ms | 1437.0 ms | 38401.4 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 51194.1 ms | 49817.0 ms | 1377.2 ms | 19503.5 ms |
| Dustin_humanize | LLGoNoLTO | 49951.3 ms | 48767.1 ms | 1184.2 ms | 18707.9 ms |
| Etcdctl | Go | 25243.5 ms | 23484.1 ms | 1759.4 ms | 8198.2 ms |
| XGo | Go | 14426.5 ms | 13412.4 ms | 1014.1 ms | 4480.9 ms |
| Aws_restjson | Go | 6033.8 ms | 5481.5 ms | 552.3 ms | 2497.4 ms |
| Gorm_schema | Go | 4309.6 ms | 3988.3 ms | 321.3 ms | 1685.1 ms |
| Uber_zap | Go | 4072.2 ms | 3725.8 ms | 346.3 ms | 1625.7 ms |
| K8s_workqueue | Go | 3540.8 ms | 3156.7 ms | 384.1 ms | 1638.1 ms |
| Toml | Go | 1553.5 ms | 1347.5 ms | 206.0 ms | 734.4 ms |
| Dustin_humanize | Go | 672.5 ms | 507.6 ms | 165.0 ms | 817.1 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2329220.6 ms | 1651377.1 ms | 9 |
| LLGoFullLTOGlobalDCE | 2173169.3 ms | 1508958.2 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2094000.8 ms | 1457158.4 ms | 9 |
| LLGoNoLTO | 1368814.6 ms | 454208.1 ms | 9 |
| LLGoDeadcodeDrop | 1314594.4 ms | 449181.4 ms | 9 |
| Go | 122583.4 ms | 39125.8 ms | 9 |

Dependency download details are in `download-timings.log`.
