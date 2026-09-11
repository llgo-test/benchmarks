## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 832823.9 ms | 825590.7 ms | 7233.1 ms | 564882.7 ms |
| IXGo | LLGoFullLTOGlobalDCE | 690429.1 ms | 683743.2 ms | 6685.9 ms | 453670.7 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 652380.3 ms | 645934.0 ms | 6446.3 ms | 429688.0 ms |
| IXGo | LLGoDeadcodeDrop | 451854.3 ms | 445802.2 ms | 6052.1 ms | 151427.8 ms |
| IXGo | LLGoNoLTO | 446917.7 ms | 440856.2 ms | 6061.5 ms | 147498.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 281056.6 ms | 276097.6 ms | 4958.9 ms | 171110.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 280465.5 ms | 275613.7 ms | 4851.8 ms | 171716.6 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 270123.5 ms | 265450.2 ms | 4673.3 ms | 165222.1 ms |
| Etcdctl | LLGoDeadcodeDrop | 203727.7 ms | 199595.4 ms | 4132.3 ms | 67260.8 ms |
| Etcdctl | LLGoNoLTO | 198936.5 ms | 194775.1 ms | 4161.3 ms | 65332.8 ms |
| XGo | LLGoFullLTONoGlobalDCE | 184892.2 ms | 181790.8 ms | 3101.5 ms | 130481.8 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 184707.8 ms | 181591.9 ms | 3116.0 ms | 128686.0 ms |
| XGo | LLGoFullLTOGlobalDCE | 182639.3 ms | 179425.2 ms | 3214.1 ms | 127322.6 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 142314.4 ms | 140034.3 ms | 2280.1 ms | 104842.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 139581.6 ms | 137019.2 ms | 2562.4 ms | 98918.3 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 134575.6 ms | 132335.0 ms | 2240.6 ms | 95439.5 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 114737.1 ms | 112738.8 ms | 1998.3 ms | 88604.6 ms |
| XGo | LLGoDeadcodeDrop | 111828.5 ms | 109078.5 ms | 2750.0 ms | 41662.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 111622.6 ms | 109734.2 ms | 1888.3 ms | 83770.7 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 111083.8 ms | 109238.2 ms | 1845.6 ms | 87406.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 108731.5 ms | 106830.1 ms | 1901.4 ms | 85125.9 ms |
| XGo | LLGoNoLTO | 108648.3 ms | 105810.8 ms | 2837.5 ms | 40502.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 107981.6 ms | 106154.5 ms | 1827.1 ms | 80623.8 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 96310.2 ms | 94577.4 ms | 1732.9 ms | 72330.3 ms |
| Aws_restjson | LLGoDeadcodeDrop | 83539.6 ms | 81513.8 ms | 2025.8 ms | 38534.3 ms |
| Aws_restjson | LLGoNoLTO | 83153.3 ms | 81088.6 ms | 2064.7 ms | 38674.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 68004.3 ms | 66596.2 ms | 1408.1 ms | 47538.5 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 67976.5 ms | 66647.1 ms | 1329.5 ms | 47938.1 ms |
| Uber_zap | LLGoDeadcodeDrop | 58696.5 ms | 57160.9 ms | 1535.6 ms | 25834.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 57504.7 ms | 56167.6 ms | 1337.1 ms | 36692.4 ms |
| Uber_zap | LLGoNoLTO | 56954.2 ms | 55405.2 ms | 1549.1 ms | 25066.4 ms |
| Toml | LLGoFullLTONoGlobalDCE | 53528.7 ms | 52456.8 ms | 1071.8 ms | 41442.6 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 51362.2 ms | 49879.4 ms | 1482.8 ms | 23922.1 ms |
| K8s_workqueue | LLGoNoLTO | 50971.9 ms | 49450.4 ms | 1521.4 ms | 23351.7 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 48834.1 ms | 47675.8 ms | 1158.3 ms | 35342.4 ms |
| Toml | LLGoFullLTOGlobalDCE | 47448.9 ms | 46405.2 ms | 1043.7 ms | 34688.1 ms |
| IXGo | Go | 46669.0 ms | 43629.8 ms | 3039.3 ms | 13375.7 ms |
| Gorm_schema | LLGoDeadcodeDrop | 39506.2 ms | 38294.5 ms | 1211.7 ms | 12879.7 ms |
| Gorm_schema | LLGoNoLTO | 37869.8 ms | 36725.2 ms | 1144.6 ms | 12252.8 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 34045.4 ms | 33196.3 ms | 849.2 ms | 26758.8 ms |
| Etcdctl | Go | 33707.6 ms | 31632.3 ms | 2075.3 ms | 10142.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 25480.0 ms | 24651.0 ms | 829.0 ms | 17947.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 25334.8 ms | 24514.6 ms | 820.2 ms | 17718.8 ms |
| Toml | LLGoDeadcodeDrop | 24129.4 ms | 23154.7 ms | 974.7 ms | 9077.7 ms |
| Toml | LLGoNoLTO | 23569.9 ms | 22637.5 ms | 932.4 ms | 8931.0 ms |
| XGo | Go | 19332.4 ms | 18131.7 ms | 1200.7 ms | 5654.8 ms |
| Dustin_humanize | LLGoNoLTO | 13722.0 ms | 12978.5 ms | 743.4 ms | 5776.6 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 13693.5 ms | 12956.2 ms | 737.3 ms | 5838.3 ms |
| Aws_restjson | Go | 7925.4 ms | 7251.0 ms | 674.5 ms | 3187.0 ms |
| Gorm_schema | Go | 5746.8 ms | 5365.2 ms | 381.6 ms | 2180.4 ms |
| Uber_zap | Go | 5464.8 ms | 4995.5 ms | 469.2 ms | 2138.3 ms |
| K8s_workqueue | Go | 4881.5 ms | 4412.3 ms | 469.2 ms | 1760.3 ms |
| Toml | Go | 2101.8 ms | 1860.2 ms | 241.6 ms | 963.8 ms |
| Dustin_humanize | Go | 795.1 ms | 655.0 ms | 140.1 ms | 381.2 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTOGlobalDCEPlugin | 1777185.3 ms | 1210058.3 ms | 9 |
| LLGoFullLTOGlobalDCE | 1646346.8 ms | 1113466.8 ms | 9 |
| LLGoFullLTONoGlobalDCE | 1631081.9 ms | 1122384.8 ms | 9 |
| LLGoDeadcodeDrop | 1038338.0 ms | 376438.3 ms | 9 |
| LLGoNoLTO | 1020743.5 ms | 367386.3 ms | 9 |
| Go | 126624.5 ms | 39784.2 ms | 9 |

Dependency download details are in `download-timings.log`.
