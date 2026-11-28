# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18507696 | 15227288 | 17289040 | 13824968 | 13534864 |
| Dustin_humanize | 4999050 | 6999000 | 5223592 | 6303880 | 4198808 | 4124664 |
| Etcdctl | 25896967 | 30529160 | 27915120 | 29145640 | 28100400 | 27693080 |
| Gorm_schema | 9421675 | 10097032 | 9281728 | 9324696 | 8941184 | 6467048 |
| IXGo | 47404128 | 47415592 | 46567840 | 46094152 | 45582752 | 45452664 |
| K8s_workqueue | 10681827 | 16321112 | 14475496 | 15294072 | 15018712 | 11283480 |
| Toml | 7324966 | 8846104 | 7331704 | 8120040 | 6427808 | 6325960 |
| Uber_zap | 10025000 | 16730080 | 13318168 | 15626752 | 13171864 | 12432528 |
| XGo | 18662581 | 25018184 | 20977504 | 23860784 | 19612864 | 19239080 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12804448 | 9628400 | 11740696 | 9402872 | 9183328 |
| Dustin_humanize | 3711728 | 4721424 | 3013280 | 4248696 | 2864456 | 2806264 |
| Etcdctl | 20251432 | 21725280 | 19183856 | 20319032 | 19638616 | 19243792 |
| Gorm_schema | 7186360 | 7025368 | 6237608 | 6487312 | 6225672 | 4557304 |
| IXGo | 37601624 | 31279096 | 30466152 | 29272344 | 28994840 | 28888728 |
| K8s_workqueue | 8105040 | 11342096 | 9544016 | 10441240 | 10290128 | 7683232 |
| Toml | 5573864 | 6139104 | 4685320 | 5561944 | 4477496 | 4393232 |
| Uber_zap | 7635104 | 11579328 | 8265704 | 10672680 | 9005368 | 8461208 |
| XGo | 14015312 | 17556280 | 13669592 | 16332112 | 13354384 | 13058016 |
