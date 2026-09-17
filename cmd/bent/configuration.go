// Copyright 2021 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

//go:build go1.16

package main

import (
	"bufio"
	"bytes"
	"fmt"
	"io"
	"os"
	"os/exec"
	"path"
	"runtime"
	"strconv"
	"strings"
	"sync"
	"time"
)

// Configuration is a structure that holds all the variables necessary to
// initiate a bent run. These structures are read from a .toml file at
// boot-time.
type Configuration struct {
	Name          string   // Short name used for binary names, mention on command line
	Root          string   // Specific Go root to use for this trial
	Compiler      string   // Optional go-compatible compiler command; defaults to Go from Root
	OmitVetFlag   bool     // Do not pass Go's -vet=off flag to this compiler
	UseBuildCache bool     // Reuse package-cache entries unless Bent's -a flag is explicitly requested
	BuildCache    string   // Optional cache policy: "shared" or isolated "stdlib"
	PgoGen        string   // Name of sub-directory to put profiles for later loading
	PgoUse        string   // Name of sub-directory to take generated profile files
	BuildFlags    []string // BuildFlags supplied to the configured build command (e.g., "-p 1")
	AfterBuild    []string // Array of commands to run, output of all commands for a configuration (across binaries) is collected in <runstamp>.<config>.<cmd>
	GcFlags       string   // GcFlags supplied to the configured build command
	LdFlags       string   // LdFlags supplied to the configured build command
	GcEnv         []string // Environment variables supplied to the configured build command
	RunFlags      []string // Extra flags passed to every runnable test binary
	RunEnv        []string // Extra environment variables passed to the runnable test binary
	RunWrapper    []string // (Outermost) Command and args to precede the runnable test binary; may fail in the sandbox.
	Disabled      bool     // True if this configuration is temporarily disabled
	benchWriter   *os.File
	rootCopy      string          // The contents of GOROOT are copied here to isolate compilation benchmarking.
	cacheSeed     string          // Standard-library-only cache seed, when BuildCache is "stdlib".
	failedSuites  map[string]bool // Build failures affect only this configuration.
}

func (c *Configuration) isDisabledFor(b *Benchmark) bool {
	return c.Disabled || b.IsDisabled() || c.failedSuites[b.Suite]
}

func (c *Configuration) disableSuite(b *Benchmark) {
	if c.failedSuites == nil {
		c.failedSuites = make(map[string]bool)
	}
	c.failedSuites[b.Suite] = true
}

var dirs *directories // constant across all configurations, useful in other contexts.

func (c *Configuration) buildBenchName() string {
	return c.thingBenchName("build")
}

func (c *Configuration) thingBenchName(suffix string) string {
	if len(suffix) != 0 {
		suffix = path.Base(suffix)
	}
	return path.Join(dirs.benchDir, runstamp+"."+c.Name+"."+suffix)
}

func (c *Configuration) benchName(b *Benchmark, count int, randomizingBinaries bool) string {
	n := b.Suite + "_" + c.Name
	if randomizingBinaries {
		n += "_" + strconv.FormatInt(int64(count), 10)
	}

	return n
}

func (c *Configuration) goCommandCopy() string {
	if c.Compiler != "" {
		return c.Compiler
	}
	gocmd := "go"
	if c.rootCopy != "" {
		gocmd = path.Join(c.rootCopy, "bin", gocmd)
	}
	return gocmd
}

func (config *Configuration) buildCommandArgs(bench *Benchmark, randomizingBinaries bool) []string {
	mode := bench.effectiveBuildMode()
	args := []string{mode}
	if mode == buildModeTest {
		if !config.OmitVetFlag {
			args = append(args, "-vet=off")
		}
		args = append(args, "-c")
	}
	// Preserve Bent's historic default of a fresh build. Configurations which
	// can safely share a cache may opt in, while an explicit -a always wins.
	if !randomizingBinaries && (!config.usesBuildCache() || explicitAll != 0) {
		args = append(args, "-a")
	}
	return args
}

