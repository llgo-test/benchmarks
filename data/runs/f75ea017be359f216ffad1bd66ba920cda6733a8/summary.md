# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 17404760 | 14228176 | 16928816 | 13524536 | 13226144 |
| Dustin_humanize | 4999050 | 6675624 | 4969856 | 6113432 | 4055208 | 3983856 |
| Etcdctl | 25896967 | 29145672 | 26575120 | 28741400 | 27718384 | 27302848 |
| Gorm_schema | 9421675 | 9679216 | 8875240 | 9109848 | 8732056 | 6317792 |
| IXGo | 47404128 | 45768808 | 44908424 | 45730520 | 45218776 | 45043608 |
| K8s_workqueue | 10681827 | 15273256 | 13470720 | 14965152 | 14691504 | 10998872 |
| Toml | 7324966 | 8518024 | 7035032 | 7957496 | 6295096 | 6194656 |
| Uber_zap | 10025000 | 15673712 | 12378808 | 15283544 | 12903120 | 12154728 |
| XGo | 18662581 | 23621536 | 19721448 | 23416184 | 19213880 | 18830192 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12563336 | 9474928 | 11534760 | 9265912 | 9035944 |
| Dustin_humanize | 3711728 | 4590056 | 2942952 | 4119320 | 2777464 | 2720360 |
| Etcdctl | 20251432 | 21355848 | 18850184 | 20081816 | 19406512 | 19002728 |
| Gorm_schema | 7186360 | 6863184 | 6085224 | 6324280 | 6067128 | 4453632 |
| IXGo | 37601624 | 31244656 | 30411560 | 29219560 | 28944288 | 28796240 |
| K8s_workqueue | 8105040 | 11075120 | 9314400 | 10254080 | 10107768 | 7557160 |
| Toml | 5573864 | 6019272 | 4588344 | 5444888 | 4391816 | 4307264 |
| Uber_zap | 7635104 | 11316560 | 8104848 | 10461632 | 8877464 | 8328520 |
| XGo | 14015312 | 17108416 | 13336064 | 15979888 | 13060432 | 12755656 |
