# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18146688 | 14978720 | 17312656 | 13929016 | 13626296 |
| Dustin_humanize | 4999050 | 6856768 | 5145256 | 6244632 | 4187296 | 4114624 |
| Etcdctl | 25896967 | 29967752 | 27409688 | 29080976 | 28042912 | 27627664 |
| Gorm_schema | 9421675 | 9877080 | 9078032 | 9206944 | 8826840 | 6423232 |
| IXGo | 47404128 | 46585856 | 45723160 | 45625000 | 45125344 | 44976976 |
| K8s_workqueue | 10681827 | 15995880 | 14198536 | 15344312 | 15074784 | 11406784 |
| Toml | 7324966 | 8701560 | 7224008 | 8067528 | 6393096 | 6291288 |
| Uber_zap | 10025000 | 16403712 | 13115456 | 15643072 | 13282464 | 12544288 |
| XGo | 18662581 | 24404160 | 20510104 | 23720152 | 19552208 | 19167912 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12668408 | 9594952 | 11633624 | 9362552 | 9139944 |
| Dustin_humanize | 3711728 | 4692592 | 3042112 | 4229080 | 2887992 | 2831400 |
| Etcdctl | 20251432 | 21485936 | 18995920 | 20155592 | 19472576 | 19074832 |
| Gorm_schema | 7186360 | 6956784 | 6184208 | 6421712 | 6162000 | 4553240 |
| IXGo | 37601624 | 31200448 | 30385464 | 28928800 | 28652560 | 28537560 |
| K8s_workqueue | 8105040 | 11210536 | 9458984 | 10348000 | 10198664 | 7659728 |
| Toml | 5573864 | 6119216 | 4695928 | 5551328 | 4475128 | 4391784 |
| Uber_zap | 7635104 | 11453768 | 8255616 | 10551688 | 8968152 | 8427824 |
| XGo | 14015312 | 17233608 | 13473576 | 16064168 | 13150968 | 12851704 |
