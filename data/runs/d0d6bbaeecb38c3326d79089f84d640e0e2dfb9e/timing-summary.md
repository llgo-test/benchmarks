## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 682626.9 ms | 670078.0 ms | 12548.9 ms | 358127.8 ms |
| IXGo | LLGoFullLTOGlobalDCE | 650942.7 ms | 638366.4 ms | 12576.2 ms | 344027.0 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 649200.8 ms | 637636.7 ms | 11564.1 ms | 345390.7 ms |
| IXGo | LLGoNoLTO | 502383.5 ms | 491412.7 ms | 10970.8 ms | 143683.7 ms |
| IXGo | LLGoDeadcodeDrop | 493816.7 ms | 479604.4 ms | 14212.3 ms | 146888.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 303026.4 ms | 297297.8 ms | 5728.7 ms | 192417.4 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 299766.4 ms | 294123.8 ms | 5642.6 ms | 192667.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 299013.7 ms | 292986.4 ms | 6027.3 ms | 191156.7 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 233659.2 ms | 230079.6 ms | 3579.6 ms | 143455.3 ms |
| Aws_restjson | LLGoDeadcodeDrop | 226835.8 ms | 223571.2 ms | 3264.6 ms | 78510.1 ms |
| Aws_restjson | LLGoNoLTO | 223587.0 ms | 220411.0 ms | 3176.0 ms | 77931.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 220567.3 ms | 216975.0 ms | 3592.3 ms | 127977.3 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 218476.7 ms | 214808.7 ms | 3668.0 ms | 127560.0 ms |
| XGo | LLGoFullLTOGlobalDCE | 210996.3 ms | 207268.7 ms | 3727.6 ms | 151670.9 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 210514.3 ms | 206832.1 ms | 3682.3 ms | 151079.1 ms |
| XGo | LLGoFullLTONoGlobalDCE | 210432.0 ms | 206847.7 ms | 3584.3 ms | 152085.7 ms |
| Etcdctl | LLGoDeadcodeDrop | 208635.9 ms | 203189.3 ms | 5446.6 ms | 68971.0 ms |
| Etcdctl | LLGoNoLTO | 206940.2 ms | 202460.0 ms | 4480.2 ms | 67168.8 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 193459.5 ms | 190349.2 ms | 3110.2 ms | 125420.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 188203.9 ms | 185076.1 ms | 3127.8 ms | 121611.7 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 187183.7 ms | 183935.6 ms | 3248.1 ms | 122115.4 ms |
| Uber_zap | LLGoNoLTO | 183999.5 ms | 181359.9 ms | 2639.7 ms | 68196.8 ms |
| Uber_zap | LLGoDeadcodeDrop | 183474.4 ms | 180769.8 ms | 2704.7 ms | 68139.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 182498.9 ms | 179369.5 ms | 3129.4 ms | 112751.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 181754.5 ms | 178555.6 ms | 3198.9 ms | 112454.5 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 176823.7 ms | 174121.6 ms | 2702.1 ms | 65974.9 ms |
| K8s_workqueue | LLGoNoLTO | 174620.4 ms | 171873.2 ms | 2747.2 ms | 64823.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 170080.0 ms | 166985.2 ms | 3094.8 ms | 103841.0 ms |
| XGo | LLGoDeadcodeDrop | 119137.6 ms | 115637.9 ms | 3499.7 ms | 44289.9 ms |
| XGo | LLGoNoLTO | 117854.6 ms | 114998.8 ms | 2855.7 ms | 42061.9 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 99817.6 ms | 97823.7 ms | 1994.0 ms | 61498.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 99393.5 ms | 97326.8 ms | 2066.8 ms | 60547.3 ms |
| Gorm_schema | LLGoDeadcodeDrop | 97964.0 ms | 96196.2 ms | 1767.8 ms | 32634.6 ms |
| Gorm_schema | LLGoNoLTO | 96113.8 ms | 94252.4 ms | 1861.3 ms | 32027.4 ms |
| Toml | LLGoFullLTONoGlobalDCE | 90984.3 ms | 89084.2 ms | 1900.1 ms | 55679.0 ms |
| Toml | LLGoDeadcodeDrop | 90621.9 ms | 88923.4 ms | 1698.5 ms | 30157.5 ms |
| Toml | LLGoNoLTO | 89709.6 ms | 88055.2 ms | 1654.4 ms | 30012.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 88334.6 ms | 86437.0 ms | 1897.7 ms | 48169.9 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 82715.9 ms | 80812.1 ms | 1903.8 ms | 45849.6 ms |
| IXGo | Go | 82172.6 ms | 76244.7 ms | 5927.8 ms | 22519.6 ms |
| Toml | LLGoFullLTOGlobalDCE | 81183.5 ms | 79350.5 ms | 1833.0 ms | 45595.4 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 64652.0 ms | 63303.2 ms | 1348.8 ms | 41468.9 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 62920.6 ms | 61708.3 ms | 1212.3 ms | 22772.1 ms |
| Dustin_humanize | LLGoNoLTO | 62259.4 ms | 61075.8 ms | 1183.6 ms | 22483.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 54597.4 ms | 53247.2 ms | 1350.2 ms | 30947.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 54006.0 ms | 52745.5 ms | 1260.5 ms | 30742.2 ms |
| Etcdctl | Go | 33196.4 ms | 30989.3 ms | 2207.1 ms | 9994.5 ms |
| XGo | Go | 19170.0 ms | 17889.5 ms | 1280.5 ms | 5592.7 ms |
| Aws_restjson | Go | 7998.8 ms | 7298.6 ms | 700.3 ms | 3187.1 ms |
| Gorm_schema | Go | 5798.8 ms | 5393.4 ms | 405.4 ms | 2180.9 ms |
| Uber_zap | Go | 5358.1 ms | 4936.8 ms | 421.3 ms | 2069.4 ms |
| K8s_workqueue | Go | 4728.4 ms | 4288.4 ms | 439.9 ms | 1680.7 ms |
| Toml | Go | 2090.2 ms | 1852.1 ms | 238.1 ms | 1167.0 ms |
| Dustin_humanize | Go | 795.9 ms | 685.3 ms | 110.6 ms | 381.2 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2029155.7 ms | 1239781.0 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1992871.1 ms | 1170744.0 ms | 9 |
| LLGoFullLTOGlobalDCE | 1986061.4 ms | 1185783.1 ms | 9 |
| LLGoDeadcodeDrop | 1660230.6 ms | 558337.6 ms | 9 |
| LLGoNoLTO | 1657467.9 ms | 548388.8 ms | 9 |
| Go | 161309.2 ms | 48773.0 ms | 9 |

Dependency download details are in `download-timings.log`.
