## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTONoGlobalDCE | 536230.9 ms | 524687.3 ms | 11543.6 ms | 284447.4 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 523136.5 ms | 511493.8 ms | 11642.7 ms | 276924.5 ms |
| IXGo | LLGoFullLTOGlobalDCE | 513965.1 ms | 501762.5 ms | 12202.6 ms | 270977.0 ms |
| IXGo | LLGoDeadcodeDrop | 414140.0 ms | 403648.9 ms | 10491.1 ms | 123650.5 ms |
| IXGo | LLGoNoLTO | 398060.6 ms | 388526.6 ms | 9534.0 ms | 117753.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 266420.7 ms | 261418.2 ms | 5002.5 ms | 164337.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 255576.5 ms | 250951.0 ms | 4625.5 ms | 156082.0 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 254291.0 ms | 249776.4 ms | 4514.7 ms | 156948.8 ms |
| Etcdctl | LLGoDeadcodeDrop | 191382.8 ms | 187192.3 ms | 4190.6 ms | 63362.5 ms |
| Etcdctl | LLGoNoLTO | 188914.4 ms | 184950.1 ms | 3964.3 ms | 62055.5 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 178994.2 ms | 175656.3 ms | 3337.9 ms | 123590.7 ms |
| XGo | LLGoFullLTONoGlobalDCE | 176177.0 ms | 172925.6 ms | 3251.4 ms | 121961.4 ms |
| XGo | LLGoFullLTOGlobalDCE | 176055.1 ms | 172892.5 ms | 3162.6 ms | 120410.0 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 134741.9 ms | 132397.7 ms | 2344.2 ms | 97108.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 123579.2 ms | 121153.7 ms | 2425.5 ms | 85010.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 121698.7 ms | 119435.9 ms | 2262.8 ms | 83818.1 ms |
| XGo | LLGoDeadcodeDrop | 109286.0 ms | 106519.4 ms | 2766.7 ms | 40575.4 ms |
| XGo | LLGoNoLTO | 109258.1 ms | 106472.9 ms | 2785.2 ms | 40058.8 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 106979.7 ms | 105256.7 ms | 1723.1 ms | 81123.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 98734.6 ms | 96613.9 ms | 2120.7 ms | 71852.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 97951.9 ms | 96168.8 ms | 1783.2 ms | 70635.2 ms |
| IXGo | Go | 83119.7 ms | 78058.2 ms | 5061.5 ms | 23369.7 ms |
| Aws_restjson | LLGoDeadcodeDrop | 82323.6 ms | 80078.5 ms | 2245.1 ms | 37235.5 ms |
| Aws_restjson | LLGoNoLTO | 81978.2 ms | 79841.5 ms | 2136.7 ms | 36770.2 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 61802.3 ms | 60420.6 ms | 1381.7 ms | 41915.7 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 61584.3 ms | 60261.0 ms | 1323.3 ms | 41372.2 ms |
| Uber_zap | LLGoDeadcodeDrop | 57280.5 ms | 55703.0 ms | 1577.6 ms | 24337.0 ms |
| Uber_zap | LLGoNoLTO | 55801.9 ms | 54373.6 ms | 1428.2 ms | 24073.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 51871.9 ms | 50504.8 ms | 1367.1 ms | 31397.3 ms |
| Toml | LLGoFullLTONoGlobalDCE | 48599.4 ms | 47514.6 ms | 1084.9 ms | 36498.1 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 41999.1 ms | 40847.1 ms | 1152.0 ms | 28989.3 ms |
| Toml | LLGoFullLTOGlobalDCE | 40879.6 ms | 39786.4 ms | 1093.3 ms | 28633.2 ms |
| Gorm_schema | LLGoDeadcodeDrop | 39911.9 ms | 38718.7 ms | 1193.2 ms | 13361.2 ms |
| Gorm_schema | LLGoNoLTO | 39272.9 ms | 38092.8 ms | 1180.0 ms | 12902.7 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 34362.1 ms | 33494.5 ms | 867.6 ms | 26618.8 ms |
| Etcdctl | Go | 33599.2 ms | 31338.7 ms | 2260.4 ms | 10824.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 26070.4 ms | 25184.1 ms | 886.4 ms | 18152.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 25917.6 ms | 25036.0 ms | 881.6 ms | 17948.1 ms |
| Toml | LLGoDeadcodeDrop | 25452.8 ms | 24392.3 ms | 1060.5 ms | 9537.0 ms |
| Toml | LLGoNoLTO | 24024.1 ms | 23060.8 ms | 963.3 ms | 8929.0 ms |
| XGo | Go | 18789.6 ms | 17580.4 ms | 1209.2 ms | 5601.3 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 14291.3 ms | 13558.2 ms | 733.1 ms | 5967.2 ms |
| Dustin_humanize | LLGoNoLTO | 13800.9 ms | 13081.7 ms | 719.2 ms | 5766.0 ms |
| Aws_restjson | Go | 7843.4 ms | 7177.6 ms | 665.8 ms | 3168.5 ms |
| Gorm_schema | Go | 5720.0 ms | 5327.3 ms | 392.6 ms | 2184.5 ms |
| Uber_zap | Go | 5264.2 ms | 4874.8 ms | 389.4 ms | 2020.8 ms |
| K8s_workqueue | Go | 4684.9 ms | 4219.8 ms | 465.1 ms | 1661.2 ms |
| Toml | Go | 2026.7 ms | 1765.2 ms | 261.5 ms | 917.2 ms |
| Dustin_humanize | Go | 826.6 ms | 686.7 ms | 140.0 ms | 423.0 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1353184.3 ms | 846622.3 ms | 8 |
| LLGoFullLTOGlobalDCE | 1305255.8 ms | 799348.6 ms | 8 |
| LLGoFullLTOGlobalDCEPlugin | 1299179.8 ms | 790781.3 ms | 8 |
| LLGoDeadcodeDrop | 934069.1 ms | 318026.5 ms | 8 |
| LLGoNoLTO | 911111.1 ms | 308308.9 ms | 8 |
| Go | 161874.3 ms | 50170.9 ms | 9 |

Dependency download details are in `download-timings.log`.
