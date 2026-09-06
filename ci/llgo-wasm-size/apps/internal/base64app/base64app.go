// Package base64app implements a streaming Base64 command.
package base64app

import (
	"encoding/base64"
	"io"
)

// Run encodes standard input, or decodes it when the first argument is "decode".
func Run(args []string, input io.Reader, output io.Writer) error {
	if len(args) > 0 && args[0] == "decode" {
		_, err := io.Copy(output, base64.NewDecoder(base64.StdEncoding, input))
		return err
	}

	encoder := base64.NewEncoder(base64.StdEncoding, output)
	if _, err := io.Copy(encoder, input); err != nil {
		return err
	}
	return encoder.Close()
}
