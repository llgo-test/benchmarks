## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| Etcdctl | LLGoFullLTONoGlobalDCE | 437069.9 ms | 425314.9 ms | 11755.0 ms | 307779.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 419602.8 ms | 407681.6 ms | 11921.3 ms | 299538.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 418564.8 ms | 406808.8 ms | 11756.0 ms | 298599.3 ms |
| XGo | LLGoFullLTONoGlobalDCE | 306560.4 ms | 298780.2 ms | 7780.1 ms | 239958.3 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 291101.4 ms | 284579.5 ms | 6521.9 ms | 194547.1 ms |
| XGo | LLGoFullLTOGlobalDCE | 274781.0 ms | 267014.0 ms | 7767.0 ms | 207175.8 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 267952.3 ms | 260256.4 ms | 7696.0 ms | 200743.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 265165.8 ms | 258413.3 ms | 6752.5 ms | 164801.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 261699.0 ms | 255140.9 ms | 6558.1 ms | 164516.0 ms |
| Etcdctl | LLGoDeadcodeDrop | 250429.4 ms | 239840.7 ms | 10588.7 ms | 82588.7 ms |
| Etcdctl | LLGoNoLTO | 249205.0 ms | 239818.9 ms | 9386.2 ms | 81329.7 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 245558.4 ms | 239886.2 ms | 5672.2 ms | 168137.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 242125.2 ms | 236461.4 ms | 5663.8 ms | 166630.4 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 235855.0 ms | 230244.5 ms | 5610.6 ms | 162583.7 ms |
| Aws_restjson | LLGoNoLTO | 232007.7 ms | 226549.7 ms | 5458.0 ms | 71890.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 224673.1 ms | 219062.9 ms | 5610.2 ms | 147254.3 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 221900.0 ms | 216462.9 ms | 5437.1 ms | 143804.0 ms |
| Aws_restjson | LLGoDeadcodeDrop | 213561.6 ms | 208018.8 ms | 5542.8 ms | 66813.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 203076.1 ms | 197848.5 ms | 5227.6 ms | 129012.0 ms |
| Uber_zap | LLGoNoLTO | 176349.2 ms | 172060.1 ms | 4289.1 ms | 56187.9 ms |
| Uber_zap | LLGoDeadcodeDrop | 175175.3 ms | 170665.0 ms | 4510.3 ms | 55922.8 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 167530.9 ms | 162756.0 ms | 4774.9 ms | 54057.5 ms |
| K8s_workqueue | LLGoNoLTO | 167334.7 ms | 162963.6 ms | 4371.2 ms | 53539.3 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 144808.6 ms | 140873.5 ms | 3935.1 ms | 98774.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 143616.3 ms | 139771.4 ms | 3844.9 ms | 96875.4 ms |
| Toml | LLGoFullLTONoGlobalDCE | 134961.9 ms | 131217.8 ms | 3744.1 ms | 91977.1 ms |
| XGo | LLGoNoLTO | 128145.8 ms | 122062.1 ms | 6083.7 ms | 45781.1 ms |
| XGo | LLGoDeadcodeDrop | 127417.0 ms | 120398.5 ms | 7018.5 ms | 44769.5 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 124916.8 ms | 121271.2 ms | 3645.5 ms | 79539.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 121068.8 ms | 117461.6 ms | 3607.2 ms | 74463.0 ms |
| Toml | LLGoFullLTOGlobalDCE | 117830.3 ms | 114318.3 ms | 3512.0 ms | 74598.1 ms |
| Gorm_schema | LLGoDeadcodeDrop | 110797.1 ms | 107261.8 ms | 3535.4 ms | 37722.9 ms |
| Gorm_schema | LLGoNoLTO | 107587.0 ms | 104299.2 ms | 3287.8 ms | 36407.5 ms |
| Toml | LLGoDeadcodeDrop | 100992.9 ms | 98150.8 ms | 2842.1 ms | 34107.8 ms |
| Toml | LLGoNoLTO | 100780.6 ms | 97826.5 ms | 2954.1 ms | 33797.1 ms |
| IXGo | Go | 95557.9 ms | 80782.5 ms | 14775.4 ms | 26375.9 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 94523.3 ms | 92030.3 ms | 2492.9 ms | 66612.9 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 76202.6 ms | 73903.2 ms | 2299.4 ms | 47884.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 75943.7 ms | 73626.7 ms | 2317.0 ms | 47820.8 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 69703.0 ms | 67540.2 ms | 2162.8 ms | 25468.2 ms |
| Dustin_humanize | LLGoNoLTO | 69323.7 ms | 67201.0 ms | 2122.7 ms | 25326.3 ms |
| Etcdctl | Go | 37414.5 ms | 32187.8 ms | 5226.7 ms | 11182.9 ms |
| XGo | Go | 21523.8 ms | 18481.5 ms | 3042.3 ms | 6311.6 ms |
| Aws_restjson | Go | 8963.0 ms | 7450.9 ms | 1512.2 ms | 3621.6 ms |
| Gorm_schema | Go | 6472.8 ms | 5539.5 ms | 933.3 ms | 2503.3 ms |
| Uber_zap | Go | 5881.5 ms | 4999.3 ms | 882.2 ms | 2336.3 ms |
| K8s_workqueue | Go | 5225.3 ms | 4394.0 ms | 831.3 ms | 1836.2 ms |
| Toml | Go | 2198.4 ms | 1841.7 ms | 356.7 ms | 1024.7 ms |
| Dustin_humanize | Go | 905.6 ms | 666.1 ms | 239.5 ms | 432.4 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1890438.9 ms | 1330370.4 ms | 8 |
| LLGoFullLTOGlobalDCE | 1759233.4 ms | 1203470.1 ms | 8 |
| LLGoFullLTOGlobalDCEPlugin | 1699885.3 ms | 1139785.9 ms | 8 |
| LLGoNoLTO | 1230733.7 ms | 404259.3 ms | 8 |
| LLGoDeadcodeDrop | 1215607.2 ms | 401450.6 ms | 8 |
| Go | 184142.9 ms | 55624.9 ms | 9 |

Dependency download details are in `download-timings.log`.
