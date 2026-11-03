## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 1005243.0 ms | 979573.1 ms | 25669.8 ms | 596552.1 ms |
| IXGo | LLGoFullLTOGlobalDCE | 938964.7 ms | 912613.0 ms | 26351.7 ms | 572684.7 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 927372.8 ms | 901394.8 ms | 25978.0 ms | 569638.5 ms |
| IXGo | LLGoDeadcodeDrop | 632002.9 ms | 604765.1 ms | 27237.8 ms | 188804.8 ms |
| IXGo | LLGoNoLTO | 598211.2 ms | 576033.5 ms | 22177.6 ms | 178048.8 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 446048.0 ms | 433967.6 ms | 12080.4 ms | 327820.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 444043.0 ms | 431939.5 ms | 12103.5 ms | 323386.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 438737.0 ms | 426633.7 ms | 12103.2 ms | 319395.3 ms |
| XGo | LLGoFullLTONoGlobalDCE | 328890.7 ms | 320457.1 ms | 8433.6 ms | 263409.4 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 309881.4 ms | 303040.5 ms | 6840.9 ms | 212291.7 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 287187.8 ms | 279125.0 ms | 8062.8 ms | 219606.4 ms |
| XGo | LLGoFullLTOGlobalDCE | 286856.5 ms | 278957.0 ms | 7899.4 ms | 220113.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 275803.7 ms | 269380.6 ms | 6423.0 ms | 176378.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 267560.4 ms | 261237.2 ms | 6323.2 ms | 171780.5 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 262319.3 ms | 256659.6 ms | 5659.7 ms | 186558.8 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 247314.0 ms | 241566.5 ms | 5747.4 ms | 173771.1 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 247008.2 ms | 241398.2 ms | 5610.0 ms | 176525.5 ms |
| Etcdctl | LLGoDeadcodeDrop | 233635.1 ms | 222628.7 ms | 11006.4 ms | 79845.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 232923.3 ms | 227563.9 ms | 5359.4 ms | 155610.4 ms |
| Etcdctl | LLGoNoLTO | 225278.1 ms | 215324.4 ms | 9953.7 ms | 76020.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 223871.5 ms | 218585.0 ms | 5286.5 ms | 149900.3 ms |
| Aws_restjson | LLGoNoLTO | 220474.0 ms | 215128.0 ms | 5345.9 ms | 68991.7 ms |
| Aws_restjson | LLGoDeadcodeDrop | 213994.7 ms | 208253.3 ms | 5741.4 ms | 67076.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 208158.0 ms | 202868.0 ms | 5290.0 ms | 136661.1 ms |
| Uber_zap | LLGoNoLTO | 176384.0 ms | 172093.4 ms | 4290.6 ms | 56238.4 ms |
| Uber_zap | LLGoDeadcodeDrop | 173470.9 ms | 168777.8 ms | 4693.1 ms | 55808.0 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 167332.6 ms | 162342.3 ms | 4990.3 ms | 54049.1 ms |
| K8s_workqueue | LLGoNoLTO | 165197.3 ms | 160722.1 ms | 4475.2 ms | 52970.1 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 151319.1 ms | 147316.8 ms | 4002.3 ms | 106998.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 150696.1 ms | 146704.1 ms | 3992.0 ms | 105067.5 ms |
| Toml | LLGoFullLTONoGlobalDCE | 135692.1 ms | 132087.7 ms | 3604.5 ms | 93821.5 ms |
| XGo | LLGoDeadcodeDrop | 129314.9 ms | 121920.2 ms | 7394.8 ms | 45575.5 ms |
| XGo | LLGoNoLTO | 128505.7 ms | 122109.4 ms | 6396.3 ms | 46209.2 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 122360.2 ms | 118529.9 ms | 3830.4 ms | 77184.8 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 120884.2 ms | 117392.7 ms | 3491.6 ms | 78150.4 ms |
| Toml | LLGoFullLTOGlobalDCE | 120466.9 ms | 116976.7 ms | 3490.2 ms | 77638.6 ms |
| Gorm_schema | LLGoNoLTO | 109520.8 ms | 106265.0 ms | 3255.8 ms | 37124.7 ms |
| Gorm_schema | LLGoDeadcodeDrop | 109423.2 ms | 105628.5 ms | 3794.7 ms | 37839.1 ms |
| Toml | LLGoDeadcodeDrop | 101968.7 ms | 98849.1 ms | 3119.6 ms | 34811.3 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 100914.0 ms | 98362.2 ms | 2551.8 ms | 73114.1 ms |
| IXGo | Go | 100701.0 ms | 85525.9 ms | 15175.1 ms | 27516.5 ms |
| Toml | LLGoNoLTO | 99865.2 ms | 96907.7 ms | 2957.5 ms | 33604.8 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 76699.2 ms | 74345.1 ms | 2354.1 ms | 49744.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 76517.8 ms | 74198.5 ms | 2319.4 ms | 49443.2 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 70251.5 ms | 67913.6 ms | 2337.9 ms | 25831.9 ms |
| Dustin_humanize | LLGoNoLTO | 69915.6 ms | 67928.8 ms | 1986.8 ms | 25682.3 ms |
| Etcdctl | Go | 38446.0 ms | 33145.5 ms | 5300.5 ms | 11703.4 ms |
| XGo | Go | 22563.8 ms | 19573.3 ms | 2990.5 ms | 6588.3 ms |
| Aws_restjson | Go | 9578.3 ms | 8018.9 ms | 1559.4 ms | 4031.9 ms |
| Gorm_schema | Go | 6795.9 ms | 5781.9 ms | 1014.1 ms | 2791.9 ms |
| Uber_zap | Go | 6063.5 ms | 5150.4 ms | 913.1 ms | 2433.8 ms |
| K8s_workqueue | Go | 5535.4 ms | 4626.1 ms | 909.3 ms | 2007.8 ms |
| Toml | Go | 2291.6 ms | 1917.8 ms | 373.9 ms | 1094.5 ms |
| Dustin_humanize | Go | 985.1 ms | 721.4 ms | 263.8 ms | 659.7 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2909445.6 ms | 2010178.5 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2767996.3 ms | 1809282.9 ms | 9 |
| LLGoFullLTOGlobalDCE | 2756290.9 ms | 1843785.7 ms | 9 |
| LLGoDeadcodeDrop | 1831394.7 ms | 589641.6 ms | 9 |
| LLGoNoLTO | 1793351.7 ms | 574890.6 ms | 9 |
| Go | 192960.8 ms | 58827.7 ms | 9 |

Dependency download details are in `download-timings.log`.
