# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 17375248 | 14202280 | 16814288 | 13447944 | 13156040 |
| Dustin_humanize | 4999050 | 6661024 | 4958472 | 6090592 | 4038880 | 3967784 |
| Etcdctl | 25896967 | 29119432 | 26549464 | 28672512 | 27652360 | 27238320 |
| Gorm_schema | 9421675 | 9661560 | 8859160 | 9072304 | 8695936 | 6287416 |
| IXGo | 47404128 | — | — | — | — | — |
| K8s_workqueue | 10681827 | 15249424 | 13448000 | 14902728 | 14633240 | 10949496 |
| Toml | 7324966 | 8502160 | 7021184 | 7932184 | 6242336 | 6142648 |
| Uber_zap | 10025000 | 15649744 | 12357160 | 15219328 | 12839544 | 12098984 |
| XGo | 18662581 | 23595264 | 19696448 | 23349288 | 19148824 | 18772704 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12547440 | 9463328 | 11437416 | 9203640 | 8979840 |
| Dustin_humanize | 3711728 | 4584872 | 2940400 | 4100944 | 2764744 | 2707952 |
| Etcdctl | 20251432 | 21344672 | 18840104 | 20021872 | 19346968 | 18944272 |
| Gorm_schema | 7186360 | 6856496 | 6079360 | 6298728 | 6041568 | 4431408 |
| IXGo | 37601624 | — | — | — | — | — |
| K8s_workqueue | 8105040 | 11063720 | 9304688 | 10199952 | 10053632 | 7510632 |
| Toml | 5573864 | 6013384 | 4584904 | 5422232 | 4343912 | 4259544 |
| Uber_zap | 7635104 | 11304976 | 8095920 | 10406088 | 8821640 | 8279024 |
| XGo | 14015312 | 17096904 | 13326120 | 15924040 | 13003616 | 12704808 |

10 paired size measurements are missing; excluded from DWARF comparisons.
