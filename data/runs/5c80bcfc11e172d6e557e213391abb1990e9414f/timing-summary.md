## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 620829.3 ms | 607894.8 ms | 12934.4 ms | 328494.1 ms |
| IXGo | LLGoFullLTOGlobalDCE | 619577.3 ms | 606754.4 ms | 12822.9 ms | 316340.4 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 590345.5 ms | 578691.8 ms | 11653.6 ms | 300278.2 ms |
| IXGo | LLGoDeadcodeDrop | 467713.5 ms | 456399.7 ms | 11313.8 ms | 137145.3 ms |
| IXGo | LLGoNoLTO | 455487.4 ms | 445470.4 ms | 10017.0 ms | 133335.6 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 266632.8 ms | 261804.8 ms | 4828.0 ms | 163525.5 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 262073.4 ms | 256797.3 ms | 5276.1 ms | 160789.4 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 258398.2 ms | 253712.7 ms | 4685.4 ms | 159732.7 ms |
| Etcdctl | LLGoDeadcodeDrop | 196674.1 ms | 192328.5 ms | 4345.6 ms | 64981.6 ms |
| Etcdctl | LLGoNoLTO | 190774.6 ms | 186709.8 ms | 4064.7 ms | 63005.1 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 186204.5 ms | 182241.6 ms | 3962.9 ms | 127778.3 ms |
| XGo | LLGoFullLTOGlobalDCE | 185215.8 ms | 181735.1 ms | 3480.8 ms | 127858.6 ms |
| XGo | LLGoFullLTONoGlobalDCE | 184846.9 ms | 181544.4 ms | 3302.5 ms | 127737.9 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 139669.1 ms | 137258.1 ms | 2411.0 ms | 102213.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 129676.3 ms | 126801.9 ms | 2874.3 ms | 89876.3 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 127175.4 ms | 124821.4 ms | 2354.0 ms | 88387.1 ms |
| XGo | LLGoDeadcodeDrop | 113456.1 ms | 110548.2 ms | 2908.0 ms | 42044.6 ms |
| XGo | LLGoNoLTO | 111531.3 ms | 108723.8 ms | 2807.5 ms | 41122.4 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 111032.7 ms | 109137.2 ms | 1895.6 ms | 84453.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 106253.3 ms | 104017.6 ms | 2235.7 ms | 82404.6 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 103903.5 ms | 102071.3 ms | 1832.2 ms | 80440.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 102449.3 ms | 100451.7 ms | 1997.6 ms | 74036.2 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 101659.1 ms | 99734.0 ms | 1925.1 ms | 73585.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 91748.8 ms | 89828.9 ms | 1919.9 ms | 66908.6 ms |
| Aws_restjson | LLGoDeadcodeDrop | 87228.8 ms | 84940.4 ms | 2288.4 ms | 40446.7 ms |
| IXGo | Go | 86936.3 ms | 81516.9 ms | 5419.4 ms | 25002.6 ms |
| Aws_restjson | LLGoNoLTO | 84653.1 ms | 82531.5 ms | 2121.6 ms | 39237.8 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 63908.9 ms | 62459.5 ms | 1449.4 ms | 44096.1 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 63643.6 ms | 62101.1 ms | 1542.4 ms | 43602.8 ms |
| Uber_zap | LLGoDeadcodeDrop | 58917.5 ms | 57185.2 ms | 1732.3 ms | 25296.5 ms |
| Uber_zap | LLGoNoLTO | 58055.2 ms | 56513.2 ms | 1542.1 ms | 24688.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 54330.5 ms | 52831.5 ms | 1498.9 ms | 33121.3 ms |
| Toml | LLGoFullLTONoGlobalDCE | 50547.2 ms | 49319.3 ms | 1227.9 ms | 38014.4 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 50306.1 ms | 48740.3 ms | 1565.8 ms | 22626.4 ms |
| K8s_workqueue | LLGoNoLTO | 49941.1 ms | 48242.4 ms | 1698.7 ms | 23050.5 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 44097.0 ms | 42950.2 ms | 1146.8 ms | 30441.5 ms |
| Toml | LLGoFullLTOGlobalDCE | 43114.0 ms | 41928.2 ms | 1185.9 ms | 29948.2 ms |
| Gorm_schema | LLGoDeadcodeDrop | 40296.1 ms | 38972.6 ms | 1323.5 ms | 13664.3 ms |
| Gorm_schema | LLGoNoLTO | 39774.8 ms | 38498.7 ms | 1276.1 ms | 13466.7 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 35711.8 ms | 34768.6 ms | 943.2 ms | 27828.7 ms |
| Etcdctl | Go | 34430.9 ms | 32350.3 ms | 2080.6 ms | 10355.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 27294.2 ms | 26364.4 ms | 929.8 ms | 19107.9 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 27147.0 ms | 26185.9 ms | 961.1 ms | 19110.3 ms |
| Toml | LLGoDeadcodeDrop | 25687.3 ms | 24662.0 ms | 1025.2 ms | 9582.9 ms |
| Toml | LLGoNoLTO | 24568.5 ms | 23553.9 ms | 1014.5 ms | 9435.7 ms |
| XGo | Go | 19500.5 ms | 18288.6 ms | 1211.9 ms | 5812.1 ms |
| Dustin_humanize | LLGoNoLTO | 14535.6 ms | 13692.6 ms | 843.0 ms | 6165.9 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 14534.6 ms | 13700.7 ms | 834.0 ms | 6170.1 ms |
| Aws_restjson | Go | 8201.9 ms | 7502.6 ms | 699.4 ms | 3376.2 ms |
| Gorm_schema | Go | 5890.7 ms | 5467.6 ms | 423.1 ms | 2310.7 ms |
| Uber_zap | Go | 5612.8 ms | 5053.3 ms | 559.5 ms | 2538.8 ms |
| K8s_workqueue | Go | 4794.4 ms | 4271.9 ms | 522.5 ms | 1704.6 ms |
| Toml | Go | 2098.2 ms | 1852.6 ms | 245.6 ms | 955.3 ms |
| Dustin_humanize | Go | 812.4 ms | 671.3 ms | 141.1 ms | 385.0 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1538363.7 ms | 964795.5 ms | 9 |
| LLGoFullLTOGlobalDCE | 1535858.8 ms | 942026.6 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1523262.5 ms | 933289.7 ms | 9 |
| LLGoDeadcodeDrop | 1054814.1 ms | 361958.4 ms | 9 |
| LLGoNoLTO | 1029321.6 ms | 353508.5 ms | 9 |
| Go | 168278.1 ms | 52441.1 ms | 9 |

Dependency download details are in `download-timings.log`.
