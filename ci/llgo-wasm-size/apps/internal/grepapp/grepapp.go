// Package grepapp implements a line-oriented regular-expression filter.
package grepapp

import (
	"bufio"
	"errors"
	"io"
	"regexp"
)

var errMissingPattern = errors.New("usage: grep PATTERN")

// Run emits the input lines that match the first command-line argument.
func Run(args []string, input io.Reader, output io.Writer) error {
	if len(args) == 0 {
		return errMissingPattern
	}
	expression, err := regexp.Compile(args[0])
	if err != nil {
		return err
	}
	scanner := bufio.NewScanner(input)
	writer := bufio.NewWriter(output)
	for scanner.Scan() {
		if expression.Match(scanner.Bytes()) {
			if _, err := writer.Write(scanner.Bytes()); err != nil {
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
