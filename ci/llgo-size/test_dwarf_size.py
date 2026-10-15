import hashlib
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "cmd/bent/scripts/benchsize-dwarf.py"


class DwarfSizeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.temp.cleanup)
        cls.root = Path(cls.temp.name)
        cls.binary = cls.root / "hello"
        source = cls.root / "main.go"
        source.write_text('package main\nfunc main() { println("hello") }\n')
        cls.env = {**os.environ, "GOOS": "linux", "GOARCH": "amd64", "CGO_ENABLED": "0",
                   "GOFLAGS": "", "GOWORK": "off", "BENT_SIZE_DWARF_PAIRS": "1",
                   "BENT_READELF": shutil.which("llvm-readelf") or "readelf",
                   "BENT_STRIP": shutil.which("llvm-strip") or "strip"}
        subprocess.run(["go", "build", "-ldflags=-s=false -w=false", "-o", str(cls.binary), str(source)],
                       env=cls.env, check=True, capture_output=True)

    def run_measurement(self, binary=None, **env):
        return subprocess.run(["bash", str(SCRIPT.with_name("benchsize")), str(binary or self.binary), "Hello"],
                              env={**self.env, **env}, text=True, capture_output=True)

    def test_real_elf_pair_preserves_original_code_and_symbols(self):
        before = hashlib.sha256(self.binary.read_bytes()).digest()
        capture = self.root / "stripped"
        wrapper = self.root / "capture-strip"
        wrapper.write_text(f'#!{sys.executable}\nimport os,shutil,subprocess,sys\n'
                           'subprocess.run([os.environ["REAL_STRIP"], *sys.argv[1:]], check=True)\n'
                           'shutil.copy2(sys.argv[-1], os.environ["CAPTURE"])\n')
        wrapper.chmod(0o755)
        result = self.run_measurement(BENT_STRIP=str(wrapper), REAL_STRIP=self.env["BENT_STRIP"], CAPTURE=str(capture))
        self.assertEqual(result.returncode, 0, result.stderr)
        metrics = {parts[3]: int(parts[2]) for line in result.stdout.splitlines()
                   if (parts := line.split()) and parts[0] == "BenchmarkHello"}
        self.assertEqual(before, hashlib.sha256(self.binary.read_bytes()).digest())
        self.assertEqual(metrics["total-bytes"], self.binary.stat().st_size)
        self.assertEqual(metrics["with-dwarf-bytes"], self.binary.stat().st_size)
        self.assertEqual(metrics["without-dwarf-bytes"], capture.stat().st_size)
        self.assertLess(metrics["without-dwarf-bytes"], metrics["with-dwarf-bytes"])
        def readelf(*args):
            return subprocess.check_output([self.env["BENT_READELF"], *args], text=True)
        stripped_sections = readelf("-SW", str(capture))
        self.assertNotIn(".debug_", stripped_sections)
        self.assertIn(".symtab", stripped_sections)
        for section in (".text", ".gopclntab", ".rodata"):
            self.assertEqual(readelf("-x", section, str(self.binary)), readelf("-x", section, str(capture)))
        rejected = self.run_measurement(capture)
        self.assertNotEqual(rejected.returncode, 0)
        self.assertIn("no DWARF", rejected.stderr)
        self.assertEqual(rejected.stdout, "")

    def test_strip_failure_and_noop_do_not_emit_measurements(self):
        for command in ("false", "true"):
            with self.subTest(command=command):
                result = self.run_measurement(BENT_STRIP=shutil.which(command))
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(result.stdout, "")

    def test_invalid_input_is_rejected(self):
        source = self.root / "not-elf"
        source.write_text("not an ELF")
        result = self.run_measurement(source)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")


if __name__ == "__main__":
    unittest.main()
