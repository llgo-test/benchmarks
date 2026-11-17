# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18460912 | 15208304 | 17233376 | 13806736 | 13513224 |
| Dustin_humanize | 4999050 | 6993240 | 5242680 | 6299512 | 4224216 | 4150624 |
| Etcdctl | 25896967 | 30435464 | 27826128 | 29033928 | 28008864 | 27597248 |
| Gorm_schema | 9421675 | 10071472 | 9262568 | 9283768 | 8905352 | 6468376 |
| IXGo | 47404128 | 47105144 | 46250736 | 45671312 | 45183952 | 45045296 |
| K8s_workqueue | 10681827 | 16293272 | 14453584 | 15257224 | 14983696 | 11272856 |
| Toml | 7324966 | 8835160 | 7342160 | 8108280 | 6436696 | 6335744 |
| Uber_zap | 10025000 | 16705344 | 13313816 | 15590472 | 13158568 | 12417104 |
| XGo | 18662581 | 24936152 | 20922256 | 23764552 | 19546600 | 19170248 |

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
