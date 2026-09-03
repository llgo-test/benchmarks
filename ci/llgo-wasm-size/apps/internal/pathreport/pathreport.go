// Package pathreport renders normalized input paths as an HTML list.
package pathreport

import (
	"bufio"
	"html"
	"io"
	"path/filepath"
)

// Run reads one path per line and writes a complete escaped HTML report.
func Run(_ []string, input io.Reader, output io.Writer) error {
	scanner := bufio.NewScanner(input)
	writer := bufio.NewWriter(output)
	if _, err := writer.WriteString("<!doctype html><meta charset=\"utf-8\"><title>Paths</title><ul>\n"); err != nil {
		return err
	}
	for scanner.Scan() {
		path := filepath.ToSlash(filepath.Clean(scanner.Text()))
		if _, err := writer.WriteString("<li>" + html.EscapeString(path) + "</li>\n"); err != nil {
			return err
		}
	}
	if err := scanner.Err(); err != nil {
		return err
	}
	if _, err := writer.WriteString("</ul>\n"); err != nil {
		return err
	}
	return writer.Flush()
}
