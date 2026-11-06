# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 17375552 | 14202144 | 16814008 | 13447608 | 13156392 |
| Dustin_humanize | 4999050 | 6661024 | 4958472 | 6090584 | 4038880 | 3967808 |
| Etcdctl | 25896967 | 29119336 | 26549536 | 28672816 | 27652648 | 27238968 |
| Gorm_schema | 9421675 | 9661568 | 8859152 | 9072296 | 8695936 | 6287416 |
| IXGo | 47404128 | — | — | — | — | — |
| K8s_workqueue | 10681827 | 15249384 | 13447992 | 14902680 | 14633176 | 10949688 |
| Toml | 7324966 | 8502176 | 7021088 | 7932360 | 6242240 | 6142688 |
| Uber_zap | 10025000 | 15649888 | 12357016 | 15219408 | 12839720 | 12099160 |
| XGo | 18662581 | 23595432 | 19696632 | 23349152 | 19148688 | 18772552 |

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
