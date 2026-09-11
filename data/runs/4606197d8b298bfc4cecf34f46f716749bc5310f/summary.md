# LLGo binary-size CI
All values are ELF file sizes in bytes, collected by Bent `benchsize`.

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635492 | 12932040 | 10566704 | 12239480 | 10362696 | 10250200 |
| Dustin_humanize | 4999034 | 4698224 | 3365832 | 4377536 | 3276928 | 3232968 |
| Etcdctl | 25896983 | 21812568 | 20537376 | 20944904 | 20588080 | 20292680 |
| Gorm_schema | 9421683 | 7076792 | 6464848 | 6705032 | 6533264 | 5180424 |
| IXGo | 41505755 | 29915184 | 29262072 | 28921512 | 28622840 | 28495544 |
| K8s_workqueue | 10681819 | 11351016 | 10641688 | 10837600 | 10743000 | 8662592 |
| Toml | 7324958 | 6184056 | 5034112 | 5812672 | 4924256 | 4868352 |
| Uber_zap | 10024992 | 11626816 | 9259968 | 11089632 | 9533432 | 9397728 |
| XGo | 18662581 | 17892552 | 15683584 | 17122656 | 16812808 | 16706384 |
