# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18614384 | 15327296 | 17419280 | 13945512 | 13651504 |
| Dustin_humanize | 4999050 | 7093640 | 5314264 | 6410648 | 4298664 | 4223880 |
| Etcdctl | 25896967 | 30658280 | 28037800 | 29309912 | 28261224 | 27850752 |
| Gorm_schema | 9421675 | 10195480 | 9378608 | 9438776 | 9054240 | 6571208 |
| IXGo | 47404128 | 47500224 | 46649880 | 46211336 | 45703128 | 45568944 |
| K8s_workqueue | 10681827 | 16440200 | 14589504 | 15436472 | 15161880 | 11405312 |
| Toml | 7324966 | 8941784 | 7425408 | 8230552 | 6533632 | 6430408 |
| Uber_zap | 10025000 | 16849152 | 13427568 | 15769488 | 13306424 | 12558920 |
| XGo | 18662581 | 25138760 | 21092400 | 24004504 | 19745192 | 19371920 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12924232 | 9742544 | 11873720 | 9529880 | 9308744 |
| Dustin_humanize | 3711728 | 4826432 | 3115120 | 4362728 | 2973240 | 2914936 |
| Etcdctl | 20251432 | 21856088 | 19308888 | 20470320 | 19787576 | 19390520 |
| Gorm_schema | 7186360 | 7132816 | 6344432 | 6604960 | 6343280 | 4669112 |
| IXGo | 37601624 | 31416592 | 30603384 | 29427736 | 29150528 | 29043504 |
| K8s_workqueue | 8105040 | 11464904 | 9663280 | 10578992 | 10427888 | 7807944 |
| Toml | 5573864 | 6245128 | 4789224 | 5677272 | 4589480 | 4505008 |
| Uber_zap | 7635104 | 11700488 | 8377096 | 10808144 | 9135776 | 8585936 |
| XGo | 14015312 | 17678952 | 13786552 | 16469752 | 13485904 | 13188488 |
