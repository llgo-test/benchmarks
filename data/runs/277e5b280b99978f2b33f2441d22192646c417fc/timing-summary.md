## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoDeadcodeDrop | 513954.0 ms | 487720.3 ms | 26233.6 ms | 158512.0 ms |
| IXGo | LLGoNoLTO | 502466.8 ms | 480525.1 ms | 21941.6 ms | 151132.5 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 426081.1 ms | 414114.6 ms | 11966.5 ms | 309253.8 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 421934.1 ms | 409941.1 ms | 11993.0 ms | 309930.7 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 418146.9 ms | 406375.9 ms | 11771.0 ms | 303705.8 ms |
| XGo | LLGoFullLTONoGlobalDCE | 312239.9 ms | 304006.6 ms | 8233.3 ms | 249164.5 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 292053.1 ms | 285541.3 ms | 6511.8 ms | 199979.0 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 275020.7 ms | 267156.2 ms | 7864.6 ms | 210122.2 ms |
| XGo | LLGoFullLTOGlobalDCE | 272630.2 ms | 264914.2 ms | 7716.0 ms | 208030.0 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 261787.7 ms | 255412.0 ms | 6375.7 ms | 167830.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 260053.7 ms | 253883.8 ms | 6169.9 ms | 167035.8 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 245073.5 ms | 239473.7 ms | 5599.8 ms | 172644.5 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 238958.6 ms | 233292.2 ms | 5666.4 ms | 168808.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 235814.0 ms | 230247.2 ms | 5566.7 ms | 166065.6 ms |
| Etcdctl | LLGoDeadcodeDrop | 224442.8 ms | 213547.0 ms | 10895.8 ms | 76583.7 ms |
| Etcdctl | LLGoNoLTO | 223445.2 ms | 213853.9 ms | 9591.3 ms | 75068.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 220492.9 ms | 215118.6 ms | 5374.3 ms | 146880.2 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 217597.7 ms | 212412.9 ms | 5184.8 ms | 145066.9 ms |
| Aws_restjson | LLGoDeadcodeDrop | 210115.7 ms | 204554.8 ms | 5560.9 ms | 66139.9 ms |
| Aws_restjson | LLGoNoLTO | 209780.4 ms | 204668.9 ms | 5111.5 ms | 65558.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 203171.6 ms | 198059.6 ms | 5112.0 ms | 132936.8 ms |
| Uber_zap | LLGoNoLTO | 170565.6 ms | 166497.2 ms | 4068.4 ms | 54434.4 ms |
| Uber_zap | LLGoDeadcodeDrop | 170518.1 ms | 165948.3 ms | 4569.8 ms | 54670.0 ms |
| K8s_workqueue | LLGoNoLTO | 165291.3 ms | 160985.2 ms | 4306.1 ms | 52872.5 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 162796.0 ms | 158135.6 ms | 4660.5 ms | 52669.8 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 145978.5 ms | 142164.2 ms | 3814.3 ms | 101841.0 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 142698.0 ms | 138910.6 ms | 3787.4 ms | 98735.3 ms |
| Toml | LLGoFullLTONoGlobalDCE | 131633.8 ms | 128179.0 ms | 3454.8 ms | 91407.1 ms |
| XGo | LLGoNoLTO | 124805.5 ms | 118912.9 ms | 5892.6 ms | 44578.9 ms |
| XGo | LLGoDeadcodeDrop | 124660.6 ms | 117352.1 ms | 7308.5 ms | 44061.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 119657.0 ms | 115997.2 ms | 3659.8 ms | 75384.8 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 115284.7 ms | 111886.1 ms | 3398.5 ms | 74005.8 ms |
| Toml | LLGoFullLTOGlobalDCE | 113779.1 ms | 110490.4 ms | 3288.7 ms | 73005.0 ms |
| Gorm_schema | LLGoDeadcodeDrop | 107356.9 ms | 103779.8 ms | 3577.1 ms | 36969.8 ms |
| Gorm_schema | LLGoNoLTO | 104884.5 ms | 101812.0 ms | 3072.5 ms | 35622.9 ms |
| Toml | LLGoDeadcodeDrop | 100230.0 ms | 97228.4 ms | 3001.6 ms | 33908.0 ms |
| Toml | LLGoNoLTO | 98179.7 ms | 95332.2 ms | 2847.5 ms | 32998.4 ms |
| IXGo | Go | 96924.6 ms | 82065.8 ms | 14858.8 ms | 26393.7 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 94835.7 ms | 92376.2 ms | 2459.5 ms | 68141.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 75033.8 ms | 72704.3 ms | 2329.5 ms | 48391.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 74620.7 ms | 72343.0 ms | 2277.7 ms | 48179.8 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 68876.7 ms | 66591.7 ms | 2285.0 ms | 25174.0 ms |
| Dustin_humanize | LLGoNoLTO | 67754.6 ms | 65781.4 ms | 1973.2 ms | 24825.9 ms |
| Etcdctl | Go | 37991.8 ms | 32654.3 ms | 5337.5 ms | 11517.6 ms |
| XGo | Go | 21528.9 ms | 18435.3 ms | 3093.6 ms | 6410.3 ms |
| Aws_restjson | Go | 8973.8 ms | 7436.6 ms | 1537.2 ms | 3684.0 ms |
| Gorm_schema | Go | 6498.0 ms | 5573.1 ms | 924.9 ms | 2539.6 ms |
| Uber_zap | Go | 5947.3 ms | 5029.4 ms | 917.9 ms | 2384.0 ms |
| K8s_workqueue | Go | 5298.6 ms | 4391.6 ms | 907.0 ms | 1871.7 ms |
| Toml | Go | 2267.4 ms | 1869.8 ms | 397.6 ms | 1069.4 ms |
| Dustin_humanize | Go | 883.5 ms | 682.6 ms | 200.9 ms | 433.1 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 1882707.3 ms | 1361916.4 ms | 8 |
| LLGoFullLTOGlobalDCE | 1735340.2 ms | 1209824.2 ms | 8 |
| LLGoFullLTOGlobalDCEPlugin | 1696529.5 ms | 1164805.3 ms | 8 |
| LLGoDeadcodeDrop | 1682951.0 ms | 548688.7 ms | 9 |
| LLGoNoLTO | 1667173.6 ms | 537092.4 ms | 9 |
| Go | 186314.0 ms | 56303.6 ms | 9 |

Dependency download details are in `download-timings.log`.
