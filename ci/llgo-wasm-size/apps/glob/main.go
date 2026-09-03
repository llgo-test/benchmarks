package main

import (
	"xgo.dev/benchmarks/wasm-apps/internal/command"
	"xgo.dev/benchmarks/wasm-apps/internal/globapp"
)

func main() {
	command.Main(globapp.Run)
}
