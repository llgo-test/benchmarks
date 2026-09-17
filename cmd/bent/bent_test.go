// Copyright 2021 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

//go:build go1.16

package main

import (
	"fmt"
	"os"
	"os/exec"
	"path"
	"reflect"
	"runtime"
	"strings"
	"testing"
)

var dir string

// TestMain implemented to allow (1) alternate use as bent command itself if BENT_TEST_IS_CMD_BENT is in environment,
// and (2) to create and remove a temporary directory for test initialization.
func TestMain(m *testing.M) {
	if os.Getenv("BENT_TEST_IS_COMPILER") != "" {
		log, err := os.OpenFile(os.Getenv("BENT_TEST_COMPILER_LOG"), os.O_CREATE|os.O_APPEND|os.O_WRONLY, 0o600)
		if err != nil {
			panic(err)
		}
		pair := os.Getenv("BENT_BENCH") + "/" + os.Getenv("BENT_CONFIG")
		fmt.Fprintln(log, pair)
		log.Close()
		if pair == "first/broken" {
			os.Exit(9)
		}
		for i, arg := range os.Args {
			if arg == "-o" {
				if err := os.WriteFile(os.Args[i+1], []byte("test binary"), 0o700); err != nil {
					panic(err)
				}
			}
		}
		os.Exit(0)
	}
	if os.Getenv("BENT_TEST_IS_CMD_BENT") != "" {
		main()
		os.Exit(0)
	}
	var err error
	dir, err = os.MkdirTemp("", "bent_test")
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
	defer os.RemoveAll(dir)
	m.Run()
}

func TestConfigurationBuildCommandArgs(t *testing.T) {
	originalExplicitAll := explicitAll
	defer func() { explicitAll = originalExplicitAll }()

	tests := []struct {
		name          string
		configuration Configuration
		benchmark     Benchmark
		randomizing   bool
		explicitAll   counterFlag
		want          []string
	}{
		{
			name: "default fresh build",
			want: []string{"test", "-vet=off", "-c", "-a"},
		},
		{
			name:          "cached alternate compiler",
			configuration: Configuration{OmitVetFlag: true, UseBuildCache: true},
			want:          []string{"test", "-c"},
		},
		{
			name:          "standard library cache",
			configuration: Configuration{OmitVetFlag: true, BuildCache: buildCacheStdlib},
			want:          []string{"test", "-c"},
		},
		{
			name:      "main package fresh build",
			benchmark: Benchmark{BuildMode: "build"},
			want:      []string{"build", "-a"},
		},
		{
			name:          "main package cached alternate compiler",
			configuration: Configuration{OmitVetFlag: true, UseBuildCache: true},
			benchmark:     Benchmark{BuildMode: "build"},
			want:          []string{"build"},
		},
		{
			name:          "explicit a overrides cache opt in",
			configuration: Configuration{OmitVetFlag: true, UseBuildCache: true},
			explicitAll:   1,
			want:          []string{"test", "-c", "-a"},
		},
		{
			name:        "randomized builds never force a",
			randomizing: true,
			explicitAll: 1,
			want:        []string{"test", "-vet=off", "-c"},
		},
	}

	for _, test := range tests {
		t.Run(test.name, func(t *testing.T) {
			explicitAll = test.explicitAll
			got := test.configuration.buildCommandArgs(&test.benchmark, test.randomizing)
			if !reflect.DeepEqual(got, test.want) {
				t.Fatalf("buildCommandArgs() = %q, want %q", got, test.want)
			}
		})
	}
}

func TestBenchmarkBuildMode(t *testing.T) {
	tests := []struct {
		mode     string
		wantMode string
		wantTest bool
		wantErr  bool
	}{
		{wantMode: buildModeTest, wantTest: true},
		{mode: buildModeTest, wantMode: buildModeTest, wantTest: true},
		{mode: buildModeBuild, wantMode: buildModeBuild},
		{mode: "install", wantMode: "install", wantErr: true},
	}
	for _, test := range tests {
		t.Run(test.mode, func(t *testing.T) {
			benchmark := Benchmark{Name: "example", BuildMode: test.mode}
			if got := benchmark.effectiveBuildMode(); got != test.wantMode {
				t.Errorf("effectiveBuildMode() = %q, want %q", got, test.wantMode)
			}
			if got := benchmark.buildsTestBinary(); got != test.wantTest {
				t.Errorf("buildsTestBinary() = %t, want %t", got, test.wantTest)
			}
			if err := benchmark.validateBuildMode(); (err != nil) != test.wantErr {
				t.Errorf("validateBuildMode() error = %v, wantErr %t", err, test.wantErr)
			}
		})
	}
}

