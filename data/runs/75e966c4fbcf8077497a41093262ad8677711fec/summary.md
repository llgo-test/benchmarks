# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 17390960 | 14243048 | 17170504 | 13575088 | 13436088 |
| Dustin_humanize | 4999050 | 6634104 | 4939168 | 6157520 | 4070960 | 4015512 |
| Etcdctl | 25896967 | 29036584 | 26512816 | 29054800 | 27941008 | 27663976 |
| Gorm_schema | 9421675 | 9613016 | 8822344 | 9187392 | 8786384 | 6375328 |
| IXGo | 47404128 | 45456024 | 44502776 | 46203408 | 45449656 | 45327896 |
| K8s_workqueue | 10681827 | 15252928 | 13481256 | 15157888 | 14830760 | 11182304 |
| Toml | 7324966 | 8465720 | 6984552 | 8059816 | 6320432 | 6250216 |
| Uber_zap | 10025000 | 15628256 | 12363688 | 15464264 | 12495336 | 12334000 |
| XGo | 18662581 | 23545616 | 19680376 | 23741504 | 19322520 | 19139760 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12616648 | 9562272 | 11681224 | 9304760 | 9179856 |
| Dustin_humanize | 3711728 | 4574960 | 2939648 | 4137472 | 2787576 | 2738848 |
| Etcdctl | 20251432 | 21380600 | 18924000 | 20257896 | 19531080 | 19230176 |
| Gorm_schema | 7186360 | 6844864 | 6082232 | 6361944 | 6089032 | 4483312 |
| IXGo | 37601624 | 31133872 | 30215696 | 29486800 | 29037888 | 28898968 |
| K8s_workqueue | 8105040 | 11129080 | 9402120 | 10388456 | 10209504 | 7694024 |
| Toml | 5573864 | 6003080 | 4577656 | 5506528 | 4393064 | 4330792 |
| Uber_zap | 7635104 | 11347344 | 8168952 | 10574704 | 8595976 | 8448088 |
| XGo | 14015312 | 17138568 | 13403608 | 16158168 | 13100560 | 12938784 |
