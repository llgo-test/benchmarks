# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 17397520 | 14362400 | 17141376 | 13554776 | 13415288 |
| Dustin_humanize | 4999050 | 6635832 | 4947720 | 6145040 | 4072768 | 4017104 |
| Etcdctl | 25896967 | 29053392 | 27337400 | 29006840 | 27893696 | 27615896 |
| Gorm_schema | 9421675 | 9619336 | 8833792 | 9170472 | 8768064 | 6363064 |
| IXGo | 47404128 | 45485616 | 44530704 | 46153360 | 45405424 | 45281464 |
| K8s_workqueue | 10681827 | 15262856 | 14287920 | 15130632 | 14803552 | 11159720 |
| Toml | 7324966 | 8469056 | 6998448 | 8043512 | 6315400 | 6245280 |
| Uber_zap | 10025000 | 15636384 | 12590424 | 15436440 | 12471232 | 12309824 |
| XGo | 18662581 | 23563416 | 19806648 | 23702696 | 19288864 | 19108536 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12625248 | 9681224 | 11682528 | 9306320 | 9181464 |
| Dustin_humanize | 3711728 | 4577968 | 2949344 | 4138408 | 2795232 | 2746536 |
| Etcdctl | 20251432 | 21394224 | 19732488 | 20261512 | 19534064 | 19233056 |
| Gorm_schema | 7186360 | 6848688 | 6090544 | 6362304 | 6089512 | 4483136 |
| IXGo | 37601624 | 31150064 | 30231896 | 29495912 | 29046272 | 28907304 |
| K8s_workqueue | 8105040 | 11137024 | 10193184 | 10390520 | 10211760 | 7695840 |
| Toml | 5573864 | 6007168 | 4592168 | 5507520 | 4399008 | 4336832 |
| Uber_zap | 7635104 | 11355160 | 8389976 | 10576864 | 8598096 | 8450272 |
| XGo | 14015312 | 17153216 | 13525104 | 16167472 | 13110416 | 12948688 |