func TestBenchOneSkipsBuildMode(t *testing.T) {
	config := Configuration{RunWrapper: []string{"/must-not-run"}}
	benchmark := Benchmark{Name: "command", BuildMode: buildModeBuild}

	output, rc := benchOne(&config, &benchmark, 0, nil)
	if output != "" || rc != 0 {
		t.Fatalf("benchOne(build mode) = (%q, %d), want (\"\", 0)", output, rc)
	}
}

func TestCompileOneBuildsMainPackage(t *testing.T) {
	goCommand, err := exec.LookPath("go")
	if err != nil {
		t.Fatal(err)
	}

	workspace := t.TempDir()
	buildDir := t.TempDir()
	if err := os.MkdirAll(path.Join(workspace, "testbin"), 0o755); err != nil {
		t.Fatal(err)
	}
	if err := os.WriteFile(path.Join(buildDir, "go.mod"), []byte("module example.com/main\n\ngo 1.22\n"), 0o644); err != nil {
		t.Fatal(err)
	}
	if err := os.WriteFile(path.Join(buildDir, "main.go"), []byte("package main\n\nfunc main() {}\n"), 0o644); err != nil {
		t.Fatal(err)
	}

	oldDirs, oldDefaultEnv, oldReportBuildTime := dirs, defaultEnv, reportBuildTime
	defer func() {
		dirs = oldDirs
		defaultEnv = oldDefaultEnv
		reportBuildTime = oldReportBuildTime
	}()
	dirs = &directories{wd: workspace, testBinDir: "testbin"}
	defaultEnv = replaceEnv(os.Environ(), "GOCACHE", t.TempDir())
	reportBuildTime = false

	config := Configuration{Name: "Main", Compiler: goCommand, UseBuildCache: true}
	benchmark := Benchmark{Name: "hello", Suite: "hello", Repo: ".", BuildMode: "build", buildDir: buildDir, NotSandboxed: true}
	if failure := config.compileOne(&benchmark, workspace, 1, false); failure != "" {
		t.Fatal(failure)
	}
	if _, err := os.Stat(path.Join(workspace, "testbin", "hello_Main")); err != nil {
		t.Fatalf("main binary was not created: %v", err)
	}
}

func TestBuildFailureIsLimitedToConfigurationAndSuite(t *testing.T) {
	oldDirs, oldDefaultEnv := dirs, defaultEnv
	t.Cleanup(func() { dirs, defaultEnv = oldDirs, oldDefaultEnv })
	workspace := t.TempDir()
	dirs = &directories{wd: workspace, testBinDir: "testbin"}
	defaultEnv = os.Environ()
	failed := Configuration{Name: "broken", Compiler: path.Join(workspace, "missing-compiler")}
	good := Configuration{Name: "good"}
	benchmark := Benchmark{Name: "first", Suite: "shared", Repo: ".", buildDir: workspace, NotSandboxed: true}
	if failure := failed.compileOne(&benchmark, workspace, 0, false); failure == "" {
		t.Fatal("missing compiler unexpectedly succeeded")
	}
	if benchmark.IsDisabled() || good.isDisabledFor(&benchmark) {
		t.Fatal("one compiler failure disabled the benchmark for other configurations")
	}
	alias := Benchmark{Name: "second", Suite: "shared"}
	if !failed.isDisabledFor(&alias) {
		t.Fatal("other benchmarks sharing the failed binary must not run it")
	}
	other := Benchmark{Name: "other", Suite: "other"}
	if failed.isDisabledFor(&other) {
		t.Fatal("failure disabled unrelated suites")
	}
	if output, rc := benchOne(&failed, &alias, 0, nil); output != "" || rc != 0 {
		t.Fatalf("failed binary was run: %q, %d", output, rc)
	}
}

