## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoNoLTO | 504270.4 ms | 484712.0 ms | 19558.4 ms | 153844.0 ms |
| IXGo | LLGoDeadcodeDrop | 417431.6 ms | 393764.6 ms | 23667.0 ms | 128835.6 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 355388.4 ms | 344362.3 ms | 11026.1 ms | 266174.8 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 351951.5 ms | 341266.3 ms | 10685.2 ms | 262850.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 342451.8 ms | 331738.4 ms | 10713.4 ms | 253596.6 ms |
| XGo | LLGoFullLTONoGlobalDCE | 260087.6 ms | 252765.8 ms | 7321.8 ms | 210944.7 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 235153.7 ms | 229135.0 ms | 6018.6 ms | 164435.4 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 225142.8 ms | 217990.7 ms | 7152.1 ms | 175917.5 ms |
| XGo | LLGoFullLTOGlobalDCE | 221558.0 ms | 214631.9 ms | 6926.0 ms | 173091.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 210812.7 ms | 205090.4 ms | 5722.3 ms | 138026.3 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 209429.6 ms | 203472.8 ms | 5956.8 ms | 137508.5 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 198141.1 ms | 193098.9 ms | 5042.2 ms | 145310.7 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 193391.4 ms | 188391.6 ms | 4999.8 ms | 140373.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 183785.3 ms | 178694.1 ms | 5091.2 ms | 133391.9 ms |
| Aws_restjson | LLGoDeadcodeDrop | 182170.3 ms | 176807.6 ms | 5362.7 ms | 59949.1 ms |
| Etcdctl | LLGoNoLTO | 175260.7 ms | 166404.0 ms | 8856.7 ms | 59970.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 174603.5 ms | 169694.5 ms | 4909.0 ms | 120627.7 ms |
| Etcdctl | LLGoDeadcodeDrop | 173101.1 ms | 163155.0 ms | 9946.1 ms | 63563.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 172177.0 ms | 167140.7 ms | 5036.2 ms | 118404.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 164959.5 ms | 160202.0 ms | 4757.5 ms | 112423.4 ms |
| Aws_restjson | LLGoNoLTO | 164762.6 ms | 159979.3 ms | 4783.3 ms | 51665.9 ms |
| Uber_zap | LLGoNoLTO | 128649.4 ms | 124518.2 ms | 4131.2 ms | 41989.6 ms |
| Uber_zap | LLGoDeadcodeDrop | 126069.0 ms | 121727.8 ms | 4341.3 ms | 41539.7 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 124105.4 ms | 119822.9 ms | 4282.5 ms | 41137.3 ms |
| K8s_workqueue | LLGoNoLTO | 122403.1 ms | 118362.1 ms | 4041.0 ms | 40424.2 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 115353.2 ms | 111682.3 ms | 3670.9 ms | 83577.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 112929.9 ms | 109340.2 ms | 3589.7 ms | 80719.0 ms |
| Toml | LLGoFullLTONoGlobalDCE | 102856.4 ms | 99630.4 ms | 3225.9 ms | 72976.7 ms |
| XGo | LLGoNoLTO | 95736.0 ms | 90156.9 ms | 5579.2 ms | 35726.6 ms |
| XGo | LLGoDeadcodeDrop | 94539.9 ms | 88224.9 ms | 6315.0 ms | 34379.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 93149.5 ms | 89680.9 ms | 3468.6 ms | 60620.6 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 91399.7 ms | 88422.4 ms | 2977.3 ms | 60615.0 ms |
| Toml | LLGoFullLTOGlobalDCE | 90097.5 ms | 87041.4 ms | 3056.1 ms | 59955.5 ms |
| Gorm_schema | LLGoNoLTO | 81056.7 ms | 78124.6 ms | 2932.0 ms | 28144.3 ms |
| Gorm_schema | LLGoDeadcodeDrop | 79160.0 ms | 75959.8 ms | 3200.2 ms | 28293.9 ms |
| Toml | LLGoNoLTO | 75735.8 ms | 73133.4 ms | 2602.4 ms | 26016.8 ms |
| Toml | LLGoDeadcodeDrop | 75254.0 ms | 72533.1 ms | 2720.8 ms | 26228.2 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 74595.0 ms | 72316.4 ms | 2278.6 ms | 55288.2 ms |
| IXGo | Go | 74214.5 ms | 61378.1 ms | 12836.3 ms | 20589.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 59742.7 ms | 57604.1 ms | 2138.6 ms | 39757.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 58796.5 ms | 56664.1 ms | 2132.4 ms | 39493.8 ms |
| Dustin_humanize | LLGoNoLTO | 52408.6 ms | 50455.2 ms | 1953.4 ms | 19901.4 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 51072.5 ms | 49011.4 ms | 2061.0 ms | 19452.9 ms |
| Etcdctl | Go | 29064.7 ms | 24496.4 ms | 4568.2 ms | 9198.3 ms |
| XGo | Go | 16833.9 ms | 14173.7 ms | 2660.2 ms | 5042.0 ms |
| Aws_restjson | Go | 7141.3 ms | 5795.4 ms | 1345.9 ms | 3534.8 ms |
| Gorm_schema | Go | 5094.0 ms | 4238.7 ms | 855.3 ms | 2047.9 ms |
| Uber_zap | Go | 4644.4 ms | 3851.3 ms | 793.1 ms | 1930.8 ms |
| K8s_workqueue | Go | 4045.3 ms | 3260.9 ms | 784.4 ms | 1484.2 ms |
| Toml | Go | 1778.5 ms | 1428.3 ms | 350.3 ms | 858.4 ms |
| Dustin_humanize | Go | 727.4 ms | 534.1 ms | 193.3 ms | 361.5 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1531529.8 ms | 1135757.8 ms | 8 |
| LLGoNoLTO | 1400283.4 ms | 457683.6 ms | 9 |
| LLGoFullLTOGlobalDCE | 1395035.2 ms | 998902.3 ms | 8 |
| LLGoFullLTOGlobalDCEPlugin | 1371389.2 ms | 971421.6 ms | 8 |
| LLGoDeadcodeDrop | 1322903.7 ms | 443379.7 ms | 9 |
| Go | 143543.8 ms | 45047.0 ms | 9 |

Dependency download details are in `download-timings.log`.
