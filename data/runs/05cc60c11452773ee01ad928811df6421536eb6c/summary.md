# LLGo binary-size CI
All values are ELF file sizes in bytes, collected by Bent `benchsize`.

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635492 | 12978256 | 10616536 | 12296920 | 10409728 | 10297176 |
| Dustin_humanize | 4999034 | 4742952 | 3415640 | 4416848 | 3314216 | 3270448 |
| Etcdctl | 25896983 | 21802360 | 20522208 | 20968168 | 20610720 | 20314920 |
| Gorm_schema | 9421683 | 7102568 | 6489680 | 6731816 | 6561728 | 5205648 |
| IXGo | 47404136 | 31451040 | 30748768 | 30172592 | 29873784 | 29738384 |
| K8s_workqueue | 10681819 | 11431056 | 10719552 | 10925512 | 10832176 | 8732280 |
| Toml | 7324958 | 6201864 | 5067720 | 5823504 | 4947208 | 4891192 |
| Uber_zap | 10024992 | 11676680 | 9304776 | 11146304 | 9582224 | 9446432 |
| XGo | 18662581 | 17833936 | 15646880 | 17108056 | 16803480 | 16697416 |
