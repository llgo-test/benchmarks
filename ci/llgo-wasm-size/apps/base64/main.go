package main

import (
	"xgo.dev/benchmarks/wasm-apps/internal/base64app"
	"xgo.dev/benchmarks/wasm-apps/internal/command"
)

func main() {
	command.Main(base64app.Run)
}
