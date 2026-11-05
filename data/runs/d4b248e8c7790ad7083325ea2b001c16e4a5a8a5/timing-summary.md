## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTONoGlobalDCE | 760773.9 ms | 737563.1 ms | 23210.8 ms | 462381.4 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 728285.7 ms | 704897.1 ms | 23388.5 ms | 470934.5 ms |
| IXGo | LLGoFullLTOGlobalDCE | 720535.4 ms | 696957.9 ms | 23577.5 ms | 450393.4 ms |
| IXGo | LLGoDeadcodeDrop | 408743.7 ms | 385163.0 ms | 23580.7 ms | 126819.0 ms |
| IXGo | LLGoNoLTO | 365805.4 ms | 346183.3 ms | 19622.1 ms | 111091.7 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 360006.6 ms | 349192.9 ms | 10813.7 ms | 266582.6 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 347054.0 ms | 336015.8 ms | 11038.2 ms | 257922.6 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 338780.1 ms | 328602.2 ms | 10177.9 ms | 251499.9 ms |
| XGo | LLGoFullLTONoGlobalDCE | 254389.2 ms | 247060.8 ms | 7328.4 ms | 206430.7 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 234850.1 ms | 228973.0 ms | 5877.1 ms | 164825.6 ms |
| XGo | LLGoFullLTOGlobalDCE | 231306.3 ms | 224105.7 ms | 7200.6 ms | 181098.1 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 223189.9 ms | 216154.7 ms | 7035.3 ms | 173182.4 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 222846.5 ms | 217156.0 ms | 5690.5 ms | 145118.5 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 213779.9 ms | 208126.2 ms | 5653.7 ms | 141343.3 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 204334.8 ms | 199295.5 ms | 5039.2 ms | 147770.4 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 188713.0 ms | 183727.9 ms | 4985.1 ms | 136673.1 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 185327.6 ms | 180450.3 ms | 4877.3 ms | 133742.4 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 179632.0 ms | 174968.1 ms | 4663.9 ms | 123359.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 174371.0 ms | 169585.1 ms | 4785.9 ms | 120466.4 ms |
| Etcdctl | LLGoDeadcodeDrop | 171706.5 ms | 162164.0 ms | 9542.4 ms | 59520.6 ms |
| Etcdctl | LLGoNoLTO | 170432.9 ms | 161793.4 ms | 8639.5 ms | 58133.4 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 164982.7 ms | 160258.0 ms | 4724.7 ms | 112212.0 ms |
| Aws_restjson | LLGoNoLTO | 163162.7 ms | 158589.7 ms | 4573.0 ms | 51513.5 ms |
| Aws_restjson | LLGoDeadcodeDrop | 159475.3 ms | 154385.2 ms | 5090.1 ms | 51013.5 ms |
| Uber_zap | LLGoDeadcodeDrop | 135267.5 ms | 131019.0 ms | 4248.5 ms | 44742.7 ms |
| Uber_zap | LLGoNoLTO | 129170.6 ms | 125134.3 ms | 4036.4 ms | 42294.8 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 122638.5 ms | 118513.6 ms | 4124.9 ms | 40781.2 ms |
| K8s_workqueue | LLGoNoLTO | 120718.3 ms | 117037.8 ms | 3680.5 ms | 39428.3 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 115753.7 ms | 112232.3 ms | 3521.4 ms | 83187.9 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 115164.0 ms | 111673.8 ms | 3490.2 ms | 81984.7 ms |
| Toml | LLGoFullLTONoGlobalDCE | 110086.3 ms | 106758.9 ms | 3327.4 ms | 79532.2 ms |
| XGo | LLGoNoLTO | 97084.2 ms | 91692.9 ms | 5391.3 ms | 35827.9 ms |
| XGo | LLGoDeadcodeDrop | 96234.6 ms | 89810.0 ms | 6424.6 ms | 35384.5 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 95599.8 ms | 92606.2 ms | 2993.6 ms | 63578.6 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 93658.0 ms | 90360.0 ms | 3298.0 ms | 60506.6 ms |
| Toml | LLGoFullLTOGlobalDCE | 89286.1 ms | 86347.7 ms | 2938.4 ms | 58804.6 ms |
| Gorm_schema | LLGoNoLTO | 79671.0 ms | 76806.9 ms | 2864.1 ms | 27743.5 ms |
| Gorm_schema | LLGoDeadcodeDrop | 79396.8 ms | 76170.1 ms | 3226.7 ms | 28295.0 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 74372.4 ms | 72054.8 ms | 2317.6 ms | 55047.8 ms |
| Toml | LLGoNoLTO | 73995.7 ms | 71427.3 ms | 2568.3 ms | 25476.9 ms |
| Toml | LLGoDeadcodeDrop | 73510.1 ms | 70804.3 ms | 2705.8 ms | 25615.1 ms |
| IXGo | Go | 73091.9 ms | 59987.7 ms | 13104.2 ms | 20087.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 62039.3 ms | 59915.7 ms | 2123.6 ms | 41568.0 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 59096.1 ms | 57045.8 ms | 2050.3 ms | 39252.2 ms |
| Dustin_humanize | LLGoNoLTO | 50718.0 ms | 48959.3 ms | 1758.7 ms | 19095.8 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 50447.0 ms | 48511.4 ms | 1935.7 ms | 19249.3 ms |
| Etcdctl | Go | 30224.2 ms | 25502.4 ms | 4721.7 ms | 9332.1 ms |
| XGo | Go | 16786.6 ms | 14056.2 ms | 2730.4 ms | 5073.8 ms |
| Aws_restjson | Go | 7481.8 ms | 6097.7 ms | 1384.1 ms | 3242.2 ms |
| Gorm_schema | Go | 5058.6 ms | 4185.3 ms | 873.4 ms | 2014.1 ms |
| Uber_zap | Go | 4638.3 ms | 3824.7 ms | 813.6 ms | 1929.4 ms |
| K8s_workqueue | Go | 4139.9 ms | 3314.1 ms | 825.8 ms | 2041.0 ms |
| Toml | Go | 1735.9 ms | 1398.8 ms | 337.1 ms | 838.6 ms |
| Dustin_humanize | Go | 730.8 ms | 533.4 ms | 197.4 ms | 376.4 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2303279.9 ms | 1602431.7 ms | 9 |
| LLGoFullLTOGlobalDCE | 2136713.1 ms | 1462360.3 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2108221.3 ms | 1444607.5 ms | 9 |
| LLGoDeadcodeDrop | 1297420.0 ms | 431420.9 ms | 9 |
| LLGoNoLTO | 1250758.8 ms | 410605.9 ms | 9 |
| Go | 143888.0 ms | 44934.5 ms | 9 |

Dependency download details are in `download-timings.log`.
