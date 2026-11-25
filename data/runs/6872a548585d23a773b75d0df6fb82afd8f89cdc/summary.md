# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18523168 | 15254272 | 17306816 | 13851696 | 13558648 |
| Dustin_humanize | 4999050 | 7048800 | 5280480 | 6354728 | 4259112 | 4185584 |
| Etcdctl | 25896967 | 30504328 | 27893136 | 29139776 | 28092912 | 27681344 |
| Gorm_schema | 9421675 | 10131384 | 9317616 | 9355976 | 8970064 | 6509736 |
| IXGo | 47404128 | 47321544 | 46477144 | 45979240 | 45470400 | 45340664 |
| K8s_workqueue | 10681827 | 16352744 | 14508920 | 15327440 | 15049480 | 11315976 |
| Toml | 7324966 | 8890552 | 7381456 | 8163024 | 6471392 | 6369544 |
| Uber_zap | 10025000 | 16764984 | 13360592 | 15661776 | 13207680 | 12465688 |
| XGo | 18662581 | 25009552 | 20979816 | 23840656 | 19595328 | 19220520 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12846752 | 9682616 | 11800168 | 9468488 | 9247896 |
| Dustin_humanize | 3711728 | 4791704 | 3091240 | 4329336 | 2950696 | 2892888 |
| Etcdctl | 20251432 | 21725360 | 19187832 | 20371312 | 19688256 | 19291936 |
| Gorm_schema | 7186360 | 7081656 | 6296104 | 6553008 | 6290328 | 4631168 |
| IXGo | 37601624 | 31264168 | 30453808 | 29288080 | 29011016 | 28903960 |
| K8s_workqueue | 8105040 | 11391328 | 9596352 | 10509832 | 10358432 | 7752792 |
| Toml | 5573864 | 6203768 | 4754808 | 5636832 | 4552040 | 4468096 |
| Uber_zap | 7635104 | 11630512 | 8323592 | 10740952 | 9075392 | 8529432 |
| XGo | 14015312 | 17571936 | 13694784 | 16373136 | 13397224 | 13099744 |
