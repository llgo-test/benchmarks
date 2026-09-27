# LLGo binary-size CI
All values are ELF file sizes in bytes, collected by Bent `benchsize`.

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635492 | 12978144 | 10616424 | 12296920 | 10409728 | 10297176 |
| Dustin_humanize | 4999034 | 4742840 | 3415528 | 4416848 | 3314216 | 3270448 |
| Etcdctl | 25896983 | 21802232 | 20522096 | 20968152 | 20610720 | 20314920 |
| Gorm_schema | 9421683 | 7102440 | 6489552 | 6731800 | 6561728 | 5205664 |
| IXGo | 47404136 | 31450920 | 30748656 | 30172592 | 29873784 | 29738384 |
| K8s_workqueue | 10681819 | 11430928 | 10719360 | 10925512 | 10832176 | 8732280 |
| Toml | 7324958 | 6201752 | 5067608 | 5823504 | 4947208 | 4891192 |
| Uber_zap | 10024992 | 11676552 | 9304664 | 11146304 | 9582224 | 9446432 |
| XGo | 18662581 | 17833808 | 15646776 | 17108056 | 16803480 | 16697416 |
