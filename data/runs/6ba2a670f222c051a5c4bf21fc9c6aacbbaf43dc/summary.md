# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18617896 | 15331272 | 17419456 | 13945640 | 13651536 |
| Dustin_humanize | 4999050 | 7096728 | 5317520 | 6411160 | 4299000 | 4224600 |
| Etcdctl | 25896967 | 30660360 | 28040432 | 29310192 | 28262032 | 27851672 |
| Gorm_schema | 9421675 | 10198472 | 9381632 | 9439320 | 9054856 | 6571584 |
| IXGo | 47404128 | 47503920 | 46653248 | 46216080 | 45705272 | 45566880 |
| K8s_workqueue | 10681827 | 16443416 | 14592944 | 15436816 | 15162400 | 11405696 |
| Toml | 7324966 | 8944944 | 7428600 | 8231160 | 6533840 | 6430704 |
| Uber_zap | 10025000 | 16851960 | 13430704 | 15770112 | 13306768 | 12559200 |
| XGo | 18662581 | 25142096 | 21095456 | 24005216 | 19746232 | 19371960 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12926144 | 9744512 | 11873832 | 9529992 | 9308856 |
| Dustin_humanize | 3711728 | 4828432 | 3117088 | 4362840 | 2973352 | 2915048 |
| Etcdctl | 20251432 | 21858008 | 19310848 | 20470432 | 19787704 | 19390632 |
| Gorm_schema | 7186360 | 7134808 | 6346424 | 6605072 | 6343392 | 4669224 |
| IXGo | 37601624 | 31418584 | 30605328 | 29427896 | 29150640 | 29043616 |
| K8s_workqueue | 8105040 | 11466848 | 9665264 | 10579056 | 10428000 | 7808056 |
| Toml | 5573864 | 6247080 | 4791152 | 5677384 | 4589592 | 4505120 |
| Uber_zap | 7635104 | 11702448 | 8379072 | 10808256 | 9135920 | 8586048 |
| XGo | 14015312 | 17680888 | 13788512 | 16469864 | 13486016 | 13188600 |
