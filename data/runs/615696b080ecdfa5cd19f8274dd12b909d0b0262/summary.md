# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18460912 | 15208256 | 17233880 | 13807072 | 13513272 |
| Dustin_humanize | 4999050 | 6993232 | 5242680 | 6299512 | 4224216 | 4150624 |
| Etcdctl | 25896967 | 30435632 | 27826272 | 29034208 | 28009032 | 27597136 |
| Gorm_schema | 9421675 | 10071480 | 9262576 | 9283768 | 8905352 | 6468384 |
| IXGo | 47404128 | 47104336 | 46251912 | 45670896 | 45186832 | 45048616 |
| K8s_workqueue | 10681827 | 16292928 | 14453272 | 15257072 | 14983480 | 11272896 |
| Toml | 7324966 | 8835080 | 7341968 | 8108280 | 6436720 | 6335632 |
| Uber_zap | 10025000 | 16705216 | 13313656 | 15590552 | 13158952 | 12417264 |
| XGo | 18662581 | 24936480 | 20922512 | 23764944 | 19546528 | 19170712 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12808288 | 9657560 | 11746584 | 9436176 | 9216136 |
| Dustin_humanize | 3711728 | 4755544 | 3069688 | 4286768 | 2926680 | 2869080 |
| Etcdctl | 20251432 | 21687144 | 19152936 | 20299696 | 19627256 | 19230520 |
| Gorm_schema | 7186360 | 7044520 | 6263416 | 6503968 | 6245856 | 4604896 |
| IXGo | 37601624 | 31298448 | 30489000 | 29220016 | 28946424 | 28838464 |
| K8s_workqueue | 8105040 | 11352816 | 9562408 | 10454776 | 10306136 | 7721040 |
| Toml | 5573864 | 6167360 | 4732688 | 5594544 | 4526096 | 4442728 |
| Uber_zap | 7635104 | 11592184 | 8296720 | 10687096 | 9038264 | 8493528 |
| XGo | 14015312 | 17528832 | 13665264 | 16310136 | 13353720 | 13057208 |
