# LLGo binary-size CI
All values are ELF file sizes in bytes, collected by Bent `benchsize`.

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635492 | 12978192 | 10616456 | 12296920 | 10409728 | 10297176 |
| Dustin_humanize | 4999034 | 4742912 | 3415576 | 4416848 | 3314216 | 3270448 |
| Etcdctl | 25896983 | 21802280 | 20522128 | 20968152 | 20610720 | 20314920 |
| Gorm_schema | 9421683 | 7102496 | 6489600 | 6731800 | 6561728 | 5205664 |
| IXGo | 47404136 | 31450976 | 30748720 | 30172592 | 29873784 | 29738384 |
| K8s_workqueue | 10681819 | 11430992 | 10719408 | 10925512 | 10832176 | 8732280 |
| Toml | 7324958 | 6201816 | 5067672 | 5823504 | 4947208 | 4891192 |
| Uber_zap | 10024992 | 11676600 | 9304712 | 11146304 | 9582224 | 9446432 |
| XGo | 18662581 | 17833864 | 15646840 | 17108056 | 16803480 | 16697416 |
