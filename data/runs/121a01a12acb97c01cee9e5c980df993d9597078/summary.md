# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18460912 | 15208216 | 17233616 | 13806624 | 13513360 |
| Dustin_humanize | 4999050 | 6993240 | 5242680 | 6299512 | 4224216 | 4150624 |
| Etcdctl | 25896967 | 30435608 | 27826472 | 29033936 | 28009024 | 27597312 |
| Gorm_schema | 9421675 | 10071480 | 9262576 | 9283768 | 8905352 | 6468376 |
| IXGo | 47404128 | 47103264 | 46249440 | 45671448 | 45181864 | 45048576 |
| K8s_workqueue | 10681827 | 16292848 | 14453568 | 15257216 | 14983816 | 11272736 |
| Toml | 7324966 | 8835072 | 7341808 | 8108224 | 6436712 | 6335448 |
| Uber_zap | 10025000 | 16705432 | 13313456 | 15590480 | 13158736 | 12417248 |
| XGo | 18662581 | 24936376 | 20922280 | 23764792 | 19546560 | 19170504 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12808272 | 9657560 | 11746584 | 9436176 | 9216136 |
| Dustin_humanize | 3711728 | 4755544 | 3069688 | 4286768 | 2926680 | 2869080 |
| Etcdctl | 20251432 | 21687144 | 19152936 | 20299696 | 19627256 | 19230520 |
| Gorm_schema | 7186360 | 7044520 | 6263416 | 6503968 | 6245856 | 4604896 |
| IXGo | 37601624 | 31298448 | 30489000 | 29220016 | 28946424 | 28838464 |
| K8s_workqueue | 8105040 | 11352800 | 9562408 | 10454776 | 10306120 | 7721040 |
| Toml | 5573864 | 6167360 | 4732688 | 5594544 | 4526096 | 4442728 |
| Uber_zap | 7635104 | 11592184 | 8296720 | 10687096 | 9038264 | 8493528 |
| XGo | 14015312 | 17528832 | 13665264 | 16310136 | 13353720 | 13057208 |
