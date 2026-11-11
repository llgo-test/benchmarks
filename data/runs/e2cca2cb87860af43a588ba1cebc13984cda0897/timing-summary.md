## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTONoGlobalDCE | 932385.4 ms | 904765.4 ms | 27620.1 ms | 577592.1 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 930390.8 ms | 903679.9 ms | 26710.8 ms | 588128.1 ms |
| IXGo | LLGoFullLTOGlobalDCE | 842432.4 ms | 816582.9 ms | 25849.5 ms | 545193.8 ms |
| IXGo | LLGoDeadcodeDrop | 525198.1 ms | 497888.7 ms | 27309.4 ms | 168931.6 ms |
| IXGo | LLGoNoLTO | 503987.3 ms | 481173.6 ms | 22813.7 ms | 157927.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 502478.4 ms | 489273.7 ms | 13204.7 ms | 365710.0 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 498001.3 ms | 484716.5 ms | 13284.7 ms | 367182.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 482688.0 ms | 470207.7 ms | 12480.3 ms | 353155.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 364710.0 ms | 357146.9 ms | 7563.0 ms | 235501.8 ms |
| XGo | LLGoFullLTONoGlobalDCE | 361625.8 ms | 352664.7 ms | 8961.1 ms | 289265.7 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 352410.6 ms | 344832.9 ms | 7577.7 ms | 237170.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 334916.4 ms | 327505.9 ms | 7410.5 ms | 210740.3 ms |
| XGo | LLGoFullLTOGlobalDCE | 317460.2 ms | 308884.0 ms | 8576.2 ms | 244337.8 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 315692.2 ms | 307105.8 ms | 8586.4 ms | 243640.3 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 300689.4 ms | 293843.0 ms | 6846.4 ms | 209181.2 ms |
| Aws_restjson | LLGoNoLTO | 295239.9 ms | 289079.3 ms | 6160.6 ms | 95305.5 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 292740.4 ms | 286318.9 ms | 6421.6 ms | 202369.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 291388.7 ms | 284641.7 ms | 6746.9 ms | 194142.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 284630.5 ms | 277900.8 ms | 6729.6 ms | 197194.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 275435.5 ms | 269015.8 ms | 6419.6 ms | 180743.4 ms |
| Aws_restjson | LLGoDeadcodeDrop | 270636.9 ms | 264106.7 ms | 6530.2 ms | 86102.6 ms |
| Etcdctl | LLGoNoLTO | 255766.9 ms | 245745.3 ms | 10021.5 ms | 87396.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 251676.6 ms | 245595.6 ms | 6080.9 ms | 163892.8 ms |
| Etcdctl | LLGoDeadcodeDrop | 241238.9 ms | 230906.3 ms | 10332.6 ms | 83918.8 ms |
| Uber_zap | LLGoDeadcodeDrop | 223745.3 ms | 218318.2 ms | 5427.1 ms | 73256.2 ms |
| Uber_zap | LLGoNoLTO | 211266.4 ms | 206253.3 ms | 5013.1 ms | 67253.6 ms |
| K8s_workqueue | LLGoNoLTO | 210168.7 ms | 204786.6 ms | 5382.1 ms | 67533.2 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 197778.0 ms | 192846.2 ms | 4931.8 ms | 64580.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 165274.6 ms | 161234.0 ms | 4040.5 ms | 112059.2 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 152106.0 ms | 148360.2 ms | 3745.8 ms | 103215.1 ms |
| Toml | LLGoFullLTONoGlobalDCE | 149389.8 ms | 145396.7 ms | 3993.1 ms | 100306.4 ms |
| XGo | LLGoNoLTO | 144553.7 ms | 137910.0 ms | 6643.7 ms | 53290.9 ms |
| XGo | LLGoDeadcodeDrop | 143352.4 ms | 135634.8 ms | 7717.6 ms | 52064.8 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 132993.7 ms | 129434.7 ms | 3559.0 ms | 83396.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 130030.7 ms | 126305.7 ms | 3725.1 ms | 79611.6 ms |
| Toml | LLGoFullLTOGlobalDCE | 126504.3 ms | 122786.7 ms | 3717.7 ms | 78886.8 ms |
| Gorm_schema | LLGoDeadcodeDrop | 117369.7 ms | 113755.6 ms | 3614.2 ms | 41057.9 ms |
| Gorm_schema | LLGoNoLTO | 116215.5 ms | 113030.1 ms | 3185.4 ms | 39997.8 ms |
| Toml | LLGoDeadcodeDrop | 112457.2 ms | 109030.7 ms | 3426.4 ms | 38700.6 ms |
| Toml | LLGoNoLTO | 107517.4 ms | 104479.9 ms | 3037.5 ms | 36874.7 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 107255.3 ms | 104505.5 ms | 2749.8 ms | 76283.5 ms |
| IXGo | Go | 98448.4 ms | 83554.9 ms | 14893.4 ms | 26734.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 86234.4 ms | 83841.7 ms | 2392.7 ms | 54672.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 84491.8 ms | 82095.3 ms | 2396.5 ms | 53757.8 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 73887.4 ms | 71641.8 ms | 2245.5 ms | 27333.1 ms |
| Dustin_humanize | LLGoNoLTO | 72909.7 ms | 70963.7 ms | 1946.1 ms | 26934.6 ms |
| Etcdctl | Go | 39460.0 ms | 33945.3 ms | 5514.7 ms | 12480.3 ms |
| XGo | Go | 22783.1 ms | 19574.0 ms | 3209.1 ms | 6770.1 ms |
| Aws_restjson | Go | 9514.4 ms | 7907.4 ms | 1607.0 ms | 4064.5 ms |
| Gorm_schema | Go | 6550.1 ms | 5599.1 ms | 951.0 ms | 2536.2 ms |
| Uber_zap | Go | 5955.7 ms | 5105.4 ms | 850.3 ms | 2415.4 ms |
| K8s_workqueue | Go | 5465.5 ms | 4581.9 ms | 883.5 ms | 1959.8 ms |
| Toml | Go | 2309.7 ms | 1897.0 ms | 412.7 ms | 1117.6 ms |
| Dustin_humanize | Go | 1024.7 ms | 725.9 ms | 298.7 ms | 665.6 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 3146604.1 ms | 2162565.9 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2959848.8 ms | 1970535.2 ms | 9 |
| LLGoFullLTOGlobalDCE | 2959580.3 ms | 2014229.1 ms | 9 |
| LLGoNoLTO | 1917625.5 ms | 632514.4 ms | 9 |
| LLGoDeadcodeDrop | 1905663.8 ms | 635945.7 ms | 9 |
| Go | 191511.5 ms | 58743.5 ms | 9 |

Dependency download details are in `download-timings.log`.
