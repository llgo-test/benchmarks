#!/usr/bin/env python3
"""Run the upstream JS host runner; keep startup separate from TS compilation."""
import json
import os
from pathlib import Path
import subprocess
import sys

from run_command import run


def main():
    config, binary, prefix = sys.argv[1:]
    log = prefix + ".version.log"
    functional = {"status": "not_run", "reason": "Actual TypeScript compilation in the JS host has not been validated; --version tests startup only"}
    if config == "TinyGo":
        startup = {"status": "not_run", "reason": "No TinyGo JS startup adapter configured"}
    else:
        node = os.environ.get("NODE_BIN", "node")
        seconds = float(os.environ.get("WASM_CHECK_TIMEOUT_SECONDS", "120"))
        try:
            if config == "Go":
                goroot = subprocess.check_output(["go", "env", "GOROOT"], text=True,
                                                 stderr=subprocess.STDOUT, timeout=seconds).strip()
                command = [node, str(Path(goroot) / "lib/wasm/wasm_exec_node.js"), binary, "--version"]
            else:
                command = [node, str(Path(os.environ["LLGO_ROOT"]) / "targets/emscripten-runner.mjs"),
                           "--browser-only", binary, "--version"]
        except subprocess.TimeoutExpired as error:
            startup = {"status": "timeout", "exitCode": 124, "reason": str(error)}
            Path(log).write_text(str(error) + "\n")
        except (OSError, subprocess.CalledProcessError, KeyError) as error:
            startup = {"status": "failed", "reason": str(error)}
            Path(log).write_text(str(error) + "\n" + str(getattr(error, "output", "")))
        else:
            startup = run(command, seconds, log)
            if startup["status"] == "success" and not any(line.startswith("Version ") for line in Path(log).read_text().splitlines()):
                startup["status"] = "failed"
                startup["reason"] = "tsc did not print its version"
        startup["log"] = "logs/" + Path(log).name
    Path(prefix + ".checks.json").write_text(json.dumps({"startup": startup, "functional": functional}, indent=2) + "\n")
    return 0 if startup["status"] in {"success", "not_run"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
