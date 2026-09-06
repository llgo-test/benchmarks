package main

import (
	"fmt"
	"io"
	"os"
	"strconv"
	"time"

	"github.com/universonic/go-rust-wasm-bench/go/jsonrt"
)

func main() {
	iterations := 1
	if len(os.Args) >= 3 && os.Args[1] == "--bench" {
		iterations, _ = strconv.Atoi(os.Args[2])
	}

	input, err := io.ReadAll(os.Stdin)
	if err != nil {
		fmt.Fprintf(os.Stderr, "read error: %v\n", err)
		os.Exit(1)
	}

	warmup := 0
	measured := iterations
	if iterations > 1 {
		warmup = 5
		measured = iterations - warmup
	}

	var result []byte

	for i := 0; i < warmup; i++ {
		result, _ = jsonrt.Process(input)
	}

	for i := 0; i < measured; i++ {
		start := time.Now()
		result, err = jsonrt.Process(input)
		elapsed := time.Since(start)
		if err != nil {
			fmt.Fprintf(os.Stderr, "process error: %v\n", err)
			os.Exit(1)
		}
		if iterations > 1 {
			fmt.Fprintf(os.Stderr, "iteration %d: %.6f ms\n", i+1, float64(elapsed.Nanoseconds())/1e6)
		}
	}

	os.Stdout.Write(result)
}
