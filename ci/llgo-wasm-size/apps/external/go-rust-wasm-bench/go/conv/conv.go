package conv

import "math"

var Kernel3 = [][]float64{
	{1, 2, 1},
	{2, 4, 2},
	{1, 2, 1},
}

var Kernel5 = [][]float64{
	{1, 4, 6, 4, 1},
	{4, 16, 24, 16, 4},
	{6, 24, 36, 24, 6},
	{4, 16, 24, 16, 4},
	{1, 4, 6, 4, 1},
}

func KernelBySize(size int) [][]float64 {
	if size == 5 {
		return Kernel5
	}
	return Kernel3
}

func Convolve(img []byte, w, h int, kernel [][]float64) []byte {
	kSize := len(kernel)
	kHalf := kSize / 2
	out := make([]byte, w*h*4)

	var kSum float64
	for _, row := range kernel {
		for _, v := range row {
			kSum += v
		}
	}
	if kSum == 0 {
		kSum = 1
	}

	for y := 0; y < h; y++ {
		for x := 0; x < w; x++ {
			idx := (y*w + x) * 4
			for c := 0; c < 3; c++ {
				var sum float64
				for ky := 0; ky < kSize; ky++ {
					for kx := 0; kx < kSize; kx++ {
						iy := y + ky - kHalf
						ix := x + kx - kHalf
						if iy >= 0 && iy < h && ix >= 0 && ix < w {
							sum += float64(img[(iy*w+ix)*4+c]) * kernel[ky][kx]
						}
					}
				}
				val := sum / kSum
				if val < 0 {
					val = 0
				} else if val > 255 {
					val = 255
				}
				out[idx+c] = byte(math.Round(val))
			}
			out[idx+3] = img[idx+3]
		}
	}
	return out
}