func (config *Configuration) createFilesForLater() {
	if config.Disabled {
		return
	}
	f, err := os.Create(config.buildBenchName())
	if err != nil {
		fmt.Println("Error creating build benchmark file ", config.buildBenchName(), ", err=", err)
		config.Disabled = true
	} else {
		fmt.Fprintf(f, "goos: %s\n", runtime.GOOS)
		fmt.Fprintf(f, "goarch: %s\n", runtime.GOARCH)
		f.Close() // will be appending later
	}

	for _, cmd := range config.AfterBuild {
		tbn := config.thingBenchName(cmd)
		f, err := os.Create(tbn)
		if err != nil {
			fmt.Printf("Error creating %s benchmark file %s, err=%v\n", cmd, config.thingBenchName(cmd), err)
			continue
		} else {
			f.Close() // will be appending later
		}
	}
}

func (config *Configuration) runOtherBenchmarks(b *Benchmark, cwd string, cmdEnv []string, count int, randomizingBinaries bool) {
	// Run various other "benchmark" commands on the built binaries, e.g., size, quality of debugging information.
	if config.Disabled {
		return
	}

	for _, cmd := range config.AfterBuild {
		tbn := config.thingBenchName(cmd)
		f, err := os.OpenFile(tbn, os.O_WRONLY|os.O_APPEND, os.ModePerm)
		if err != nil {
			fmt.Printf("There was an error opening %s for append, error %v\n", tbn, err)
			continue
		}

		s := fmt.Sprintf("toolchain: %s\n", config.Name)
		if verbose > 0 {
			fmt.Print(s)
		}
		f.Write([]byte(s))

		if !strings.ContainsAny(cmd, "/") {
			cmd = path.Join(cwd, cmd)
		}
		if b.Disabled {
			f.Close()
			continue
		}
		testBinaryName := config.benchName(b, count, randomizingBinaries)
		c := exec.Command(cmd, path.Join(cwd, dirs.testBinDir, testBinaryName), strings.Title(b.Name))

		c.Env = cmdEnv
		if !b.NotSandboxed {
			c.Env = replaceEnv(c.Env, "GOOS", "linux")
		}

		if verbose > 0 {
			fmt.Println(asCommandLine(cwd, c))
		}
		output, err := c.CombinedOutput()
		if verbose > 0 || err != nil {
			fmt.Println(string(output))
		} else {
			fmt.Print(".")
		}
		if err != nil {
			fmt.Printf("Error running %s\n", cmd)
			f.Close()
			continue
		}
		f.Write(output)
		f.Sync()
		f.Close()
	}
}

