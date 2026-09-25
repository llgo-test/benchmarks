#!/usr/bin/env python3
"""Bound one build/check and retain its real exit status, including timeouts."""
import json
import math
import os
from pathlib import Path
import signal
import subprocess
import sys
import time


def run(command, seconds, log):
    if not math.isfinite(seconds) or seconds <= 0:
        raise ValueError("timeout must be positive and finite")
    start = time.monotonic()
    status = "failed"
    with Path(log).open("w") as stream:
        stream.write("command: " + json.dumps(command) + "\n")
        stream.flush()
        try:
            process = subprocess.Popen(command, stdout=stream, stderr=subprocess.STDOUT,
                                       start_new_session=True)
        except OSError as error:
            stream.write(str(error) + "\n")
            code = 127
        else:
            try:
                code = process.wait(timeout=seconds)
                status = "success" if code == 0 else "failed"
            except subprocess.TimeoutExpired:
                status, code = "timeout", 124
                stream.write(f"Timed out after {seconds:g}s; terminating process group\n")
                try:
                    os.killpg(process.pid, signal.SIGTERM)
                    process.wait(timeout=2)
                except (ProcessLookupError, subprocess.TimeoutExpired):
                    pass
                finally:
                    # A compiler can exit while leaving its linker running.
                    try:
                        os.killpg(process.pid, signal.SIGKILL)
                    except ProcessLookupError:
                        pass
                    process.wait()
        stream.write(f"Result: {status}; exit code: {code}\n")
    return {"status": status, "exitCode": code, "seconds": time.monotonic() - start}


if __name__ == "__main__":
    seconds, log, result, *command = sys.argv[1:]
    data = run(command, float(seconds), log)
    Path(result).write_text(json.dumps(data, indent=2) + "\n")
    raise SystemExit(124 if data["status"] == "timeout" else 0 if data["status"] == "success" else 1)
