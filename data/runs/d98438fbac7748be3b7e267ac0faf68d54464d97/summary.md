# LLGo binary-size CI
All values are ELF file sizes in bytes, collected by Bent `benchsize`.

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635492 | 12889456 | 10569768 | 12253720 | 10421248 | 10309104 |
| Dustin_humanize | 4999034 | 4686600 | 3377816 | 4386832 | 3303632 | 3260632 |
| Etcdctl | 25896983 | 21729784 | 20479480 | 20925288 | 20601680 | 20299200 |
| Gorm_schema | 9421683 | 7043896 | 6442072 | 6707280 | 6544504 | 5210256 |
| IXGo | 41505755 | 29765704 | 29135504 | 28818448 | 28567856 | 28432112 |
| K8s_workqueue | 10681819 | 11322912 | 10628080 | 10836808 | 10768672 | 8714008 |
| Toml | 7324958 | 6155608 | 5037888 | 5820352 | 4957640 | 4902040 |
| Uber_zap | 10024992 | 11596888 | 9279792 | 11092824 | 9592376 | 9456936 |
| XGo | 18662581 | 17642512 | 15502240 | 16936208 | 16668480 | 16560432 |
