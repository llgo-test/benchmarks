import json
import os
from pathlib import Path
import subprocess
import tempfile
import textwrap
import unittest


HERE = Path(__file__).resolve().parent
CONFIGS = ["Go", "LLGoNoLTO", "LLGoDeadcodeDrop", "LLGoFullLTONoGlobalDCE",
           "LLGoFullLTOGlobalDCE", "LLGoFullLTOGlobalDCEPlugin"]
CASES = ["Toml", "Aws_restjson", "Dustin_humanize", "K8s_workqueue", "Uber_zap",
         "Gorm_schema", "Etcdctl", "XGo", "IXGo"]


class NativeReportTest(unittest.TestCase):
    def test_workflow_restores_failure_after_publishing(self):
        workflow = (HERE.parent.parent / ".github/workflows/llgo-binary-size-suite.yml").read_text()
        marker = "      - name: Report benchmark failures after preserving results"
        self.assertLess(workflow.index("        id: publish"), workflow.index(marker))
        step = workflow.split(marker, 1)[1].split("  deploy-pages:", 1)[0]
        script = textwrap.dedent(step.split("        run: |\n", 1)[1])
        for outcome in ("success", "failure"):
            with self.subTest(outcome=outcome):
                # continue-on-error changes conclusion to success; the final
                # gate must still surface the original build failure.
                steps = {"wasm": {"outcome": outcome, "conclusion": "success"},
                         "bent": {"outcome": "success"}, "publish": {"outcome": "success"}}
                result = subprocess.run(["bash", "-c", script], capture_output=True, text=True,
                                        env={**os.environ, "STEP_RESULTS": json.dumps(steps)})
                self.assertEqual(result.returncode, 1 if outcome == "failure" else 0, result.stderr)
        deploy = workflow.split("  deploy-pages:", 1)[1].split("    steps:", 1)[0]
        self.assertIn("needs.binary-size.outputs.published == 'true'", deploy)
        self.assertNotIn("needs.binary-size.result == 'success'", deploy)

    def test_partial_results_preserve_all_cases_and_other_compilers(self):
        for missing in (set(), {("Toml", "LLGoDeadcodeDrop")},
                        {(case, "Go") for case in CASES},
                        {(case, config) for case in CASES for config in CONFIGS}):
            with self.subTest(missing=len(missing)), tempfile.TemporaryDirectory() as temp:
                root = Path(temp)
                bench = root / "bench"
                bench.mkdir()
                for config in CONFIGS:
                    (bench / f"test.{config}.benchsize").write_text("".join(
                        f"Benchmark{case} 1 123 total-bytes\n" for case in CASES if (case, config) not in missing))
                (root / "build.log").write_text("compiler failure evidence\n")
                result = subprocess.run(["bash", str(HERE / "report.sh"), str(root)],
                                        capture_output=True, text=True)
                self.assertEqual(result.returncode, 1 if missing else 0, result.stderr)
                rows = {row["name"]: row for row in json.loads((root / "results/results.json").read_text())["benchmarks"]}
                self.assertEqual(set(rows), set(CASES))
                for case in CASES:
                    for config in CONFIGS:
                        self.assertEqual(rows[case]["values"][config], None if (case, config) in missing else 123)
                        self.assertEqual(rows[case]["builds"][config]["status"], "missing" if (case, config) in missing else "success")
                self.assertEqual((root / "results/build.log").read_text(), "compiler failure evidence\n")


if __name__ == "__main__":
    unittest.main()
