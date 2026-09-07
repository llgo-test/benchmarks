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

    def test_reject_missing_or_failed_required_configuration(self):
        app = self.manifest[1]
        for mode in report.CONFIGS:
            for missing in (False, True):
                with self.subTest(mode=mode, missing=missing):
                    values = results(100, 50, 20)
                    if missing:
                        del values[mode]
                    else:
                        values[mode] = {"bytes": None, "status": "failed"}
                    with self.assertRaises(ValueError):
                        report.build_document([app], {app["id"]: values})

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
    def run_fixture(self, root, policy="required", failure="", invalid=False, binaryen="132"):
        script = root / "script"
        script.mkdir()
        for name in ("run.sh", "report.py"):
            shutil.copy2(HERE / name, script / name)
        app = report.read_manifest(HERE / "apps.tsv")[0]
        app["tinygo"] = policy
        (script / "apps" / app["source"]).mkdir(parents=True)
        with (script / "apps.tsv").open("w") as stream:
            writer = csv.DictWriter(stream, fieldnames=app, delimiter="\t")
            writer.writeheader()
            writer.writerow(app)
        bin_dir = root / "bin"
        bin_dir.mkdir()
        # The fake compilers exercise shell orchestration, output verification,
        # failure policy, and argv boundaries without requiring toolchains in PR CI.
        program = '''#!PYTHON
import json, os, sys
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
    f.write(json.dumps({"config": config, "args": sys.argv[1:], "wasmopt": os.environ.get("WASMOPT"), "gowork": os.environ.get("GOWORK"), "ccflags": os.environ.get("CCFLAGS"), "ldflags": os.environ.get("LDFLAGS")}) + "\\n")
output = Path(sys.argv[sys.argv.index("-o")+1])
if config == os.environ["FAIL_CONFIG"]:
    output.write_bytes(b"invalid")
    print("compiler failure evidence")
    raise SystemExit(0 if os.environ["INVALID_WASM"] == "1" else 9)
output.write_bytes(b"\\0asm" + b"x" * 20)
'''.replace("PYTHON", sys.executable)
        for name in ("go", "tinygo", "llgo", "clang++", "wasm-ld", "wasm-opt", "llgo-wasm-opt"):
            path = bin_dir / name
            path.write_text(program)
            path.chmod(0o755)
        env = {**os.environ, "PATH": str(bin_dir) + os.pathsep + os.environ["PATH"],
               "LLGO_BIN": str(bin_dir / "llgo"), "GO_VERSION": "1.26.2",
               "TINYGO_VERSION": "0.41.1", "BINARYEN_VERSION": "132", "LLVM_VERSION": "22",
               "LLGO_WASMOPT": str(bin_dir / "llgo-wasm-opt"),
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
                    completed, output = self.run_fixture(Path(temp), "required", config, invalid)
                    self.assertNotEqual(completed.returncode, 0)
                    self.assertFalse((output / "results.json").exists())
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
            self.assertIn("index.html", files)
            self.assertEqual((pages / "wasm-tinygo.html").read_bytes(), (HERE.parent / "llgo-size" / "site" / "wasm-tinygo.html").read_bytes())


if __name__ == "__main__":
    unittest.main()