func TestBuildOnlyContinuesMatrixBeforeReturningFailure(t *testing.T) {
	workspace := t.TempDir()
	run := func(args ...string) ([]byte, error) {
		cmd := bentCmd(t, args...)
		cmd.Dir = workspace
		cmd.Env = append(cmd.Env, "PWD="+workspace, "BENT_TEST_COMPILER_LOG="+path.Join(workspace, "calls"))
		return cmd.CombinedOutput()
	}
	if output, err := run("-I"); err != nil {
		t.Fatalf("initialize: %v\n%s", err, output)
	}
	exe, err := os.Executable()
	if err != nil {
		t.Fatal(err)
	}
	var benchmarks, configurations strings.Builder
	for _, name := range []string{"first", "second"} {
		fmt.Fprintf(&benchmarks, "[[Benchmarks]]\nName = %q\nRepo = \".\"\nStandalone = true\nNotSandboxed = true\n", name)
		buildDir := path.Join(workspace, "build", name)
		if err := os.MkdirAll(buildDir, 0o755); err != nil {
			t.Fatal(err)
		}
		if err := os.WriteFile(path.Join(buildDir, "go.mod"), []byte("module example.com/"+name+"\n\ngo 1.25\n"), 0o600); err != nil {
			t.Fatal(err)
		}
	}
	for _, name := range []string{"broken", "good"} {
		fmt.Fprintf(&configurations, "[[Configurations]]\nName = %q\nCompiler = %q\nGcEnv = [\"BENT_TEST_IS_COMPILER=1\"]\n", name, exe)
	}
	for name, data := range map[string]string{"cases.toml": benchmarks.String(), "compilers.toml": configurations.String()} {
		if err := os.WriteFile(path.Join(workspace, name), []byte(data), 0o600); err != nil {
			t.Fatal(err)
		}
	}
	output, err := run("-X", "-S=0", "-build-only", "-B=cases.toml", "-C=compilers.toml")
	if exit, ok := err.(*exec.ExitError); !ok || exit.ExitCode() != 1 {
		t.Fatalf("build-only failure = %v, want exit 1\n%s", err, output)
	}
	calls, err := os.ReadFile(path.Join(workspace, "calls"))
	if err != nil {
		t.Fatal(err)
	}
	if len(strings.Fields(string(calls))) != 4 {
		t.Fatalf("matrix did not complete: %s\n%s", calls, output)
	}
	for _, pair := range []string{"first/broken", "first/good", "second/broken", "second/good"} {
		if !strings.Contains(string(calls), pair+"\n") {
			t.Errorf("missing build %s: %s", pair, calls)
		}
	}
}

// bentCmd returns a "bent" command (that is implemented by rerunning the current program after setting
// BENT_TEST_IS_CMD_BENT).  The command is always run in the temporary directory created by TestMain.
func bentCmd(t *testing.T, args ...string) *exec.Cmd {
	exe, err := os.Executable()
	if err != nil {
		t.Fatal(err)
	}
	cmd := exec.Command(exe, args...)
	cmd.Dir = dir
	cmd.Env = append(os.Environ(), "BENT_TEST_IS_CMD_BENT=1", "PWD="+dir)
	return cmd
}

func TestBent(t *testing.T) {
	if runtime.GOARCH == "wasm" {
		t.Skipf("skipping test: exec not supported on %s/%s", runtime.GOOS, runtime.GOARCH)
	}
	cmd := bentCmd(t, "-I")
	output, err := cmd.CombinedOutput()
	if err != nil {
		fmt.Fprintf(os.Stderr, "%s\n", output)
		t.Fatal(err)
	}
	t.Log(string(output))
	Cs := []string{"sample", "cronjob", "cmpjob", "gollvm", "llgo-size"}
	Bs := []string{"all", "100", "gc", "gcplus", "trial", "llgo-size"}
	for _, c := range Cs {
		for _, b := range Bs {
			cmd = bentCmd(t, "-l", "-C=configurations-"+c+".toml", "-B=benchmarks-"+b+".toml")
			output, err = cmd.CombinedOutput()
			if err != nil {
				fmt.Fprintf(os.Stderr, "%s\n", output)
				t.Fatal(err)
			}
			t.Log(string(output))
		}
		Bs = Bs[:1] // truncate Bs for remaining configurations
	}
	cmd = bentCmd(t, "-l", "-C=configurations-llgo-compatibility.toml", "-B=benchmarks-llgo-compatibility.toml")
	output, err = cmd.CombinedOutput()
	if err != nil {
		fmt.Fprintf(os.Stderr, "%s\n", output)
		t.Fatal(err)
	}
}
