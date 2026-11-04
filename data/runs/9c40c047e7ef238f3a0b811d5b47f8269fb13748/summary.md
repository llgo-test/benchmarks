# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 17343632 | 14200880 | 16879488 | 13338240 | 13198384 |
| Dustin_humanize | 4999050 | 6644648 | 4953512 | 6087544 | 4023768 | 3968488 |
| Etcdctl | 25896967 | 29033840 | 26522888 | 28651936 | 27547320 | 27270912 |
| Gorm_schema | 9421675 | 9641792 | 8853368 | 9082816 | 8684288 | 6301232 |
| IXGo | 47404128 | 45442736 | 44499344 | 45605848 | 44850824 | 44735304 |
| K8s_workqueue | 10681827 | 15210216 | 13439448 | 14911568 | 14588464 | 10974520 |
| Toml | 7324966 | 8486520 | 7010568 | 7963168 | 6242464 | 6172688 |
| Uber_zap | 10025000 | 15587776 | 12328832 | 15209480 | 12267800 | 12106024 |
| XGo | 18662581 | 23535872 | 19673312 | 23351912 | 18969552 | 18789640 |

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
