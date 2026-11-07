# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18032472 | 14865400 | 17174104 | 13797592 | 13496752 |
| Dustin_humanize | 4999050 | 6711600 | 5005376 | 6116232 | 4061368 | 3989888 |
| Etcdctl | 25896967 | 29840032 | 27280640 | 29055176 | 28035616 | 27617360 |
| Gorm_schema | 9421675 | 9738832 | 8941672 | 9106392 | 8729840 | 6316664 |
| IXGo | 47404128 | 46593696 | 45744832 | 45740752 | 45231656 | 45050744 |
| K8s_workqueue | 10681827 | 15857056 | 14058216 | 15250784 | 14982528 | 11282048 |
| Toml | 7324966 | 8556384 | 7079568 | 7960992 | 6268120 | 6167208 |
| Uber_zap | 10025000 | 16260480 | 12967296 | 15564040 | 13177528 | 12430688 |
| XGo | 18662581 | 24268216 | 20370896 | 23721112 | 19510544 | 19133480 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12569288 | 9496208 | 11467992 | 9231744 | 9006576 |
| Dustin_humanize | 3711728 | 4560040 | 2913936 | 4100560 | 2764048 | 2707424 |
| Etcdctl | 20251432 | 21369600 | 18878400 | 20063600 | 19389088 | 18985640 |
| Gorm_schema | 7186360 | 6829448 | 6058608 | 6299176 | 6041296 | 4431680 |
| IXGo | 37601624 | 31283592 | 30468352 | 29038920 | 28764304 | 28607392 |
| K8s_workqueue | 8105040 | 11083064 | 9330480 | 10229176 | 10083712 | 7538792 |
| Toml | 5573864 | 5987296 | 4565000 | 5422736 | 4343488 | 4259112 |
| Uber_zap | 7635104 | 11322968 | 8118696 | 10437464 | 8852088 | 8308000 |
| XGo | 14015312 | 17112416 | 13350440 | 15953640 | 13032304 | 12732888 |
