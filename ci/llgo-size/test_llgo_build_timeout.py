import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import unittest


WRAPPER = Path(__file__).parent / "bin" / "llgo-build-timeout"


class LLGoBuildTimeoutTest(unittest.TestCase):
    def run_wrapper(self, compiler, *args, **environment):
        env = os.environ.copy()
        env.update(
            LLGO_REAL_BIN=str(compiler),
            LLGO_BUILD_TIMEOUT_SECONDS="2",
            LLGO_BUILD_KILL_GRACE_SECONDS="0.2",
        )
        env.update(environment)
        return subprocess.run(
            [sys.executable, str(WRAPPER), *args],
            env=env,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_preserves_arguments_and_exit_status(self):
        result = self.run_wrapper(
            sys.executable,
            "-c",
            "import sys; print(sys.argv[1]); raise SystemExit(7)",
            "argument with spaces",
        )
        self.assertEqual(result.returncode, 7)
        self.assertEqual(result.stdout.strip(), "argument with spaces")

    def test_times_out_and_kills_the_process_group(self):
        with tempfile.TemporaryDirectory() as directory:
            marker = Path(directory) / "child-finished"
            program = (
                "import subprocess, sys, time; "
                "subprocess.Popen([sys.executable, '-c', "
                "'import pathlib, sys, time; time.sleep(1); pathlib.Path(sys.argv[1]).touch()', "
                "sys.argv[1]]); "
                "time.sleep(10)"
            )
            result = self.run_wrapper(
                sys.executable,
                "-c",
                program,
                str(marker),
                LLGO_BUILD_TIMEOUT_SECONDS="0.2",
                BENT_BENCH="k8s_workqueue",
                BENT_CONFIG="LLGoDeadcodeDrop",
            )
            self.assertEqual(result.returncode, 124)
            self.assertIn("benchmark=k8s_workqueue", result.stderr)
            self.assertIn("configuration=LLGoDeadcodeDrop", result.stderr)
            time.sleep(1.1)
            self.assertFalse(marker.exists(), "compiler child survived the timeout")

    def test_rejects_missing_compiler(self):
        env = os.environ.copy()
        env.pop("LLGO_REAL_BIN", None)
        result = subprocess.run(
            [sys.executable, str(WRAPPER)],
            env=env,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 2)
        self.assertIn("requires LLGO_REAL_BIN", result.stderr)


if __name__ == "__main__":
    unittest.main()
