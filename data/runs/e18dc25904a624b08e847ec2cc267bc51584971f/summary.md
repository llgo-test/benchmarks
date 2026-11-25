# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18530152 | 15261208 | 17297056 | 13845920 | 13551112 |
| Dustin_humanize | 4999050 | 7056280 | 5288448 | 6354384 | 4260016 | 4186192 |
| Etcdctl | 25896967 | 30511456 | 27900576 | 29124688 | 28077456 | 27667088 |
| Gorm_schema | 9421675 | 10138032 | 9324880 | 9354592 | 8969280 | 6509816 |
| IXGo | 47404128 | 47327696 | 46477640 | 45964040 | 45458672 | 45324520 |
| K8s_workqueue | 10681827 | 16359752 | 14515744 | 15318800 | 15042624 | 11310536 |
| Toml | 7324966 | 8898360 | 7388800 | 8161648 | 6471408 | 6369016 |
| Uber_zap | 10025000 | 16771672 | 13367600 | 15654024 | 13200808 | 12458256 |
| XGo | 18662581 | 25017168 | 20987416 | 23829448 | 19587384 | 19211888 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12850112 | 9685992 | 11798480 | 9467200 | 9246312 |
| Dustin_humanize | 3711728 | 4795064 | 3094632 | 4329984 | 2951904 | 2893920 |
| Etcdctl | 20251432 | 21728688 | 19191176 | 20366472 | 19683568 | 19286936 |
| Gorm_schema | 7186360 | 7085000 | 6299464 | 6553280 | 6290768 | 4631880 |
| IXGo | 37601624 | 31267584 | 30457240 | 29282152 | 29005344 | 28898784 |
| K8s_workqueue | 8105040 | 11394672 | 9599680 | 10508096 | 10356760 | 7751544 |
| Toml | 5573864 | 6207152 | 4758168 | 5637136 | 4552848 | 4468680 |
| Uber_zap | 7635104 | 11633888 | 8326920 | 10739104 | 9073824 | 8527584 |
| XGo | 14015312 | 17575280 | 13698192 | 16370328 | 13394912 | 13097240 |
