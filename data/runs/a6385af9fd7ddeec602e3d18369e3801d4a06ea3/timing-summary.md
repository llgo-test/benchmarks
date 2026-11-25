## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCE | 915607.7 ms | 889544.8 ms | 26062.8 ms | 577787.3 ms |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 857326.7 ms | 831223.1 ms | 26103.6 ms | 555038.2 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 821801.7 ms | 795741.2 ms | 26060.4 ms | 537684.7 ms |
| IXGo | LLGoDeadcodeDrop | 513747.1 ms | 486054.5 ms | 27692.6 ms | 166760.4 ms |
| IXGo | LLGoNoLTO | 503005.2 ms | 480140.5 ms | 22864.8 ms | 156984.8 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 459980.0 ms | 447827.9 ms | 12152.0 ms | 332821.7 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 455597.5 ms | 443385.9 ms | 12211.6 ms | 330386.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 443601.9 ms | 431307.9 ms | 12294.0 ms | 317572.7 ms |
| XGo | LLGoFullLTONoGlobalDCE | 333674.6 ms | 325494.4 ms | 8180.3 ms | 262955.0 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 317182.2 ms | 310484.3 ms | 6697.9 ms | 212522.1 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 305153.5 ms | 298546.6 ms | 6606.9 ms | 189755.6 ms |
| XGo | LLGoFullLTOGlobalDCE | 289879.6 ms | 281628.6 ms | 8250.9 ms | 219656.6 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 283811.2 ms | 275639.6 ms | 8171.6 ms | 213602.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 280918.0 ms | 274351.7 ms | 6566.2 ms | 176145.5 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 272828.3 ms | 266824.4 ms | 6003.9 ms | 187729.7 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 269222.5 ms | 263416.2 ms | 5806.2 ms | 187221.4 ms |
| Aws_restjson | LLGoNoLTO | 263880.8 ms | 258072.3 ms | 5808.5 ms | 82135.3 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 259308.3 ms | 253425.6 ms | 5882.7 ms | 180276.5 ms |
| Etcdctl | LLGoDeadcodeDrop | 251505.0 ms | 240555.2 ms | 10949.8 ms | 86782.9 ms |
| Aws_restjson | LLGoDeadcodeDrop | 250899.5 ms | 244614.8 ms | 6284.7 ms | 81071.9 ms |
| Etcdctl | LLGoNoLTO | 244458.5 ms | 235098.2 ms | 9360.3 ms | 83646.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 242463.3 ms | 236772.9 ms | 5690.4 ms | 160026.7 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 242414.3 ms | 236821.2 ms | 5593.1 ms | 158435.2 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 219077.6 ms | 213687.6 ms | 5390.0 ms | 140560.0 ms |
| Uber_zap | LLGoDeadcodeDrop | 213035.4 ms | 207673.3 ms | 5362.1 ms | 69385.0 ms |
| Uber_zap | LLGoNoLTO | 212263.3 ms | 207261.6 ms | 5001.7 ms | 67728.2 ms |
| K8s_workqueue | LLGoNoLTO | 209297.3 ms | 204099.9 ms | 5197.4 ms | 67196.1 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 207624.4 ms | 202524.8 ms | 5099.7 ms | 67999.7 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 160664.2 ms | 156707.7 ms | 3956.5 ms | 110450.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 151593.1 ms | 147645.8 ms | 3947.3 ms | 102783.8 ms |
| XGo | LLGoNoLTO | 144504.6 ms | 138189.5 ms | 6315.1 ms | 52998.5 ms |
| Toml | LLGoFullLTONoGlobalDCE | 142142.2 ms | 138489.3 ms | 3652.9 ms | 95860.2 ms |
| XGo | LLGoDeadcodeDrop | 142122.1 ms | 134485.5 ms | 7636.6 ms | 51467.8 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 128583.9 ms | 124878.2 ms | 3705.7 ms | 78680.9 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 128007.9 ms | 124452.9 ms | 3555.1 ms | 80785.5 ms |
| Toml | LLGoFullLTOGlobalDCE | 125303.1 ms | 121734.2 ms | 3568.9 ms | 78522.2 ms |
| Gorm_schema | LLGoDeadcodeDrop | 119512.4 ms | 115783.6 ms | 3728.8 ms | 41791.3 ms |
| Gorm_schema | LLGoNoLTO | 118224.0 ms | 114947.8 ms | 3276.1 ms | 40945.9 ms |
| Toml | LLGoNoLTO | 112469.6 ms | 109528.5 ms | 2941.1 ms | 38517.9 ms |
| Toml | LLGoDeadcodeDrop | 111220.1 ms | 107946.6 ms | 3273.5 ms | 38472.9 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 101834.4 ms | 99226.1 ms | 2608.3 ms | 72317.7 ms |
| IXGo | Go | 97144.6 ms | 82240.5 ms | 14904.1 ms | 26708.7 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 85103.3 ms | 82703.9 ms | 2399.4 ms | 53815.6 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 81807.4 ms | 79464.0 ms | 2343.5 ms | 51908.9 ms |
| Dustin_humanize | LLGoNoLTO | 75344.9 ms | 73337.5 ms | 2007.4 ms | 28081.1 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 75266.2 ms | 73064.9 ms | 2201.3 ms | 28148.7 ms |
| Etcdctl | Go | 37755.9 ms | 32519.7 ms | 5236.2 ms | 11338.9 ms |
| XGo | Go | 21653.4 ms | 18510.6 ms | 3142.8 ms | 6522.9 ms |
| Aws_restjson | Go | 9115.2 ms | 7570.5 ms | 1544.7 ms | 3669.8 ms |
| Gorm_schema | Go | 6565.8 ms | 5584.7 ms | 981.1 ms | 2609.9 ms |
| Uber_zap | Go | 5975.1 ms | 5047.6 ms | 927.5 ms | 2384.4 ms |
| K8s_workqueue | Go | 5295.4 ms | 4388.2 ms | 907.2 ms | 1986.8 ms |
| Toml | Go | 2274.5 ms | 1863.6 ms | 410.8 ms | 1081.4 ms |
| Dustin_humanize | Go | 1014.5 ms | 709.9 ms | 304.6 ms | 712.0 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2865033.3 ms | 1990182.8 ms | 9 |
| LLGoFullLTOGlobalDCE | 2824632.0 ms | 1885235.0 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2685222.9 ms | 1789884.8 ms | 9 |
| LLGoDeadcodeDrop | 1884932.3 ms | 631880.6 ms | 9 |
| LLGoNoLTO | 1883448.2 ms | 618234.5 ms | 9 |
| Go | 186794.4 ms | 57014.8 ms | 9 |

Dependency download details are in `download-timings.log`.
