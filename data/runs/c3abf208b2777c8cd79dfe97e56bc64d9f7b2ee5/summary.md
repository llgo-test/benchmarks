# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18152344 | 14982232 | 17316920 | 13930952 | 13628608 |
| Dustin_humanize | 4999050 | 6863264 | 5149608 | 6250240 | 4191184 | 4118568 |
| Etcdctl | 25896967 | 29965360 | 27407768 | 29070136 | 28039784 | 27626176 |
| Gorm_schema | 9421675 | 9883272 | 9083232 | 9212272 | 8831680 | 6425152 |
| IXGo | 47404128 | 46582888 | 45728712 | 45625184 | 45129376 | 44977752 |
| K8s_workqueue | 10681827 | 16000472 | 14203312 | 15348512 | 15077792 | 11409248 |
| Toml | 7324966 | 8707616 | 7227784 | 8073448 | 6396056 | 6294248 |
| Uber_zap | 10025000 | 16407336 | 13117248 | 15645864 | 13283400 | 12545256 |
| XGo | 18662581 | 24409584 | 20512712 | 23725544 | 19554336 | 19170504 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12671648 | 9595920 | 11636824 | 9364000 | 9141432 |
| Dustin_humanize | 3711728 | 4696832 | 3044344 | 4233416 | 2890248 | 2833632 |
| Etcdctl | 20251432 | 21481840 | 18992128 | 20148984 | 19471536 | 19074184 |
| Gorm_schema | 7186360 | 6960144 | 6187336 | 6425504 | 6166112 | 4555168 |
| IXGo | 37601624 | 31203264 | 30388096 | 28931912 | 28655848 | 28540880 |
| K8s_workqueue | 8105040 | 11213768 | 9461744 | 10350752 | 10201448 | 7661064 |
| Toml | 5573864 | 6123488 | 4697880 | 5555608 | 4477152 | 4393824 |
| Uber_zap | 7635104 | 11455800 | 8255480 | 10553736 | 8969040 | 8428776 |
| XGo | 14015312 | 17237056 | 13474952 | 16067704 | 13152568 | 12853360 |
