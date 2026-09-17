## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 546389.4 ms | 532867.7 ms | 13521.7 ms | 282692.2 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 523128.9 ms | 510707.2 ms | 12421.7 ms | 274062.6 ms |
| IXGo | LLGoFullLTOGlobalDCE | 521755.4 ms | 508917.3 ms | 12838.0 ms | 274849.8 ms |
| IXGo | LLGoDeadcodeDrop | 408734.6 ms | 397936.6 ms | 10798.0 ms | 121401.3 ms |
| IXGo | LLGoNoLTO | 397558.2 ms | 387306.3 ms | 10251.9 ms | 118055.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 277771.9 ms | 272372.1 ms | 5399.8 ms | 163880.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 272619.5 ms | 267467.8 ms | 5151.6 ms | 160898.6 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 271754.5 ms | 266777.7 ms | 4976.8 ms | 161407.1 ms |
| Etcdctl | LLGoDeadcodeDrop | 208501.7 ms | 203899.5 ms | 4602.2 ms | 67675.9 ms |
| Etcdctl | LLGoNoLTO | 205528.6 ms | 201015.8 ms | 4512.7 ms | 66571.1 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 175199.9 ms | 171718.8 ms | 3481.1 ms | 122203.3 ms |
| XGo | LLGoFullLTOGlobalDCE | 173441.4 ms | 169993.6 ms | 3447.7 ms | 121064.6 ms |
| XGo | LLGoFullLTONoGlobalDCE | 172799.8 ms | 169584.8 ms | 3215.0 ms | 121969.3 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 167252.5 ms | 164944.2 ms | 2308.3 ms | 133248.3 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 153824.9 ms | 151295.1 ms | 2529.7 ms | 119126.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 153560.8 ms | 151306.5 ms | 2254.3 ms | 118780.2 ms |
| Aws_restjson | LLGoDeadcodeDrop | 109835.9 ms | 107907.1 ms | 1928.8 ms | 69047.8 ms |
| Aws_restjson | LLGoNoLTO | 108512.5 ms | 106555.3 ms | 1957.3 ms | 68709.3 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 105854.9 ms | 103960.2 ms | 1894.7 ms | 81480.1 ms |
| XGo | LLGoDeadcodeDrop | 104259.5 ms | 101334.2 ms | 2925.3 ms | 39712.1 ms |
| XGo | LLGoNoLTO | 103628.6 ms | 100520.9 ms | 3107.8 ms | 39628.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 100117.9 ms | 98210.1 ms | 1907.8 ms | 78716.4 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 99764.3 ms | 97921.5 ms | 1842.8 ms | 78575.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 95603.6 ms | 93692.4 ms | 1911.1 ms | 70713.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 95048.8 ms | 93281.2 ms | 1767.6 ms | 70570.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 86556.6 ms | 84726.8 ms | 1829.8 ms | 64822.2 ms |
| IXGo | Go | 78328.8 ms | 72672.3 ms | 5656.5 ms | 21936.5 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 60481.1 ms | 59104.1 ms | 1377.0 ms | 41973.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 60350.5 ms | 58878.9 ms | 1471.5 ms | 41469.6 ms |
| Uber_zap | LLGoDeadcodeDrop | 55134.1 ms | 53666.9 ms | 1467.2 ms | 24501.3 ms |
| Uber_zap | LLGoNoLTO | 53865.4 ms | 52254.4 ms | 1611.0 ms | 24158.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 50065.2 ms | 48666.3 ms | 1398.9 ms | 30959.6 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 47912.0 ms | 46420.8 ms | 1491.2 ms | 22428.6 ms |
| K8s_workqueue | LLGoNoLTO | 47433.8 ms | 45825.0 ms | 1608.7 ms | 22181.5 ms |
| Toml | LLGoFullLTONoGlobalDCE | 46941.5 ms | 45830.0 ms | 1111.5 ms | 35775.9 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 40471.4 ms | 39390.9 ms | 1080.5 ms | 28358.0 ms |
| Toml | LLGoFullLTOGlobalDCE | 39674.2 ms | 38625.8 ms | 1048.3 ms | 28090.2 ms |
| Gorm_schema | LLGoDeadcodeDrop | 37683.2 ms | 36337.9 ms | 1345.4 ms | 12852.5 ms |
| Gorm_schema | LLGoNoLTO | 36962.3 ms | 35767.2 ms | 1195.1 ms | 12317.5 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 33397.6 ms | 32508.3 ms | 889.3 ms | 26327.4 ms |
| Etcdctl | Go | 31490.9 ms | 29273.2 ms | 2217.7 ms | 9465.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 24732.8 ms | 23821.9 ms | 910.9 ms | 17777.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 24372.7 ms | 23501.6 ms | 871.1 ms | 17691.6 ms |
| Toml | LLGoDeadcodeDrop | 23244.0 ms | 22170.7 ms | 1073.3 ms | 8745.2 ms |
| Toml | LLGoNoLTO | 22194.8 ms | 21194.5 ms | 1000.3 ms | 8419.8 ms |
| XGo | Go | 18263.2 ms | 16827.0 ms | 1436.2 ms | 5568.9 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 12810.9 ms | 12008.1 ms | 802.9 ms | 5668.8 ms |
| Dustin_humanize | LLGoNoLTO | 12615.7 ms | 11873.9 ms | 741.8 ms | 5496.8 ms |
| Aws_restjson | Go | 7425.8 ms | 6704.6 ms | 721.2 ms | 3069.0 ms |
| Gorm_schema | Go | 5500.0 ms | 5075.3 ms | 424.7 ms | 2138.8 ms |
| Uber_zap | Go | 5087.8 ms | 4599.0 ms | 488.8 ms | 1982.5 ms |
| K8s_workqueue | Go | 4730.4 ms | 4007.3 ms | 723.1 ms | 1973.2 ms |
| Toml | Go | 1960.5 ms | 1730.9 ms | 229.6 ms | 893.5 ms |
| Dustin_humanize | Go | 785.7 ms | 636.1 ms | 149.6 ms | 384.2 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1481375.2 ms | 954819.4 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1450615.7 ms | 900533.8 ms | 9 |
| LLGoFullLTOGlobalDCE | 1440941.1 ms | 912131.6 ms | 9 |
| LLGoDeadcodeDrop | 1008116.0 ms | 372033.4 ms | 9 |
| LLGoNoLTO | 988299.9 ms | 365538.3 ms | 9 |
| Go | 153573.1 ms | 47411.8 ms | 9 |

Dependency download details are in `download-timings.log`.
