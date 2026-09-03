// Package globapp implements a line-oriented wildcard filter.
package globapp

import (
	"bufio"
	"errors"
	"io"

	"github.com/tidwall/match"
)

var errMissingPattern = errors.New("usage: glob PATTERN")

// Run emits the input lines that match the first command-line argument.
func Run(args []string, input io.Reader, output io.Writer) error {
	if len(args) == 0 {
		return errMissingPattern
	}
	scanner := bufio.NewScanner(input)
	writer := bufio.NewWriter(output)
	for scanner.Scan() {
		if match.Match(scanner.Text(), args[0]) {
			if _, err := writer.WriteString(scanner.Text()); err != nil {
				return err
			}
			if err := writer.WriteByte('\n'); err != nil {
				return err
			}
		}
	}
	if err := scanner.Err(); err != nil {
		return err
	}
	return writer.Flush()
}
