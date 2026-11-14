# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18152792 | 14982168 | 17316904 | 13930904 | 13628016 |
| Dustin_humanize | 4999050 | 6863264 | 5149600 | 6250240 | 4191176 | 4118560 |
| Etcdctl | 25896967 | 29964984 | 27407704 | 29070072 | 28040304 | 27626256 |
| Gorm_schema | 9421675 | 9883272 | 9083232 | 9212280 | 8831680 | 6425152 |
| IXGo | 47404128 | 46584328 | 45727712 | 45627624 | 45135128 | 44976800 |
| K8s_workqueue | 10681827 | 16000464 | 14203064 | 15348440 | 15077952 | 11409320 |
| Toml | 7324966 | 8707480 | 7227880 | 8073480 | 6396048 | 6294240 |
| Uber_zap | 10025000 | 16407632 | 13117368 | 15645864 | 13283400 | 12545136 |
| XGo | 18662581 | 24409360 | 20513280 | 23725568 | 19554680 | 19170704 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12671648 | 9595920 | 11636824 | 9364000 | 9141432 |
| Dustin_humanize | 3711728 | 4696832 | 3044344 | 4233416 | 2890248 | 2833632 |
| Etcdctl | 20251432 | 21481840 | 18992128 | 20148984 | 19471536 | 19074184 |
| Gorm_schema | 7186360 | 6960144 | 6187336 | 6425504 | 6166112 | 4555168 |
| IXGo | 37601624 | 31203264 | 30388096 | 28931912 | 28655848 | 28540880 |
| K8s_workqueue | 8105040 | 11213768 | 9461760 | 10350768 | 10201448 | 7661064 |
| Toml | 5573864 | 6123488 | 4697880 | 5555608 | 4477152 | 4393824 |
| Uber_zap | 7635104 | 11455784 | 8255480 | 10553736 | 8969040 | 8428776 |
| XGo | 14015312 | 17237056 | 13474952 | 16067704 | 13152568 | 12853360 |
