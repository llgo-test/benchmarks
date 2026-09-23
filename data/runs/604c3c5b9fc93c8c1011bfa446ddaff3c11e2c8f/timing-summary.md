## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTONoGlobalDCE | 587923.6 ms | 576736.9 ms | 11186.7 ms | 295606.9 ms |
| IXGo | LLGoFullLTOGlobalDCE | 548946.9 ms | 537382.8 ms | 11564.1 ms | 284890.7 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 546134.1 ms | 533675.8 ms | 12458.3 ms | 283464.4 ms |
| IXGo | LLGoDeadcodeDrop | 434598.9 ms | 424574.8 ms | 10024.1 ms | 129186.2 ms |
| IXGo | LLGoNoLTO | 419043.3 ms | 409493.4 ms | 9549.9 ms | 123849.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 259741.0 ms | 255093.8 ms | 4647.2 ms | 158181.9 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 256727.9 ms | 252240.0 ms | 4487.8 ms | 158490.9 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 256407.6 ms | 251681.7 ms | 4725.9 ms | 156985.8 ms |
| Etcdctl | LLGoDeadcodeDrop | 196700.3 ms | 192459.5 ms | 4240.8 ms | 65309.7 ms |
| Etcdctl | LLGoNoLTO | 188430.8 ms | 184317.1 ms | 4113.7 ms | 63375.6 ms |
| XGo | LLGoFullLTOGlobalDCE | 184423.3 ms | 181046.4 ms | 3377.0 ms | 127038.4 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 181659.3 ms | 178405.7 ms | 3253.6 ms | 123909.4 ms |
| XGo | LLGoFullLTONoGlobalDCE | 178014.1 ms | 174974.8 ms | 3039.3 ms | 122314.4 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 140693.5 ms | 138216.8 ms | 2476.6 ms | 102139.1 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 133044.7 ms | 130496.1 ms | 2548.5 ms | 92580.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 128789.0 ms | 126570.1 ms | 2218.9 ms | 89301.4 ms |
| XGo | LLGoNoLTO | 110223.0 ms | 107426.6 ms | 2796.5 ms | 41080.6 ms |
| XGo | LLGoDeadcodeDrop | 109665.3 ms | 106978.4 ms | 2686.9 ms | 40705.4 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 108175.6 ms | 106491.7 ms | 1684.0 ms | 81561.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 100277.6 ms | 98497.7 ms | 1779.8 ms | 71736.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 100031.3 ms | 98305.0 ms | 1726.4 ms | 73022.8 ms |
| Aws_restjson | LLGoDeadcodeDrop | 84991.1 ms | 83002.2 ms | 1988.9 ms | 39496.4 ms |
| Aws_restjson | LLGoNoLTO | 83666.6 ms | 81738.6 ms | 1928.0 ms | 39078.3 ms |
| IXGo | Go | 81148.8 ms | 75912.8 ms | 5236.0 ms | 22680.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 62993.1 ms | 61691.7 ms | 1301.4 ms | 42376.1 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 62775.6 ms | 61444.4 ms | 1331.2 ms | 42532.6 ms |
| Uber_zap | LLGoDeadcodeDrop | 57861.3 ms | 56398.9 ms | 1462.3 ms | 25176.1 ms |
| Uber_zap | LLGoNoLTO | 57829.4 ms | 56410.3 ms | 1419.2 ms | 24524.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 52723.8 ms | 51403.7 ms | 1320.1 ms | 32056.9 ms |
| Toml | LLGoFullLTONoGlobalDCE | 47837.1 ms | 46866.9 ms | 970.2 ms | 35706.8 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 41284.5 ms | 40247.4 ms | 1037.1 ms | 28143.8 ms |
| Toml | LLGoFullLTOGlobalDCE | 40741.0 ms | 39746.4 ms | 994.6 ms | 28476.3 ms |
| Gorm_schema | LLGoDeadcodeDrop | 40146.5 ms | 38939.6 ms | 1206.9 ms | 13457.4 ms |
| Gorm_schema | LLGoNoLTO | 39191.5 ms | 38034.2 ms | 1157.3 ms | 12908.0 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 35882.5 ms | 35014.4 ms | 868.1 ms | 27832.4 ms |
| Etcdctl | Go | 32671.9 ms | 30664.2 ms | 2007.7 ms | 9800.3 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 26481.0 ms | 25663.8 ms | 817.2 ms | 18350.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 25797.2 ms | 25040.2 ms | 756.9 ms | 18200.3 ms |
| Toml | LLGoNoLTO | 24395.6 ms | 23469.8 ms | 925.8 ms | 9333.2 ms |
| Toml | LLGoDeadcodeDrop | 24110.2 ms | 23216.3 ms | 893.9 ms | 9128.2 ms |
| XGo | Go | 18906.0 ms | 17691.5 ms | 1214.5 ms | 5581.2 ms |
| Dustin_humanize | LLGoNoLTO | 14219.8 ms | 13550.2 ms | 669.7 ms | 5968.1 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 13680.4 ms | 13000.8 ms | 679.6 ms | 5809.6 ms |
| Aws_restjson | Go | 7828.9 ms | 7200.9 ms | 628.0 ms | 3197.2 ms |
| Gorm_schema | Go | 5820.4 ms | 5318.4 ms | 502.0 ms | 2517.2 ms |
| Uber_zap | Go | 5321.8 ms | 4864.8 ms | 457.0 ms | 2266.7 ms |
| K8s_workqueue | Go | 4507.4 ms | 4088.2 ms | 419.2 ms | 1579.0 ms |
| Toml | Go | 1979.8 ms | 1770.8 ms | 209.1 ms | 901.3 ms |
| Dustin_humanize | Go | 792.1 ms | 682.0 ms | 110.1 ms | 387.4 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1418029.8 ms | 866184.1 ms | 8 |
| LLGoFullLTOGlobalDCE | 1348129.5 ms | 820291.9 ms | 8 |
| LLGoFullLTOGlobalDCEPlugin | 1341346.0 ms | 808423.5 ms | 8 |
| LLGoDeadcodeDrop | 961754.0 ms | 328269.0 ms | 8 |
| LLGoNoLTO | 937000.0 ms | 320117.7 ms | 8 |
| Go | 158977.1 ms | 48911.1 ms | 9 |

Dependency download details are in `download-timings.log`.
