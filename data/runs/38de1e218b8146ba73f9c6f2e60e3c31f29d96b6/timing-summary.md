## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 858814.3 ms | 832097.7 ms | 26716.6 ms | 552102.4 ms |
| IXGo | LLGoFullLTOGlobalDCE | 843227.4 ms | 816781.0 ms | 26446.4 ms | 533452.8 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 826440.7 ms | 799976.6 ms | 26464.1 ms | 531098.9 ms |
| IXGo | LLGoDeadcodeDrop | 497010.6 ms | 469918.1 ms | 27092.6 ms | 153874.0 ms |
| IXGo | LLGoNoLTO | 470382.2 ms | 447481.3 ms | 22900.9 ms | 143050.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 452403.7 ms | 440099.6 ms | 12304.0 ms | 325682.1 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 448919.3 ms | 436471.7 ms | 12447.6 ms | 324826.4 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 447622.3 ms | 435215.0 ms | 12407.2 ms | 321805.6 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 336115.2 ms | 328621.9 ms | 7493.3 ms | 220530.8 ms |
| XGo | LLGoFullLTONoGlobalDCE | 331654.8 ms | 322852.2 ms | 8802.6 ms | 262689.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 304150.8 ms | 296976.7 ms | 7174.0 ms | 189469.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 303103.2 ms | 295852.4 ms | 7250.8 ms | 188923.5 ms |
| XGo | LLGoFullLTOGlobalDCE | 294821.1 ms | 286343.7 ms | 8477.4 ms | 224866.8 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 291539.7 ms | 283254.3 ms | 8285.5 ms | 221841.3 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 280096.3 ms | 273643.8 ms | 6452.5 ms | 191064.5 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 272030.9 ms | 265693.7 ms | 6337.2 ms | 185839.7 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 270589.5 ms | 264066.4 ms | 6523.1 ms | 185676.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 259028.0 ms | 252821.9 ms | 6206.1 ms | 169290.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 255893.4 ms | 249747.1 ms | 6146.3 ms | 165569.9 ms |
| Aws_restjson | LLGoNoLTO | 252956.9 ms | 247023.0 ms | 5933.9 ms | 77069.9 ms |
| Aws_restjson | LLGoDeadcodeDrop | 247864.1 ms | 241559.6 ms | 6304.4 ms | 76829.2 ms |
| Etcdctl | LLGoDeadcodeDrop | 243212.2 ms | 232492.8 ms | 10719.4 ms | 81728.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 237411.7 ms | 231445.6 ms | 5966.1 ms | 151660.6 ms |
| Etcdctl | LLGoNoLTO | 237016.8 ms | 227414.6 ms | 9602.2 ms | 78899.0 ms |
| Uber_zap | LLGoDeadcodeDrop | 204083.8 ms | 198955.0 ms | 5128.8 ms | 64451.9 ms |
| Uber_zap | LLGoNoLTO | 203733.5 ms | 199008.9 ms | 4724.6 ms | 63257.4 ms |
| K8s_workqueue | LLGoNoLTO | 197077.6 ms | 192163.0 ms | 4914.6 ms | 61688.0 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 196509.2 ms | 191219.9 ms | 5289.3 ms | 62715.0 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 150444.4 ms | 146526.4 ms | 3918.0 ms | 102127.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 148697.1 ms | 144895.5 ms | 3801.5 ms | 99933.1 ms |
| Toml | LLGoFullLTONoGlobalDCE | 140056.7 ms | 136345.8 ms | 3710.9 ms | 95263.2 ms |
| XGo | LLGoDeadcodeDrop | 131811.3 ms | 124384.2 ms | 7427.0 ms | 46141.3 ms |
| XGo | LLGoNoLTO | 131688.0 ms | 125494.1 ms | 6193.9 ms | 46664.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 126814.6 ms | 123078.0 ms | 3736.6 ms | 77631.1 ms |
| Toml | LLGoFullLTOGlobalDCE | 122804.7 ms | 119312.7 ms | 3492.1 ms | 77603.2 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 122355.9 ms | 118868.2 ms | 3487.8 ms | 77264.8 ms |
| Gorm_schema | LLGoNoLTO | 113632.0 ms | 110439.5 ms | 3192.4 ms | 38082.2 ms |
| Gorm_schema | LLGoDeadcodeDrop | 113148.5 ms | 109563.5 ms | 3585.0 ms | 38731.7 ms |
| Toml | LLGoNoLTO | 105194.7 ms | 102354.0 ms | 2840.8 ms | 35310.9 ms |
| Toml | LLGoDeadcodeDrop | 104934.1 ms | 101939.8 ms | 2994.3 ms | 35414.8 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 98758.2 ms | 96211.1 ms | 2547.1 ms | 69427.0 ms |
| IXGo | Go | 98554.6 ms | 83520.0 ms | 15034.6 ms | 26878.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 80591.1 ms | 78203.8 ms | 2387.3 ms | 50498.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 79361.3 ms | 77018.5 ms | 2342.8 ms | 49678.1 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 73455.5 ms | 71270.0 ms | 2185.5 ms | 26781.4 ms |
| Dustin_humanize | LLGoNoLTO | 71799.6 ms | 69806.5 ms | 1993.1 ms | 26082.7 ms |
| Etcdctl | Go | 38168.2 ms | 32728.3 ms | 5439.9 ms | 11576.6 ms |
| XGo | Go | 22275.6 ms | 19038.1 ms | 3237.5 ms | 6574.8 ms |
| Aws_restjson | Go | 9123.9 ms | 7593.5 ms | 1530.4 ms | 3754.7 ms |
| Gorm_schema | Go | 6624.7 ms | 5660.0 ms | 964.7 ms | 2607.1 ms |
| Uber_zap | Go | 5975.0 ms | 5089.1 ms | 885.9 ms | 2420.2 ms |
| K8s_workqueue | Go | 5393.6 ms | 4379.8 ms | 1013.8 ms | 2300.4 ms |
| Toml | Go | 2281.4 ms | 1888.9 ms | 392.5 ms | 1077.4 ms |
| Dustin_humanize | Go | 902.4 ms | 703.5 ms | 199.0 ms | 446.8 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2883075.1 ms | 1982704.1 ms | 9 |
| LLGoFullLTOGlobalDCE | 2771743.4 ms | 1851939.3 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2728927.6 ms | 1811174.2 ms | 9 |
| LLGoDeadcodeDrop | 1812029.2 ms | 586667.6 ms | 9 |
| LLGoNoLTO | 1783481.2 ms | 570104.3 ms | 9 |
| Go | 189299.4 ms | 57636.2 ms | 9 |

Dependency download details are in `download-timings.log`.
