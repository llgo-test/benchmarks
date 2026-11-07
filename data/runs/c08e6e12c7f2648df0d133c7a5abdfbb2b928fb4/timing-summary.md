## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 891157.9 ms | 864832.2 ms | 26325.7 ms | 554483.0 ms |
| IXGo | LLGoFullLTOGlobalDCE | 844419.5 ms | 817976.9 ms | 26442.6 ms | 535274.7 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 831972.7 ms | 805555.9 ms | 26416.8 ms | 530132.7 ms |
| IXGo | LLGoDeadcodeDrop | 550247.3 ms | 523479.6 ms | 26767.6 ms | 166717.8 ms |
| IXGo | LLGoNoLTO | 518832.4 ms | 496598.7 ms | 22233.7 ms | 156518.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 460610.5 ms | 447859.1 ms | 12751.4 ms | 332387.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 446062.5 ms | 433516.8 ms | 12545.7 ms | 322115.4 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 443686.2 ms | 431412.1 ms | 12274.1 ms | 323125.2 ms |
| XGo | LLGoFullLTONoGlobalDCE | 333370.4 ms | 324721.7 ms | 8648.7 ms | 265576.8 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 329979.8 ms | 322627.6 ms | 7352.2 ms | 218100.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 301194.9 ms | 294077.0 ms | 7117.9 ms | 187735.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 298639.2 ms | 291708.2 ms | 6931.0 ms | 186503.6 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 293595.9 ms | 285170.6 ms | 8425.3 ms | 224738.9 ms |
| XGo | LLGoFullLTOGlobalDCE | 289174.2 ms | 281105.3 ms | 8068.9 ms | 221717.5 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 281187.5 ms | 274979.1 ms | 6208.4 ms | 192679.2 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 271487.2 ms | 265316.9 ms | 6170.3 ms | 187462.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 268757.5 ms | 262249.4 ms | 6508.1 ms | 184494.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 260407.9 ms | 254108.5 ms | 6299.3 ms | 172368.2 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 254699.1 ms | 248818.0 ms | 5881.1 ms | 164383.3 ms |
| Aws_restjson | LLGoNoLTO | 248335.0 ms | 242606.2 ms | 5728.9 ms | 75569.7 ms |
| Aws_restjson | LLGoDeadcodeDrop | 244854.2 ms | 238707.8 ms | 6146.4 ms | 76061.4 ms |
| Etcdctl | LLGoNoLTO | 235700.4 ms | 225781.5 ms | 9918.9 ms | 78963.3 ms |
| Etcdctl | LLGoDeadcodeDrop | 235660.2 ms | 224853.6 ms | 10806.6 ms | 79175.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 235594.7 ms | 229582.2 ms | 6012.5 ms | 150391.7 ms |
| Uber_zap | LLGoDeadcodeDrop | 202004.3 ms | 196655.2 ms | 5349.2 ms | 63951.4 ms |
| Uber_zap | LLGoNoLTO | 201523.9 ms | 196687.5 ms | 4836.4 ms | 62749.2 ms |
| K8s_workqueue | LLGoNoLTO | 192598.0 ms | 188010.9 ms | 4587.1 ms | 59998.6 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 191840.8 ms | 186666.8 ms | 5174.0 ms | 61361.5 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 149956.3 ms | 146100.7 ms | 3855.6 ms | 101895.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 147461.8 ms | 143671.1 ms | 3790.7 ms | 99295.7 ms |
| Toml | LLGoFullLTONoGlobalDCE | 140387.2 ms | 136762.8 ms | 3624.4 ms | 96492.5 ms |
| XGo | LLGoNoLTO | 130792.2 ms | 124714.9 ms | 6077.3 ms | 46265.5 ms |
| XGo | LLGoDeadcodeDrop | 129641.8 ms | 122340.6 ms | 7301.2 ms | 45431.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 124361.5 ms | 120758.1 ms | 3603.4 ms | 76432.5 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 123538.6 ms | 119945.7 ms | 3592.9 ms | 78432.5 ms |
| Toml | LLGoFullLTOGlobalDCE | 121596.4 ms | 118202.1 ms | 3394.2 ms | 77060.8 ms |
| Gorm_schema | LLGoDeadcodeDrop | 113212.6 ms | 109669.9 ms | 3542.7 ms | 38627.8 ms |
| Gorm_schema | LLGoNoLTO | 112152.5 ms | 108988.9 ms | 3163.6 ms | 37730.8 ms |
| Toml | LLGoDeadcodeDrop | 103817.8 ms | 100693.0 ms | 3124.9 ms | 34956.4 ms |
| Toml | LLGoNoLTO | 102673.5 ms | 99716.7 ms | 2956.8 ms | 34512.9 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 99833.4 ms | 97189.3 ms | 2644.1 ms | 70056.7 ms |
| IXGo | Go | 99594.9 ms | 84522.4 ms | 15072.5 ms | 27081.9 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 79968.2 ms | 77587.4 ms | 2380.8 ms | 50495.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 78337.0 ms | 76069.6 ms | 2267.4 ms | 49347.5 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 71871.9 ms | 69717.8 ms | 2154.1 ms | 26331.4 ms |
| Dustin_humanize | LLGoNoLTO | 71555.5 ms | 69547.6 ms | 2007.9 ms | 26028.5 ms |
| Etcdctl | Go | 38014.6 ms | 32718.6 ms | 5296.0 ms | 11458.0 ms |
| XGo | Go | 21794.8 ms | 18714.7 ms | 3080.1 ms | 6367.8 ms |
| Aws_restjson | Go | 9122.4 ms | 7664.8 ms | 1457.6 ms | 3738.9 ms |
| Gorm_schema | Go | 6654.6 ms | 5670.8 ms | 983.8 ms | 2702.1 ms |
| Uber_zap | Go | 6164.9 ms | 5153.9 ms | 1011.0 ms | 2767.1 ms |
| K8s_workqueue | Go | 5330.1 ms | 4473.3 ms | 856.8 ms | 1909.9 ms |
| Toml | Go | 2335.2 ms | 1914.0 ms | 421.2 ms | 1183.6 ms |
| Dustin_humanize | Go | 904.3 ms | 696.3 ms | 207.9 ms | 445.0 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2881860.6 ms | 1985521.6 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2762165.6 ms | 1818249.1 ms | 9 |
| LLGoFullLTOGlobalDCE | 2757411.7 ms | 1849409.4 ms | 9 |
| LLGoDeadcodeDrop | 1843151.0 ms | 592615.0 ms | 9 |
| LLGoNoLTO | 1814163.4 ms | 578336.7 ms | 9 |
| Go | 189915.8 ms | 57654.3 ms | 9 |

Dependency download details are in `download-timings.log`.
