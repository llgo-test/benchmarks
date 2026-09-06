// Package wordcount implements a Unicode-aware text statistics command.
package wordcount

import (
	"bytes"
	"io"
	"unicode"
	"unicode/utf8"
)

// Run counts bytes, lines, words, and UTF-8 runes and writes a JSON record.
func Run(_ []string, input io.Reader, output io.Writer) error {
	data, err := io.ReadAll(input)
	if err != nil {
		return err
	}
	lines := bytes.Count(data, []byte{'\n'})
	if len(data) > 0 && data[len(data)-1] != '\n' {
		lines++
	}
	words := 0
	inWord := false
	for _, r := range string(data) {
		if unicode.IsSpace(r) {
			inWord = false
		} else if !inWord {
			words++
			inWord = true
		}
	}
	report := []byte("{\"bytes\":")
	report = appendUint(report, uint64(len(data)))
	report = append(report, ",\"lines\":"...)
	report = appendUint(report, uint64(lines))
	report = append(report, ",\"words\":"...)
	report = appendUint(report, uint64(words))
	report = append(report, ",\"runes\":"...)
	report = appendUint(report, uint64(utf8.RuneCount(data)))
	report = append(report, '}', '\n')
	_, err = output.Write(report)
	return err
}

func appendUint(destination []byte, value uint64) []byte {
	var digits [20]byte
	position := len(digits)
	for {
		position--
		digits[position] = byte(value%10) + '0'
		value /= 10
		if value == 0 {
			return append(destination, digits[position:]...)
		}
	}
}
