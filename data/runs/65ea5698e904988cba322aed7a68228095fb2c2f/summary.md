# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18150800 | 14980904 | 17315224 | 13928920 | 13626512 |
| Dustin_humanize | 4999050 | 6862120 | 5148248 | 6248704 | 4189312 | 4116472 |
| Etcdctl | 25896967 | 29964152 | 27406560 | 29067408 | 28038984 | 27622880 |
| Gorm_schema | 9421675 | 9882120 | 9082064 | 9210200 | 8830368 | 6423560 |
| IXGo | 47404128 | 46581184 | 45728416 | 45621976 | 45128736 | 44975176 |
| K8s_workqueue | 10681827 | 15999088 | 14201912 | 15346696 | 15075872 | 11407384 |
| Toml | 7324966 | 8706248 | 7226328 | 8072256 | 6394184 | 6292304 |
| Uber_zap | 10025000 | 16406208 | 13116040 | 15643976 | 13281776 | 12543304 |
| XGo | 18662581 | 24407848 | 20511728 | 23724008 | 19551968 | 19169552 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12670776 | 9595024 | 11635848 | 9362968 | 9140376 |
| Dustin_humanize | 3711728 | 4695944 | 3043456 | 4232456 | 2889280 | 2832616 |
| Etcdctl | 20251432 | 21480952 | 18991256 | 20147960 | 19470472 | 19073080 |
| Gorm_schema | 7186360 | 6959568 | 6186760 | 6424424 | 6164984 | 4554056 |
| IXGo | 37601624 | 31202664 | 30387528 | 28930816 | 28654736 | 28539720 |
| K8s_workqueue | 8105040 | 11212864 | 9460888 | 10349792 | 10200448 | 7660064 |
| Toml | 5573864 | 6122608 | 4696992 | 5554560 | 4476104 | 4392744 |
| Uber_zap | 7635104 | 11454912 | 8254592 | 10552752 | 8967992 | 8427744 |
| XGo | 14015312 | 17236160 | 13474072 | 16066656 | 13151576 | 12852360 |
