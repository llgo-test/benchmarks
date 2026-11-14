# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18157864 | 14984976 | 17322632 | 13932360 | 13630160 |
| Dustin_humanize | 4999050 | 6868888 | 5152800 | 6255760 | 4193008 | 4120256 |
| Etcdctl | 25896967 | 29971664 | 27412688 | 29075336 | 28045488 | 27631944 |
| Gorm_schema | 9421675 | 9888872 | 9088112 | 9217664 | 8837360 | 6427312 |
| IXGo | 47404128 | 46590152 | 45738320 | 45630456 | 45136304 | 44985040 |
| K8s_workqueue | 10681827 | 16006600 | 14208504 | 15353736 | 15083352 | 11411120 |
| Toml | 7324966 | 8713504 | 7230856 | 8079288 | 6398096 | 6296600 |
| Uber_zap | 10025000 | 16413352 | 13120328 | 15651600 | 13285496 | 12547136 |
| XGo | 18662581 | 24414976 | 20516200 | 23730688 | 19556944 | 19172552 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12675600 | 9597576 | 11640512 | 9365232 | 9142608 |
| Dustin_humanize | 3711728 | 4700704 | 3045976 | 4237120 | 2891400 | 2834864 |
| Etcdctl | 20251432 | 21485728 | 18995392 | 20152752 | 19475000 | 19077640 |
| Gorm_schema | 7186360 | 6964072 | 6190752 | 6429240 | 6169568 | 4556384 |
| IXGo | 37601624 | 31207136 | 30391552 | 28935680 | 28659520 | 28544552 |
| K8s_workqueue | 8105040 | 11217672 | 9465040 | 10354456 | 10205136 | 7662296 |
| Toml | 5573864 | 6127352 | 4699488 | 5559328 | 4478352 | 4395024 |
| Uber_zap | 7635104 | 11459768 | 8257104 | 10557424 | 8970256 | 8430024 |
| XGo | 14015312 | 17240936 | 13476592 | 16071552 | 13153968 | 12854720 |
