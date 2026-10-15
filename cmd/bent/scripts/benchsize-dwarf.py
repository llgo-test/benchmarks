#!/usr/bin/env python3
"""Measure a Linux ELF with DWARF and a strip-debug copy, without rebuilding."""
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile


def sections(binary):
    output = subprocess.check_output(
        [os.environ.get("BENT_READELF", "llvm-readelf"), "--sections", "--wide", str(binary)],
        text=True,
    )
    # Both GNU readelf and llvm-readelf print: [index] name type addr offset size ...
    pattern = r"^\s*\[\s*\d+\]\s+(\S+)\s+\S+\s+[0-9a-fA-F]+\s+[0-9a-fA-F]+\s+([0-9a-fA-F]+)\s"
    result = {match[1]: int(match[2], 16) for line in output.splitlines()
              if (match := re.match(pattern, line))}
    if not result:
        raise ValueError("cannot read ELF section table")
    return result


def is_debug(name):
    return name.startswith((".debug_", ".zdebug_"))


def measure(binary):
    with binary.open("rb") as source:
        if source.read(4) != b"\x7fELF":
            raise ValueError("DWARF size pairs require a Linux ELF binary")
    original = sections(binary)
    if not (original.get(".debug_info", 0) or original.get(".zdebug_info", 0)):
        raise ValueError("input has no DWARF .debug_info; refusing an unmatched comparison")
    with tempfile.TemporaryDirectory(prefix="benchsize-dwarf-") as temp:
        stripped = Path(temp) / "without-dwarf"
        shutil.copy2(binary, stripped)
        subprocess.run([os.environ.get("BENT_STRIP", "llvm-strip"), "--strip-debug", str(stripped)], check=True)
        remaining = sections(stripped)
        if any(is_debug(name) for name in remaining):
            raise ValueError("strip left DWARF sections in the output")
        stripped_size = stripped.stat().st_size
    return {
        "total-bytes": binary.stat().st_size,
        "with-dwarf-bytes": binary.stat().st_size,
        "without-dwarf-bytes": stripped_size,
        "text-bytes": original.get(".text", 0),
        "data-bytes": original.get(".data", 0),
        "rodata-bytes": original.get(".rodata", 0),
        "pclntab-bytes": original.get(".gopclntab", 0),
        "debug-bytes": sum(size for name, size in original.items() if is_debug(name)),
    }


def main():
    try:
        metrics = measure(Path(sys.argv[1]))
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        print(f"DWARF size measurement failed: {error}", file=sys.stderr)
        return 1
    # Emit nothing until both measurements and section checks succeed.
    print("goos: linux")
    print("goarch:", os.environ.get("GOARCH", ""))
    print("pkg:")
    for unit, value in metrics.items():
        print(f"Unit {unit} assume=exact")
        print(f"Benchmark{sys.argv[2]} 1 {value} {unit}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
