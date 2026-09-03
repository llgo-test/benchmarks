package main

import (
	"fmt"
	"io"
	"os"
	"strconv"
	"time"

	"github.com/universonic/go-rust-wasm-bench/go/conv"
)

func main() {
	if len(os.Args) < 4 {
		fmt.Fprintf(os.Stderr, "usage: conv-wasi <width> <height> <kernel_size> [--bench N]\n")
		os.Exit(1)
	}

	w, _ := strconv.Atoi(os.Args[1])
	h, _ := strconv.Atoi(os.Args[2])
	kernelSize, _ := strconv.Atoi(os.Args[3])

	iterations := 1
	if len(os.Args) >= 6 && os.Args[4] == "--bench" {
		iterations, _ = strconv.Atoi(os.Args[5])
	}

	img, err := io.ReadAll(os.Stdin)
	if err != nil {
		fmt.Fprintf(os.Stderr, "read error: %v\n", err)
		os.Exit(1)
	}

	expected := w * h * 4
	if len(img) < expected {
		fmt.Fprintf(os.Stderr, "expected %d bytes, got %d\n", expected, len(img))
		os.Exit(1)
	}
	img = img[:expected]

	kernel := conv.KernelBySize(kernelSize)

	warmup := 0
	measured := iterations
	if iterations > 1 {
		warmup = 5
		measured = iterations - warmup
	}

	var result []byte

	for i := 0; i < warmup; i++ {
		result = conv.Convolve(img, w, h, kernel)
	}

	for i := 0; i < measured; i++ {
		start := time.Now()
		result = conv.Convolve(img, w, h, kernel)
		elapsed := time.Since(start)
		if iterations > 1 {
			fmt.Fprintf(os.Stderr, "iteration %d: %.6f ms\n", i+1, float64(elapsed.Nanoseconds())/1e6)
		}
	}

	os.Stdout.Write(result)
}
