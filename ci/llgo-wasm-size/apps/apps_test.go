package apps_test

import (
	"bytes"
	"io"
	"strings"
	"testing"

	"xgo.dev/benchmarks/wasm-apps/internal/base64app"
	"xgo.dev/benchmarks/wasm-apps/internal/checksumapp"
	"xgo.dev/benchmarks/wasm-apps/internal/globapp"
	"xgo.dev/benchmarks/wasm-apps/internal/grepapp"
	"xgo.dev/benchmarks/wasm-apps/internal/pathreport"
	"xgo.dev/benchmarks/wasm-apps/internal/wordcount"
)

func TestApplications(t *testing.T) {
	tests := []struct {
		name string
		run  application
		args []string
		in   string
		want string
	}{
		{
			name: "base64",
			run:  base64app.Run,
			in:   "Go WASI",
			want: "R28gV0FTSQ==",
		},
		{
			name: "checksum",
			run:  checksumapp.Run,
			in:   "Go WASI",
			want: "crc32\t9db7214d\nfnv1a\t1030bea5\n",
		},
		{
			name: "grep",
			run:  grepapp.Run,
			args: []string{`^go`},
			in:   "go\nrust\ngopher\n",
			want: "go\ngopher\n",
		},
		{
			name: "glob",
			run:  globapp.Run,
			args: []string{"go*"},
			in:   "go\nrust\ngopher\n",
			want: "go\ngopher\n",
		},
		{
			name: "path-report",
			run:  pathreport.Run,
			in:   "docs/../README.md\na&b/report.html\n",
			want: "<!doctype html><meta charset=\"utf-8\"><title>Paths</title><ul>\n<li>README.md</li>\n<li>a&amp;b/report.html</li>\n</ul>\n",
		},
		{
			name: "word-count",
			run:  wordcount.Run,
			in:   "Hello, 世界\nGo\n",
			want: "{\"bytes\":17,\"lines\":2,\"words\":3,\"runes\":13}\n",
		},
	}

	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			input := bytes.NewBufferString(test.in)
			output := new(bytes.Buffer)
			if err := test.run(test.args, input, output); err != nil {
				t.Fatal(err)
			}
			if got := output.String(); got != test.want {
				t.Fatalf("output = %q, want %q", got, test.want)
			}
		})
	}
}

type application func([]string, io.Reader, io.Writer) error

func TestBase64Decode(t *testing.T) {
	input := strings.NewReader("R28gV0FTSQ==")
	output := new(bytes.Buffer)
	if err := base64app.Run([]string{"decode"}, input, output); err != nil {
		t.Fatal(err)
	}
	if got := output.String(); got != "Go WASI" {
		t.Fatalf("output = %q", got)
	}
}
