# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 17391216 | 14243304 | 17166128 | 13571184 | 13432504 |
| Dustin_humanize | 4999050 | 6634096 | 4939192 | 6157528 | 4070960 | 4015512 |
| Etcdctl | 25896967 | 29036032 | 26512640 | 29053384 | 27940640 | 27663704 |
| Gorm_schema | 9421675 | 9613000 | 8822320 | 9187392 | 8786376 | 6375328 |
| IXGo | 47404128 | 45457688 | 44498272 | 46205304 | 45450488 | 45325600 |
| K8s_workqueue | 10681827 | 15252720 | 13481320 | 15157944 | 14830784 | 11182200 |
| Toml | 7324966 | 8465592 | 6984128 | 8060064 | 6320192 | 6250200 |
| Uber_zap | 10025000 | 15628032 | 12363520 | 15464136 | 12495264 | 12334064 |
| XGo | 18662581 | 23545320 | 19680104 | 23741592 | 19322632 | 19139576 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12616664 | 9562296 | 11679336 | 9302792 | 9177960 |
| Dustin_humanize | 3711728 | 4574960 | 2939648 | 4137472 | 2787576 | 2738848 |
| Etcdctl | 20251432 | 21380408 | 18924000 | 20257880 | 19530984 | 19230112 |
| Gorm_schema | 7186360 | 6844864 | 6082232 | 6361944 | 6089032 | 4483312 |
| IXGo | 37601624 | 31133520 | 30215360 | 29486800 | 29037872 | 28898952 |
| K8s_workqueue | 8105040 | 11129080 | 9402120 | 10388456 | 10209504 | 7694024 |
| Toml | 5573864 | 6003080 | 4577656 | 5506528 | 4393064 | 4330792 |
| Uber_zap | 7635104 | 11347344 | 8168952 | 10574704 | 8595976 | 8448088 |
| XGo | 14015312 | 17138568 | 13403592 | 16158168 | 13100560 | 12938784 |
