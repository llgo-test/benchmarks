# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18146224 | 14978552 | 17311336 | 13927944 | 13625232 |
| Dustin_humanize | 4999050 | 6856992 | 5146264 | 6244080 | 4188376 | 4115304 |
| Etcdctl | 25896967 | 29959688 | 27402440 | 29063440 | 28034696 | 27619872 |
| Gorm_schema | 9421675 | 9877640 | 9078296 | 9206216 | 8826392 | 6422688 |
| IXGo | 47404128 | 46582072 | 45725128 | 45619312 | 45122824 | 44972296 |
| K8s_workqueue | 10681827 | 15994856 | 14198256 | 15342200 | 15072040 | 11406272 |
| Toml | 7324966 | 8701872 | 7224432 | 8067456 | 6393280 | 6291376 |
| Uber_zap | 10025000 | 16401592 | 13114496 | 15639720 | 13280928 | 12542328 |
| XGo | 18662581 | 24403264 | 20509856 | 23719288 | 19551256 | 19167552 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12667696 | 9594352 | 11632344 | 9361992 | 9139352 |
| Dustin_humanize | 3711728 | 4692872 | 3042816 | 4229000 | 2888224 | 2831624 |
| Etcdctl | 20251432 | 21477792 | 18988768 | 20144584 | 19467136 | 19069752 |
| Gorm_schema | 7186360 | 6956472 | 6184040 | 6421008 | 6161680 | 4553048 |
| IXGo | 37601624 | 31199608 | 30384848 | 28927376 | 28651152 | 28536216 |
| K8s_workqueue | 8105040 | 11209760 | 9458416 | 10346288 | 10196984 | 7658992 |
| Toml | 5573864 | 6119448 | 4696352 | 5551184 | 4475112 | 4391768 |
| Uber_zap | 7635104 | 11451816 | 8253904 | 10549304 | 8967032 | 8426688 |
| XGo | 14015312 | 17233064 | 13473400 | 16063288 | 13150648 | 12851384 |
