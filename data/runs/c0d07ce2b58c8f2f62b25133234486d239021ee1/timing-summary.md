## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 880934.9 ms | 854127.0 ms | 26807.9 ms | 567313.6 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 863966.7 ms | 837233.2 ms | 26733.5 ms | 551411.6 ms |
| IXGo | LLGoFullLTOGlobalDCE | 835193.3 ms | 809203.9 ms | 25989.4 ms | 537142.9 ms |
| IXGo | LLGoDeadcodeDrop | 533466.5 ms | 506542.3 ms | 26924.3 ms | 171175.8 ms |
| IXGo | LLGoNoLTO | 469046.0 ms | 446823.2 ms | 22222.8 ms | 147896.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 456311.9 ms | 443877.9 ms | 12434.0 ms | 330320.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 452328.7 ms | 440259.2 ms | 12069.5 ms | 327826.0 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 451502.4 ms | 439124.2 ms | 12378.2 ms | 330099.1 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 345790.8 ms | 338054.8 ms | 7736.0 ms | 230081.7 ms |
| XGo | LLGoFullLTONoGlobalDCE | 334518.0 ms | 325932.8 ms | 8585.2 ms | 266156.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 315610.2 ms | 308182.2 ms | 7428.0 ms | 202475.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 305250.0 ms | 297955.1 ms | 7294.9 ms | 194498.6 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 299551.4 ms | 291295.8 ms | 8255.6 ms | 229423.3 ms |
| XGo | LLGoFullLTOGlobalDCE | 296410.6 ms | 288209.1 ms | 8201.4 ms | 226915.3 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 291031.1 ms | 284319.3 ms | 6711.8 ms | 200152.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 279957.0 ms | 273536.7 ms | 6420.3 ms | 193371.4 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 278887.8 ms | 272479.4 ms | 6408.5 ms | 193786.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 269645.2 ms | 263391.5 ms | 6253.7 ms | 175850.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 267482.7 ms | 261195.3 ms | 6287.4 ms | 177587.5 ms |
| Aws_restjson | LLGoNoLTO | 247703.4 ms | 242105.9 ms | 5597.5 ms | 77713.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 245106.5 ms | 238785.4 ms | 6321.0 ms | 159190.5 ms |
| Etcdctl | LLGoDeadcodeDrop | 244456.5 ms | 233611.3 ms | 10845.2 ms | 84933.6 ms |
| Aws_restjson | LLGoDeadcodeDrop | 243170.5 ms | 237001.8 ms | 6168.7 ms | 78013.1 ms |
| Etcdctl | LLGoNoLTO | 240058.1 ms | 230487.6 ms | 9570.4 ms | 82497.1 ms |
| Uber_zap | LLGoNoLTO | 210900.0 ms | 206218.6 ms | 4681.4 ms | 67338.0 ms |
| Uber_zap | LLGoDeadcodeDrop | 207757.5 ms | 202589.5 ms | 5168.0 ms | 67661.9 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 197176.8 ms | 191771.9 ms | 5404.9 ms | 64429.7 ms |
| K8s_workqueue | LLGoNoLTO | 195594.1 ms | 190794.9 ms | 4799.1 ms | 62722.4 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 155906.1 ms | 151772.8 ms | 4133.3 ms | 105269.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 148971.0 ms | 145176.0 ms | 3795.0 ms | 99593.8 ms |
| Toml | LLGoFullLTONoGlobalDCE | 141975.8 ms | 138259.0 ms | 3716.9 ms | 95779.2 ms |
| XGo | LLGoNoLTO | 135481.8 ms | 129236.3 ms | 6245.5 ms | 50192.8 ms |
| XGo | LLGoDeadcodeDrop | 134851.6 ms | 127430.1 ms | 7421.5 ms | 49213.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 126356.4 ms | 122687.7 ms | 3668.7 ms | 77021.4 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 124415.8 ms | 120730.0 ms | 3685.8 ms | 76919.3 ms |
| Toml | LLGoFullLTOGlobalDCE | 124112.6 ms | 120560.3 ms | 3552.3 ms | 77118.8 ms |
| Gorm_schema | LLGoNoLTO | 116537.8 ms | 113268.8 ms | 3269.0 ms | 40395.6 ms |
| Gorm_schema | LLGoDeadcodeDrop | 114674.2 ms | 111121.8 ms | 3552.5 ms | 39836.0 ms |
| Toml | LLGoDeadcodeDrop | 111543.1 ms | 108436.2 ms | 3106.9 ms | 38222.9 ms |
| Toml | LLGoNoLTO | 107839.8 ms | 104736.7 ms | 3103.0 ms | 36738.2 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 97817.0 ms | 95300.8 ms | 2516.2 ms | 68581.7 ms |
| IXGo | Go | 97235.2 ms | 82618.7 ms | 14616.5 ms | 26482.9 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 78993.5 ms | 76733.0 ms | 2260.6 ms | 49534.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 78854.5 ms | 76569.3 ms | 2285.2 ms | 49238.9 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 73288.9 ms | 71057.9 ms | 2231.0 ms | 27121.3 ms |
| Dustin_humanize | LLGoNoLTO | 72522.2 ms | 70549.2 ms | 1972.9 ms | 26621.1 ms |
| Etcdctl | Go | 38175.2 ms | 32694.5 ms | 5480.7 ms | 12040.8 ms |
| XGo | Go | 21766.6 ms | 18673.8 ms | 3092.8 ms | 6317.0 ms |
| Aws_restjson | Go | 9110.0 ms | 7500.9 ms | 1609.0 ms | 3750.1 ms |
| Gorm_schema | Go | 6508.9 ms | 5577.9 ms | 931.0 ms | 2556.2 ms |
| Uber_zap | Go | 5947.9 ms | 5076.1 ms | 871.9 ms | 2404.8 ms |
| K8s_workqueue | Go | 5311.0 ms | 4449.5 ms | 861.5 ms | 1894.0 ms |
| Toml | Go | 2279.2 ms | 1873.9 ms | 405.4 ms | 1076.1 ms |
| Dustin_humanize | Go | 900.5 ms | 657.1 ms | 243.4 ms | 466.6 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2961395.8 ms | 2041318.7 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2796925.8 ms | 1868048.8 ms | 9 |
| LLGoFullLTOGlobalDCE | 2788560.3 ms | 1883293.4 ms | 9 |
| LLGoDeadcodeDrop | 1860385.8 ms | 620607.7 ms | 9 |
| LLGoNoLTO | 1795683.0 ms | 592115.9 ms | 9 |
| Go | 187234.5 ms | 56988.5 ms | 9 |

Dependency download details are in `download-timings.log`.
