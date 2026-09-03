// Package checksumapp implements a streaming checksum command.
package checksumapp

import (
	"hash/crc32"
	"hash/fnv"
	"io"
)

// Run calculates two checksums for standard input and writes a stable text report.
func Run(_ []string, input io.Reader, output io.Writer) error {
	crc := crc32.NewIEEE()
	fnv1a := fnv.New32a()
	if _, err := io.Copy(io.MultiWriter(crc, fnv1a), input); err != nil {
		return err
	}
	encoded := encodeHex(crc.Sum(nil))
	if _, err := output.Write(append(append([]byte("crc32\t"), encoded...), '\n')); err != nil {
		return err
	}
	encoded = encodeHex(fnv1a.Sum(nil))
	_, err := output.Write(append(append([]byte("fnv1a\t"), encoded...), '\n'))
	return err
}

func encodeHex(source []byte) []byte {
	const digits = "0123456789abcdef"
	encoded := make([]byte, len(source)*2)
	for index, value := range source {
		encoded[index*2] = digits[value>>4]
		encoded[index*2+1] = digits[value&0x0f]
	}
	return encoded
}
