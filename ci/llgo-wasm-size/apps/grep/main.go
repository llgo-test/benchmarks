package main

import (
	"xgo.dev/benchmarks/wasm-apps/internal/command"
	"xgo.dev/benchmarks/wasm-apps/internal/grepapp"
)

func main() {
	command.Main(grepapp.Run)
}
