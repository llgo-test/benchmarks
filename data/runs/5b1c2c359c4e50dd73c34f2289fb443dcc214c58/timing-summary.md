## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTONoGlobalDCE | 725444.2 ms | 711550.3 ms | 13894.0 ms | 374226.9 ms |
| IXGo | LLGoFullLTOGlobalDCE | 695073.0 ms | 672052.5 ms | 23020.5 ms | 367536.6 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 662230.8 ms | 648609.5 ms | 13621.3 ms | 348139.0 ms |
| IXGo | LLGoDeadcodeDrop | 512435.3 ms | 499722.8 ms | 12712.5 ms | 156189.0 ms |
| IXGo | LLGoNoLTO | 496863.0 ms | 484491.5 ms | 12371.5 ms | 150467.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 355868.9 ms | 348713.5 ms | 7155.4 ms | 211909.5 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 341918.6 ms | 335747.8 ms | 6170.8 ms | 205568.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 338639.8 ms | 332470.9 ms | 6169.0 ms | 199943.7 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 279075.7 ms | 275046.0 ms | 4029.7 ms | 155865.1 ms |
| Aws_restjson | LLGoDeadcodeDrop | 276368.5 ms | 272941.5 ms | 3427.1 ms | 93516.1 ms |
| Aws_restjson | LLGoNoLTO | 270769.3 ms | 267413.0 ms | 3356.3 ms | 92035.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 269204.8 ms | 265156.7 ms | 4048.1 ms | 141632.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 267870.4 ms | 263961.0 ms | 3909.5 ms | 140898.4 ms |
| Etcdctl | LLGoDeadcodeDrop | 261855.4 ms | 256285.4 ms | 5570.0 ms | 89008.2 ms |
| Etcdctl | LLGoNoLTO | 259982.0 ms | 254747.6 ms | 5234.4 ms | 87609.8 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 257136.6 ms | 252631.6 ms | 4504.9 ms | 170629.7 ms |
| XGo | LLGoFullLTOGlobalDCE | 251683.0 ms | 247202.5 ms | 4480.5 ms | 166242.1 ms |
| XGo | LLGoFullLTONoGlobalDCE | 248530.5 ms | 244174.8 ms | 4355.6 ms | 164019.6 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 236634.6 ms | 232963.6 ms | 3671.0 ms | 137070.0 ms |
| Uber_zap | LLGoDeadcodeDrop | 236119.9 ms | 233234.0 ms | 2885.9 ms | 83731.4 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 234660.8 ms | 231155.8 ms | 3505.0 ms | 135029.7 ms |
| Uber_zap | LLGoNoLTO | 233032.5 ms | 230060.7 ms | 2971.8 ms | 82756.4 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 231336.7 ms | 228017.6 ms | 3319.0 ms | 82777.3 ms |
| K8s_workqueue | LLGoNoLTO | 226072.6 ms | 223020.3 ms | 3052.3 ms | 81446.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 225784.5 ms | 222467.5 ms | 3316.9 ms | 129741.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 221734.9 ms | 218132.1 ms | 3602.8 ms | 121128.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 221701.9 ms | 218249.0 ms | 3452.9 ms | 121482.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 215907.8 ms | 212574.1 ms | 3333.7 ms | 117326.6 ms |
| XGo | LLGoDeadcodeDrop | 166118.5 ms | 162392.0 ms | 3726.6 ms | 61611.2 ms |
| XGo | LLGoNoLTO | 158197.2 ms | 154717.7 ms | 3479.5 ms | 59198.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 111913.0 ms | 109816.4 ms | 2096.6 ms | 64414.9 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 110553.5 ms | 108406.9 ms | 2146.6 ms | 64530.5 ms |
| Gorm_schema | LLGoDeadcodeDrop | 108826.2 ms | 106980.3 ms | 1846.0 ms | 35991.3 ms |
| Gorm_schema | LLGoNoLTO | 107955.2 ms | 106229.1 ms | 1726.1 ms | 35697.6 ms |
| Toml | LLGoFullLTONoGlobalDCE | 104049.5 ms | 101829.4 ms | 2220.1 ms | 59998.8 ms |
| Toml | LLGoNoLTO | 102853.7 ms | 100960.7 ms | 1893.0 ms | 34390.3 ms |
| Toml | LLGoDeadcodeDrop | 101556.7 ms | 99741.3 ms | 1815.4 ms | 33566.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 96234.9 ms | 94200.1 ms | 2034.8 ms | 50324.5 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 94764.4 ms | 92617.6 ms | 2146.8 ms | 50329.3 ms |
| Toml | LLGoFullLTOGlobalDCE | 90706.4 ms | 88733.6 ms | 1972.8 ms | 47948.7 ms |
| IXGo | Go | 85256.7 ms | 80144.4 ms | 5112.3 ms | 24056.3 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 71404.2 ms | 69991.4 ms | 1412.7 ms | 43122.3 ms |
| Dustin_humanize | LLGoNoLTO | 71309.2 ms | 70067.7 ms | 1241.5 ms | 25585.4 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 71253.4 ms | 70029.1 ms | 1224.3 ms | 25441.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 62762.3 ms | 61337.7 ms | 1424.6 ms | 33817.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 61864.2 ms | 60515.5 ms | 1348.8 ms | 33564.1 ms |
| Etcdctl | Go | 33273.2 ms | 31183.2 ms | 2090.0 ms | 10270.0 ms |
| XGo | Go | 19259.2 ms | 17874.2 ms | 1384.9 ms | 5958.8 ms |
| Aws_restjson | Go | 8246.1 ms | 7402.4 ms | 843.7 ms | 3711.8 ms |
| Gorm_schema | Go | 5937.3 ms | 5497.6 ms | 439.7 ms | 2330.6 ms |
| Uber_zap | Go | 5573.4 ms | 4997.9 ms | 575.5 ms | 2344.4 ms |
| K8s_workqueue | Go | 4919.7 ms | 4267.7 ms | 651.9 ms | 2340.8 ms |
| Toml | Go | 2069.3 ms | 1836.0 ms | 233.3 ms | 959.5 ms |
| Dustin_humanize | Go | 830.5 ms | 672.9 ms | 157.6 ms | 394.6 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2352271.4 ms | 1339431.1 ms | 9 |
| LLGoFullLTOGlobalDCE | 2265236.2 ms | 1271773.2 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2235845.4 ms | 1245236.7 ms | 9 |
| LLGoDeadcodeDrop | 1965870.7 ms | 661831.7 ms | 9 |
| LLGoNoLTO | 1927034.7 ms | 649187.8 ms | 9 |
| Go | 165365.3 ms | 52366.8 ms | 9 |

Dependency download details are in `download-timings.log`.
