// Package command contains the common command-line adapter used by the WASI apps.
package command

import (
	"io"
	"os"
)

// Main runs an application with WASI standard streams and reports failures.
func Main(run func([]string, io.Reader, io.Writer) error) {
	if err := run(os.Args[1:], os.Stdin, os.Stdout); err != nil {
		_, _ = os.Stderr.WriteString(err.Error() + "\n")
		os.Exit(1)
	}
}
