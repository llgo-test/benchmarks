## Build timing diagnostics

Native Bent `-report-build-time` records, sorted by CPU time (`user + sys`, slowest first). Wall time is diagnostic only.

| Benchmark | Configuration | CPU (user + sys) | User | Sys | Wall (reference) |
| --- | --- | ---: | ---: | ---: | ---: |
| IXGo | LLGoFullLTOGlobalDCEPlugin | 906959.1 ms | 880199.0 ms | 26760.1 ms | 578392.3 ms |
| IXGo | LLGoFullLTOGlobalDCE | 837655.4 ms | 811222.8 ms | 26432.7 ms | 538607.9 ms |
| IXGo | LLGoFullLTONoGlobalDCE | 818587.2 ms | 792332.8 ms | 26254.4 ms | 530566.5 ms |
| IXGo | LLGoDeadcodeDrop | 523299.0 ms | 495741.5 ms | 27557.4 ms | 168958.5 ms |
| IXGo | LLGoNoLTO | 471946.5 ms | 450328.1 ms | 21618.4 ms | 148279.0 ms |
| Etcdctl | LLGoFullLTOGlobalDCEPlugin | 465289.5 ms | 452925.7 ms | 12363.7 ms | 336979.1 ms |
| Etcdctl | LLGoFullLTOGlobalDCE | 464131.8 ms | 451635.6 ms | 12496.2 ms | 335940.4 ms |
| Etcdctl | LLGoFullLTONoGlobalDCE | 457237.5 ms | 445208.7 ms | 12028.9 ms | 335291.3 ms |
| Aws_restjson | LLGoFullLTONoGlobalDCE | 344209.0 ms | 336980.2 ms | 7228.9 ms | 229805.2 ms |
| XGo | LLGoFullLTONoGlobalDCE | 344088.0 ms | 335385.0 ms | 8703.0 ms | 273539.2 ms |
| Aws_restjson | LLGoFullLTOGlobalDCEPlugin | 324098.9 ms | 316794.6 ms | 7304.3 ms | 203530.8 ms |
| Aws_restjson | LLGoFullLTOGlobalDCE | 309910.7 ms | 302724.5 ms | 7186.3 ms | 195781.2 ms |
| XGo | LLGoFullLTOGlobalDCE | 305165.6 ms | 296849.0 ms | 8316.6 ms | 235234.8 ms |
| XGo | LLGoFullLTOGlobalDCEPlugin | 304322.6 ms | 295933.8 ms | 8388.8 ms | 233609.3 ms |
| Uber_zap | LLGoFullLTONoGlobalDCE | 294604.6 ms | 287987.7 ms | 6616.9 ms | 203927.9 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCE | 285952.9 ms | 279298.9 ms | 6654.0 ms | 198608.7 ms |
| K8s_workqueue | LLGoFullLTONoGlobalDCE | 276362.6 ms | 269956.4 ms | 6406.2 ms | 191304.8 ms |
| Uber_zap | LLGoFullLTOGlobalDCEPlugin | 271461.0 ms | 265286.7 ms | 6174.3 ms | 179074.5 ms |
| Uber_zap | LLGoFullLTOGlobalDCE | 264985.3 ms | 258967.8 ms | 6017.5 ms | 175726.0 ms |
| Aws_restjson | LLGoNoLTO | 261159.3 ms | 255469.3 ms | 5690.0 ms | 81345.3 ms |
| K8s_workqueue | LLGoFullLTOGlobalDCEPlugin | 257439.9 ms | 251141.7 ms | 6298.2 ms | 167378.8 ms |
| Aws_restjson | LLGoDeadcodeDrop | 256361.7 ms | 250075.0 ms | 6286.7 ms | 82113.3 ms |
| Etcdctl | LLGoDeadcodeDrop | 242551.4 ms | 232044.6 ms | 10506.8 ms | 84264.1 ms |
| Etcdctl | LLGoNoLTO | 236967.8 ms | 227634.4 ms | 9333.4 ms | 81385.6 ms |
| Uber_zap | LLGoNoLTO | 209784.4 ms | 205042.3 ms | 4742.2 ms | 66837.2 ms |
| Uber_zap | LLGoDeadcodeDrop | 204732.7 ms | 199621.3 ms | 5111.4 ms | 66640.1 ms |
| K8s_workqueue | LLGoNoLTO | 202437.3 ms | 197497.5 ms | 4939.8 ms | 64741.6 ms |
| K8s_workqueue | LLGoDeadcodeDrop | 197689.5 ms | 192746.3 ms | 4943.3 ms | 64518.4 ms |
| Gorm_schema | LLGoFullLTOGlobalDCE | 151117.7 ms | 147343.0 ms | 3774.7 ms | 101145.5 ms |
| Gorm_schema | LLGoFullLTONoGlobalDCE | 146549.3 ms | 142789.2 ms | 3760.1 ms | 99239.5 ms |
| XGo | LLGoDeadcodeDrop | 138344.8 ms | 130963.5 ms | 7381.3 ms | 50190.6 ms |
| Toml | LLGoFullLTONoGlobalDCE | 138243.7 ms | 134629.7 ms | 3614.0 ms | 92807.7 ms |
| XGo | LLGoNoLTO | 134264.3 ms | 128121.8 ms | 6142.5 ms | 49453.7 ms |
| Toml | LLGoFullLTOGlobalDCEPlugin | 129145.0 ms | 125649.1 ms | 3495.8 ms | 80742.1 ms |
| Toml | LLGoFullLTOGlobalDCE | 127109.8 ms | 123678.9 ms | 3431.0 ms | 79973.7 ms |
| Gorm_schema | LLGoFullLTOGlobalDCEPlugin | 124103.6 ms | 120529.3 ms | 3574.3 ms | 75573.5 ms |
| Gorm_schema | LLGoDeadcodeDrop | 112930.7 ms | 109535.5 ms | 3395.2 ms | 39150.1 ms |
| Gorm_schema | LLGoNoLTO | 110144.7 ms | 107190.3 ms | 2954.4 ms | 37881.7 ms |
| Toml | LLGoDeadcodeDrop | 106089.1 ms | 102999.0 ms | 3090.1 ms | 36318.3 ms |
| Toml | LLGoNoLTO | 104770.5 ms | 102063.4 ms | 2707.1 ms | 35717.4 ms |
| Dustin_humanize | LLGoFullLTONoGlobalDCE | 100267.7 ms | 97630.5 ms | 2637.1 ms | 70211.1 ms |
| IXGo | Go | 98251.4 ms | 83368.9 ms | 14882.5 ms | 26776.2 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCEPlugin | 83116.8 ms | 80657.3 ms | 2459.5 ms | 52562.4 ms |
| Dustin_humanize | LLGoFullLTOGlobalDCE | 81971.0 ms | 79626.5 ms | 2344.5 ms | 51791.6 ms |
| Dustin_humanize | LLGoDeadcodeDrop | 76191.2 ms | 73917.6 ms | 2273.6 ms | 28392.9 ms |
| Dustin_humanize | LLGoNoLTO | 73537.7 ms | 71606.8 ms | 1930.9 ms | 26939.3 ms |
| Etcdctl | Go | 38286.4 ms | 33034.8 ms | 5251.6 ms | 11771.9 ms |
| XGo | Go | 22106.2 ms | 18986.6 ms | 3119.6 ms | 6743.1 ms |
| Aws_restjson | Go | 9313.0 ms | 7781.5 ms | 1531.5 ms | 3827.9 ms |
| Gorm_schema | Go | 6662.7 ms | 5716.8 ms | 945.9 ms | 2606.2 ms |
| Uber_zap | Go | 6035.9 ms | 5130.7 ms | 905.2 ms | 2440.0 ms |
| K8s_workqueue | Go | 5351.2 ms | 4399.4 ms | 951.8 ms | 1913.4 ms |
| Toml | Go | 2294.5 ms | 1914.1 ms | 380.4 ms | 1089.5 ms |
| Dustin_humanize | Go | 902.8 ms | 673.4 ms | 229.4 ms | 432.4 ms |

### Configuration totals

| Configuration | Total CPU (user + sys) | Total wall (reference) | Cases |
| --- | ---: | ---: | ---: |
| LLGoFullLTONoGlobalDCE | 2920149.7 ms | 2026693.2 ms | 9 |
| LLGoFullLTOGlobalDCEPlugin | 2865936.2 ms | 1907843.0 ms | 9 |
| LLGoFullLTOGlobalDCE | 2828000.3 ms | 1912809.8 ms | 9 |
| LLGoDeadcodeDrop | 1858190.1 ms | 620546.2 ms | 9 |
| LLGoNoLTO | 1805012.5 ms | 592580.9 ms | 9 |
| Go | 189204.0 ms | 57600.7 ms | 9 |

Dependency download details are in `download-timings.log`.
