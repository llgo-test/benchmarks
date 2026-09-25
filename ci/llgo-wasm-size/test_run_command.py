from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from run_command import run


class BoundedCommandTest(unittest.TestCase):
    def test_timeout_kills_linker_even_when_parent_exits_on_term(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            pidfile = root / "child.pid"
            child = "import signal,time; signal.signal(signal.SIGTERM, signal.SIG_IGN); time.sleep(60)"
            parent = (
                "import subprocess,sys,time,pathlib; "
                f"p=subprocess.Popen([sys.executable,'-c',{child!r}]); "
                f"pathlib.Path({str(pidfile)!r}).write_text(str(p.pid)); "
                "time.sleep(60)"
            )
            result = run([sys.executable, "-c", parent], 1, root / "build.log")
            self.assertEqual(result["status"], "timeout")
            self.assertEqual(result["exitCode"], 124)
            pid = int(pidfile.read_text())
            state = subprocess.run(["ps", "-o", "stat=", "-p", str(pid)],
                                   capture_output=True, text=True).stdout.strip()
            self.assertTrue(not state or state.startswith("Z"), state)

    def test_nonzero_exit_is_not_a_timeout(self):
        with tempfile.TemporaryDirectory() as temp:
            result = run([sys.executable, "-c", "raise SystemExit(23)"], 5, Path(temp) / "build.log")
            self.assertEqual(result["status"], "failed")
            self.assertEqual(result["exitCode"], 23)


if __name__ == "__main__":
    unittest.main()