func (config *Configuration) compileOne(bench *Benchmark, cwd string, count int, randomizingBinaries bool) string {
	root := config.rootCopy
	if root == "" {
		// Alternate compilers use the configured GOROOT directly instead of a
		// Bent-owned copy of the standard library.
		root = config.Root
	}
	gocmd := config.goCommandCopy()
	gopath := path.Join(cwd, "gopath")

	cmd := exec.Command(gocmd, config.buildCommandArgs(bench, randomizingBinaries)...)
	compileTo := path.Join(dirs.wd, dirs.testBinDir, config.benchName(bench, count, randomizingBinaries))

	cmd.Env = DefaultEnv()

	if !bench.NotSandboxed {
		cmd.Env = replaceEnv(cmd.Env, "GOOS", "linux")
	}
	if root != "" {
		cmd.Env = replaceEnv(cmd.Env, "GOROOT", root)
	}
	cmd.Env = append(cmd.Env, "BENT_BENCH="+bench.Name)
	cmd.Env = append(cmd.Env, "BENT_CONFIG="+config.Name)
	cmd.Env = append(cmd.Env, "BENT_I="+fmt.Sprintf("%d", count))
	cmd.Env = replaceEnvs(cmd.Env, sliceExpandEnv(bench.GcEnv, cmd.Env))
	cmd.Env = replaceEnvs(cmd.Env, sliceExpandEnv(config.GcEnv, cmd.Env))
	cacheDir, cacheCleanup, err := config.isolatedBuildCache()
	if err != nil {
		s := fmt.Sprintf("Could not prepare isolated build cache for %s/%s: %v", bench.Suite, config.Name, err)
		fmt.Println(s + " DISABLING build " + bench.Name + "/" + config.Name)
		config.disableSuite(bench)
		return s + "(" + bench.Name + ")\n"
	}
	defer cacheCleanup()
	if cacheDir != "" {
		cmd.Env = buildCacheEnv(cmd.Env, cacheDir)
	}
	configGoArch := getenv(cmd.Env, "GOARCH")

	cmdEnv := append([]string{}, cmd.Env...) // for after-build
	if configGoArch == "" {
		// inject a default, since the after-build may not be a go program
		cmdEnv = append(cmdEnv, "GOARCH="+runtime.GOARCH)
	}

	cmd.Args = append(cmd.Args, "-o", compileTo)
	cmd.Args = append(cmd.Args, sliceExpandEnv(bench.BuildFlags, cmd.Env)...)
	cmd.Args = append(cmd.Args, sliceExpandEnv(config.BuildFlags, cmd.Env)...)

	if config.PgoUse != "" {
		// We want to use pprof file for pgo
		cmd.Args = append(cmd.Args, "-pgo="+path.Join(dirs.wd, config.PgoUse, bench.Name+".prof"))
	}

	if config.GcFlags != "" {
		cmd.Args = append(cmd.Args, "-gcflags="+expandEnv(config.GcFlags, cmd.Env))
	}
	if strings.TrimSpace(config.LdFlags) != "" {
		cmd.Args = append(cmd.Args, "-ldflags="+expandEnv(config.LdFlags, cmd.Env))
	}
	cmd.Args = append(cmd.Args, bench.Repo)
	cmd.Dir = bench.BuildDir() // use module-mode

	if verbose > 0 {
		fmt.Println(asCommandLine(cwd, cmd))
	} else if os.Getenv("BENT_QUIET_RUN_OUTPUT") != "" {
		fmt.Printf("\ncompiling: %s (%s)\n", bench.Name, config.Name)
	} else {
		fmt.Print(".")
	}

	defer cleanup(gopath)

	start := time.Now()
	output, err := cmd.CombinedOutput()
	realTime := time.Since(start)
	if err != nil {
		s := ""
		buildCommand := fmt.Sprintf("%s %s", gocmd, bench.effectiveBuildMode())
		switch e := err.(type) {
		case *exec.ExitError:
			s = fmt.Sprintf("There was an error running %q, output = %s", buildCommand, output)
		default:
			s = fmt.Sprintf("There was an error running %q, output = %s, error = %v", buildCommand, output, e)
		}
		fmt.Println(s + " DISABLING build " + bench.Name + "/" + config.Name)
		config.disableSuite(bench) // Other configurations can still build and run.
		return s + "(" + bench.Name + ")\n"
	}

	if reportBuildTime {
		// Report and record build stats to testbin
		bs := BenchStat{
			Name:     bench.Name,
			RealTime: realTime,
			UserTime: cmd.ProcessState.UserTime(),
			SysTime:  cmd.ProcessState.SystemTime(),
		}

		buf := new(bytes.Buffer)
		var goarchVal string
		if configGoArch != runtime.GOARCH && configGoArch != "" {
			goarchVal = fmt.Sprintf("%s-%s", runtime.GOARCH, configGoArch)
		} else {
			goarchVal = runtime.GOARCH
		}
		var s string
		s += fmt.Sprintf("goarch: %s\n", goarchVal)
		s += fmt.Sprintf("toolchain: %s\n", config.Name)
		if verbose > 0 {
			fmt.Print(s)
		}
		buf.WriteString(s)
		s = fmt.Sprintf("Benchmark%s 1 %d build-real-ns/op %d build-user-ns/op %d build-sys-ns/op\n",
			strings.Title(bench.Name), bs.RealTime.Nanoseconds(), bs.UserTime.Nanoseconds(), bs.SysTime.Nanoseconds())
		if verbose > 0 {
			fmt.Print(s)
		}
		buf.WriteString(s)
		f, err := os.OpenFile(config.buildBenchName(), os.O_WRONLY|os.O_APPEND, os.ModePerm)
		if err != nil {
			fmt.Printf("There was an error opening %s for append, error %v\n", config.buildBenchName(), err)
			cleanup(gopath)
			os.Exit(2)
		}
		f.Write(buf.Bytes())
		f.Sync()
		f.Close()
	}

	// Trim /usr/bin/time info from soutput, it's ugly
	if verbose > 0 {
		soutput := string(output)
		i := strings.LastIndex(soutput, "real")
		if i >= 0 {
			soutput = soutput[:i]
		}
		fmt.Print(soutput)
	}

	// Do this here before any cleanup.
	if count == 0 {
		config.runOtherBenchmarks(bench, cwd, cmdEnv, count, randomizingBinaries)
	}

	return ""
}

