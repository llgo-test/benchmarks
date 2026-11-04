# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 17343736 | 14200752 | 16879360 | 13337992 | 13198488 |
| Dustin_humanize | 4999050 | 6644640 | 4953512 | 6087536 | 4023768 | 3968488 |
| Etcdctl | 25896967 | 29033584 | 26522664 | 28651776 | 27547656 | 27271120 |
| Gorm_schema | 9421675 | 9641792 | 8853368 | 9082824 | 8684280 | 6301232 |
| IXGo | 47404128 | 45442848 | 44498256 | 45608072 | 44851800 | 44735840 |
| K8s_workqueue | 10681827 | 15210008 | 13439600 | 14911400 | 14588336 | 10974664 |
| Toml | 7324966 | 8486600 | 7010656 | 7963152 | 6242504 | 6172696 |
| Uber_zap | 10025000 | 15587528 | 12328672 | 15209536 | 12267592 | 12106168 |
| XGo | 18662581 | 23535928 | 19673080 | 23351824 | 18969496 | 18789744 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12494720 | 9444984 | 11485280 | 9133640 | 9009168 |
| Dustin_humanize | 3711728 | 4555864 | 2924352 | 4093320 | 2753824 | 2705128 |
| Etcdctl | 20251432 | 21239840 | 18795952 | 19996400 | 19269448 | 18968528 |
| Gorm_schema | 7186360 | 6822680 | 6061864 | 6297640 | 6025392 | 4437152 |
| IXGo | 37601624 | 30909288 | 30001936 | 29074984 | 28623808 | 28494104 |
| K8s_workqueue | 8105040 | 11006992 | 9281512 | 10203096 | 10023928 | 7533784 |
| Toml | 5573864 | 5982464 | 4562104 | 5448312 | 4346864 | 4284768 |
| Uber_zap | 7635104 | 11224616 | 8052224 | 10388624 | 8427280 | 8279648 |
| XGo | 14015312 | 17016160 | 13284984 | 15912944 | 12876192 | 12714760 |
