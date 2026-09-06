package main

import (
	"xgo.dev/benchmarks/wasm-apps/internal/command"
	"xgo.dev/benchmarks/wasm-apps/internal/wordcount"
)

func main() {
	command.Main(wordcount.Run)
}
