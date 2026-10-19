## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 627609.6 ms | 617405.3 ms | 10204.3 ms | 400449.9 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 585514.0 ms | 575471.2 ms | 10042.7 ms | 388677.5 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 573062.6 ms | 562843.3 ms | 10219.4 ms | 381595.3 ms |
| IXGo | LLGoDeadcodeDrop | 337441.7 ms | 327068.1 ms | 10373.5 ms | 108280.7 ms |
| IXGo | LLGoNoLTO | 319918.2 ms | 311977.3 ms | 7941.0 ms | 99411.6 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 318650.6 ms | 313775.8 ms | 4874.7 ms | 243015.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 316564.2 ms | 311088.6 ms | 5475.6 ms | 241102.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 277093.2 ms | 272371.6 ms | 4721.6 ms | 210854.5 ms |
| XGo | LLGoFullLTONoGlobalDCE | 237188.5 ms | 233606.2 ms | 3582.3 ms | 196457.1 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 217640.9 ms | 214474.3 ms | 3166.6 ms | 157236.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 208864.3 ms | 205900.2 ms | 2964.1 ms | 134716.5 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 204013.8 ms | 200795.6 ms | 3218.2 ms | 160929.6 ms |
| XGo | LLGoFullLTOGlobalDCE | 191843.1 ms | 188807.5 ms | 3035.6 ms | 152090.4 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 191737.3 ms | 188881.6 ms | 2855.7 ms | 142968.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 186970.6 ms | 184103.8 ms | 2866.8 ms | 127683.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 186796.6 ms | 183951.2 ms | 2845.4 ms | 139466.9 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 185172.8 ms | 182220.5 ms | 2952.3 ms | 138670.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 177658.6 ms | 175078.3 ms | 2580.3 ms | 128051.2 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 160440.4 ms | 157830.5 ms | 2610.0 ms | 114219.6 ms |
| Aws_restjson | LLGoNoLTO | 158776.1 ms | 156271.9 ms | 2504.2 ms | 55575.1 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 153297.6 ms | 150622.7 ms | 2674.9 ms | 107554.5 ms |
| Aws_restjson | LLGoDeadcodeDrop | 149063.8 ms | 146334.4 ms | 2729.4 ms | 52876.6 ms |
| Etcdctl | LLGoNoLTO | 145193.6 ms | 141479.5 ms | 3714.1 ms | 51701.5 ms |
| Etcdctl | LLGoDeadcodeDrop | 142104.1 ms | 138155.4 ms | 3948.7 ms | 51378.8 ms |
| Uber_zap | LLGoNoLTO | 130705.1 ms | 128611.4 ms | 2093.6 ms | 48772.7 ms |
| K8s_workqueue | LLGoNoLTO | 127579.2 ms | 125402.7 ms | 2176.4 ms | 47812.0 ms |
| Uber_zap | LLGoDeadcodeDrop | 125194.0 ms | 122963.8 ms | 2230.3 ms | 47907.2 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 114847.5 ms | 112554.1 ms | 2293.4 ms | 43941.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 97858.8 ms | 96113.1 ms | 1745.7 ms | 71283.1 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 93207.7 ms | 91525.0 ms | 1682.8 ms | 67793.6 ms |
| XGo | LLGoNoLTO | 86942.1 ms | 84693.2 ms | 2248.9 ms | 34578.6 ms |
| Toml | LLGoFullLTONoGlobalDCE | 86491.7 ms | 84713.4 ms | 1778.3 ms | 63145.0 ms |
| XGo | LLGoDeadcodeDrop | 86332.6 ms | 83536.9 ms | 2795.7 ms | 34270.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 78249.4 ms | 76610.3 ms | 1639.1 ms | 51020.8 ms |
| Toml | LLGoFullLTOGlobalDCE | 73983.4 ms | 72374.0 ms | 1609.4 ms | 50130.7 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 71529.2 ms | 69875.6 ms | 1653.6 ms | 47854.4 ms |
| Gorm_schema | LLGoDeadcodeDrop | 69306.0 ms | 67735.8 ms | 1570.1 ms | 24028.2 ms |
| Gorm_schema | LLGoNoLTO | 66985.5 ms | 65568.2 ms | 1417.3 ms | 22794.9 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 64950.5 ms | 63601.5 ms | 1349.0 ms | 48815.4 ms |
| Toml | LLGoDeadcodeDrop | 59379.5 ms | 57811.9 ms | 1567.7 ms | 20363.2 ms |
| Toml | LLGoNoLTO | 58926.7 ms | 57578.1 ms | 1348.6 ms | 20003.8 ms |
| IXGo | Go | 57868.4 ms | 53738.2 ms | 4130.2 ms | 16347.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 51338.2 ms | 50130.2 ms | 1208.0 ms | 34590.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 50264.2 ms | 49069.1 ms | 1195.1 ms | 34030.0 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 44668.2 ms | 43531.0 ms | 1137.2 ms | 16744.6 ms |
| Dustin_humanize | LLGoNoLTO | 43191.8 ms | 42181.1 ms | 1010.6 ms | 15892.3 ms |
| Etcdctl | Go | 23157.2 ms | 21546.1 ms | 1611.1 ms | 7059.1 ms |
| XGo | Go | 13136.5 ms | 12186.2 ms | 950.3 ms | 3980.3 ms |
| Aws_restjson | Go | 5228.0 ms | 4733.3 ms | 494.7 ms | 2209.7 ms |
| Gorm_schema | Go | 3783.1 ms | 3477.5 ms | 305.6 ms | 1483.6 ms |
| Uber_zap | Go | 3614.7 ms | 3283.7 ms | 331.0 ms | 1452.9 ms |
| K8s_workqueue | Go | 3087.9 ms | 2771.5 ms | 316.4 ms | 1118.2 ms |
| Toml | Go | 1322.6 ms | 1135.8 ms | 186.8 ms | 619.1 ms |
| Dustin_humanize | Go | 538.1 ms | 427.9 ms | 110.2 ms | 259.4 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1968102.6 ms | 1439697.5 ms | 9 |
| LLGoFullLTOGlobalDCE | 1871152.1 ms | 1314599.8 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1828737.1 ms | 1280104.9 ms | 9 |
| LLGoNoLTO | 1138218.3 ms | 396542.5 ms | 9 |
| LLGoDeadcodeDrop | 1128337.5 ms | 399790.5 ms | 9 |
| Go | 111736.5 ms | 34529.1 ms | 9 |

Dependency download details are in `download-timings.log`.
