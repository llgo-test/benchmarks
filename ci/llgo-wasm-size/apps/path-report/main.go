package main

import (
	"xgo.dev/benchmarks/wasm-apps/internal/command"
	"xgo.dev/benchmarks/wasm-apps/internal/pathreport"
)

func main() {
	command.Main(pathreport.Run)
}
