import csv
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest import mock

import prepare_sources
import report


class ExternalSourcesTest(unittest.TestCase):
    def repo(self, root):
        root.mkdir()
        subprocess.run(['git', 'init', '-q', str(root)], check=True)
        (root / 'cmd').mkdir()
        (root / 'cmd/main.go').write_text('package main\nfunc main() {}\n')
        (root / 'go.mod').write_text('module example.com/original\n\ngo 1.27.0\n')
        subprocess.run(['git', '-C', str(root), 'add', '.'], check=True)
        subprocess.run(['git', '-C', str(root), '-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.com', 'commit', '-qm', 'original'], check=True)
        return prepare_sources.git(root, 'rev-parse', 'HEAD')

    def test_fetch_exact_commit_preserve_module_and_reject_dirty_cache(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            upstream = (root / 'upstream').resolve()
            revision = self.repo(upstream)
            # Move upstream HEAD; a branch checkout would silently use the wrong code.
            (upstream / 'cmd/main.go').write_text('package main\nfunc main() { panic("new revision") }\n')
            subprocess.run(['git', '-C', str(upstream), '-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.com', 'commit', '-qam', 'later'], check=True)
            result = prepare_sources.checkout(upstream.as_uri(), revision, root / 'cache')
            self.assertEqual((result / 'cmd/main.go').read_text(), 'package main\nfunc main() {}\n')
            self.assertEqual((result / 'go.mod').read_bytes(), (upstream / 'go.mod').read_bytes())
            self.assertEqual(result, prepare_sources.checkout(upstream.as_uri(), revision, root / 'cache'))
            (result / 'go.mod').write_text('module rewritten\n')
            with self.assertRaisesRegex(ValueError, 'modified'):
                prepare_sources.checkout(upstream.as_uri(), revision, root / 'cache')
            with self.assertRaises(subprocess.CalledProcessError):
                prepare_sources.checkout(upstream.as_uri(), '0' * 40, root / 'cache')

    def test_original_entry_toolchain_and_published_identity(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            upstream = (root / 'upstream').resolve()
            revision = self.repo(upstream)
            app = dict(id='example', command='original', source='cmd', provenance='example/original', kind='command', description='Original application', tinygo='optional', repository='https://github.com/example/original.git', revision=revision, go_version='1.27.0')
            manifest = root / 'apps.tsv'
            with manifest.open('w') as stream:
                writer = csv.DictWriter(stream, fieldnames=app, delimiter='\t')
                writer.writeheader(); writer.writerow(app)
            with mock.patch.object(prepare_sources, 'checkout', return_value=upstream), mock.patch.dict(os.environ, {'GO_VERSION': '1.26.2'}):
                plan = prepare_sources.prepare(manifest, root / 'local', root / 'cache')
                self.assertEqual(plan[0][2:], [str(upstream), './cmd', 'optional', 'go1.27.0', revision])
                sizes = {config: {'bytes': None if config == 'TinyGo' else 100, 'status': 'failed' if config == 'TinyGo' else 'success'} for config in report.CONFIGS}
                document = report.build_document([app], {'example': sizes})
                local = {**app, 'id': 'local', 'go_version': 'default', 'repository': '-', 'revision': '-'}
                mixed = report.build_document([app, local], {'example': sizes, 'local': sizes})
                self.assertFalse(mixed['protocol']['sameGoToolchain'])
                self.assertTrue(mixed['protocol']['sameGoToolchainPerApplication'])
            row = document['benchmarks'][0]
            self.assertEqual(row['repository'], app['repository'])
            self.assertEqual(row['revision'], revision)
            self.assertEqual(row['goVersion'], '1.27.0')
            self.assertIsNone(row['values']['TinyGo'])
            # A symlink must not redirect the selected entry outside the source tree.
            (upstream / 'escape').symlink_to(root, target_is_directory=True)
            app['source'] = 'escape'
            with manifest.open('w') as stream:
                writer = csv.DictWriter(stream, fieldnames=app, delimiter='\t')
                writer.writeheader(); writer.writerow(app)
            with mock.patch.object(prepare_sources, 'checkout', return_value=upstream), self.assertRaisesRegex(ValueError, 'invalid application entry'):
                prepare_sources.prepare(manifest, root / 'local', root / 'cache')

    def test_manifest_requires_immutable_ref_and_contained_entry(self):
        base = report.read_manifest(Path(__file__).with_name('apps.tsv'))[-1]
        for fields in [dict(repository='https://github.com/example/repo.git', revision='main'), dict(source='../outside'), dict(go_version='auto')]:
            with self.subTest(fields=fields), tempfile.TemporaryDirectory() as temp:
                app = {**base, **fields}
                path = Path(temp) / 'apps.tsv'
                with path.open('w') as stream:
                    writer = csv.DictWriter(stream, fieldnames=app, delimiter='\t')
                    writer.writeheader(); writer.writerow(app)
                with self.assertRaises(ValueError):
                    report.read_manifest(path)


if __name__ == '__main__':
    unittest.main()
