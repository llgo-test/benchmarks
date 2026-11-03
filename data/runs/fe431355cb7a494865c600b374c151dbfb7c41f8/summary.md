# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 17340560 | 14197872 | 16875352 | 13334280 | 13197080 |
| Dustin_humanize | 4999050 | 6640472 | 4949128 | 6083128 | 4019392 | 3964304 |
| Etcdctl | 25896967 | 29030704 | 26519912 | 28647600 | 27544040 | 27267696 |
| Gorm_schema | 9421675 | 9637448 | 8849336 | 9078496 | 8679984 | 6296624 |
| IXGo | 47404128 | 45449224 | 44500664 | 45607112 | 44848360 | 44736040 |
| K8s_workqueue | 10681827 | 15207008 | 13436664 | 14907216 | 14585256 | 10970264 |
| Toml | 7324966 | 8483152 | 7006896 | 7959072 | 6238128 | 6168288 |
| Uber_zap | 10025000 | 15584552 | 12325496 | 15205704 | 12263816 | 12101736 |
| XGo | 18662581 | 23531664 | 19669312 | 23347896 | 18965928 | 18786112 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12492248 | 9442464 | 11482768 | 9130968 | 9006448 |
| Dustin_humanize | 3711728 | 4553096 | 2921584 | 4090512 | 2750912 | 2702280 |
| Etcdctl | 20251432 | 21237608 | 18793688 | 19993904 | 19266768 | 18965936 |
| Gorm_schema | 7186360 | 6819808 | 6058992 | 6294720 | 6022416 | 4434240 |
| IXGo | 37601624 | 30907432 | 30000080 | 29072832 | 28621584 | 28491968 |
| K8s_workqueue | 8105040 | 11004536 | 9279024 | 10200512 | 10021288 | 7531144 |
| Toml | 5573864 | 5979992 | 4559256 | 5445816 | 4343872 | 4281824 |
| Uber_zap | 7635104 | 11222176 | 8049752 | 10386136 | 8424624 | 8277016 |
| XGo | 14015312 | 17013608 | 13282448 | 15910480 | 12873712 | 12712184 |
