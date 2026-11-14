## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 837082.4 ms | 811262.9 ms | 25819.4 ms | 543399.9 ms |
| IXGo | LLGoFullLTOGlobalDCE | 822775.4 ms | 796453.1 ms | 26322.3 ms | 532178.0 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 815158.6 ms | 789400.1 ms | 25758.5 ms | 530013.2 ms |
| IXGo | LLGoDeadcodeDrop | 490272.6 ms | 463663.2 ms | 26609.3 ms | 159713.2 ms |
| IXGo | LLGoNoLTO | 465374.9 ms | 443238.4 ms | 22136.5 ms | 146623.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 451113.3 ms | 438812.4 ms | 12300.9 ms | 326713.8 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 451009.2 ms | 438575.4 ms | 12433.8 ms | 329570.2 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 449826.8 ms | 437658.4 ms | 12168.4 ms | 325683.6 ms |
| XGo | LLGoFullLTONoGlobalDCE | 337984.5 ms | 329308.5 ms | 8676.0 ms | 268550.0 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 337727.8 ms | 330601.3 ms | 7126.5 ms | 225293.9 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 306627.1 ms | 299544.2 ms | 7082.9 ms | 194682.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 306265.8 ms | 299231.3 ms | 7034.4 ms | 193943.8 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 300495.2 ms | 292275.1 ms | 8220.1 ms | 229513.0 ms |
| XGo | LLGoFullLTOGlobalDCE | 295061.4 ms | 286975.2 ms | 8086.1 ms | 225839.9 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 286822.3 ms | 280315.8 ms | 6506.6 ms | 198681.6 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 277607.4 ms | 271190.7 ms | 6416.7 ms | 191859.2 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 276807.4 ms | 270428.7 ms | 6378.7 ms | 192301.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 266449.7 ms | 260184.5 ms | 6265.1 ms | 177261.6 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 262466.8 ms | 256172.1 ms | 6294.7 ms | 172770.8 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 242301.3 ms | 236328.4 ms | 5972.9 ms | 157821.4 ms |
| Aws_restjson | LLGoNoLTO | 242225.2 ms | 236834.1 ms | 5391.1 ms | 75947.1 ms |
| Aws_restjson | LLGoDeadcodeDrop | 241414.0 ms | 235296.6 ms | 6117.4 ms | 77175.0 ms |
| Etcdctl | LLGoDeadcodeDrop | 240178.1 ms | 229700.8 ms | 10477.3 ms | 83578.3 ms |
| Etcdctl | LLGoNoLTO | 237115.1 ms | 227683.3 ms | 9431.8 ms | 81771.8 ms |
| Uber_zap | LLGoNoLTO | 204289.5 ms | 199444.0 ms | 4845.5 ms | 65324.1 ms |
| Uber_zap | LLGoDeadcodeDrop | 203611.0 ms | 198447.7 ms | 5163.2 ms | 66276.6 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 195368.9 ms | 190319.1 ms | 5049.8 ms | 63855.4 ms |
| K8s_workqueue | LLGoNoLTO | 195184.9 ms | 190419.3 ms | 4765.6 ms | 62150.6 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 148276.7 ms | 144533.7 ms | 3743.0 ms | 100674.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 146584.4 ms | 142857.7 ms | 3726.7 ms | 98380.0 ms |
| Toml | LLGoFullLTONoGlobalDCE | 139117.3 ms | 135461.9 ms | 3655.4 ms | 92996.9 ms |
| XGo | LLGoNoLTO | 135421.6 ms | 129256.7 ms | 6164.9 ms | 49894.8 ms |
| XGo | LLGoDeadcodeDrop | 134239.9 ms | 126935.5 ms | 7304.4 ms | 48842.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 124827.3 ms | 121276.7 ms | 3550.6 ms | 76223.2 ms |
| Toml | LLGoFullLTOGlobalDCE | 123597.7 ms | 120122.1 ms | 3475.5 ms | 77011.0 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 123184.7 ms | 119643.0 ms | 3541.7 ms | 76155.6 ms |
| Gorm_schema | LLGoDeadcodeDrop | 113924.2 ms | 110499.9 ms | 3424.3 ms | 39762.6 ms |
| Gorm_schema | LLGoNoLTO | 110631.3 ms | 107512.2 ms | 3119.1 ms | 38195.6 ms |
| Toml | LLGoDeadcodeDrop | 106410.7 ms | 103413.6 ms | 2997.2 ms | 36422.5 ms |
| Toml | LLGoNoLTO | 105394.3 ms | 102535.5 ms | 2858.8 ms | 35866.5 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 96976.1 ms | 94488.8 ms | 2487.3 ms | 67825.9 ms |
| IXGo | Go | 96264.5 ms | 81311.5 ms | 14953.0 ms | 26293.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 78860.5 ms | 76610.2 ms | 2250.2 ms | 49442.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 78312.1 ms | 76027.8 ms | 2284.3 ms | 49029.4 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 73510.3 ms | 71402.0 ms | 2108.3 ms | 27341.1 ms |
| Dustin_humanize | LLGoNoLTO | 71897.3 ms | 69911.1 ms | 1986.2 ms | 26478.5 ms |
| Etcdctl | Go | 37552.7 ms | 32307.6 ms | 5245.1 ms | 11313.3 ms |
| XGo | Go | 21707.0 ms | 18639.0 ms | 3068.0 ms | 6454.8 ms |
| Aws_restjson | Go | 9250.0 ms | 7695.5 ms | 1554.5 ms | 3778.1 ms |
| Gorm_schema | Go | 6560.8 ms | 5628.5 ms | 932.2 ms | 2538.5 ms |
| Uber_zap | Go | 6025.0 ms | 5169.0 ms | 855.9 ms | 2401.4 ms |
| K8s_workqueue | Go | 5296.6 ms | 4386.8 ms | 909.7 ms | 1872.0 ms |
| Toml | Go | 2269.4 ms | 1882.5 ms | 386.9 ms | 1125.7 ms |
| Dustin_humanize | Go | 886.2 ms | 669.8 ms | 216.4 ms | 442.1 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2889879.9 ms | 2005908.0 ms | 9 |
| LLGoFullLTOGlobalDCE | 2766841.9 ms | 1871925.1 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2726597.1 ms | 1825984.0 ms | 9 |
| LLGoDeadcodeDrop | 1798929.7 ms | 602967.1 ms | 9 |
| LLGoNoLTO | 1767534.1 ms | 582252.1 ms | 9 |
| Go | 185812.1 ms | 56219.6 ms | 9 |

Dependency download details are in `download-timings.log`.
