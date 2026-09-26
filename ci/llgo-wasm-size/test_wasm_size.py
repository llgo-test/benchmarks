import importlib.util
import json
import os
import csv
import shutil
import sys
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest import mock


HERE = Path(__file__).resolve().parent


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


report = load_module("wasm_size_report", HERE / "report.py")
archive = load_module("wasm_size_archive", HERE / "archive.py")


def results(go, tinygo, llgo):
    values = [go, tinygo, llgo, llgo, llgo, llgo]
    return {config: {"bytes": value, "status": "success" if value is not None else "failed"}
            for config, value in zip(report.CONFIGS, values)}


class WasmSizeTest(unittest.TestCase):
    def test_report_requires_exact_app_set_and_records_six_configs(self):
        manifest = [
            {"id": "base64", "command": "base64", "source": "base64", "provenance": "repository", "kind": "streaming codec", "description": "Encoding", "tinygo": "required"},
            {"id": "grep", "command": "grep", "source": "grep", "provenance": "repository", "kind": "text search", "description": "Matching", "tinygo": "required"},
        ]
        with mock.patch.dict(os.environ, {"GO_VERSION": "1.26.2", "LLGO_BUILD_GO_VERSION": "1.27.0", "TINYGO_VERSION": "0.41.1"}, clear=True):
            document = report.build_document(manifest, {"base64": results(900, 100, 80), "grep": results(1200, 200, 600)})
        self.assertEqual(document["target"], {"goos": "wasip1", "goarch": "wasm"})
        self.assertEqual(document["configs"], report.CONFIGS)
        self.assertTrue(document["protocol"]["sameGoToolchain"])
        self.assertEqual(document["run"]["llgoBuildGoVersion"], "1.27.0")
        self.assertEqual(document["protocol"]["Go"], ["build", "-trimpath", "-ldflags=-s -w"])
        self.assertEqual(document["protocol"]["LLGoNoLTO"], ["build", "-a", "-Oz"])
        self.assertIn("Emscripten wasm-opt", document["protocol"]["LLGoPostLink"])
        self.assertEqual(document["benchmarks"][1]["source"], "grep")
        self.assertEqual(document["benchmarks"][0]["provenance"], "repository")
        self.assertEqual(document["benchmarks"][1]["values"]["LLGoNoLTO"], 600)
        self.assertEqual(document["benchmarks"][0]["values"]["Go"], 900)
        with self.assertRaisesRegex(ValueError, "missing=.*grep"):
            report.build_document(manifest, {"base64": results(900, 100, 80)})

    def test_independent_suites_merge_in_either_order_and_replace_only_owned_rows(self):
        for order in (("standard", "tsgo"), ("tsgo", "standard")):
            with self.subTest(order=order), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                apps = report.read_manifest(HERE / "apps.tsv")
                for index, suite in enumerate((*order, order[0])):
                    app = next(row for row in apps if (row["id"] == "tsgo") == (suite == "tsgo"))
                    directory = root / str(index)
                    directory.mkdir()
                    with mock.patch.dict(os.environ, {"WASM_SUITE": suite, "LLGO_COMMIT": "a" * 40}):
                        document = report.build_document([app], {app["id"]: results(100 + index, 50, 20)})
                    (directory / "results.json").write_text(json.dumps(document))
                    report.write_summary(document, directory / "summary.md")
                    (directory / "sizes.tsv").write_text("app\tconfig\tbytes\tstatus\n")
                    (directory / "logs").mkdir()
                    (directory / "logs" / (app["id"] + ".Go.log")).write_text(str(index))
                    archive.archive(directory, root / "pages")
                published = root / "pages/data/wasm/runs" / ("a" * 40)
                merged = json.loads((published / "results.json").read_text())
                rows = {row["id"]: row for row in merged["benchmarks"]}
                self.assertEqual(set(rows), {"base64", "tsgo"})
                self.assertEqual(rows["tsgo" if order[0] == "tsgo" else "base64"]["values"]["Go"], 102)
                self.assertEqual(len((published / "sizes.tsv").read_text().splitlines()), 13)
                self.assertEqual(len(list((published / "logs").iterdir())), 2)
                self.assertEqual(set(merged["comparisonsByTarget"]), {"js", "wasip1"})

    def test_archive_keys_history_by_llgo_commit(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            run_dir = root / "run"
            pages_dir = root / "pages"
            run_dir.mkdir()
            document = {
                "format": "wasm-file-size",
                "run": {
                    "id": "42",
                    "createdAt": "2026-09-03T00:00:00Z",
                    "llgoRepository": "xgo-dev/llgo",
                    "llgoCommit": "a" * 40,
                    "llgoMainIndex": 7,
                    "llgoBuildGoVersion": "1.27.0",
                    "tinygoVersion": "0.41.1",
                },
            }
            (run_dir / "results.json").write_text(json.dumps(document), encoding="utf-8")
            (run_dir / "summary.md").write_text("summary\n", encoding="utf-8")
            (run_dir / "sizes.tsv").write_text(
                "app\tgo_bytes\ttinygo_bytes\tllgo_bytes\nbase64\t100\t10\t20\n",
                encoding="utf-8",
            )
            key = archive.archive(run_dir, pages_dir)
            self.assertEqual(key, "a" * 40)
            index = json.loads((pages_dir / "data" / "wasm" / "index.json").read_text(encoding="utf-8"))
            self.assertEqual(index["runs"][0]["path"], f"wasm/runs/{'a' * 40}/results.json")
            self.assertEqual(index["runs"][0]["tinygoVersion"], "0.41.1")
            self.assertEqual(index["runs"][0]["llgoBuildGoVersion"], "1.27.0")

    def test_archive_and_linux_publisher_reject_path_segment_keys(self):
        publisher = HERE.parent / "llgo-size" / "publish.sh"
        site_files = (
            "index.html",
            "wasm-tinygo.html",
            "js-wasm.html",
            "js-wasm-tinygo.html",
            "linux.html",
            "app.js",
            "wasm.js",
            "performance.html",
            "performance.js",
            "compatibility.html",
            "compatibility.js",
            "style.css",
            "_config.yml",
        )
        for key in (".", ".."):
            with self.subTest(key=key), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                results_dir = root / "results"
                pages_dir = root / "pages"
                site_dir = root / "site"
                results_dir.mkdir()
                site_dir.mkdir()
                document = {"run": {"llgoCommit": key}}
                (results_dir / "results.json").write_text(json.dumps(document), encoding="utf-8")
                for name in site_files:
                    (site_dir / name).write_text("placeholder\n", encoding="utf-8")

                with self.assertRaisesRegex(ValueError, "invalid WASM run key"):
                    archive.run_key(document)
                completed = subprocess.run(
                    [publisher, results_dir, pages_dir, site_dir],
                    check=False,
                    capture_output=True,
                    text=True,
                )
                self.assertNotEqual(completed.returncode, 0)
                self.assertIn("invalid run key", completed.stderr)
                self.assertFalse((pages_dir / "data" / "results.json").exists())
                self.assertFalse((pages_dir / "data" / "runs" / "results.json").exists())


class NullableResultsTest(unittest.TestCase):
    def setUp(self):
        self.manifest = report.read_manifest(HERE / "apps.tsv")[:2]
        self.manifest[0]["tinygo"] = "optional"

    def test_nullable_json_and_baseline_sample_sets(self):
        sizes = {self.manifest[0]["id"]: results(100, None, 50),
                 self.manifest[1]["id"]: results(200, 50, 200)}
        document = report.build_document(self.manifest, sizes)
        document = json.loads(json.dumps(document, allow_nan=False))
        self.assertEqual(document["schemaVersion"], 2)
        self.assertIsNone(document["benchmarks"][0]["values"]["TinyGo"])
        self.assertEqual(document["benchmarks"][0]["builds"]["TinyGo"]["status"], "failed")
        for mode in report.LLGO_CONFIGS:
            self.assertAlmostEqual(document["comparisons"]["Go"][mode]["ratio"], 0.5 ** 0.5)
            self.assertEqual(document["comparisons"]["Go"][mode]["samples"], 2)
            self.assertEqual(document["comparisons"]["TinyGo"][mode], {"ratio": 4.0, "samples": 1})
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "summary.md"
            report.write_summary(document, output)
            self.assertIn("vs. TinyGo", output.read_text())
            self.assertIn("| 4.000x | 1 |", output.read_text())

    def test_empty_tinygo_sample_set(self):
        app = self.manifest[0]
        document = report.build_document([app], {app["id"]: results(100, None, 50)})
        for value in document["comparisons"]["TinyGo"].values():
            self.assertEqual(value, {"ratio": None, "samples": 0})

    def test_required_failures_are_reported_but_missing_configurations_are_rejected(self):
        app = self.manifest[1]
        for mode in report.CONFIGS:
            for missing in (False, True):
                with self.subTest(mode=mode, missing=missing):
                    values = results(100, 50, 20)
                    if missing:
                        del values[mode]
                    else:
                        values[mode] = {"bytes": None, "status": "failed"}
                    if missing:
                        with self.assertRaises(ValueError):
                            report.build_document([app], {app["id"]: values})
                    else:
                        document = report.build_document([app], {app["id"]: values})
                        self.assertIsNone(document["benchmarks"][0]["values"][mode])
                        with tempfile.TemporaryDirectory() as temp:
                            output = Path(temp) / "summary.md"
                            report.write_summary(document, output)
                            self.assertIn("failed", output.read_text().lower())
                            self.assertNotIn("None", output.read_text())

    def test_invalid_status_sizes_and_duplicate_rows(self):
        for rows in ("base64\tGo\t0\tsuccess\n", "base64\tGo\tnull\tsuccess\n",
                     "base64\tTinyGo\t40\tfailed\n", "base64\tGo\t10\tsuccess\n" * 2,
                     "base64\tunknown\t10\tsuccess\n"):
            with self.subTest(rows=rows), tempfile.TemporaryDirectory() as temp:
                path = Path(temp) / "sizes.tsv"
                path.write_text("app\tconfig\tbytes\tstatus\n" + rows)
                with self.assertRaises(ValueError):
                    report.read_sizes(path)


class RunnerTest(unittest.TestCase):
    def run_fixture(self, root, policy="required", failure="", invalid=False, binaryen="132", two_apps=False, js=False, timeout=False, suite=""):
        script = root / "script"
        script.mkdir()
        for name in ("run.sh", "report.py", "prepare_sources.py"):
            shutil.copy2(HERE / name, script / name)
        wrapper_dir = root / "llgo-size" / "bin"
        wrapper_dir.mkdir(parents=True)
        shutil.copy2(HERE.parent / "llgo-size" / "bin" / "llgo-build-timeout", wrapper_dir)
        app = report.read_manifest(HERE / "apps.tsv")[0]
        app["tinygo"] = policy
        if js:
            app.update(id="tsgo", command="tsgo", goos="js")
        (script / "apps" / app["source"]).mkdir(parents=True)
        with (script / "apps.tsv").open("w") as stream:
            writer = csv.DictWriter(stream, fieldnames=app, delimiter="\t")
            writer.writeheader()
            writer.writerow(app)
            if two_apps:
                second = {**app, "id": "second", "source": "second", "command": "second"}
                (script / "apps" / "second").mkdir()
                writer.writerow(second)
        bin_dir = root / "bin"
        bin_dir.mkdir()
        # The fake compilers exercise shell orchestration, output verification,
        # failure policy, and argv boundaries without requiring toolchains in PR CI.
        program = '''#!PYTHON
import json, os, sys, time
from pathlib import Path
name = Path(sys.argv[0]).name
if "-o" not in sys.argv:
    print("wasm-opt version " + os.environ["RESOLVED_BINARYEN"] if name == "wasm-opt" else name + " fixture 22.1.8")
    raise SystemExit(0)
config = {"go": "Go", "tinygo": "TinyGo"}.get(name, "LLGoNoLTO")
if name == "llgo":
    if "-deadcodedrop" in sys.argv: config = "LLGoDeadcodeDrop"
    if "-lto=full" in sys.argv:
        config = "LLGoFullLTONoGlobalDCE" if "-globaldce=false" in sys.argv else "LLGoFullLTOGlobalDCE"
with open(os.environ["CALLS"], "a") as f:
    f.write(json.dumps({"config": config, "args": sys.argv[1:], "wasmopt": os.environ.get("WASMOPT"), "gowork": os.environ.get("GOWORK"), "ccflags": os.environ.get("CCFLAGS"), "ldflags": os.environ.get("LDFLAGS"), "goos": os.environ.get("GOOS"), "goflags": os.environ.get("GOFLAGS")}) + "\\n")
output = Path(sys.argv[sys.argv.index("-o")+1])
if config == os.environ["FAIL_CONFIG"] and Path.cwd().name == "base64":
    if os.environ.get("TIMEOUT_BUILD") == "1": time.sleep(10)
    output.write_bytes(b"invalid")
    print("compiler failure evidence")
    raise SystemExit(0 if os.environ["INVALID_WASM"] == "1" else 9)
if output.suffix == ".mjs":
    output.write_text("export default function() {}")
    output = output.with_suffix(".wasm")
output.write_bytes(b"\\0asm" + b"x" * 20)
'''.replace("PYTHON", sys.executable)
        for name in ("go", "tinygo", "llgo", "clang++", "wasm-ld", "wasm-opt", "llgo-wasm-opt"):
            path = bin_dir / name
            path.write_text(program)
            path.chmod(0o755)
        env = {**os.environ, "PATH": str(bin_dir) + os.pathsep + os.environ["PATH"],
               "LLGO_BIN": str(bin_dir / "llgo"), "GO_VERSION": "1.26.2",
               "TINYGO_VERSION": "0.41.1", "BINARYEN_VERSION": "132", "LLVM_VERSION": "22",
               "LLGO_WASMOPT": str(bin_dir / "llgo-wasm-opt"), "LLGO_ROOT": str(root),
               "TIMEOUT_BUILD": "1" if timeout else "0", "WASM_SUITE": suite,
               "LLGO_BUILD_TIMEOUT_SECONDS": "0.3" if timeout else "20",
               "CALLS": str(root / "calls.jsonl"), "FAIL_CONFIG": failure,
               "INVALID_WASM": "1" if invalid else "0", "RESOLVED_BINARYEN": binaryen, "GOWORK": "/unrelated/go.work"}
        output = root / "output"
        # Pre-existing success must not mask a failing compiler invocation.
        stale = output / "raw" / "TinyGo" / "base64.wasm"
        stale.parent.mkdir(parents=True)
        stale.write_bytes(b"\0asmstale")
        (output / "results.json").write_text('{"stale": true}')
        (output / "summary.md").write_text('stale success')
        completed = subprocess.run(["bash", str(script / "run.sh"), str(output)], env=env,
                                   capture_output=True, text=True)
        return completed, output

    def test_execution_suites_are_disjoint(self):
        for suite, expected in (("standard", "second"), ("tsgo", "tsgo")):
            with self.subTest(suite=suite), tempfile.TemporaryDirectory() as temp:
                completed, output = self.run_fixture(Path(temp), js=True, two_apps=True, suite=suite)
                self.assertEqual(completed.returncode, 0, completed.stderr)
                document = json.loads((output / "results.json").read_text())
                self.assertEqual([row["id"] for row in document["benchmarks"]], [expected])
                self.assertEqual(document["suite"], suite)

    def test_js_suite_matches_wasi_sources_plus_tsgo(self):
        rows = report.read_manifest(HERE / "apps.tsv")
        wasi = {row["id"]: row for row in rows if row["goos"] == "wasip1"}
        js = {row["id"]: row for row in rows if row["goos"] == "js"}
        self.assertEqual(set(js), {name + "-js" for name in wasi} | {"tsgo"})
        for name, row in wasi.items():
            self.assertEqual(js[name + "-js"], dict(row, id=name + "-js", goos="js"))
        self.assertEqual(js["tsgo"]["source"], "tsc/cmd/tsc")

    def test_js_glue_target_and_uniform_build_results(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            completed, output = self.run_fixture(root, js=True)
            self.assertEqual(completed.returncode, 0, completed.stderr)
            document = json.loads((output / "results.json").read_text())
            app = document["benchmarks"][0]
            self.assertEqual(app["target"], {"goos": "js", "goarch": "wasm"})
            self.assertEqual(app["values"]["LLGoNoLTO"], 24)
            self.assertNotIn("validation", app)
            calls = [json.loads(line) for line in (root / "calls.jsonl").read_text().splitlines()]
            for call in calls:
                self.assertEqual(call["goos"], "js")
                self.assertIn("-p=1", call["goflags"])
                if call["config"].startswith("LLGo"):
                    self.assertIn("-Oz", call["args"])
                    self.assertTrue(call["args"][call["args"].index("-o")+1].endswith(".mjs"))

    def test_timeout_is_not_failure_or_zero_and_later_cells_run(self):
        with tempfile.TemporaryDirectory() as temp:
            completed, output = self.run_fixture(Path(temp), failure="LLGoNoLTO", timeout=True)
            self.assertNotEqual(completed.returncode, 0)
            app = json.loads((output / "results.json").read_text())["benchmarks"][0]
            self.assertEqual(app["builds"]["LLGoNoLTO"]["status"], "timeout")
            self.assertIn("Compiler exit status: 124", (output / "logs" / "base64.LLGoNoLTO.log").read_text())
            self.assertIsNone(app["values"]["LLGoNoLTO"])
            self.assertEqual(app["builds"]["LLGoFullLTOGlobalDCE"]["status"], "success")
            self.assertIn("timeout", (output / "summary.md").read_text())

    def test_six_builds_and_recorded_flags_match_actual_argv(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            completed, output = self.run_fixture(root, binaryen="132 (version_132)")
            self.assertEqual(completed.returncode, 0, completed.stderr)
            document = json.loads((output / "results.json").read_text())
            calls = [json.loads(line) for line in (root / "calls.jsonl").read_text().splitlines()]
            self.assertEqual([call["config"] for call in calls], report.CONFIGS)
            for call in calls:
                self.assertEqual(call["args"][:-3], document["protocol"][call["config"]])
                self.assertEqual(call["gowork"], "off")
                self.assertEqual(call["ccflags"], document["protocol"]["environment"][call["config"]]["CCFLAGS"])
                self.assertEqual(call["ldflags"], document["protocol"]["environment"][call["config"]]["LDFLAGS"])
                expected = "wasm-opt" if call["config"] == "TinyGo" else "llgo-wasm-opt"
                self.assertEqual(Path(call["wasmopt"]).name, expected)

    def test_optional_tinygo_failure_or_invalid_header_keeps_llgo(self):
        for invalid in (False, True):
            with self.subTest(invalid=invalid), tempfile.TemporaryDirectory() as temp:
                completed, output = self.run_fixture(Path(temp), "optional", "TinyGo", invalid)
                self.assertEqual(completed.returncode, 0, completed.stderr)
                row = json.loads((output / "results.json").read_text())["benchmarks"][0]
                self.assertIsNone(row["values"]["TinyGo"])
                self.assertEqual(row["builds"]["TinyGo"]["status"], "failed")
                self.assertTrue(all(row["values"][mode] > 0 for mode in report.LLGO_CONFIGS))
                self.assertFalse((output / "raw" / "TinyGo" / "base64.wasm").exists())
                self.assertIn("compiler failure evidence", (output / "logs" / "base64.TinyGo.log").read_text())

    def test_required_failure_or_invalid_header_fails_ci(self):
        for config in report.CONFIGS:
            for invalid in (False, True):
                with self.subTest(config=config, invalid=invalid), tempfile.TemporaryDirectory() as temp:
                    root = Path(temp)
                    completed, output = self.run_fixture(root, "required", config, invalid, two_apps=True)
                    self.assertNotEqual(completed.returncode, 0)
                    document = json.loads((output / "results.json").read_text())
                    self.assertEqual(len(document["benchmarks"]), 2)
                    self.assertEqual(document["benchmarks"][0]["builds"][config]["status"], "failed")
                    self.assertTrue(all(value > 0 for value in document["benchmarks"][1]["values"].values()))
                    calls = (root / "calls.jsonl").read_text().splitlines()
                    self.assertEqual(len(calls), 2 * len(report.CONFIGS))
                    self.assertFalse((output / "raw" / config / "base64.wasm").exists())
                    self.assertIn(f"{config}\tnull\tfailed", (output / "sizes.tsv").read_text())

    def test_shadowed_binaryen_is_rejected_before_building(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            completed, output = self.run_fixture(root, binaryen="116")
            self.assertNotEqual(completed.returncode, 0)
            self.assertIn("expected TinyGo Binaryen 132", completed.stderr)
            self.assertFalse((root / "calls.jsonl").exists())
            self.assertFalse((output / "results.json").exists())

    def test_invalid_policy_is_rejected_before_building(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            completed, _ = self.run_fixture(root, "typo")
            self.assertNotEqual(completed.returncode, 0)
            self.assertFalse((root / "calls.jsonl").exists())


class ArchiveCompatibilityTest(unittest.TestCase):
    def test_publish_partial_results_with_either_family_unavailable(self):
        for mode in ("both", "native", "wasm"):
            with self.subTest(mode=mode), tempfile.TemporaryDirectory() as temp:
                root = Path(temp)
                remote, pages, native, wasm = [root / name for name in ("remote.git", "pages", "native", "wasm")]
                subprocess.run(["git", "init", "--bare", str(remote)], check=True, capture_output=True)
                subprocess.run(["git", "clone", str(remote), str(pages)], check=True, capture_output=True)
                native.mkdir()
                native_doc = {"run": {"id": "partial-run"}, "benchmarks": [
                    {"name": "Toml", "values": {"Go": None, "LLGoNoLTO": 123}}]}
                (native / "results.json").write_text(json.dumps(native_doc))
                for name in ("summary.md", "total-bytes.tsv", "timing-summary.md", "build-times.tsv", "download-timings.log", "build.log"):
                    (native / name).write_text("partial result\n")
                (native / "raw").mkdir()
                (native / "raw/current.benchsize").write_text("BenchmarkToml 1 123 total-bytes\n")
                wasm.mkdir()
                app = report.read_manifest(HERE / "apps.tsv")[0]
                values = results(100, 50, 20)
                values["LLGoDeadcodeDrop"] = {"bytes": None, "status": "failed"}
                with mock.patch.dict(os.environ, {}, clear=True):
                    document = report.build_document([app], {app["id"]: values})
                document["run"]["id"] = "partial-run"
                (wasm / "results.json").write_text(json.dumps(document))
                report.write_summary(document, wasm / "summary.md")
                (wasm / "sizes.tsv").write_text("app\tconfig\tbytes\tstatus\nbase64\tLLGoDeadcodeDrop\tnull\tfailed\n")
                (wasm / "logs").mkdir()
                (wasm / "logs/base64.LLGoDeadcodeDrop.log").write_text("compiler failure evidence\n")
                command = ["bash", str(HERE.parent / "llgo-size/publish.sh"),
                           str(native) if mode != "wasm" else "", str(pages),
                           str(HERE.parent / "llgo-size/site"), "", str(wasm) if mode != "native" else ""]
                completed = subprocess.run(command, capture_output=True, text=True)
                self.assertEqual(completed.returncode, 0, completed.stderr)
                if mode != "native":
                    archived = pages / "data/wasm/runs/partial-run"
                    self.assertEqual(json.loads((archived / "results.json").read_text())["benchmarks"][0]["builds"]["LLGoDeadcodeDrop"]["status"], "failed")
                    self.assertIn("failure evidence", (archived / "logs/base64.LLGoDeadcodeDrop.log").read_text())
                if mode != "wasm":
                    archived = pages / "data/runs/partial-run"
                    self.assertIsNone(json.loads((archived / "results.json").read_text())["benchmarks"][0]["values"]["Go"])
                    (native / "raw/current.benchsize").unlink()
                    repeated = subprocess.run(command, capture_output=True, text=True)
                    self.assertEqual(repeated.returncode, 0, repeated.stderr)
                    self.assertFalse((archived / "raw/current.benchsize").exists())
                self.assertTrue((pages / "index.html").exists())

    def test_mixed_schema_history_preserves_old_bytes_and_nullable_results(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            run_dir, pages = root / "run", root / "pages"
            run_dir.mkdir()
            (run_dir / "summary.md").write_text("summary\n")
            (run_dir / "sizes.tsv").write_text("fixture\n")
            legacy = {"schemaVersion": 1, "format": "wasm-file-size",
                      "run": {"llgoCommit": "a" * 40, "llgoMainIndex": 1},
                      "configs": ["Go", "TinyGo", "LLGo"],
                      "benchmarks": [{"id": "base64", "values": {"Go": 100, "TinyGo": 10, "LLGo": 20}}]}
            original = json.dumps(legacy)
            (run_dir / "results.json").write_text(original)
            archive.archive(run_dir, pages)
            app = report.read_manifest(HERE / "apps.tsv")[0]
            app["tinygo"] = "optional"
            current = report.build_document([app], {app["id"]: results(100, None, 20)})
            current["run"].update({"llgoCommit": "b" * 40, "llgoMainIndex": 2})
            (run_dir / "results.json").write_text(json.dumps(current))
            logs = run_dir / "logs"
            logs.mkdir()
            (logs / "base64.TinyGo.log").write_text("compiler failure evidence")
            archive.archive(run_dir, pages)
            data = pages / "data" / "wasm"
            self.assertEqual((data / "runs" / ("a" * 40) / "results.json").read_text(), original)
            archived = json.loads((data / "runs" / ("b" * 40) / "results.json").read_text())
            self.assertIsNone(archived["benchmarks"][0]["values"]["TinyGo"])
            self.assertEqual((data / "runs" / ("b" * 40) / "logs" / "base64.TinyGo.log").read_text(), "compiler failure evidence")
            index = json.loads((data / "index.json").read_text())
            self.assertEqual([run["schemaVersion"] for run in index["runs"]], [2, 1])
            self.assertEqual(index["runs"][0]["configs"], report.CONFIGS)

    def test_page_only_publisher_includes_both_views(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            remote, pages = root / "remote.git", root / "pages"
            subprocess.run(["git", "init", "--bare", str(remote)], check=True, capture_output=True)
            subprocess.run(["git", "clone", str(remote), str(pages)], check=True, capture_output=True)
            completed = subprocess.run(["bash", str(HERE.parent / "llgo-size" / "publish-site.sh"),
                                        str(pages), str(HERE.parent / "llgo-size" / "site")],
                                       capture_output=True, text=True)
            self.assertEqual(completed.returncode, 0, completed.stderr)
            files = subprocess.check_output(["git", "--git-dir", str(remote), "ls-tree", "--name-only", "pages"], text=True)
            self.assertIn("wasm-tinygo.html", files)
            self.assertIn("js-wasm.html", files)
            self.assertIn("js-wasm-tinygo.html", files)
            self.assertIn("index.html", files)
            self.assertEqual((pages / "wasm-tinygo.html").read_bytes(), (HERE.parent / "llgo-size" / "site" / "wasm-tinygo.html").read_bytes())


if __name__ == "__main__":
    unittest.main()
