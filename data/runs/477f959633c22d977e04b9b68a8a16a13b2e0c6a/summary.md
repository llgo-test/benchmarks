# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 17397584 | 14362480 | 17141144 | 13554880 | 13415280 |
| Dustin_humanize | 4999050 | 6635824 | 4947720 | 6145040 | 4072768 | 4017112 |
| Etcdctl | 25896967 | 29053248 | 27337640 | 29007224 | 27894152 | 27615712 |
| Gorm_schema | 9421675 | 9619336 | 8833784 | 9170472 | 8768064 | 6363064 |
| IXGo | 47404128 | 45484296 | 44531816 | 46156840 | 45403184 | 45279920 |
| K8s_workqueue | 10681827 | 15262832 | 14287848 | 15130440 | 14803368 | 11159784 |
| Toml | 7324966 | 8469112 | 6998432 | 8043512 | 6315424 | 6245224 |
| Uber_zap | 10025000 | 15636680 | 12590400 | 15436256 | 12471024 | 12310072 |
| XGo | 18662581 | 23563704 | 19806664 | 23702440 | 19288648 | 19108696 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12625248 | 9681224 | 11682528 | 9306320 | 9181464 |
| Dustin_humanize | 3711728 | 4577968 | 2949344 | 4138408 | 2795232 | 2746536 |
| Etcdctl | 20251432 | 21394224 | 19732472 | 20261512 | 19534064 | 19233056 |
| Gorm_schema | 7186360 | 6848688 | 6090544 | 6362304 | 6089512 | 4483136 |
| IXGo | 37601624 | 31150064 | 30231896 | 29495912 | 29046272 | 28907304 |
| K8s_workqueue | 8105040 | 11137024 | 10193184 | 10390520 | 10211760 | 7695840 |
| Toml | 5573864 | 6007168 | 4592168 | 5507520 | 4399008 | 4336832 |
| Uber_zap | 7635104 | 11355160 | 8389976 | 10576864 | 8598096 | 8450272 |
| XGo | 14015312 | 17153216 | 13525104 | 16167472 | 13110416 | 12948688 |
