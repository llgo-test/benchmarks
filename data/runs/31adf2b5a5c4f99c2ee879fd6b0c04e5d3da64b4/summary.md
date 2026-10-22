# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 17400504 | 14365016 | 17144240 | 13556808 | 13417984 |
| Dustin_humanize | 4999050 | 6638192 | 4950288 | 6147768 | 4075360 | 4019200 |
| Etcdctl | 25896967 | 29055072 | 27339416 | 29008880 | 27896016 | 27618824 |
| Gorm_schema | 9421675 | 9621744 | 8835992 | 9172712 | 8771032 | 6365656 |
| IXGo | 47404128 | 45495008 | 44539544 | 46157816 | 45408872 | 45283840 |
| K8s_workqueue | 10681827 | 15265048 | 14290688 | 15133024 | 14806152 | 11162416 |
| Toml | 7324966 | 8471072 | 7000792 | 8045680 | 6318096 | 6247664 |
| Uber_zap | 10025000 | 15638896 | 12592712 | 15438712 | 12474016 | 12312424 |
| XGo | 18662581 | 23565960 | 19809312 | 23705440 | 19291656 | 19111016 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12627120 | 9683088 | 11684240 | 9308000 | 9183160 |
| Dustin_humanize | 3711728 | 4579776 | 2951360 | 4140152 | 2797048 | 2748320 |
| Etcdctl | 20251432 | 21396080 | 19734328 | 20263208 | 19535712 | 19234736 |
| Gorm_schema | 7186360 | 6850528 | 6092400 | 6364016 | 6091248 | 4484912 |
| IXGo | 37601624 | 31151952 | 30233736 | 29497576 | 29047920 | 28909000 |
| K8s_workqueue | 8105040 | 11138848 | 10195008 | 10392264 | 10213488 | 7697632 |
| Toml | 5573864 | 6008992 | 4594008 | 5509216 | 4400720 | 4338464 |
| Uber_zap | 7635104 | 11357008 | 8391768 | 10578624 | 8599824 | 8451936 |
| XGo | 14015312 | 17155072 | 13526944 | 16169168 | 13112224 | 12950432 |
