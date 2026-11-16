# LLGo binary-size CI

Each configuration is built once with `-ldflags='-s=false -w=false'`. The second size comes from `llvm-strip --strip-debug` on a copy. DWARF presence/absence is checked; ordinary symbol tables are preserved. All values are complete ELF file sizes in bytes.

## With DWARF (verified)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635476 | 18292560 | 15083768 | 17074912 | 13684048 | 13391184 |
| Dustin_humanize | 4999050 | 6925096 | 5187872 | 6240160 | 4177888 | 4106176 |
| Etcdctl | 25896967 | 30173384 | 27586472 | 28789288 | 27764528 | 27351400 |
| Gorm_schema | 9421675 | 9970880 | 9168760 | 9195264 | 8814832 | 6408464 |
| IXGo | 47404128 | 46697768 | 45830024 | 45301344 | 44802296 | 44663920 |
| K8s_workqueue | 10681827 | 16135904 | 14327424 | 15125896 | 14851032 | 11184104 |
| Toml | 7324966 | 8776408 | 7275648 | 8058000 | 6377560 | 6277424 |
| Uber_zap | 10025000 | 16537360 | 13203360 | 15422104 | 13055272 | 12321640 |
| XGo | 18662581 | 24596488 | 20628496 | 23462536 | 19289208 | 18911672 |

## Without DWARF (strip --strip-debug)

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 11613712 | 12692592 | 9584584 | 11636240 | 9356128 | 9135200 |
| Dustin_humanize | 3711728 | 4709944 | 3038272 | 4242744 | 2894600 | 2838024 |
| Etcdctl | 20251432 | 21515312 | 19003672 | 20130064 | 19452664 | 19056088 |
| Gorm_schema | 7186360 | 6975272 | 6200936 | 6437776 | 6178464 | 4561040 |
| IXGo | 37601624 | 30987896 | 30169328 | 28922968 | 28645904 | 28529616 |
| K8s_workqueue | 8105040 | 11243936 | 9483744 | 10355784 | 10205896 | 7655568 |
| Toml | 5573864 | 6134104 | 4691648 | 5564160 | 4483672 | 4400576 |
| Uber_zap | 7635104 | 11482808 | 8243240 | 10555208 | 8962728 | 8421528 |
| XGo | 14015312 | 17273744 | 13456808 | 16067224 | 13145608 | 12846784 |
