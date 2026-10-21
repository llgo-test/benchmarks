# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 17397760 | 14362312 | 17141072 | 13554752 | 13415224 |
| Dustin_humanize | 4999050 | 6635824 | 4947728 | 6145040 | 4072768 | 4017120 |
| Etcdctl | 25896967 | 29053248 | 27337368 | 29006744 | 27893904 | 27615968 |
| Gorm_schema | 9421675 | 9619328 | 8833784 | 9170472 | 8768056 | 6363064 |
| IXGo | 47404128 | 45485040 | 44534320 | 46155304 | 45403888 | 45280088 |
| K8s_workqueue | 10681827 | 15262536 | 14287816 | 15130704 | 14803336 | 11159680 |
| Toml | 7324966 | 8469016 | 6998400 | 8043512 | 6315472 | 6245288 |
| Uber_zap | 10025000 | 15636720 | 12590576 | 15436280 | 12471056 | 12309712 |
| XGo | 18662581 | 23563664 | 19806656 | 23702504 | 19288632 | 19108504 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12625248 | 9681224 | 11682528 | 9306320 | 9181464 |
| Dustin_humanize | 3711728 | 4577968 | 2949344 | 4138408 | 2795232 | 2746536 |
| Etcdctl | 20251432 | 21394224 | 19732488 | 20261512 | 19534064 | 19233056 |
| Gorm_schema | 7186360 | 6848688 | 6090544 | 6362304 | 6089512 | 4483136 |
| IXGo | 37601624 | 31150064 | 30231896 | 29495912 | 29046272 | 28907304 |
| K8s_workqueue | 8105040 | 11137008 | 10193184 | 10390520 | 10211760 | 7695840 |
| Toml | 5573864 | 6007168 | 4592168 | 5507520 | 4399008 | 4336832 |
| Uber_zap | 7635104 | 11355160 | 8389976 | 10576864 | 8598096 | 8450272 |
| XGo | 14015312 | 17153216 | 13525104 | 16167472 | 13110416 | 12948688 |
