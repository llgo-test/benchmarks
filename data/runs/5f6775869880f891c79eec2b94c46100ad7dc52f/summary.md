# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18614424 | 15327520 | 17419272 | 13945640 | 13651520 |
| Dustin_humanize | 4999050 | 7093640 | 5314264 | 6410648 | 4298664 | 4223856 |
| Etcdctl | 25896967 | 30657968 | 28037712 | 29310416 | 28261480 | 27850872 |
| Gorm_schema | 9421675 | 10195480 | 9378608 | 9438768 | 9054232 | 6571208 |
| IXGo | 47404128 | 47502160 | 46649816 | 46211336 | 45704328 | 45566256 |
| K8s_workqueue | 10681827 | 16440272 | 14589552 | 15436640 | 15161968 | 11405320 |
| Toml | 7324966 | 8941704 | 7425456 | 8230448 | 6533600 | 6430472 |
| Uber_zap | 10025000 | 16848968 | 13427800 | 15769712 | 13306480 | 12559168 |
| XGo | 18662581 | 25138672 | 21092616 | 24004544 | 19745368 | 19371560 |

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
