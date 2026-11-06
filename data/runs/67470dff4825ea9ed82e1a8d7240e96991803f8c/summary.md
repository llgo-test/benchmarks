# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 17405344 | 14227792 | 16928480 | 13524544 | 13226048 |
| Dustin_humanize | 4999050 | 6675624 | 4969856 | 6113424 | 4055200 | 3983856 |
| Etcdctl | 25896967 | 29145496 | 26575024 | 28741400 | 27718912 | 27302896 |
| Gorm_schema | 9421675 | 9679312 | 8875248 | 9109848 | 8732056 | 6317792 |
| IXGo | 47404128 | 45766840 | 44906824 | 45730448 | 45217760 | 45046808 |
| K8s_workqueue | 10681827 | 15273056 | 13470608 | 14965000 | 14691480 | 10998912 |
| Toml | 7324966 | 8517968 | 7035032 | 7957480 | 6295040 | 6194552 |
| Uber_zap | 10025000 | 15673656 | 12378816 | 15283464 | 12902960 | 12154776 |
| XGo | 18662581 | 23621416 | 19721600 | 23415880 | 19213672 | 18830184 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12563336 | 9474928 | 11534760 | 9265912 | 9035944 |
| Dustin_humanize | 3711728 | 4590056 | 2942952 | 4119320 | 2777464 | 2720360 |
| Etcdctl | 20251432 | 21355848 | 18850184 | 20081816 | 19406512 | 19002728 |
| Gorm_schema | 7186360 | 6863168 | 6085224 | 6324280 | 6067128 | 4453632 |
| IXGo | 37601624 | 31244656 | 30411560 | 29219560 | 28944288 | 28796240 |
| K8s_workqueue | 8105040 | 11075120 | 9314416 | 10254080 | 10107768 | 7557160 |
| Toml | 5573864 | 6019272 | 4588344 | 5444888 | 4391816 | 4307264 |
| Uber_zap | 7635104 | 11316560 | 8104832 | 10461632 | 8877464 | 8328520 |
| XGo | 14015312 | 17108416 | 13336064 | 15979888 | 13060432 | 12755656 |
