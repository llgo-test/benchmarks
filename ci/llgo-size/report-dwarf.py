#!/usr/bin/env python3
"""Add paired DWARF measurements to the native report, retaining missing cells."""
import csv
import json
from pathlib import Path
import sys


def report(result_dir):
    path = result_dir / "results.json"
    document = json.loads(path.read_text())
    configs = document["configs"]
    metrics = {}
    for config in configs:
        for raw in sorted((result_dir / "raw").glob(f"*.{config}.benchsize")):
            for line in raw.read_text().splitlines():
                fields = line.split()
                if len(fields) == 4 and fields[0].startswith("Benchmark") and fields[3] in ("with-dwarf-bytes", "without-dwarf-bytes"):
                    value = int(fields[2])
                    if value > 0:
                        metrics.setdefault((fields[0][9:], config, fields[3]), value)
    missing = 0
    for row in document["benchmarks"]:
        row["sizes"] = {}
        for variant, metric in (("withDwarf", "with-dwarf-bytes"), ("withoutDwarf", "without-dwarf-bytes")):
            row["sizes"][variant] = {config: metrics.get((row["name"], config, metric)) for config in configs}
            missing += sum(value is None for value in row["sizes"][variant].values())
    document["schemaVersion"] = 2
    document["sizeProtocol"] = {
        "buildsPerConfiguration": 1,
        "ldflags": "-s=false -w=false",
        "withDwarf": "ELF with nonempty .debug_info or .zdebug_info",
        "withoutDwarf": "temporary copy with no .debug_* or .zdebug_* sections",
        "stripCommand": ["llvm-strip", "--strip-debug"],
        "symbolTable": "preserved",
    }
    (result_dir / "summary.md").write_text(
        "# LLGo binary-size CI\n\n"
        "Each configuration is built once with `-ldflags='-s=false -w=false'`. "
        "The second size comes from `llvm-strip --strip-debug` on a copy. "
        "DWARF presence/absence is checked; ordinary symbol tables are preserved. "
        "All values are complete ELF file sizes in bytes.\n"
    )
    for variant, filename, title in (
        ("withDwarf", "with-dwarf-bytes.tsv", "With DWARF (verified)"),
        ("withoutDwarf", "without-dwarf-bytes.tsv", "Without DWARF (strip --strip-debug)"),
    ):
        document["native"][variant + "Tsv"] = filename
        with (result_dir / filename).open("w", newline="") as output:
            writer = csv.writer(output, delimiter="\t", lineterminator="\n")
            writer.writerow(["benchmark", *configs])
            for row in document["benchmarks"]:
                writer.writerow([row["name"], *(row["sizes"][variant][config] or "null" for config in configs)])
        with (result_dir / "summary.md").open("a") as output:
            output.write(f"\n## {title}\n\n")
            output.write("| Benchmark | " + " | ".join(configs) + " |\n")
            output.write("| --- | " + " | ".join("---:" for _ in configs) + " |\n")
            for row in document["benchmarks"]:
                output.write("| " + row["name"] + " | " + " | ".join(str(row["sizes"][variant][config] or "—") for config in configs) + " |\n")
    if missing:
        with (result_dir / "summary.md").open("a") as output:
            output.write(f"\n{missing} paired size measurements are missing; excluded from DWARF comparisons.\n")
        print(f"missing {missing} paired DWARF measurements", file=sys.stderr)
    path.write_text(json.dumps(document, indent=2) + "\n")
    return bool(missing)


if __name__ == "__main__":
    sys.exit(report(Path(sys.argv[1])))