// say writes s to c's benchmark output file
func (c *Configuration) say(s string) {
	b := []byte(s)
	nw, err := c.benchWriter.Write(b)
	if err != nil {
		fmt.Printf("Error writing, err = %v, nwritten = %d, nrequested = %d\n", err, nw, len(b))
	}
	c.benchWriter.Sync()
	fmt.Print(string(b))
}

// runBinary runs cmd and displays the output.
// If the command returns an error, returns an error string.
func (c *Configuration) runBinary(cwd string, cmd *exec.Cmd, printWorkingDot bool) (string, int) {
	line := asCommandLine(cwd, cmd)
	if verbose > 0 {
		fmt.Println(line)
	} else {
		if printWorkingDot {
			fmt.Print(".")
		}
	}

	rc := 0

	stdout, err := cmd.StdoutPipe()
	if err != nil {
		return fmt.Sprintf("Error [stdoutpipe] running '%s', %v", line, err), rc
	}
	stderr, err := cmd.StderrPipe()
	if err != nil {
		return fmt.Sprintf("Error [stderrpipe] running '%s', %v", line, err), rc
	}
	err = cmd.Start()
	if err != nil {
		return fmt.Sprintf("Error [command start] running '%s', %v", line, err), rc
	}

	var mu = &sync.Mutex{}

	quietRunOutput := os.Getenv("BENT_QUIET_RUN_OUTPUT") != ""
	f := func(r *bufio.Reader, done chan error) {
		for {
			bytes, err := r.ReadBytes('\n')
			n := len(bytes)
			if n > 0 {
				mu.Lock()
				nw, err := c.benchWriter.Write(bytes[0:n])
				if err != nil {
					fmt.Printf("Error writing, err = %v, nwritten = %d, nrequested = %d\n", err, nw, n)
				}
				c.benchWriter.Sync()
				if !quietRunOutput {
					fmt.Print(string(bytes[0:n]))
				}
				mu.Unlock()
			}
			if err == io.EOF || n == 0 {
				break
			}
			if err != nil {
				done <- err
				return
			}
		}
		done <- nil
	}

	doneS := make(chan error)
	doneE := make(chan error)

	go f(bufio.NewReader(stdout), doneS)
	go f(bufio.NewReader(stderr), doneE)

	errS := <-doneS
	errE := <-doneE

	err = cmd.Wait()
	rc = cmd.ProcessState.ExitCode()

	if err != nil {
		switch e := err.(type) {
		case *exec.ExitError:
			return fmt.Sprintf("Error running '%s', stderr = %s, rc = %d", line, e.Stderr, rc), rc
		default:
			return fmt.Sprintf("Error running '%s', %v, rc = %d", line, e, rc), rc

		}
	}
	if errS != nil {
		return fmt.Sprintf("Error [read stdout] running '%s', %v, rc = %d", line, errS, rc), rc
	}
	if errE != nil {
		return fmt.Sprintf("Error [read stderr] running '%s', %v, rc = %d", line, errE, rc), rc
	}
	return "", rc
}
