# LLGo binary-size CI
All values are ELF file sizes in bytes, collected by Bent `benchsize`.

| Benchmark | Go | LLGoNoLTO | LLGoDeadcodeDrop | LLGoFullLTONoGlobalDCE | LLGoFullLTOGlobalDCE | LLGoFullLTOGlobalDCEPlugin |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Aws_restjson | 14635492 | 12979384 | 10617632 | 12297968 | 10410808 | 10298256 |
| Dustin_humanize | 4999034 | 4744144 | 3416760 | 4417952 | 3315296 | 3271544 |
| Etcdctl | 25896983 | 21803480 | 20523328 | 20969096 | 20611608 | 20315840 |
| Gorm_schema | 9421683 | 7103728 | 6490784 | 6732888 | 6562808 | 5206720 |
| IXGo | 47404136 | 31452144 | 30749888 | 30173496 | 29874672 | 29739288 |
| K8s_workqueue | 10681819 | 11432200 | 10720608 | 10926600 | 10833288 | 8733376 |
| Toml | 7324958 | 6203008 | 5068872 | 5824632 | 4948272 | 4892288 |
| Uber_zap | 10024992 | 11677792 | 9305848 | 11147384 | 9583280 | 9447512 |
| XGo | 18662581 | 17835064 | 15648000 | 17108936 | 16804384 | 16698368 |
