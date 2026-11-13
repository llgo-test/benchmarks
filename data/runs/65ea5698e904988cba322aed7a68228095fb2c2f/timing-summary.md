## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 639504.5 ms | 619400.3 ms | 20104.2 ms | 414820.2 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 635387.6 ms | 615358.0 ms | 20029.6 ms | 409339.6 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 602787.0 ms | 582909.2 ms | 19877.8 ms | 409008.3 ms |
| IXGo | LLGoNoLTO | 344358.4 ms | 327853.8 ms | 16504.6 ms | 107036.7 ms |
| IXGo | LLGoDeadcodeDrop | 324836.0 ms | 305678.4 ms | 19157.5 ms | 107434.0 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 324072.6 ms | 314728.8 ms | 9343.8 ms | 244617.3 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 310655.4 ms | 301496.6 ms | 9158.8 ms | 233466.6 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 306134.5 ms | 296880.7 ms | 9253.8 ms | 228590.1 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 250927.0 ms | 244978.0 ms | 5948.9 ms | 170163.8 ms |
| XGo | LLGoFullLTONoGlobalDCE | 245353.4 ms | 238454.9 ms | 6898.5 ms | 199614.7 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 236864.8 ms | 231217.5 ms | 5647.3 ms | 155011.6 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 217223.4 ms | 211846.5 ms | 5376.9 ms | 142222.2 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 216895.6 ms | 210594.1 ms | 6301.5 ms | 170097.8 ms |
| XGo | LLGoFullLTOGlobalDCE | 210194.9 ms | 203881.3 ms | 6313.6 ms | 164387.0 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 203205.1 ms | 198370.1 ms | 4835.0 ms | 145921.0 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 196517.4 ms | 191416.7 ms | 5100.6 ms | 142223.5 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 190120.9 ms | 185077.6 ms | 5043.3 ms | 136365.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 184170.0 ms | 179361.6 ms | 4808.5 ms | 126760.1 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 182491.7 ms | 177582.6 ms | 4909.0 ms | 125475.8 ms |
| Aws_restjson | LLGoNoLTO | 170941.9 ms | 166712.9 ms | 4229.0 ms | 53688.1 ms |
| Aws_restjson | LLGoDeadcodeDrop | 165816.5 ms | 161288.1 ms | 4528.4 ms | 54036.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 163215.1 ms | 158619.6 ms | 4595.5 ms | 110563.9 ms |
| Etcdctl | LLGoDeadcodeDrop | 160696.3 ms | 152910.8 ms | 7785.5 ms | 57308.5 ms |
| Etcdctl | LLGoNoLTO | 153340.0 ms | 146148.2 ms | 7191.8 ms | 53486.6 ms |
| K8s_workqueue | LLGoNoLTO | 138856.6 ms | 135057.6 ms | 3799.0 ms | 44431.3 ms |
| Uber_zap | LLGoNoLTO | 137164.1 ms | 133721.6 ms | 3442.6 ms | 44920.3 ms |
| Uber_zap | LLGoDeadcodeDrop | 129184.9 ms | 125218.9 ms | 3966.0 ms | 43136.7 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 126315.0 ms | 122302.8 ms | 4012.2 ms | 42748.5 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 111015.3 ms | 107999.7 ms | 3015.6 ms | 76958.1 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 109449.1 ms | 106480.0 ms | 2969.1 ms | 77726.0 ms |
| XGo | LLGoDeadcodeDrop | 93491.4 ms | 88297.3 ms | 5194.1 ms | 35131.0 ms |
| XGo | LLGoNoLTO | 90424.6 ms | 85833.4 ms | 4591.2 ms | 33731.2 ms |
| Toml | LLGoFullLTONoGlobalDCE | 89957.0 ms | 87066.6 ms | 2890.4 ms | 62748.7 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 87490.3 ms | 84707.6 ms | 2782.7 ms | 56948.5 ms |
| Toml | LLGoFullLTOGlobalDCE | 84900.3 ms | 82220.0 ms | 2680.3 ms | 56147.3 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 82796.9 ms | 80019.7 ms | 2777.2 ms | 52888.2 ms |
| Gorm_schema | LLGoNoLTO | 74396.8 ms | 72035.8 ms | 2361.0 ms | 26238.5 ms |
| Gorm_schema | LLGoDeadcodeDrop | 73160.3 ms | 70206.0 ms | 2954.2 ms | 26235.2 ms |
| Toml | LLGoNoLTO | 72469.3 ms | 70235.5 ms | 2233.8 ms | 25171.3 ms |
| Toml | LLGoDeadcodeDrop | 66734.6 ms | 64298.9 ms | 2435.7 ms | 23624.5 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 66287.2 ms | 64365.0 ms | 1922.2 ms | 48806.6 ms |
| IXGo | Go | 61363.8 ms | 50874.0 ms | 10489.8 ms | 16903.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 56168.8 ms | 54426.8 ms | 1742.0 ms | 37236.1 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 53410.2 ms | 51675.2 ms | 1735.0 ms | 35134.5 ms |
| Dustin_humanize | LLGoNoLTO | 47062.9 ms | 45445.0 ms | 1617.9 ms | 17851.3 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 44436.1 ms | 42894.3 ms | 1541.7 ms | 16945.1 ms |
| Etcdctl | Go | 24352.9 ms | 20615.1 ms | 3737.8 ms | 7471.2 ms |
| XGo | Go | 14744.1 ms | 12480.7 ms | 2263.5 ms | 4477.8 ms |
| Aws_restjson | Go | 5959.5 ms | 4864.1 ms | 1095.4 ms | 2549.2 ms |
| Gorm_schema | Go | 4289.1 ms | 3603.5 ms | 685.6 ms | 1707.4 ms |
| Uber_zap | Go | 3959.2 ms | 3307.1 ms | 652.1 ms | 1660.7 ms |
| K8s_workqueue | Go | 3353.3 ms | 2736.9 ms | 616.4 ms | 1233.6 ms |
| Toml | Go | 1539.2 ms | 1233.3 ms | 305.9 ms | 789.8 ms |
| Dustin_humanize | Go | 619.2 ms | 482.6 ms | 136.6 ms | 327.6 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2082159.2 ms | 1494971.9 ms | 9 |
| LLGoFullLTOGlobalDCE | 2005913.0 ms | 1390835.2 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 1969123.6 ms | 1347435.9 ms | 9 |
| LLGoNoLTO | 1229014.6 ms | 406555.4 ms | 9 |
| LLGoDeadcodeDrop | 1184671.0 ms | 406599.8 ms | 9 |
| Go | 120180.4 ms | 37121.0 ms | 9 |

Dependency download details are in `download-timings.log`.
