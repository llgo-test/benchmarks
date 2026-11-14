# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18150864 | 14981088 | 17315352 | 13929088 | 13626584 |
| Dustin_humanize | 4999050 | 6862128 | 5148432 | 6248760 | 4189392 | 4116520 |
| Etcdctl | 25896967 | 29964472 | 27406416 | 29067568 | 28038992 | 27623192 |
| Gorm_schema | 9421675 | 9882240 | 9082152 | 9210360 | 8830424 | 6423536 |
| IXGo | 47404128 | 46583960 | 45728568 | 45623960 | 45132560 | 44974544 |
| K8s_workqueue | 10681827 | 15999256 | 14201976 | 15346904 | 15076248 | 11407648 |
| Toml | 7324966 | 8706248 | 7226512 | 8072256 | 6394128 | 6292160 |
| Uber_zap | 10025000 | 16406408 | 13116264 | 15643624 | 13281960 | 12543480 |
| XGo | 18662581 | 24408072 | 20512016 | 23724120 | 19552296 | 19169536 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12670808 | 9595056 | 11635864 | 9362984 | 9140392 |
| Dustin_humanize | 3711728 | 4695992 | 3043488 | 4232472 | 2889296 | 2832632 |
| Etcdctl | 20251432 | 21480984 | 18991288 | 20147976 | 19470488 | 19073096 |
| Gorm_schema | 7186360 | 6959600 | 6186792 | 6424440 | 6165000 | 4554072 |
| IXGo | 37601624 | 31202696 | 30387560 | 28930832 | 28654768 | 28539736 |
| K8s_workqueue | 8105040 | 11212896 | 9460920 | 10349792 | 10200448 | 7660080 |
| Toml | 5573864 | 6122640 | 4697024 | 5554576 | 4476120 | 4392760 |
| Uber_zap | 7635104 | 11454944 | 8254624 | 10552768 | 8968008 | 8427760 |
| XGo | 14015312 | 17236192 | 13474104 | 16066672 | 13151592 | 12852376 |
