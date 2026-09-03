package main

import (
	"xgo.dev/benchmarks/wasm-apps/internal/checksumapp"
	"xgo.dev/benchmarks/wasm-apps/internal/command"
)

func main() {
	command.Main(checksumapp.Run)
}
